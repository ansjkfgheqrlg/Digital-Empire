"""
EMPIRE FLOW — evidenza calcolata per i gate umani.

Owner: Claude · Origine: FORGE (LOTTO 2 completamento Workflow Estate, CP-20260723)

## Cosa fa e cosa NON fa

Un gate `human` non diventa mai verde da solo (regola di `gate.py`, GEM-06 §3). Resta vero.
Quello che mancava è che l'umano doveva confermare **al buio**: "7/7 contattati?" senza che
nessuno gli mettesse davanti il conteggio reale. Così le conferme diventano rituali e i gate
umani si trasformano in timbri.

Questo modulo calcola l'evidenza dai dati veri e la mostra accanto al gate. **Informa la
decisione, non la prende.** Nessuna funzione qui dentro può portare un gate a GREEN.

## La guardia di provenienza (la parte che conta davvero)

Costruendo questo modulo il 23/07 ho controllato le sorgenti dei lead e ho trovato che
sul disco ci sono soltanto dati di test: `test_lead_finti.csv` ("Autosalone Test Uno",
"Via Finta 1"), `esempio_lead_5_righe.csv`, `stato_lead_test.csv`. I 61 lead reali
dichiarati in STATO-EMPIRE non esistono come file.

Un contatore ingenuo avrebbe risposto "7/7 contattati" e avrebbe fatto confermare a Max un
gate costruito su nomi inventati. Perciò ogni evidenza porta con sé un giudizio sulla
**provenienza** del dato: se la sorgente ha l'impronta di dati di prova, l'evidenza lo dice
forte, prima del numero. Un numero giusto calcolato su dati finti è più pericoloso di
nessun numero, perché ha l'aria di essere verificato.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path

from ..paths import repo_root

__all__ = ["Evidence", "compute", "provenance_warning"]

# Impronte di dati non reali. Volutamente generose: un falso allarme costa una riga di
# testo da leggere, un falso silenzio costa una decisione commerciale presa sul nulla.
_TEST_FILENAME = re.compile(r"(test|finti?|esempio|sample|demo|fake|dummy|mock)", re.IGNORECASE)
_TEST_CONTENT = re.compile(
    r"(via finta|test uno|test due|test tre|lorem ipsum|mario rossi|foo@|example\.com|"
    r"1234567|maps\.google\.com/test)", re.IGNORECASE)


@dataclass(slots=True)
class Evidence:
    label: str
    value: str
    source: str
    warning: str = ""

    def render(self) -> str:
        base = f"{self.label}: {self.value}  [fonte: {self.source}]"
        if self.warning:
            return f"!! {self.warning} !! {base}"
        return base


def provenance_warning(path: Path, text: str | None = None) -> str:
    """Ritorna una frase di allarme se la sorgente sembra contenere dati di prova."""
    reasons = []
    if _TEST_FILENAME.search(path.name):
        reasons.append(f"il nome del file ({path.name}) indica dati di prova")
    if text:
        m = _TEST_CONTENT.search(text)
        if m:
            reasons.append(f"il contenuto contiene {m.group(0)!r}")
    if not reasons:
        return ""
    return "DATI DI PROVA, NON REALI: " + " e ".join(reasons)


def _read_csv(path: Path) -> tuple[list[dict], str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    rows = list(csv.DictReader(text.splitlines()))
    return rows, text


def _cross_check(cfg: dict, rows: list[dict]) -> str:
    """Verifica che le entità di un CSV siano rintracciabili in una sorgente a monte.

    Serve contro il caso che la regex sulle impronte non sa vedere: un file di lead
    scritto a mano con nomi plausibili. Nomi credibili non rendono reale un lead — la
    sola prova che un lead esista è che provenga da qualche parte (uno scraping, un
    export, un CRM). Se le righe non si ritrovano in nessuna sorgente dichiarata,
    l'evidenza lo dice invece di far passare per verificato un elenco inventato.
    """
    pattern = cfg.get("cross_check_glob")
    key = cfg.get("key_column")
    if not pattern or not key or not rows:
        return ""
    haystack = []
    for p in repo_root().glob(pattern):
        if p.is_file():
            try:
                haystack.append(p.read_text(encoding="utf-8", errors="replace").lower())
            except OSError:
                continue
    if not haystack:
        return (f"nessuna sorgente a monte trovata ({pattern}): le righe di questo file "
                f"non sono verificabili contro nulla")
    blob = "\n".join(haystack)
    names = [(r.get(key) or "").strip() for r in rows]
    names = [n for n in names if n]
    found = [n for n in names if n.lower() in blob]
    if len(found) >= max(1, len(names) // 2):
        return ""
    return (f"tracciabilita' assente: solo {len(found)}/{len(names)} voci risultano in "
            f"una sorgente a monte ({pattern}) — righe forse inserite a mano")


def _csv_rows(cfg: dict) -> Evidence:
    rel_path = cfg.get("path", "")
    path = repo_root() / rel_path
    label = cfg.get("label", "righe")
    if not path.exists():
        return Evidence(label, "sorgente assente", rel_path,
                        warning=f"il file dichiarato non esiste: {rel_path}")

    rows, text = _read_csv(path)
    total = len(rows)
    column = cfg.get("column")

    if not column:
        counted = total
        detail = f"{counted} righe"
    else:
        empty_values = {str(v).strip().lower() for v in (cfg.get("empty_values") or [])}
        counted = 0
        for r in rows:
            val = (r.get(column) or "").strip()
            if val and val.lower() not in empty_values:
                counted += 1
        detail = f"{counted}/{total} righe con '{column}' valorizzato"

    expected = cfg.get("expected")
    if expected is not None:
        detail += f"  (atteso: {expected})"

    warning = provenance_warning(path, text) or _cross_check(cfg, rows)
    return Evidence(label, detail, rel_path, warning=warning)


def _glob(cfg: dict) -> Evidence:
    pattern = cfg.get("pattern", "")
    label = cfg.get("label", "file trovati")
    matches = sorted(repo_root().glob(pattern))
    if not matches:
        return Evidence(label, "nessun file", pattern,
                        warning=f"nessun file corrisponde a {pattern}")
    names = ", ".join(str(m.relative_to(repo_root())) for m in matches[:3])
    more = f" (+{len(matches) - 3})" if len(matches) > 3 else ""
    warning = ""
    for m in matches[:5]:
        w = provenance_warning(m)
        if w:
            warning = w
            break
    return Evidence(label, f"{len(matches)} trovati: {names}{more}", pattern, warning=warning)


def _file_contains(cfg: dict) -> Evidence:
    rel_path = cfg.get("path", "")
    needle = cfg.get("contains", "")
    label = cfg.get("label", "contenuto")
    path = repo_root() / rel_path
    if not path.exists():
        return Evidence(label, "sorgente assente", rel_path,
                        warning=f"il file dichiarato non esiste: {rel_path}")
    text = path.read_text(encoding="utf-8", errors="replace")
    found = needle in text
    return Evidence(label, "presente" if found else "ASSENTE", rel_path,
                    warning=provenance_warning(path, text))


_KINDS = {"csv_rows": _csv_rows, "glob": _glob, "file_contains": _file_contains}


def compute(spec: dict | None) -> Evidence | None:
    """Calcola l'evidenza descritta nel blocco `evidence:` di un gate.

    Un `kind` sconosciuto non solleva: ritorna un'evidenza che dichiara il problema,
    perché un errore di configurazione non deve poter far saltare la lettura dei gate.
    """
    if not spec:
        return None
    kind = spec.get("kind", "")
    fn = _KINDS.get(kind)
    if fn is None:
        return Evidence(spec.get("label", "evidenza"), "non calcolabile", kind or "(nessun kind)",
                        warning=f"tipo di evidenza sconosciuto: {kind!r}")
    try:
        return fn(spec)
    except OSError as e:
        return Evidence(spec.get("label", "evidenza"), "errore di lettura", str(spec.get("path", "")),
                        warning=str(e))
