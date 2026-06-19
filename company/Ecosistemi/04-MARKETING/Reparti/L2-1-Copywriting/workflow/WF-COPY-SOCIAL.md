---
Type: WORKFLOW
Status: Active
Tags: #workflow #copywriting #social #apsoc #L2-1
Created: 2026-06-18
Last updated: 2026-06-18
---

# WF-COPY-SOCIAL — Sequenza social strategica (5 post)

> **Reparto:** L2.1 Copywriting · **Owner:** COPY-MASTER · **Gate di uscita:** A8 ≥80 + brand gate G2 + pattern library check
> **Dossier:** `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md` §2 (L2.1), §4a (routing)

---

## Scopo

Produrre una **sequenza di 5 post social** coerente e strategica (non 5 post scollegati): hook
d'apertura → sviluppo narrativo → proof → gestione obiezione → CTA. Il formato `social` entra
da MKT-Conductor e viene instradato qui da COPY-MASTER quando il committente (03-CF, 05-MB, o
04-MKT stesso) chiede contenuto di conversione per i canali social.

**Confine:** L2.1 produce il COPY dei post. Il visual/creative viene da 03-CONTENT-FACTORY
(handoff). La pubblicazione e lo scheduling NON sono di L2.1.

---

## Input

```json
{
  "committente": "03-CF | 05-MB | 04-MKT",
  "formato": "social",
  "piattaforma": "instagram | linkedin | tiktok | x | facebook",
  "icp": "riferimento avatar (namespace marketing/avatars/{icp})",
  "awareness_level": "unaware | problem-aware | solution-aware | product-aware | most-aware",
  "obiettivo": "azione misurabile (salvataggio, click bio, commento, DM)",
  "tema": "argomento/angolo della sequenza",
  "brand_kit": "DE | cliente-X (default: Mandato Empire)"
}
```

## Output

```json
{
  "sequenza_id": "SOCIAL-001",
  "post": [
    {"n": 1, "ruolo": "hook", "testo": "...", "score_apsoc_parziale": 0},
    {"n": 2, "ruolo": "sviluppo", "testo": "..."},
    {"n": 3, "ruolo": "proof", "testo": "..."},
    {"n": 4, "ruolo": "obiezione", "testo": "..."},
    {"n": 5, "ruolo": "cta", "testo": "..."}
  ],
  "score_apsoc": 0,
  "brand_gate": "PASS | FAIL",
  "pattern_usati": ["..."],
  "handoff_visual_03cf": "brief inviato sì/no"
}
```

---

## Passi

1. **Validazione contratto** (COPY-MASTER) — `icp` esiste in `marketing/avatars/{icp}`? `awareness_level`
   dichiarato? Se manca avatar → spawna A2/T-AVATAR prima di procedere (regola §1.2 dossier).
2. **Recall pattern** (COPY-MASTER) — `memory_search("marketing/copy/patterns/{icp}")`: quali hook/angoli
   hanno già performato per questo ICP su questa piattaforma? Si parte dai pattern vincenti, non da zero.
3. **Mappa la sequenza** (COPY-MASTER) — assegna i 5 ruoli APSOC distribuiti sui 5 post: post 1 = A
   (attenzione/hook), post 2 = P (problema/sviluppo), post 3 = S+proof (soluzione con prova), post 4 = O
   (obiezione anticipata), post 5 = C (CTA). Adatta il dosaggio all'awareness (unaware → più A/P).
4. **Scrittura** (A3 hook, A4 problema, A5 soluzione, A6 obiezione, A7 CTA) — ogni writer produce il suo
   post nel ruolo assegnato. Regola inviolabile: **P prima di S** (Art.4.2 Mandato).
5. **Gate A8** (A8 Copy Reviewer) — score APSOC sulla sequenza completa ≥80. Sotto soglia → iterazione
   mirata gestita da COPY-QA-LEAD (max 3 cicli, poi escalation umana).
6. **Gate G2 brand** (Brand-Voice Sentinel) — voce diretta/provocatoria/trasparente, ogni claim ha proof
   (CPB), zero AI-slop, brand_kit rispettato. Blocco non derogabile se fail.
7. **Handoff visual** (COPY-MASTER → 03-CF) — brief creativo per i visual dei 5 post (BR3 di L2.5 può
   essere coinvolto per la direction). Il copy è pronto; il visual viaggia in parallelo.
8. **Consolidamento** (AN4 di L2.4, post-pubblicazione) — i pattern che performano entrano in
   `marketing/copy/patterns/{icp}`; quelli che falliscono in antipatterns. Loop §4b.

---

## Gate di uscita

| Gate | Chi | Soglia |
|---|---|---|
| G1 Score APSOC | A8 + COPY-QA-LEAD | ≥80 sulla sequenza · P prima di S (−15 se violata) |
| G2 Brand gate | Brand-Voice Sentinel | checklist Art.2 binaria, tutta verde |
| Pattern check | COPY-MASTER | almeno i pattern ICP pregressi sono stati consultati (no copy "da zero" se esiste storia) |

---

## Esempio

**Input:** committente 04-MKT, piattaforma LinkedIn, ICP "fondatori SaaS B2B", awareness solution-aware,
obiettivo = commento/DM, tema "perché l'agenzia che NON ti rende dipendente vale di più".

**Sequenza prodotta:** post 1 hook provocatorio ("La maggior parte delle agenzie ti vende dipendenza,
non risultati"); post 2 problema (il costo nascosto del canone perpetuo); post 3 soluzione+proof (modello
"progettata per essere licenziata" + caso reale); post 4 obiezione ("ma se mi mollano dopo?" → CPB); post 5
CTA (DM "AUTONOMIA" per il caso studio). Score A8 = 84, G2 PASS.

---

## Connessioni

- [[copy-master]] · `agenti/copy-master.md`
- [[a8-copy-reviewer]] · `agenti/a8-copy-reviewer.md`
- [[copy-qa-lead]] · `agenti/copy-qa-lead.md`
- [[WF-COPY-FULL]] · `workflow/WF-COPY-FULL.md`
- [[Framework_Cold_Outreach_APSOC]] · `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`
- [[MANDATO-EMPIRE]] Art.2 (brand) + Art.4.2 (gate, P prima di S)
