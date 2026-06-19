---
Type: PRINCIPI
Status: Active
Tags: #principi #content-factory #CF-R2 #brand-kit #multi-tenant #non-negoziabile
Created: 2026-06-19
Last updated: 2026-06-19
---

# PRINCIPI — CF-R2 Brand-Kit & Tenant Registry

> Tre principi non negoziabili. Nessun agente del reparto può derogarvi.
> Ogni eccezione richiede ADR approvato dal Board.

---

## Principio 1: Multi-tenant è strutturale, non opzionale

CF-DE non ha un brand. Ha un registry di brand. Ogni contenuto prodotto porta l'identità
di uno e un solo tenant — mai un contenuto ibrido, mai un contenuto senza tenant dichiarato.

**In pratica:**
- Ogni ordine entra con `brand_kit` e `icp` dichiarati. Senza questi due input, l'ordine
  non esiste per CF-DE.
- Il registry CF-R2 è la fonte di verità sull'identità di ogni tenant: quello che c'è nel
  `brand-kit.json` approvato è la specifica vincolante, non le preferenze comunicative
  informali del committente.
- Aggiungere un nuovo tenant richiede WF-BRAND-ONBOARDING completo. Non esistono
  "ordini di prova con brand provvisorio".

**Cosa viola questo principio:** produrre contenuti prima che il brand sia approvato nel
registry; usare colori o toni "simili a quelli del brand" senza caricarli nel brand_kit;
creare ordini con brand_kit puntante a file non nel registry CF-R2.

---

## Principio 2: Nessun contenuto senza brand_kit + icp approvati (pattern 11 del Piano Maestro)

Il brand_kit descrive l'identità visiva e vocale. L'icp descrive a chi si parla e come.
Senza entrambi, il contenuto non sa né chi è né a chi sta parlando. Un contenuto così
prodotto non è un contenuto — è un riempitivo con stile casuale.

**In pratica:**
- CF-D-QA blocca ogni ordine con brand_kit mancante o icp mancante. Il blocco è automatico
  e non bypassabile.
- CF-R2-QA blocca ogni brand_kit con schema incompleto o con esempi voice pari al
  segnaposto non sostituito del template.
- CF-R1-ANALYST non può avviare il brief se `brands/<slug>/brand-kit.json` non ha
  gate PASS nel registry.

**Cosa viola questo principio:** passare il gate manualmente su un brand_kit "quasi pronto"
perché c'è urgenza; produrre contenuti di test con brand_kit stub; compilare icp.json con
dati generici per superare il gate velocemente.

---

## Principio 3: Il drift si previene, non si cura

Intervenire sul brand-drift dopo che decine di output sono stati prodotti fuori specifica
è inefficiente e dannoso. Un brand che ha perso coerenza visiva o vocale sul proprio
canale ha un problema reputazionale, non solo operativo.

**In pratica:**
- CF-R2-DRIFT campiona ogni ciclo di produzione. Non è un'attività straordinaria: è
  infrastruttura obbligatoria come i gate di produzione.
- Un alert drift non è un'eccezione da gestire al volo: avvia WF-BRAND-MAINTENANCE con
  root-cause analysis (il drift è nel brand_kit o nel processo di produzione?).
- Ogni aggiornamento al brand_kit genera un nuovo gate CF-R2-QA e una nuova versione
  con changelog. Non esistono aggiornamenti informali.

**Cosa viola questo principio:** saltare il campionamento drift per un ciclo "perché si
è a corto di tempo"; aggiornare brand_kit.json direttamente senza passare per CF-R2-QA;
ignorare alert drift su brand minori perché hanno poca produzione.

---

## Connessioni

- [[03-ECOSISTEMA-CONTENT-FACTORY-V2]] · `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY-V2.md §CF-R2`
- [[CF-R2-Brand-Kit-Registry]] · `README.md` — questi principi governano il reparto
- [[WF-BRAND-ONBOARDING]] · `workflow/WF-BRAND-ONBOARDING.md` — principio 1 e 2 in azione
