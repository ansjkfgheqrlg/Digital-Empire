"""
Orchestrator (PIANO-KDP-67, CP9) — unico entrypoint end-to-end: Ricerca -> Qualifica ->
Piano -> Scrittura -> Formattazione -> Copertina -> Pacchetto.

Checkpoint su disco dopo ogni fase (sessions/../engine/_run_checkpoints/<run_id>.json):
se il processo crolla a metà (Playwright bloccato, LM Arena non risponde, kill manuale),
un rilancio con lo stesso run_id riprende dalla fase giusta, non da capo.

STATO (2026-08-05): le fasi RESEARCH (CP2), PLANNING/WRITING (CP5), COVER (CP7) non sono
ancora costruite — bloccate su CP1 (sessioni Amazon/LM Arena, richiede login manuale di
Gael, vedi session_manager.py). Qui sono richieste via dependency injection (`deps`): se
non passate, sollevano NotImplementedError esplicito — MAI un placeholder che finge di
funzionare. QUALIFICATION, FORMATTING, PACKAGING usano già i moduli reali costruiti
(story_validator, kdp_formatter, book_output_manager) e sono pienamente operative.

Il meccanismo di checkpoint/resume è testato in fondo con moduli finti per le fasi non
costruite — verifica che RIPRENDE dalla fase giusta senza rieseguire quelle già fatte,
indipendentemente da cosa faranno le fasi vere una volta costruite.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Callable

from . import amazon_research, book_output_manager, config, cover_generator, kdp_formatter, story_validator


class Phase(str, Enum):
    RESEARCH = "research"
    QUALIFICATION = "qualification"
    PLANNING = "planning"
    WRITING = "writing"
    FORMATTING = "formatting"
    COVER = "cover"
    PACKAGING = "packaging"
    DONE = "done"


PHASE_ORDER = [
    Phase.RESEARCH, Phase.QUALIFICATION, Phase.PLANNING, Phase.WRITING,
    Phase.FORMATTING, Phase.COVER, Phase.PACKAGING, Phase.DONE,
]


@dataclass
class RunState:
    run_id: str
    current_phase: Phase
    data: dict = field(default_factory=dict)
    started_at: str = ""
    updated_at: str = ""

    def to_json(self) -> dict:
        d = asdict(self)
        d["current_phase"] = self.current_phase.value
        return d

    @classmethod
    def from_json(cls, d: dict) -> "RunState":
        d = dict(d)
        d["current_phase"] = Phase(d["current_phase"])
        return cls(**d)


class Orchestrator:
    def __init__(self, run_id: str, checkpoints_dir: Path | None = None,
                 output_dir: Path | None = None, deps: dict[str, Callable] | None = None):
        self.run_id = run_id
        self.checkpoints_dir = checkpoints_dir or (config.ENGINE_DIR / "_run_checkpoints")
        self.checkpoint_path = self.checkpoints_dir / f"{run_id}.json"
        self.output_dir = output_dir or (config.LIBRI_DIR / "_wip")
        self.deps = deps or {}

    def _load_or_init_state(self) -> RunState:
        if self.checkpoint_path.exists():
            data = json.loads(self.checkpoint_path.read_text(encoding="utf-8"))
            print(f"[orchestrator] run {self.run_id}: checkpoint trovato, "
                  f"riprendo da fase '{data['current_phase']}'")
            return RunState.from_json(data)
        now = datetime.now().isoformat()
        return RunState(run_id=self.run_id, current_phase=Phase.RESEARCH, started_at=now, updated_at=now)

    def _save_state(self, state: RunState) -> None:
        state.updated_at = datetime.now().isoformat()
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoint_path.write_text(
            json.dumps(state.to_json(), indent=2, ensure_ascii=False), encoding="utf-8"
        )

    # --- fasi -------------------------------------------------------------- #
    def _phase_research(self, state: RunState) -> None:
        fn = self.deps.get("research")
        if fn is None:
            raise NotImplementedError("Fase RESEARCH non ancora costruita (CP2, bloccata su CP1)")
        state.data["research"] = fn()

    def _phase_qualification(self, state: RunState) -> None:
        research = state.data["research"]
        result = story_validator.validate(research["title"], research.get("description", ""))
        if not result.is_go:
            raise RuntimeError(f"NO-GO in qualifica: {result.motivation}")
        state.data["qualification"] = {"is_go": result.is_go, "motivation": result.motivation}

    def _phase_planning(self, state: RunState) -> None:
        fn = self.deps.get("planning")
        if fn is None:
            raise NotImplementedError("Fase PLANNING non ancora costruita (CP5, bloccata su CP4/CP1)")
        state.data["planning"] = fn(state.data["research"])

    def _phase_writing(self, state: RunState) -> None:
        fn = self.deps.get("writing")
        if fn is None:
            raise NotImplementedError("Fase WRITING non ancora costruita (CP5, bloccata su CP4/CP1)")
        state.data["writing"] = fn(state.data["planning"])

    def _phase_formatting(self, state: RunState) -> None:
        manuscript_data = state.data["writing"]
        manuscript = kdp_formatter.BookManuscript(
            title=manuscript_data["title"],
            author=manuscript_data.get("author", "Digital Empire"),
            chapters=[kdp_formatter.Chapter(**c) for c in manuscript_data["chapters"]],
        )
        safe_title = book_output_manager.sanitize_title(manuscript.title)
        docx_path = self.output_dir / f"{safe_title}.docx"
        result = kdp_formatter.build_manuscript_docx(manuscript, docx_path)
        if not result.within_target:
            raise RuntimeError(
                f"Formattazione fuori target: {result} — serve tornare a WRITING per "
                f"altri capitoli, non impacchettare un libro corto (bug ripetuto 2 volte "
                f"nello zip originale, qui bloccato per costruzione)"
            )
        state.data["formatting"] = {
            "docx_path": str(docx_path),
            "word_count": result.word_count,
            "page_count": result.estimated_pages,
        }

    def _phase_cover(self, state: RunState) -> None:
        fn = self.deps.get("cover")
        if fn is None:
            raise NotImplementedError("Fase COVER non ancora costruita (CP7, bloccata su CP4/CP1)")
        # Contesto completo (non solo `writing`): il prompt di copertina reale (CP7) usa
        # genere/personaggi/trama da research+planning, non solo il titolo — altrimenti
        # copertine di libri diversi rischierebbero di somigliarsi troppo.
        state.data["cover"] = fn({
            "writing": state.data["writing"],
            "planning": state.data.get("planning", {}),
            "research": state.data.get("research", {}),
        })

    def _phase_packaging(self, state: RunState) -> None:
        formatting = state.data["formatting"]
        cover = state.data["cover"]
        result = book_output_manager.create_book_package(
            book_title=state.data["writing"]["title"],
            manuscript_path=Path(formatting["docx_path"]),
            cover_path=Path(cover["cover_path"]),
            kdp_metadata_text=state.data.get("planning", {}).get("kdp_metadata", ""),
            word_count=formatting["word_count"],
            page_count=formatting["page_count"],
        )
        state.data["packaging"] = {"folder_path": str(result.folder_path)}

    # --- entrypoint ---------------------------------------------------------#
    def run(self) -> RunState:
        state = self._load_or_init_state()
        handlers = {
            Phase.RESEARCH: self._phase_research,
            Phase.QUALIFICATION: self._phase_qualification,
            Phase.PLANNING: self._phase_planning,
            Phase.WRITING: self._phase_writing,
            Phase.FORMATTING: self._phase_formatting,
            Phase.COVER: self._phase_cover,
            Phase.PACKAGING: self._phase_packaging,
        }
        start_index = PHASE_ORDER.index(state.current_phase)
        for phase in PHASE_ORDER[start_index:]:
            if phase == Phase.DONE:
                break
            print(f"[orchestrator] fase: {phase.value}")
            handlers[phase](state)
            state.current_phase = PHASE_ORDER[PHASE_ORDER.index(phase) + 1]
            self._save_state(state)
        print(f"[orchestrator] run {self.run_id} COMPLETATO: {state.data.get('packaging')}")
        return state


def make_real_research_dep(keyword: str, working_title: str, description: str = "") -> Callable[[], dict]:
    """Dependency REALE per la fase RESEARCH (CP9, sostituisce il modulo finto usato nel
    self-test sotto): esegue una ricerca Amazon vera (CP2, sessione reale salvata in CP1)
    sul keyword indicato e la allega come dato di mercato reale al libro in lavorazione.

    Il titolo/descrizione del libro da SCRIVERE restano quelli forniti da chi lancia il
    run (Gael) — non vengono inventati qui: generare titolo/outline in autonomia richiede
    CP4 (LM Arena, bloccato dal 2026-08-05, vedi PIANO-KDP-67.md §3 punto 5). Finche' CP4
    resta bloccato, un run con questa dependency supera RESEARCH e QUALIFICATION con dati
    reali, poi si ferma onestamente su PLANNING con NotImplementedError — non e' un bug,
    e' lo stato reale del piano."""
    from dataclasses import asdict

    from playwright.sync_api import sync_playwright

    def _research() -> dict:
        with sync_playwright() as p:
            competitors = amazon_research.search_amazon(p, keyword, headless=True)
        print(f"[orchestrator] research reale: {len(competitors)} competitor trovati su "
              f"Amazon per '{keyword}'")
        return {
            "keyword": keyword,
            "title": working_title,
            "description": description,
            "competitors": [asdict(c) for c in competitors],
        }

    return _research


def make_real_planning_dep() -> Callable[[dict], dict]:
    """Dependency REALE per la fase PLANNING (CP9, sostituisce il modulo finto): apre una
    sessione LM Arena propria (CP4, sessione salvata in CP1), genera l'outline reale (CP5)
    e chiude la sessione. Sessione indipendente dalla fase WRITING (non condivisa) perche'
    un resume dopo crash puo' rilanciare WRITING da sola, in un processo diverso, senza
    l'outline della fase precedente in memoria di un browser gia' aperto."""
    from playwright.sync_api import sync_playwright

    from . import book_writer, lmarena_client

    def _planning(research: dict) -> dict:
        with sync_playwright() as p:
            session = lmarena_client.open_session(p, headless=True)
            try:
                outline = book_writer.generate_outline(session.page, research)
            finally:
                session.close()
        print(f"[orchestrator] planning reale: outline '{outline['title']}' generata")
        return outline

    return _planning


def make_real_writing_dep(total_chapters: int = 24, words_per_chapter: int = 1500) -> Callable[[dict], dict]:
    """Dependency REALE per la fase WRITING (CP9): apre una sessione LM Arena propria,
    genera il manoscritto capitolo per capitolo con continuita' (CP5), chiude la sessione.
    Default 24 capitoli x 1500 parole = 36000 parole, dentro il range target di
    kdp_formatter (120±5 pagine a 300 parole/pagina = 34500-37500)."""
    from playwright.sync_api import sync_playwright

    from . import book_writer, lmarena_client

    def _writing(planning: dict) -> dict:
        with sync_playwright() as p:
            session = lmarena_client.open_session(p, headless=True)
            try:
                book = book_writer.write_chapters(session.page, planning, total_chapters, words_per_chapter)
            finally:
                session.close()
        print(f"[orchestrator] writing reale: {len(book['chapters'])} capitoli generati")
        return book

    return _writing


if __name__ == "__main__":
    import argparse
    import shutil
    import sys
    import tempfile

    cli = argparse.ArgumentParser(
        description="CP9 Orchestrator — senza argomenti esegue il self-test del "
                     "meccanismo checkpoint/resume; con --keyword/--title esegue un run "
                     "REALE completo (research Amazon + planning/writing/cover via LM "
                     "Arena + formatting/packaging)."
    )
    cli.add_argument("--keyword", help="Keyword reale per la ricerca Amazon (CP2)")
    cli.add_argument("--title", help="Titolo di lavoro del libro da qualificare (CP3)")
    cli.add_argument("--description", default="", help="Descrizione/sinossi di lavoro")
    cli.add_argument("--run-id", default=None, help="Run id per checkpoint/resume (default: timestamp)")
    cli.add_argument("--total-chapters", type=int, default=24, help="Numero capitoli (default 24)")
    cli.add_argument("--words-per-chapter", type=int, default=1500, help="Parole/capitolo (default 1500)")
    args = cli.parse_args()

    if args.keyword or args.title:
        if not (args.keyword and args.title):
            cli.error("--keyword e --title vanno passati insieme")
        run_id = args.run_id or f"real_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"=== CP9 run REALE completo (run_id={run_id}): research Amazon + "
              f"planning/writing/cover via LM Arena + formatting/packaging ===\n")
        deps = {
            "research": make_real_research_dep(args.keyword, args.title, args.description),
            "planning": make_real_planning_dep(),
            "writing": make_real_writing_dep(args.total_chapters, args.words_per_chapter),
            "cover": cover_generator.make_real_cover_dep(),
        }
        orch = Orchestrator(run_id, deps=deps)
        try:
            orch.run()
        except NotImplementedError as e:
            # fase non ancora costruita — stato atteso del piano, non un errore reale
            print(f"\n[orchestrator] fermato onestamente, fase non ancora costruita: {e}")
            print(f"[orchestrator] checkpoint salvato: {orch.checkpoint_path}")
            sys.exit(0)
        except RuntimeError as e:
            # errore reale (NO-GO qualifica, formattazione fuori target, sessione LM Arena
            # non valida, ecc.) — MAI mascherato da exit 0, altrimenti un run fallito
            # sembrerebbe riuscito a chiunque controlli solo l'exit code
            print(f"\n[orchestrator] FALLITO: {e}")
            print(f"[orchestrator] checkpoint salvato: {orch.checkpoint_path}")
            sys.exit(1)
        sys.exit(0)

    print("=== CP9 self-test: meccanismo checkpoint/resume, fasi non costruite "
          "sostituite da moduli finti (dependency injection) ===\n")

    call_counts = {"research": 0, "planning": 0, "writing": 0, "cover": 0}

    def fake_research():
        call_counts["research"] += 1
        return {"title": "The Cozy Cat Mystery of Test Street: A Small Town Cozy Mystery",
                "description": "cozy mystery cats small town"}

    def fake_planning(research):
        call_counts["planning"] += 1
        return {"outline": "3-act", "kdp_metadata": "keywords: cozy mystery cats"}

    def fake_writing(planning):
        call_counts["writing"] += 1
        filler = " ".join(["parola"] * 1500)
        chapters = [{"title": f"Chapter {i+1}", "paragraphs": [filler, filler]} for i in range(12)]
        return {"title": "The Cozy Cat Mystery of Test Street", "author": "Test Author", "chapters": chapters}

    def fake_cover(writing):
        call_counts["cover"] += 1
        cover_path = Path(tempfile.gettempdir()) / "cp9_test_cover.png"
        cover_path.write_bytes(b"FINTA-COPERTINA-TEST" * 20)
        return {"cover_path": str(cover_path)}

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        checkpoints_dir = tmp_path / "_run_checkpoints"
        output_dir = tmp_path / "_wip"
        libri_pronti_original = config.LIBRI_PRONTI_DIR
        config.LIBRI_PRONTI_DIR = tmp_path / "LIBRI" / "libri_pronti"

        try:
            # --- Test 1: run completo con tutte le dipendenze finte presenti ---
            deps_complete = {"research": fake_research, "planning": fake_planning,
                              "writing": fake_writing, "cover": fake_cover}
            orch = Orchestrator("test_run_1", checkpoints_dir, output_dir, deps=deps_complete)
            final_state = orch.run()
            assert final_state.current_phase == Phase.DONE
            assert Path(final_state.data["packaging"]["folder_path"]).exists()
            print(f"[Test 1] run completo OK: {final_state.data['packaging']['folder_path']}")
            assert call_counts == {"research": 1, "planning": 1, "writing": 1, "cover": 1}
            print("[Test 1] ogni fase chiamata esattamente 1 volta — OK\n")

            # --- Test 2: NotImplementedError esplicito se una fase non è costruita ---
            orch2 = Orchestrator("test_run_2", checkpoints_dir, output_dir, deps={})
            try:
                orch2.run()
                raise AssertionError("ERRORE: doveva sollevare NotImplementedError")
            except NotImplementedError as e:
                print(f"[Test 2] NotImplementedError corretto per fase non costruita: {e}\n")

            # --- Test 3: resume dopo crash a metà — NON deve rieseguire le fasi già fatte ---
            call_counts_resume = {"research": 0, "planning": 0}

            def counting_research():
                call_counts_resume["research"] += 1
                return fake_research()

            def counting_planning(research):
                call_counts_resume["planning"] += 1
                if call_counts_resume["planning"] == 1:
                    raise RuntimeError("Crash simulato a metà (es. LM Arena non risponde)")
                return fake_planning(research)

            deps_crash = {"research": counting_research, "planning": counting_planning,
                          "writing": fake_writing, "cover": fake_cover}
            orch3a = Orchestrator("test_run_3", checkpoints_dir, output_dir, deps=deps_crash)
            try:
                orch3a.run()
                raise AssertionError("ERRORE: doveva crashare al primo tentativo")
            except RuntimeError:
                print("[Test 3] crash simulato durante PLANNING, come atteso")

            assert call_counts_resume["research"] == 1, "research doveva essere chiamata 1 volta prima del crash"
            checkpoint_after_crash = json.loads((checkpoints_dir / "test_run_3.json").read_text())
            assert checkpoint_after_crash["current_phase"] == "planning", (
                f"ERRORE: checkpoint doveva essere fermo a 'planning', trovato "
                f"'{checkpoint_after_crash['current_phase']}'"
            )
            print(f"[Test 3] checkpoint su disco fermo a fase 'planning', come atteso")

            # Rilancio con lo STESSO run_id — deve riprendere da planning, NON richiamare research
            orch3b = Orchestrator("test_run_3", checkpoints_dir, output_dir, deps=deps_crash)
            final_state_3 = orch3b.run()
            assert final_state_3.current_phase == Phase.DONE
            assert call_counts_resume["research"] == 1, (
                f"ERRORE CRITICO: research richiamata {call_counts_resume['research']} volte — "
                f"il resume ha rieseguito una fase già completata invece di riprendere"
            )
            assert call_counts_resume["planning"] == 2, "planning doveva essere richiamata (1 crash + 1 successo)"
            print("[Test 3] resume corretto: research NON rieseguita, planning ripresa e completata\n")

            # --- Test 4: qualifica NO-GO blocca la pipeline prima di scrivere ---
            def diary_research():
                return {"title": "My Daily Gratitude Journal Planner", "description": "guided journal tracker"}

            deps_diary = {"research": diary_research, "planning": fake_planning,
                          "writing": fake_writing, "cover": fake_cover}
            orch4 = Orchestrator("test_run_4", checkpoints_dir, output_dir, deps=deps_diary)
            try:
                orch4.run()
                raise AssertionError("ERRORE: doveva essere NO-GO e bloccare la pipeline")
            except RuntimeError as e:
                assert "NO-GO" in str(e)
                print(f"[Test 4] pipeline bloccata correttamente su NO-GO qualifica: {e}\n")

        finally:
            config.LIBRI_PRONTI_DIR = libri_pronti_original

    print("CP9 self-test: TUTTO VERIFICATO OK (meccanismo checkpoint/resume)")
    print("NOTA: qui sopra le fasi sono moduli finti (dependency injection), per isolare il "
          "test del meccanismo checkpoint/resume dal costo/tempo di chiamate reali. Le "
          "dependency REALI esistono per TUTTE le fasi (research/planning/writing/cover) e "
          "sono integrate nella CLI — usale con "
          "'python -m engine.orchestrator --keyword ... --title ...'. Run end-to-end reale "
          "non ancora verificato: richiede una sessione LM Arena valida (vedi PIANO-KDP-67.md).")
    sys.exit(0)
