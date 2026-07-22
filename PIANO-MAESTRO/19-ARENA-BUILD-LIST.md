# 19 — ARENA BUILD LIST (cose da costruire su Arena, scaricare in zip, importare qui)

> Creato 2026-07-22, Claude, su richiesta Max. Arena = piattaforma agente esterna (Max ha accesso),
> usata per costruire workflow/skill/agenti che poi arrivano qui via zip e vengono importati
> (pattern già usato per DIGITAL-EMPIRE/, vedi CP-20260721-004). Ogni riga = 1 build candidata,
> priorità legata a P7 Master Plan (`DIGITAL-EMPIRE/01-PLANNING/PLANNING-P7-MASTER-PLAN.md`).

## Come si usa questa lista
Max sceglie una riga → la fa costruire su Arena → scarica zip → me lo consegna → io lo importo
con lo stesso protocollo ADR-008 (audit secrets/bloat, registro-impresa, skills-map.yaml).

---

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

6. **Cross-video pattern miner (Andrei Pascu, su second-brain esistente)**
   Cosa: agente che legge le 10 pagine `Source_Andrei_Pascu_*` già in wiki + le pagine `Concept_*`
   collegate, e produce sintesi cross-video (pattern ricorrenti, non ripetizioni per singolo video).
   Perché: i primi 10/29 video Andrei Pascu sono già ingeriti (Empire Studio, dati reali, non stime)
   — questa build NON è "guardare i video da zero", è mining di quello che già abbiamo.
   Nota: i restanti 19/29 video vanno comunque ingeriti con Empire Studio (pipeline video reale,
   non sostituibile da Arena — Arena può minare solo quello che è GIÀ stato visto).

## 🥉 Priorità BASSA — non serve per l'estate, non urgente

7. **Carousel/social asset variant generator** — estende `carousel-factory` esistente, non urgente
   (S3/S4 hanno già motore, tagli 80/20 P7 §6 escludono espansioni questa settimana).
8. **Empire Desk modulo aggiuntivo** — fuori scope, ownership Max, coordinarsi prima di aggiungere.

---

## Regola di import (vale per ogni zip da Arena)
Stesso protocollo ADR-008 già usato per DIGITAL-EMPIRE/: audit secrets (grep chiavi/.env),
audit bloat (node_modules/venv vendorizzati), registrazione in `company/REGISTRO-IMPRESA.md` §5
e `company/skills-map.yaml`, checkpoint in `company/Memory/checkpoints/`. Nessuna eccezione anche
se il contenuto sembra "solo un piccolo script".
