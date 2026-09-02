"""
Scrittore: il pezzo che chiama un modello per far scrivere il testo (2026-08-30).

QUESTO MODULO RIBALTA UNA DECISIONE, E LO DICE.
Il 2026-08-15 il progetto ha archiviato tutta l'automazione che chiamava un modello
(`_archivio_automazione_modelli/`) e ha deciso: "il libro lo scrive Claude in sessione".
Quella decisione nasceva da TRE fallimenti reali, non da un capriccio:

  1. LM Arena via Playwright -> captcha, 4 volte di fila sul solo capitolo 1.
  2. Claude Code CLI + Haiku (13 ago) -> il wrapper `claude.CMD` troncava i prompt
     multiriga alla prima riga E faceva sparire `--model`, quindi si pagava un modello
     diverso da quello scelto senza accorgersene. Poi il piano ha toccato il limite di spesa.
  3. Di nuovo LM Arena -> fermato prima di ripetere la strada.

Si riprova SOLO perche' i tre guasti sono stati verificati chiusi, uno per uno, il
2026-08-30 (vedi ADR-014 e CP-20260830-001), non perche' "stavolta andra' meglio":

  * multiriga: il prompt si passa da STDIN, mai in argv. Provato: prompt di 3 righe,
    risposta esatta dalla riga 3.
  * modello: si passa l'ID ESPLICITO e si VERIFICA nella risposta quale ha girato.
    Provato che serve davvero: `--model sonnet` restituisce `claude-sonnet-4-6`,
    NON Sonnet 5. L'alias mente. E' esattamente il guasto del 13 agosto, ancora vivo.
  * spesa: `--output-format json` riporta `total_cost_usd` per chiamata, quindi il
    budget e' misurabile e c'e' un freno che ferma il flusso invece di sfondare il piano.

LE TRE LEZIONI DELL'ARCHIVIO, QUI DIVENTATE CODICE:
  1. "Un successo dichiarato non e' un successo" -> `_verifica()` guarda cosa e' ARRIVATO
     (testo non vuoto, lunghezza plausibile, modello giusto), non se il comando ha risposto 0.
  2. "Un test che non guarda il prompt non testa la scrittura" -> `Esito.prompt` conserva il
     prompt REALE inviato, cosi' i test possono affermare su quello.
  3. "I log valgono piu' della documentazione" -> ogni chiamata finisce in `chiamate.jsonl`.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

# ID ESPLICITO, MAI un alias. Verificato il 2026-08-30:
#   --model sonnet        -> claude-sonnet-4-6   (NON e' Sonnet 5)
#   --model claude-sonnet-5 -> claude-sonnet-5   (giusto)
# Scelta di Max il 2026-08-30: Sonnet 5 per il testo.
MODELLO_DEFAULT = "claude-sonnet-5"

# Il CLI usa sempre un modello piccolo per lavoro interno suo (titoli, contatori):
# vederlo nella risposta NON significa che il testo l'ha scritto lui.
MODELLI_ACCESSORI = ("claude-haiku-4-5", "claude-haiku")

TIMEOUT_DEFAULT_S = 1800          # 30 min: un blocco di capitoli e' lungo
MIN_PAROLE_PLAUSIBILI = 30        # sotto questo non e' una risposta, e' un errore educato


class BudgetSuperato(RuntimeError):
    """Il tetto di spesa e' stato raggiunto: si ferma, non si tira dritto."""


@dataclass
class Budget:
    """Il freno che il 13 agosto non c'era.

    Non e' un contatore decorativo: `verifica()` viene chiamata PRIMA di ogni chiamata
    e solleva. Un budget che si guarda solo alla fine e' un budget che non esiste.
    """
    limite_usd: float
    speso_usd: float = 0.0
    chiamate: int = 0

    def verifica(self, stima_usd: float = 0.0) -> None:
        if self.limite_usd <= 0:
            return                                   # 0 o negativo = nessun tetto
        if self.speso_usd + stima_usd >= self.limite_usd:
            raise BudgetSuperato(
                "tetto di spesa raggiunto: %.2f$ spesi su %.2f$ consentiti in %d chiamate. "
                "Il lavoro fatto finora e' salvato su disco."
                % (self.speso_usd, self.limite_usd, self.chiamate))

    def aggiungi(self, costo_usd: float) -> None:
        self.speso_usd += costo_usd
        self.chiamate += 1

    @property
    def residuo_usd(self) -> float:
        return max(0.0, self.limite_usd - self.speso_usd) if self.limite_usd > 0 else float("inf")


@dataclass
class Esito:
    """Cosa e' tornato davvero. `ok` e' False anche quando il comando esce 0 ma il
    contenuto non regge: e' il punto della lezione 1."""
    ok: bool
    testo: str = ""
    errore: str = ""
    costo_usd: float = 0.0
    durata_s: float = 0.0
    modelli: list[str] = field(default_factory=list)
    prompt: str = ""                   # il prompt REALE inviato (lezione 2)
    parole: int = 0


class ScrittoreClaudeCLI:
    """Chiama `claude -p`. Nessuna chiave API: usa le credenziali gia' presenti.

    Perche' il CLI e non l'SDK: il 2026-08-30 su questa macchina non c'erano ne'
    `ANTHROPIC_API_KEY`, ne' il pacchetto `anthropic`, ne' la CLI `ant`. Il CLI funziona
    subito. L'SDK resta la strada migliore a regime (niente tassa di harness per chiamata,
    prompt caching sul contesto ripetuto: circa un terzo del costo) ed e' il motivo per cui
    questa classe ha un'interfaccia minima — `genera()` — facile da sostituire.
    """

    def __init__(self, modello: str = MODELLO_DEFAULT, budget: Budget | None = None,
                 timeout_s: int = TIMEOUT_DEFAULT_S, log_path: Path | None = None,
                 eseguibile: str = "claude"):
        self.modello = modello
        self.budget = budget or Budget(limite_usd=0.0)
        self.timeout_s = timeout_s
        self.log_path = Path(log_path) if log_path else None
        self.eseguibile = eseguibile

    # ------------------------------------------------------------------ utilita'
    @staticmethod
    def disponibile(eseguibile: str = "claude") -> bool:
        return shutil.which(eseguibile) is not None

    def _registra(self, voce: dict) -> None:
        if not self.log_path:
            return
        try:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.log_path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(voce, ensure_ascii=False) + "\n")
        except OSError:
            pass                                     # il log non deve mai fermare il lavoro

    def _verifica(self, dati: dict, prompt: str) -> Esito:
        """Guarda COSA e' arrivato, non SE ha risposto (lezione 1 dell'archivio)."""
        costo = float(dati.get("total_cost_usd") or 0.0)
        durata = float(dati.get("duration_ms") or 0) / 1000.0
        modelli = list((dati.get("modelUsage") or {}).keys())
        testo = (dati.get("result") or "").strip()
        parole = len(testo.split())

        base = dict(costo_usd=costo, durata_s=durata, modelli=modelli,
                    prompt=prompt, testo=testo, parole=parole)

        if dati.get("is_error"):
            return Esito(ok=False, errore="il CLI ha riportato is_error=true: %s"
                                          % (dati.get("result") or "")[:200], **base)
        if not testo:
            return Esito(ok=False, errore="risposta vuota", **base)
        if parole < MIN_PAROLE_PLAUSIBILI:
            return Esito(ok=False,
                         errore="risposta di %d parole: troppo corta per essere il testo "
                                "chiesto (probabile rifiuto o errore raccontato a parole)"
                                % parole, **base)

        # Il modello richiesto ha davvero girato? E' il guasto del 13 agosto.
        sostanziali = [m for m in modelli
                       if not any(m.startswith(a) for a in MODELLI_ACCESSORI)]
        if sostanziali and not any(m.startswith(self.modello) for m in sostanziali):
            return Esito(ok=False,
                         errore="ho chiesto %s ma ha girato %s (e' il bug del 13 agosto: "
                                "il modello richiesto non e' quello usato)"
                                % (self.modello, ", ".join(sostanziali)), **base)
        return Esito(ok=True, **base)

    # ------------------------------------------------------------------ chiamata
    def genera(self, prompt: str, etichetta: str = "") -> Esito:
        """Manda il prompt e restituisce cosa e' arrivato. Non solleva per un fallimento
        del modello (torna `Esito.ok=False`); solleva solo per budget superato."""
        self.budget.verifica()

        if not self.disponibile(self.eseguibile):
            return Esito(ok=False, prompt=prompt,
                         errore="'%s' non trovato nel PATH" % self.eseguibile)

        # cwd NEUTRA: verificato il 2026-08-30 che `claude -p` lanciato dentro il monorepo
        # carica il CLAUDE.md del progetto (regole memory-first, wiki, graphify) a OGNI
        # chiamata — contesto inutile che si paga e che devia lo scrittore. Da una cartella
        # temporanea vuota non succede.
        tmp = tempfile.mkdtemp(prefix="kdp_scrittore_")
        cmd = [self.eseguibile, "-p",
               "--model", self.modello,              # ID esplicito, mai alias
               "--output-format", "json",
               "--disallowed-tools", "Bash", "Edit", "Write", "WebFetch", "WebSearch"]
        avvio = time.time()
        try:
            proc = subprocess.run(
                cmd,
                input=prompt.encode("utf-8"),        # STDIN, mai argv: bug del 13 agosto
                capture_output=True, cwd=tmp, timeout=self.timeout_s,
            )
        except subprocess.TimeoutExpired:
            esito = Esito(ok=False, prompt=prompt, durata_s=time.time() - avvio,
                          errore="timeout dopo %ds" % self.timeout_s)
            self._registra({"etichetta": etichetta, "ok": False, "errore": esito.errore})
            return esito
        except OSError as e:
            return Esito(ok=False, prompt=prompt, errore="avvio fallito: %s" % e)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

        grezzo = proc.stdout.decode("utf-8", "replace").strip()
        if not grezzo:
            err = proc.stderr.decode("utf-8", "replace").strip()[:300]
            return Esito(ok=False, prompt=prompt,
                         errore="nessun output (exit %d) %s" % (proc.returncode, err))
        try:
            dati = json.loads(grezzo)
        except json.JSONDecodeError:
            return Esito(ok=False, prompt=prompt,
                         errore="output non JSON: %s" % grezzo[:200])

        esito = self._verifica(dati, prompt)
        self.budget.aggiungi(esito.costo_usd)        # il costo si paga anche se l'esito e' no
        self._registra({
            "quando": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "etichetta": etichetta, "ok": esito.ok, "errore": esito.errore,
            "modello_chiesto": self.modello, "modelli_usati": esito.modelli,
            "costo_usd": round(esito.costo_usd, 5), "durata_s": round(esito.durata_s, 1),
            "parole": esito.parole, "speso_totale_usd": round(self.budget.speso_usd, 5),
            "prompt_caratteri": len(prompt),
        })
        return esito


class ScrittoreFinto:
    """Per i test: risponde con testo fabbricato, MA conserva i prompt ricevuti.

    Esiste apposta contro la lezione 2 dell'archivio ("un test che non guarda il prompt non
    testa la scrittura"): i test vecchi usavano un invio finto che ignorava il prompt, ed e'
    per questo che nessuno si era accorto che il capitolo 1 veniva istruito male.
    """

    def __init__(self, parole_per_risposta: int = 1700, fallisci_su: set[int] | None = None):
        self.parole_per_risposta = parole_per_risposta
        self.fallisci_su = fallisci_su or set()
        self.prompt_ricevuti: list[str] = []
        self.budget = Budget(limite_usd=0.0)
        self.modello = "finto"

    def genera(self, prompt: str, etichetta: str = "") -> Esito:
        self.prompt_ricevuti.append(prompt)
        n = len(self.prompt_ricevuti)
        if n in self.fallisci_su:
            return Esito(ok=False, prompt=prompt, errore="fallimento simulato n.%d" % n)
        testo = " ".join(["parola"] * self.parole_per_risposta)
        return Esito(ok=True, testo=testo, prompt=prompt, costo_usd=0.0,
                     parole=self.parole_per_risposta, modelli=["finto"])
