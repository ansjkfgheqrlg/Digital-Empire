# 19 — ARENA BUILD LIST (cose da costruire su Arena, scaricare in zip, importare qui)

> Creato 2026-07-22, Claude, su richiesta Max. Arena = piattaforma agente esterna (Max ha accesso),
> usata per costruire workflow/skill/agenti che poi arrivano qui via zip e vengono importati
> (pattern già usato per DIGITAL-EMPIRE/, vedi CP-20260721-004). Ogni riga = 1 build candidata,
> priorità legata a P7 Master Plan (`DIGITAL-EMPIRE/01-PLANNING/PLANNING-P7-MASTER-PLAN.md`).

## Come si usa questa lista
Max sceglie una riga → la fa costruire su Arena → scarica zip → me lo consegna → io lo importo
con lo stesso protocollo ADR-008 (audit secrets/bloat, registro-impresa, skills-map.yaml).

---j

## 🥇 Priorità ALTA — servono ORA (settimana 21-26/07, stream S1/S6)

1. **Script freddo APSOC concessionari (Maps + cold call)**
   Cosa: agente/workflow che genera script di chiamata a freddo per concessionari auto scoperti via
   Google Maps scraping, struttura APSOC (Attenzione-Problema-Soluzione-Obiezioni-CTA), variante
   scritta (WhatsApp/email) + variante vocale (call).
   Perché ora: Max lo ha chiesto esplicitamente ("serve uno script perfetto strategico impeccabile"),
   serve ad ALLARGARE S1 oltre i 7 lead caldi già in lavorazione da WF-S1.
   Nota: WF-S1 (i 7 lead caldi) è GIÀ pronto (A5/A8 reparti 01-AGENCY) — questa build serve per i lead
   NUOVI, non sostituisce quello che esiste.

2. **Google Maps scraper concessionari (lead gen)**
   Cosa: agente che scrape Google Maps per categoria+zona, estrae nome/telefono/sito/recensioni,
   qualifica lead (no sito, ads scarsi = priorità, pattern già in `Agenti/Agency/outreach/rules/`).
   Perché ora: alimenta la lista lead per lo script sopra — senza lead nuovi lo script non serve.

3. **Preventa — pagina + naming asset (rebrand PreventivoForge)**
   Cosa: generatore landing/promo-kit per il nuovo nome "Preventa" (DEC-EST-002, default attivo
   22/07 salvo veto Max). Copy + verifica dominio + kit visivo.
   Perché ora: Gael lo fa già dentro DIGITAL-EMPIRE (S6, 25/07) — se Arena lo fa più veloce/meglio,
   sostituisce quel task, non lo duplica.

## 🥈 Priorità MEDIA — settimane successive (S5 YouTube, compounding)

4. **YouTube niche-scout agent per nicchia AI/Claude ITA**
   Cosa: agente che analizza canali YouTube italiani nicchia AI/Claude Code (DEC-EST-004, nicchia
   già scelta di default), trova pattern titoli/thumbnail/durata che convertono, cross-referenzia
   con l'ICP del Manuale (cross-sell).
   Perché: la skill `.claude/skills/youtube-automation-factory/` esiste già (11 agenti, 5 workflow)
   ma non è mai stata eseguita su una nicchia reale — questo sarebbe il primo run vero (WF1).
   Nota: non duplicare — se Arena costruisce questo, deve WRAPPARE la skill esistente, non
   ricrearla da zero (regola ADR-003 "wrap non riscrivere", vale anche per import da Arena).

5. **Channel audit agent (Legami D'amore + Dose Mentale)**
   Cosa: agente che, dato uno YouTube handle/URL, tira fuori: iscritti, ore di visualizzazione
   stimate, stato monetizzazione, ultimi upload, performance media.
   Perché: serve per decidere SE riattivare Legami D'amore e COSA copiare da Dose Mentale.
   Blocco attuale: servono gli URL/handle dei 2 canali — vedi richiesta sotto, prima cosa da darmi.

6. **✅ Cross-video pattern miner (Andrei Pascu, su second-brain esistente) — COMPLETATO E IMPORTATO 2026-07-22**
   - **Stato:** Costruito su Arena (`workspace-019f88c9-de31-7a8f-ac70-4fe9a6ece098.zip` / `Andrei_Pascu_Sistema_Operativo.zip`), audit ADR-008 superato (0 secrets, 0 bloat), censito in `company/REGISTRO-IMPRESA.md` e `company/skills-map.yaml`.
   - **Contenuto:** `playbook.md` (AP VIDEO SYSTEM e AP SYSTEM, 9 principi, 8-step loop), `checklist_APSOC.md` (25 item GO/NO-GO score ≥92% e log evidenza), `LEGGIMI.md`.
   - **Dove si trova nel sistema:**
     - `SKILL & Agenti/Empire Studio Suite/andrei-pascu-system/`
     - `second-brain-vault/wiki/03 - Frameworks/System_Andrei_Pascu_v1/`
   - **Prossimo step su questo fronte:** Quando Empire Studio girerà sui restanti 19/29 video, userà `checklist_APSOC.md` per validare e arricchire la matrice.

## 🥉 Priorità BASSA — non serve per l'estate, non urgente

7. **Carousel/social asset variant generator** — estende `carousel-factory` esistente, non urgente
   (S3/S4 hanno già motore, tagli 80/20 P7 §6 escludono espansioni questa settimana).
8. **Empire Desk modulo aggiuntivo** — fuori scope, ownership Max, coordinarsi prima di aggiungere.

---

---

## PROMPT PRONTI PER ARENA (copia-incolla, uno per build)

> Regola: ogni prompt dice ad Arena di consegnare uno ZIP auto-contenuto con dentro un `LEGGIMI.md`
> che spiega struttura + come si usa, così l'import qui è pulito. Nessuna chiave API dentro lo zip.

### PROMPT 1 — Script freddo APSOC concessionari (priorità ALTA)
```
Sei un architetto di sistemi di vendita B2B. Costruiscimi un pacchetto completo e auto-contenuto
per fare outreach a freddo verso CONCESSIONARI AUTO italiani, per vendere un software che genera
preventivi personalizzati per i loro clienti (prodotto: "Preventa", ex PreventivoForge).

CONTESTO: il concessionario oggi fa preventivi a mano o con gestionali lenti; perde tempo e clienti
che vogliono risposte veloci. Il nostro software genera un preventivo PDF professionale in minuti,
brandizzato, con voci di prezzo controllate. Modello: licenza a canone, kill-switch remoto.

Voglio che TUTTO segua la formula APSOC (Attenzione, Problema, Soluzione, Obiezione, CTA) + un livello
di consapevolezza crescente (unaware → problem-aware → solution-aware → product-aware).

CONSEGNAMI in uno ZIP:
1. Script CHIAMATA A FREDDO completo (apertura in 8 secondi, gancio, qualifica, pitch APSOC,
   gestione delle 10 obiezioni più comuni dei concessionari con risposta parola-per-parola, chiusura
   con micro-impegno + appuntamento). Tono: diretto, peer-to-peer, zero venditore aggressivo.
2. Script WhatsApp/EMAIL a freddo in 3 messaggi (msg1 gancio, msg2 valore/prova, msg3 CTA+urgenza),
   ognuno <600 caratteri, APSOC compresso.
3. Argomentario obiezioni esteso (tabella: obiezione → cosa nasconde davvero → risposta → prova).
4. 5 varianti di gancio d'apertura A/B da testare.
5. Un mini-copione per il follow-up (giorno +2, +5) senza risultare insistente.
6. LEGGIMI.md che spiega quando usare quale asset e in che ordine.

Vincoli: italiano nativo (non tradotto), niente promesse illegali/garanzie di risultato, niente
prezzi inventati (lascia [PREZZO] placeholder). Massima concretezza, zero teoria.
```

### PROMPT 2 — Google Maps scraper concessionari (priorità ALTA)
```
Costruiscimi uno strumento (script Python auto-contenuto) che, data una lista di città/province
italiane e la categoria "concessionario auto", estragga da Google Maps: nome attività, indirizzo,
telefono, sito web (se presente), numero e media recensioni, e un flag "ha_sito" / "ha_ads_attive".

Deve produrre un CSV pulito e deduplicato, pronto per l'outreach. Aggiungi una colonna "priorità_lead"
calcolata con questa regola: alta priorità = NO sito web OPPURE sito vecchio/scarso (sono i più facili
da convincere che serve modernizzarsi). Includi rate-limiting rispettoso e gestione errori.

CONSEGNA: ZIP con lo script, requirements.txt, un LEGGIMI.md con istruzioni d'uso passo-passo, e un
CSV di esempio con 5 righe finte. NON includere chiavi API nello zip: se serve una API (es. Places),
lascia un .env.example con il nome della variabile e spiega nel LEGGIMI come ottenerla.
```

### PROMPT 3 — Preventa: kit lancio + naming (priorità ALTA)
```
Sei un brand + copy strategist. Il prodotto "PreventivoForge" viene rinominato "Preventa" (verifica
tu se il nome regge come brand; se hai un'alternativa nettamente migliore, proponila con motivazione,
ma il default è Preventa). Costruiscimi il kit di lancio B2B verso concessionari auto.

CONSEGNA in ZIP:
1. Copy landing page one-page (hero APSOC, sezione problema, sezione soluzione con 3 benefici tradotti
   da feature, prova/demo, gestione obiezioni, CTA singola forte, FAQ). Struttura pronta da impaginare.
2. 3 nomi di dominio candidati + note su disponibilità da verificare.
3. Palette + tono di voce del brand (1 pagina).
4. 5 headline alternative per A/B.
5. Un one-pager PDF "brochure commerciale" (testo pronto) da allegare alle email.
6. LEGGIMI.md.

Vincoli: italiano nativo, niente claim garantiti, allineato al posizionamento "software che rende il
concessionario autonomo e veloce, non un'agenzia da cui dipendere".
```

### PROMPT 4 — YouTube niche-scout AI/Claude ITA (priorità MEDIA)
```
Sei un analista YouTube. Analizza la nicchia "AI / Claude / automazione in ITALIANO" su YouTube.
Obiettivo: capire quali formati/titoli/copertine/durate convertono, per un canale che NON punta
all'adsense ma a portare traffico verso un prodotto (un manuale su Claude Code a €67).

CONSEGNA in ZIP:
1. Mappa di 15-20 canali italiani della nicchia con: iscritti, view medie, frequenza upload, formato.
2. Pattern vincenti estratti (struttura titolo, stile copertina, hook primi 15s, durata ottimale).
3. 20 idee di video PRONTE con titolo + angolo, ognuna pensata per finire con CTA al manuale.
4. Template descrizione + tag SEO ottimizzati.
5. LEGGIMI.md che spiega come questo si aggancia alla skill esistente youtube-automation-factory
   (NON ricostruire quella skill: questo pacchetto la alimenta con dati di nicchia reali).

Vincoli: dati reali dove possibile, niente numeri inventati (marca le stime come stime).
```

### PROMPT 5 — Channel audit agent (Legami + Dose + qualsiasi canale) (priorità MEDIA)
```
Costruiscimi uno strumento che, dato un handle/URL YouTube, produca un report di audit: iscritti,
numero video, view medie/mediane ultimi 20 video, ratio view/iscritti (segnala se <2% = pubblico
freddo/gonfiato), lingua, nicchia, frequenza upload, stima grezza di guadagno adsense (view × RPM
di nicchia ÷ 1000) con RPM esplicitato, e un verdetto "vale la pena riattivarlo/comprarlo? sì/no/perché".

CONSEGNA: ZIP con script Python (usa yt-dlp), requirements, LEGGIMI, e un report di esempio.
Deve funzionare offline sui dati pubblici, nessun login richiesto.
```

### PROMPT 6 — Cross-video pattern miner Andrei Pascu (priorità MEDIA)
```
Ti do 10 documenti di analisi (li allego): sono 10 video di Andrei Pascu già analizzati frame-per-frame
sul copywriting. Voglio che tu NON li riassuma uno per uno, ma che estragga i PATTERN RICORRENTI
cross-video: quali principi ripete sempre, quale sequenza logica usa per insegnare, quali esempi/prove
riusa, come struttura un video che converte. Output = un unico "sistema Andrei Pascu" operativo:
un playbook che possiamo applicare al nostro copy e ai nostri video.

CONSEGNA: ZIP con il playbook (markdown), una checklist operativa APSOC derivata, e un LEGGIMI.
```

---

## Regola di import (vale per ogni zip da Arena)
Stesso protocollo ADR-008 già usato per DIGITAL-EMPIRE/: audit secrets (grep chiavi/.env),
audit bloat (node_modules/venv vendorizzati), registrazione in `company/REGISTRO-IMPRESA.md` §5
e `company/skills-map.yaml`, checkpoint in `company/Memory/checkpoints/`. Nessuna eccezione anche
se il contenuto sembra "solo un piccolo script".
