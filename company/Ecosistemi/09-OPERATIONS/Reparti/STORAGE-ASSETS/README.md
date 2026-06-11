# L2 — STORAGE-ASSETS (Asset Management e Backup)

> **Ecosistema:** 09-OPERATIONS · **Coordinator:** `ops-asset-keeper` · **Direttore:** `ops-director`
> **Workflow L3:** `Workflow/WF-ASSET-MGMT/` · `Workflow/WF-BACKUP/`

## Cosa fa

STORAGE-ASSETS dà ordine fisico alla produzione della holding: ogni asset prodotto
(immagini, video, export, PDF, copertine KDP, render) ha **nome canonico, posizione
nota, hash anti-duplicato e data di scadenza**. E garantisce che ciò che non può
essere riprodotto (wiki, knowledge, registry, Memory) sia **backuppato con restore
testato** — un backup mai restorato non è un backup.

Due workflow:
1. **WF-ASSET-MGMT** — naming convention multi-tenant (`<brand>/<ecosistema>/<commessa>/...`),
   dedup per hash, retention per classe di asset (es. render intermedi 30gg, deliverable
   clienti permanenti), indice in `operations/assets`.
2. **WF-BACKUP** — backup programmati di wiki/knowledge/registry/Memory + **restore
   test mensile** (KPI: 1/mese, verde).

**Vincolo ADR-004 (sync GitHub):** gli asset pesanti NON viaggiano nel monorepo
(video mp4, zip, PNG copertine, session data sono in `.gitignore`; file >100MB → Drive).
STORAGE-ASSETS è il reparto che fa rispettare questa regola e tiene l'indice di dove
ogni asset vive davvero.

## Come si collega

| Con chi | Direzione | Cosa passa |
|---|---|---|
| CONTENT-FACTORY / MULTI-BUSINESS / PLATFORM | inbound | asset prodotti da registrare: `{path, brand_kit, commessa, classe, retention}` |
| RUNTIME | inbound | output dei batch swarm → registrazione automatica a fine merge |
| SCHEDULING | bidirezionale | i job di backup e pulizia retention girano sotto WF-CRON |
| MONITORING-DASHBOARD | outbound | spazio disco, asset orfani, esiti backup/restore |
| INTELLIGENCE | outbound | per knowledge/wiki: STORAGE fa il backup, INTELLIGENCE resta owner del contenuto |
| 10-MEMORY | outbound | esiti backup/restore test → CP; cambi di policy retention → ADR |

## 🧠 Come si ATTIVA e RAGIONA

**Attivazione.** (a) evento "asset prodotto" sul Bus (da RUNTIME o da un ecosistema);
(b) cron di pulizia retention e di backup (via SCHEDULING); (c) richiesta di lookup
("dove sta l'asset X della commessa Y?").

**Ragionamento del coordinator (`ops-asset-keeper`):**
1. Asset in ingresso: calcola hash → esiste già? Sì → NON duplica, registra alias e
   avvisa il produttore (dedup). No → applica naming canonico e classifica
   (deliverable cliente / asset interno / intermedio).
2. Assegna retention dalla classe; intermedi senza classe dichiarata → default 30gg
   con warning (niente vive per sempre per pigrizia).
3. Verifica regola repo: asset binario pesante dentro il monorepo → alert immediato
   (rischio push 100MB+) e indicazione della destinazione corretta (Drive/locale).
4. Pulizia periodica: scaduti → cestino logico 7gg → eliminazione; mai hard-delete
   diretto di un deliverable cliente (quello richiede ok umano).
5. Backup: esegue, verifica integrità archivio, e 1 volta/mese RESTORA in area di
   test confrontando con l'originale. Restore fallito → incidente, escalation
   a ops-director + CTO.

**Principio:** lo storage non è un magazzino, è un indice. Se per trovare un asset
serve "cercare a mano", il reparto ha fallito.

*Fonte: dossier 06 §09 L2 STORAGE & ASSETS · Aggiornato: 2026-06-11*
