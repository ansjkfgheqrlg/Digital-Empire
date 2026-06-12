> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A6 + sez. 4 + sez. 8

# A6 — MARKETING-INTERNO

> Reparto L2 di 01-AGENCY · Coordinatore: `AG-A6-COORD` (sonnet) · Topologia: `star`
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A6

## Cosa fa

Gestisce la **vetrina e la prova sociale** dell'agency: landing, presentazione, case study,
testimonianze e upsell mapping. Genera inbound e **munizioni** per outreach e preventivi.
Regola fondamentale: solo metriche e risultati reali — **"prove non promesse"** (Mandato Empire).

| Livello | Team | Flusso / Funzione |
|---|---|---|
| L3 | `WF-ASSET-VETRINA` | manutenzione `agency-empire-landing` + `presentazione-empire.vercel.app` (build via 06 PLATFORM) |
| L3 | `WF-CASE-STUDY` | delivery chiusa → raccolta testimonianza → case study APSOC → produzione asset via 03 CF → pubblicazione |
| L4 | `T-proof-collector` | raccolta testimonianze e metriche reali a fine 90gg supporto ("prove non promesse") |
| L4 | `T-case-writer` | scrittura case study con skill `cro-copy-architect` (struttura APSOC: problema → soluzione → risultato reale) |
| L4 | `T-upsell-mapper` | mappa cliente→prossima offerta (prodotto singolo → Engine Room €8.000; cliente → referral) |

Agenti L5: `AG-A6-COORD` · `AG-A6-PROOF-W` · `AG-A6-CASE-W` · `AG-A6-UPSELL-W`
(schede in `../../Agenti/`).

## Come si collega

| Direzione | Con chi | Cosa passa |
|---|---|---|
| ← A4 Delivery | intra-BUS | segnale "Gate Delivery firmato" + metriche reali → avvia `WF-CASE-STUDY` |
| → A2 Acquisizione | intra-BUS | case study e metriche reali come munizioni per outreach e preventivi |
| → A5 Copy-interno | intra-BUS | testimonianze reali come input per libreria obiezioni e copy |
| → 03 CONTENT-FACTORY | `HC-AG-CF-01` | brief case study → asset grafici/video (caroselli, reel social proof) |
| → 06 PLATFORM | `HC-AG-PL-01` | feature request per landing e presentazione |
| ← 04 MARKETING | `HC-MK-AG-01` | copy sales page e case study maggiore (refresh strutturali) |
| Memoria | `agency/clients` · `agency/kpi` | testimonianze + metriche per tenant; feed del ReasoningBank |

Asset esistenti: `agency-empire-landing/` (**usa-così**, evolvi con case study quando arrivano);
`presentazione-empire.vercel.app` (**usa-così**, CTA standard di ogni canale outreach).
Skill operative: `case-study-forge` (da delivery chiusa a case study APSOC verificato);
`upsell-mapper` (matrice cliente→offerta).

## Come si ATTIVA e RAGIONA

**Trigger.**
1. Gate Delivery firmato → `T-proof-collector` contatta il cliente (messaggio personalizzato,
   non automatico: "prove non promesse" richiede raccolta attiva, non presunta).
2. 90gg supporto chiusi → `T-upsell-mapper` analizza il cliente per cross-sell / Engine Room / referral.
3. Aggiornamento landing/presentazione → `WF-ASSET-VETRINA` coordina con 06 PLATFORM.

**Decomposizione.** `AG-A6-COORD` orchestra task in parallelo (`star`): i task sono indipendenti
e a bassa frequenza (un case study per cliente, non una pipeline quotidiana):
- `T-proof-collector`: raccoglie metriche reali (reply rate del cliente, tempo setup, ROI misurato),
  trascrizione o schermata della testimonianza del cliente → mai inventare o parafrasare;
- `T-case-writer`: struttura APSOC (il caso APRE con il problema del cliente, poi soluzione, poi
  risultati con numeri reali) → passato dal Gate Brand corporate (Mandato Empire: zero claim non
  documentati) → pubblicazione su landing e wiki;
- `T-upsell-mapper`: SOLO attivo dopo Gate Delivery + segnale positivo; mai durante 90gg supporto;
  proposta upsell via Max (umana), non automatica.

**Regola proof.** `T-proof-collector` raccoglie SOLO a fine supporto 90gg (il cliente ha dati reali
solo dopo aver usato il sistema per 90gg). Case study scritto SOLO con metriche documentate dal
cliente. Se il cliente non fornisce metriche → case study qualitativo (descrittivo) senza numeri,
non fabbricati. L'upsell-mapper segnala opportunità, non decide: la proposta va via Max.

**Failure.**
- Cliente non risponde per testimonianza → un secondo follow-up dopo 7gg, poi si chiude senza
  case study; nessuna pressione (rovina il rapporto e viola il brand gate).
- Case study bocciato dal Brand-Voice Sentinel → rework sulla sezione non conforme; mai bypass.
- Landing/presentazione non aggiornata (build rossa da 06 PLATFORM) → alert a `HC-AG-PL-01`.

## KPI

| KPI | Definizione |
|---|---|
| Case study per cliente chiuso | 1 per delivery (con metriche o qualitativo documentato) |
| Call da inbound | call prenotate da chi ha visto landing/case study, non da outreach |
| Testimonianze raccolte | % clienti che forniscono testimonianza a fine 90gg |

## Connessioni

- [`../../Workflow/WF-CASE-STUDY/`](../../Workflow/WF-CASE-STUDY/) · [`WF-ASSET-VETRINA/`](../../Workflow/WF-ASSET-VETRINA/)
- [`../../Funzioni/T-proof-collector/`](../../Funzioni/T-proof-collector/) · [`T-case-writer/`](../../Funzioni/T-case-writer/) · [`T-upsell-mapper/`](../../Funzioni/T-upsell-mapper/)
- [`../A4-Delivery/`](../A4-Delivery/) (fornitore: delivery chiusa) · [`../A2-Acquisizione/`](../A2-Acquisizione/) (cliente: munizioni outreach)
- [`../../BACKBONE.md`](../../BACKBONE.md) · [`../../ECOSISTEMA.md`](../../ECOSISTEMA.md)
