---
Type: PROJECT
Status: Active
Tags: #outreach #automation #decisions #architecture #strategy
Created: 2026-04-30
Last updated: 2026-04-30
---

# Decision Log — Outreach System v2.0

Registro cronologico di tutte le decisioni chiave prese durante la costruzione del sistema outreach. Non solo il "cosa" ma il "perché" — il materiale più prezioso per capire le scelte future.

---

## Decisione 1: Da Apify a Facebook Ad Library API gratuita

**Data**: 2026-04-29
**Cosa**: Sostituire Apify (scraping a pagamento) con la Facebook Ad Library API ufficiale (gratuita).

**Perché**:
- Apify costa $50-200/mese — fisso, anche nei mesi senza lead
- Facebook Ad Library API è ufficiale, stabile, e completamente gratuita
- L'API restituisce esattamente quello che serve: business che fanno ads in Italia, con settore e URL pagina

**Trade-off accettato**:
- Apify aveva scraping più flessibile (Google Maps + altri)
- L'API FB richiede un token da rinnovare ogni 60 giorni
- Decisione: vale la pena — il token si rinnova in 5 minuti ogni 2 mesi

---

## Decisione 2: Da Haiku a Sonnet per le email (poi cambiata)

**Data**: 2026-04-29 → rivista 2026-04-30
**Cosa**: Piano originale usava Claude Haiku. Piano v2 voleva Claude Sonnet 4.6.

**Perché Sonnet inizialmente**:
- Qualità email significativamente superiore per cold outreach
- La risposta rate delle email è l'unica metrica che conta
- Costo stimato: ~$2.50/giorno per 300 email con caching

**Perché poi NVIDIA**:
- L'utente ha un abbonamento Claude Pro (web), che non copre le chiamate API da Python
- Le API Anthropic richiedono crediti separati dall'abbonamento
- NVIDIA Nemotron via OpenRouter è gratuito al 100% via API
- **Soluzione**: compensare la differenza qualitativa con una knowledge base estesa (30+ esempi, framework, regole) che "addestrino" NVIDIA prima di scrivere ogni email

**Trade-off accettato**:
- NVIDIA < Sonnet per qualità creativa pura
- NVIDIA + knowledge base estesa + 3-check QA ≈ output accettabile
- Costo: $0/giorno invece di $2.50/giorno → ~$75/mese risparmiati

---

## Decisione 3: Architettura da 4 a 6 team

**Data**: 2026-04-30
**Cosa**: Aggiungere Team 2 (Copy Knowledge) e trasformare il Team QA in un team di 3 checker.

**Perché Team 2 (Copy Knowledge)**:
- Con NVIDIA invece di Sonnet, la qualità dipende dal contesto fornito
- Il sistema deve "formare" NVIDIA prima che scriva ogni email
- CopyKnowledgeAgent prepara: esempi rilevanti per settore, anti-esempi, regole specifiche, apertura personalizzata
- Risultato: ogni NVIDIA call riceve il miglior contesto possibile per quel lead specifico

**Perché 3-check QA invece di 1**:
- Un singolo check "approva/rifiuta" senza capire perché
- 3 check separati (humanness + APSOC + brand voice) danno feedback specifico al writer
- Se il feedback è preciso, la revisione risolve il problema giusto

**Trade-off accettato**:
- 5 chiamate NVIDIA per ogni email (qualifier + copy_knowledge + strategist + writer + 3 QA)
- Ma NVIDIA è gratuito, quindi il costo è solo di tempo (~50-60 min per 300 email)

---

## Decisione 4: Target 300 email/giorno (non 500)

**Data**: 2026-04-30
**Perché**:
- Gmail free tier: 500 email/giorno è il limite teorico, ma mandare 500/giorno da un account normale aumenta il rischio di spam detection
- 300 email/giorno è il "sweet spot": abbondante per generare lead, sicuro per la reputazione del dominio
- Con il tempo e se servisse di più: creare un secondo account Gmail o passare a Google Workspace ($6/mese)

---

## Decisione 5: 3 Template fissi (A, B, C)

**Data**: 2026-04-29
**Perché**:
- Template A (no sito): angolo loss aversion — clienti persi ogni giorno
- Template B (ads + funnel scarso): angolo ROI — stessa spesa, più conversioni
- Template C (AI implementation): angolo efficienza — ore risparmiate, scalabilità

**Logica**: 3 angoli coprono il 95% dei business italiani raggiungibili su FB Ads. Aggiungere altri template aumenta la complessità senza aumentare il coverage.

---

## Decisione 6: Andrei Pascu come benchmark tono

**Data**: 2026-04-30
**Perché**:
- È il riferimento più riconoscibile nel copywriting B2B italiano
- Il suo stile (diretto, numeri reali, peer-to-peer) è esattamente il tono giusto per cold email
- Audit CRO fatto su di lui (score 51/100) — conosciamo i suoi punti di forza e deboli
- Usarlo come benchmark = standard chiaro per il QA agent

---

## Connessioni

- [[Tool_Outreach_MultiTeam_System]] — il sistema che implementa queste decisioni
- [[Andrei_Pascu]] — il benchmark tono
- [[Concept_Human_Voice_QA]] — il framework QA nato da queste scelte
- [[Concept_APSOC_Email_Application]] — il framework copy scelto
- [[Project_Outreach_Automation_Implementation]] — il progetto padre
