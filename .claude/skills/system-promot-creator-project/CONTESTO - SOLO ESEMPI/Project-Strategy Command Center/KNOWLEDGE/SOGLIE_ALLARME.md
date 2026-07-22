# ═══════════════════════════════════════════════════════════════
# 📄 SOGLIE_ALLARME.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: SAFETY
# Priorità: P0 — BLOCCANTE
# Dipendenze: GERARCHIA_PILLAR.md (per le regole di riallocazione), DASHBOARD_ENGINE.md (i dati dashboard attivano gli allarmi)
# Referenziato da: Custom Instructions — Sezione 2.1 (Step 5), Sezione 2.3 (Checkpoint 3), Sezione 5.2, Sezione 6.3, Sezione 8.1 (Step 5), Sezione 8.2 (Step 6)
# ═══════════════════════════════════════════════════════════════

## 📋 SCOPO

Questo file definisce le 6 soglie di allarme del Command Center — le condizioni critiche che richiedono azione IMMEDIATA quando vengono superate. Funziona come il sistema di allarme di un aereo: quando scatta, tutto il resto passa in secondo piano.

Principio fondante: "Un allarme ignorato diventa una crisi. Una crisi ignorata diventa un disastro. Il Command Center non permette allarmi ignorati."

Gli allarmi sono divisi in 2 livelli:
- **🔴 CRITICO**: Richiede azione immediata. Può richiedere riallocazione totale delle risorse.
- **🟡 ATTENZIONE**: Richiede monitoraggio e intervento pianificato entro 7 giorni.

---

## 📖 CONTENUTO PRINCIPALE

### 1. PANORAMICA ALLARMI
SISTEMA DI ALLARME — 6 SOGLIE
══════════════════════════════

LIVELLO 🔴 CRITICO (4 allarmi):
──────────────────────────────
ALM-1: Revenue agenzia in calo per 2 mesi consecutivi
ALM-2: Zero vendite info-biz per 30+ giorni
ALM-3: Zero video YouTube per 3+ settimane
ALM-4: Zero azioni cross-pillar per 30+ giorni

LIVELLO 🟡 ATTENZIONE (2 allarmi):
───────────────────────────────────
ALM-5: OKR trimestrale sotto 30% a metà Q
ALM-6: Tempo satellite superiore al 10%

REGOLA DI PRECEDENZA:
├── Gli allarmi 🔴 hanno precedenza ASSOLUTA
│ su qualsiasi altra attività del Command Center
├── Se ci sono più allarmi 🔴 contemporanei →
│ ALM-1 (Agenzia) ha sempre la precedenza
│ (coerente con GERARCHIA_PILLAR.md)
├── Gli allarmi 🟡 devono essere gestiti entro
│ 7 giorni dalla rilevazione
└── Un allarme resta attivo finché la condizione
non rientra nella norma. Non si "chiude" un
allarme perché "ci sto lavorando" — si chiude
quando il dato rientra.

text


---

### 2. ALM-1 🔴 — REVENUE AGENZIA IN CALO PER 2 MESI
═══════════════════════════════════════════════════════════
ALM-1: REVENUE AGENZIA ↓↓ (CRITICO)
═══════════════════════════════════════════════════════════

CONDIZIONE DI ATTIVAZIONE:
Il revenue dell'agenzia CRO è in calo per 2 mesi
consecutivi rispetto al mese precedente.

Esempio:
├── Mese 1: €4.000
├── Mese 2: €3.200 (↓ -20%) → primo calo, monitora
├── Mese 3: €2.800 (↓ -12.5%) → SECONDO calo
└── → ALM-1 ATTIVATO

NOTA: Anche una piccola discesa conta. Non serve
un crollo del 50%. Due cali consecutivi, anche
piccoli, indicano un TREND negativo.

PERCHÉ È L'ALLARME PIÙ GRAVE:
L'agenzia è l'ossigeno (GERARCHIA_PILLAR.md).
Se il revenue dell'agenzia cala per 2 mesi:
├── Il cash flow si deteriora
├── La fiducia nel business si deteriora
├── La capacità di investire negli altri pillar
│ si deteriora
└── Se non intervieni → il calo si accelera
(meno clienti = meno casi studio = meno
credibilità = ancora meno clienti)

─────────────────────────────────────────────────────
PROTOCOLLO DI RISPOSTA IMMEDIATA:
─────────────────────────────────────────────────────

STEP 1: RIALLOCAZIONE (entro 24 ore)
├── Agenzia: 70-80% del tempo
├── Info-Business: 10-15% (solo mantenimento)
│ ├── Nurture email settimanale → continua
│ ├── Rispondi a studenti → continua
│ ├── Nuovi lanci → STOP
│ └── Creazione nuovi prodotti → STOP
├── YouTube: 10-15% (solo video già programmati)
│ ├── Video già registrati → pubblica
│ ├── Nuove registrazioni → STOP (tranne video
│ │ tipo "caso studio" che servono anche
│ │ per l'agenzia)
│ └── Shorts/clip → STOP
├── Satellite: 0% (stop completo)
└── Durata: finché l'agenzia non torna a 🟡 o 🟢

STEP 2: DIAGNOSI (entro 48 ore)
Usa l'albero diagnostico in DASHBOARD_ENGINE.md
sezione 11 per identificare la causa:

├── CAUSA: Meno lead in entrata?
│ └── AZIONE: Outreach intensivo
│ ├── 10+ messaggi personalizzati/giorno
│ ├── Riattiva TUTTI i canali di acquisizione
│ ├── Chiedi referral a tutti i clienti
│ │ passati e attuali
│ └── Invia email alla lista info-biz con
│ offerta audit CRO gratuito
│ (CROSS_POLLINATION_ENGINE.md Flusso 7)
│
├── CAUSA: Lead OK ma close rate calato?
│ └── AZIONE: Rivedi il processo di vendita
│ ├── Riascolta le ultime 3 call registrate
│ ├── Identifica dove perdi il prospect
│ ├── Rivedi la proposta: pricing, positioning,
│ │ struttura
│ └── Usa Sales Call Closer (skill) per
│ ottimizzare lo script
│
├── CAUSA: Clienti persi / non rinnovano?
│ └── AZIONE: Retention
│ ├── Contatta ogni cliente per feedback
│ ├── Identifica se è un problema di risultati
│ │ o di comunicazione
│ ├── Proponi upsell o estensione a prezzo
│ │ speciale
│ └── Documenta le ragioni di perdita per
│ prevenire in futuro
│
└── CAUSA: Valore medio progetto calato?
└── AZIONE: Repricing
├── Stai attirando clienti troppo piccoli?
├── Il tuo positioning è chiaro?
├── Rivedi il target: aziende con traffico
│ > [N] visitatori/mese
└── Considera success fee per aumentare
il valore medio

STEP 3: PIANO D'AZIONE SETTIMANALE (entro 72 ore)
Definisci 3 azioni concrete per QUESTA settimana:

┌────┬──────────────────────────────┬───────────────┐
│ # │ Azione │ Entro quando │
├────┼──────────────────────────────┼───────────────┤
│ 1 │ [Azione specifica] │ [Giorno] │
│ 2 │ [Azione specifica] │ [Giorno] │
│ 3 │ [Azione specifica] │ [Giorno] │
└────┴──────────────────────────────┴───────────────┘

STEP 4: MONITORAGGIO GIORNALIERO
Per tutta la durata dell'allarme:
├── Quanti outreach inviati oggi? [N]
├── Quante risposte ricevute? [N]
├── Call prenotate questa settimana? [N]
├── Pipeline attuale: [N] lead attivi
└── Revenue previsto prossimo mese: €[N]

CONDIZIONE DI CHIUSURA:
L'allarme si chiude quando:
├── Il revenue del mese corrente è ≥ al mese
│ precedente (il trend si inverte)
├── E la pipeline ha almeno 3 lead attivi
│ per i prossimi 30 giorni
└── Solo allora si torna alla distribuzione
standard delle risorse

text


---

### 3. ALM-2 🔴 — ZERO VENDITE INFO-BIZ PER 30+ GIORNI
═══════════════════════════════════════════════════════════
ALM-2: ZERO VENDITE INFO-BIZ 30+ GG (CRITICO)
═══════════════════════════════════════════════════════════

CONDIZIONE DI ATTIVAZIONE:
Nessun prodotto info-business venduto (€0 revenue
info-biz) per 30 o più giorni consecutivi.

NOTA: Si conta solo se ci sono prodotti ATTIVI nel
catalogo e il funnel è ATTIVO. Se non hai ancora
lanciato nessun prodotto → questo allarme non si
applica (stato ⚪).

PERCHÉ È GRAVE:
├── Il funnel è ROTTO o il traffico è ZERO
├── La lista email non sta convertendo
├── L'investimento in creazione prodotto non sta
│ generando ritorno
└── Se non intervieni → la lista si raffredda,
il funnel si deteriora, il prodotto diventa
obsoleto

─────────────────────────────────────────────────────
PROTOCOLLO DI RISPOSTA:
─────────────────────────────────────────────────────

STEP 1: DIAGNOSI FUNNEL (entro 48 ore)
Percorri il funnel dall'alto al basso e trova
dove si blocca:

TRAFFICO → LANDING → OPT-IN → NURTURE → VENDITA
│ │ │ │ │
▼ ▼ ▼ ▼ ▼
C'è La landing Gli opt-in Le email La sales
traffico converte? ricevono vengono page
al (>30%?) email? aperte? converte?
funnel? (>20%?) (>2%?)
│ │ │ │ │
NO→[A] NO→[B] NO→[C] NO→[D] NO→[E]

[A] PROBLEMA: TRAFFICO
├── Quanti visitatori/mese arrivano alla landing?
├── SE zero → nessuno vede il funnel
├── AZIONI:
│ ├── Aggiungi CTA più chiara nei video YouTube
│ ├── Invia email alla lista (se ne hai una)
│ │ che porta alla landing
│ ├── Verifica che i link in descrizione YT
│ │ funzionino
│ ├── Valuta 1 test ads con budget minimo (€50)
│ │ per validare se il funnel converte con
│ │ traffico
│ └── Attiva cross-pollination: menziona il PDF
│ in ogni touchpoint (email firma, bio social,
│ link nei libri KDP)

[B] PROBLEMA: LANDING PAGE
├── La landing riceve traffico ma nessuno fa opt-in
├── Opt-in rate < 20% → problema SERIO
├── AZIONI:
│ ├── Testa una nuova headline (la più impattante)
│ ├── Verifica che il lead magnet sia DESIDERABILE
│ │ (il titolo promette un beneficio chiaro?)
│ ├── Semplifica il form (solo email, niente nome)
│ ├── Aggiungi social proof (testimonianze, numeri)
│ └── A/B test: prova 2 versioni per 1 settimana

[C] PROBLEMA: DELIVERABILITY EMAIL
├── Gli opt-in non ricevono le email
├── AZIONI:
│ ├── Controlla la cartella spam del tuo provider
│ ├── Verifica che l'automazione email sia attiva
│ ├── Invia una email di test a te stesso
│ ├── Controlla il sender score
│ └── Se usi un nuovo dominio → potrebbe servire
│ un warmup

[D] PROBLEMA: EMAIL SEQUENCE
├── Le email arrivano ma nessuno le apre/clicca
├── Open rate < 20% → problema di subject line
│ o di frequenza (troppo alta → spam/ignore)
├── Click rate < 1% → problema di contenuto email
│ o di CTA
├── AZIONI:
│ ├── Riscrivi le subject line (usa curiosità,
│ │ beneficio specifico, urgenza reale)
│ ├── Verifica la frequenza: stai inviando
│ │ troppo spesso? O troppo raramente?
│ ├── Controlla che il contenuto delle email
│ │ dia VALORE prima di chiedere l'acquisto
│ ├── La CTA è chiara e visibile?
│ └── Stai raccontando storie o solo vendendo?

[E] PROBLEMA: SALES PAGE / OFFERTA
├── Le email vengono aperte e cliccate, ma nessuno
│ compra sulla sales page
├── AZIONI:
│ ├── Il prezzo è giusto per il target?
│ │ (usa Product Pricing Strategist)
│ ├── La sales page comunica chiaramente il
│ │ BENEFICIO, non le feature?
│ ├── C'è social proof sufficiente?
│ ├── La garanzia è presente e visibile?
│ ├── Il prodotto risolve un VERO problema
│ │ che il target HA?
│ └── DOMANDA CHIAVE: "Se fossi il mio target,
│ comprerei questo prodotto a questo prezzo
│ basandomi solo su questa pagina?"

STEP 2: FIX RAPIDO (entro 7 giorni)
Scegli il punto di rottura del funnel (da Step 1)
e implementa il fix con la priorità più alta.

REGOLA: Correggi UN punto alla volta. Non
ristrutturare tutto il funnel — trova il COLLO
DI BOTTIGLIA e sbloccalo.

STEP 3: MONITORAGGIO
├── Controlla le metriche del funnel ogni 2 giorni
│ per 2 settimane dopo il fix
├── Se il fix funziona (vendite riprendono) →
│ allarme chiuso
├── Se il fix NON funziona → passa al punto di
│ rottura successivo e ripeti
└── Se dopo 3 fix il funnel non converte →
RICONSIDERARE il prodotto stesso
(forse non c'è domanda per questo prodotto)

CONDIZIONE DI CHIUSURA:
├── Almeno 1 vendita nei 7 giorni successivi al fix
├── E almeno 3 vendite nei 30 giorni successivi
└── Solo allora l'allarme si chiude

text


---

### 4. ALM-3 🔴 — ZERO VIDEO YOUTUBE PER 3+ SETTIMANE
═══════════════════════════════════════════════════════════
ALM-3: ZERO VIDEO YOUTUBE 3+ SETTIMANE (CRITICO)
═══════════════════════════════════════════════════════════

CONDIZIONE DI ATTIVAZIONE:
Nessun video pubblicato sul canale YouTube per 21+
giorni consecutivi.

PERCHÉ È GRAVE:
├── YouTube premia la COSTANZA. 3 settimane di
│ silenzio = l'algoritmo ti penalizza
├── La lead generation organica si ferma
├── Il pubblico perde abitudine → iscritti
│ smettono di cercarti
├── La pipeline di contenuti si svuota → quando
│ riprendi è più difficile ricominciare
└── Il compound interest della costanza si resetta

─────────────────────────────────────────────────────
PROTOCOLLO DI RISPOSTA:
─────────────────────────────────────────────────────

STEP 1: DIAGNOSI (entro 24 ore)
Perché non stai pubblicando?

├── CAUSA: Non ho tempo
│ └── AZIONE: Verifica allocazione tempo
│ ├── YouTube dovrebbe avere 15-20% del tempo
│ ├── Se l'Agenzia è in crisi (ALM-1 attivo)
│ │ → OK, YouTube può essere in pausa
│ │ temporanea. Ma pubblica almeno 1 video
│ │ semplice ogni 2 settimane per non
│ │ perdere momentum
│ └── Se l'Agenzia NON è in crisi → stai
│ dando troppo tempo a qualcos'altro.
│ Ribilancia.
│
├── CAUSA: Non ho idee per i video
│ └── AZIONE: Usa le fonti di idee automatiche
│ ├── Domande clienti agenzia
│ │ (CROSS_POLLINATION_ENGINE.md Flusso 1)
│ ├── Commenti sui video precedenti
│ │ (CROSS_POLLINATION_ENGINE.md Flusso 9)
│ ├── Errori comuni visti negli audit
│ │ (CROSS_POLLINATION_ENGINE.md Flusso 11A)
│ ├── Casi studio completati
│ │ (CROSS_POLLINATION_ENGINE.md Flusso 11A)
│ └── Clip da webinar registrati
│ (CROSS_POLLINATION_ENGINE.md Flusso 11B)
│
├── CAUSA: Non ho motivazione / è noioso
│ └── AZIONE: Semplifica il formato
│ ├── Non serve un video perfetto da 15 minuti
│ ├── Un video semplice da 5-7 minuti
│ │ registrato con il telefono → BASTA
│ ├── "Done is better than perfect"
│ ├── Oppure: registra 3-4 video in 1 sessione
│ │ (batch recording) → pubblicali nelle
│ │ settimane successive
│ └── Oppure: estrai clip da webinar/corsi
│ esistenti → zero registrazione nuova
│
└── CAUSA: Problema tecnico / editing
└── AZIONE: Elimina il collo di bottiglia
├── Se il problema è l'editing → pubblica
│ senza editing elaborato (taglio base)
├── Se il problema è l'attrezzatura → registra
│ con il telefono
└── Se il problema è l'upload → programma
l'upload in anticipo

STEP 2: VIDEO DI EMERGENZA (entro 72 ore)
Pubblica 1 video QUESTA settimana. Non deve essere
perfetto. Deve esistere.

Formati di emergenza (rapidi da produrre):
├── "3 errori che vedo sempre nei funnel"
│ (5 minuti, parlato a camera, zero editing)
├── "Rispondo a una domanda di un cliente"
│ (5 minuti, screen recording + voce)
├── Clip da un webinar registrato
│ (0 minuti di registrazione, solo editing)
└── YouTube Short da 60 secondi
(1 minuto di registrazione, 5 di editing)

STEP 3: RIPRISTINO CADENZA
├── Settimana 1: 1 video (emergenza)
├── Settimana 2: 1 video
├── Settimana 3: 1 video
├── Settimana 4+: cadenza normale (1+/settimana)
└── Se non riesci a mantenere 1/settimana →
abbassa a 2/mese ma MANTIENILI costanti.
Meglio 2/mese costanti che 4 in una settimana
poi 0 per un mese.

CONDIZIONE DI CHIUSURA:
├── 2 video pubblicati in 14 giorni consecutivi
└── Piano di produzione per le prossime 4 settimane

text


---

### 5. ALM-4 🔴 — ZERO AZIONI CROSS-PILLAR PER 30+ GIORNI
═══════════════════════════════════════════════════════════
ALM-4: ZERO CROSS-POLLINATION 30+ GG (CRITICO)
═══════════════════════════════════════════════════════════

CONDIZIONE DI ATTIVAZIONE:
Nessuna azione cross-pillar eseguita per 30+ giorni.
(Riferimento: registro azioni in
CROSS_POLLINATION_ENGINE.md Sezione 14)

PERCHÉ È GRAVE:
├── I 3 pillar stanno operando in ISOLAMENTO
├── Le sinergie si stanno perdendo
├── Il compound interest delle connessioni si resetta
├── L'ecosistema sta diventando 3 business separati
└── Ogni settimana senza cross-pollination = 1
settimana di sinergia persa che non recuperi

─────────────────────────────────────────────────────
PROTOCOLLO DI RISPOSTA:
─────────────────────────────────────────────────────

STEP 1: AZIONE IMMEDIATA (QUESTO LUNEDÌ)
Apri CROSS_POLLINATION_ENGINE.md Sezione 14
(Checklist Settimanale) e scegli 1 azione dalla
lista "AZIONI RAPIDE (< 30 minuti)".

Non pensarci troppo. Scegli la prima che puoi fare.
Falla OGGI.

STEP 2: SISTEMATIZZA
Il problema non è che non hai fatto 1 azione.
Il problema è che non hai un SISTEMA per farla.

Fix del sistema:
├── Metti un reminder nel calendario: "LUNEDÌ 9:00
│ — Cross-pollination settimanale (15 min)"
├── Prepara una lista di 4 azioni (1 per settimana
│ del mese) all'inizio di ogni mese
├── Nella review settimanale del Command Center,
│ lo step "Cross-pollination action" è
│ OBBLIGATORIO — non opzionale
└── Se il lunedì è troppo pieno → sposta al
martedì, ma NON saltare

STEP 3: RECUPERO
├── Settimana 1: 1 azione (rapida, < 30 minuti)
├── Settimana 2: 1 azione (rapida)
├── Settimana 3: 1 azione (media, 30-60 minuti)
├── Settimana 4: 1 azione (a scelta)
└── Fine mese: 4 azioni completate → allarme chiuso

CONDIZIONE DI CHIUSURA:
├── 4 azioni cross-pillar in 30 giorni (1/settimana)
└── Sistema di reminder attivo per le settimane
successive

text


---

### 6. ALM-5 🟡 — OKR TRIMESTRALE SOTTO 30% A METÀ Q
═══════════════════════════════════════════════════════════
ALM-5: OKR < 30% A METÀ Q (ATTENZIONE)
═══════════════════════════════════════════════════════════

CONDIZIONE DI ATTIVAZIONE:
A metà del trimestre (fine mese 2 di 3), il
progresso complessivo dei KR è sotto il 30%.

Come calcolare:
Media dei progressi % di tutti i KR attivi.
Esempio:
├── Agenzia KR1: 20%, KR2: 35%, KR3: 10%
├── Info-Biz KR1: 40%, KR2: 15%
├── YouTube KR1: 25%, KR2: 30%
├── Media: (20+35+10+40+15+25+30) / 7 = 25%
└── 25% < 30% → ALM-5 ATTIVATO

PERCHÉ È IMPORTANTE:
├── A metà Q dovresti essere almeno al 40-50%
├── Se sei al 30% → la probabilità di raggiungere
│ il 70% (target) a fine Q è bassa
├── Serve capire se il problema è di AMBIZIONE
│ (OKR troppo ambiziosi) o di ESECUZIONE
│ (non stai eseguendo abbastanza)
└── Ignorare questo segnale → fine Q con completion
rate sotto il 50% → frustrazione e perdita
di fiducia nel sistema OKR

─────────────────────────────────────────────────────
PROTOCOLLO DI RISPOSTA (entro 7 giorni):
─────────────────────────────────────────────────────

STEP 1: DIAGNOSI
Per ogni KR sotto il 30%, chiediti:

"Il target era REALISTICO quando l'ho definito?"
├── SÌ, era realistico → Il problema è l'ESECUZIONE
│ ├── Non ho dedicato abbastanza tempo?
│ ├── I task dello sprint non muovevano i KR?
│ ├── Ci sono stati imprevisti (emergenze, salute)?
│ └── La distribuzione tempo tra pillar era
│ sbilanciata?
│
└── NO, era troppo ambizioso → Il problema è il TARGET
├── Avevo le risorse necessarie?
├── Il timeframe era realistico?
├── C'erano dipendenze esterne fuori controllo?
└── L'ambiente di mercato è cambiato?

STEP 2: DECISIONE

OPZIONE A: RICALIBRA I TARGET
Se il problema è l'ambizione:
├── Riduci il target dei KR critici al livello
│ raggiungibile nel tempo rimanente
├── Mantieni l'Objective invariato (la direzione
│ resta la stessa)
├── Documenta il motivo della ricalibrazione
└── ATTENZIONE: Non ricalibra per pigrizia.
Ricalibra solo se ci sono dati oggettivi
che mostrano che il target era irrealistico.

OPZIONE B: INTENSIFICA L'ESECUZIONE
Se il problema è l'esecuzione:
├── Identifica i 1-2 KR con più impatto
├── Concentra il mese rimanente SOLO su quelli
├── Sacrifica i KR a bassa priorità
│ (meglio 2 KR al 70% che 5 KR al 30%)
├── Ribilancia lo sprint mensile del mese 3
│ → tutti i 7 task puntano ai 2 KR prioritari
└── Aumenta il tempo dedicato se possibile

OPZIONE C: ACCETTA E IMPARA
Se ci sono stati imprevisti legittimi:
├── Documenta cosa è successo
├── Accetta che questo Q sarà sotto-performante
├── Usa le lezioni per definire OKR più realistici
│ nel Q successivo
└── NON abbatterti. Un Q debole non definisce
l'intero anno.

CONDIZIONE DI CHIUSURA:
├── Decisione presa (A, B, o C) e documentata
├── Sprint del mese 3 ricalibrato
└── Review di fine Q per verificare il risultato

text


---

### 7. ALM-6 🟡 — TEMPO SATELLITE SUPERIORE AL 10%
═══════════════════════════════════════════════════════════
ALM-6: SATELLITE > 10% (ATTENZIONE)
═══════════════════════════════════════════════════════════

CONDIZIONE DI ATTIVAZIONE:
Il tempo dedicato ai progetti satellite (KDP +
AI Influencer) supera il 10% del tempo totale
per 2+ settimane consecutive.

Come misurare:
├── Stima le ore dedicate a KDP + AI Influencer
│ nella settimana
├── Dividi per le ore totali lavorate
├── Se > 10% per 2+ settimane → ALM-6 ATTIVATO
└── Esempio: 6 ore su KDP in una settimana di 45
ore totali = 13.3% → ⚠️

PERCHÉ È IMPORTANTE:
├── I satellite sono INTEGRATORI, non CORE
│ (GERARCHIA_PILLAR.md: "vitamine, non ossigeno")
├── Se superano il 10%, stanno rubando tempo
│ a un pillar principale
├── Il tempo rubato viene quasi sempre dal pillar
│ che "sembra noioso" → spesso l'Agenzia
│ (outreach, follow-up = ripetitivo)
├── Il satellite genera meno revenue per ora
│ investita rispetto ai pillar principali
└── È un SINTOMO di ADD imprenditoriale:
i satellite sono "nuovi e eccitanti" rispetto
ai pillar consolidati

─────────────────────────────────────────────────────
PROTOCOLLO DI RISPOSTA (entro 7 giorni):
─────────────────────────────────────────────────────

STEP 1: IDENTIFICA DA DOVE ARRIVA IL TEMPO
"Quale pillar principale ha PERSO tempo a favore
del satellite?"

┌─────────────────┬──────────┬──────────┬─────────────┐
│ Pillar │ % Target │ % Attuale│ Differenza │
├─────────────────┼──────────┼──────────┼─────────────┤
│ Agenzia CRO │ 50-60% │ [N]% │ [+/-] │
│ Info-Business │ 20-30% │ [N]% │ [+/-] │
│ YouTube │ 15-20% │ [N]% │ [+/-] │
│ Satellite │ 5-10% │ [N]% │ [+N]% ⚠️ │
└─────────────────┴──────────┴──────────┴─────────────┘

STEP 2: RIBILANCIA
├── SE il tempo è stato rubato all'Agenzia:
│ → PRIORITÀ MASSIMA. Ripristina l'allocazione
│ agenzia IMMEDIATAMENTE. L'ossigeno non si
│ negozia.
│
├── SE il tempo è stato rubato all'Info-Biz:
│ → Importante ma non critico. Ribilancia entro
│ la prossima settimana.
│
└── SE il tempo è stato rubato a YouTube:
→ Accettabile a breve termine, ma se YouTube
non pubblica video (→ ALM-3) diventa critico.

STEP 3: DEFINISCI LIMITI CONCRETI
├── "Questa settimana, dedico MAX [N] ore ai
│ satellite. Non un'ora di più."
├── Blocca il tempo nel calendario: slot dedicato
│ ai satellite (es: venerdì pomeriggio 2 ore)
├── Fuori da quello slot → satellite non esiste
└── Se il satellite richiede più di 5 ore/settimana
→ valuta se DELEGARE parte del lavoro

STEP 4: VERIFICA MOTIVAZIONE
"Perché sto dedicando così tanto tempo al satellite?"
├── "Perché sta generando risultati" → OK ma non
│ a scapito del core. Mantieni il limite del 10%
├── "Perché è più divertente" → ADD ALERT.
│ Attiva FILTRO_ANTI_ADD.md Sezione 4 (Pratiche
│ preventive). Il divertimento non paga le bollette,
│ l'Agenzia sì.
└── "Perché ci sono scadenze" → Le scadenze del
satellite non possono mai superare le priorità
dei pillar. Posponi la scadenza del satellite
se necessario.

CONDIZIONE DI CHIUSURA:
├── Tempo satellite ≤ 10% per 2 settimane consecutive
└── Allocazione pillar principali rientrata nei range
target

text


---

### 8. PANNELLO ALLARMI — TEMPLATE DI MONITORAGGIO
═══════════════════════════════════════════════════════════
PANNELLO ALLARMI — [MESE] [ANNO]
═══════════════════════════════════════════════════════════

Questo pannello si compila OGNI settimana nella
review settimanale (Step 6: Health check rapido)
e OGNI mese nella review mensile (Dashboard
Sezione 7).

┌─────┬──────────────────────────┬────────┬────────────┐
│ ALM │ Descrizione │ Stato │ Azione │
├─────┼──────────────────────────┼────────┼────────────┤
│ 1 │ Revenue agenzia ↓ per │ [OK / │ [Se ⚠️: │
│ 🔴 │ 2 mesi consecutivi │ ⚠️] │ protocollo │
│ │ │ │ ALM-1] │
├─────┼──────────────────────────┼────────┼────────────┤
│ 2 │ Zero vendite info-biz │ [OK / │ [Se ⚠️: │
│ 🔴 │ per 30+ giorni │ ⚠️ / │ protocollo │
│ │ │ ⚪] │ ALM-2] │
├─────┼──────────────────────────┼────────┼────────────┤
│ 3 │ Zero video YouTube │ [OK / │ [Se ⚠️: │
│ 🔴 │ per 3+ settimane │ ⚠️] │ protocollo │
│ │ │ │ ALM-3] │
├─────┼──────────────────────────┼────────┼────────────┤
│ 4 │ Zero azioni cross-pillar │ [OK / │ [Se ⚠️: │
│ 🔴 │ per 30+ giorni │ ⚠️] │ protocollo │
│ │ │ │ ALM-4] │
├─────┼──────────────────────────┼────────┼────────────┤
│ 5 │ OKR trimestrale < 30% │ [OK / │ [Se ⚠️: │
│ 🟡 │ a metà Q │ ⚠️ / │ protocollo │
│ │ │ N/A] │ ALM-5] │
├─────┼──────────────────────────┼────────┼────────────┤
│ 6 │ Tempo satellite > 10% │ [OK / │ [Se ⚠️: │
│ 🟡 │ │ ⚠️] │ protocollo │
│ │ │ │ ALM-6] │
└─────┴──────────────────────────┴────────┴────────────┘

ALLARMI ATTIVI: [N]
├── Se 0 → ✅ Tutto nella norma
├── Se 1-2 🟡 → Gestire entro 7 giorni
├── Se 1+ 🔴 → Azione IMMEDIATA (oggi)
└── Se 2+ 🔴 → EMERGENZA. Agenzia (ALM-1) ha
sempre la precedenza. Poi gli altri 🔴.

STORICO ALLARMI:
┌────────┬─────┬──────────────┬───────────────┬────────┐
│ Data │ ALM │ Attivato / │ Azione presa │ Durata │
│ │ │ Chiuso │ │ │
├────────┼─────┼──────────────┼───────────────┼────────┤
│ [DATA] │ [N] │ [ATT / CHI] │ [Descrizione] │ [N gg] │
│ [DATA] │ [N] │ [ATT / CHI] │ [Descrizione] │ [N gg] │
│ [DATA] │ [N] │ [ATT / CHI] │ [Descrizione] │ [N gg] │
└────────┴─────┴──────────────┴───────────────┴────────┘

PATTERN ANALYSIS (trimestrale):
├── Allarme più frequente: ALM-[N]
│ → Indica un problema SISTEMICO in [area]
│ → Azione: [risolvere la causa alla radice]
├── Allarme mai attivato: ALM-[N]
│ → Ottimo. Oppure: la soglia è troppo bassa?
└── Tempo medio di risoluzione allarmi: [N] giorni
→ Target: < 14 giorni per 🔴, < 7 giorni per 🟡

text


---

### 9. COMBINAZIONI DI ALLARMI — SCENARI MULTI-CRISI
═══════════════════════════════════════════════════════════
QUANDO PIÙ ALLARMI SCATTANO CONTEMPORANEAMENTE
═══════════════════════════════════════════════════════════

SCENARIO A: ALM-1 + ALM-3 (Agenzia in calo + Zero video)
─────────────────────────────────────────────────────────
Priorità: ALM-1 (Agenzia) SEMPRE PRIMA.
YouTube può aspettare. L'ossigeno no.
Piano: 80% Agenzia per 2-4 settimane. YouTube pubblica
solo video di emergenza (1 ogni 2 settimane).

SCENARIO B: ALM-2 + ALM-4 (Zero vendite info + Zero cross-poll)
──────────────────────────────────────────────────────────────────
Probabilmente COLLEGATI: zero cross-pollination →
zero traffico al funnel info-biz → zero vendite.
Piano: Risolvi ALM-4 prima (1 azione cross-poll che
porta traffico al funnel info-biz). Poi diagnostica
il funnel (ALM-2).

SCENARIO C: ALM-1 + ALM-2 + ALM-3 (tutto in crisi)
────────────────────────────────────────────────────
Situazione CRITICA ma non irreversibile.
Piano: 100% Agenzia per 2 settimane. Poi gradualmente
ripristina gli altri pillar. Non cercare di risolvere
tutto contemporaneamente — è la ricetta per non
risolvere niente.

SCENARIO D: ALM-5 + ALM-6 (OKR deboli + troppo satellite)
──────────────────────────────────────────────────────────
Probabilmente COLLEGATI: troppo tempo su satellite →
meno tempo sui pillar → OKR non avanzano.
Piano: Risolvi ALM-6 prima (taglia satellite al 5%).
Il tempo recuperato va sui KR più indietro.
ALM-5 si risolverà di conseguenza.

REGOLA GENERALE PER MULTI-ALLARME:

Identifica se gli allarmi sono COLLEGATI
(uno causa l'altro)
SE collegati → risolvi la CAUSA (l'allarme a monte)
SE indipendenti → segui la precedenza:
ALM-1 > ALM-2 > ALM-3 > ALM-4 > ALM-5 > ALM-6
MAI cercare di risolvere più di 2 allarmi
contemporaneamente
text


---

## 🔧 COME UTILIZZARE QUESTO FILE

**Quando consultarlo:**
- In OGNI review settimanale (Step 6: Health check rapido) → compila il pannello allarmi
- In OGNI review mensile (Dashboard Sezione 7) → pannello allarmi completo
- Ogni volta che l'utente riporta un dato che potrebbe attivare un allarme
- Quando un pillar cambia status da 🟢 a 🟡 o 🔴 → verifica se un allarme è attivato
- Quando si pianifica il trimestre successivo → rivedi lo storico allarmi per pattern

**Come integrare nella risposta:**
1. Se un allarme è attivo → segnalalo IN CIMA alla risposta, PRIMA di qualsiasi altro contenuto. Formato: "⚠️ ALLARME ALM-[N] ATTIVO: [descrizione breve]. Protocollo in corso."
2. Non minimizzare MAI un allarme. Se i dati dicono che è attivo → è attivo. Anche se l'utente dice "ma secondo me va bene".
3. Se più allarmi sono attivi → usa la Sezione 9 (combinazioni) per gestire la precedenza
4. Quando un allarme si chiude → segnalalo: "✅ ALLARME ALM-[N] CHIUSO. Condizione rientrata nella norma il [DATA]."
5. Registra SEMPRE nello storico (Sezione 8) apertura e chiusura di ogni allarme

---

## 🔗 COLLEGAMENTI

- **Dipende da**: `KB/GERARCHIA_PILLAR.md` (regole di riallocazione in ALM-1), `KB/DASHBOARD_ENGINE.md` (i dati dashboard attivano gli allarmi), `KB/CROSS_POLLINATION_ENGINE.md` (per ALM-4)
- **Alimenta**: `KB/DECISION_FRAMEWORK.md` (gli allarmi 🔴 sovrascrivono le priorità normali del processo decisionale), `KB/OKR_SYSTEM.md` (ALM-5 può portare a ricalibrazione degli OKR)
- **Collegato a**: `KB/FILTRO_ANTI_ADD.md` (ALM-6 è spesso un sintomo di ADD), `KB/WORKFLOW_CADENZE.md` (gli allarmi si controllano in ogni cadenza di review)
- **Custom Instructions**: Sezione 2.1 Step 5, Sezione 2.3 Checkpoint 3, Sezione 5.2, Sezione 6.3, Sezione 8.1 Step 5, Sezione 8.2 Step 6

---

## 💡 ESEMPI PRATICI

### Esempio: Rilevazione e gestione ALM-1

**Situazione:** L'utente dice "Questo mese l'agenzia ha fatturato €2.800. Il mese scorso €3.200. Due mesi fa €4.000."

**Risposta tipo:**
⚠️ ALLARME ALM-1 ATTIVO — REVENUE AGENZIA ↓↓

Dati:
├── 2 mesi fa: €4.000
├── Mese scorso: €3.200 (↓ -20%)
├── Questo mese: €2.800 (↓ -12.5%)
└── Trend: 2 cali CONSECUTIVI → ALM-1 ATTIVATO

RIALLOCAZIONE IMMEDIATA:
├── Agenzia: 75% del tempo (da domani)
├── Info-Biz: 15% (solo mantenimento)
├── YouTube: 10% (solo video già pronti)
├── Satellite: 0%
└── Durata: finché revenue non risale

DIAGNOSI NECESSARIA:

Quanti lead qualificati hai ricevuto questo mese? [___]
Quante call strategiche hai fatto? [___]
Hai perso clienti o sono terminati i progetti? [___]
Il close rate è cambiato rispetto ai mesi scorsi? [___]
Fornisci questi dati e procedo con il piano d'azione
specifico.

text


---

## ⚠️ NOTE E AVVERTENZE

1. **Un allarme NON si chiude perché "ci stai lavorando".** Si chiude quando il DATO rientra nella norma. "Sto facendo outreach" non chiude ALM-1. "Il revenue è risalito a €3.500" chiude ALM-1.

2. **Non aggiungere nuovi allarmi senza rimuoverne uno.** 6 allarmi sono sufficienti. Se vuoi monitorare qualcosa di nuovo → sostituisci l'allarme meno rilevante nella review trimestrale.

3. **ALM-1 ha SEMPRE la precedenza.** Anche se hai ALM-2, ALM-3 e ALM-4 tutti attivi, se ALM-1 è attivo → si risolve PRIMA. L'agenzia è l'ossigeno.

4. **Le soglie sono calibrate per un business in crescita.** Se sei all'inizio e il revenue dell'agenzia è €0 (non hai ancora clienti), gli allarmi di calo non si applicano — non puoi calare da 0. Si attivano quando hai stabilito un baseline.

5. **Il pannello allarmi deve essere VISIBILE.** Non nascosto in un file. Mettilo in cima alla dashboard mensile e alla review settimanale. Un allarme che non vedi è un allarme che non esiste.

6. **Lo storico allarmi (Sezione 8) è fondamentale per le retrospettive.** Se ALM-3 (zero video) si attiva ogni 2 mesi → c'è un problema SISTEMICO con la produzione video. Non serve un fix temporaneo — serve un cambio strutturale (batch recording, formato più semplice, outsourcing editing).