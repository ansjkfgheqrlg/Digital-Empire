> Fonte: PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md sez. 2 (CF-R5)

# CF-R5 — PUBBLICAZIONE & DISTRIBUZIONE

> Reparto L2 di 03-CONTENT-FACTORY · Coordinatore: `CF-R5-A01-publish-lead`
> Fonte: dossier 03 §2 (CF-R5), §4e, §6.

---

## Cosa fa

Porta i deliverable con gate verdi sui canali: IG, TikTok, LinkedIn, YouTube, Drive
cliente. Gestisce schedulazione, adattamento per canale, verifica post-pubblicazione e
raccolta performance.

**Questo reparto non esiste in CF Exponium: è il punto in cui DE supera il modello.**
CF Exponium consegna internamente al team lancio; CF-DE pubblica autonomamente
(con review umana obbligatoria nelle fasi iniziali) su N canali per N brand.

Il **motore di pubblicazione ufficiale** è il sistema Python già esistente:
`SKILL & Agenti/Workflow pubblicazione automatica/` — `main_orchestrator.py`,
`mentalita_orchestrator.py`, moduli IG/TikTok/LinkedIn/Drive. Va wrappato (ADR-003),
NON riscritto.

### Org interna

| Livello | Team | Contenuto | Owner |
|---|---|---|---|
| L3 | **WF-PUBLISH** | coda → slot calendario → adattamento per canale → review umana → publish → post-check → log | CF-R5-A03-publisher-social |
| L3 | **WF-DELIVERY** | consegna a committente non-social: pacchetto in Drive/cartella cliente con manifest.json | CF-R5-A04-delivery-packager |
| L3 | **WF-FEEDBACK** | raccolta performance post-pubblicazione (48h, 7gg) → MKT Analytics + cf/patterns | CF-R5-A05-perf-collector |
| L4 | T-utm | UTM builder per ogni link pubblicato (tracciamento attribuibile) | CF-R5-A02-channel-adapter |
| L4 | T-uploader | upload per piattaforma (formati, API, token refresh) | CF-R5-A03-publisher-social |
| L4 | T-postcheck | screenshot/verifica live del post dopo pubblicazione | CF-R5-A05-perf-collector |

### Agenti L5 (schede complete in `../../Agenti/`)

| ID | Ruolo | Tier |
|---|---|---|
| CF-R5-A01-publish-lead | coordina coda pubblicazione e consegne, gestisce slot calendario | sonnet |
| CF-R5-A02-channel-adapter | adatta caption/formato/hashtag per ogni canale (lunghezza IG vs LinkedIn vs TikTok) | haiku |
| CF-R5-A03-publisher-social | esegue publish via orchestratori Python (IG/TikTok/LinkedIn), gestisce token health | wasm/haiku |
| CF-R5-A04-delivery-packager | crea pacchetto consegna (manifest.json + asset ordinati) per committente non-social | haiku |
| CF-R5-A05-perf-collector | raccoglie metriche post-publish → MKT Analytics (AN2) + cf/patterns | haiku |

---

## Come si collega

**Inbound:**
- `CF-R4` o `CF-R3` → handoff con `{asset_dir: orders/<id>/06-delivery/, manifest.json}`
  con 3 gate verdi in state.json e caption presente per ogni canale richiesto.
- `CF-R1/WF-CALENDAR` → slot di pubblicazione per ogni brand.
- `04-MARKETING` → UTM standard, naming convention campagne.

**Outbound:**
- Post live sul canale → log in `state.json.publish[]` + entry `wiki/log.md`.
- Pacchetto in Drive/cartella cliente → notifica al committente.
- Metriche (48h, 7gg) → `04-MARKETING/L2.4` (AN2 Attribution Analyst) e
  `cf/patterns` (per quale brand+formato+hook funzionano).

---

## Come si ATTIVA e RAGIONA

**Pre-condizione assoluta:** handoff da CF-R4/CF-R3 con 3 gate verdi in `state.json`.
Nessuna pubblicazione senza gate. Anche con gate verdi: **review umana obbligatoria**
nella fase iniziale (vincolo Piano Maestro; il Board può rimuoverlo).

**Logica WF-PUBLISH per ogni canale dichiarato nell'ordine:**
1. CF-R5-A02 adatta la caption: lunghezza (IG ≤2200 / LinkedIn ≤3000 / TikTok ≤150),
   hashtag (n. e stile per canale), aspect dell'asset.
2. Dry-run (default): genera il piano di pubblicazione `{cosa, dove, quando, caption}`
   senza toccare i canali — output in `state.json.publish_plan`.
3. Review umana sul piano — approvazione esplicita.
4. T-uploader via orchestratori Python → publish. Token scaduti (IG/FB):
   CF-R5-A03 rileva e interrompe con alert (mai pubblicazione silenziosa su token scaduto).
5. T-postcheck: screenshot/verifica live a +5 minuti → stato nel `state.json`.
6. Log append-only in `trace.jsonl` + entry `wiki/log.md` (pattern wiki-first #12).

**WF-FEEDBACK (a 48h e 7gg):**
- CF-R5-A05 raccoglie reach, impression, engagement rate, click per ogni post.
- Handoff a `04-MARKETING/AN2` per attribuzione campagna.
- `memory_store("cf/patterns", {brand, formato, hook, canale, metriche})` per il
  learning loop della fabbrica.

**Failure handling:** token scaduto → blocco + alert al Conductor per rinnovo (CF-F4
della roadmap include token-health check come step 0); rate limit → posticipo slot nel
calendario (non silenzioso); ban/shadow-ban → alert umano immediato + pausa campagna.

## KPI del reparto

| KPI | Definizione | Direzione |
|---|---|---|
| Puntualità publish | % slot calendario rispettati | ↑ |
| Post-check success rate | % post verificati live senza errori | ↑ |
| Token health | % token attivi e non scaduti per brand/canale | ↑ (target 100%) |
| Lead time delivery | ore da gate verde a consegna committente (WF-DELIVERY) | ↓ |
| Feedback coverage | % ordini con metriche raccolte a 48h e 7gg | ↑ |

## Connessioni

- [[ECOSISTEMA]] — `company/Ecosistemi/03-CONTENT-FACTORY/ECOSISTEMA.md`
- [[BACKBONE]] — `company/Ecosistemi/03-CONTENT-FACTORY/BACKBONE.md`
- `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` §2, §4e, §6
- `SKILL & Agenti/Workflow pubblicazione automatica/` — motore Python (wrappare, NON riscrivere, ADR-003)
- `company/Ecosistemi/04-MARKETING/Reparti/Analytics/` — destinazione metriche WF-FEEDBACK

*Fonte: dossier 03 §2, §4e, §6 · Aggiornato: 2026-06-11*
