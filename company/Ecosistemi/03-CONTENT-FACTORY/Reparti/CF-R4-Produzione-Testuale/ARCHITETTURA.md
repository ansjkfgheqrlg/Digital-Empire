---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #content-factory #CF-R4 #produzione #testuale #handoff-marketing
Created: 2026-06-19
Last updated: 2026-06-19
---

# ARCHITETTURA — CF-R4 Produzione Testuale

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Produzione · **Reparto:** CF-R4

---

## Posizione nella gerarchia CF-DE

```
CF-DIRECTOR (CF-D-LEAD)
│
└── L1-PROD — CAPO AREA PRODUZIONE
    │
    ├── CF-R3 — PRODUZIONE VIDEO
    │
    ├── CF-R4 — PRODUZIONE TESTUALE  ← questo reparto
    │         CF-R4-COORD riporta a L1-PROD
    │
    └── CF-R5 — VISUAL & DESIGN / CAROSELLI
```

CF-R4-COORD è il punto di contatto verso L1-PROD per ogni escalation, aggiornamento
di stato e report di reparto. Non riporta mai direttamente al CF-Director: passa sempre
per L1-PROD (separazione di livello, pattern MEGA-REPARTO ADR-007).

---

## Confine CF/MARKETING — invariante non valicabile

Il confine tra CF-R4 e 04-MARKETING è la regola architetturale più importante del reparto:

| Tipo di testo | Owner | Percorso |
|---|---|---|
| Corpo articolo, narrative, spiegazioni, storytelling | CF-R4 | WF-ARTICOLO |
| Corpo newsletter (editoriale, racconto, approfondimento) | CF-R4 | WF-NEWSLETTER |
| Script video strutturale (hook, corpo, CTA strutturale) | CF-R4 | WF-SCRIPT |
| Derivati multi-formato da pezzo madre | CF-R4 | WF-REPURPOSING |
| Caption editoriali (informative, narrative) | CF-R4 | WF-REPURPOSING / CF-R4-CAPTION |
| **Blocco CTA APSOC, headline sales, copy ads** | **04-MARKETING** | **HC-MK-CF-01** |
| **Claim di risultato con prove, garanzie, scarcity** | **04-MARKETING** | **HC-MK-CF-01** |

CF-R4 non valica mai il confine. Sui pezzi ibridi (newsletter con CTA, script con
call-to-action di vendita), CF-R4 scrive il corpo e si ferma prima della sezione APSOC;
emette la richiesta `HC-MK-CF-01` verso 04-MARKETING con il contesto del pezzo;
attende il blocco APSOC approvato dalla Copy Guild di MARKETING; poi fa il merge.

---

## Topologia degli agenti e flusso principale

```
[IN] brief.json da orders/<id>/01-brief/
     (prodotto da CF-R1; brand_kit + icp già caricati)
        │
        ▼
CF-R4-COORD — scelta workflow
  ├── formato: articolo / newsletter → WF-ARTICOLO o WF-NEWSLETTER
  ├── formato: script / video → WF-SCRIPT
  └── formato: repurposing → WF-REPURPOSING
        │
        ▼
CF-R4-WRITE — produzione draft
  Riceve brief + brand_kit.voice + icp
  Produce outline → draft completo → struttura heading
        │
        ├── (se articolo) ─────────────────────────────────▶ CF-R4-SEO
        │                                                     Pass SEO/AI-SEO
        │                                                     (keyword density,
        │                                                      heading H1-H3,
        │                                                      meta description,
        │                                                      schema markup)
        │◀─────────────────────────────────────────────────────────────────────
        │
        ├── (se newsletter) ──────────────────────────────▶ HC-MK-CF-01
        │                                                    Richiesta blocco
        │                                                    APSOC a MARKETING
        │◀─────────────────────────────────────────────────── blocco approvato
        │
        ├── (ogni formato) ──────────────────────────────▶ CF-R4-HEADLINE
        │                                                   3 varianti titolo A/B
        │◀──────────────────────────────────────────────────────────────────────
        │
        ▼
CF-R4-QA — GATE-COPY (BLOCCANTE)
  [ ] Struttura heading valida (H1 unico, H2/H3 coerenti)
  [ ] Hook in apertura (prime 3 righe / primo paragrafo)
  [ ] CTA presente e unica (o handoff MARKETING documentato)
  [ ] Zero claim non verificabili (Mandato Art.2)
  [ ] Parole_vietate assenti (brand_kit.voice)
  [ ] Lunghezza coerente con brief (word_count ±20%)
  PASS → avanza a GATE-BRAND (CF-R6) → output
  FAIL → motivo strutturato → rework agente specifico
        │
        ▼
[OUT] orders/<id>/02-copy/ → articolo.md | newsletter.html | script.md | captions.json
      orders/<id>/state.json aggiornato: fase "02-copy" completata
```

---

## Handoff HC-MK-CF-01 — dettaglio

Il handoff `HC-MK-CF-01` è bidirezionale:

**Da CF-R4 verso 04-MARKETING:**
```json
{
  "handoff_id": "HC-MK-CF-01-<order_id>",
  "mittente": "CF-R4-COORD",
  "destinatario": "04-MARKETING/L2-1-Copywriting",
  "tipo": "richiesta-blocco-APSOC",
  "order_id": "CF-2026-0099",
  "brand_slug": "brand-agency",
  "contesto": "Newsletter settimanale Agency — corpo scritto; manca blocco CTA per offerta Engine Room",
  "corpo_cf_path": "orders/CF-2026-0099/02-copy/newsletter-corpo.md",
  "icp_ref": "brands/brand-agency/icp.json",
  "cta_target": "prenotare discovery call",
  "sla_ore": 24
}
```

**Da 04-MARKETING verso CF-R4:**
```json
{
  "handoff_id": "HC-MK-CF-01-<order_id>",
  "mittente": "04-MARKETING/L2-1-Copywriting",
  "destinatario": "CF-R4-COORD",
  "tipo": "consegna-blocco-APSOC",
  "gate_copy_guild": "PASS",
  "blocco_path": "orders/CF-2026-0099/02-copy/cta-apsoc.md",
  "note": "blocco APSOC approvato; merge nella sezione finale newsletter"
}
```

CF-R4-COORD non fa merge finché `gate_copy_guild` non è `PASS`. Il blocco non approvato
non entra nel pezzo — mai, per nessuna ragione di urgenza.

---

## Namespace

| Namespace | Path | Owner scrittura | Regole |
|---|---|---|---|
| `cf/text` | `orders/<id>/02-copy/*.md` | CF-R4-QA (solo su PASS) | Solo testo con gate CF-R4-QA = PASS |
| `cf/scripts` | `orders/<id>/02-copy/script.md` | CF-R4-QA | Script con hook 3s verificato |
| `cf/captions` | `orders/<id>/02-copy/captions.json` | CF-R4-CAPTION | Caption per canale; limiti piattaforma rispettati |

---

## Dry-run per ogni workflow

Ogni workflow espone la modalità dry-run:
- `WF-ARTICOLO dry-run` → produce `outline.json` senza scrivere il draft
- `WF-NEWSLETTER dry-run` → produce `struttura-newsletter.json` senza avviare HC-MK-CF-01
- `WF-SCRIPT dry-run` → produce `script-intent.json` (hook + struttura, non il testo completo)
- `WF-REPURPOSING dry-run` → lista derivati pianificati con formato e lunghezza stimata

Il dry-run non aggiorna `state.json` con fase completata e non avvia handoff reali.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R4`
- [[CF-R1-Strategia-Brief]] · fornitore brief.json validato (input di ogni workflow)
- [[CF-R6-QA-Gate]] · destinatario del testo per gate finale GATE-BRAND + GATE-COPY-APSOC
