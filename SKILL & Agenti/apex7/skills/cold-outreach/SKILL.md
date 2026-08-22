---
name: cold-outreach-apsoc-engine
description: Genera sequenze B2B cold outreach ad altissimo ROI con framework APSOC chirurgico (Attention-Problem-Solution-Offer-Close) per target specifici, offrendo meccanismo logico non prodotto e CTA a basso attrito per chiudere clienti estivi per Digital Empire Stream S2.
---

# OBIETTIVO
Creare in <90 secondi una sequenza di 3 email a freddo B2B (Email 1 max 100 parole Giorno 0, Email 2 Follow-up Giorno 3 con leva sociale, Email 3 Rottura Giorno 7 con takeaway) che applicano rigorosamente APSOC, con tasso risposta target ≥12% e zero fuffa aziendale, pronte per invio con spacing mobile-optimized.

# TRIGGER
Questa skill si attiva quando:
- Utente scrive "sequenza di 3 email a freddo destinate a: [TARGET]" + "vendergli: [SERVIZIO]" + "framework APSOC"
- Utente menziona: "cold outreach", "cold email", "APSOC", "Stream S2", "chiudere clienti estivi"
- Input contiene placeholder [INSERISCI TARGET] e [INSERISCI SERVIZIO]
- Planner rileva intent = cold-outreach con confidence >0.8
- È richiesto copy B2B diretto, chirurgico, per conversione lead in appuntamenti

# REGOLE FERREE
1. Framework APSOC OBBLIGATORIO in ogni email: A=oggetti magnetici + prima riga pattern interrupt (MAI "Ciao come stai" o "Spero tu stia bene"), P=dolore acuto attuale target (lead che non rispondono, bruciati 73%), S=meccanismo logico non prodotto (es. Risposta 27sec → Qualifica → Handoff), O=offerta irresistibile basso rischio (14gg pilot, paghi solo se +8 appuntamenti), C=CTA singola senza attrito (Rispondi OK/FLUSSO)
2. Email 1 MASSIMO 100 parole, diretta chirurgica, niente fuffa aziendale - conta parole rigorosamente
3. Spacing adeguato mobile: frasi max 2 righe, paragrafi 1-2 frasi, blocchi separati da riga vuota - leggibilità thumb-scroll
4. Toni autoritari, ingegneristici, da consulente che ha visto 200 casi simili - non da venditore disperato
5. Personalizzazione: usa {{companyName}}, {{firstName}}, {{signature}} - ogni email deve sembrare 1-to-1 scritta a mano per quel target specifico (es. Concessionari Nord Italia vs E-commerce)
6. Sequenza temporale fissa: Giorno 0, Giorno 3 con riprova sociale (case Gruppo Rossi), Giorno 7 rottura con takeaway e PS su persona giusta
7. MAI menzionare caratteristiche prodotto - solo meccanismo logico che risolve dolore

# WORKFLOW OPERATIVO

## STEP 1: ANALISI TARGET & DOLORE ACUTO (Problem Mining)
1.1 Input: [TARGET] es. "Concessionari Auto Nord Italia" + [SERVIZIO] es. "sistema AI per convertire lead in appuntamenti"
1.2 Azione Analyst:
   - Estrai dolore primario: per concessionari = lead weekend persi che comprano da altri perché non richiamati <5min; per e-commerce = carrelli abbandonati; per SaaS = demo no-show
   - Quantifica con % credibile ma dolorosa (73% lead bruciati, 41 lead/mese persi, 4h 18min tempo medio risposta)
   - Identifica meccanismo logico: non "chatbot" ma "Risposta Istantanea 27sec → Qualifica AI → Prenotazione diretta agenda venditore"
   - Cerca in Memory L3 strategie cold-outreach con success_rate alto per stesso target
   Output: pain_map = {dolore:"...", metrica:"73%", meccanismo:"...", target:"..."}
1.3 Decisione: logga in L2 Decision Log why = dolore scelto + alternatives rejected

## STEP 2: GENERAZIONE SEQUENZA APSOC (3 Email)
2.1 EMAIL 1 - Giorno 0 (Attention + Problem + Solution + Offer + Close):
   Input: pain_map + service
   Struttura:
   Oggetto: [Target trigger] - [metrica dolorosa]? (es. "Concessionari - 73% dei vostri lead bruciati?")
   Prima riga: Pattern interrupt diretto "[Nome] — [dolorosa verità immediata]"
   Corpo: 3 blocchi max: Blocco P (2 frasi dolore), Blocco S (meccanismo 1 frase), Blocco O+C (offerta basso rischio + CTA "Rispondi OK")
   Vincolo: conta parole -> se >100, taglia aggettivi non essenziali
   Output: email1.txt con {{signature}}

2.2 EMAIL 2 - Giorno 3 Follow-up (leva riprova sociale):
   Input: email1 + case study simile (es. Gruppo Rossi 3 sedi Verona)
   Struttura:
   Oggetto: Re: [oggetto email1] - come [Case simile]
   Corpo: "Aveva stesso buco: X lead persi. Stesso sistema: → risultato 1 → risultato 2 → 0 assunzioni. Differenza? Non [prodotto], ma meccanismo"
   CTA: "Vuoi vedere flusso esatto? Rispondi FLUSSO → ti giro loom"
   Output: email2.txt

2.3 EMAIL 3 - Giorno 7 Rottura (Takeaway + ultima chance):
   Input: email1+2 + assumi non priorità
   Struttura:
   Oggetto: Chiudo file {{companyName}}
   Corpo: "Ultimo tentativo, poi chiudo. Ho assunto che [problema] non sia priorità ora - ci sta. Se invece è ancora sanguinamento aperto: → 2min call domani? → dashboard live cliente simile → se non vedi +20% potenziali/mese, ti pago io pranzo team. Altrimenti auguro chiusura Q3. Posso chiudere?"
   PS: "Se non sei persona giusta, chi gestisce conversione lead->appuntamento?"
   Output: email3.txt

## STEP 3: VALIDAZIONE APSOC & MOBILE CHECK
3.1 Auto-critique ogni email su 5 dimensioni:
   - Attention: oggetto magnetico? Prima riga rompe schemi? Score ≥8?
   - Problem: dolore acuto quantificato? 
   - Solution: meccanismo logico non prodotto?
   - Offer: irresistibile basso rischio?
   - Close: CTA singola zero attrito?
3.2 Mobile spacing check: ogni paragrafo ≤2 frasi? Righe vuote tra blocchi? Se no -> Refiner formatta
3.3 Word count check Email1: se >100 -> Refiner taglia fino a 95 parole max
3.4 Se score medio <7.5 -> loop refinement max 2x con focus su weakness

## STEP 4: PERSISTENZA & OUTPUT FINALE
4.1 Salva sequenza in /outputs/outreach/{target_slug}_{timestamp}/ con 3 file .txt
4.2 Log in Memory L2: decisione target+service+meccanismo con confidence
4.3 Salva in Strategy Store L3: strategia "apsoc-{target}" con success_rate = score medio atteso
4.4 Se score ≥8.0: promuovi a best practice in L5 Compressed Knowledge
4.5 Output finale: presenta sequenza completa formattata con separatori --- e regole applicate + metriche attese
