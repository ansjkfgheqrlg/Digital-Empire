# -*- coding: utf-8 -*-
"""verifica_fatti.py — confronta in codice i fatti fra la fonte e lo script riscritto.

REGOLA CHE LO ORDINA: A4-RC-02 (company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/
RIPASSO_COSTRUTTIVO.py). E' `verifica_originalita` (regolatori.py:153) applicata al CONTENUTO
invece che alla FORMA: quella funzione misura solo se il testo e' troppo SIMILE alla fonte, e
davanti a un fatto storpiato da' via libera (una data spostata RIDUCE la sovrapposizione
letterale, non la aumenta). Qui si estraggono le entita' — nomi propri, date/durate, cifre,
citazioni fra virgolette, relazioni — dalla fonte e dallo script, e si confrontano.

IL BUCO CHE CHIUDE, misurato il 2026-09-05 su tutta la fabbrica (script-writer.md §8): cercato
*fact-check*, *verifica dei fatti*, *controllo dei fatti* su ogni .md e .py — zero risultati.
L'unico presidio era prosa letta da un umano prima di consegnare lo script. Il 2026-09-10 e'
nato l'agente `03-AGENTI-E-RUOLI/regolatori/regolatore-fatti.md`, che cita esplicitamente
QUESTO script come "non esiste ancora" e resta il verdetto umano finche' non esiste.

NON E' ANCORA AGGANCIATO. Nessun file della catena di produzione importa questo modulo (ADR-029,
binario B: si applica solo al gate di categoria). Chi lo agganciera' lo trova pronto qui: la
funzione `verifica_fatti(script, sorgente, fonti_extra="")` e' importabile e ricalca la firma e
lo stile di ritorno di `regolatori.verifica_originalita` (dict con chiave "esito": "passa" o
"BLOCCO"), senza importare ne' modificare regolatori.py.

LIMITE DICHIARATO (nello stesso spirito di `_elementi_nuovi` in regolatori.py): questa e' una
misura approssimata. Per date/cifre il confronto e' per CONTESTO (le parole intorno al numero),
quindi affidabile a rilevare un'alterazione mantenendo intorno lo stesso testo. Per nomi propri,
citazioni e relazioni il confronto e' per somiglianza fuzzy (difflib): un'entita' MAI vista nella
fonte (nessuna somiglianza) e' segnalata come "non_verificabile" ma NON BLOCCA da sola — bloccare
ogni nome non ritrovato letteralmente produrrebbe troppi falsi positivi su un testo riscritto per
essere utile. Solo una "discordanza" con evidenza diretta (stesso contesto/entita' simile, valore
diverso) genera BLOCCO. Il taglio dei fatti "non verificabili" resta decisione umana
(regolatore-fatti / capo-copy), come dichiarato nell'agente stesso.

USO
    python verifica_fatti.py --aiuto
    python verifica_fatti.py --script script-adattati/mkaNzHTBw1M.md --sorgente transcripts/dosementale-mkaNzHTBw1M.it.vtt
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    sys.stderr.reconfigure(encoding="utf-8", line_buffering=True)


# --------------------------------------------------------------------------------------
# Convenzioni copiate da regolatori.py (letto, non modificato): stessa forma di ritorno.
# --------------------------------------------------------------------------------------
def _esito(regolatore: str, passa: bool, motivo: str, **dettagli) -> dict:
    return {"regolatore": regolatore, "esito": "passa" if passa else "BLOCCO",
            "motivo": motivo, **dettagli}


# --------------------------------------------------------------------------------------
# Estrazione entita' — cinque famiglie di script-writer.md §8 / regolatore-fatti.md
# --------------------------------------------------------------------------------------
_TOKEN_RE = re.compile(r"[A-Za-zÀ-ÿ]+|\d{1,4}(?:[.,]\d+)?")
_NUM_RE = re.compile(r"^\d{1,4}(?:[.,]\d+)?$")

_NOME_PROPRIO_RE = re.compile(
    r"\b[A-ZÀ-Ú][a-zà-ù]+(?:\s+[A-ZÀ-Ú][a-zà-ù]+){0,2}\b"
)
# Parole che iniziano frase/periodo: se un "nome proprio" comincia con una di queste, e' quasi
# certamente un falso positivo dell'euristica (maiuscola di inizio frase, non un nome).
_PAROLE_NON_NOME = {
    "Il", "La", "Lo", "Gli", "Le", "Un", "Una", "Uno", "Ma", "E", "Ed", "Poi", "Quando",
    "Dopo", "Prima", "Cosa", "Come", "Perché", "Perche", "Infatti", "Tuttavia", "Inoltre",
    "Oggi", "Ieri", "Domani", "Anche", "Questo", "Questa", "Quello", "Quella", "Nel", "Nella",
    "Del", "Della", "Dei", "Delle", "In", "Su", "Per", "Con", "Se", "Non", "Ecco", "Insomma",
}

_CITAZIONE_RE = re.compile(r'[«"“]([^»"”]{4,240})[»"”]')

_RELAZIONE_RE = re.compile(
    r"\b(il figlio di|la figlia di|il marito di|la moglie di|il padre di|la madre di|"
    r"il fratello di|la sorella di|nipote di|cugino di|cugina di)\s+"
    r"([A-ZÀ-Ú][a-zà-ùA-ZÀ-Ú' ]{2,40}?)(?=[,.;:\n]|$)",
    re.IGNORECASE,
)


def _tokenizza(testo: str) -> list[str]:
    return _TOKEN_RE.findall(testo or "")


def estrai_fatti(testo: str) -> dict:
    """Elenco grezzo delle entita' trovate in un testo, per famiglia."""
    testo = testo or ""
    nomi = sorted({
        m.group(0) for m in _NOME_PROPRIO_RE.finditer(testo)
        if m.group(0).split()[0] not in _PAROLE_NON_NOME
    })
    citazioni = [m.group(1).strip() for m in _CITAZIONE_RE.finditer(testo)]
    relazioni = [(m.group(1).lower(), m.group(2).strip()) for m in _RELAZIONE_RE.finditer(testo)]
    return {"nomi_propri": nomi, "citazioni": citazioni, "relazioni": relazioni}


# --------------------------------------------------------------------------------------
# Confronto cifre/date per CONTESTO — il cuore della misura richiesta ("una data alterata")
# --------------------------------------------------------------------------------------
def _mappa_contesto_numeri(tokens: list[str], finestra: int = 2) -> dict[tuple, set]:
    """Per ogni numero trovato, la chiave e' il contesto (parole intorno, minuscole) con un
    segnaposto al posto del numero. Serve a ritrovare "lo stesso punto del discorso" anche se
    il numero e' cambiato."""
    mappa: dict[tuple, set] = {}
    for i, tok in enumerate(tokens):
        if not _NUM_RE.match(tok):
            continue
        prima = tuple(t.lower() for t in tokens[max(0, i - finestra):i])
        dopo = tuple(t.lower() for t in tokens[i + 1:i + 1 + finestra])
        chiave = prima + ("<NUM>",) + dopo
        mappa.setdefault(chiave, set()).add(tok)
    return mappa


def _confronta_numeri(tok_script: list[str], tok_fonte: list[str]) -> list[dict]:
    mappa_fonte = _mappa_contesto_numeri(tok_fonte)
    risultati, viste = [], set()
    for i, tok in enumerate(tok_script):
        if not _NUM_RE.match(tok):
            continue
        prima = tuple(t.lower() for t in tok_script[max(0, i - 2):i])
        dopo = tuple(t.lower() for t in tok_script[i + 1:i + 3])
        chiave = prima + ("<NUM>",) + dopo
        if (chiave, tok) in viste:
            continue
        viste.add((chiave, tok))

        valori_fonte = mappa_fonte.get(chiave)
        if valori_fonte is None:
            # contesto ridotto: tollera piccole riscritture intorno al numero
            chiave_corta_dopo = (prima[-1:] if prima else ()) + ("<NUM>",) + (dopo[:1] if dopo else ())
            chiave_corta_prima = (prima[-1:] if prima else ()) + ("<NUM>",)
            for k, vals in mappa_fonte.items():
                if k[-len(chiave_corta_dopo):] == chiave_corta_dopo and chiave_corta_dopo != ("<NUM>",):
                    valori_fonte = vals
                    break
                if k[:len(chiave_corta_prima)] == chiave_corta_prima and chiave_corta_prima != ("<NUM>",):
                    valori_fonte = vals
                    break

        if valori_fonte is None:
            risultati.append({"famiglia": "cifre_date", "valore": tok, "esito": "non_verificabile"})
        elif tok in valori_fonte:
            risultati.append({"famiglia": "cifre_date", "valore": tok, "esito": "coerente"})
        else:
            risultati.append({
                "famiglia": "cifre_date", "valore": tok, "esito": "discordante",
                "dettaglio": f"nella fonte, lo stesso punto del discorso ha: {', '.join(sorted(valori_fonte))}",
            })
    return risultati


# --------------------------------------------------------------------------------------
# Confronto fuzzy per nomi/citazioni/relazioni
# --------------------------------------------------------------------------------------
def _finestre(testo: str, n_parole: int) -> list[str]:
    parole = testo.split()
    n_parole = max(n_parole, 1)
    return [" ".join(parole[i:i + n_parole]) for i in range(max(len(parole) - n_parole + 1, 0))]


def _verifica_fuzzy(valore: str, fonte_testo: str, soglia_discordanza: float = 0.6) -> tuple[str, float, str | None]:
    v = " ".join((valore or "").split()).strip()
    if not v:
        return "non_verificabile", 0.0, None
    fonte_norm = " ".join((fonte_testo or "").split())
    if v.lower() in fonte_norm.lower():
        return "coerente", 1.0, None
    migliore, punteggio = None, 0.0
    for finestra in _finestre(fonte_norm, len(v.split())):
        r = difflib.SequenceMatcher(None, v.lower(), finestra.lower()).ratio()
        if r > punteggio:
            punteggio, migliore = r, finestra
    if punteggio >= soglia_discordanza:
        return "discordante", punteggio, migliore
    return "non_verificabile", punteggio, None


# --------------------------------------------------------------------------------------
# Funzione principale — importabile
# --------------------------------------------------------------------------------------
def verifica_fatti(script: str, sorgente: str, fonti_extra: str = "") -> dict:
    """Confronta i fatti riportati in `script` con quelli disponibili in `sorgente`
    (+ `fonti_extra` opzionali). Ritorna un dict nello stile di regolatori.esito().

    BLOCCO solo se esiste almeno una discordanza con evidenza diretta (stesso contesto/entita'
    simile, valore diverso). I fatti "non_verificabili" sono riportati in `note` ma non
    bloccano da soli (vedi limite dichiarato in cima al file)."""
    fonte_completa = "\n".join(t for t in (sorgente or "", fonti_extra or "") if t)

    fatti_script = estrai_fatti(script)
    tok_script = _tokenizza(script)
    tok_fonte = _tokenizza(fonte_completa)

    risultati = _confronta_numeri(tok_script, tok_fonte)

    for nome in fatti_script["nomi_propri"]:
        esito_f, punteggio, simile = _verifica_fuzzy(nome, fonte_completa)
        voce = {"famiglia": "nomi_propri", "valore": nome, "esito": esito_f}
        if simile:
            voce["trovato_in_fonte"] = simile
        risultati.append(voce)

    for citazione in fatti_script["citazioni"]:
        # Regola dura sulle virgolette (script-writer.md §8): anche una somiglianza alta ma non
        # identica e' discordanza, mai un'approssimazione accettata.
        esito_f, punteggio, simile = _verifica_fuzzy(citazione, fonte_completa, soglia_discordanza=0.5)
        voce = {"famiglia": "citazioni", "valore": citazione, "esito": esito_f}
        if simile:
            voce["trovato_in_fonte"] = simile
        risultati.append(voce)

    for tipo, nome in fatti_script["relazioni"]:
        valore = f"{tipo} {nome}"
        esito_f, punteggio, simile = _verifica_fuzzy(valore, fonte_completa)
        voce = {"famiglia": "relazioni", "valore": valore, "esito": esito_f}
        if simile:
            voce["trovato_in_fonte"] = simile
        risultati.append(voce)

    discordanti = [r for r in risultati if r["esito"] == "discordante"]
    non_verificabili = [r for r in risultati if r["esito"] == "non_verificabile"]
    coerenti = [r for r in risultati if r["esito"] == "coerente"]
    conteggio = {"coerenti": len(coerenti), "discordanti": len(discordanti),
                 "non_verificabili": len(non_verificabili)}

    if discordanti:
        return _esito(
            "verifica-fatti", False,
            f"Trovate {len(discordanti)} discordanze fra script e fonte: un fatto riportato "
            f"e' diverso da come compare nella fonte.",
            fatti=risultati, discordanze=discordanti, conteggio=conteggio,
        )

    nota = (f"{len(non_verificabili)} fatti non trovati in nessuna fonte: non bloccano da soli, "
            f"vanno mostrati a un umano (regolatore-fatti / capo-copy) prima della firma."
            if non_verificabili else "")
    return _esito(
        "verifica-fatti", True,
        f"Nessuna discordanza diretta trovata ({conteggio['coerenti']} fatti coerenti, "
        f"{conteggio['non_verificabili']} non verificabili).",
        fatti=risultati, discordanze=[], conteggio=conteggio, nota=nota,
    )


# --------------------------------------------------------------------------------------
def _leggi(percorso: str) -> str:
    with open(percorso, encoding="utf-8") as f:
        return f.read()


def main() -> int:
    ap = argparse.ArgumentParser(
        add_help=False,
        description="Confronta i fatti (nomi, date, cifre, citazioni, relazioni) fra uno "
                    "script riscritto e la sua fonte. A4-RC-02 — non ancora agganciato al gate.",
    )
    ap.add_argument("--aiuto", "-h", action="help", help="mostra questo aiuto ed esce")
    ap.add_argument("--script", required=True, help="percorso dello script riscritto (.md/.txt)")
    ap.add_argument("--sorgente", required=True, help="percorso del transcript/fonte originale")
    ap.add_argument("--fonti-extra", default=None, help="percorso di fonti esterne aggiuntive (opzionale)")
    ap.add_argument("--json", action="store_true", help="stampa il risultato come JSON invece che a righe")
    args = ap.parse_args()

    for percorso, etichetta in ((args.script, "script"), (args.sorgente, "sorgente")):
        if not os.path.exists(percorso):
            print(f"[!] File {etichetta} inesistente: {percorso}")
            return 1

    script_testo = _leggi(args.script)
    sorgente_testo = _leggi(args.sorgente)
    fonti_extra_testo = _leggi(args.fonti_extra) if args.fonti_extra and os.path.exists(args.fonti_extra) else ""

    risultato = verifica_fatti(script_testo, sorgente_testo, fonti_extra_testo)

    if args.json:
        print(json.dumps(risultato, ensure_ascii=False, indent=2))
    else:
        simbolo = "[OK]" if risultato["esito"] == "passa" else "[BLOCCO]"
        print(f"{simbolo} {risultato['regolatore']} — {risultato['motivo']}")
        for d in risultato.get("discordanze", []):
            print(f"      · {d['famiglia']}: '{d['valore']}' — {d.get('dettaglio', '')}")
        conteggio = risultato.get("conteggio", {})
        print(f"      conteggio: {conteggio}")
        if risultato.get("nota"):
            print(f"      nota: {risultato['nota']}")

    return 1 if risultato["esito"] == "BLOCCO" else 0


if __name__ == "__main__":
    sys.exit(main())
