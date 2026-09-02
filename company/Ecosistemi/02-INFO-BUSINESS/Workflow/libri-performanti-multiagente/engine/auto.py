"""
Produzione automatica di un libro completo, da un comando solo (2026-08-30).

    python -m engine.kdp auto "<argomento>"      # oppure senza argomento: prende dal magazzino

Dall'avvio alla cartella finale non chiede NIENTE. Cosa fa, in ordine:

    1. argomento (dal magazzino o dalla riga di comando)
    2. titolo + outline + fili narrativi + prompt copertina      -> 1 chiamata
    3. capitoli a BLOCCHI, con i riassunti scritti insieme       -> N chiamate
       dopo ogni blocco gira il GATE: se boccia, RISCRIVE quel blocco
       (non tira dritto: e' tutta la differenza fra correggere 4 capitoli e correggerne 24)
    4. copy Amazon (titolo, sottotitolo, descrizione, keyword)   -> 1 chiamata, validata
    5. assemblaggio: docx + PDF + EPUB + prompt copertina + copy nella STESSA cartella

PERCHE' A BLOCCHI E NON UN CAPITOLO PER CHIAMATA. Misurato il 2026-08-30: ogni invocazione
di `claude -p` costa ~0,08-0,11 $ di solo harness, prima ancora di scrivere una parola. A
capitolo singolo sarebbero ~2,4 $ di sola tassa su 24 capitoli. A blocchi di 4 diventano
~0,5 $. Il blocco e' anche l'unita' che il gate gia' usa, quindi i due ritmi coincidono.

IL FRENO. Il 13 agosto un tentativo simile ha sfondato il limite di spesa mensile del piano
senza accorgersene. Qui il budget si controlla PRIMA di ogni chiamata e, quando finisce, il
flusso si ferma e salva: `BudgetSuperato` non e' un errore, e' il comportamento voluto.

COSA NON FA, di proposito: non genera l'immagine di copertina e non carica su KDP. Restano
i due passi umani (uno perche' serve un generatore di immagini, l'altro perche' e'
irreversibile verso l'esterno).
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

from . import config, gate_blocco, magazzino, metriche, validators
from .book_project import BookProject, slugify
from .scrittore import Budget, BudgetSuperato, ScrittoreClaudeCLI

CAPITOLI_PER_BLOCCO = 4
TENTATIVI_PER_BLOCCO = 3
BUDGET_DEFAULT_USD = 5.0          # scelta di Max, 2026-08-30

_RE_JSON = re.compile(r"\{.*\}", re.DOTALL)
_RE_CAP = re.compile(r"^===\s*CAP\s*(\d{1,2})\s*===\s*$", re.MULTILINE)
_RE_RIASS = re.compile(r"^===\s*RIASSUNTI\s*===\s*$", re.MULTILINE)


@dataclass
class EsitoAuto:
    slug: str = ""
    titolo: str = ""
    ok: bool = False
    fase_fallita: str = ""
    errore: str = ""
    cartella: str = ""
    capitoli_scritti: int = 0
    capitoli_totali: int = 0
    parole: int = 0
    riscritture: int = 0
    costo_usd: float = 0.0
    minuti: float = 0.0
    pubblicabile: bool = False
    nota_pubblicazione: str = ""
    passi: list = field(default_factory=list)

    def __str__(self) -> str:
        r = ["", "=" * 74,
             " PRODUZIONE AUTOMATICA — %s" % ("COMPLETATA" if self.ok else "INTERROTTA"),
             "=" * 74,
             "  libro     : %s (%s)" % (self.titolo or "?", self.slug or "?"),
             "  capitoli  : %d/%d  (%d parole)" % (self.capitoli_scritti,
                                                   self.capitoli_totali, self.parole),
             "  riscritture per gate bocciato: %d" % self.riscritture,
             "  costo     : $%.4f" % self.costo_usd,
             "  tempo     : %.1f minuti" % self.minuti]
        if self.cartella:
            r.append("  cartella  : %s" % self.cartella)
            r.append("  stato     : %s" % ("CARICABILE SU KDP" if self.pubblicabile else
                                           "COMPLETO — manca solo l'immagine di copertina "
                                           "(passo umano)"))
        if not self.ok:
            r += ["", "  FERMATO in fase '%s':" % self.fase_fallita,
                  "    %s" % self.errore,
                  "  Il lavoro fatto e' salvato: si riprende senza ricominciare."]
        r.append("")
        return "\n".join(r)


def _log(passi: list, testo: str) -> None:
    print("  %s" % testo, flush=True)
    passi.append(testo)


def _estrai_json(testo: str) -> dict | None:
    m = _RE_JSON.search(testo)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


# --------------------------------------------------------------------- prompt
_REGOLE = """REGOLE NON NEGOZIABILI (il testo viene controllato da un programma):
- Scrivi in INGLESE. E' un libro per Amazon KDP US.
- MAI lineette lunghe (em dash, en dash, doppio trattino) fuori dal dialogo: sono la firma
  piu' riconoscibile della scrittura automatica e vengono bocciate automaticamente.
  Usa virgole, punti o punti e virgola.
- Nessun capitolo deve ripetere la scena di un altro.
- Ogni capitolo deve FINIRE, mai interrompersi a meta' frase o di scena.
- Niente testo di servizio: nessuna nota, nessun commento, nessun "ecco il capitolo"."""


def _prompt_outline(argomento: str, nicchia: str, capitoli: int, parole: int) -> str:
    return f"""Sei un romanziere professionista. Progetta un romanzo completo.

ARGOMENTO: {argomento}
NICCHIA (mercato Amazon KDP): {nicchia}
STRUTTURA: {capitoli} capitoli da circa {parole} parole ciascuno.

{_REGOLE}

Rispondi SOLO con un oggetto JSON, senza testo attorno, con queste chiavi:
{{
  "titolo": "titolo del romanzo in inglese, evocativo, 2-5 parole",
  "autore": "nome d'autore inglese plausibile per la nicchia",
  "premessa": "2 frasi",
  "personaggi": [{{"nome": "...", "ruolo": "...", "voluto": "cosa vuole", "segreto": "..."}}],
  "ambientazione": "dove e quando, 2 frasi",
  "atti": ["atto 1 in 1 frase", "atto 2", "atto 3"],
  "capitoli": [{{"n": 1, "titolo": "...", "cosa_succede": "2 frasi concrete: chi fa cosa, dove, e cosa cambia alla fine"}}],
  "prompt_copertina": "prompt in inglese per un generatore di immagini: soggetto, stile, palette, mood. Niente testo nell'immagine."
}}
L'elenco "capitoli" deve avere esattamente {capitoli} voci, numerate da 1 a {capitoli}."""


def _prompt_blocco(cfg: dict, piano: dict, da: int, a: int, riassunto: str,
                   correzione: str = "") -> str:
    schede = [c for c in piano.get("capitoli", []) if da <= int(c.get("n", 0)) <= a]
    scaletta = "\n".join("  cap %02d — %s: %s" % (int(c["n"]), c.get("titolo", ""),
                                                  c.get("cosa_succede", ""))
                         for c in schede)
    personaggi = "\n".join("  %s (%s): vuole %s. Segreto: %s"
                           % (p.get("nome"), p.get("ruolo"), p.get("voluto"),
                              p.get("segreto", "nessuno"))
                           for p in piano.get("personaggi", []))
    parole = cfg["parole_per_capitolo"]
    testa = ""
    if correzione:
        testa = ("UN CONTROLLO AUTOMATICO HA BOCCIATO LA VERSIONE PRECEDENTE DI QUESTI "
                 "CAPITOLI. Riscrivili da capo correggendo esattamente questo:\n%s\n\n"
                 % correzione)
    prima = ("QUESTO E' L'INIZIO DEL LIBRO: non c'e' niente prima."
             if not riassunto else "QUELLO CHE E' GIA' SUCCESSO:\n%s" % riassunto)

    return f"""{testa}Sei un romanziere professionista. Scrivi i capitoli da {da} a {a} di un romanzo.

TITOLO: {cfg['titolo']}
AMBIENTAZIONE: {piano.get('ambientazione', '')}
PERSONAGGI:
{personaggi}

{prima}

SCALETTA DEI CAPITOLI DA SCRIVERE ORA:
{scaletta}

LUNGHEZZA: ogni capitolo ALMENO {parole} parole. E' un minimo, non un bersaglio: un
capitolo corto fa bocciare l'intero blocco e va riscritto. Scrivi scene piene, con dialogo,
azione e dettagli concreti.

{_REGOLE}

FORMATO DELLA RISPOSTA, esatto e senza altro attorno:

=== CAP {da} ===
# Titolo del capitolo
(il testo del capitolo)

=== CAP {da + 1} ===
# Titolo del capitolo
(il testo del capitolo)

...e cosi' via fino al capitolo {a}. Poi, alla fine, UNA SOLA VOLTA:

=== RIASSUNTI ===
### cap {da:02d}
un paragrafo di cosa e' successo in questo capitolo
### cap {da + 1:02d}
un paragrafo
(...un blocco ### cap NN per OGNI capitolo che hai scritto ora)"""


def _prompt_copy(cfg: dict, piano: dict) -> str:
    return f"""Scrivi il copy per la scheda Amazon KDP di questo romanzo.

TITOLO: {cfg['titolo']}
AUTORE: {cfg['autore']}
NICCHIA: {cfg['nicchia']}
PREMESSA: {piano.get('premessa', '')}

{_REGOLE}

Rispondi SOLO con un oggetto JSON:
{{
  "titolo": "{cfg['titolo']}",
  "sottotitolo": "sottotitolo commerciale in inglese, max 12 parole",
  "descrizione": "la quarta di copertina, 150-250 parole in inglese, che fa venire voglia di comprarlo. Niente spoiler del finale.",
  "keyword": ["7 keyword di ricerca Amazon in inglese"],
  "categorie": ["2 categorie KDP plausibili"]
}}"""


# ----------------------------------------------------------------------- fasi
def _scrivi_blocco(p: BookProject, scrittore, cfg: dict, piano: dict,
                   da: int, a: int, passi: list) -> tuple[bool, str, int]:
    """Scrive (o riscrive) un blocco finche' il gate lo accetta. Torna (ok, errore, riscritture)."""
    correzione = ""
    riscritture = 0

    for tentativo in range(1, TENTATIVI_PER_BLOCCO + 1):
        etichetta = "%s/cap%02d-%02d/t%d" % (p.slug, da, a, tentativo)
        prompt = _prompt_blocco(cfg, piano, da, a, p.riassunto_progressivo(), correzione)
        esito = scrittore.genera(prompt, etichetta)
        if not esito.ok:
            correzione = "la risposta precedente non e' arrivata: %s" % esito.errore
            _log(passi, "  tentativo %d: %s" % (tentativo, esito.errore[:90]))
            riscritture += 1
            continue

        pezzi = _spezza_blocco(esito.testo, da, a)
        if isinstance(pezzi, str):                      # messaggio d'errore
            correzione = pezzi
            _log(passi, "  tentativo %d: formato non valido (%s)" % (tentativo, pezzi[:70]))
            riscritture += 1
            continue

        capitoli, riassunti = pezzi
        for n, testo in capitoli.items():
            p.path_capitolo(n).write_text(testo, encoding="utf-8")
        if riassunti:
            _aggiungi_riassunti(p, riassunti)

        g = gate_blocco.controlla(p)
        metriche.registra(p.slug, "blocco",
                          esito="passato" if g.si_prosegue else "bocciato",
                          motivi=g.blocchi)
        if g.si_prosegue:
            _log(passi, "  cap %d-%d scritti (%d parole, media %d/cap) — GATE OK"
                 % (da, a, g.parole, g.media_per_capitolo))
            return True, "", riscritture

        correzione = "\n".join("- %s" % b for b in g.blocchi)
        riscritture += 1
        _log(passi, "  cap %d-%d BOCCIATI dal gate (tentativo %d/%d): %s"
             % (da, a, tentativo, TENTATIVI_PER_BLOCCO, g.blocchi[0][:90]))

    return False, ("il blocco %d-%d non ha passato il gate in %d tentativi. Ultimo motivo:\n%s"
                   % (da, a, TENTATIVI_PER_BLOCCO, correzione)), riscritture


def _spezza_blocco(testo: str, da: int, a: int):
    """Divide la risposta in capitoli + riassunti. Torna (dict, str) oppure un errore str.

    Non si fida del formato: se manca un capitolo lo DICE, invece di salvare meta' blocco
    e far fallire il gate per un motivo sbagliato."""
    corpo, riassunti = testo, ""
    m = _RE_RIASS.search(testo)
    if m:
        corpo, riassunti = testo[:m.start()], testo[m.end():].strip()

    tagli = list(_RE_CAP.finditer(corpo))
    if not tagli:
        return ("la risposta non contiene nessun marcatore '=== CAP N ==='. "
                "Rispetta il formato richiesto.")

    capitoli: dict[int, str] = {}
    for i, t in enumerate(tagli):
        n = int(t.group(1))
        fine = tagli[i + 1].start() if i + 1 < len(tagli) else len(corpo)
        contenuto = corpo[t.end():fine].strip()
        if contenuto:
            capitoli[n] = contenuto

    attesi = set(range(da, a + 1))
    mancanti = sorted(attesi - set(capitoli))
    if mancanti:
        return ("mancano i capitoli %s: la risposta si e' fermata prima. Scrivili TUTTI."
                % mancanti)
    return {n: capitoli[n] for n in sorted(attesi)}, riassunti


def _aggiungi_riassunti(p: BookProject, nuovi: str) -> None:
    """Appende i riassunti nella sezione '## Capitoli' che il gate legge."""
    testo = p.riassunti_path.read_text(encoding="utf-8") if p.riassunti_path.exists() else ""
    if "## Capitoli" not in testo:
        testo += "\n\n## Capitoli\n"
    testo = testo.rstrip() + "\n\n" + nuovi.strip() + "\n"
    p.riassunti_path.write_text(testo, encoding="utf-8")


# ------------------------------------------------------------------- pubblica
def produci(argomento: str | None = None, *, nicchia: str | None = None,
            capitoli: int | None = None, parole_per_capitolo: int | None = None,
            budget_usd: float = BUDGET_DEFAULT_USD, modello: str | None = None,
            per_blocco: int = CAPITOLI_PER_BLOCCO, scrittore=None,
            motivo_nicchia: str | None = None) -> EsitoAuto:
    """Produce un libro completo. Non chiede niente."""
    avvio = time.time()
    passi: list = []
    e = EsitoAuto()
    budget = Budget(limite_usd=budget_usd)
    if scrittore is None:
        log = Path(config.__file__).resolve().parent.parent / "LIBRI" / "chiamate.jsonl"
        scrittore = ScrittoreClaudeCLI(
            modello=modello or ScrittoreClaudeCLI.__init__.__defaults__[0],
            budget=budget, log_path=log)
    else:
        budget = getattr(scrittore, "budget", budget)

    try:
        # --- 1. argomento -------------------------------------------------- #
        arg_magazzino = None
        if not argomento:
            arg_magazzino = magazzino.prendi()
            if arg_magazzino is None:
                e.fase_fallita, e.errore = "argomento", (
                    "nessun argomento passato e magazzino vuoto. Aggiungine uno con "
                    "`kdp magazzino --aggiungi`, oppure passa l'argomento al comando.")
                return e
            # `Argomento` ha titolo_lavoro + premessa, NON un campo `idea`. La prima
            # versione qui cadeva su str(argomento) e passava al modello il repr della
            # dataclass ("Argomento(nicchia='...', titolo_lavoro=...)") invece del tema:
            # il libro sarebbe nato da una riga di Python. Visto al primo run reale.
            titolo_lavoro = getattr(arg_magazzino, "titolo_lavoro", "") or ""
            premessa = getattr(arg_magazzino, "premessa", "") or ""
            argomento = ("%s. %s" % (titolo_lavoro, premessa)).strip(" .")
            if not argomento:
                e.fase_fallita, e.errore = "argomento", (
                    "l'argomento preso dal magazzino non ha ne' titolo_lavoro ne' premessa")
                return e
            nicchia = nicchia or getattr(arg_magazzino, "nicchia", None)
        nicchia = nicchia or getattr(config, "NICCHIA_DEFAULT", None) or "contemporary fiction"

        # LA DISCIPLINA DI CATALOGO VALE ANCHE QUI. `kdp nuovo` interroga
        # `_controlla_nicchia_catalogo` e pretende un `--motivo` per scostarsi dalla nicchia
        # attiva; questo flusso chiama `BookProject.crea` direttamente e quindi saltava quel
        # controllo — cioe' riapriva in silenzio esattamente il buco che il 23 agosto era
        # stato chiuso (tre libri, tre nicchie, nessuna quella attiva; B-018 ancora aperto).
        # Non potendo chiedere niente dopo l'avvio, lo scarto non si vieta: si DICHIARA.
        if not motivo_nicchia:
            try:
                from .kdp import _controlla_nicchia_catalogo
                _controlla_nicchia_catalogo(nicchia, None)
            except ValueError:
                motivo_nicchia = (
                    "scarto automatico: argomento preso dal magazzino con nicchia '%s', "
                    "diversa da quella attiva del catalogo. Dichiarato dal flusso `kdp auto` "
                    "invece che deciso in silenzio (B-018 resta aperto)." % nicchia)
                _log(passi, "NICCHIA fuori catalogo: scarto dichiarato in progetto.json")
            except Exception:
                pass
        _log(passi, "argomento: %s" % argomento[:90])
        _log(passi, "nicchia  : %s | budget $%.2f | modello %s"
             % (nicchia, budget_usd, getattr(scrittore, "modello", "?")))

        capitoli = capitoli or getattr(config, "DEFAULT_TOTAL_CHAPTERS", 24)
        parole_per_capitolo = parole_per_capitolo or getattr(
            config, "DEFAULT_WORDS_PER_CHAPTER", 1600)

        # --- 2. outline ----------------------------------------------------- #
        _log(passi, "fase 1/4: titolo, personaggi e scaletta...")
        r = scrittore.genera(_prompt_outline(argomento, nicchia, capitoli,
                                             parole_per_capitolo), "outline")
        if not r.ok:
            e.fase_fallita, e.errore = "outline", r.errore
            return e
        piano = _estrai_json(r.testo)
        if not piano or not piano.get("titolo") or not piano.get("capitoli"):
            e.fase_fallita, e.errore = "outline", (
                "la risposta non contiene un piano JSON valido (titolo + capitoli)")
            return e
        if len(piano["capitoli"]) < capitoli:
            e.fase_fallita, e.errore = "outline", (
                "la scaletta ha %d capitoli invece di %d" % (len(piano["capitoli"]), capitoli))
            return e

        titolo = str(piano["titolo"]).strip()
        e.titolo, e.slug = titolo, slugify(titolo)
        e.capitoli_totali = capitoli
        try:
            p = BookProject.crea(titolo, nicchia, str(piano.get("autore") or "Digital Empire"),
                                 capitoli, parole_per_capitolo)
        except FileExistsError:
            e.fase_fallita, e.errore = "creazione", (
                "esiste gia' un progetto '%s'. Cancellalo o cambia argomento." % e.slug)
            return e
        if motivo_nicchia:
            p._aggiorna_config(scarto_nicchia={"nicchia_catalogo": nicchia,
                                               "motivo": motivo_nicchia})
        metriche.registra(p.slug, "progetto_creato", nicchia=nicchia,
                          autore=piano.get("autore"), automatico=True)
        p.salva_piano(piano)
        p.outline_path.write_text(_outline_markdown(piano, titolo), encoding="utf-8")
        (p.dir / "copertina-prompt.md").write_text(
            "# Prompt copertina — %s\n\n%s\n" % (titolo, piano.get("prompt_copertina", "")),
            encoding="utf-8")
        if arg_magazzino is not None:
            try:
                magazzino.collega_libro(getattr(arg_magazzino, "titolo_lavoro", ""), p.slug)
            except Exception:
                pass
        _log(passi, "titolo: %s  (slug %s)" % (titolo, p.slug))

        # --- 3. capitoli a blocchi ------------------------------------------ #
        _log(passi, "fase 2/4: scrittura di %d capitoli a blocchi di %d..."
             % (capitoli, per_blocco))
        for da in range(1, capitoli + 1, per_blocco):
            a = min(da + per_blocco - 1, capitoli)
            ok, errore, risc = _scrivi_blocco(p, scrittore, p._config(), piano, da, a, passi)
            e.riscritture += risc
            if not ok:
                e.fase_fallita, e.errore = "capitoli %d-%d" % (da, a), errore
                return e

        st = p.stato()
        e.capitoli_scritti, e.parole = len(st.capitoli_scritti), st.parole_scritte

        # --- 4. copy Amazon -------------------------------------------------- #
        _log(passi, "fase 3/4: copy Amazon...")
        rc = scrittore.genera(_prompt_copy(p._config(), piano), "%s/copy" % p.slug)
        if not rc.ok:
            e.fase_fallita, e.errore = "copy", rc.errore
            return e
        copy = _estrai_json(rc.testo)
        if not copy:
            e.fase_fallita, e.errore = "copy", "la risposta non contiene un JSON valido"
            return e
        try:
            p.salva_copy(copy)
        except Exception as ex:
            e.fase_fallita, e.errore = "copy", (
                "il copy non ha passato la validazione: %s" % str(ex)[:200])
            return e
        _log(passi, "copy salvato e validato")

        # --- 5. assemblaggio ------------------------------------------------- #
        _log(passi, "fase 4/4: assemblaggio del pacchetto...")
        # `assembla()` SOLLEVA se il pacchetto non e' pubblicabile, e senza immagine di
        # copertina non lo e' mai. Ma per questo flusso quello NON e' un fallimento: la
        # copertina e' un passo umano dichiarato (serve un generatore di immagini), e il
        # pacchetto viene creato lo stesso. Distinguere i due casi e' esattamente cio' che
        # `kdp pacchetto` chiama COMPLETO contro CARICABILE SU KDP.
        try:
            risultato = p.assembla(cover_path=None)
            e.pubblicabile = True
        except RuntimeError as ex:
            risultato, e.pubblicabile = {}, False
            e.nota_pubblicazione = str(ex)[:300]
        cartella = (risultato or {}).get("pacchetto")
        if not cartella:                      # il raise arriva dopo la creazione: cercala
            cartella = _trova_pacchetto(e.titolo)
        if not cartella:
            e.fase_fallita = "assemblaggio"
            e.errore = e.nota_pubblicazione or "il pacchetto non e' stato creato"
            return e
        e.cartella = str(cartella)

        # Se NON e' pubblicabile, lo e' solo per la copertina? Qualunque altro bloccante
        # e' un guasto vero e non va fatto passare per un successo.
        if not e.pubblicabile:
            altri = [b for b in _bloccanti(Path(cartella))
                     if "copertina" not in b.lower()]
            if altri:
                e.fase_fallita = "validazione"
                e.errore = "il pacchetto ha bloccanti oltre la copertina: %s" % "; ".join(
                    a[:120] for a in altri[:3])
                return e
            _log(passi, "pacchetto COMPLETO (manca solo l'immagine di copertina: passo umano)")

        metriche.registra(p.slug, "consegna", con_copertina=False, automatico=True)
        e.ok = True
        return e

    except BudgetSuperato as ex:
        e.fase_fallita, e.errore = "budget", str(ex)
        return e
    except Exception as ex:                       # nessun crash silenzioso
        e.fase_fallita = e.fase_fallita or "imprevisto"
        e.errore = "%s: %s" % (type(ex).__name__, str(ex)[:300])
        return e
    finally:
        e.costo_usd = budget.speso_usd
        e.minuti = round((time.time() - avvio) / 60, 1)
        e.passi = passi


def _trova_pacchetto(titolo: str) -> Path | None:
    """La cartella del pacchetto appena creato, cercata per titolo."""
    pronti = getattr(config, "LIBRI_PRONTI_DIR", None) or (config.LIBRI_DIR / "libri_pronti")
    if not Path(pronti).exists():
        return None
    atteso = re.sub(r"[^a-z0-9]+", "", (titolo or "").lower())
    for d in sorted(Path(pronti).iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
        if d.is_dir() and re.sub(r"[^a-z0-9]+", "", d.name.lower()) == atteso:
            return d
    return None


def _bloccanti(cartella: Path) -> list[str]:
    """I bloccanti scritti da `assembla` in validazione.json."""
    f = cartella / "validazione.json"
    if not f.exists():
        return []
    try:
        return [str(b) for b in json.loads(f.read_text(encoding="utf-8")).get("bloccanti", [])]
    except (json.JSONDecodeError, OSError):
        return []


def _outline_markdown(piano: dict, titolo: str) -> str:
    righe = ["# Outline — %s" % titolo, "",
             "## Premessa", piano.get("premessa", ""), "",
             "## Ambientazione", piano.get("ambientazione", ""), "",
             "## Personaggi"]
    for pers in piano.get("personaggi", []):
        righe.append("- **%s** (%s): vuole %s. Segreto: %s"
                     % (pers.get("nome"), pers.get("ruolo"), pers.get("voluto"),
                        pers.get("segreto", "—")))
    righe += ["", "## Atti"]
    righe += ["%d. %s" % (i + 1, a) for i, a in enumerate(piano.get("atti", []))]
    righe += ["", "## Capitoli"]
    for c in piano.get("capitoli", []):
        righe.append("%02d. **%s** — %s" % (int(c.get("n", 0)), c.get("titolo", ""),
                                            c.get("cosa_succede", "")))
    return "\n".join(righe) + "\n"
