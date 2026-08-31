---
Type: ENTITY
Status: ✅ Attivo — piano editoriale mensile 70 video pronto all'esecuzione
Tags: #youtube #faceless-automation #relationship-niche #attivo
Created: 2026-07-22
Last updated: 2026-08-26
---

# Legami d'amore (@Legamidiamore) — YouTube Channel

## Overview
**Blocco del 07-22 risolto il 2026-08-05**: Max ha fornito le credenziali dirette e login reale
in YouTube Studio è riuscito — il canale è confermato SUO, monetizzato, gestibile. Nicchia reale:
psicologia femminile/maschile, segnali di attrazione — prevalentemente in ITALIANO (correzione:
lo scrape del 07-22 aveva letto "inglese" da un campione non rappresentativo).

Decisione di Max (2026-08-05): il progetto "canale copia di Dose Mentale" va in pausa. Priorità
ora è @Legamidiamore — nicchia INVARIATA, si prosegue con studio competitor + calendario +
produzione+pubblicazione reale sulla stessa fabbrica F1-F6, riconfigurata per questa nicchia.

## Dettagli reali (audit YouTube Studio, login 2026-08-05)
- **Iscritti**: 14.793 (+18 negli ultimi 28gg — crescita quasi ferma)
- **Views ultimi 28gg**: 11,1K · **Watch time**: 1,4K ore
- **Revenue stimata ultimi 28gg: €44,02** — conferma la diagnosi del 07-22 ("rende quasi nulla"
  nonostante 14.7k iscritti e 471 video)
- **Monetizzazione attiva**: sì (revenue tracciata + programma membership disponibile) → canale
  gia' idoneo YPP, non da costruire da zero
- **Top contenuti recenti (48h)**: 148/89/61 view — cadenza di upload rada, non un flusso attivo
- Video reale piu' virale nel campione scrape pubblico: "5 Segnali Che piaci ad una DONNA Ma Lo
  Nasconde" — 29.000 viste, 5.0 views/ora

## Prossimi passi (completati/in corso — aggiornato 2026-08-23)
1. ✅ Studio copy competitor reali (Codice Donna, Psicologia dell'Attrazione, Psicologia Femminile,
   Linguaggio Segreto del Corpo — trovati via ricerca YouTube reale, non inventati)
2. ✅ Calendario contenuti (`CALENDARIO-LEGAMIDIAMORE.md`)
3. ✅ **Primo video reale pubblicato**: https://youtu.be/2t4BZR3KAiU, script replicato da
   competitor vagliato (fonte: 20260805 audit, script scritto 20260816), voce femminile
   realistica (Fliki), scelta deliberata di Max: **Public** (non Private, override esplicito
   sulla regola "sempre privato di default")
4. 🟡 **3 nuovi video in produzione** (2026-08-19): script scritti e passati tutti i gate reali
   (critic 8.10-8.37/10, SEO 92.5-100/100), 3 generazioni Fliki reali avviate — replica da
   competitor `@PsicologiaFemminile-f8c` (catalogo proprio del canale troppo debole, mediana
   0.34 vph). Upload non ancora fatto, in attesa delle copertine di Max (regola permanente:
   nessun upload senza copertina).

## Bug reali trovati e fixati durante la produzione (2026-08-15 → 08-19)
- **Tag SEO inquinati**: `run_phase_5` leggeva anche le etichette interne di pattern copy
  ("comando_maiuscolo", "parentesi") come se fossero keyword cercabili — finivano nei tag YouTube
  reali. Rimossa la fonte, SEO invariato a 92.5/100 con tag ora tutti keyword vere.
- **`duration: 720` bloccava ogni generazione Fliki**: il campo era documentato come "inerte" ma
  Fliki ha iniziato a validarlo sul serio (max 15 minuti). Fixato in `fliki_client.py` e
  `regolatori.py`.
- **Voce reale (Fiamma) legge a ~197-201 parole/minuto**, non le ~140 stimate dal template —
  serve puntare a 2400-2700 parole per un margine reale, non fermarsi al primo PASS del critic.
- **Credential-keeper** (nuovo agente, 2026-08-15): legge `.env`, mai chiede conferma — sblocca
  login persistente, voce femminile cablata, tag SEO a 4 livelli, tutto "ricordato per sempre"
  invece di riconfigurato ogni volta.

## Piano editoriale mensile 70 video / 30 giorni / 3 strategie (2026-08-26)

Dopo il gate "video 03 privato pulito" confermato passato, costruito un piano editoriale
completo e immediatamente eseguibile: 70 video, 27/08→25/09, 3 strategie testate in parallelo,
ognuna mappata su un canale competitor reale verificato con scraping fresco (non cache stale):
- **A — Segnali & Decodifica** (28 video, @PsicologiaFemminile-f8c)
- **B — Tecnica & Comando** (14 video, @PsicologiadellAttrazionee — volume basso deliberato,
  solo 23 candidati reali disponibili sul canale)
- **C — Allarme & Verità Sociale** (28 video, @DinamicheSocialiAcademy)

**Correzione reale trovata nel refresh**: 2 dei 6 canali storicamente monitorati
(`@ciraolone`, `@linguaggiosegretodelcorpo-6589`) sono risultati oggi fuori nicchia (rispettivamente
canale AI/tech e scuola di ballo) — esclusi come fonte, mai usati.

Deliverable: `06-DASHBOARD-E-METRICHE/piano-editoriale-70-legamidiamore-30gg.pdf` (20 pagine,
stile Digital Empire argento/rosso + grana), `01-FLUSSI-E-PIANI/CALENDARIO-70-LEGAMIDIAMORE.md`,
`memory/piano_editoriale_70.json`/`.csv`. Ogni riga è autosufficiente: comando CLI pronto
(`apex7_orchestrator.py run --canale legamidiamore --video-sorgente <url> --phase 1`), nessuna
decisione umana aggiuntiva richiesta. Dettaglio: [CP-20260826-003](../../../company/Memory/checkpoints/CP-20260826-003.md).

## Come Impatta DE
Confermato: ASSET esistente reale (14.8k iscritti, monetizzato), problema di performance non di
accesso — coerente con l'ipotesi (1) del 07-22 ("gia' automatizzato e poi abbandonato"), non la (2).
**Aggiornamento 08-23**: la fabbrica ha chiuso il ciclo completo per la prima volta — dalla
selezione competitor alla pubblicazione reale — e sta scalando a produzione multipla (3 video
in parallelo).

## Connessioni
- [[Entity_Dose_Mentale_Channel]] — stesso genere faceless automation, ora in pausa
- [[Andrei_Pascu]] — perché il modello view non paga come il modello prodotto
- [[project_piano_estate_revenue]]

## Status
- First added: 2026-07-22 · Riconciliato: 2026-08-05 · Primo video pubblicato: 2026-08-18 · Confidence: Alta, dati da login reale + pubblicazione verificata
