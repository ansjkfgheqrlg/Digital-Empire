# ═══════════════════════════════════════════════════════════════
# 📄 OUTPUT_TEMPLATES.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: TEMPLATES
# Priorità: P1 — CRITICO
# Dipendenze: Tutti i file CORE_LOGIC (i template si riempiono con i dati e i processi definiti negli altri file)
# Referenziato da: Custom Instructions — Sezione 4.1, Sezione 4.2, Sezione 4.3, Sezione 4.4, Sezione 5.2
# ═══════════════════════════════════════════════════════════════

## 📋 SCOPO

Questo file contiene i template preconfigurati per OGNI tipo di output che il Command Center produce. Garantisce che ogni risposta abbia una struttura coerente, completa e azionabile — indipendentemente dalla richiesta.

Principio fondante: "Ogni output del Command Center deve contenere: DATO → DIAGNOSI → AZIONE → PRIORITÀ → PROSSIMO STEP. Se manca uno di questi elementi, l'output è incompleto."

---

## 📖 CONTENUTO PRINCIPALE

### 1. INDICE DEI TEMPLATE
TEMPLATE DISPONIBILI
════════════════════

T1: Health Check Rapido (risposta in 2 minuti)
T2: Dashboard Rapida Settimanale
T3: Dashboard Completa Mensile
T4: OKR Status Report
T5: Sprint Mensile Nuovo
T6: Gap Analysis Report
T7: Piano d'Azione
T8: Cross-Pollination Suggerimento Settimanale
T9: Cross-Pollination Report Mensile
T10: Filtro Anti-ADD (singola idea)
T11: Allarme Attivo
T12: Decisione Binaria (A vs B)
T13: Review Settimanale Riepilogo
T14: Retrospettiva Trimestrale Riepilogo
T15: Revenue Report

REGOLA DI SELEZIONE:
Per ogni richiesta dell'utente, identifica quale
template (o combinazione di template) è più adatto.
Non inventare formati nuovi se esiste un template.

text


---

### 2. T1 — HEALTH CHECK RAPIDO
Uso: Quando l'utente chiede "come sta il business?"
o fornisce pochi dati e vuole una vista veloce.
Tempo di compilazione: 2-3 minuti
Dati necessari: status 🟢🟡🔴 di ogni pillar + 1
frase di contesto per ciascuno

TEMPLATE:
═══════════════════════════════════════════════

🏥 HEALTH CHECK — [Data]
Pillar	Status	Contesto	Azione Immediata
Agenzia CRO	[🟢🟡🔴]	[1 frase con dato]	[1 azione o "Mantieni"]
Info-Business	[🟢🟡🔴]	[1 frase con dato]	[1 azione o "Mantieni"]
YouTube	[🟢🟡🔴]	[1 frase con dato]	[1 azione o "Mantieni"]
Satellite	[🟢🟡🔴⚪]	[1 frase con dato]	[1 azione o "Nessuna"]
ALLARMI ATTIVI: [Nessuno / Lista allarmi]

FOCUS QUESTA SETTIMANA:
[1 frase che indica la priorità #1]

═══════════════════════════════════════════════

text


---

### 3. T2 — DASHBOARD RAPIDA SETTIMANALE
Uso: Nella review settimanale (Step 2)
Tempo di compilazione: 10-15 minuti
Dati necessari: numeri chiave della settimana

TEMPLATE:
═══════════════════════════════════════════════

📊 DASHBOARD RAPIDA — Settimana [N] ([Date])
Status Pillar
Pillar	Status	Contesto
Agenzia CRO	[🟢🟡🔴]	[Es: "3 clienti attivi, 1 proposta in attesa"]
Info-Business	[🟢🟡🔴]	[Es: "Funnel attivo, 12 vendite questa settimana"]
YouTube	[🟢🟡🔴]	[Es: "2 video pubblicati, CTR 6.2%"]
Satellite	[🟢🟡🔴⚪]	[Es: "KDP stabile, AI non avviato"]
Numeri Chiave
Metrica	Questa Sett.	Sett. Prec.	Trend
Nuovi lead agenzia	[N]	[N]	[↑↓→]
Revenue incassato	€[N]	€[N]	[↑↓→]
Vendite info-biz	[N] (€[N])	[N] (€[N])	[↑↓→]
Video pubblicati	[N]	[N]	[↑↓→]
Lead da YouTube	[N]	[N]	[↑↓→]
Azione Cross-Pollination
[✅ Fatta: (descrizione)] / [❌ Non fatta — da fare entro: (giorno)]

Allarmi
[Nessuno / Lista con azione]

Focus Prossima Settimana
[1 frase]

═══════════════════════════════════════════════

text


---

### 4. T3 — DASHBOARD COMPLETA MENSILE
Uso: Nella review mensile (Step 1)
Tempo di compilazione: 30-45 minuti
Dati necessari: tutti i dati del mese per ogni pillar
Nota: Il template completo è in DASHBOARD_ENGINE.md
Sezioni 3-9. Qui il formato di OUTPUT finale.

TEMPLATE:
═══════════════════════════════════════════════

📊 DASHBOARD EMPIRE — [Mese] [Anno]
Overview
Pillar	Revenue	% Totale	Target %	Status
Agenzia CRO	€[N]	[N]%	50-60%	[🟢🟡🔴]
Info-Business	€[N]	[N]%	20-30%	[🟢🟡🔴]
YouTube	€[N]	[N]%	5-15%	[🟢🟡🔴]
KDP	€[N]	[N]%	2-5%	[🟢🟡🔴]
AI Influencer	€[N]	[N]%	2-5%	[🟢🟡🔴⚪]
TOTALE	€[N]	100%		
Trend vs mese prec.: [↑↓→] ([+/-]%)
Target Q: €[N] — Progresso: [N]%

Agenzia CRO — Highlights
Metrica	Target	Reale	Status
Lead qualificati	[N]	[N]	[🟢🟡🔴]
Close rate	[N]%	[N]%	[🟢🟡🔴]
Revenue	€[N]	€[N]	[🟢🟡🔴]
NPS clienti	>8	[N]	[🟢🟡🔴]
Health: [Pipeline OK/Debole] | [Delivery OK/Sovraccarico] | [Outreach Attivo/Fermo]

Info-Business — Highlights
Metrica	Target	Reale	Status
Nuovi lead lista	[N]	[N]	[🟢🟡🔴]
Revenue info-biz	€[N]	€[N]	[🟢🟡🔴]
Open rate email	>25%	[N]%	[🟢🟡🔴]
Funnel CR	>2%	[N]%	[🟢🟡🔴]
Lancio attivo: [Sì: (dettagli) / No]
Funnel evergreen: [Attivo / Non attivo]

YouTube — Highlights
Metrica	Target	Reale	Status
Video pubblicati	[N]	[N]	[🟢🟡🔴]
Lead da YouTube	[N]	[N]	[🟢🟡🔴]
Nuovi iscritti	[N]	[N]	[🟢🟡🔴]
CTR medio	>5%	[N]%	[🟢🟡🔴]
Content mix: Anchor [N] / Shift [N] / Conversion [N]

Cross-Pollination
Metrica	Risultato	Target
Azioni eseguite	[N]	≥4
Studenti → lead agenzia	[N]	—
Lead YT → opt-in info	[N]	—
Revenue cross-poll	€[N]	↑
Allarmi
ALM	Stato	Azione
1 🔴 Revenue agenzia ↓↓	[OK/⚠️]	[Azione se attivo]
2 🔴 Zero vendite info 30gg	[OK/⚠️]	[Azione se attivo]
3 🔴 Zero video YT 3 sett.	[OK/⚠️]	[Azione se attivo]
4 🔴 Zero cross-poll 30gg	[OK/⚠️]	[Azione se attivo]
5 🟡 OKR < 30% metà Q	[OK/⚠️]	[Azione se attivo]
6 🟡 Satellite > 10%	[OK/⚠️]	[Azione se attivo]
Azioni Prioritarie Mese Prossimo
[Azione #1 — pillar — KR collegato]
[Azione #2 — pillar — KR collegato]
[Azione #3 — pillar — KR collegato]
═══════════════════════════════════════════════

text


---

### 5. T4 — OKR STATUS REPORT
Uso: Nella review mensile (Step 2) e quando l'utente
chiede "come stanno gli OKR?"
Tempo di compilazione: 15-20 minuti

TEMPLATE:
═══════════════════════════════════════════════

🎯 OKR STATUS — Q[N] [Anno] (Mese [1/2/3] di 3)
Progresso per Pillar
Pillar	KR	Target Q	Progresso	%	Status
Agenzia	KR1: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
Agenzia	KR2: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
Agenzia	KR3: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
Info-Biz	KR1: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
Info-Biz	KR2: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
YouTube	KR1: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
YouTube	KR2: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
Cross	KR1: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
Cross	KR2: [breve]	[N]	[N]	[N]%	[🟢🟡🔴]
Media complessiva: [N]%
Target per questo punto del Q: [30-35% / 60-65% / 90-100%]
Valutazione: [On Track / A Rischio / Off Track]

KR più forte
[Quale KR sta andando meglio e perché]

KR più debole
[Quale KR è più indietro, causa, azione correttiva]

3 Priorità del Q — Status
#	Priorità	Progresso	Note
1	[Descrizione]	[🟢🟡🔴]	[Stato attuale]
2	[Descrizione]	[🟢🟡🔴]	[Stato attuale]
3	[Descrizione]	[🟢🟡🔴]	[Stato attuale]
Prossimo Step
[Cosa fare questo mese per migliorare i KR più deboli]

═══════════════════════════════════════════════

text


---

### 6. T5 — SPRINT MENSILE NUOVO
Uso: Nella review mensile (Step 4) e quando l'utente
chiede "cosa devo fare questo mese?"

TEMPLATE:
═══════════════════════════════════════════════

🏃 SPRINT MENSILE — [Mese] [Anno]
Focus del Mese
"Questo mese mi concentro su [1 frase chiara]."

7 Task Prioritari
#	Task	Pillar	KR	Sett.	Status
1	[Task specifico e misurabile]	[AGZ]	[KR#]	[S1]	⬜
2	[Task specifico e misurabile]	[AGZ]	[KR#]	[S1-2]	⬜
3	[Task specifico e misurabile]	[AGZ]	[KR#]	[S2]	⬜
4	[Task specifico e misurabile]	[IB]	[KR#]	[S2-3]	⬜
5	[Task specifico e misurabile]	[IB]	[KR#]	[S3]	⬜
6	[Task specifico e misurabile]	[YT]	[KR#]	[S3-4]	⬜
7	[Task specifico e misurabile]	[CROSS]	[KR#]	[S4]	⬜
Verifica Distribuzione
Pillar	Task	Target	Status
Agenzia	[N]/7	3-4	[✅/⚠️]
Info-Biz	[N]/7	1-2	[✅/⚠️]
YouTube	[N]/7	1	[✅/⚠️]
Cross-Poll	[N]/7	0-1	[✅/⚠️]
Satellite	[N]/7	0-1	[✅/⚠️]
Not To Do Questo Mese
[Cosa NON faccio] — Motivo: [perché]
[Cosa NON faccio] — Motivo: [perché]
[Cosa NON faccio] — Motivo: [perché]
Metriche di Successo
"Questo mese è un successo se: [condizione misurabile]"

═══════════════════════════════════════════════

text


---

### 7. T6 — GAP ANALYSIS REPORT
Uso: Nella review mensile (Step 3) e quando l'utente
chiede "dove sono i problemi?"

TEMPLATE:
═══════════════════════════════════════════════

🔍 GAP ANALYSIS — [Data]
Tabella Gap
Pillar	Area	Target	Reale	Gap	Gap %	Causa Radice
Agenzia	[Metrica]	[N]	[N]	[N]	[N]%	[Causa]
Info-Biz	[Metrica]	[N]	[N]	[N]	[N]%	[Causa]
YouTube	[Metrica]	[N]	[N]	[N]	[N]%	[Causa]
Prioritizzazione (Formula Impatto)
Pillar	Gap	Dim.(1-5)	Leva(1-5)	Vel.(1-5)	IMPATTO
[Pillar]	[Gap]	[N]	[N]	[N]	[N] ⭐
[Pillar]	[Gap]	[N]	[N]	[N]	[N]
[Pillar]	[Gap]	[N]	[N]	[N]	[N]
Decisione
Focus su: [Gap con impatto più alto]
Motivo: [Perché questo gap prima degli altri]
Tempo stimato per risoluzione: [N settimane]

Azione Immediata
[3 azioni concrete per questa settimana]

═══════════════════════════════════════════════

text


---

### 8. T7 — PIANO D'AZIONE
Uso: Dopo una gap analysis, dopo una decisione,
dopo un allarme attivato.

TEMPLATE:
═══════════════════════════════════════════════

⚡ PIANO D'AZIONE — [Titolo/Obiettivo]
Contesto
Problema/Opportunità: [Descrizione]
Pillar: [Quale]
Causa radice: [Da gap analysis o diagnosi]
Obiettivo: Da [valore attuale] a [valore target] entro [data]

Azioni Questa Settimana (max 3)
#	Azione	Entro	Metrica di completamento
1	[Azione specifica]	[Giorno]	[Come sai che è fatta]
2	[Azione specifica]	[Giorno]	[Come sai che è fatta]
3	[Azione specifica]	[Giorno]	[Come sai che è fatta]
Azioni Questo Mese (5-7 task)
#	Task	Settimana	KR collegato
1	[Task]	S1	[KR#]
2	[Task]	S1-2	[KR#]
3	[Task]	S2	[KR#]
4	[Task]	S3	[KR#]
5	[Task]	S3-4	[KR#]
Misurazione Progresso
Metrica principale: [Cosa misuri]
Cadenza: [Ogni quanto la controlli]
Target intermedio (2 sett.): [Valore]
Target finale (fine mese): [Valore]
Not To Do
#	Cosa NON faccio	Perché
1	[Attività sospesa]	[Motivo]
2	[Attività sospesa]	[Motivo]
3	[Attività sospesa]	[Motivo]
Prossima Review
Data: [Quando]
Cosa verifico: [Metrica]
Se non c'è progresso: [Piano B]
═══════════════════════════════════════════════

text


---

### 9. T8 — CROSS-POLLINATION SUGGERIMENTO SETTIMANALE
Uso: Nella review settimanale (Step 3) e quando
l'utente chiede "quale sinergia attivo?"

TEMPLATE:
═══════════════════════════════════════════════

🔄 CROSS-POLLINATION — Settimana [N]
Stato Flussi Recenti
Flusso	Ultima Esecuzione	Status
1. Domande clienti → idee	[Data o "Mai"]	[✅/⚠️]
3. Caso studio → content	[Data o "Mai"]	[✅/⚠️]
6. Studenti → lead agenzia	[Data o "Mai"]	[✅/⚠️]
9. YT → lead info-biz	[Data o "Mai"]	[✅/⚠️]
11. Content da altri pillar	[Data o "Mai"]	[✅/⚠️]
Azione Suggerita Questa Settimana
Flusso: [N] — [Nome del flusso]
Azione: [Descrizione specifica dell'azione]
Tempo stimato: [N] minuti
Output atteso: [Cosa produce]
Riutilizzo: [Come l'output alimenta altri pillar]

Motivo della scelta: [Perché questa azione è la più impattante questa settimana]

Registro
Settimana [N] | Flusso [N] | Azione: _________
Risultato: _________ (compilare dopo l'esecuzione)

═══════════════════════════════════════════════

text


---

### 10. T9 — CROSS-POLLINATION REPORT MENSILE
Uso: Nella review mensile (Step 5)

TEMPLATE:
═══════════════════════════════════════════════

🔄 CROSS-POLLINATION REPORT — [Mese] [Anno]
Azioni Eseguite
Sett.	Flusso	Azione	Risultato
S1	[N]	[Descrizione]	[Risultato]
S2	[N]	[Descrizione]	[Risultato]
S3	[N]	[Descrizione]	[Risultato]
S4	[N]	[Descrizione]	[Risultato]
Totale: [N]/4 — Status: [🟢 ≥4 / 🟡 2-3 / 🔴 0-1]

Bridge Metrics
Flusso	Mese Corrente	Mese Precedente	Trend
Studenti → lead agenzia	[N]	[N]	[↑↓→]
Clienti → acquisto corso	[N]	[N]	[↑↓→]
Lead YT → opt-in info	[N]	[N]	[↑↓→]
Lettori KDP → opt-in	[N]	[N]	[↑↓→]
Revenue cross-poll	€[N]	€[N]	[↑↓→]
Flussi Più Attivi
[Flusso N] — [Perché funziona]
[Flusso N] — [Perché funziona]
Flussi Dormienti (azione suggerita)
[Flusso N] — Suggerimento: [Azione]
[Flusso N] — Suggerimento: [Azione]
Focus Cross-Poll Mese Prossimo
[Quale flusso attivare o intensificare e perché]

═══════════════════════════════════════════════

text


---

### 11. T10 — FILTRO ANTI-ADD (SINGOLA IDEA)
Uso: Quando l'utente presenta una nuova idea,
opportunità, progetto o impulso.

TEMPLATE:
═══════════════════════════════════════════════

🔍 FILTRO ANTI-ADD — Idea: "[Nome dell'idea]"
Fonte: [Da dove arriva: podcast / competitor / impulso / cliente / dato]

Le 5 Domande
D1: È collegata ai 3 pillar?
├── Agenzia CRO: [Sì direttamente / Indirettamente / No]
├── Info-Business: [Sì direttamente / Indirettamente / No]
├── YouTube: [Sì direttamente / Indirettamente / No]
└── Verdetto D1: [SÌ → Procedi / INDIRETTAMENTE → Backlog / NO → SCARTA]

D2: Tutti i pillar sono 🟢?
├── Agenzia: [🟢🟡🔴]
├── Info-Biz: [🟢🟡🔴]
├── YouTube: [🟢🟡🔴]
└── Verdetto D2: [Tutti 🟢 → Procedi / Almeno 1 🟡 → FERMA / Almeno 1 🔴 → FERMA]

D3: Muove un KR definito?
├── KR candidato: [Quale KR potrebbe muovere]
├── Collegamento diretto? [Sì / No / Indiretto]
└── Verdetto D3: [SÌ → Procedi / NO → BACKLOG]

D4: Ho capacità senza togliere dal core?
├── Tempo richiesto: [N] ore/settimana per [N] settimane
├── Da dove prendo il tempo? [Tempo libero / Satellite / Pillar principale]
└── Verdetto D4: [SÌ → Procedi / NO → POSPONI]

D5: Se scomparisse, il business ne soffrirebbe?
├── Impatto su revenue: [Sì / No]
├── Impatto su pillar: [Sì / No]
├── Impatto su KR: [Sì / No]
└── Verdetto D5: [SÌ → AGISCI / NO → DISTRAZIONE]

Esito Finale
Esito	Descrizione
[✅/📋/⏸️/🚫/🛑]	[Spiegazione dell'esito]
Azione
[Se ✅ AGISCI: le prime 3 azioni concrete]
[Se 📋 BACKLOG: data di rivalutazione]
[Se ⏸️ POSPONI: condizione per riprendere]
[Se 🚫 SCARTA: motivo definitivo]
[Se 🛑 BLOCCATA: quale pillar risolvere prima]

═══════════════════════════════════════════════

text


---

### 12. T11 — ALLARME ATTIVO
Uso: Quando un allarme viene rilevato nella dashboard
o nella review.

TEMPLATE:
═══════════════════════════════════════════════

⚠️ ALLARME ALM-[N] ATTIVO — [Titolo]
Livello: [🔴 CRITICO / 🟡 ATTENZIONE]
Attivato il: [Data]
Condizione: [Descrizione della condizione che ha attivato l'allarme]

Dati
Metrica	Soglia Allarme	Valore Attuale	Scostamento
[Metrica]	[Soglia]	[Valore]	[Quanto sopra/sotto]
Diagnosi
Causa probabile: [Da albero diagnostico o analisi]
Causa radice: [Se identificata]

Protocollo di Risposta
STEP 1 — IMMEDIATO (entro 24h):
[Azione immediata dal protocollo in SOGLIE_ALLARME.md]

STEP 2 — QUESTA SETTIMANA:

#	Azione	Entro
1	[Azione]	[Giorno]
2	[Azione]	[Giorno]
3	[Azione]	[Giorno]
STEP 3 — MONITORAGGIO:
[Cosa monitorare, con quale frequenza]

Riallocazione Risorse (se applicabile)
Pillar	% Prima	% Durante Allarme
Agenzia	[N]%	[N]%
Info-Biz	[N]%	[N]%
YouTube	[N]%	[N]%
Satellite	[N]%	[N]%
Condizione di Chiusura
[Cosa deve succedere perché l'allarme si chiuda]

═══════════════════════════════════════════════

text


---

### 13. T12 — DECISIONE BINARIA (A vs B)
Uso: Quando l'utente deve scegliere tra 2 opzioni.

TEMPLATE:
═══════════════════════════════════════════════

⚖️ DECISIONE: [Opzione A] vs [Opzione B]
Contesto
[Perché questa decisione è necessaria ora]

Matrice di Valutazione
Criterio	Opz. A: [Nome]	Opz. B: [Nome]
1. Impatto revenue (1-5)	[N]	[N]
2. Allineamento gerarchia (1-5)	[N]	[N]
3. Velocità risultato (1-5)	[N]	[N]
4. Rischio (1=alto, 5=basso)	[N]	[N]
5. Effetto cross-pollination (1-5)	[N]	[N]
6. Reversibilità (1-5)	[N]	[N]
TOTALE	[N]/30	[N]/30
Analisi
Differenza: [N] punti
Interpretazione:
[>5 punti: scelta chiara / 3-5: leggero vantaggio / <3: quasi uguali]

Raccomandazione
Scegli: [Opzione A/B]
Motivo principale: [1 frase]
Rischio: [Cosa potrebbe andare storto]
Piano B: [Se non funziona, cosa fai]

Tiebreaker (se quasi uguali)
"Quale opzione, se FALLISCE, causa MENO danni?"
→ [Risposta]

═══════════════════════════════════════════════

text


---

### 14. T13 — REVIEW SETTIMANALE RIEPILOGO
Uso: Output finale della review settimanale (dopo
aver completato tutti i 6 step)

TEMPLATE:
═══════════════════════════════════════════════

📋 REVIEW SETTIMANALE — [Data]
Sprint: [N]/7 task completati ([N]%)
Task completati questa sett.	Task in corso	Task bloccati
[Lista]	[Lista]	[Lista + motivo]
Pillar Status: AGZ [🟢🟡🔴] | IB [🟢🟡🔴] | YT [🟢🟡🔴] | SAT [🟢🟡🔴⚪]
Cross-Poll: [✅ Flusso N: (azione)] / [❌ Non fatta]
Allarmi: [Nessuno] / [ALM-N attivo: (azione)]
Idee filtrate: [N] → [Esiti: N✅ N📋 N🚫]
Focus Prossima Settimana
"La prossima settimana mi concentro su: [1 frase]"
Task da muovere: #[N], #[N], #[N]

═══════════════════════════════════════════════

text


---

### 15. T14 — RETROSPETTIVA TRIMESTRALE RIEPILOGO
Uso: Output finale della retrospettiva (usato insieme
al template completo in RETROSPETTIVA_ENGINE.md)

TEMPLATE:
═══════════════════════════════════════════════

📋 RETROSPETTIVA Q[N] [Anno] — Riepilogo
Numeri del Trimestre
Revenue totale Q: €[N] ([+/-]% vs Q precedente)
OKR Completion Rate: [N]%
Sprint Completion media: [N]%
Azioni cross-poll: [N]/12
Top 3 Lezioni
[Lezione + come impatta Q+1]
[Lezione + come impatta Q+1]
[Lezione + come impatta Q+1]
KEEP (continua a fare)
[Cosa]
[Cosa]
[Cosa]
STOP (smetti di fare)
[Cosa]
[Cosa]
[Cosa]
START (inizia a fare)
[Cosa]
[Cosa]
[Cosa]
Decisione Migliore: [Quale]
Decisione Peggiore: [Quale]
Domanda Chiave per Q+1
"[La domanda più importante da rispondere nel prossimo trimestre]"

═══════════════════════════════════════════════

text


---

### 16. T15 — REVENUE REPORT
Uso: Nella review mensile (Step 6) e quando l'utente
chiede "come vanno i numeri?"

TEMPLATE:
═══════════════════════════════════════════════

💰 REVENUE REPORT — [Mese] [Anno]
Revenue del Mese
Pillar	Revenue	vs Mese Prec.	Trend
Agenzia CRO	€[N]	[+/-]%	[↑↓→]
Info-Business	€[N]	[+/-]%	[↑↓→]
YouTube	€[N]	[+/-]%	[↑↓→]
KDP	€[N]	[+/-]%	[↑↓→]
AI Influencer	€[N]	[+/-]%	[↑↓→]
TOTALE	€[N]	[+/-]%	[↑↓→]
Distribuzione vs Target
Pillar	% Attuale	% Target	Status
Agenzia	[N]%	50-60%	[✅/⚠️]
Info-Biz	[N]%	20-30%	[✅/⚠️]
YouTube	[N]%	5-15%	[✅/⚠️]
Satellite	[N]%	5-10%	[✅/⚠️]
Trend Trimestrale
Mese	Revenue	Trend
[M1]	€[N]	—
[M2]	€[N]	[↑↓→]
[M3 attuale]	€[N]	[↑↓→]
Totale Q	€[N]	
Target Q	€[N]	
Progresso	[N]%	
Revenue da Cross-Pollination
€[N] questo mese (dettaglio: [da dove])

Insight
[1-2 frasi su cosa dicono i numeri e cosa fare]

═══════════════════════════════════════════════

text


---

## 🔧 COME UTILIZZARE QUESTO FILE

**Quando consultarlo:**
- SEMPRE prima di generare una risposta — identifica quale template usare
- Se la richiesta non corrisponde a nessun template → usa il più vicino e adatta
- Se la richiesta richiede più template → combinali (es: Dashboard + OKR Status)

**Come integrare nella risposta:**
1. Scegli il template appropriato
2. Riempi con i dati dell'utente
3. Se mancano dati → lascia "[DATO MANCANTE — fornisci: ___]"
4. Verifica che l'output contenga SEMPRE: Dato → Diagnosi → Azione → Priorità → Prossimo Step
5. Non usare template vuoti — se non hai dati sufficienti, chiedi prima i dati

**Regole di formattazione:**
- Usa SEMPRE tabelle Markdown per i dati
- Usa SEMPRE 🟢🟡🔴 per gli status
- Usa SEMPRE heading ## e ### per la struttura
- Usa SEMPRE grassetto per i valori chiave
- Ogni output termina con "Prossimo Step" o "Focus"

---

## 🔗 COLLEGAMENTI

- **Dipende da**: Tutti i file CORE_LOGIC (i template si riempiono con i dati e processi degli altri file)
- **Alimenta**: Tutte le risposte del Command Center usano questi template
- **Custom Instructions**: Sezione 4.1-4.4, Sezione 5.2

---

## 💡 ESEMPI PRATICI

### Esempio: Selezione del template corretto

| L'utente dice... | Template da usare |
|-----------------|-------------------|
| "Come sta il business?" | T1 (Health Check Rapido) |
| "Facciamo la review settimanale" | T2 + T13 |
| "Compila la dashboard del mese" | T3 |
| "Come stanno gli OKR?" | T4 |
| "Cosa faccio questo mese?" | T5 (Sprint Nuovo) |
| "Dove sono i problemi?" | T6 (Gap Analysis) |
| "Ho un allarme attivo" | T11 |
| "Devo scegliere tra A e B" | T12 |
| "Ho un'idea per un podcast" | T10 (Filtro Anti-ADD) |
| "Quale sinergia attivo?" | T8 |
| "Come vanno i numeri?" | T15 |
| "È fine trimestre" | T14 + T4 + T5 |

---

## ⚠️ NOTE E AVVERTENZE

1. **I template sono STRUTTURE, non gabbie.** Se una situazione richiede un formato leggermente diverso, adatta. Ma parti sempre dal template — non da zero.

2. **Non usare MAI un template vuoto come risposta.** I template servono per essere RIEMPITI con dati reali. Un template vuoto è una lista di domande, non una risposta.

3. **Ogni template include la sezione "Azione/Prossimo Step".** Se la tua risposta non contiene un'azione concreta → non è una risposta del Command Center, è un report passivo. Aggiungi sempre l'azione.

4. **Combina i template quando necessario.** La review mensile usa T3 + T4 + T6 + T5 + T9 + T15 in sequenza. Non è un problema — ogni template copre una funzione specifica.

5. **La consistenza è più importante della perfezione.** Usa sempre lo stesso template per lo stesso tipo di richiesta. L'utente deve riconoscere il formato e sapere dove trovare le informazioni.