"""
Arena Book Writer — FASI 2/3/5 del flusso "libri via Arena v3" (2026-08-15): piano di
produzione, capitoli uno alla volta, copy KDP finale — tutto via LM Arena (Playwright),
mai via un modello Claude/API.

Sostituisce `_archivio_testo_lmarena/book_writer.py` (archiviato il 2026-08-10 dopo un
tentativo reale fallito per captcha), riusandone la logica gia' matura — continuita' via
riassunto progressivo (mai il testo intero, scala su libri lunghi), retry su risposta
troncata, guardia anti-duplicato (bug reale gia' trovato una volta: risposta di un turno
precedente riletta per errore) — con tre estensioni richieste dal flusso a 5 fasi:

1. **Il piano (Fase 2) include un sommario capitolo-per-capitolo E il prompt copertina.**
   Il vecchio outline archiviato aveva solo TITLE/CHARACTERS/ACT1/ACT2/ACT3 — nessuna
   traccia per-capitolo, nessun prompt immagine. Qui si porta dentro lo shape gia'
   collaudato in produzione del prompt Haiku (`scrittore_haiku.prompt_outline`, che ha
   gia' un CHAPTERS: numerato) aggiungendo COVER_PROMPT, mai esistito prima.

2. **Ogni capitolo si scrive SU DISCO appena generato**, non si accumula in RAM per
   ritornare un dict a fine libro (comportamento del vecchio `write_chapters`). Necessario
   per ereditare la resilienza gia' costruita in `workflow.riprendi_libro()` senza
   reinventarla: se il processo si interrompe a meta', i capitoli gia' scritti restano.

3. **Nuovo: `generate_copy()`** — tag/keyword/descrizione/titolo finale, mai esistito nel
   vecchio flusso Arena (esisteva solo nel percorso Claude CLI ormai abbandonato per la
   scrittura). Pensato per girare nella STESSA chat dell'ultimo capitolo
   (`force_new_chat=False`), coerente con la richiesta esplicita di Gael.

`force_new_chat` (vedi `lmarena_client.send_text_prompt`) e' esposto ovunque qui invece di
essere deciso a priori: quale pattern eviti meglio il captcha lo misura
`engine/lmarena_captcha_probe.py` (Fase 0), non un'assunzione di questo modulo.

Ogni funzione `verifica_*` NON solleva mai un'eccezione da sola: ritorna una lista di
problemi (vuota = tutto ok), stesso pattern gia' in produzione in `validators.py`/
`report_validazione.py`. Sono gli "agenti controllori" del flusso — funzioni Python che
girano davvero, non narrativa (vedi il precedente a 95+ agenti finti in
`_archivio_blueprint_narrativo/`, controllato e trovato a zero automazione reale).
"""
from __future__ import annotations

import re

from playwright.sync_api import Page

from . import config, lmarena_client, story_validator

SUMMARY_MARKER = "---RIASSUNTO---"

# Limite reale del form KDP per le keyword di ricerca — citato a memoria (era gia' cosi'
# nel flusso Claude CLI precedente), da RICONFERMARE sulla UI KDP corrente prima di
# considerarlo un fatto verificato in questa sessione.
LIMITE_KEYWORDS_KDP = 7


# --------------------------------------------------------------------------- #
# Parsing condiviso — tollerante a decorazione markdown (**bold**, # heading, ecc.)
# --------------------------------------------------------------------------- #

def _normalizza_riga(riga: str) -> str:
    return riga.strip().lstrip("#*_ \t").strip()


def _pulisci_valore_campo(testo: str) -> str:
    """Rimuove whitespace e decorazione markdown dai bordi di un valore estratto — stesso
    idioma gia' in `workflow.estrai_titolo`, qui generalizzato a ogni campo: i modelli
    decorano l'intero output, non solo la riga del titolo."""
    return testo.strip().strip("*_\"'").strip()


def _matched_field(riga_pulita: str, nomi_campo: list[str]) -> tuple[str, str] | None:
    upper = riga_pulita.upper()
    for nome in nomi_campo:
        prefisso = f"{nome}:"
        if upper.startswith(prefisso):
            return nome, riga_pulita[len(prefisso):].strip()
    return None


def _raccogli_campi(raw: str, nomi_campo: list[str]) -> dict[str, list[str]]:
    """Divide una risposta in blocchi per campo, tollerando decorazione markdown sulle
    righe di intestazione. Stesso principio di `book_writer._parse_outline` (archiviato),
    generalizzato a un elenco di campi qualsiasi invece che ai 5 fissi dell'outline."""
    lines_by_field: dict[str, list[str]] = {k: [] for k in nomi_campo}
    current: str | None = None
    for riga in raw.splitlines():
        pulita = _normalizza_riga(riga)
        match = _matched_field(pulita, nomi_campo) if pulita else None
        if match:
            current, resto = match
            if resto:
                lines_by_field[current].append(resto)
            continue
        if current and riga.strip():
            lines_by_field[current].append(riga.strip())
    return lines_by_field


_CHAPTER_LINE_RE = re.compile(r"^\s*\d+[.\)]\s*(.+)$")


def _parse_chapters_block(righe: list[str]) -> list[str]:
    """Estrae le voci numerate del sommario capitoli. Una riga senza numero in testa si
    considera continuazione della voce precedente (il modello a volte spezza una
    descrizione lunga su piu' righe)."""
    capitoli: list[str] = []
    for r in righe:
        r = r.strip()
        if not r:
            continue
        m = _CHAPTER_LINE_RE.match(r)
        if m:
            capitoli.append(_pulisci_valore_campo(m.group(1)))
        elif capitoli:
            capitoli[-1] = f"{capitoli[-1]} {r}".strip()
    return capitoli


# --------------------------------------------------------------------------- #
# FASE 2 — Piano di produzione (outline + sommario capitoli + prompt copertina)
# --------------------------------------------------------------------------- #

_CAMPI_PIANO_TESTO_LIBERO = ["CHARACTERS", "ACT1", "ACT2", "ACT3", "COVER_PROMPT"]
_CAMPI_PIANO = _CAMPI_PIANO_TESTO_LIBERO + ["CHAPTERS"]


def prompt_piano(nicchia: str, titolo_lavoro: str, competitor: list[str], capitoli: int) -> str:
    riferimenti = "\n".join(f"- {t}" for t in competitor[:5]) or "- (none)"
    return f"""You are outlining a new genre-fiction novel for the Amazon KDP market.

Genre/niche: {nicchia}
Working title: {titolo_lavoro}

Successful books in the same niche (to understand what readers want — do NOT copy them,
the text must be completely original):
{riferimenti}

Write the FULL PRODUCTION PLAN for this novel, in English, in EXACTLY this format:

TITLE: <final, commercial title, clear about the genre>
CHARACTERS: <4-5 main characters, one line, comma-separated, each with a short role>
ACT1: <setup, 3-4 sentences>
ACT2: <development and complication, 3-4 sentences>
ACT3: <resolution, including the final twist, 3-4 sentences>
CHAPTERS:
1. <what happens in chapter 1, one line>
2. <...>
(exactly {capitoli} chapters, numbered 1 to {capitoli})
COVER_PROMPT: <a vivid, specific visual description for a book cover illustration — scene,
mood, main character(s) if shown, setting, color palette. Creative description ONLY — do
NOT mention dimensions, resolution, or technical specs, those are added separately.>

Rules: no explicit violence, no explicit sexual content. Every chapter must end on a hook
that pulls the reader to the next one. Reply ONLY with the format above, no commentary."""


def _parse_piano(raw: str, capitoli_attesi: int) -> dict:
    from . import workflow  # import locale: evita un ciclo — workflow.py importera' questo
                             # modulo per lo STEP 2 una volta agganciato (vedi piano, Fase 11)

    lines_by_field = _raccogli_campi(raw, _CAMPI_PIANO)
    titolo = workflow.estrai_titolo(raw)

    mancanti = [c for c in _CAMPI_PIANO_TESTO_LIBERO if not lines_by_field[c]]
    if not lines_by_field["CHAPTERS"]:
        mancanti.append("CHAPTERS")
    if not titolo:
        mancanti.insert(0, "TITLE")
    if mancanti:
        raise ValueError(
            f"Piano incompleto, campi mancanti: {mancanti}. Risposta grezza: {raw[:500]!r}"
        )

    capitoli = _parse_chapters_block(lines_by_field["CHAPTERS"])
    if len(capitoli) != capitoli_attesi:
        raise ValueError(
            f"Piano con {len(capitoli)} capitoli nel sommario, attesi {capitoli_attesi}. "
            f"Sommario grezzo: {lines_by_field['CHAPTERS']!r}"
        )

    return {
        "title": titolo,
        "characters": _pulisci_valore_campo(" ".join(lines_by_field["CHARACTERS"])),
        "act1": _pulisci_valore_campo(" ".join(lines_by_field["ACT1"])),
        "act2": _pulisci_valore_campo(" ".join(lines_by_field["ACT2"])),
        "act3": _pulisci_valore_campo(" ".join(lines_by_field["ACT3"])),
        "chapters": capitoli,
        "cover_prompt": _pulisci_valore_campo(" ".join(lines_by_field["COVER_PROMPT"])),
    }


def generate_plan(page: Page, mercato: dict, nicchia: str, titolo_lavoro: str,
                   capitoli: int = 24) -> dict:
    """Genera il piano di produzione — Fase 2. Retry su risposta incompleta o conteggio
    capitoli sbagliato: si RIMANDA il prompt (una generazione NUOVA), mai si prova a
    rileggere una risposta troncata (stesso principio del vecchio `generate_outline`
    archiviato)."""
    competitor_titoli = mercato.get("titoli", [])
    prompt = prompt_piano(nicchia, titolo_lavoro, competitor_titoli, capitoli)

    ultimo_errore: ValueError | None = None
    for tentativo in range(1, config.MAX_RETRIES + 1):
        raw = lmarena_client.send_text_prompt(page, prompt)
        try:
            return _parse_piano(raw, capitoli)
        except ValueError as exc:
            ultimo_errore = exc
            print(f"[arena_book_writer] piano incompleto al tentativo {tentativo}/"
                  f"{config.MAX_RETRIES} ({exc}) — rigenero")
    raise ultimo_errore


def verifica_piano(piano: dict, capitoli_attesi: int) -> list[str]:
    """Verificatore Fase 2 — controlla il piano PRIMA che la Fase 3 lo usi per scrivere.
    Mai un'eccezione da sola: ritorna la lista dei problemi, chi chiama decide se
    bloccare (stesso pattern di `validators.py`)."""
    problemi: list[str] = []
    for campo in ("title", "characters", "act1", "act2", "act3", "cover_prompt"):
        if not (piano.get(campo) or "").strip():
            problemi.append(f"campo '{campo}' vuoto nel piano")

    capitoli = piano.get("chapters", [])
    if len(capitoli) != capitoli_attesi:
        problemi.append(f"sommario con {len(capitoli)} capitoli, attesi {capitoli_attesi}")
    if any(not c.strip() for c in capitoli):
        problemi.append("almeno una voce del sommario capitoli e' vuota")

    verdetto = story_validator.validate(
        piano.get("title", ""),
        f"{piano.get('act1', '')} {piano.get('act2', '')} {piano.get('act3', '')}",
    )
    if not verdetto.is_go:
        problemi.append(f"story_validator NO-GO sulla trama: {verdetto.motivation}")

    return problemi


# --------------------------------------------------------------------------- #
# FASE 3 — Capitoli uno alla volta
# --------------------------------------------------------------------------- #

def _chapter_prompt(piano: dict, numero: int, totale: int, riassunto_corrente: str,
                     parole: int) -> str:
    continuita = (
        f"What has happened so far: {riassunto_corrente}"
        if riassunto_corrente else
        "This is the FIRST chapter — establish the setting and characters, no prior events."
    )
    capitoli = piano.get("chapters", [])
    traccia = capitoli[numero - 1] if 0 <= numero - 1 < len(capitoli) else ""
    traccia_nota = f"\nWhat should happen in THIS chapter, per the plan: {traccia}" if traccia else ""
    return (
        f"Continue writing the novel \"{piano['title']}\".\n"
        f"Characters: {piano['characters']}\n"
        f"Overall plot — Act 1: {piano['act1']} Act 2: {piano['act2']} Act 3: {piano['act3']}\n"
        f"{continuita}{traccia_nota}\n\n"
        f"Write chapter {numero} of {totale}, approximately {parole} words, prose only "
        "(no title heading, no meta-commentary), consistent with the characters and plot "
        "established above.\n\n"
        f"After the chapter text, add a line with EXACTLY '{SUMMARY_MARKER}' followed by a "
        "2-3 sentence summary of THIS chapter's events, to be used as continuity context "
        "for the next one."
    )


def _split_chapter_and_summary(raw: str) -> tuple[str, str]:
    if SUMMARY_MARKER not in raw:
        raise ValueError(
            f"Risposta capitolo senza marcatore '{SUMMARY_MARKER}' — impossibile estrarre "
            f"il riassunto per il capitolo successivo. Risposta grezza: {raw[:300]!r}"
        )
    body, _, summary = raw.partition(SUMMARY_MARKER)
    body, summary = body.strip(), summary.strip()
    if not body or not summary:
        raise ValueError("Capitolo o riassunto vuoto dopo lo split — generazione incompleta")
    return body, summary


def _assert_not_duplicate(body: str, numero: int, gia_scritti: list[str]) -> None:
    """Guardia anti-duplicato — bug reale gia' trovato una volta (2026-08-06, archivio
    `book_writer.py`): un bug nel client LM Arena poteva restituire la risposta di un
    turno PRECEDENTE. Portata identica, mai riscoperta da capo."""
    normalizzato = " ".join(body.split()).lower()
    for prev_numero, prev_body in enumerate(gia_scritti, start=1):
        prev_normalizzato = " ".join(prev_body.split()).lower()
        if normalizzato == prev_normalizzato:
            raise RuntimeError(
                f"Capitolo {numero}: testo IDENTICO al capitolo {prev_numero} — quasi "
                f"certamente un bug di estrazione (risposta di un turno precedente riletta "
                f"per errore), mai una coincidenza reale a questa lunghezza."
            )


def _generate_one_chapter(page: Page, piano: dict, numero: int, totale: int,
                           riassunto_corrente: str, parole: int, gia_scritti: list[str],
                           *, force_new_chat: bool) -> tuple[str, str]:
    """Genera UN capitolo, con retry su risposta troncata/duplicata. `CaptchaRequired` NON
    viene catturata: li' serve un umano, ritentare da soli non puo' funzionare."""
    prompt = _chapter_prompt(piano, numero, totale, riassunto_corrente, parole)
    ultimo_errore: Exception | None = None
    for tentativo in range(1, config.MAX_RETRIES + 1):
        raw = lmarena_client.send_text_prompt(page, prompt, timeout_s=600,
                                              force_new_chat=force_new_chat)
        try:
            body, summary = _split_chapter_and_summary(raw)
            _assert_not_duplicate(body, numero, gia_scritti)
            return body, summary
        except lmarena_client.CaptchaRequired:
            raise
        except (ValueError, RuntimeError) as exc:
            ultimo_errore = exc
            print(f"[arena_book_writer] capitolo {numero}: risposta non valida al "
                  f"tentativo {tentativo}/{config.MAX_RETRIES} ({exc}) — rigenero")
    raise ultimo_errore


def write_chapters(page: Page, progetto, piano: dict, *, force_new_chat: bool = True,
                    da_capitolo: int = 1, parole_per_capitolo: int = 1500,
                    doc_session=None) -> None:
    """Scrive i capitoli da `da_capitolo` in poi, uno alla volta, SCRIVENDO OGNI CAPITOLO
    SU DISCO appena generato (differenza deliberata dal vecchio `write_chapters`
    archiviato, che accumulava tutto in RAM e ritornava un dict a fine libro) — necessario
    per ereditare la resilienza di `workflow.riprendi_libro()` senza reinventarla: se il
    processo si interrompe a meta', i capitoli gia' scritti restano su disco.

    `doc_session`, se passato (una `google_doc_staging.GoogleDocSession`), riceve ogni
    capitolo appena scritto come staging di sicurezza — MAI bloccante: un fallimento li'
    non deve mai far fallire la scrittura, che ha gia' un canale affidabile (il file)."""
    totale = len(piano["chapters"])
    # `riassunto_progressivo()` e non la lettura grezza del file: `crea()` ci lascia dentro
    # un'intestazione e un commento segnaposto, che letti cosi' finivano nel prompt del
    # capitolo 1 come se fossero la storia accaduta finora (bug reale, 2026-08-15).
    riassunto = progetto.riassunto_progressivo()
    gia_scritti = [
        progetto.path_capitolo(n).read_text(encoding="utf-8")
        for n in range(1, da_capitolo)
        if progetto.path_capitolo(n).exists()
    ]

    for numero in range(da_capitolo, totale + 1):
        corpo, riassunto_capitolo = _generate_one_chapter(
            page, piano, numero, totale, riassunto, parole_per_capitolo, gia_scritti,
            force_new_chat=force_new_chat,
        )
        progetto.path_capitolo(numero).write_text(corpo, encoding="utf-8")
        gia_scritti.append(corpo)
        riassunto = f"{riassunto} {riassunto_capitolo}".strip()
        progetto.riassunti_path.write_text(riassunto, encoding="utf-8")
        print(f"[arena_book_writer] capitolo {numero}/{totale} scritto "
              f"({len(corpo.split())} parole)")

        if doc_session is not None:
            from . import google_doc_staging
            titolo_capitolo = piano["chapters"][numero - 1] if numero - 1 < len(piano["chapters"]) else f"Chapter {numero}"
            ok = google_doc_staging.append_chapter(doc_session, numero, titolo_capitolo, corpo)
            if not ok:
                print(f"[arena_book_writer] staging Google Doc fallito per il capitolo "
                      f"{numero} (non bloccante, il capitolo e' comunque salvo su disco)")


# --------------------------------------------------------------------------- #
# FASE 5 — Copy KDP (nella stessa chat dell'ultimo capitolo)
# --------------------------------------------------------------------------- #

_CAMPI_COPY = ["FINAL_TITLE", "SUBTITLE", "DESCRIPTION", "KEYWORDS", "CATEGORIES"]
_CAMPI_COPY_OBBLIGATORI = ["FINAL_TITLE", "DESCRIPTION", "KEYWORDS"]


def prompt_copy(piano: dict) -> str:
    return f"""The novel "{piano['title']}" is now complete.
Characters: {piano['characters']}
Overall plot — Act 1: {piano['act1']} Act 2: {piano['act2']} Act 3: {piano['act3']}

Using the chapters just written in this conversation (or, if not visible, the plot above),
write the KDP (Kindle Direct Publishing) back-cover copy package for this novel, in this
EXACT format:

FINAL_TITLE: <the final title, possibly refined from the working title>
SUBTITLE: <an optional short subtitle that adds genre/hook clarity, or leave blank>
DESCRIPTION: <a compelling back-cover description, 150-250 words, written to sell the book
to a browsing reader>
KEYWORDS: <up to {LIMITE_KEYWORDS_KDP} KDP search keywords/phrases, one per line>
CATEGORIES: <2-3 Amazon browse categories this book fits, one per line>

Reply ONLY with the format above, no commentary."""


def _lista_da_righe(righe: list[str]) -> list[str]:
    """Una voce per riga e' il formato chiesto, ma tollera anche elenchi separati da
    virgola sulla stessa riga — il modello non e' sempre coerente sul formato."""
    voci: list[str] = []
    for r in righe:
        for pezzo in r.split(","):
            pulito = _pulisci_valore_campo(pezzo.strip().lstrip("-•* \t"))
            if pulito:
                voci.append(pulito)
    return voci


def _parse_copy(raw: str) -> dict:
    lines_by_field = _raccogli_campi(raw, _CAMPI_COPY)
    mancanti = [c for c in _CAMPI_COPY_OBBLIGATORI if not lines_by_field[c]]
    if mancanti:
        raise ValueError(
            f"Copy incompleto, campi mancanti: {mancanti}. Risposta grezza: {raw[:500]!r}"
        )
    return {
        "titolo_finale": _pulisci_valore_campo(" ".join(lines_by_field["FINAL_TITLE"])),
        "sottotitolo": _pulisci_valore_campo(" ".join(lines_by_field["SUBTITLE"])),
        "descrizione": _pulisci_valore_campo(" ".join(lines_by_field["DESCRIPTION"])),
        "keywords": _lista_da_righe(lines_by_field["KEYWORDS"]),
        "categorie": _lista_da_righe(lines_by_field["CATEGORIES"]),
    }


def generate_copy(page: Page, piano: dict, progetto, *, force_new_chat: bool = False) -> dict:
    """Genera tag/keyword/descrizione/titolo finale — Fase 5. Default `force_new_chat=False`:
    per costruzione va chiamata subito dopo l'ultimo capitolo, sulla STESSA `page` (stessa
    chat), prima di chiuderla — richiesta esplicita di Gael."""
    ultimo_errore: ValueError | None = None
    for tentativo in range(1, config.MAX_RETRIES + 1):
        raw = lmarena_client.send_text_prompt(page, prompt_copy(piano),
                                              force_new_chat=force_new_chat)
        try:
            return _parse_copy(raw)
        except ValueError as exc:
            ultimo_errore = exc
            print(f"[arena_book_writer] copy incompleto al tentativo {tentativo}/"
                  f"{config.MAX_RETRIES} ({exc}) — rigenero")
    raise ultimo_errore


def verifica_copy(copy: dict) -> list[str]:
    """Verificatore Fase 5 — mai un'eccezione da sola, stesso pattern degli altri
    verificatori di questo modulo."""
    problemi: list[str] = []
    if not (copy.get("titolo_finale") or "").strip():
        problemi.append("titolo_finale vuoto nel copy")
    if not (copy.get("descrizione") or "").strip():
        problemi.append("descrizione vuota nel copy")
    keywords = copy.get("keywords", [])
    if not keywords:
        problemi.append("nessuna keyword nel copy")
    elif len(keywords) > LIMITE_KEYWORDS_KDP:
        problemi.append(
            f"{len(keywords)} keyword nel copy, il limite KDP e' {LIMITE_KEYWORDS_KDP}"
        )
    return problemi
