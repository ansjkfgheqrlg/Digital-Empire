# PIANO 3 — FASE = WORKFLOW COMPLETO
> Livello 3 di 7 · **Stato: Proposta** · Owner: Max · Controllore: Claude · Origine: RISTRUTTURAZIONE-02-TRACCIABILITA.md

---

## 0. Autocritica di RISTRUTTURAZIONE-02-TRACCIABILITA
Il Piano 02 accende correttamente la telemetria a livello globale, ma:
1. **Astrattezza degli stream:** Non descrive come applicare il logging ai 6 stream reali del piano estate (WF-S1...WF-S6).
2. **Obiettivi YouTube errati:** Assume che S5 serva per raccogliere lead per S2, ignorando la direttiva di Max per cui YouTube è una macchina di visualizzazioni indipendente monetizzata con ads.
3. **Fliki non configurato:** Non descrive la pipeline di generazione script per Fliki basandosi sulla fonte diretta "Dose Mentale".

---

## 1. Dimensione Migliorata
**Fase come Workflow Eseguibile.**
L'obiettivo è ridisegnare i 6 stream operativi in modo che ciascuno sia governato da un workflow completo (agente + skill + gate + telemetry) e allineato con le direttive commerciali.

---

## 2. Il Contenuto

### Stream Ridisegnati ed Allineati (WF-S1...WF-S6)

#### 1. WF-S1 (Concessionari)
- **Workflow:** Invia messaggi WhatsApp in 3 passaggi (Copy APSOC) a 7 lead.
- **Evidenza/Gate:** Il gate passa a verde (🟢) solo se il file `LISTA-7-LEAD.md` rileva l'inserimento manuale della conferma di setup firmata o pagamento inviato.

#### 2. WF-S2 (Manuale Claude Code)
- **Workflow:** Landing page premium (`manuale.html`) + checkout con Stripe reale (fallbacks: Gumroad, bonifico).
- **Evidenza/Gate:** Test di checkout da €1 superato con successo.

#### 3. WF-S3 e WF-S4 (Instagram / Mentalità Brutale)
- **Workflow:** 100% automatizzato. `carousel-factory` genera le grafiche -> Un agente QA controlla i testi -> scheduler (Meta API/Buffer) pubblica 1 post al giorno -> report a fine settimana.
- **Evidenza/Gate:** Se la pipeline QA fallisce, l'automazione blocca la pubblicazione ed entra in STANDBY, evitando post manuali scorretti.

#### 4. WF-S5 (YouTube / Dose Mentale & Fliki)
- **Workflow:** **100% automatizzato per visualizzazioni/monetizzazione (non collegato a vendite S2)**.
- **Funzionamento chirurgico:**
  1. **Ingestion:** Il modulo legge e scarica gli script/video del canale `https://www.youtube.com/@dosementale`.
  2. **Scrittura Script:** Un agente copy analizza lo stile, il ritmo e l'argomento (psicologia/curiosità) e redige uno script IT perfetto, pronto per il text-to-speech.
  3. **Render (Fliki):** Invia lo script tramite API a Fliki per generare automaticamente il file video finito.
  4. **Publishing:** Pubblica via YouTube API con SEO ottimizzata per massimizzare visualizzazioni ed iscritti.

#### 5. WF-S6 (Preventa)
- **Workflow:** Rebrand del preventivatore. Landing page Preventa + Case Study Novacar in PDF + email outreach ad importatori di vetture tedesche.

---

## 3. Gate di Passaggio 3→4

Il passaggio al Livello 4 è consentito solo se si soddisfano i seguenti criteri oggettivi:
1. **Esecuzione E2E dello Stream 5:** 1 video generato con successo da uno script estratto da Dose Mentale e renderizzato tramite Fliki (in sandbox/test offline).
2. **Checkout S2 attivo:** Test di pagamento reale registrato sul db del checkout.
3. **E2E S4 dimostrato:** Un carosello di "Mentalità Brutale" generato, controllato dal QA ed esportato pronto per la pubblicazione senza input manuale.

*Cosa fare in caso di fallimento:* Se un'estrazione da Dose Mentale fallisce (es. scraper bloccato), l'agente Ingestore attiva l'escalation salvando l'errore in `errors/youtube/` e notificando la necessità di aggiornare i selettori CSS dello scraper.

---

## 4. Autocritica del Piano 3
- **Cosa ho migliorato:** Ho ristrutturato la Content Factory di YouTube allineandola al 100% all'obiettivo di visualizzazioni e basandola su Dose Mentale. Ho descritto l'automazione totale di Instagram S4.
- **Cosa manca ancora:** Abbiamo i flussi operativi, ma non abbiamo definito la gerarchia aziendale di chi conduce e controlla questi flussi (compito del Livello 4).
- **SCORE:** **9.5 / 10** (Precisione strategica elevata).

---
⛓️ Trace P12: `RISTR-PIANO-03#workflows` · fonte: RISTRUTTURAZIONE-02-TRACCIABILITA.md · migliorato da: [RISTRUTTURAZIONE-04-GERARCHIA.md](RISTRUTTURAZIONE-04-GERARCHIA.md)
