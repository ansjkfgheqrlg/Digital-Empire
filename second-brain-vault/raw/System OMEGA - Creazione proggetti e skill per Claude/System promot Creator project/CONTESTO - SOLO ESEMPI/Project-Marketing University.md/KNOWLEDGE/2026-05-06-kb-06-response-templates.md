# KB_06_RESPONSE_TEMPLATES

> Source: File system (`System OMEGA - Creazione proggetti e skill per Claude\System promot Creator project\CONTESTO - SOLO ESEMPI\Project-Marketing University.md\KNOWLEDGE\KB_06_RESPONSE_TEMPLATES.md`)
> Collected: 2026-05-06
> Published: Unknown

# ═══════════════════════════════════════════════════════════════
# 📄 KB_06_RESPONSE_TEMPLATES.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: TEMPLATES
# Priorità: P0
# Dipendenze: KB_02_EXTRACTION_ENGINE.md (template scheda),
#             KB_03_PROJECT_CONNECTION_MATRIX.md (collegamento progetti),
#             KB_04_STUDY_METHOD_PIPELINE.md (report applicazione/validazione),
#             KB_05_WEEKLY_MONTHLY_ROUTINE.md (template review)
# Referenziato da: Custom Instructions — Sezione 4.1, 4.2, 4.4
# ═══════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────
# 📋 SCOPO
# ──────────────────────────────────────────────────────

Questo file contiene i template completi per OGNI tipo di output
che l'AI genera in Marketing University.

L'obiettivo è garantire:
1. COERENZA: ogni risposta segue lo stesso formato strutturato
2. COMPLETEZZA: nessun campo obbligatorio viene dimenticato
3. AZIONABILITÀ: ogni output contiene azioni concrete
4. NAVIGABILITÀ: l'utente trova immediatamente ciò che cerca

L'AI NON deve mai restituire template vuoti. Deve COMPILARLI
con i dati specifici della situazione. Il template è la STRUTTURA,
il contenuto è sempre specifico e contestualizzato.


# ──────────────────────────────────────────────────────
# 📖 SEZIONE 1: TEMPLATE W1 — ANALISI MATERIALE NUOVO
# ──────────────────────────────────────────────────────

## 1.1 — Template Completo W1

Questo template viene utilizzato quando l'utente fornisce materiale
formativo e l'AI esegue il Workflow W1 (Analisi Materiale Nuovo).
🔬 ANALISI MATERIALE — [Nome Materiale]
📋 Panoramica Analisi
Campo	Valore
Fonte	[Nome completo del corso/libro/guida/video]
Area primaria	AREA_[N] — [Nome Area]
Aree secondarie	[Se applicabile]
Qualità operativa	[Alta / Media / Bassa]
Lunghezza materiale	[Breve / Medio / Lungo / Ultra]
Framework estratti	[N]
Concetti scartati	[N] (con motivo)
📦 Framework Estratti
Framework 1 di [N]: [Nome Framework]
┌─────────────────────────────────────────────────────────────┐
│ 📋 SCHEDA FRAMEWORK ESTRATTO │
│ ID: [AREA][SOTTOAREA][NUM][YYMMDD] │
├─────────────────────────────────────────────────────────────┤
│ │
│ ① FONTE: [Nome completo] │
│ │
│ ② DATA STUDIO: [GG/MM/AAAA] │
│ │
│ ③ CLASSIFICAZIONE: │
│ Area: AREA[N] — [Nome Area] │
│ Sottoarea: [XY] — [Nome Sottoarea] │
│ Argomento: [codice] — [Nome Argomento] │
│ │
│ ④ CONCETTO CHIAVE: │
│ [1-2 righe: la lezione fondamentale] │
│ │
│ ⑤ FRAMEWORK OPERATIVO: │
│ Nome: "[Nome del Framework]" │
│ Step 1: [azione specifica] │
│ Step 2: [azione specifica] │
│ Step 3: [azione specifica] │
│ [...] │
│ Step N: [azione specifica] │
│ │
│ ⑥ ESEMPIO PRATICO: │
│ [3-8 righe: esempio concreto nel contesto │
│ Digital Empire o dal materiale originale] │
│ │
│ ⑦ COLLEGAMENTO PROGETTI: │
│ Progetto primario: [emoji + nome] │
│ Fase specifica: [fase del progetto] │
│ Situazione trigger: [quando usare] │
│ Progetti secondari: [se applicabile] │
│ │
│ ⑧ AZIONE ENTRO 7 GIORNI: │
│ AZIONE: [specifica, misurabile, eseguibile] │
│ TEMPO STIMATO: [ore/minuti] │
│ RISULTATO ATTESO: [cosa ci si aspetta] │
│ SCADENZA: [data] │
│ │
│ ⑨ STATUS: │
│ ✅ Studiato ✅ Estratto □ Applicato □ Validato │
│ Data ultimo aggiornamento: [GG/MM/AAAA] │
│ │
└─────────────────────────────────────────────────────────────┘

Framework 2 di [N]: [Nome Framework]
[Stessa struttura scheda — ripetere per ogni framework]

🗑️ Concetti Scartati
#	Concetto	Motivo dello Scarto
1	[concetto]	[Puramente teorico / Non step-by-step / Non riutilizzabile / Già catalogato]
2	[concetto]	[motivo]
📊 Report Estrazione
Metrica	Valore
Materiale analizzato	[Nome]
Lunghezza stimata	[N parole]
Qualità operativa	[Alta/Media/Bassa]
Framework estratti	[N]
Concetti scartati	[N]
Concetti trasformati (teoria → framework)	[N]
Aree coperte	[lista]
Progetti collegati	[lista emoji + nomi]
Azioni definite	[N]
Segnalazioni:
[Eventuali contraddizioni con framework esistenti]
[Eventuali gap nella biblioteca evidenziati]
[Eventuali suggerimenti di studio complementare]
[Eventuali parti del materiale non estraibili e perché]
⏭️ Prossimi Passi
Entro 7 giorni: Applica le [N] azioni definite sopra
Venerdì: Review settimanale per verificare lo status
Suggerimento studio successivo: [se rilevante]
text


## 1.2 — Regole di Compilazione Template W1
REGOLE OBBLIGATORIE:

OGNI scheda deve avere TUTTI i 9 campi compilati — nessuno vuoto
La sezione "Concetti Scartati" è OBBLIGATORIA anche se vuota
(in quel caso: "Nessun concetto scartato — tutti estraibili")
Il "Report Estrazione" è SEMPRE presente alla fine
I "Prossimi Passi" sono SEMPRE l'ultima sezione
SE il materiale genera più di 4 framework:
→ Presenta i primi 4 nel formato completo
→ Per i restanti, usa formato compatto (solo campi ④⑤⑦⑧)
→ Chiedi: "Vuoi le schede complete anche per i restanti [N]?"
SE il materiale è di qualità bassa:
→ La "Panoramica Analisi" deve segnalarlo chiaramente
→ Spiega PERCHÉ e suggerisci alternative
text


## 1.3 — Variante W1: Materiale Parziale / Appunti

Quando l'utente fornisce appunti parziali invece del materiale completo:
🔬 ANALISI APPUNTI — [Argomento]
⚠️ Nota: Questa analisi è basata su appunti parziali,
non sul materiale originale completo. Alcuni framework
potrebbero essere incompleti. Dove ho integrato con
conoscenza propria, è segnalato esplicitamente.

[... resto del template W1 come sopra ...]

⚠️ Elementi Potenzialmente Incompleti:
[Step X del Framework Y]: integrato dall'AI —
verificare con materiale originale
[Esempio nel Framework Z]: creato dall'AI —
non presente negli appunti
text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 2: TEMPLATE W2 — RICERCA FRAMEWORK RAPIDA
# ──────────────────────────────────────────────────────

## 2.1 — Template Completo W2

Questo template viene utilizzato quando l'utente cerca un concetto
o framework specifico nella biblioteca.
🔍 FRAMEWORK: [Nome Framework]
📍 Posizione nella Biblioteca
Campo	Valore
Area	AREA_[N] — [Nome]
Sottoarea	[XY] — [Nome]
Argomento	[codice] — [Nome]
ID Scheda	[ID se esiste nel registro]
Fonte originale	[da dove è stato estratto]
🔧 Framework Step-by-Step
Nome: [Nome del Framework]

Step	Azione	Dettaglio
1	[Verbo + azione]	[Spiegazione breve di come eseguire lo step]
2	[Verbo + azione]	[Spiegazione]
3	[Verbo + azione]	[Spiegazione]
N	[Verbo + azione]	[Spiegazione]
💡 Esempio Pratico
[Esempio concreto del framework in azione — 3-8 righe.
Se il framework è stato applicato in passato, usa
quell'esperienza come esempio.]

🔗 Collegamento ai Progetti
Progetto	Fase	Quando Usarlo
[emoji + nome]	[fase]	[trigger specifico]
[emoji + nome]	[fase]	[trigger specifico]
📝 Ultima Applicazione
[SE il framework è stato applicato in passato:]

Data: [GG/MM/AAAA]
Progetto: [dove]
Risultato: [cosa è successo]
Validato: [Sì/No/In attesa]
[SE mai applicato:]

Questo framework non è ancora stato applicato.
Suggerimento: applicalo in [progetto] → [fase] → [azione specifica].

⏭️ Applicazione Suggerita ORA
Contesto attuale: [basato su ciò che l'utente sta facendo]
Azione suggerita: [come applicare questo framework adesso]
Tempo stimato: [quanto serve]

text


## 2.2 — Variante W2: Framework Non Trovato

Quando il framework richiesto NON esiste nel registro:
🔍 RICERCA: [Concetto Richiesto]
❌ Framework Non Trovato nel Registro
Il concetto "[concetto]" non ha una scheda framework dedicata
nella biblioteca.

Possibili Cause:
Non ancora studiato: nessun materiale su questo tema
è stato analizzato
Classificazione diversa: potrebbe essere catalogato
con un nome diverso
Cosa Posso Fare:
OPZIONE A — Cerco nei Framework Precaricati (KB_14):
[SE trovato in KB_14: mostra il framework]
[SE non trovato: "Non presente neanche nei framework precaricati"]

OPZIONE B — Genero un Framework dalla Mia Conoscenza:

⚠️ Questo framework è generato dalla conoscenza dell'AI,
NON estratto da materiale formativo specifico dell'utente.
Potrebbe necessitare di validazione con fonti esterne.

[Framework generato in formato step-by-step]

OPZIONE C — Suggerisco Materiale da Studiare:
Per costruire un framework solido su "[concetto]", suggerisco
di studiare:

[Fonte 1]: [perché è rilevante]
[Fonte 2]: [perché è rilevante]
Area della biblioteca: AREA_[N] → [Sottoarea]
text


## 2.3 — Variante W2: Esplorazione Area

Quando l'utente chiede "mostra tutti i framework dell'area X":
📚 BIBLIOTECA — AREA_[N]: [Nome Area]
Panoramica Area
Metrica	Valore
Schede totali	[N]
Schede validate	[N]
Schede in attesa di applicazione	[N]
Sottoaree coperte	[N]/4
Sottoarea [XA] — [Nome]
#	Framework	ID	Status	Progetto Collegato
1	[Nome]	[ID]	✅✅✅✅ / ✅✅□□ / etc.	[emoji]
2	[Nome]	[ID]	[status]	[emoji]
Sottoarea [XB] — [Nome]
#	Framework	ID	Status	Progetto Collegato
1	[Nome]	[ID]	[status]	[emoji]
[Ripetere per tutte le sottoaree]

Sottoarea [XC] — [Nome]
[Se vuota]: > 🔴 Nessun framework in questa sottoarea — GAP identificato

Sottoarea [XD] — [Nome]
[Materiale di riferimento disponibile]

📊 Gap Analysis Area_[N]
Sottoarea	Schede	Livello	Azione Suggerita
[XA]	[N]	🟢/🟡/🔴	[Se gap: "Studiare [materiale] per colmare"]
[XB]	[N]	🟢/🟡/🔴	[azione]
[XC]	[N]	🟢/🟡/🔴	[azione]
[XD]	[N]	🟢/🟡/🔴	[azione]
text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 3: TEMPLATE W3 — SUGGERIMENTO STUDIO
# ──────────────────────────────────────────────────────

## 3.1 — Template Completo W3

Questo template viene utilizzato quando l'utente chiede cosa studiare.
📖 SUGGERIMENTO STUDIO — Settimana del [data]
🎯 Diagnosi
Domanda chiave: Quale progetto ha il problema più urgente?
[SE l'utente ha specificato il problema:]

Problema identificato: "[problema]"
Progetto: [emoji + nome]
Fase: [fase del progetto]

[SE l'utente NON ha specificato:]

Per suggerirti cosa studiare, ho bisogno di sapere:
Quale progetto ha il problema più urgente questa settimana?

Opzioni rapide:

⚡ Agency — [possibile problema suggerito basandosi sul contesto]
🎥 YouTube — [possibile problema]
📚 KDP — [possibile problema]
🤖 AI Lab — [possibile problema]
🧠 Strategy — [possibile problema]
Rispondi con il numero o descrivi il problema.

📚 Percorso di Studio Suggerito
Problema → Area → Materiale → Azione
Step	Dettaglio
Problema	[Descrizione specifica del problema]
Area Biblioteca	AREA_[N] → [Sottoarea] → [Argomento]
Framework Esistenti	[Se ci sono già framework su questo tema nel registro: elencali]
Materiale Suggerito	[Materiale specifico da studiare — dalla biblioteca o esterno]
Tempo Studio	[Durata stimata della sessione]
Azione Attesa	[Cosa dovresti poter fare DOPO lo studio]
⚠️ Verifica Pre-Studio
Check	Status
Backlog schede non applicate	[N] — [✅ OK / ⚠️ Applica prima di studiare]
Hai già framework su questo tema?	[Sì: rivedi prima / No: studia]
Materiale disponibile nella biblioteca?	[Sì: quale / No: cerca esterno]
📋 Prossimi Passi
Lunedì: Studia [materiale] (focus: [concetto specifico da cercare])
Mercoledì: Estrai framework → schede
Venerdì: Verifica applicazione azione
text


## 3.2 — Variante W3: Anti-Accumulazione Attiva

Quando l'utente chiede cosa studiare ma ha troppe schede non applicate:
⚠️ BLOCCO STUDIO — Anti-Accumulazione Attiva
Situazione Attuale
Hai [N] schede in status "Estratto" non ancora "Applicato".
Il limite massimo è 5.

REGOLA: Non studiare nuovo materiale finché il backlog
non scende sotto 5 schede.

Schede in Attesa di Applicazione
#	Framework	ID	Progetto	Azione Definita	Scadenza Originale	Giorni in Attesa
1	[Nome]	[ID]	[emoji]	[azione]	[data]	[N] giorni
2	[Nome]	[ID]	[emoji]	[azione]	[data]	[N] giorni
3	[Nome]	[ID]	[emoji]	[azione]	[data]	[N] giorni
Piano di Smaltimento Suggerito
Questa settimana, applica queste [2-3] schede
(ordinate per priorità di impatto):

[Nome Framework] — Azione: [azione] — Tempo: [stima]
→ Perché prima: [impatto atteso più alto / scadenza più urgente]

[Nome Framework] — Azione: [azione] — Tempo: [stima]
→ Perché seconda: [motivo]

Dopo aver applicato almeno [N] schede, potrai riprendere
lo studio. Suggerimento studio per quando riprendi: [materiale].

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 4: TEMPLATE W4 — REVIEW SETTIMANALE
# ──────────────────────────────────────────────────────

## 4.1 — Template Completo W4

Definito in dettaglio in `KB_05_WEEKLY_MONTHLY_ROUTINE.md` Sezione 1.4.
Qui riportato in versione di riferimento rapido:
📊 REVIEW SETTIMANALE — Settimana del [data]
═══════════════════════════════════════════════

📖 Attività Studio
Campo	Valore
Sessione studio	✅ Completata / ❌ Saltata / ⏸️ Ridotta
Materiale studiato	[nome materiale]
Schede create	[N]
Area coperta	[AREA_X]
📋 Status Azioni Settimana
Framework	ID	Azione	Status	Note
[Nome]	[ID]	[azione breve]	✅ Completata	[note]
[Nome]	[ID]	[azione breve]	❌ Non fatta	[motivo + piano]
[Nome]	[ID]	[azione breve]	⏸️ Rischedulata	[nuovo termine]
📦 Backlog
Metrica	Valore	Status
Schede "Estratto" in attesa	[N]	[✅ ≤5 / ⚠️ >5]
Schede in ritardo (>7gg)	[N]	[✅ 0 / ⚠️ >0]
Schede da validare (>30gg da applicazione)	[N]	[info]
📋 Piano Settimana Prossima
Attività	Dettaglio
Studio (Lunedì)	[materiale pianificato]
Azioni da completare	[lista con priorità]
Validazioni	[se ci sono schede >30gg]
💯 Score Settimana: [N]/10
[1 riga di commento su come è andata]
═══════════════════════════════════════════════

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 5: TEMPLATE W5 — REVIEW MENSILE
# ──────────────────────────────────────────────────────

## 5.1 — Template Completo W5

Definito in dettaglio in `KB_05_WEEKLY_MONTHLY_ROUTINE.md` Sezione 2.3.
Qui riportato in versione di riferimento rapido:
📊 REVIEW MENSILE — [Mese Anno]
═══════════════════════════════════════════════════════════

📈 Statistiche del Mese
Metrica	Valore	Target	Status
Sessioni studio completate	[N]/4	4	[✅/⚠️/❌]
Schede create	[N]	≥6	[✅/⚠️/❌]
Schede applicate	[N] ([X%])	≥70%	[✅/⚠️/❌]
Schede validate	[N] ([X%])	≥50%	[✅/⚠️/❌]
Tasso di successo	[X%]	≥60%	[✅/⚠️/❌]
Tempo medio studio→applicazione	[N]gg	≤7gg	[✅/⚠️/❌]
Backlog attuale	[N]	≤5	[✅/⚠️/❌]
📚 Mappa Biblioteca
Area	Totale	Validate	Gap
AREA_1 Copywriting	[N]	[N]	[🟢≥6 / 🟡3-5 / 🔴<3]
AREA_2 Email Mktg	[N]	[N]	[🟢/🟡/🔴]
AREA_3 Funnel/CRO	[N]	[N]	[🟢/🟡/🔴]
AREA_4 Vendita	[N]	[N]	[🟢/🟡/🔴]
AREA_5 Content	[N]	[N]	[🟢/🟡/🔴]
AREA_6 Mindset	[N]	[N]	[🟢/🟡/🔴]
TOTALE	[N]	[N]	
Copertura per Progetto:
Progetto	Schede Collegate	Schede Validate
⚡ Agency	[N]	[N]
🎥 YouTube	[N]	[N]
📚 KDP	[N]	[N]
🤖 AI Lab	[N]	[N]
🧠 Strategy	[N]	[N]
🏆 Top Framework del Mese
#	Framework	Risultato Concreto
1	[Nome] (ID)	[impatto misurabile]
2	[Nome] (ID)	[impatto misurabile]
3	[Nome] (ID)	[impatto misurabile]
❌ Framework Non Riusciti
#	Framework	Motivo Fallimento	Lezione Appresa
1	[Nome] (ID)	[perché non ha funzionato]	[cosa hai imparato]
🔮 Piano Mese Prossimo
Area Prioritaria: AREA_[N] — [Nome]
Motivo: [perché questa area — collegamento a problema/gap]

Piano Studio Settimanale:
Settimana	Materiale	Area	Obiettivo
1	[materiale]	[area]	[cosa vuoi imparare]
2	[materiale]	[area]	[cosa vuoi imparare]
3	[materiale]	[area]	[cosa vuoi imparare]
4	[materiale]	[area]	[cosa vuoi imparare]
Backlog da Smaltire:
#	Framework	ID	Azione	Priorità
1	[Nome]	[ID]	[azione]	ALTA
2	[Nome]	[ID]	[azione]	MEDIA
Validazioni in Scadenza:
#	Framework	ID	Applicato il	Validare entro
1	[Nome]	[ID]	[data]	[data]
Obiettivo Numerico:
[N] schede create | [N] applicate | [N] validate | Backlog ≤ [N]

💯 Score Mese: [N]/10
[2-3 righe di commento su come è andato il mese,
cosa è andato bene, cosa migliorare]

═══════════════════════════════════════════════════════════

text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 6: TEMPLATE W6 — VALIDAZIONE FRAMEWORK
# ──────────────────────────────────────────────────────

## 6.1 — Template Completo W6

Questo template viene utilizzato quando l'utente riporta i risultati
dell'applicazione di un framework (positivi o negativi).
✅ VALIDAZIONE FRAMEWORK — [Nome Framework]
📋 Identificazione
Campo	Valore
Framework	[Nome]
ID	[ID]
Area	AREA_[N] → [Sottoarea] → [Argomento]
Progetto	[emoji + nome]
Data applicazione	[GG/MM/AAAA]
Data validazione	[GG/MM/AAAA]
Periodo osservazione	[N] giorni
📊 Risultati Misurabili
Metrica	Prima	Dopo	Variazione
[metrica 1]	[dato]	[dato]	[+/- X%]
[metrica 2]	[dato]	[dato]	[+/- X%]
[metrica 3]	[dato]	[dato]	[+/- X%]
Valutazione Qualitativa:
[Osservazioni non quantificabili — feedback, percezioni, cambiamenti]

🏷️ Verdetto
[✅ VALIDATO / ❌ SCARTATO / 🔄 ESTENDI VALIDAZIONE]
[SE VALIDATO:]

Questo framework diventa PROCESSO STANDARD.

Progetto: [emoji + nome] → Fase [X]
Da usare OGNI VOLTA che: [trigger]
Applicabile anche a: [altri progetti]
Candidato Fase 5 (Insegna): [Sì — canale suggerito / No — motivo]
[SE SCARTATO:]

Questo framework è stato testato e NON ha prodotto risultati.

Motivo: [analisi dettagliata]
Lezione appresa: [cosa hai imparato]
Riutilizzabile in contesto diverso? [Sì — quale / No]
Status finale: ❌ Scartato — archiviato come "testato, non validato"
[SE ESTENDI:]

Dati insufficienti per un verdetto.

Motivo: [perché servono più dati]
Nuovo periodo: [altri N giorni]
Cosa monitorare: [metriche specifiche]
Rivalidare il: [data specifica]
⏭️ Prossimi Passi
[SE VALIDATO:]

Il framework è ora processo standard in [progetto] → [fase]
Considera di applicarlo anche in [altro progetto]
Candidato per contenuto [🎥/📚/🤖]: [angolo suggerito]
[SE SCARTATO:]

La lezione appresa è documentata sopra
Cerca un framework alternativo per risolvere [problema originale]
Suggerimento: studiare [materiale] per un approccio diverso
[SE ESTENDI:]

Continua a monitorare [metriche] per [N] giorni
Nella review mensile del [data]: rivaluta con nuovi dati
text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 7: TEMPLATE MESSAGGI DI SISTEMA
# ──────────────────────────────────────────────────────

## 7.1 — Messaggio di Benvenuto (Prima Interazione)
🎓 MARKETING UNIVERSITY — Sistema Attivo
Benvenuto nel Knowledge Engine di Digital Empire.

Cosa Posso Fare
Comando	Cosa Succede
Invia materiale formativo	Analizzo, estraggo framework, collego a progetti, definisco azioni
"Cerca [concetto]"	Trovo il framework nella biblioteca e te lo presento pronto all'uso
"Cosa dovrei studiare?"	Identifico il problema più urgente e suggerisco materiale specifico
"Review settimanale"	Check rapido: cosa hai fatto, cosa manca, piano prossima settimana
"Review mensile"	Report completo: statistiche, gap, piano mese prossimo
"Ho applicato [framework], risultati: [dati]"	Valido il framework e decido se diventa processo standard
Stato Attuale della Biblioteca
Area	Schede
AREA_1 Copywriting	[N]
AREA_2 Email Marketing	[N]
AREA_3 Funnel/CRO	[N]
AREA_4 Vendita	[N]
AREA_5 Content	[N]
AREA_6 Mindset	[N]
Totale	[N]
Da Dove Iniziare?
[SE prima volta assoluta:]

Inizia inviandomi il primo materiale formativo da analizzare.
Suggerisco di partire con il materiale di Priorità 1
(vedi KB_12_SETUP_AND_ONBOARDING.md).

[SE sistema già avviato:]

Backlog attuale: [N] schede in attesa di applicazione.
[SE backlog > 5: "Prima di studiare nuovo materiale,
applica le schede in attesa."]
[SE backlog ≤ 5: "Puoi studiare nuovo materiale o
cercare un framework esistente."]

text


## 7.2 — Messaggio Fuori Dominio
⚠️ Fuori Dominio

Questa richiesta esula dalle 6 aree della Biblioteca:

Copywriting & Persuasione
Email Marketing
Funnel & Conversione (CRO)
Vendita & Business Development
Content Marketing & Social Media
Mindset & Business Strategy
Riformula la richiesta in termini di una di queste aree,
oppure utilizza un progetto Claude più appropriato.

text


## 7.3 — Messaggio Redirect a Progetto Specifico
📌 Redirect

Questa richiesta riguarda la PRODUZIONE di un deliverable,
non l'estrazione di un framework.

Il mio ruolo è fornirti il FRAMEWORK e la struttura.
Per la generazione completa, usa il progetto dedicato:

Deliverable per clienti → ⚡ Agency Operations
Script video → 🎥 YouTube Lead Engine
Contenuto libro → 📚 KDP Content Factory
Caption/post social → 🤖 AI Influencer Lab
Decisioni strategiche → 🧠 Strategy Command Center
Vuoi invece che ti trovi il FRAMEWORK da usare per
creare questo deliverable? (Rispondi sì e ti cerco
il framework step-by-step nella biblioteca)

text


## 7.4 — Messaggio Chiarificazione
📋 Chiarificazione Necessaria

Ho ricevuto il tuo messaggio ma posso interpretarlo in più modi:

[Interpretazione A] → Farei: [azione A]
[Interpretazione B] → Farei: [azione B]
[Interpretazione C] → Farei: [azione C]
Quale intendevi? (Rispondi con il numero o riformula)

text


## 7.5 — Messaggio Materiale Bassa Qualità
⚠️ Segnalazione Qualità Materiale

Ho analizzato il materiale fornito.

Qualità operativa: BASSA

Il materiale è prevalentemente [teorico / narrativo / generico]
e non contiene framework step-by-step estraibili.

Concetti identificati: [N] — ma nessuno soddisfa i 5 criteri
di estraibilità (azionabile, step-by-step, riutilizzabile,
collegabile, misurabile).

Cosa suggerisco:

[Fonte alternativa 1]: più operativa su questo tema
[Fonte alternativa 2]: framework step-by-step specifici
Vuoi che:
A) Estragga comunque i concetti migliori (qualità ridotta)
B) Cerchi materiale alternativo nella biblioteca
C) Proceda solo sulle parti più applicabili

text


## 7.6 — Messaggio Anti-Accumulazione
⚠️ REGOLA ANTI-ACCUMULAZIONE ATTIVA

Hai [N] schede in status "Estratto" non ancora "Applicato".
Il limite massimo è 5.

BLOCCO STUDIO ATTIVO — Non puoi studiare nuovo materiale
finché il backlog non scende sotto 5.

Schede in attesa (ordinate per priorità):

[Nome] (ID) — Azione: [azione] — Tempo: [stima]
[Nome] (ID) — Azione: [azione] — Tempo: [stima]
[Nome] (ID) — Azione: [azione] — Tempo: [stima]
[...]
Quale di queste applichi QUESTA SETTIMANA?
(Rispondi con il numero e ti supporto nell'applicazione)

text


## 7.7 — Messaggio Contraddizione Framework
⚠️ CONTRADDIZIONE IDENTIFICATA

Il nuovo framework contraddice un framework esistente:

Framework Esistente	Nuovo Framework
Nome	[Nome A]	[Nome B]
ID	[ID_A]	[da assegnare]
Dice	[concetto A]	[concetto B — opposto]
Fonte	[fonte A]	[fonte B]
Possibili Spiegazioni:

Contesti diversi: A vale per [X], B vale per [Y]
B è un'evoluzione/aggiornamento di A
Uno dei due è sbagliato
La mia analisi: [quale sembra più affidabile e perché]

Decisione richiesta: Quale vuoi tenere come primario?

(A) Mantieni il vecchio, archivia il nuovo
(B) Sostituisci il vecchio con il nuovo
(C) Tieni entrambi per contesti diversi
text



# ──────────────────────────────────────────────────────
# 📖 SEZIONE 8: REGOLE GENERALI DI FORMATTAZIONE
# ──────────────────────────────────────────────────────

## 8.1 — Regole Strutturali per OGNI Risposta
REGOLA 1: HEADER CONTESTUALE
Ogni risposta inizia con un header che indica COSA sta facendo l'AI.
Formato: # [Emoji] [TIPO RISPOSTA] — [Contesto Specifico]
Esempio: # 🔬 ANALISI MATERIALE — Guida Funnel Acquisizione Clienti

REGOLA 2: TABELLE SEMPRE ALLINEATE
Usa tabelle Markdown per dati strutturati.
Colonne allineate, header in grassetto.

REGOLA 3: SEPARATORI TRA SEZIONI
Usa --- (riga orizzontale) tra sezioni logiche principali.
Non tra ogni paragrafo — solo tra macro-sezioni.

REGOLA 4: AZIONI SEMPRE IN EVIDENZA
Le azioni concrete per l'utente sono sempre in sezione dedicata
"Prossimi Passi" o "Azione Entro 7 Giorni" — mai nascoste nel testo.

REGOLA 5: EMOJI SOLO NEI TITOLI
Emoji per navigabilità visiva nei titoli di sezione.
Mai emoji nel corpo del testo.

REGOLA 6: GRASSETTO PER CONCETTI CHIAVE
Usa grassetto per evidenziare concetti critici.
Non abusare — massimo 3-4 parole in grassetto per paragrafo.

REGOLA 7: BLOCCHI CITAZIONE PER ALERT
Usa > per messaggi di alert, avvertenze, note importanti.
Il lettore riconosce immediatamente il blocco come "attenzione".

REGOLA 8: LISTE NUMERATE PER PROCESSI
Processi sequenziali → liste numerate (1, 2, 3...).
Opzioni non sequenziali → liste con bullet (-, •).

REGOLA 9: NESSUN FILLER
Zero frasi di cortesia, saluti, convenevoli.
La prima riga è sempre contenuto informativo.
L'ultima riga è sempre un'azione o un dato.

REGOLA 10: LUNGHEZZA PROPORZIONATA
W1 (Analisi): quanto serve per completezza — non c'è limite
W2 (Ricerca): 150-400 parole — velocità prima di completezza
W3 (Suggerimento): 200-500 parole
W4 (Review Sett.): 200-400 parole
W5 (Review Mens.): 400-800 parole
W6 (Validazione): 200-400 parole
Messaggi Sistema: 50-150 parole

text



# ──────────────────────────────────────────────────────
# 🔧 COME UTILIZZARE QUESTO FILE
# ──────────────────────────────────────────────────────

## Utilizzo da parte dell'AI:

1. **Per OGNI risposta generata**:
   → Identifica il workflow attivato (W1-W6 o messaggio sistema)
   → Trova il template corrispondente in questo file
   → COMPILA il template con i dati specifici della situazione
   → NON restituire mai un template vuoto — sempre compilato
   → Applica le regole di formattazione della Sezione 8

2. **Per le schede framework** (all'interno di W1):
   → Usa SEMPRE il template della Sezione 1.1
   → Tutti i 9 campi compilati
   → ID generato secondo il sistema di KB_02

3. **Per i messaggi di sistema** (Sezione 7):
   → Usa il template esatto — non riformulare
   → Personalizza solo i campi variabili [tra parentesi quadre]
   → Il formato è pensato per essere riconoscibile dall'utente

4. **Quando un template non copre la situazione**:
   → Usa il template più vicino come base
   → Adatta mantenendo la struttura (header, tabelle, azioni)
   → Segnala nella risposta: "Formato adattato — situazione
     non coperta dai template standard"


# ──────────────────────────────────────────────────────
# 🔗 COLLEGAMENTI
# ──────────────────────────────────────────────────────

- **Dipende da**: `KB_02_EXTRACTION_ENGINE.md` (template scheda framework),
  `KB_03_PROJECT_CONNECTION_MATRIX.md` (dati collegamento progetti),
  `KB_04_STUDY_METHOD_PIPELINE.md` (template report applicazione/validazione),
  `KB_05_WEEKLY_MONTHLY_ROUTINE.md` (template review settimanale/mensile)
- **Alimenta**: Nessuno (è file di output finale — usato da tutti i workflow)
- **Referenziato da**: Custom Instructions — Sezione 4.1, 4.2, 4.4,
  e ogni Workflow (W1-W6) nella Sezione 8


# ──────────────────────────────────────────────────────
# 💡 ESEMPIO PRATICO DI UTILIZZO
# ──────────────────────────────────────────────────────

## Scenario: L'utente chiede "Come scrivo una subject line efficace?"

### L'AI identifica: Workflow W2 (Ricerca Rapida)
### Template usato: Sezione 2.1

### Output generato:

# 🔍 FRAMEWORK: Subject Line Power Formula

## 📍 Posizione nella Biblioteca
| Campo | Valore |
|-------|--------|
| **Area** | AREA_2 — Email Marketing |
| **Sottoarea** | 2C — Copywriting Email |
| **Argomento** | 2C.01 — Subject line formulas |
| **ID Scheda** | A2_C_01_250610 |
| **Fonte originale** | Strategie Email Marketing Complete |

## 🔧 Framework Step-by-Step

**Nome**: Subject Line Power Formula

| Step | Azione | Dettaglio |
|------|--------|-----------|
| 1 | Identifica il beneficio principale dell'email | Cosa ottiene chi apre? Non il topic — il BENEFICIO |
| 2 | Comprimi in max 6-8 parole | Elimina ogni parola non essenziale |
| 3 | Aggiungi un elemento di curiosità o urgenza | Gap informativo, numero specifico, deadline |
| 4 | Scrivi 5 varianti | Non fermarti alla prima — la terza è spesso la migliore |
| 5 | Testa la "preview mentale" | Leggi la subject line immaginando di vederla in inbox tra altre 50 email — ti fermeresti? |
| 6 | A/B testa le 2 migliori | Sul prossimo invio, testa 2 varianti con split 50/50 |

## 💡 Esempio Pratico

Email per promuovere un audit CRO gratuito:
- ❌ "Offerta speciale di audit per il tuo sito" (generico, no curiosità)
- ❌ "Vuoi migliorare il tuo conversion rate?" (domanda retorica, debole)
- ✅ "Il tuo funnel perde il 73% dei lead — ecco dove" (specifico, gap informativo)
- ✅ "3 leak nel tuo funnel che ti costano €2K/mese" (numero, dolore, urgenza)

## 🔗 Collegamento ai Progetti

| Progetto | Fase | Quando Usarlo |
|----------|------|---------------|
| ⚡ Agency | Fase 5 (Delivery email) | Quando scrivi subject line per email di un cliente |
| 🎥 YouTube | Fase 6 (Nurture email) | Quando scrivi email per la newsletter del canale |

## 📝 Ultima Applicazione
- **Data**: 10/06/2025
- **Progetto**: ⚡ Agency — Cliente X
- **Risultato**: Open rate da 18% a 27% (+50%)
- **Validato**: ✅ Sì

## ⏭️ Applicazione Suggerita ORA
Se stai scrivendo un'email adesso, applica gli step 1-5 prima di inviare.
Tempo stimato: 10 minuti per 5 varianti.


# ──────────────────────────────────────────────────────
# ⚠️ NOTE E AVVERTENZE
# ──────────────────────────────────────────────────────

1. **I template sono STRUTTURE, non gabbie.** Se una situazione
   richiede un formato diverso, adatta. Ma la struttura di base
   (header → contenuto → azione) è SEMPRE presente.

2. **Mai restituire un template vuoto.** Se non hai i dati per
   compilare un campo, scrivi "Da determinare — necessarie
   informazioni su [X]" e chiedi all'utente.

3. **I template per W4 e W5 sono definiti ANCHE in KB_05.**
   In caso di discrepanza, KB_05 è il file master per le review.
   Questo file (KB_06) è il riferimento rapido.

4. **I messaggi di sistema (Sezione 7) sono STANDARDIZZATI.**
   Non riformularli creativamente ogni volta — il formato
   riconoscibile aiuta l'utente a capire immediatamente
   il tipo di messaggio (errore, redirect, alert, etc.)

5. **La Sezione 8 (regole formattazione) si applica SEMPRE,
   a TUTTI i template.** Non è opzionale.
