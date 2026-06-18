---
Type: CONCEPT
Status: Active
Tags: #skills #brand #creative-strategy #L2-5
Created: 2026-06-18
Last updated: 2026-06-18
---

# SKILLS — L2.5 Brand & Creative Strategy

> Skill proprie del reparto + mapping skill esistenti (da §5.2 dossier 04-MARKETING-V2).
> Fonte di verità per integrazione con 07-FORGE e registro skill della holding.

---

## Skill propria P0 — `brand-strategy-gate`

**Stato:** da forgiare via 07-FORGE (priorità P0 — §6 dossier 04-MARKETING-V2)
**Owner:** BR-QA (applicazione), BRAND-LEAD (autorità)
**Tier:** Sonnet (esecuzione gate deterministico)

### Descrizione
Implementa il gate G5 (Brand Consistency) come skill eseguibile deterministicamente.
Riceve un output (copy, brief visivo, email, ads) + il brand_kit_id e verifica la coerenza
su 5 dimensioni binarie. Produce PASS o FAIL con feedback granulare.

### PRD (requisiti prima della build)
Prima di forgiare questa skill, 07-FORGE esegue:
1. `skill-contradiction-analyzer` contro `empire-brand-gate` (CMO/Board), `market-brand` esistente.
   Rischio: sovrapposizione — la skill IMPLEMENTA la checklist esistente, non la ridefinisce.
2. Architettura: 5 dimensioni di check (voce, proof_points, proibizioni, tono_canale, visual_language),
   schema input/output JSON, output binario PASS/FAIL con feedback granulare.

### Schema check (5 dimensioni binarie)
```
1. voce_coerente_con_kit      → true/false (tono, registro, distanza percepita)
2. ogni_claim_ha_proof        → true/false (ogni affermazione rilevante ha evidenza)
3. proibizioni_rispettate     → true/false (parole/frasi vietate assenti)
4. tono_corretto_per_canale   → true/false (tone_chart per il canale dichiarato)
5. visual_language_coerente   → true/false | n/a (solo per output con elementi visual)
```
Gate: PASS se tutte le dimensioni applicabili = true. FAIL su qualsiasi false.

### Input atteso
```json
{
  "output_id": "...",
  "tipo_output": "copy | brief_visivo | email | ads | brand_kit",
  "brand_kit_id": "DE | cliente-X",
  "testo_o_path": "...",
  "canale": "email | ads | social | n/a"
}
```

### Priorità build
P0 — serve dal giorno 1 per rendere G5 operativo. Senza questa skill, il gate è manuale
e soggetto a interpretazione. Con la skill, è deterministico e documentato.

---

## Skill esistenti — mapping a L2.5

Queste skill esistono nel repo e sono mappate a L2.5 come ausiliarie (§5.2 dossier 04-MARKETING-V2).
Non si duplicano, non si modificano — si referenziano.

### `market-brand`
**Path:** (skill esistente, da verificare in `SKILL & Agenti/`)
**Owner reparto:** L2.5
**Uso:** brand identity base, positioning operativo per DE e clienti. Ausiliaria per BRAND-LEAD
e BR2 quando serve un framework rapido di brand identity senza workflow completo.
**Gerarchia:** ausiliaria — il motore primario è il workflow WF-BRAND-KIT-BUILD con i 6 agenti.

### `market-social`
**Path:** (skill esistente, da verificare in `SKILL & Agenti/`)
**Owner reparto:** L2.5 + 04-MARKETING trasversale
**Uso:** social presence, tono per canali social. Ausiliaria per BR2 (tone_chart social)
e BR3 (brief visual per post social). Non sostituisce il brand_kit — lo integra per il canale social.

### `market-competitors`
**Path:** (skill esistente, da verificare in `SKILL & Agenti/`)
**Owner reparto:** L2.5 + 08-INTELLIGENCE
**Uso:** competitor profiling per BR4. Ausiliaria al dossier competitor del WF-BRAND-AUDIT.
Quando 08-INTELLIGENCE non ha il profilo aggiornato, BR4 può invocare questa skill per una
ricerca rapida prima del dossier completo.

---

## Skill da mappare in futuro (non urgenti)

| Skill candidata | Reparto | Nota |
|---|---|---|
| `brand-voice-evolution` | L2.5 | Codifica il WF-BRAND-EVOLUTION in skill eseguibile (P3, dopo P0 e P1) |
| `icp-language-mapper` | L2.5 + L2.1 | Raccolta sistematica del linguaggio ICP da fonti digitali (P2) |

---

## Anti-contraddizione (regola pre-build §6 dossier)

Prima di forgiare ogni skill nuova → `skill-contradiction-analyzer` contro le skill esistenti.
Rischio concreto per `brand-strategy-gate`: sovrapposizione con:
- `empire-brand-gate` (Board CMO): quella skill è per il gate APSOC + voce a livello Board.
  `brand-strategy-gate` è per il gate brand_kit multi-tenant di L2.5 — scope diverso.
  Risoluzione: le due skill si referenziano a vicenda, non si sovrappongono. `empire-brand-gate`
  presidia il gate LX (holding-wide), `brand-strategy-gate` presidia il gate L2.5 (per brand_kit specifici).
- `market-brand`: ausiliaria esistente. `brand-strategy-gate` non la sostituisce — è complementare.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md`
- [[br-qa-brand-consistency-verifier]] · `agenti/br-qa-brand-consistency-verifier.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §6 (skill nuove)
- [[07-BACKBONE-RUFLO-SKILLS]] · `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md` (registro skill holding)
