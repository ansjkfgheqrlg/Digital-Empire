---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #landing-page #lancio #design-system #claude-code
Created: 2026-09-06
Last updated: 2026-09-06
---

# Andrei Pascu — armageddon.bsns.it, la pagina di lancio

## Overview
Pagina di lancio a tempo per l'**Armageddon Pack** (outEmail + outFunnel + outHeadline + outViral 2 + voucher 199 € su Funnel Operator) a **199 €** contro 784 € di listino, scadenza 10 settembre 2026. Catturata forense il 2026-09-06: 5.103px desktop, 57 blocchi di copy, 2 CTA. È la decima pagina dello studio siti dell'ecosistema Andrei Pascu e la prima pagina di **lancio** analizzata.

Non è la sua pagina più bella — è la sua **meglio costruita**.

## La scoperta che conta più del design
Il CSS è servito in chiaro e commentato. I commenti citano `docs/homepage-design/full-page-mockup.pdf` (826,46 × 2.851,92 unità), **`CLAUDE.md §4`**, `assets/brand.css`, un ticket **`AP-138`** e richieste datate (*"Andrei asked on 5 September"*).

**Andrei Pascu costruisce le sue landing con Claude Code**, con un CLAUDE.md numerato e citabile, un brand.css di casa, un mockup PDF misurato in unità e un sistema di ticket. Con il nostro stesso strumento.

## I fatti tecnici
- **Zero framework, zero build, zero dipendenze.** 1 CSS di 1.020 righe scritto a mano + 1 IIFE inline da 5,6 KB. Funziona con JavaScript disattivato.
- **La colonna `--u`**: `min(100cqw, 960px)`. Ogni misura della pagina è `calc(var(--u) * frazione)`, con cifre non arrotondate (`0.86487`, `0.330483`). Un solo media query in tutto il file.
- **Due colori**: `#000` e `#bc0807`. La gerarchia la fa una scala di opacità del bianco (0.42 → 1): più un testo è vicino al denaro, più è opaco.
- **Due caratteri**: Curseyt (blackletter self-hosted, `font-display: block`) grida, Plus Jakarta Sans spiega.
- **Nativo al posto delle librerie**: `<dialog>`, `<details>`, `IntersectionObserver`, `scrollbar-gutter`, container query, `prefers-reduced-motion` che spegne anche il JavaScript.
- **I prezzi si sommano dal DOM** (`data-price`): 784/199/585 non sono scritti a mano da nessuna parte.

## La struttura
57 blocchi di copy su 5.103px, contro i 337 di `/copy` e i 241 di `outheadline`. Nessun benefit, nessuna prova sociale, nessuna bio, nessuna garanzia: **la pagina di lancio non vende, incassa.** La persuasione è già avvenuta nel video da 13 minuti e nella lista. Regge solo su traffico caldo.

## Il copy
Undici FAQ, e **sei allontanano l'acquisto**: *"Ho già uno dei quattro corsi. Posso pagare meno?" — "No. […] fai tu il conto prima di comprare."* · *"Mi garantite dei risultati?" — "No, e diffida di chi lo fa."* Il voucher è spiegato con quattro negazioni consecutive che chiudono ogni contestazione prima del pagamento.

## I difetti misurati
Contatore che non gestisce la propria scadenza · `mailto` blu di default, unico colore fuori palette · zero dati strutturati con 11 FAQ scritte bene · nessun fallback per chi non guarda il video.

## Cosa ne è nato
[[Dossier_32_Fabbrica_Siti]] — il sistema unico di Digital Empire per produrre siti, con le 12 mosse prese da qui e i 3 difetti trasformati in controlli automatici.

## Connessioni
- [[Source_Andrei_Pascu_10_Lead_Magnet]]
- [[Source_Andrei_Pascu_Importanza_Landing]]
- [[Source_Andrei_Pascu_Ordine_Funnel]]
- `competitor/Andrei Pascu/site-study/reports/11-armageddon.md` — rapporto completo
- `competitor/Andrei Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md` — schermata per schermata
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — il piano
