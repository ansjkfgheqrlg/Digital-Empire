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

**AGGIORNAMENTO 2026-09-03 21:3x — le 3 sentinelle morte sono state recuperate.** Swarm di
3 agenti paralleli (`studia-rizzo`, `studia-roberts`, `sentinella-cfo-ai`), tutte chiuse
end-to-end. Dettaglio: CP-20260903-014 (Rizzo), CP-20260903-015 (Roberts), CP-20260903-017
(CFO-AI). Pagine wiki: `Source_Simone_Rizzo_Loop_Engineering.md`,
`Source_Jack_Roberts_7_Claude_Design_Skills.md`, `Source_Giovanni_Beggiato_CFO_AI_Claude.md`
+ nuova `tools/Tool_Tesoreria_Digital_Empire.md`. Il deliverable speciale
`runs/max17-v15/confronto-tesoreria.md` è scritto: 5 consigli concreti per la Tesoreria
(soglie in codice, campo data-scadenza scadenzario, verifica automatica su risposte in
prosa, test di determinismo, terzo tipo di dato "parametro esterno") — nessuna patch
applicata, restano da decidere.

**Trovato due volte lo stesso difetto sistemico** (Rizzo + Roberts, sessioni diverse): le
sentinelle morte avevano dichiarato lavoro fatto (patch applicate, N frame coperti) che
non risultava vero sul disco. Le sentinelle di recupero hanno verificato tutto con grep/diff
prima di fidarsi e corretto i manifest — ma il pattern (auto-dichiarazione non verificata
prima del crash) è **da controllare strutturalmente**, non solo corretto caso per caso.

**CORREZIONE 2026-09-03 22:0x — il "quattro video mai guardati" era sbagliato, verificato
sul disco prima di lanciare le sentinelle:**

| Run | id | Titolo reale | Stato vero |
|---|---|---|---|
| `max17-v12` | `pUu4G2lINnk` | Insane Claude Design Skills | **DOPPIONE di v11-Roberts, già chiuso** — stesso id/titolo/durata, non lanciare |
| `max17-v13` | `BSUHmVcaO1g` | Se usi ancora i prompt... | **DOPPIONE di v07-Rizzo, già chiuso** — stesso id/titolo/durata, non lanciare |
| `max17-v14` | `P-BQ-AGS0ck` | "Become a Master Storyteller" | **CHIUSO 2026-09-03 22:xx** — CP-20260903-019 |
| `max17-v16` | `gUnQK6bWHkI` | Micro-personal-brand da milioni | genuinamente nuovo, 859 frame, verificato unico — **IN CORSO** |

**AUTOCORREZIONE 2026-09-03 22:xx — mi ero sbagliato IO su Vishen, non il checkpoint
originale.** Avevo scritto sopra "il video vero di Vishen non risulta scaricato da nessuna
parte" giudicando solo dal titolo testuale ("Become a Master Storyteller" ≠ "Vishen story").
**Falso.** La sentinella che ha guardato davvero `max17-v14` per intero conferma: e' Vishen
Lakhiani (fondatore Mindvalley) in persona, parlato + `info.json` (uploader `@vishen`)
verificati. E' lo stesso identico video del `max17-v09-vishen-story` originale (id
`P-BQ-AGS0ck` in entrambi), solo che v09 ne aveva un download parziale (30MB) e v14 quello
completo (78MB). **Vishen era gia' su disco, non mancava nulla.** Lezione: un titolo
testuale da solo non basta a giudicare "contenuto sbagliato" — verificare uploader/id prima
di dichiarare un buco che non c'e'. La cartella `v09-vishen-story` ora e' ridondante (v14 la
sostituisce, download completo) — puo' restare come doppione minore, non blocca nulla.

**Resta valido invece** (verificato su id, non su titolo): v12/v13 sono doppioni reali di
Roberts/Rizzo, stesso id+durata esatti, non solo titolo simile.

**Causa probabile del doppio-download v12/v13/v14**: un batch di ingest lanciato il
2026-09-03 13:31 (stesso timestamp su tutti e tre) ha ri-scaricato url già usate — bug
nella lista sorgente, non nel motore di ingest. Da controllare quando si torna sull'ingest,
non ora (Fase 1 = studio).

**Due video mai scaricati:** `rvpRQD43wdY` (**Beggiato, guida agenzia, 4h17** — le
trascrizioni ci sono già in `runs/max-17-2026-09/subs/`) e **Justin Sung 4h55**, di cui
non ho l'indirizzo da nessuna parte.

---

## 4. IL PROSSIMO PASSO ESATTO

1. ~~Recuperare le tre sentinelle morte~~ — **FATTO 2026-09-03 21:3x**, vedi §3.
2. ~~v14 (Vishen/Master Storyteller)~~ — **FATTO 2026-09-03 22:xx**, CP-20260903-019.
   ~~v12, v13~~ — non servivano, doppioni di Roberts/Rizzo già chiusi.
3. **In corso ora: v16** (micro-personal-brand, 859 frame) — una sentinella e' morta per
   errore di connessione a meta', rilanciata da dove poteva riprendere (scenes.json gia'
   fatto). Ultimo video del lotto v01-v16.
4. Poi il mostro da 4h17 (Beggiato-guida-agenzia, `rvpRQD43wdY`, trascrizioni già in
   `runs/max-17-2026-09/subs/`) e Justin Sung 4h55 (link da ritrovare).
5. Poi valutare il pattern trovato in §3 (auto-dichiarazione non verificata prima del
   crash di sessione) — serve un controllo strutturale, non solo correzioni a mano.

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
