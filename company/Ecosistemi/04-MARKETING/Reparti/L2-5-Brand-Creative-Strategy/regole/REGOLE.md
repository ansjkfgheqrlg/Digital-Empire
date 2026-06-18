---
Type: CONCEPT
Status: Active
Tags: #regole #brand #creative-strategy #L2-5 #non-negoziabile
Created: 2026-06-18
Last updated: 2026-06-18
---

# REGOLE — L2.5 Brand & Creative Strategy

> Regole non negoziabili. Non sono suggerimenti né best practice: sono vincoli operativi.
> Chiunque, in qualsiasi momento, può citare queste regole per bloccare un'azione non conforme.

---

## Regola 1 — Solo Max modifica il Mandato Art.2

Nessun agente di L2.5, nessun Conductor, nessun membro del Board può modificare il Mandato
Art.2 (Brand Voice DE) senza approvazione esplicita di Max. Questo vale anche se:
- L'urgenza è alta.
- La modifica sembra "piccola" o "temporanea".
- Il CEO o il CMO la richiedono.

**Azione corretta:** aprire WF-BRAND-EVOLUTION, costruire ADR-bozza, scalare a Max.
**Azione sbagliata:** modificare la voice guide DE "in via provvisoria" o "per un singolo progetto".

---

## Regola 2 — brand_kit esplicito obbligatorio per ogni richiesta copy

Nessuna richiesta copy a L2.1 è valida senza `brand_kit` dichiarato nel contratto. Il campo
`brand_kit` nel contratto di richiesta (§1.2 dossier) non è opzionale. L2.1 blocca ogni
richiesta senza brand_kit — non interpreta, non assume il default DE.

**Default:** il default è il brand_kit DE solo se esplicitamente dichiarato come "DE".
"Non so quale kit usare" non è una risposta — il committente deve specificarlo. Se il kit
non esiste → L2.5 avvia WF-BRAND-KIT-BUILD prima di sbloccare L2.1.

---

## Regola 3 — BR-QA è bloccante su incoerenza brand (gate G5)

Il gate G5 di BR-QA è bloccante. Un output che fallisce G5 non viene consegnato al committente.
Non ci sono eccezioni per urgenza, campagne in corso, o pressione del budget. Se si bypassa
G5, l'incidente va loggato immediatamente in state/README.md con motivazione e owner.
Un bypass senza log è una violazione più grave del bypass stesso.

**Fast-track ammesso:** in caso di urgenza documentata, BRAND-LEAD può autorizzare una verifica
G5 ridotta (solo dimensioni critiche: proof_point e proibizioni) — non un bypass completo.

---

## Regola 4 — Il reparto non scrive copy di conversione

L2.5 produce: voice guide, positioning statement, brief visivi, tone chart, dossier competitor,
ADR-bozze. Non scrive: headline finali, body copy, email sequences, sales page, VSL.
Quello è il mandato esclusivo di L2.1.

Se un agente di L2.5 si trova a "migliorare" o "correggere" un copy — anche con le migliori
intenzioni — sta violando il confine architettonico. Il confine esiste per garantire che il
gate G5 resti credibile (chi scrive non può verificare il proprio output in modo affidabile).

---

## Regola 5 — Nessun dato senza fonte

Ogni dati, metrica, affermazione di mercato prodotta da L2.5 deve avere una fonte dichiarata.
BR4 non può scrivere "i competitor si stanno spostando su X" senza citare da dove viene
quella informazione (sito, post LinkedIn, data, screenshot se necessario).

**Perché:** il reparto brand alimenta le decisioni strategiche di tutta la holding. Un dato
sbagliato nel dossier competitor di BR4 produce un posizionamento sbagliato in BR1, una
voice guide sbagliata in BR2, e copy non efficace in L2.1. L'inquinamento dell'input è
più pericoloso dell'errore di esecuzione.

---

## Regola 6 — I brand_kit clienti non sostituiscono il Mandato nei vincoli fondamentali

I clienti hanno voce propria — rispettata. Ma i vincoli fondamentali del Mandato Art.2 (zero
claim senza proof, zero dependency-language come stile istruito, zero scarcity falsa strutturale)
si applicano anche ai brand_kit clienti. Il cliente può avere un tono diverso da DE; non può
avere un modello di comunicazione che violi l'integrità.

Se un cliente richiede che il suo brand_kit contenga "prometti rendimenti alti" come regola
di voce → L2.5 blocca e negozia. BRAND-LEAD decide se il cliente è compatibile con i principi
operativi della holding.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md`
- [[MANDATO-EMPIRE]] · `company/Mandato/MANDATO-EMPIRE.md` (Art.2 + Art.4 + Art.5.3)
- [[br-qa-brand-consistency-verifier]] · `agenti/br-qa-brand-consistency-verifier.md`
- [[brand-lead]] · `agenti/brand-lead.md`
