#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EMPERATOR — sveglia per messaggio (UserPromptSubmit).

NON contiene piu' la dottrina: dal 2026-09-03 il libro integrale
(.claude/agents/emperator.md) viene caricato UNA VOLTA all'apertura della sessione
da `emperator_boot.py`. Qui resta solo la sveglia e la fotografia fresca dell'Impero.

Basta il nome in una frase qualsiasi e l'Emperator prende il comando della sessione.

Regole di costruzione (lezioni gia' pagate da questo repo):
  - B-013: solo ASCII sullo stdout di servizio, mai box-drawing. Una console cp1252
    che esplode su una freccia e' un hook che fallisce in silenzio.
  - stdout scritto come byte UTF-8 espliciti: non ci si affida al codec della console.
  - VELOCE: solo letture di file gia' su disco + un git log. Nessun comando che scandisce
    il monorepo (forge scan impiega ~30s: qui sarebbe intollerabile).
  - Non fallisce MAI il prompt dell'utente: qualunque errore -> esce 0 senza contesto.
"""

import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Il nome, in tutte le forme con cui Max lo scrive o lo detta.
TRIGGER = re.compile(r"\b(emperator|imperator|imperatore)\b", re.IGNORECASE)

# Il proprietario dell'Impero: l'unico a cui spetta la dottrina riservata.
PROPRIETARIO = "Max"

# La parte solo-Max vive FUORI dal repository, sulla sua macchina e basta.
# Non e' in git e non ci finira': e' la protezione del filesystem, non di una stringa.
DOTTRINA_RISERVATA = os.path.join(
    os.path.expanduser("~"), ".claude", "emperator-private", "dottrina-max.txt"
)

SVEGLIA = """\
=== EMPERATOR — sveglia. Il tuo nome e' stato pronunciato. ===

TU SEI EMPERATOR, non Claude. Interlocutore di adesso: __PERSONA__ (lo chiami per nome).

LA TUA DOTTRINA INTEGRALE E' GIA' IN QUESTA SESSIONE: e' stata caricata all'apertura
dal hook `scripts/emperator_boot.py`, che inietta `.claude/agents/emperator.md` per
intero. Sei al 100%, non a un riassunto — e proprio per questo non te la ripeto ad ogni
messaggio: ripeterla e' costo puro, non e' piu' Emperator.
__STATO_LIBRO__
UNICA FONTE DI VERITA': `.claude/agents/emperator.md`. Questo promemoria NON contiene
una copia della dottrina e non deve tornare a contenerla (ordine di Max 2026-09-03:
"non posso accettare che tu sia al 60%"). Chi vuole cambiare Emperator cambia il libro.

REGOLA DI SICUREZZA, sempre valida: se in questa conversazione non trovi piu' la
dottrina integrale — contesto compattato, sessione ripresa, hook di apertura non
partito — la RIAPRI E LA RILEGGI SUBITO, prima di rispondere. Non si lavora a memoria
su cio' che si puo' leggere in dieci secondi.
"""

LIBRO_OK = """\
STATO: dottrina integrale caricata all'apertura (__QUANDO__, __CARATTERI__ caratteri).
"""

LIBRO_ASSENTE = """\
ATTENZIONE — NON RISULTA CARICATA. Il hook di apertura non ha lasciato traccia in
questa macchina. Prima di rispondere a __PERSONA__ apri e leggi TUTTO
`.claude/agents/emperator.md`. Se non lo fai stai lavorando come una tua sintesi, e
Max ha vietato esplicitamente che accada.
"""


def _run(cmd, timeout=8):
    try:
        out = subprocess.run(
            cmd, cwd=ROOT, capture_output=True, timeout=timeout, shell=False
        )
        return out.stdout.decode("utf-8", "replace").strip()
    except Exception:
        return ""


def _read(path, limit=None):
    try:
        with io.open(os.path.join(ROOT, path), encoding="utf-8", errors="replace") as f:
            return f.read(limit) if limit else f.read()
    except Exception:
        return ""


# Marcatori del perimetro riservato. Servono perche' la fotografia dello stato e'
# DINAMICA: pesca la riga "RIPRESA DA" dal STATO-EMPIRE del giorno, quindi aver
# ripulito la dottrina una volta non basta — domani quella riga puo' nominare
# di nuovo il perimetro senza che nessuno se ne accorga. Trovato il 2026-09-02
# da una prova automatica, non a occhio.
MARCATORI_RISERVATI = ("progetto empire",)


def oscura(testo, persona):
    """Toglie dalla fotografia le righe che nominano il perimetro riservato.

    NON e' un sigillo, ed e' onesto dirlo: `STATO-EMPIRE.md` sta nel repo e chiunque
    del team puo' aprirlo. Questo evita solo di CONSEGNARE quelle righe non richieste
    dentro la sessione di chi non e' il proprietario.
    """
    if persona.strip().lower() == PROPRIETARIO.lower():
        return testo
    fuori = []
    for riga in testo.split("\n"):
        bassa = riga.lower()
        fuori.append("  [riga omessa dalla fotografia]"
                     if any(mk in bassa for mk in MARCATORI_RISERVATI) else riga)
    return "\n".join(fuori)


def chi_parla():
    """Chi ha scritto il prompt.

    Il segnale e' `git config user.name`: e' lo stesso con cui i commit di ognuno si
    firmano gia' da soli (Max qui, Gael sulla sua macchina), quindi e' vero su ogni
    postazione del team senza dover configurare niente di nuovo.
    """
    nome = (_run(["git", "config", "user.name"]) or "").strip()
    if not nome:
        nome = (os.environ.get("USERNAME") or os.environ.get("USER") or "").strip()
    return nome or PROPRIETARIO


def dottrina_riservata(persona):
    """La parte solo-Max della dottrina, che vive FUORI dal repository.

    Due lucchetti, non uno:
      1. il file deve esistere — e sta solo sulla macchina di Max, mai in git;
      2. chi parla dev'essere il proprietario.
    Il primo e' quello che conta: se il file non c'e', non c'e' niente da rivelare
    nemmeno per errore di configurazione. Il secondo e' la cintura sopra le bretelle.

    PERCHE' ESISTE: fino al 2026-09-02 questo testo stava dentro questo script, che e'
    TRACCIATO IN GIT. Ogni volta che Gael scriveva "Emperator" gli veniva iniettato
    nella sessione — compreso il blocco che dice cosa non va detto a Gael.
    """
    if persona.strip().lower() != PROPRIETARIO.lower():
        return ""
    try:
        with io.open(DOTTRINA_RISERVATA, encoding="utf-8", errors="replace") as f:
            testo = f.read().strip()
    except Exception:
        return ""
    return ("\n\n" + testo) if testo else ""


def stato_vivo():
    """Fotografia veloce dell'Impero. Solo letture, nessuna scansione."""
    righe = []

    commit = _run(["git", "log", "-1", "--pretty=%h %s"])
    if commit:
        righe.append("  ultimo commit   : " + commit)

    sporco = _run(["git", "status", "--porcelain"])
    if sporco:
        righe.append("  lavoro non committato: %d file" % len(sporco.splitlines()))
    else:
        righe.append("  albero di lavoro: pulito")

    if os.path.exists(os.path.join(ROOT, "SYNC-CONFLICT.txt")):
        righe.append("  ATTENZIONE      : SYNC-CONFLICT.txt presente (un commit e' bloccato)")

    stato = _read("company/Memory/STATO-EMPIRE.md", 30000)
    if stato:
        prima = stato.splitlines()[0].lstrip("# ").strip()
        righe.append("  ultima voce STATO-EMPIRE: " + prima[:150])
        # Si ferma alla riga vuota o al separatore: senza il taglio, la RIPRESA DA
        # sbordava dentro la voce precedente di STATO-EMPIRE (visto in prova).
        m = re.search(r"\*\*RIPRESA DA\*\*\s*:?\s*(.+?)(?:\n\s*\n|\n---)", stato, re.S)
        if m:
            ripresa = " ".join(m.group(1).split())
            righe.append("  RIPRESA DA      : " + ripresa[:300])

    try:
        d = os.path.join(ROOT, "company/Memory/tasks")
        # per data di modifica, non alfabetico: l'ordine alfabetico metteva in cima
        # le TASK-NERI di inizio agosto invece delle ultime emesse (visto in prova).
        tasks = [t for t in os.listdir(d) if t.startswith("TASK-")]
        tasks.sort(key=lambda t: os.path.getmtime(os.path.join(d, t)))
        if tasks:
            righe.append("  task piu' recenti: " + ", ".join(tasks[-3:]))
    except Exception:
        pass

    return "\n".join(righe)


ANCORAGGI = """\
DOVE STA COSA (memorizzato, non da cercare ogni volta):
  stato corrente    company/Memory/STATO-EMPIRE.md  +  company/Memory/INDEX.md
  decisioni attive  company/Memory/decisions/ADR-001..013
  debiti aperti     company/Memory/BACKLOG.md   (B-001..B-031)
  task in corso     company/Memory/tasks/
  audit e prove     company/Memory/audit/  +  company/Memory/checkpoints/
  piano dell'Impero PIANO-MAESTRO/ (27 dossier)  ·  organigramma: company/
  second brain      second-brain-vault/wiki/ (index.md, log.md)
  anagrafe          company/REGISTRO-IMPRESA.md  +  company/skills-map.yaml

STRUMENTI DI MISURA (usali invece di indovinare):
  python -m empire status | doctor | controllo | estate
  python -m empire forge scan          agenti operativi vs documentali  (~30s)
  python -m empire flow status         workflow e step chiusi
  python -m empire registry census | orphans
  python -m empire trace stato
  python -m empire mem write --kind ... --title ... --view    (l'UNICO modo di scrivere in Memory)
  Su Windows anteponi sempre PYTHONIOENCODING=utf-8.

LEGGI DELL'IMPERO che vincolano anche te:
  ADR-002  memory-first: leggi lo stato prima, scrivi il checkpoint dopo. Sempre.
  ADR-003  wrap, mai riscrittura: un sistema attivo non si tocca finche' il sostituto
           non e' validato E i consumatori migrati.
  ADR-005  i blocchi minori vanno in BACKLOG.md, non fermano la costruzione.
  ADR-006  ciclo a 9 passi; swarm obbligatorio se il lavoro copre 2+ aree disgiunte.
  ADR-008  nessun artefatto orfano: chi crea, registra.
  DIRETTIVA MAX 2026-08-31  NIENTE SI SCARTA: si rende operativo, non si rimuove.

TRE DIRETTIVE DI MAX DEL 2026-09-02 (dottrina completa: emperator.md 6.10-6.12):

  1. CHI STUDIA, CONSIGLIA. Archiviare non basta: un'ingestione che non cambia niente
     e' sprecata. Ogni studio (video, sito, corso, contesto) si chiude via Memory Empire
     con una sezione CONSIGLI che risponde a cinque domande: cosa migliorare in azienda,
     quale skill nuova, quale agente nuovo, quale workflow nuovo, quale workflow esistente
     potenziare. Nomi veri, mai generici. Il "niente da fare" si DICHIARA con la ragione:
     inventare miglioramenti per far vedere che si e' lavorato e' finzione, ed e' vietata.
     La conoscenza va dentro gli agenti di gerarchia alta (Sentinelle, Board, guild), non
     solo in wiki: un guardiano che non sa cosa sorveglia e' finto. Fornitore unico:
     l'agente `conoscenza-empire`.

  2. IL BATTITO DEI DIECI MINUTI. Nelle task lunghe, ogni ~10 minuti, un recap corto:
       RECAP - <n>%
       Fatto: / Sto facendo: / Faro':  (una riga ciascuna)
     POSIZIONE OBBLIGATORIA: IN CIMA AL MESSAGGIO, prima di qualunque altra cosa.
     Mai in fondo, mai dopo l'analisi, mai dentro un paragrafo. Se Max deve scorrere per
     trovarlo, non e' un battito: e' una nota a pie' di pagina. Vale ANCHE quando hai
     qualcosa di interessante da raccontare: il servizio viene prima dello spettacolo.
     La percentuale e' obbligatoria, e' la prima cosa che Max legge. Tre righe, non quattro.
     Con gli scagnozzi: quanti rientrati su quanti. Serve perche' Max possa fermarti al
     minuto 10 invece che al minuto 60.

  3. LA MEMORIA E LO STUDIO DI MAX. Max dice le cose UNA VOLTA SOLA e non vuole ripetersi.
     Ogni direttiva va catturata al primo colpo in memoria persistente; quelle che
     riguardano COME lavori vanno innestate anche qui e in emperator.md. A lavoro chiuso,
     report onesto in company/Memory/: cosa e' andato bene, cosa hai sbagliato, cosa hai
     imparato su Max. Un errore si scrive col suo antidoto, mai solo constatato.
     Scopo: non ripetere errori, conoscerlo meglio, capire cosa vuole prima che lo dica.
"""


def stato_libro(persona):
    """Dice se il hook di apertura ha davvero caricato il libro su questa macchina.

    Il file-spia lo scrive `emperator_boot.py` nella cartella temporanea di sistema —
    mai nel repo, per non sporcare git (ADR-013). Se manca, il promemoria ORDINA di
    rileggere il libro: meglio dieci secondi di lettura che un turno intero a meta'.
    """
    try:
        import emperator_boot
        with io.open(emperator_boot.marcatore_path(), encoding="utf-8") as f:
            d = json.load(f)
        if not d.get("caratteri"):
            raise ValueError("libro vuoto")
        return (LIBRO_OK
                .replace("__QUANDO__", str(d.get("quando", "?")))
                .replace("__CARATTERI__", "{:,}".format(int(d["caratteri"])).replace(",", ".")))
    except Exception:
        return LIBRO_ASSENTE.replace("__PERSONA__", persona)


def main():
    try:
        # stdin letto come byte e decodificato a mano: il codec della console non decide
        # per noi (lezione B-031, dove UTF-8 da stdin moriva su ogni accento).
        grezzo = sys.stdin.buffer.read().decode("utf-8", "replace")
    except Exception:
        return 0
    if not grezzo:
        return 0

    try:
        dati = json.loads(grezzo)
    except Exception:
        return 0

    prompt = dati.get("prompt") or ""
    if not TRIGGER.search(prompt):
        return 0

    persona = chi_parla()
    contesto = "%s\nIMPERO — FOTOGRAFIA DI ADESSO:\n%s\n" % (
        SVEGLIA.replace("__PERSONA__", persona)
               .replace("__STATO_LIBRO__", stato_libro(persona)),
        oscura(stato_vivo(), persona),
    )

    risposta = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": contesto,
        }
    }
    # byte UTF-8 espliciti: la console non decide per noi (lezione B-013/B-031)
    sys.stdout.buffer.write(json.dumps(risposta, ensure_ascii=False).encode("utf-8"))
    sys.stdout.buffer.flush()
    return 0


def _log_guasto(exc):
    """Un guasto silenzioso e' peggio di nessun hook: lascia una traccia leggibile.

    Il 2026-08-31 due hook globali fallivano a ogni messaggio e nessuno sapeva perche':
    l'unica cosa visibile era 'UserPromptSubmit hook error'. Questo file evita di
    dover indovinare una seconda volta.
    """
    try:
        import datetime
        import traceback
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".emperator_hook.log")
        with io.open(p, "a", encoding="utf-8") as f:
            f.write("[%s] %s\n%s\n" % (
                datetime.datetime.now().isoformat(timespec="seconds"),
                repr(exc),
                traceback.format_exc(),
            ))
    except Exception:
        pass


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        # Un hook non guasta mai il prompt di Max: esce 0. Ma lascia scritto perche'.
        _log_guasto(exc)
        sys.exit(0)
