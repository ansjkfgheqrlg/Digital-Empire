# Enrichment Report — B4i1qV0LiMw
**Video:** Claude Design È PAZZESCO: Ti Insegno A Usarlo Bene (Giovanni Beggiato)  
**Data enrichment:** 2026-06-09  
**Atomi analizzati:** 16 (A01–A16)

---

## Skill che possono essere arricchite

### 1. `lead-magnets` ← A11 + A12 + A13 (alta priorità)

**Cosa manca oggi:** la skill gestisce la pianificazione del lead magnet (strategia, tipo, distribuzione) ma non contiene:
- La **keyword-matching rule** (A11): la keyword del CTA deve combaciare con il regalo per massimizzare i DM → es. "FUNNEL" per un funnel, "Claude" per una guida Claude. Regola pratica concreta, non presente nella skill.
- Il **workflow integrato** (A12): Claude Code genera sia l'infografica (PDF/PNG) sia il LinkedIn post con CTA nella stessa sessione. La skill attuale separa "pianificare il lead magnet" da "scrivere il copy" — questi due dovrebbero poter essere richiesti nella stessa sessione.
- La **scarcity mechanic** (A13): XX/100 come default su tutti i lead magnet LinkedIn. Non citata.

**Proposta di arricchimento:** aggiungere sezione "Lead Magnet LinkedIn" con le 3 regole sopra come checklist prima del CTA.

---

### 2. `skill-creator` ← A08 + A10 (media priorità)

**Cosa manca oggi:** la skill (presa da anthropics/skills) descrive il loop draft → eval → iterate, ma non menziona:
- Il **self-check pattern** (A10): ogni skill che produce output visuale (PNG, PDF, slide) dovrebbe includere uno step finale dove Claude legge l'output generato e corregge automaticamente errori (es. apostrofi al posto di accenti, overflow di testo, badge mancanti). Questo è diventato una best practice nel video — da aggiungere come "Step opzionale: self-check" nel template di creazione skill.
- Il **featuresheet:cheat-skill come esempio di riferimento** (A09): una skill matura che dimostra self-check + output 1080×1350 + PDF branded in un singolo prompt. Utile da citare come "skill di riferimento" nel materiale skill-creator.

**Proposta:** aggiungere nota "Self-check per output visuali" nella sezione "Cosa includere in una skill" di skill-creator.

---

### 3. `image` ← A09 + A10 (alta priorità)

**Cosa manca oggi:** senza leggere il SKILL.md completo di `image`, sulla base degli atomi:
- Il pattern **featuresheet:cheat-skill** (A09) — genera cheat sheet 1080×1350 PNG+PDF in un singolo prompt — non è documentato come workflow DE. La skill `image` dovrebbe avere questo come workflow standard per cheat sheet/infografiche branded.
- Il **self-check visivo** (A10) — Claude genera il PNG, poi lo rilegge natively, corregge errori (typo, overflow), ri-esporta — non è standard. Dovrebbe essere l'ultimo step di qualsiasi workflow image/cheat-sheet.

**Proposta:** aggiungere workflow "cheat-sheet-branded" in `image` con step self-check finale.

---

### 4. `social` ← A14 + A15 + A16 (media priorità)

**Cosa manca oggi:** se la skill `social` gestisce contenuti social, le seguenti framework mancano quasi certamente:
- **The Thought Leader Funnel** (A14): 5 stadi (Awareness → Authority → Intent → Conversion → Advocacy) — framework per pianificare la presenza LinkedIn come thought leader. Applicabile alla strategia social DE.
- **The Founder Authority Stack** (A15): 7 layers — "Most founders only ever build Layer 2. The ones who have built all seven." — framework per monetizzare la presence LinkedIn come fondatore. Direttamente applicabile al personal brand di Max / Digital Empire.
- **Social Media Manager 25+ skills** (A16): la lista completa di skill da avere in un progetto Claude Code dedicato ai social. Utile come riferimento per costruire il Social Media Manager DE.

**Proposta:** aggiungere sezione "LinkedIn Authority Framework" in `social` con i due framework (Funnel + Stack) + la lista skill reference.

---

### 5. `canvas-design` ← A03 + A04 + A05 + A06 + A07 (bassa priorità)

**Cosa manca oggi:** Claude Design è uno strumento recente (Research Preview). Se `canvas-design` copre la parte design, mancano:
- Il **4-Step Method** completo (Design System → Template → Skills → Lead Magnet) come workflow strutturato
- Le specifiche del Design System Claude Design (sezioni: Slides, Type, Colors, Spacing, Components, Brand)
- Il concetto di **"Start with context" sidebar** come meccanismo di brand consistency

**Proposta:** aggiungere sezione "Claude Design (claude.ai/design)" con il 4-Step Method come workflow DE.

---

## Nessuna modifica proposta su

- **agency-scalping**: contenuto non impattato dal video (design system ≠ agency operations)
- **copy-workflow**: non impattato (il video non affronta APSOC o struttura copy)
- **market-***: non impattati direttamente (il video è su tool workflow, non su marketing strategy)
- **memory-empire**: nessun nuovo pattern architettonico emerso che impatti il sistema stesso
- **exponium-content-factory** (archivio studio): non impattato

---

## Nuovi asset da creare (gap identificati)

| Asset mancante | Tipo | Priorità | Atomi base |
|---|---|---|---|
| `social-media-manager-de` project template | Progetto Claude Code | Alta | A16 |
| `featuresheet:cheat-skill` | Skill DE | Alta | A09, A10 |
| Digital Empire Design System | Progetto Claude Design | Media | A03-A07 |
| LinkedIn Authority Playbook | Framework DE | Media | A14, A15 |

---

## Status
✅ Enrichment-research completato — 4 skill con modifiche proposte, 4 nuovi asset identificati
