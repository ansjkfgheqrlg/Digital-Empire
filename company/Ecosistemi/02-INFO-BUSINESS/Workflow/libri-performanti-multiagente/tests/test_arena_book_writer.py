"""
Test del flusso "libri via Arena v3" (2026-08-15) — parser, verificatori, persistenza.

NESSUN test qui apre un browser o chiama un modello: girano sempre, gratis, in millisecondi.
Verificano la logica che deve reggere PRIMA di spendere quota reale e pazienza umana su
LM Arena (dove ogni captcha costa un intervento manuale).

I casi non sono inventati: riproducono forme di risposta REALI gia' viste da questo
progetto — decorazione markdown sui campi (`**TITLE:**`), risposte troncate a meta' campo,
capitoli identici fra loro (bug di estrazione del 2026-08-06), elenchi restituiti su una
riga separata da virgole invece che uno per riga.

    python -m pytest tests/test_arena_book_writer.py -v
"""
from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import arena_book_writer as abw  # noqa: E402
from engine import book_project, cover_generator  # noqa: E402


PIANO_VALIDO_RAW = """TITLE: Murder at Maple Bakery
CHARACTERS: Anna Reyes, 34, baker turned sleuth. Sam Cole, 40, sheriff.
ACT1: A cozy mystery begins when Anna reopens the family bakery.
ACT2: A murder investigation deepens and Anna becomes a suspect.
ACT3: The mystery is solved during the town festival.
CHAPTERS:
1. Anna arrives and reopens the bakery.
2. A threatening note appears.
3. The body is discovered at dawn.
COVER_PROMPT: A cozy small-town bakery at dusk, warm lights, autumn leaves.
"""


def _piano_valido() -> dict:
    return abw._parse_piano(PIANO_VALIDO_RAW, capitoli_attesi=3)


# --------------------------------------------------------------------------- #
# FASE 2 — parsing del piano
# --------------------------------------------------------------------------- #

def test_parse_piano_estrae_tutti_i_campi():
    piano = _piano_valido()
    assert piano["title"] == "Murder at Maple Bakery"
    assert "Anna Reyes" in piano["characters"]
    assert piano["act1"].startswith("A cozy mystery begins")
    assert len(piano["chapters"]) == 3
    assert piano["chapters"][2] == "The body is discovered at dawn."
    assert piano["cover_prompt"].startswith("A cozy small-town bakery")


def test_parse_piano_tollera_decorazione_markdown():
    """Il modello decora l'output quasi sempre — un parser rigido perde tutto il piano."""
    raw = PIANO_VALIDO_RAW.replace("TITLE:", "**TITLE:**").replace("ACT1:", "## ACT1:")
    piano = abw._parse_piano(raw, capitoli_attesi=3)
    assert piano["title"] == "Murder at Maple Bakery"
    assert piano["act1"].startswith("A cozy mystery begins")


def test_parse_piano_campo_mancante_solleva_con_nome_del_campo():
    raw = PIANO_VALIDO_RAW.replace(
        "COVER_PROMPT: A cozy small-town bakery at dusk, warm lights, autumn leaves.\n", ""
    )
    with pytest.raises(ValueError, match="COVER_PROMPT"):
        abw._parse_piano(raw, capitoli_attesi=3)


def test_parse_piano_conteggio_capitoli_sbagliato_solleva():
    """Un sommario corto significa un libro corto: va intercettato PRIMA di scrivere."""
    with pytest.raises(ValueError, match="24"):
        abw._parse_piano(PIANO_VALIDO_RAW, capitoli_attesi=24)


def test_parse_piano_voce_capitolo_su_piu_righe():
    raw = PIANO_VALIDO_RAW.replace(
        "3. The body is discovered at dawn.",
        "3. The body is discovered at dawn\n   behind the bakery, in the rain.",
    )
    piano = abw._parse_piano(raw, capitoli_attesi=3)
    assert len(piano["chapters"]) == 3
    assert "behind the bakery" in piano["chapters"][2]


# --------------------------------------------------------------------------- #
# FASE 2 — verificatore
# --------------------------------------------------------------------------- #

def test_verifica_piano_valido_non_ha_problemi():
    assert abw.verifica_piano(_piano_valido(), capitoli_attesi=3) == []


def test_verifica_piano_segnala_cover_prompt_vuoto():
    piano = _piano_valido()
    piano["cover_prompt"] = "   "
    problemi = abw.verifica_piano(piano, capitoli_attesi=3)
    assert any("cover_prompt" in p for p in problemi)


def test_verifica_piano_blocca_un_diario_non_una_storia():
    """story_validator applicato alla TRAMA vera, non alla sola keyword di nicchia."""
    piano = _piano_valido()
    piano["title"] = "My Daily Gratitude Journal Planner"
    piano["act1"] = "A guided journal with a mood tracker."
    piano["act2"] = piano["act3"] = ""
    problemi = abw.verifica_piano(piano, capitoli_attesi=3)
    assert any("NO-GO" in p for p in problemi)


def test_verifica_piano_non_solleva_mai_da_sola():
    """Ritorna problemi, non eccezioni: chi chiama decide se bloccare."""
    problemi = abw.verifica_piano({"chapters": []}, capitoli_attesi=3)
    assert isinstance(problemi, list) and problemi


# --------------------------------------------------------------------------- #
# FASE 3 — capitoli
# --------------------------------------------------------------------------- #

def test_split_chapter_richiede_il_marcatore():
    with pytest.raises(ValueError, match="RIASSUNTO"):
        abw._split_chapter_and_summary("testo del capitolo senza marcatore")


def test_split_chapter_separa_corpo_e_riassunto():
    corpo, riassunto = abw._split_chapter_and_summary(
        f"Il corpo del capitolo.\n{abw.SUMMARY_MARKER}\nAnna trova un indizio."
    )
    assert corpo == "Il corpo del capitolo."
    assert riassunto == "Anna trova un indizio."


def test_capitolo_duplicato_viene_rifiutato():
    """Bug reale del 2026-08-06: 3 capitoli identici passati inosservati."""
    testo = "Anna aprì la porta della panetteria."
    with pytest.raises(RuntimeError, match="IDENTICO"):
        abw._assert_not_duplicate(testo, 2, [testo])


def test_capitolo_duplicato_ignora_spaziatura_e_maiuscole():
    with pytest.raises(RuntimeError, match="IDENTICO"):
        abw._assert_not_duplicate("Anna  APRÌ   la porta.", 3, ["anna aprì la porta."])


def test_chapter_prompt_include_la_traccia_del_piano():
    """La traccia per-capitolo è la miglioria resa possibile dal sommario di Fase 2:
    senza, ogni capitolo sarebbe scritto senza sapere cosa deve succederci."""
    piano = _piano_valido()
    prompt = abw._chapter_prompt(piano, 2, 3, "Anna è arrivata in città.", 1500)
    assert "A threatening note appears." in prompt
    assert "Anna è arrivata in città." in prompt
    assert "chapter 2 of 3" in prompt


def test_chapter_prompt_primo_capitolo_non_finge_continuita():
    prompt = abw._chapter_prompt(_piano_valido(), 1, 3, "", 1500)
    assert "FIRST chapter" in prompt


def test_write_chapters_scrive_su_disco_e_riprende_dal_mancante(tmp_path, monkeypatch):
    """Il capitolo va su disco APPENA generato — è ciò che rende possibile il resume."""
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Test Resume", "cozy mystery",
                                              capitoli=3, parole_per_capitolo=100)
    progetto.path_capitolo(1).write_text("Capitolo uno gia' scritto.", encoding="utf-8")

    generati = []

    def finto_send(page, prompt, timeout_s=600, force_new_chat=True):
        numero = len(generati) + 2
        generati.append(numero)
        return f"Corpo del capitolo {numero}.\n{abw.SUMMARY_MARKER}\nRiassunto {numero}."

    monkeypatch.setattr(abw.lmarena_client, "send_text_prompt", finto_send)

    abw.write_chapters(None, progetto, _piano_valido(), da_capitolo=2, parole_per_capitolo=100)

    assert generati == [2, 3], "doveva generare solo i capitoli mancanti"
    assert progetto.path_capitolo(1).read_text(encoding="utf-8") == "Capitolo uno gia' scritto."
    assert "capitolo 2" in progetto.path_capitolo(2).read_text(encoding="utf-8")
    assert "Riassunto 3" in progetto.riassunti_path.read_text(encoding="utf-8")


def test_write_chapters_staging_fallito_non_blocca(tmp_path, monkeypatch):
    """Google Doc è solo staging: un suo fallimento non deve mai perdere un capitolo."""
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Test Staging", "cozy mystery",
                                              capitoli=1, parole_per_capitolo=100)

    monkeypatch.setattr(
        abw.lmarena_client, "send_text_prompt",
        lambda *a, **k: f"Corpo.\n{abw.SUMMARY_MARKER}\nRiassunto.",
    )
    from engine import google_doc_staging
    monkeypatch.setattr(google_doc_staging, "append_chapter", lambda *a, **k: False)

    piano = _piano_valido()
    piano["chapters"] = ["solo uno"]
    abw.write_chapters(None, progetto, piano, parole_per_capitolo=100,
                       doc_session=object())

    assert progetto.path_capitolo(1).exists(), "il capitolo deve esistere anche se lo staging fallisce"


# --------------------------------------------------------------------------- #
# FASE 5 — copy KDP
# --------------------------------------------------------------------------- #

COPY_RAW = """FINAL_TITLE: Murder at Maple Bakery
SUBTITLE: A Small Town Cozy Mystery
DESCRIPTION: Anna torna a casa per riaprire la panetteria di famiglia e trova un cadavere.
KEYWORDS: cozy mystery
small town bakery
amateur sleuth
CATEGORIES: Mystery
Thriller & Suspense
"""


def test_parse_copy_estrae_liste_una_per_riga():
    copy = abw._parse_copy(COPY_RAW)
    assert copy["titolo_finale"] == "Murder at Maple Bakery"
    assert copy["sottotitolo"] == "A Small Town Cozy Mystery"
    assert copy["keywords"] == ["cozy mystery", "small town bakery", "amateur sleuth"]
    assert copy["categorie"] == ["Mystery", "Thriller & Suspense"]


def test_parse_copy_tollera_liste_separate_da_virgola():
    """Il modello non rispetta sempre 'una per riga'."""
    raw = COPY_RAW.replace(
        "KEYWORDS: cozy mystery\nsmall town bakery\namateur sleuth",
        "KEYWORDS: cozy mystery, small town bakery, amateur sleuth",
    )
    assert abw._parse_copy(raw)["keywords"] == [
        "cozy mystery", "small town bakery", "amateur sleuth",
    ]


def test_parse_copy_campo_obbligatorio_mancante_solleva():
    raw = COPY_RAW.replace("FINAL_TITLE: Murder at Maple Bakery\n", "")
    with pytest.raises(ValueError, match="FINAL_TITLE"):
        abw._parse_copy(raw)


def test_verifica_copy_valido():
    assert abw.verifica_copy(abw._parse_copy(COPY_RAW)) == []


def test_verifica_copy_troppe_keyword():
    """KDP ne accetta un numero limitato: inviarne di più le fa scartare in silenzio."""
    copy = abw._parse_copy(COPY_RAW)
    copy["keywords"] = [f"kw{i}" for i in range(abw.LIMITE_KEYWORDS_KDP + 3)]
    problemi = abw.verifica_copy(copy)
    assert any(str(abw.LIMITE_KEYWORDS_KDP) in p for p in problemi)


# --------------------------------------------------------------------------- #
# Persistenza su BookProject + metadati KDP
# --------------------------------------------------------------------------- #

def test_piano_e_copy_sopravvivono_su_disco(tmp_path, monkeypatch):
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Persistenza", "cozy mystery",
                                              capitoli=3, parole_per_capitolo=100)
    piano = _piano_valido()
    progetto.salva_piano(piano)
    progetto.salva_copy(abw._parse_copy(COPY_RAW))
    progetto.salva_url_chat("https://arena.ai/c/abc")

    riletto = book_project.BookProject(progetto.slug)
    assert riletto.piano()["chapters"] == piano["chapters"]
    assert riletto.copy_kdp()["titolo_finale"] == "Murder at Maple Bakery"
    assert riletto.url_chat() == "https://arena.ai/c/abc"
    # il titolo originale del progetto non viene sovrascritto dal copy
    assert riletto._config()["titolo"] == "Persistenza"


def test_metadata_kdp_include_il_copy(tmp_path, monkeypatch):
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Con Copy", "cozy mystery",
                                              capitoli=1, parole_per_capitolo=100)
    progetto.salva_copy(abw._parse_copy(COPY_RAW))
    risultato = types.SimpleNamespace(word_count=35000, estimated_pages=116.7)

    testo = progetto._metadata_kdp(progetto._config(), risultato)
    assert "Murder at Maple Bakery" in testo
    assert "amateur sleuth" in testo
    assert "Anna torna a casa" in testo


def test_metadata_kdp_senza_copy_resta_il_minimo(tmp_path, monkeypatch):
    """Progetti vecchi (o libri senza Fase 5) non devono rompersi."""
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    progetto = book_project.BookProject.crea("Senza Copy", "cozy mystery",
                                              capitoli=1, parole_per_capitolo=100)
    risultato = types.SimpleNamespace(word_count=35000, estimated_pages=116.7)

    testo = progetto._metadata_kdp(progetto._config(), risultato)
    assert "Senza Copy" in testo
    assert "Keyword KDP" not in testo


# --------------------------------------------------------------------------- #
# FASE 4 — copertina dal piano
# --------------------------------------------------------------------------- #

def test_cover_prompt_dal_piano_conserva_i_vincoli_kdp():
    """Il wrapper tecnico non si delega mai al modello: formato 2:3 e spelling del titolo
    sono stati conquistati con bug reali (copertina quadrata, titolo troncato)."""
    prompt = cover_generator._wrap_cover_prompt(
        "A cozy bakery at dusk.", title="Murder at Maple Bakery", author="Digital Empire",
    )
    assert "2:3 aspect ratio" in prompt
    assert "Do NOT produce a square image" in prompt
    assert '"Murder at Maple Bakery"' in prompt
    assert "A cozy bakery at dusk." in prompt


def test_cover_da_piano_senza_prompt_si_ferma():
    with pytest.raises(ValueError, match="cover_prompt"):
        cover_generator.generate_cover_from_plan(None, {"cover_prompt": ""}, "Titolo")
