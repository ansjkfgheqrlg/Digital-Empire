# context-doctor
            
> Path: [[Map - Skill_And_Agenti|SKILL & Agenti > SKILL > Agente Max > skills]]

## Content

# CONTEXT-DOCTOR — Protocollo Diagnostica e Ottimizzazione Contesto

Usa questo protocollo quando l'utente ha problemi di contesto saturato, sessioni lente, costi elevati, o vuole ottimizzare preventivamente il proprio ecosistema Claude Code.

**Riferimento KB:** K05-context.md (Capitoli 20-23) per soglie e framework teorico.

---

## FASE 1 — DIAGNOSTIC PROTOCOL

### Le 5 domande diagnostiche

Prima di analizzare qualsiasi file, poni queste domande all'utente (se le risposte non sono già nel prompt):

**D1 — Sintomo principale:**
"Cosa stai osservando esattamente? Il contesto si riempie velocemente? Le risposte diventano imprecise? Claude sembra 'dimenticare' le istruzioni? Costa troppo?"

**D2 — MCP installati:**
"Quali MCP hai installati? Sono attivi in tutti i progetti o solo alcuni? (es: ClickUp, GitHub, Notion, browser)"

**D3 — CLAUDE.md:**
"Hai un CLAUDE.md? Quanto è lungo? Ha regole globali E locali?"

**D4 — Skill attive:**
"Hai skill installate globalmente? Quante? Alcune molto lunghe (>200 righe)?"

**D5 — Tipo di lavoro:**
"Quale tipo di task stai eseguendo quando il problema si manifesta? Creazione file, analisi codice, conversazioni lunghe?"

---

## FASE 2 — LE 5 PATOLOGIE COMUNI

### PATOLOGIA 1: MCP Pesante Sempre Attivo

**Sintomi:** Contesto pre-occupato >20% prima ancora di iniziare a lavorare. Sessioni costose. Claude "manca di spazio" per task complesse.

**Diagnosi:** Il ClickUp MCP può consumare il 27% del contesto da solo. Ogni MCP installato e attivo occupa token nel system context anche quando non viene usato.

**Trattamento:**
1. Identifica quali MCP sono installati: controlla `C:\Users\Utente\.claude\settings.json` → sezione `mcpServers`
2. Per ogni MCP, valuta: "Lo uso in TUTTI i progetti o solo in alcuni?"
3. Se lo usi solo in alcuni progetti: sposta la configurazione MCP nel `.claude\settings.json` locale del progetto specifico, NON nel globale
4. Se le funzionalità del MCP possono essere replicate con una skill: crea la skill e disinstalla il MCP (vedi K08-mcp.md, Capitolo 33)
5. Verifica il risultato con `/context` dopo la modifica

**Soglia critica:** MCP >15% del contesto = RED FLAG. Considera alternativa skill.

---

### PATOLOGIA 2: CLAUDE.md Gonfio o Ridondante

**Sintomi:** Regole duplicate tra livello global e local. CLAUDE.md con centinaia di righe. Regole contraddittorie che confondono Claude.

**Diagnosi:** Ogni riga di CLAUDE.md occupa tokens. Il principio è: "ogni regola deve guadagnarsi il posto". Regole ridondanti, vaghe, o mai usate sono tokens sprecati.

**Trattamento:**
1. Leggi il CLAUDE.md globale: `C:\Users\Utente\.claude\CLAUDE.md`
2. Leggi il CLAUDE.md locale (se esiste): `[progetto]\.claude\CLAUDE.md`
3. Per ogni regola, chiedi: "Claude Code rispetterebbe questo comportamento di default senza questa regola?" → Se SÌ: elimina la regola
4. Elimina duplicati tra livello global e local
5. Consolida le regole simili in una sola più generale
6. Verifica che non ci siano contraddizioni (regola A dice X, regola B dice !X)
7. Target: CLAUDE.md globale < 50 righe. CLAUDE.md locale < 30 righe.

---

### PATOLOGIA 3: Autocompact Disabilitato

**Sintomi:** Il contesto si riempie rapidamente e non si svuota mai. Sessioni che si bloccano dopo pochi scambi lunghi.

**Diagnosi:** Autocompact comprime automaticamente la cronologia messaggi quando il contesto raggiunge una soglia. Senza Autocompact, ogni messaggio si accumula fino alla saturazione.

**Trattamento:**
1. Esegui `/config` in Claude Code
2. Nella scheda CONFIG, verifica che "Autocompact" sia su ON
3. Se era OFF: attivalo immediatamente
4. Per sessioni già saturate: usa il comando `/compact` manualmente per comprimere la cronologia corrente
5. Verifica con `/context` che la percentuale scenda dopo `/compact`

---

### PATOLOGIA 4: Lost in the Middle (Istruzioni Dimenticate)

**Sintomi:** Claude rispetta le istruzioni all'inizio della conversazione ma le "dimentica" nel mezzo. Istruzioni importanti in CLAUDE.md vengono ignorate se sono al centro del file.

**Diagnosi:** I modelli LLM hanno tre bias cognitivi documentati (Capitolo 23):
- **Primacy Bias:** Il testo all'inizio ha più peso
- **Recency Bias:** Il testo alla fine ha più peso
- **Lost in the Middle:** Il testo nel mezzo viene sottopesato

**Trattamento:**
1. Sposta le regole CRITICHE e NON NEGOZIABILI all'inizio del CLAUDE.md (primacy bias)
2. Metti le istruzioni finali ricorrenti alla fine del CLAUDE.md (recency bias)
3. Evita di mettere informazioni importanti nel mezzo del file
4. Struttura raccomandata per CLAUDE.md:
   ```
   # Regole Critiche (PRIMO BLOCCO — mai modificare)
   [regole più importanti qui]

   # Informazioni Progetto
   [contesto generale]

   # Workflow Standard
   [procedure operative]

   # Istruzione Finale (ULTIMO BLOCCO)
   [reminder finale ricorrente]
   ```

---

### PATOLOGIA 5: Skill Troppo Pesanti nel Contesto

**Sintomi:** Skill installate globalmente con centinaia di righe che vengono caricate in ogni sessione anche quando non servono.

**Diagnosi:** Le skill globali contribuiscono al contesto pre-occupato. Una skill da 300 righe installata globalmente occupa ~1-2% del contesto in ogni sessione, anche quando non viene mai usata.

**Trattamento:**
1. Audita le skill installate in `C:\Users\Utente\.claude\skills\`
2. Per ogni skill: è veramente usata in TUTTI i progetti? Se no, spostala a livello locale nel progetto che la usa
3. Per skill con body >200 righe: considera di spostare parte del contenuto in `references/` e caricarla solo quando serve
4. Elimina skill non più usate

---

## FASE 3 — SOGLIE DI RIFERIMENTO

Dal Capitolo 23 del manuale (tabella ufficiale):

```
SOGLIE CONTESTO
════════════════════════════════════════════════════
Metrica                  | Verde    | Giallo   | Rosso
─────────────────────────|──────────|──────────|──────
Contesto pre-occupato    | <20%     | 20-35%   | >35%
Contesto durante lavoro  | <50%     | 50-70%   | >70%
Skill nel contesto       | <1%      | 1-3%     | >3%
MCP nel contesto         | <5%      | 5-15%    | >15%
Messaggi nel contesto    | <40%     | 40-60%   | >60%
════════════════════════════════════════════════════
```

Usa `/context` in Claude Code per ottenere le percentuali attuali e compararle con questa tabella.

---

## FASE 4 — REPORT DI DIAGNOSI

Dopo aver raccolto le informazioni e analizzato la situazione, produci questo report:

```markdown
# DIAGNOSI CONTESTO — [data]

## Stato Attuale
- Contesto pre-occupato: [X]% → [Verde/Giallo/Rosso]
- MCP attivi: [lista] → peso stimato [Y]%
- CLAUDE.md: [N] righe → [Verde/Giallo/Rosso]
- Skill globali: [N] skill → [Verde/Giallo/Rosso]

## Patologie Identificate
1. [patologia] — [gravità: CRITICA/ALTA/MEDIA/BASSA]
2. [patologia] — [gravità]

## Piano di Ottimizzazione
Step 1: [azione concreta] → riduzione stimata: [X]%
Step 2: [azione concreta] → riduzione stimata: [X]%
Step 3: [azione concreta] → riduzione stimata: [X]%

## Risultato Atteso Dopo Ottimizzazione
Contesto pre-occupato stimato: [X]% → [Verde/Giallo/Rosso]
```

---

## FASE 5 — PREVENTION CHECKLIST (pre-sessione)

Prima di iniziare ogni sessione di lavoro importante:

- [ ] Verifica `/context` — sei nel verde?
- [ ] MCP pesanti necessari per questo progetto specifico? Se no, disabilita temporaneamente
- [ ] CLAUDE.md locale configurato correttamente per questo progetto?
- [ ] Autocompact è ON? (verifica con `/config`)
- [ ] Se stai per fare lavoro ad alto token (es: leggere file grandi), usa `/compact` proattivamente quando il contesto supera il 50%

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - General|General Area]]
