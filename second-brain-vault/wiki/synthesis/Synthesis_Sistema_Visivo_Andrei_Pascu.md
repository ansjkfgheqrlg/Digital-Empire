---
Type: SYNTHESIS
Status: Active
Tags: #andrei-pascu #sistema-visivo #onda-g #fabbrica-siti
Created: 2026-09-10
Last updated: 2026-09-10
---

# Il Sistema Visivo di Andrei Pascu — sintesi per l'Impero

## La Domanda
Cosa ha di operativo il sistema visivo di Andrei Pascu, misurato a macchina su 52 pagine del suo
ecosistema (non a occhio), e cosa contraddice — invece di confermare — il canone visivo di casa?

## Fonte
`competitor/Andrei Pascu/site-study/SINTESI-SISTEMA-VISIVO.md` — chiusura dell'onda G, 2026-09-09,
costruita dai `scheda.json` di ogni pagina, non dalle prose dei singoli teardown.

## I fatti misurati

**Due mondi.** Squarespace (44 pagine, negozio): 4,8 immagini/1.000px. Artigianale (7 pagine, lanci
e agenzia): 1,2 immagini/1.000px — quattro volte meno. La disciplina non è il suo gusto: è dove
costruisce. Sulla piattaforma il costo di aggiungere un'immagine è zero.

**Su tre quarti dell'ecosistema (38/52) non dichiara un carattere.** Prende il default del browser
(`sans-serif`). Solo dove costruisce a mano il carattere è scelto (`Elza, Inter` / `Inter`) — 5
pagine su 52 hanno una voce tipografica propria.

**Il prezzo NON governa la forma della pagina** (correzione a un rapporto precedente basato su sole
3 pagine): il prodotto da 98€ e quello da 999€ hanno praticamente la stessa altezza (26.993 vs
26.952 px). **La temperatura del traffico governa tutto**: pagine "gradino" (≤2.200px, chi non ha
ancora deciso) hanno 4,9 CTA medie; pagine "di vendita" (≥9.000px, chi sta valutando) hanno 16,2 CTA
medie — undici volte l'altezza, tre volte le CTA.

**La regola dell'accento è vera al 60%, non su tutto.** Un accento speso una volta sola su 31 pagine
su 52; le 14 eccezioni sono concentrate dove la pagina naviga invece di decidere (home, negozio).
Conferma la regola per le pagine che decidono — che è dove il canone Empire la vuole.

## Dove è già dentro il canone di casa (`fabbrica-siti/CLAUDE-SITI.md`)

§8 (nessun dato duplicato), §11 (la cassa ha un gradino — pre-cassa), §12 (l'accento si spende una
volta) citano già rapporti precedenti dello stesso site-study (`11-armageddon`,
`24-25-27-28-macchina-del-funnel`). **Non duplicato qui.**

## Cosa resta nuovo (onda G, non ancora legge — richiede ADR per entrare in `CLAUDE-SITI.md`)
- La temperatura del traffico, non il prezzo, decide l'altezza e la densità di CTA di una pagina.
- Il carattere si dichiara sempre — un `sans-serif` implicito è un'identità regalata al browser.
- Densità immagini/1.000px sopra 5,0 → WARN (la pagina si riempie di figure invece che di
  argomenti).

Segnalato in `.claude/skills/empire-premium-style/SKILL.md` (nota 2026-09-10) come lavoro aperto per
Max/Emperator — non applicato in silenzio, perché cambiare un articolo di `CLAUDE-SITI.md` richiede
un ADR, non una patch di skill.

## Dove il canone di casa vince e NON si tocca

Il colore d'accento `#fb4604` sotto il 10% dell'area e la firma argento/grana **non sono in
contraddizione** con questo studio — anzi lo stesso arancione è stato misurato identico su
`claude-speedrun.com` (fonte: `company/02-info-business/ccm/brand/CCM-Brand-Guidelines.pdf`). Nessun
innesto necessario qui: è conferma, non correzione.

Le tre skill generiche nominate per il lato visivo (`frontend-design`, `brand-guidelines`,
`theme-factory`) **non sono skill di brand Digital Empire**: sono toolkit generici forniti da
Anthropic (brand-guidelines porta la palette Anthropic stessa, theme-factory 10 temi PPT generici,
frontend-design è un toolkit di stile senza canone proprio) — innestarci contenuto specifico
Andrei Pascu/Digital Empire inquinerebbe strumenti non di casa. La vera casa del sistema visivo di
Digital Empire è `fabbrica-siti/canone/` e `CLAUDE-SITI.md`.

## Connessioni
- [[Synthesis_Sistema_Copy_Andrei_Pascu|Il Sistema di Copy di Andrei Pascu]] — l'altro documento di
  chiusura dell'onda G
- [[synthesis/Piano_Implementazione_Andrei_Pascu|Piano di Implementazione — Andrei Pascu]]
- [[Tool_Conoscenza_Empire_Agente|CONOSCENZA-EMPIRE]] — possiede e cita questo corpus
- [[Concept_CCM_Brand_Guidelines|Brand Guidelines CCM]] — il canone visivo di casa che questo studio
  conferma dall'esterno
