"""
EMPIRE FORGE — misura quanto un agente e' OPERATIVO invece che documentale.

Owner: Claude · Origine: FORGE (PEZZO 1 del refinement APEX-7, CP-20260724)

## Il problema, con le parole di Max

    "Agenti, skill, flussi di lavoro sono tutti in markdown e vanno trasformati in
     agenti operativi, vere skill operative, non tanto di reference."

E dalla sua autocritica APEX-7:

    "AGENTI: definiti per nome ma non per COMPORTAMENTO. Nessun prompt interno definito.
     Nessun criterio di successo per agente. Nessuna gestione degli stati interni."

Misurato: **441 agenti**, tutti file `.md` ben scritti (Ruolo, Input, Output) e **nessuno
eseguibile**. Sono ottime schede di un personale che non lavora.

## Perche' questo modulo viene PRIMA di riscrivere gli agenti

Max ha chiesto di migliorarli "uno per uno, in checklist". Giusto — ma senza una misura,
"uno per uno" e' un ordine casuale: si finisce per lavorare sui primi in ordine alfabetico
invece che sui piu' rotti. Questo modulo produce la checklist ORDINATA per gravita', e
soprattutto rende il progresso **verificabile**: si vede il punteggio salire.

E' lo stesso principio che ha retto tutto il resto oggi: prima misurare, poi agire.

## I 6 criteri di operativita'

Non inventati: sono i buchi che Max ha elencato nella sua autocritica, resi verificabili.

    C1 IDENTITA'    ha un id stabile                        -> lo si puo' invocare
    C2 RUOLO UNICO  una sola responsabilita' dichiarata     -> non si sovrappone ad altri
    C3 INGRESSO     dice cosa gli serve per lavorare        -> lo si puo' alimentare
    C4 USCITA       dice cosa produce e dove                -> il lavoro e' verificabile
    C5 SUCCESSO     ha un criterio di riuscita o un gate    -> si sa se ha fatto bene
    C6 COMPORTAMENTO ha istruzioni operative eseguibili     -> sa COME farlo, non solo cosa

C6 e' il piu' importante e il piu' assente: e' la differenza fra una scheda e un agente.
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .paths import repo_root

__all__ = ["Criterio", "Scheda", "CRITERI", "analizza", "checklist", "salva_checklist"]

# Un criterio e' soddisfatto se il testo contiene una di queste marche.
# Volutamente generose: il falso positivo costa una riga da rileggere, il falso negativo
# manda a riscrivere un agente che andava bene.
CRITERI: dict[str, tuple[str, list[str]]] = {
    "C1-identita": ("ha un id stabile con cui invocarlo", [
        r"^\s*[-*]?\s*\*\*ID\*\*\s*[:=]", r"^\s*id\s*[:=]", r"`[a-z0-9][a-z0-9-]{3,}`"]),
    "C2-ruolo": ("una sola responsabilita' dichiarata", [
        r"##\s*Ruolo", r"\*\*Ruolo\*\*", r"^\s*Tipo\s*[:=]", r"##\s*Identit[aà]"]),
    "C3-ingresso": ("dice cosa gli serve per lavorare", [
        r"##\s*Input", r"\*\*Input\*\*", r"##\s*Ingress", r"\bINPUT\s*[:=]"]),
    "C4-uscita": ("dice cosa produce e dove", [
        r"##\s*Output", r"\*\*Output\*\*", r"##\s*Uscit", r"\bOUTPUT\s*[:=]",
        r"##\s*Artefatt"]),
    "C5-successo": ("ha un criterio di riuscita o un gate", [
        r"##\s*(Gate|Criteri|Successo|Definition of Done|DoD|Verifica|QA)",
        r"\bgate\b", r"\bcriteri[oi] di (successo|riuscita)", r"\bDoD\b",
        r"\bsoglia\b", r"\bthreshold\b"]),
    "C6-comportamento": ("ha istruzioni operative eseguibili, non solo descrittive", [
        r"##\s*(Prompt|Procedura|Algoritmo|Come lavora|Passi|Step|Esecuzione|Regole ferree)",
        r"```(bash|python|yaml|json|sh)", r"^\s*\d+\.\s+\*\*[A-Z]",
        r"\bSTEP \d", r"\bstate machine\b"]),
}

_SEVERITA = {"C6-comportamento": 3, "C5-successo": 2, "C4-uscita": 2,
             "C3-ingresso": 1, "C2-ruolo": 1, "C1-identita": 1}


@dataclass(slots=True)
class Criterio:
    nome: str
    descrizione: str
    passa: bool
    prova: str = ""


@dataclass(slots=True)
class Scheda:
    id: str
    percorso: str
    righe: int
    criteri: list[Criterio] = field(default_factory=list)

    @property
    def punteggio(self) -> float:
        if not self.criteri:
            return 0.0
        return round(sum(1 for c in self.criteri if c.passa) / len(self.criteri) * 10, 1)

    @property
    def mancanti(self) -> list[str]:
        return [c.nome for c in self.criteri if not c.passa]

    @property
    def gravita(self) -> int:
        """Quanto e' urgente sistemarlo. Pesa i criteri: mancare il COMPORTAMENTO
        e' molto peggio che mancare l'id."""
        return sum(_SEVERITA.get(n, 1) for n in self.mancanti)

    @property
    def stato(self) -> str:
        if self.punteggio >= 9:
            return "OPERATIVO"
        if self.punteggio >= 6:
            return "PARZIALE"
        return "DOCUMENTALE"


def analizza(percorso: Path) -> Scheda:
    """Misura un singolo file agente. Non lo modifica mai."""
    try:
        testo = percorso.read_text(encoding="utf-8", errors="replace")
    except OSError:
        testo = ""

    criteri: list[Criterio] = []
    for nome, (descr, patterns) in CRITERI.items():
        prova = ""
        for p in patterns:
            m = re.search(p, testo, re.IGNORECASE | re.MULTILINE)
            if m:
                prova = m.group(0).strip()[:60]
                break
        criteri.append(Criterio(nome=nome, descrizione=descr, passa=bool(prova), prova=prova))

    return Scheda(
        id=percorso.stem,
        percorso=str(percorso.relative_to(repo_root())).replace("\\", "/"),
        righe=len(testo.splitlines()),
        criteri=criteri,
    )


# File di CORREDO di un agente (non sono agenti a se': valutarli come tali produce falsi
# 0/10 che sporcano la checklist — trovato nel PEZZO 1 con evals.md e failure-modes.md).
_CORREDO = {"evals", "failure-modes", "failure_modes", "readme", "catalog", "index",
            "changelog", "license", "note", "notes", "todo"}


def _file_agenti() -> list[Path]:
    """Riusa la scoperta gia' esistente del loader invece di reinventarla,
    poi scarta i file di corredo che non sono agenti veri."""
    try:
        from .loader import _agent_files  # noqa: PLC0415
        files = list(_agent_files())
    except (ImportError, AttributeError):
        files = sorted((repo_root() / "company").rglob("*.md"))
    return [p for p in files if p.stem.lower() not in _CORREDO]


def checklist(limite: int | None = None) -> list[Scheda]:
    """La checklist ordinata per gravita': i piu' rotti in cima.

    E' la risposta alla richiesta di Max ("uno per uno, in checklist"): dice da quale
    cominciare, invece di lasciarlo all'ordine alfabetico.
    """
    schede = [analizza(p) for p in _file_agenti()]
    schede.sort(key=lambda s: (-s.gravita, s.punteggio, s.id))
    return schede[:limite] if limite else schede


def salva_checklist(schede: list[Scheda]) -> Path:
    d = repo_root() / "WORKFLOW-ESTATE" / "02-AUTOMAZIONI-E-SCRIPTS" / "metrics"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "checklist-agenti.json"
    p.write_text(json.dumps([asdict(s) | {"punteggio": s.punteggio, "stato": s.stato,
                                          "gravita": s.gravita, "mancanti": s.mancanti}
                             for s in schede], indent=2, ensure_ascii=False), encoding="utf-8")
    salva_report_visibile(schede)
    return p


def salva_report_visibile(schede: list[Scheda]) -> Path:
    """Scrive un report LEGGIBILE dentro WORKFLOW-ESTATE, dove Max lo vede senza lanciare comandi.

    Richiesta esplicita di Max (25/07): "tutto cio' che costruisci dentro il workflow estate devo
    vederlo, tutta la struttura". Il misuratore vive in empire/ (runtime), ma il suo RISULTATO
    deve essere visibile nel posto che Max guarda: 03-AGENTI-E-RUOLI.
    """
    from datetime import datetime
    tot = len(schede) or 1
    per_stato: dict[str, int] = {}
    for s in schede:
        per_stato[s.stato] = per_stato.get(s.stato, 0) + 1

    righe = [
        "# 📊 STATO AGENTI — quanto sono OPERATIVI (non solo scritti)",
        f"> Generato da `empire forge scan` · {datetime.now().astimezone().isoformat(timespec='minutes')}",
        "> Un agente OPERATIVO ha: id, ruolo unico, input, **output** (cosa produce), criterio di",
        "> successo, e istruzioni eseguibili. Uno DOCUMENTALE e' solo una scheda che non lavora.",
        "",
        "## Riepilogo",
        "",
        "| Stato | Agenti | % |",
        "|---|---|---|",
    ]
    for stato in ("OPERATIVO", "PARZIALE", "DOCUMENTALE"):
        n = per_stato.get(stato, 0)
        righe.append(f"| {stato} | {n} | {round(100*n/tot,1)}% |")
    righe += ["", f"**Totale agenti reali:** {tot}", "",
              "## Prossimi da rendere operativi (i piu' gravi per primi)", ""]
    for s in [x for x in schede if x.stato != "OPERATIVO"][:15]:
        manca = ", ".join(m.split("-")[1] for m in s.mancanti)
        righe.append(f"- **{s.id}** — {s.punteggio}/10 [{s.stato}] · manca: {manca}")
    righe += ["", "## Gia' operativi", ""]
    for s in [x for x in schede if x.stato == "OPERATIVO"][:40]:
        righe.append(f"- {s.id} — {s.punteggio}/10")
    righe.append("\n---\n⛓️ report rigenerato a ogni `forge scan --salva`")

    d = repo_root() / "WORKFLOW-ESTATE" / "03-AGENTI-E-RUOLI"
    d.mkdir(parents=True, exist_ok=True)
    rp = d / "STATO-AGENTI.md"
    rp.write_text("\n".join(righe), encoding="utf-8")
    return rp


# ------------------------------------------------------------------ CLI

def _cmd_scan(a) -> int:
    schede = checklist()
    tot = len(schede)
    per_stato: dict[str, int] = {}
    for s in schede:
        per_stato[s.stato] = per_stato.get(s.stato, 0) + 1

    print(f"AGENTI ANALIZZATI: {tot}")
    print("=" * 70)
    for stato in ("OPERATIVO", "PARZIALE", "DOCUMENTALE"):
        n = per_stato.get(stato, 0)
        pct = round(100 * n / tot, 1) if tot else 0
        print(f"  {stato:12} {n:5}   {pct:5}%")

    print("\nCRITERIO PIU' ASSENTE (quanti agenti NON ce l'hanno):")
    for nome in CRITERI:
        n = sum(1 for s in schede if nome in s.mancanti)
        pct = round(100 * n / tot, 1) if tot else 0
        barra = "#" * int(pct / 4)
        print(f"  {nome:18} {n:5}  {pct:5}%  {barra}")

    if a.salva:
        p = salva_checklist(schede)
        print(f"\nchecklist salvata: {p.relative_to(repo_root())}")
    return 0


def _cmd_prossimo(a) -> int:
    schede = checklist(limite=a.quanti)
    print(f"PROSSIMI {len(schede)} DA RENDERE OPERATIVI (i piu' gravi per primi)")
    print("=" * 70)
    for i, s in enumerate(schede, 1):
        print(f"\n{i}. {s.id}   [{s.stato}]  punteggio {s.punteggio}/10  gravita {s.gravita}")
        print(f"   {s.percorso}  ({s.righe} righe)")
        print(f"   manca: {', '.join(s.mancanti) or 'niente'}")
    return 0


def _cmd_agente(a) -> int:
    trovati = [p for p in _file_agenti() if p.stem == a.id]
    if not trovati:
        print(f"agente non trovato: {a.id}")
        return 2
    s = analizza(trovati[0])
    print(f"{s.id}   [{s.stato}]   punteggio {s.punteggio}/10")
    print(f"{s.percorso}  ({s.righe} righe)")
    print("-" * 70)
    for c in s.criteri:
        segno = "OK  " if c.passa else "NO  "
        print(f"{segno} {c.nome:18} {c.descrizione}")
        if c.prova:
            print(f"       prova: {c.prova}")
    return 0


def register(sub) -> None:
    p = sub.add_parser("forge", help="misura quanto gli agenti sono operativi invece che documentali")
    s = p.add_subparsers(dest="forge_cmd", required=True)

    q = s.add_parser("scan", help="panoramica su tutti gli agenti")
    q.add_argument("--salva", action="store_true", help="scrive la checklist in metrics/")
    q.set_defaults(fn=_cmd_scan)

    q = s.add_parser("prossimo", help="i prossimi da sistemare, i piu' gravi per primi")
    q.add_argument("--quanti", type=int, default=10)
    q.set_defaults(fn=_cmd_prossimo)

    q = s.add_parser("agente", help="scheda dettagliata di un agente")
    q.add_argument("id")
    q.set_defaults(fn=_cmd_agente)

    def _dispatch(a):
        return a.fn(a)
    p.set_defaults(fn=_dispatch)
