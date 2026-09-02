# Bonus 3 — Come collegare Claude a qualsiasi cosa

**Corso:** Claude Speedrun 2 | **Sezione:** Lezioni BONUS (3/6)
**URL:** https://www.andrei-copy.com/cs2online/bonus-3--pjb6s
**Video:** Vimeo `1178256579`, durata 21:55 (1315s)
**Tipo:** **PRATICA** — confermata con 28 frame (15 scan 90s + 13 dense).
**Fonte:** panoramica + "Cosa hai imparato" ufficiali (19 bullet), nessuna trascrizione .md.

---

## Mappa timeline (confermata)

| Tempo | Contenuto | Frame |
|---|---|---|
| 0:00–13:00 | Talking head + whiteboard — spiegazione concettuale API vs MCP, diagramma Claude→MCP→App | `frame-t3m00s...jpg` |
| 15:00 | **Demo**: documentazione ufficiale ClickUp MCP Server (istruzioni setup Claude) | `frame-t15m00s...jpg` |
| 15:30 | **Demo**: Claude Connectors settings — ClickUp "Connected", permessi granulari per 23 tool read-only (Filter Tasks, Find Member by Name, ecc.), toggle "Needs approval" | `frame-t15m30s...jpg` |
| 16:30 | **Demo — permessi live**: prompt reale "Claude wants to use Search Workspace from ClickUp" con opzioni "Always allow / Deny", su richiesta "Creo un task su ClickUp sotto la general B2C... delegalo ad Andrei" | `frame-t16m30s...jpg` |
| 18:00 | **Demo**: dialogo "Create scheduled task" su Cowork (nome, descrizione, prompt, frequenza) | `frame-t18m00s...jpg` |
| 20:00 | **Demo**: Zapier MCP, schermata "Add tools" con app disponibili (Gmail, Google Calendar, Sheets, Docs, Forms, Notion, Drive, Airtable, Zapier Tables, Outlook, HubSpot, Slack, Asana, Salesforce, Jira) | `frame-t20m00s...jpg` |
| 21:00 | **Demo**: prompt email reale "mandare una email ad andrei@apsales.eu con il testo ciao come stai?" — invio diretto da chat Claude | `frame-t21m00s...jpg` |

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Concetto MCP (Model Context Protocol): alternativa più semplice alle API dirette per collegare Claude ad app esterne — l'utente medio non deve gestire integrazioni API complesse. Catena: Claude → MCP → App esegue azioni direttamente dalla chat. | "Cosa hai imparato" + frame t3m00s |
| KA-02 | Rischio esplicito segnalato: dare accesso illimitato a Claude sulle proprie app può causare azioni indesiderate (es. rimborsi accidentali su Stripe) — da qui la necessità del sistema di permessi granulari. | "Cosa hai imparato" |
| KA-03 | Sistema di permessi Claude Connectors osservato dal vivo: per ogni tool del connector (es. 23 read-only tools di ClickUp) si può scegliere "Ask/Always allow/Deny" singolarmente — non è un accesso on/off globale. | frame-t15m30s |
| KA-04 | Prompt esatto osservato per creare task ClickUp da Claude: "Creo un task su ClickUp sotto la general B2C, general B2C, che dice inviare una mail a Marco. Metti come due date domani e delegalo ad Andrei, ovvero me stesso." — Claude chiede conferma esplicita ("Search Workspace from ClickUp — Always allow/Deny") prima di agire. | frame-t16m30s |
| KA-05 | Zapier scelto come "ponte universale" (8.000+ app) rispetto a n8n (più tecnico) e Make (user-friendly ma meno esteso) — criterio: copertura app + presenza di un MCP proprio. | "Cosa hai imparato" |
| KA-06 | Limitazione nota di Gmail come connector diretto: permette solo bozze, non invio reale — aggirata usando Zapier MCP come intermediario per l'invio effettivo. | "Cosa hai imparato" |
| KA-07 | Metodo per aggiungere un connector custom non presente in "Browse Connectors": cercare "[nome app] + MCP" su Google e copiare nome/URL del server manualmente. | "Cosa hai imparato" |
| KA-08 | Possibilità di schedulare task ricorrenti su Cowork collegati a ClickUp (osservato: dialog "Create scheduled task" con nome, descrizione, prompt, frequenza). | frame-t18m00s |
| KA-09 | Zapier MCP permette di aggiungere qualunque tool tra centinaia di app popolari (Gmail, Sheets, Notion, Airtable, Outlook, HubSpot, Slack, Asana, Salesforce, Jira, ecc.) a un singolo server MCP condiviso — un solo setup, accesso a tutto. | frame-t20m00s |

## Connessione con Knowledge Base esistente

- KA-03/KA-04 (permessi granulari per tool + conferma esplicita prima di agire su sistemi esterni) è un pattern di sicurezza rilevante per qualunque automazione DE che collega agenti AI a sistemi reali (es. outreach, CRM) — coerente con la cautela già praticata in `Preventa Outreach Automation` (WhatsApp reale, mai azioni irreversibili senza controllo). Nessuna azione — conferma di principio già applicato, non gap.

## Gate di qualità

| Check | Status |
|---|---|
| NO-FINTO | PASS — 28 frame visionati, prompt trascritti verbatim |
| NO-STUB | PASS — video 21:55 intero mappato |
| P12 traceability | PASS |

**Prossima:** Bonus 4 — "Claude Skills"
