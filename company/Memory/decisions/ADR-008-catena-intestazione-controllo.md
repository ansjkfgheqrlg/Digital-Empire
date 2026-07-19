# ADR-008 — Catena di intestazione e controllo (ogni artefatto è intestato, collegato, controllato)

- **Data:** 2026-07-19
- **Stato:** ATTIVA
- **Autorità:** direttiva integrale di Max (2026-07-19): "ogni cosa che viene creata, ogni singolo
  dettaglio, deve essere intestato, collegato, controllato da un reparto e da un controllore,
  e tutto governato dal Mandato. Siamo un'azienda."

## Decisione

**Nessun artefatto orfano.** Ogni artefatto dell'Impero — ecosistema, reparto, workflow, skill,
agente, prodotto, app, pagina social, canale, dossier, runtime — nasce e vive con QUATTRO legami
obbligatori:

| Legame | Chi è | Domanda a cui risponde |
|---|---|---|
| **1. PROPRIETARIO** | un reparto o organo (uno solo) | "Di chi è? Chi lo fa vivere?" |
| **2. CONTROLLORE** | il QA/gate competente (indipendente dove esiste) | "Chi lo verifica? Chi può bloccarlo?" |
| **3. ORIGINE** | ARCHITETTURA (struttura) → FORGE (costruzione) | "Chi l'ha progettato e costruito?" |
| **4. GOVERNO** | articolo del Mandato che lo vincola | "Sotto quale legge opera?" |

## Regole operative (bloccanti)

1. **Anagrafe unica:** ogni artefatto ha una riga in `company/REGISTRO-IMPRESA.md` (artefatti
   maggiori) e/o `company/skills-map.yaml` (skill/workflow/tool). **Creare senza registrare =
   artefatto abusivo**: la prima Sentinella/QA che lo trova apre violazione.
2. **FORGE = ufficio anagrafe.** Ogni ciclo FORGE (WF-FORGE-*) si chiude SOLO con la riga di
   registro scritta: intestazione = ultimo passo della costruzione, non un dopo.
3. **MAXIMILIAN 5-bis verifica l'intestazione.** Il review-gate chiede anche: "proprietario?
   controllore? registro aggiornato?" — se manca, NON APPROVA.
4. **Catena di controllo a 3 livelli:**
   - Livello 1 — QA del reparto proprietario (gate interno, blocca).
   - Livello 2 — controllore indipendente dove esiste (A10-QA-Cliente per AGENCY, CF-R6 per
     CONTENT-FACTORY, METHOD-GUARD per FORGE, Ispettorato dossier 15 per MAX stesso).
   - Livello 3 — MAXIMILIAN (5-bis) + Mandato (liceità) + Sentinelle (vigilanza continua).
5. **Il Mandato governa tutto.** Ogni riga di registro cita l'articolo del Mandato pertinente
   (Art.2 prove-non-promesse, Art.4.3 dry-run, Art.7.2 PII, ...). Un artefatto che non riesce a
   citare un articolo → domanda obbligatoria: "perché esiste?"
6. **Manutentore del registro:** Chief-Forge (Board). Cadenza revisione: ad ogni CP di chiusura
   ecosistema + settimanale nel RETRO.

## Conseguenze
- `company/REGISTRO-IMPRESA.md` creato (anagrafe madre) — fonte di verità delle intestazioni.
- `company/skills-map.yaml` torna VIVA: aggiornata ad ogni nuova skill/workflow (era ferma all'11/06).
- I gate esistenti (struct-gate, 5-bis) acquisiscono il check di intestazione.
- Gli artefatti PRE-esistenti vengono intestati retroattivamente (fatto in questo ADR-ciclo).

## Connessioni
- [[REGISTRO-IMPRESA]] · `company/REGISTRO-IMPRESA.md`
- [[ADR-003]] (wrap non riscrittura) · [[ADR-006]] (ciclo 9 passi) · [[ADR-007]] (scala V2)
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · [[15|Ispettorato]] · Sentinelle `company/Sentinels/`
