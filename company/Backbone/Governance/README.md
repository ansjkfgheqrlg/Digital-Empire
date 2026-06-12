# ⚖️ GOVERNANCE — Gate qualità e coerenza

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 1.3
> **Backbone component.** Il gate unico componibile che blocca deliverable non conformi PRIMA
> della consegna/pubblicazione. Exit 0 = APPROVATO · Exit 1 = BLOCCATO con note correttive.
> I gate non sono bypassabili: nessun flag --skip, nessuna eccezione inline.
> L'unica via: correggere o ottenere deroga Board registrata in `Memory/decisions/`.
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/README.md]]

---

## I 5 Gate di verify-empire (categorie)

### Categoria 1 — Struttura

Verifica che l'albero `company/` sia integro e navigabile:

```
[ ] company/GRUPPO.md esiste e ha ≥ 30 righe
[ ] company/Mandato/MANDATO-EMPIRE.md esiste
[ ] company/Board-CSuite/ ha 7 schede agente + README
[ ] company/Ecosistemi/ ha 10 cartelle, ognuna con ECOSISTEMA.md + BACKBONE.md
[ ] company/Backbone/ ha 6 componenti con README (Bus, Brain, Governance, Identity-HR, Observability, Coordination)
[ ] company/Guilds/ ha 5 guild con README (Prompt, Copy-APSOC, Quality, Cost, Design)
[ ] company/Sentinels/ ha 5 sentinel con README (Cost, Quality, Drift, Security, BrandVoice)
[ ] company/Gerarchia/ ha schema LX→L5 documentato
[ ] company/Memory/ ha INDEX.md + STATO-EMPIRE.md + ≥1 CP + ≥1 ADR
[ ] 0 cartelle vuote senza README
[ ] skills-map.yaml aggiornato (0 skill orfane — gate F3)
[ ] YAML/JSON validi — python lint e json --validate
```

### Categoria 2 — Brand / Mandato Empire

Verifica che ogni output rispetti il Mandato (Articles 1-2-3):

```
[ ] Voce diretta-provocatoria-trasparente — nessun qualificatore molle
[ ] "Prove non promesse" — ogni claim ha una proof (CPB)
[ ] Pricing one-time, zero canoni (Articolo 3.2)
[ ] Posizionamento "agenzia progettata per essere licenziata" rispettato
[ ] Zero dependency-language (Articolo 1.2)
[ ] brand_kit dichiarato in ogni handoff inter-ecosistema (Articolo 6.1)
```
Strumento: checklist + agente Brand-Voice Sentinel (Haiku).

### Categoria 3 — Qualità Copy APSOC

Verifica struttura e score di ogni copy di conversione:

```
[ ] Tutti e 5 i blocchi APSOC presenti (A, P, S, O, C)
[ ] P appare PRIMA di S (violazione = −15 automatico)
[ ] Hook nei primi 2 righi (blocco A efficace)
[ ] Una sola CTA primaria
[ ] Score ≥ 80/100 (≥ 85/100 per sales page e preventivi)
[ ] Lunghezza nei limiti del formato dichiarato
```
Strumento: skill `cro-copy-architect` in modalità audit.

### Categoria 4 — Costi

Verifica conformità al routing 3-tier e al budget:

```
[ ] Dry-run eseguito e documentato prima del run reale (Pattern #3)
[ ] Costo stimato ≤ envelope del reparto
[ ] Tier modello coerente con routing policy (§2.3 dossier 07)
[ ] Nessun Opus su task classificato Tier 0 o Tier 1
```
Strumento: cost-estimator + log routing.

### Categoria 5 — Sicurezza

Verifica che nessun artefatto esponga segreti o PII:

```
[ ] Zero segreti in file tracciati (.env, token, API key, sessioni)
[ ] PII anonimizzata su output destinati all'esterno
[ ] Skill/vendor nuovi verificati prima dell'adozione
[ ] Permessi agenti nei limiti dello scope dichiarato
```
Strumento: `aidefence_scan/is_safe/has_pii` + git-secrets.

---

## Tool del Governance

| Tool | Funzione | Stato |
|---|---|---|
| `scripts/verify-empire.ps1` | gate struttura completa (cat.1 + cat.5) — v1 ATTIVO | ✅ ATTIVO |
| `verify-empire.sh` (bash) | versione bash piena (cat. 1-5) — da costruire F2 | da costruire |
| `empire-verify` skill | wrapper skill del verify script — invocabile da agenti | da forgiare P0 |
| `empire-brand-gate` skill | checklist G2 eseguibile (cat.2) | da forgiare P0 |
| `cro-copy-architect` skill | audit APSOC (cat.3) | ✅ skill installata |
| `contradiction-analyzer` skill | verifica coerenza decisioni vs ADR (cat.1+2) | ✅ skill installata |

---

## Contradiction Gate (aggiuntivo)

`skill-contradiction-analyzer` (già installata) gira su ogni nuova skill/SOP/pagina Mandato:
- Input: documento proposto + lista ADR attivi + Mandato Empire
- Output: `{contradictions: [], bloccanti: [], warnings: []}` + pass/fail
- Zero contraddizioni bloccanti = condizione di merge

---

## Fasi di build

| Build | Cosa | Gate |
|---|---|---|
| B2.8 (F2) | verify.sh categorie 1+5 (struttura+sicurezza, deterministiche) | albero company/ integro + zero segreti |
| B3 (F2-F3) | categorie 2+3 (brand+APSOC, richiedono agente giudice) | empire-brand-gate + cro-copy-architect wired |
| B4 (F4) | categoria 4 (costi, richiede observability) | dashboard costi + envelope monitoring attivi |

Verify verde (tutte e 5 le categorie) = condizione di chiusura della fase F2.

---

## Stato

- `scripts/verify-empire.ps1` v1 — ✅ ATTIVO (gate struttura F1)
- `verify-empire.sh` cat. 1-5 — ⏳ da costruire (F2, task 2.5)
- `empire-verify` skill — ⏳ da forgiare P0
- `empire-brand-gate` skill — ⏳ da forgiare P0
