# EMP-QQ2R — Studio dei 17 video + reparti nuovi

- **Codice di ripresa:** `EMP-QQ2R`
- **Aperto:** 2026-09-03 14:05
- **Stato:** APERTO
- **Chi riprende:** basta dire `EMP-QQ2R` in una chat nuova dentro Digital Empire.
- **Ordine di Max che governa tutto:** *"prendi il controllo, fai tutto. Basta che l'azienda
  migliora, non deve mai peggiorare."* Delega piena, nessuna approvazione da chiedere.

---

## 1. IL LAVORO IN UNA FRASE

Guardare fino in fondo i 17 video del lotto `max17` (fotogramma per fotogramma, archivio
integrale, biblioteca, e i 5 consigli su cosa migliorare in azienda) e costruire i reparti
che l'azienda non aveva: **Ultimo Metro** (vede il lavoro finito e mai pubblicato) e
**Tesoreria** (conta i soldi).

---

## 2. DOVE SIAMO — cosa è FATTO davvero

**Video chiusi end-to-end: 9 su 17** (guardati + archiviati + in biblioteca + consigli dati)
Artem · Beggiato · Nico · Trivellato · Jay E · Belli · Herk · Barron · *(Vishen mai iniziato)*

**Reparti e organi costruiti:**
- **ADR-016 — ULTIMO METRO.** `scripts/ultimo_metro.py` + skill `ultimo-metro`. Prima misura:
  **25 pezzi finiti mai usciti, 2.137 MB, il più vecchio fermo da 135 giorni, 23 caricabili
  subito.**
- **ADR-020 — TESORERIA** (14° ecosistema). `scripts/tesoreria.py` + skill `tesoreria` +
  5 agenti (`tesoreria-conductor/-entrate/-spese/-report/-previsione`) + dati ad accodamento
  in `company/Memory/tesoreria/`. Collaudata e ripulita: **i registri partono vuoti**.
- **ADR-017** — revisione con un motore di famiglia diversa, in pilota su Preventa Outreach.
- **ADR-018** — dichiarato il conflitto dei due ADR-012.
- **ADR-019** — motore di orchestrazione canonico: **`orchestration-layer`** (133 file di
  codice contro 28, 24 test contro 3). Chiude B-047.
- **I 10 guardiani riempiti**: 5 sentinelle da 39 righe a 320-377, 5 guild da 38 a 364-689.
  Board C-Suite +697 righe coi numeri veri.
- **`scripts/cerca_wiki.py`** — la memoria di 1.547 pagine cerca per sinonimi, non più solo
  per parola esatta.
- **`scripts/peso_skill.py`** — misurato per la prima volta il costo delle skill: 377 skill,
  129 sopra soglia, **l'81% del peso in quelle**.
- **`scripts/checkpoint.py`** — questo sistema.

**Auto-modifiche di Emperator (doppia scrittura verificata):**
- il battito si scrive **in parole semplici**, niente gergo
- la **riga `Forze`** è obbligatoria dentro **ogni** battito, coi gradi

---

## 3. COSA È RIMASTO A METÀ

**Tre sentinelle morte insieme per limite di sessione (reset 16:30 del 2026-09-03), tutte
a un passo dalla fine.** Il loro lavoro parziale è sul disco:

| Sentinella | Video | Stato reale | Ultima parola prima di morire |
|---|---|---|---|
| `studia-rizzo` | `max17-v07-rizzo-prompt` (943 fotogrammi, prompt) | analisi scritta | *"Ora atoms.json e coverage.md"* |
| `studia-roberts` | `max17-v11-roberts-design` (689 fotogrammi, design) | analisi scritta | *"Ora atoms.json e coverage.md"* |
| `sentinella-cfo-ai` | `max17-v15` (524 fotogrammi, **CFO AI**) | formati letti, niente scritto | *"Ora scrivo i deliverable"* |

**PRIMA DI RILANCIARLE: guardare cosa c'è già sul disco.** Due su tre hanno l'analisi fatta:
rifarla da capo sarebbe buttare via il lavoro più caro (la lettura dei fotogrammi).

```bash
ls "SKILL & Agenti/Empire Studio Suite/empire-studio/runs/max17-v07-rizzo-prompt/"
ls "SKILL & Agenti/Empire Studio Suite/empire-studio/runs/max17-v11-roberts-design/"
ls "SKILL & Agenti/Empire Studio Suite/empire-studio/runs/max17-v15/"
```

**Quattro video con i fotogrammi pronti e mai guardati:**

| Run | Titolo | Fotogrammi |
|---|---|---|
| `max17-v12` | Insane Claude Design Skills — costruire siti belli | 345 |
| `max17-v13` | Se usi ancora i prompt... devi vedere questa evoluzione | 472 |
| `max17-v14` | Become a Master Storyteller (il trucco della dopamina) | 390 |
| `max17-v16` | Come creare un micro-personal brand da milioni di euro | 859 |

**Due video mai scaricati:** `rvpRQD43wdY` (**Beggiato, guida agenzia, 4h17** — le
trascrizioni ci sono già in `runs/max-17-2026-09/subs/`) e **Justin Sung 4h55**, di cui
non ho l'indirizzo da nessuna parte.

**`max17-v09-vishen-story`** (779 fotogrammi) — mai iniziato.

---

## 4. IL PROSSIMO PASSO ESATTO

1. **Recuperare le tre sentinelle morte**, partendo da ciò che hanno già scritto. La più
   preziosa è `sentinella-cfo-ai`: doveva **confrontare** il CFO artificiale del video con
   la Tesoreria costruita oggi, e produrre `confronto-tesoreria.md` dentro
   `runs/max17-v15/`. Quel confronto non esiste in nessun altro run.
2. Poi i quattro con i fotogrammi pronti (v12, v13, v14, v16).
3. Poi il mostro da 4h17.

**Massimo 2-3 sentinelle in parallelo quando leggono immagini.** Con 3 la sessione è saltata
due volte in due giorni.

---

## 5. DECISIONI GIÀ PRESE — non ridiscuterle

- **Il motore di orchestrazione canonico è `orchestration-layer`** (ADR-019). Deciso su
  misure, non su gusto. Il lavoro di Neri vince, e va detto a Neri così.
- **La Tesoreria parte da zero il 2026-09-03.** I mesi precedenti **restano vuoti**:
  ricostruirli a memoria è vietato.
- **ADR-017 in pilota su un sistema solo**, non su tutto: l'istruttoria stessa dichiarava di
  non avere prove sufficienti.
- **Non si rifattorizzano le 115 skill lunghe** finché non si è misurato: la misura c'è ora
  (`peso_skill.py`), il taglio no, ed è mirato alle 5 più care, non a tutte.
- **Il motore prima della documentazione.** La piramide EMPIRE OS è progetto al 100% e zero
  codice: nessun reparto nuovo deve diventarne un altro pezzo.

---

## 6. TRAPPOLE — errori già fatti, non rifarli

- **B-033:** ci sono **tre** cartelle `memory-empire/knowledge/`. Due sono **morte** (ferme
  al 2026-07-09). L'unica viva è quella dentro `empire-studio/`.
- **I guardiani pre-commit stanno in `.githooks/`, NON in `.git/hooks/`.** Uno scagnozzo ha
  dichiarato che non esistevano: falso, e bloccano davvero (B-054).
- **Fine-riga:** dentro `company/Memory/` servono LF (`newline="\n"` in Python). In
  `wiki/log.md` **preservare il CRLF che ha già**: un file misto è ciò che il guardiano vuole
  evitare.
- **Frontmatter YAML:** un due-punti seguito da spazio dentro `description` fa **scartare il
  file in silenzio**. È successo a 85 skill su 296.
- **Numeri di backlog:** si leggono, non si indovinano. Uno scagnozzo ne ha usati quattro già
  occupati (16 riferimenti da correggere a mano). **Il backlog è arrivato a B-054.**
- **Gli heredoc bash si rompono** con gli apostrofi italiani: usare lo strumento di scrittura
  diretta o uno script nello scratchpad.
- **Massimo 5-6 immagini per messaggio** a una sentinella: con 75 vengono scartate tutte.
- **Un indice generato può pesare 88 MB**: `.indice-ricerca.json` è escluso da git (ADR-013).

---

## 7. COMANDI PER RIPARTIRE

```bash
# dove eravamo
python scripts/checkpoint.py leggi EMP-QQ2R
cat company/Memory/STATO-EMPIRE.md | tail -60

# lo stato dei video
for d in "SKILL & Agenti/Empire Studio Suite/empire-studio/runs"/max17-*; do
  echo "$(basename $d) frame:$(ls $d/frames 2>/dev/null|wc -l) analisi:$([ -f $d/video-analysis.md ] && echo SI || echo --)"
done

# i reparti nuovi
python scripts/ultimo_metro.py
python scripts/tesoreria.py report
python scripts/peso_skill.py
python scripts/cerca_wiki.py "quello che cerchi"
```

## 8. FILE TOCCATI

`scripts/` → `ultimo_metro.py`, `cerca_wiki.py`, `peso_skill.py`, `tesoreria.py`,
`checkpoint.py`, `emperator_hook.py`
`.claude/agents/` → 5 `sentinel-*`, 5 `guild-*`, 6 del Board, 5 `tesoreria-*`,
`conoscenza-empire`, `emperator`
`.claude/skills/` → `ultimo-metro`, `tesoreria`, `cro-call`, `icp-radar`,
`discovery-call-brief`
`company/Memory/decisions/` → ADR-016, 017, 018, 019, 020
`company/Memory/` → `BACKLOG.md` (fino a B-054), `STATO-EMPIRE.md`, `ULTIMO-METRO.md`,
`PESO-SKILL.md`, `TESORERIA.md`, `checkpoints/CP-20260903-003.md`

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-QQ2R`*
