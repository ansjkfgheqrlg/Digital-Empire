# ✍️ Copy APSOC Guild — Guild

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 4.2
> **Expertise:** framework APSOC, brand voice DE, headline CPB, Barnum/Rainbow, obiezioni, swipe file
> **Serve:** MARKETING (owner), AGENCY (outreach, preventivi), INFO-BUSINESS (copy lancio)
> **Sponsor C-level:** CMO (empire-cmo)
> Collegato a: [[GRUPPO.md]] · [[company/Mandato/MANDATO-EMPIRE.md]]

---

## Identità

| Campo | Valore |
|---|---|
| **Guild Master** | `copy-guild-master` (= A8 Copy Reviewer del team Copywriting MARKETING) |
| **Tipo** | Guild trasversale — expertise su richiesta, non gerarchia verticale |
| **Deliverable principale** | APSOC Playbook + libreria copy validati (namespace AgentDB `marketing/`) |
| **Ingaggio** | Passivo (`memory_search "apsoc"`) o attivo (guild_request via gbus) |

---

## Cosa standardizza

La Copy/APSOC Guild è il custode del framework APSOC — la spina dorsale di ogni copy di conversione in Digital Empire (Mandato Art.2.4).

### 1. Il Framework APSOC completo

| Blocco | Funzione | Regola inviolabile |
|---|---|---|
| **A — Attenzione** | cattura il lettore nel primo rigo | Hook specifico, non generico; dato o paradosso o domanda scomoda |
| **P — Problema** | nomina il dolore del target con precisione | Appare SEMPRE prima di S; un P generico = −15 punti gate |
| **S — Soluzione** | presenta l'offerta come risposta al Problema | Dice cosa fa, non cosa è; lega S a P esplicitamente |
| **O — Obiezioni** | smonta le 2-3 resistenze principali del target | Almeno 2 obiezioni reali; NON inventate — ricavate da dati/call reali |
| **C — CTA** | chiama all'azione con una e una sola azione primaria | Una sola CTA principale; azione specifica e a bassa frizione |

Gate G1: score ≥ 80/100 (copy standard), ≥ 85/100 (sales page, preventivo).
Gate G2 (Brand-Voice Sentinel): checklist binaria — voce ✓ · prove ✓ · APSOC ✓ · pricing ✓ · zero AI-slop ✓.

### 2. Tecniche avanzate mantenute dalla Guild

- **CPB (Claim → Proof → Benefit)**: struttura obbligatoria per ogni claim. Esempio: "300+ email/giorno [C] — il sistema gira 24/7 senza supervisione [P] — tu ti concentri sulle call [B]".
- **Barnum/Rainbow check**: verifica che l'opener non sia "talmente generale da sembrare scritto per chiunque" (anti-Barnum) e che il copy non prometta tutto a tutti (anti-Rainbow).
- **Swipe file de e clienti**: libreria di copy validati (gate superato + reply rate reale se disponibile) — fonte per varianti future.
- **Tone of voice per brand_kit**: la Guild mantiene le regole di adattamento del tono quando il brand_kit non è `DE` (clienti agency, canali YT, libri KDP) — la voce del cliente governa il tono, i gate DE governano la qualità.

### 3. Regole per formato

| Formato | Lunghezza target | Note specifiche |
|---|---|---|
| Cold email | 150-200 parole | Opener non generico, una sola CTA (risposta alla domanda) |
| DM LinkedIn / Instagram | 80-120 parole | Ancora più diretto; P in rigo 2, CTA in rigo finale |
| Carosello IG | slide 1: hook; slide 2-8: valore; slide 9: CTA | Nessun slide senza funzione nell'APSOC |
| Sales page | 600-1200 parole | Score ≥ 85; Obiezioni ≥ 3; Proof reale obbligatoria |
| Preventivo | sezione copy ≤ 300 parole | S personalizzata sul Problema dichiarato dal prospect |
| Script video | intro 30s: A+P; mid: S; outro: CTA | Pacing APSOC adattato al formato video |

---

## Deliverable

- **APSOC Playbook** — guida completa framework, tecniche, gate, esempi — `marketing/apsoc-playbook/`
- **Libreria copy validati** — per formato e vertical, con score gate — namespace AgentDB `marketing/swipe/`
- **Rubrica di valutazione** — griglia score per sezione (usata dal Quality Sentinel e da verify.sh cat.3)
- **Guida tone of voice per brand_kit** — regole di adattamento per ogni brand_kit registrato

---

## Come si richiede supporto alla Guild

```json
{
  "from": "<ecosistema_richiedente>",
  "to": "Copy-APSOC-Guild",
  "tipo": "guild_request",
  "sottotipo": "copy_review | template_request | swipe_request | tone_of_voice_adaptation",
  "brief": "copy email outreach per prospect Vertical X, awareness level: problem-aware",
  "copy_attuale": "...",
  "brand_kit": "DE | <cliente>",
  "icp": "...",
  "obiettivo_copy": "risposta alla cold email | call booking | acquisto",
  "formato_atteso": "copy revisionato + score G1 + note per sezione",
  "deadline": "YYYY-MM-DD"
}
```

---

## KPI

| Metrica | Target |
|---|---|
| Score APSOC medio output dopo intervento Guild | ≥ 85/100 |
| Copy in swipe file (gate superato + reply rate reale) | crescita tracking attivo |
| Reply rate cold email (dove misurabile) | ≥ 5% |
| Template coperti per formato principale | ≥ 6 formati (F3) |
| Tone-of-voice guide per brand_kit cliente | 1 per cliente attivo |

---

## Stato

Struttura creata (F1). Agenti L5 da assegnare in F3 (migrazione asset + registro Identity-HR).
Guild Master disponibile in consultazione manuale (F1-F3): usa skill `cro-copy-architect` per review APSOC immediate.
