---
name: site-report
description: Genera il report finale da consegnare al cliente. Aggrega tutti gli output del progetto in un documento completo che mostra le decisioni prese, il design system, i risultati del QA, la checklist di deploy e i prossimi passi consigliati post-lancio.
---

Sei la skill di chiusura del sistema /site. Generi il documento finale che racconta l'intero progetto — dalle decisioni iniziali ai risultati del QA — in un formato consegnabile al cliente.

## Trigger

Attivata da `/site report`. Ultimo step del flusso, dopo `/site deploy`.

## Input

Leggi tutto ciò che esiste nella CWD. I file da cercare, in ordine di priorità:

**Obbligatori (il report non può essere completo senza questi):**
- `SITE-BRIEF.md`
- `SITE-STACK.md`
- `SITE-PLAN.md`
- `SITE-DESIGN.md`
- `SITE-BUILD.md` (o i file HTML per derivare le info)

**Altamente consigliati:**
- `SEO-AUDIT.md`
- `QA-REPORT.md`
- `DEPLOY-CHECKLIST.md`
- `SITE-COPY.md` (per citare headline e copy key)
- `SITE-STATUS.md`

**Opzionali — se presenti, integra:**
- `MARKETING-AUDIT.md` (da sessioni `/market audit`)
- `LANDING-CRO.md` (da sessioni `/market landing`)
- `design-tokens.css` (per estrarre palette esatta)

## Processo

### Step 1 — Leggi tutti i file disponibili
Usa Glob per trovare tutti i file `.md`, `.css`, `.html` nella CWD. Leggi ogni file rilevante nell'ordine sopra elencato. Prendi nota mentale di: nome progetto, tipo sito, stack usato, pagine costruite, score QA, piattaforma deploy.

### Step 2 — Genera `SITE-REPORT.md`

Struttura il documento con queste sezioni nell'ordine esatto:

---

**1. COVER**
```markdown
# [Nome Progetto] — Site Report

**Data:** [data di oggi]
**Tipo sito:** [da SITE-BRIEF.md]
**Stack:** [Percorso A/B/C — da SITE-STACK.md]
**Pagine costruite:** [numero]
**URL finale:** [se disponibile, altrimenti "Da configurare"]
**Consegnato da:** Sistema /site — Digital Empire
```

**2. EXECUTIVE SUMMARY**
3-5 bullet point che sintetizzano:
- Cosa è stato costruito e per chi
- L'approccio tecnico scelto e perché
- Il risultato del QA (Site Quality Score)
- Lo stato del deploy
- Il prossimo passo raccomandato

**3. BRIEF E OBIETTIVI**
- Sintesi dei requisiti raccolti nel brief (tipo sito, audience, obiettivi, tone of voice)
- Come ogni obiettivo è stato soddisfatto nel sito costruito
- Eventuali deviazioni dal brief originale con motivazione

**4. DECISIONI DI STACK**
- Percorso scelto (A/B/C) con motivazione specifica per questo progetto
- Repository/librerie usate con link
- Decisioni tecniche chiave (es. "Scelto Tailwind CDN per semplicità di deployment senza build step")

**5. ARCHITETTURA INFORMATIVA**
- Sitemap con tutte le pagine e URL
- Struttura di navigazione
- Motivazione dell'ordine e della gerarchia delle pagine

**6. SISTEMA DI DESIGN**
- Nome del movimento estetico e i 3 principi visivi
- Palette colori: nome colore + hex + uso (estrai da design-tokens.css)
- Tipografia: font display + font body + scale usata
- Componenti chiave: button variants, card style, spacing system

**7. COPYWRITING**
- Approccio al tono di voce e framework usato (AIDA, PAS, 4U)
- H1 scelte per le pagine principali (citale letteralmente)
- CTA principale adottata
- Note sul processo copy (eventuali scelte stilistiche rilevanti)

**8. BUILD SUMMARY**
- Lista pagine create con nome file e sezioni implementate
- Componenti custom sviluppati
- File JS prodotti e funzionalità implementate
- Note tecniche rilevanti (es. "FAQ implementata con <details> nativo per accessibilità")

**9. QUALITY ASSURANCE**
- Site Quality Score totale: [N]/100 — [etichetta]
- Breakdown per dimensione (tabella da QA-REPORT.md)
- Issue critiche risolte (se presenti)
- Issue rimanenti con severity e raccomandazione

**10. SEO IMPLEMENTATION**
- Schema markup implementati (lista)
- Meta tag completezza (% pagine con title + meta description)
- sitemap.xml e robots.txt: presente/assente
- Keyword focus identificate
- Highlights del SEO-AUDIT.md

**11. DEPLOY GUIDE**
- Piattaforma scelta con motivazione
- File di configurazione generati
- Comandi per il deploy:
  ```bash
  # Vercel
  npx vercel --prod

  # Netlify
  netlify deploy --prod --dir .

  # GitHub Pages
  git push origin main  # (trigger GitHub Actions automaticamente)
  ```
- Prossimi passi tecnici post-deploy (DNS, SSL, Analytics)

**12. RACCOMANDAZIONI POST-LANCIO**

Sezione con azioni consigliate dopo il go-live, ordinate per priorità:

*Settimana 1 — Verifica tecnica:*
- Esegui Lighthouse audit sull'URL live (target: Performance ≥ 80, Accessibility ≥ 90)
- Verifica Google Search Console: nessun errore di crawl
- Testa il form di contatto con un invio reale
- Controlla Analytics: il tracking riceve dati?

*Mese 1 — Ottimizzazione:*
- `/market audit [url]` — analisi completa del sito live
- `/market seo [url]` — SEO audit live con keyword ranking
- Raccogli i primi feedback utenti reali
- Identifica le pagine con bounce rate più alto

*Iterazione continua:*
- Content plan per blog (se presente) — frequenza consigliata: 2 articoli/mese
- A/B test suggeriti: [indica 2-3 elementi da testare specifici per questo progetto, es. "CTA primario vs variante", "Hero con video vs immagine statica"]
- Social media content: `/market social` per il piano editoriale

**13. APPENDICE — FILE PRODOTTI**
Lista completa di tutti i file generati durante il progetto:
```
SITE-BRIEF.md
SITE-STACK.md
SITE-PLAN.md
SITE-DESIGN.md
design-tokens.css
style-guide.html
SITE-COPY.md
index.html
[altre pagine].html
css/styles.css
css/design-tokens.css
js/main.js
js/interactions.js
js/animations.js (se /site animate eseguito)
sitemap.xml
robots.txt
QA-REPORT.md
SEO-AUDIT.md
DEPLOY-CHECKLIST.md
vercel.json / netlify.toml / deploy.yml
SITE-REPORT.md (questo documento)
```

---

### Step 3 — Aggiorna SITE-STATUS.md

Segna Report come completato. Aggiorna la fase a: **"PROGETTO COMPLETATO ✅"** con data e ora.

## Comunicazione Finale

Al termine mostra all'utente:

```
✅ PROGETTO COMPLETATO

📄 SITE-REPORT.md generato — pronto da consegnare al cliente.

Riepilogo rapido:
• Pagine costruite: [N]
• Site Quality Score: [N]/100
• Deploy: [piattaforma] — [stato]

Prossimi passi consigliati:
1. Configura DNS e SSL sul dominio
2. Testa il form di contatto live
3. Invia sitemap.xml a Google Search Console
4. Esegui /market audit [url] dopo la prima settimana live
```
