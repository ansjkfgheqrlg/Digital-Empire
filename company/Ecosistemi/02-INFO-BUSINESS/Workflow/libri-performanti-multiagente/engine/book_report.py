"""
Report di consegna del libro (2026-08-10, richiesta di Gael: "quando mi consegni un libro
devi darmi il pdf, la copertina, e il report — da dove hai preso il libro, da che
competitor, ecc.").

COSA DOCUMENTA, E COSA NO — la distinzione conta:

Il report registra i **libri di riferimento analizzati**: i concorrenti su cui e' stata
studiata la nicchia (titoli, prezzi, recensioni) e cosa e' stato ricavato dall'analisi
(posizionamento, fascia di prezzo, temi che vendono in quel segmento).

NON registra "da dove e' stato copiato il testo", perche' il testo non viene copiato da
nessuno: KDP passa i manoscritti in un controllo anti-plagio e chiude gli account per
contenuti derivati da altri libri — e un account chiuso porta via l'intero catalogo, non
solo il titolo segnalato. La ricerca competitor serve a capire il MERCATO (cosa vende, a
che prezzo, con quanta concorrenza), non i testi.

Il report include quindi anche una dichiarazione esplicita di originalita', che e' utile
averla scritta e datata se un domani qualcuno la chiede.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from . import config


def _competitor_dal_report_nicchia(keyword: str) -> dict | None:
    """Recupera l'analisi di nicchia salvata da `niche_finder` per questa keyword.
    Cerca il report piu' recente che la contiene — cosi' il report di consegna riporta i
    dati VERI su cui e' stata presa la decisione, non una ricostruzione a posteriori."""
    dir_report = config.LIBRI_DIR / "_ricerca_nicchie"
    if not dir_report.exists():
        return None
    for path in sorted(dir_report.glob("nicchie_*.json"), reverse=True):
        try:
            dati = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        for voce in dati:
            if voce.get("keyword", "").lower() == keyword.lower():
                voce["_file_analisi"] = path.name
                return voce
    return None


def genera_report(cfg: dict, stato, risultato_docx, pagine_reali: int | None,
                   percorsi: dict, esiti_validazione: dict) -> str:
    """Costruisce il testo del REPORT.md di consegna."""
    keyword = cfg.get("nicchia", "")
    analisi = _competitor_dal_report_nicchia(keyword)
    ora = datetime.now().strftime("%d/%m/%Y alle %H:%M")

    r: list[str] = []
    r.append(f"# Report di consegna — {cfg['titolo']}")
    r.append("")
    r.append(f"_Generato il {ora}_")
    r.append("")
    r.append("---")
    r.append("")

    # --- Il libro ---------------------------------------------------------- #
    r.append("## Il libro")
    r.append("")
    r.append(f"- **Titolo**: {cfg['titolo']}")
    r.append(f"- **Autore**: {cfg.get('autore', 'Digital Empire')}")
    r.append(f"- **Nicchia**: {keyword}")
    r.append(f"- **Capitoli**: {len(stato.capitoli_scritti)}")
    r.append(f"- **Parole**: {risultato_docx.word_count:,}".replace(",", "."))
    if pagine_reali:
        r.append(f"- **Pagine reali** (contate sul PDF impaginato): **{pagine_reali}**")
    r.append(f"- **Formato**: {config.TRIM_SIZE_INCHES[0]}x{config.TRIM_SIZE_INCHES[1]} pollici")
    r.append("")

    # --- File consegnati ---------------------------------------------------- #
    r.append("## File consegnati")
    r.append("")
    for etichetta, percorso in percorsi.items():
        r.append(f"- **{etichetta}**: `{Path(percorso).name}`" if percorso
                 else f"- **{etichetta}**: _non disponibile_")
    r.append("")

    # --- Analisi di mercato ------------------------------------------------- #
    r.append("## Su cosa si basa questo libro")
    r.append("")
    r.append("Il libro nasce da un'analisi di mercato su Amazon: quali libri vendono in "
             "questa nicchia, a che prezzo, con quanta concorrenza. **Il testo e' originale**: "
             "i concorrenti servono a capire cosa cerca il lettore, mai a riprendere contenuti "
             "(KDP verifica i manoscritti e chiude gli account per contenuti derivati).")
    r.append("")

    if analisi:
        r.append(f"### Perche' questa nicchia (punteggio {analisi.get('punteggio')}/100)")
        r.append("")
        r.append(f"{analisi.get('motivazione', '')}")
        r.append("")
        r.append(f"- Concorrenti esaminati in prima pagina: **{analisi.get('n_risultati')}**")
        r.append(f"- Recensioni mediane dei concorrenti: **{analisi.get('recensioni_mediana')}** "
                 f"(piu' sono basse, piu' e' aggredibile)")
        r.append(f"- Concorrenti deboli (sotto 100 recensioni): **{analisi.get('concorrenti_deboli')}**")
        r.append(f"- Prezzo medio della nicchia: **${analisi.get('prezzo_medio')}**")
        r.append(f"- Valutazione media: **{analisi.get('rating_medio')}/5**")
        r.append("")
        titoli = analisi.get("top_titoli") or []
        if titoli:
            r.append("### Libri di riferimento analizzati")
            r.append("")
            r.append("_Concorrenti in prima pagina su Amazon per questa ricerca. Usati per "
                     "capire posizionamento e prezzo, non come fonte di testo._")
            r.append("")
            for t in titoli:
                r.append(f"- {t}")
            r.append("")
        r.append(f"_Dati grezzi dell'analisi: `LIBRI/_ricerca_nicchie/{analisi.get('_file_analisi')}`_")
        r.append("")
    else:
        r.append("> ⚠️ Nessuna analisi di nicchia trovata per questa keyword. Il libro e' stato "
                 "impostato senza passare da `niche_finder`, quindi non ci sono dati di mercato "
                 "da riportare qui.")
        r.append("")

    # --- Controlli --------------------------------------------------------- #
    r.append("---")
    r.append("")
    r.append("## Controlli automatici eseguiti")
    r.append("")
    for nome, esito in esiti_validazione.items():
        if not esito:
            r.append(f"- ✅ **{nome}**: nessun problema")
        else:
            r.append(f"- ⚠️ **{nome}**: {len(esito)} da verificare")
            for voce in esito[:5]:
                r.append(f"    - {voce}")
            if len(esito) > 5:
                r.append(f"    - _...e altri {len(esito) - 5}_")
    r.append("")

    # --- Prima di pubblicare ------------------------------------------------ #
    r.append("---")
    r.append("")
    r.append("## Prima di pubblicare")
    r.append("")
    r.append("1. Apri il PDF e leggi almeno i primi capitoli: e' il tuo nome sulla copertina.")
    r.append("2. Controlla che il titolo sulla copertina sia scritto correttamente.")
    r.append("3. Su KDP: formato 6x9, carica il PDF come interno e il PNG come copertina.")
    r.append("4. A pubblicazione avvenuta, sposta questa cartella in `LIBRI/libri_pubblicati/`.")
    r.append("")

    return "\n".join(r)
