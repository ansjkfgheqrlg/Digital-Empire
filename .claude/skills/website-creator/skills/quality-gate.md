# Skill: quality-gate

Sei il controllore qualità finale. Esegui una verifica completa del file HTML prodotto in 2 fasi: automatica (script Python) e manuale (analisi del codice). Il sito non viene consegnato finché non passa tutti i check.

---

## QUANDO VIENE ATTIVATA

Chiamata da `web-master` dopo che `site_builder.py` ha assemblato il file finale. È l'ultimo step prima della consegna.

---

## FASE 1 — VERIFICA AUTOMATICA

Esegui lo script Python:

```bash
python quality_check.py [nome-sito]-index.html --verbose
```

Interpreta l'output:
- ✅ → check passato
- ❌ → errore bloccante — DEVE essere corretto
- ⚠ → warning — valuta se correggere

**Se ci sono errori:** identifica esattamente quale sezione/elemento ha il problema, richiama `section-forge` per quella sezione specifica, riassembla con `site_builder.py`, riesegui il check.

**Ciclo massimo:** 3 iterazioni di correzione. Se dopo 3 tentativi il check fallisce ancora, segnala il problema specifico all'utente e chiedi istruzioni.

---

## FASE 2 — VERIFICA MANUALE

Analisi visiva del codice HTML prodotto. Checklist completa:

### K00 — Silver Mixing (Legge Cosmica)
```
[ ] Scansiona tutti i color: hex nel file
    → Nessuno deve avere saturazione HSL > 70% senza blend silver
[ ] Controlla background: delle sezioni
    → Usa palette K04 approvata, no colori puri
[ ] Controlla stroke degli SVG divisori
    → Usa gradient metallic standard (#94A3B8 → #E3C878 → #94A3B8)
[ ] Controlla fill dei gradient text
    → Usa gradient K05 (argento → oro → bianco → oro → argento)
```

### K01 Legge 1 — Grain
```
[ ] Conta le <section> nel file
[ ] Per ognuna verifica presenza di:
    - Layer 1: "grainy-gradients.vercel.app/noise.svg" → opacity corretto per bg
    - Layer 2: "feTurbulence" → background-size:100px, opacity corretto
[ ] Ogni sezione ha overflow:hidden?
[ ] Il contenuto principale ha z-index:20+ ?
```

### K01 Legge 2 — Pattern Interrupt
```
[ ] Lista sfondi in ordine delle sezioni
[ ] Trova sezioni con background chiaro (#DCD8CF, #F8F6F2, #E8E...)
[ ] Ci sono almeno 2-3 sezioni chiare?
[ ] Non ci sono più di 3 sezioni scure consecutive?
```

### K01 Legge 3A — Lowercase
```
[ ] Titoli h1, h2, h3 sono scritti in minuscolo o hanno text-transform:lowercase?
[ ] Testi dei bottoni sono in minuscolo?
[ ] Nessun testo ALL CAPS tranne label eyebrow e abbreviazioni?
```

### K01 Legge 3B — Strong
```
[ ] Apri il file nel browser → leggi ogni paragrafo
[ ] Ogni <p> ha almeno 1 parola in grassetto visibilmente diversa?
[ ] Ogni <li> ha almeno 1 <strong>?
[ ] I <strong> su sfondo scuro sono #E2E8F0 (non stesso colore del body)?
[ ] I <strong> su sfondo chiaro sono #020202 (non stesso colore del body)?
```

### K01 Legge 4 — SVG Divider
```
[ ] C'è almeno 1 elemento SVG con stroke e linearGradient?
[ ] Il gradient usa la sequenza: #94A3B8 → #E2E8F0 → #E3C878 → #FFF → #E3C878 → #E2E8F0 → #94A3B8?
[ ] Il divisore è visibile e non nascosto da altri elementi?
```

### K01 Legge 5 — Curva
```
[ ] C'è almeno 1 sezione con clip-path contenente Q (bezier) o url(#) o ellipse?
[ ] La sezione curva ha padding-top aumentato (min 60px)?
[ ] La linea decorativa curva è presente (SVG path con Q)?
```

### CATEGORIA SPECIFICA
```
K09 Ebook:
[ ] C'è una sezione mockup 3D del prodotto?
[ ] C'è una sezione "what's inside" / indice contenuti?
[ ] C'è una sezione garanzia con badge visivo?
[ ] Il CTA è ripetuto almeno 3 volte (hero, metà, bottom)?

K10 SaaS:
[ ] C'è la nav sticky con backdrop-filter?
[ ] C'è una sezione loghi clienti / social proof numeri?
[ ] C'è la sezione pricing con 3 tier?
[ ] Il tier centrale è evidenziato?
[ ] C'è il toggle mensile/annuale funzionante?

K11 Fisico:
[ ] C'è l'ATC button sticky su mobile?
[ ] C'è una sezione ingredienti/componenti?
[ ] C'è una galleria prodotto o placeholder?
[ ] Il prezzo ha il formato: barrato + sconto + prezzo attuale?
```

### MOBILE
```
[ ] C'è il meta viewport nell'<head>?
[ ] Ogni sezione ha padding responsive (min 16px laterale)?
[ ] Le grid usano repeat(auto-fit, minmax(...)) o hanno media query?
[ ] I font usano clamp() per scalare su mobile?
[ ] L'ATC sticky è funzionante su mobile (se prodotto fisico)?
```

### PERFORMANCE
```
[ ] Non ci sono immagini pesanti esterne (solo placeholder inline)?
[ ] Il JS è inline e minimale (niente librerie esterne)?
[ ] Il CSS è inline (no fogli esterni oltre Google Fonts)?
[ ] Il file è un single-file standalone (apri nel browser, funziona)?
```

---

## OUTPUT DEL QUALITY GATE

### Se passa tutti i check:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ QUALITY GATE — APPROVATO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

File: [nome-sito]-index.html
Sezioni: [N] | Divisori: [N] | Dimensione: [X] KB

Verifiche superate:
✅ K00 — Tutti i colori argentizzati
✅ K01 L1 — Grain in ogni sezione ([N] sezioni)
✅ K01 L2 — Pattern interrupt ([N] sezioni chiare)
✅ K01 L3A — Tutti i titoli in lowercase
✅ K01 L3B — <strong> in ogni <p> e <li>
✅ K01 L4 — SVG divider metallico presente
✅ K01 L5 — Sezione con bordo curvo presente
✅ Categoria [K09/K10/K11] — Sezioni specifiche presenti
✅ Mobile responsive
✅ Single-file standalone

🎯 Il sito è pronto per la consegna.
Apri [nome-sito]-index.html nel browser.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Se ci sono errori:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ❌ QUALITY GATE — FALLITO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[N] errori da correggere:

❌ [CHECK NAME]
   Problema: [descrizione]
   Sezione: [id sezione]
   Correzione: [istruzione specifica]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Avvio correzione automatica...
[richiama section-forge per le sezioni problematiche]
```

---

## PRIORITÀ DI CORREZIONE

Errori critici (blocca consegna):
1. Colore puro non argentizzato (K00)
2. Sezione senza grain (K01 L1)
3. Nessun SVG divider (K01 L4)
4. Meta viewport mancante

Errori importanti (correggi prima di consegnare):
5. Nessuna sezione chiara (K01 L2)
6. <p> senza <strong> (K01 L3B)
7. Nessuna sezione curva (K01 L5)
8. CTA mancante o non ripetuta

Warning (segnala ma non blocca):
9. Titolo non lowercase (K01 L3A)
10. Font Cinzel non caricato
11. Responsive non ottimale
