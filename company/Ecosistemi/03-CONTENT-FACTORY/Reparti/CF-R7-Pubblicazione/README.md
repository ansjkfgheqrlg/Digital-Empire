---
Type: REPARTO
Status: Active
Tags: #reparto #content-factory #pubblicazione #distribuzione #CF-R7 #publish #social #youtube
Created: 2026-06-23
Last updated: 2026-06-23
---

# CF-R7 — Pubblicazione & Distribuzione

> **Ecosistema:** 03-CONTENT-FACTORY · **Area:** Post-Produzione · **Livello:** L2 Reparto
> **Dossier:** `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R7`
> **Standard:** CF-grade (ADR-007)
> **[WRAPPA] orchestratori Python ATTIVI: `main_orchestrator.py` + `mentalita_orchestrator.py` — runtime NON modificato (ADR-003)**

---

## Missione

Portare i deliverable con gate verdi sui canali: IG, TikTok, LinkedIn, YouTube, Drive cliente.
CF-R7 è il braccio finale della pipeline CF-DE: riceve asset approvati da CF-R6 e li distribuisce
sulle piattaforme target con schedulazione, adattamento per canale e verifica post-pubblicazione.

CF Exponium non aveva questo reparto: DE lo supera con un team di 8 agenti, 4 workflow CF-grade
e due orchestratori Python già attivi in produzione che vengono wrappati senza modifica.

**REGOLA NON BYPASSABILE:** nessun asset esce sui canali senza (a) gate verdi in `state.json`,
(b) review umana eseguita e documentata, (c) token canale validi. Il gate manuale di review
umana è policy Board — non rimovibile in V2.

---

## Cosa fa il reparto

1. **Gestisce la coda publish** — riceve dalla coda WF-CALENDAR gli slot assegnati; CF-R7-COORD
   orchestra l'ordine di pubblicazione per brand e canale.
2. **Pre-check gate** — CF-R7-QA verifica che ogni deliverable abbia gate verdi in `state.json`,
   che la review umana sia stata eseguita e che i token di accesso ai canali siano validi.
3. **Adatta per canale** — CF-R7-ADAPT calibra caption (lunghezza, hashtag, mention, link)
   e formato (aspect ratio, codec, peso) per ogni piattaforma target dell'ordine.
4. **Pubblica su social** — CF-R7-PUBLISH esegue la pubblicazione su IG/TikTok/LinkedIn
   tramite gli orchestratori Python esistenti (wrap, zero modifica runtime).
5. **Upload YouTube** — CF-R7-YT gestisce l'upload con tutti i metadati (titolo, descrizione,
   thumbnail approvata, tag, playlist, orario schedulato).
6. **Consegna a committenti non-social** — CF-R7-DELIVER impacchetta asset con manifest.json
   e checksum per consegne via Drive/email/transfer.
7. **Verifica post-pubblicazione** — CF-R7-CHECK verifica live che il post sia attivo e
   registra l'URL definitivo in `trace.jsonl`.
8. **Raccoglie metriche** — CF-R7-FEEDBACK raccoglie engagement a 48h e 7gg e li
   trasferisce a `cf/patterns` e a 04-MARKETING Analytics.

## Cosa NON fa

- Non produce contenuto: quello è CF-R3, CF-R4, CF-R5.
- Non esegue gate QA sul contenuto: quello è CF-R6 (indipendente dalla produzione).
- Non bypassa la review umana: è policy Board non negoziabile.
- Non pubblica senza gate verdi in state.json: blocco automatico CF-R7-QA.
- Non modifica gli orchestratori Python: si wrappano senza toccare il runtime (ADR-003).
- Non raccoglie metriche su n < 5 pezzi per brand/formato (insufficiente per pattern).

---

## Roster del reparto (8 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `CF-R7-COORD` | Coordinatore Pubblicazione | `agenti/cf-r7-coord.md` | coordinator | sonnet | Orchestra la coda publish; assegna slot da WF-CALENDAR; riporta a L1-POST |
| `CF-R7-QA` | Verificatore Pre-Publish | `agenti/cf-r7-qa.md` | verifier | sonnet | Check pre-publish: gate verdi, review umana, token validi; BLOCCA se manca uno |
| `CF-R7-ADAPT` | Channel Adapter | `agenti/cf-r7-adapt.md` | worker | haiku | Adatta caption/formato per canale: lunghezza, hashtag, aspect, mention, link |
| `CF-R7-PUBLISH` | Social Publisher | `agenti/cf-r7-publish.md` | worker | wasm/haiku | Pubblica IG/TikTok/LinkedIn via orchestratori Python [WRAPPA] |
| `CF-R7-YT` | YouTube Publisher | `agenti/cf-r7-yt.md` | worker | haiku | Upload YT: titolo, descrizione, thumbnail, tag, playlist, schedule |
| `CF-R7-DELIVER` | Delivery Packager | `agenti/cf-r7-deliver.md` | worker | haiku | Pacchetto + manifest per committenti non-social; naming standard |
| `CF-R7-CHECK` | Post-Publish Verifier | `agenti/cf-r7-check.md` | worker | haiku | Verifica live post pubblicato; URL attivo; log trace.jsonl con URL definitivo |
| `CF-R7-FEEDBACK` | Performance Collector | `agenti/cf-r7-feedback.md` | worker | haiku | Metriche 48h e 7gg → `cf/patterns` + handoff a 04-MARKETING Analytics |

---

## Workflow del reparto (4 workflow CF-grade)

| ID | File | Scopo | Dry-run | Gate |
|---|---|---|---|---|
| **WF-PUBLISH-SOCIAL** | `workflow/WF-PUBLISH-SOCIAL.md` | Pubblicazione IG/TikTok/LinkedIn via orchestratori Python [WRAPPA] | Piano pubblicazione senza toccare canali | Gate verdi + review umana + token validi; BLOCCO se manca uno |
| **WF-PUBLISH-YT** | `workflow/WF-PUBLISH-YT.md` | Upload YouTube con metadati completi e thumbnail A/B | Lista metadati senza upload | Thumbnail selezionata; titolo conforme brand_kit |
| **WF-DELIVERY-PACKAGER** | `workflow/WF-DELIVERY-PACKAGER.md` | Consegna committenti non-social: manifest + checksum + conferma | Manifest senza trasferimento | Manifest.json completo; conferma ricezione committente |
| **WF-FEEDBACK-LOOP** | `workflow/WF-FEEDBACK-LOOP.md` | Metriche 48h+7gg → cf/patterns → handoff MARKETING | — | ≥2 misurazioni; n≥5 pezzi per pattern; fonte tracciabile |

---

## Namespace memoria

| Namespace | Contenuto |
|---|---|
| `cf/publish` | Stato publish per ordine/canale: `{order_id, canale, esito, url, ts}` |
| `cf/delivery` | Stato consegne non-social: `{order_id, tipo, manifest_path, conferma}` |

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| % slot calendario rispettati | CF-R7-COORD | N. publish negli slot previsti / tot slot; [DM] baseline |
| Latenza gate verdi → pubblicazione | CF-R7-QA | Ore tra gate verdi in state.json e publish live; [DM] baseline |
| Post-check green rate | CF-R7-CHECK | % post verificati live con URL attivo al primo controllo; [DM] baseline |
| Metriche 48h per formato/brand | CF-R7-FEEDBACK | Reach/engagement per canale/formato/brand (da piattaforma); [DM] baseline |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | CF-R6 (QA & Gate) | Asset con gate verdi in `state.json`; `orders/<id>/06-delivery/` |
| ← riceve da | CF-R1 (WF-CALENDAR) | Slot publish per brand e canale |
| ← riceve da | CF-R5 (WF-THUMBNAIL) | Thumbnail selezionata per upload YT |
| → consegna a | Canali social (IG/TikTok/LinkedIn/YT) | Post pubblicati via orchestratori Python [WRAPPA] |
| → consegna a | Committenti non-social | Asset + manifest.json via Drive/email/transfer |
| → alimenta | `cf/patterns` | Metriche engagement per brand/formato (CF-R7-FEEDBACK) |
| → handoff | 04-MARKETING Analytics | Dati engagement organico per integrazione con analytics ads |

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- ADR-003: orchestratori Python si wrappano, non si modificano
- Review umana obbligatoria pre-publish social (policy Board)
- Gate verdi in state.json obbligatori — nessuna eccezione

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R7`
- [[CF-R6-QA-Gate]] · fornitore di asset con gate verdi; precedente nella pipeline
- [[CF-R1-Strategia-Brief]] · WF-CALENDAR che alimenta la coda slot publish
- [[04-MARKETING-Analytics]] · destinatario handoff metriche engagement
