# Bonus 3 — Come collegare Claude a qualsiasi cosa (Claude Speedrun 2)

**Fonte:** panoramica ufficiale + "Cosa hai imparato" (19 bullet) + 28 frame video visionati nativamente. Nessuna trascrizione .md.

---

## Panoramica ufficiale

In questa lezione impari come collegare Claude a qualsiasi applicazione esterna usando gli MCP (connectors). Scopri cosa sono le API, perché gli MCP le hanno sostituite per l'AI, e come usare Zapier come ponte per collegare Claude a oltre 8.000 app. Vedi passo passo come aggiungere un connector (ClickUp) per creare task direttamente da Claude, come collegare Zapier per inviare email senza uscire dalla chat, e come schedulare task ricorrenti con Cowork.

## "Cosa hai imparato" (ufficiale, integrale)

- Cos'è un API e a cosa serve: un modo per collegare applicazioni tra loro (esempio: sito e-commerce → Stripe per pagamenti)
- Perché collegare l'AI direttamente alle API è complesso e non pratico per la maggior parte degli utenti
- Cos'è un MCP (Model Context Protocol): un modo più semplice per collegare Claude ad applicazioni esterne
- Come funziona la catena Claude → MCP → app per far eseguire azioni direttamente dalla chat
- I rischi di dare accesso illimitato a Claude sulle tue app (esempio: rimborsi accidentali su Stripe)
- Come controllare le autorizzazioni di Claude sugli MCP (allow once / allow always)
- Cosa sono i connectors dentro Claude e come trovarli (Settings → Connectors)
- Come aggiungere un connector già presente nella lista "Browse Connectors"
- Come aggiungere un connector custom manualmente cercando il nome + "MCP" su Google e copiando nome e URL del server
- Cos'è ClickUp e come Andrei lo usa per organizzare i task della sua azienda
- Creare un task su ClickUp direttamente da Claude usando il connector MCP
- Differenza tra i tre tool di automazione principali: Zapier, n8n e Make
- Perché Zapier è il più collegato (+8.000 app) e ha un MCP disponibile
- Come usare Zapier come ponte intermedio: Claude → MCP Zapier → qualsiasi app
- Come configurare il server MCP di Zapier per inviare email (outbound email by Zapier)
- Inviare una email direttamente da Claude senza uscire dalla chat
- Limitazione di Gmail come connector: non permette di inviare email, solo bozze
- Come aggirare la limitazione di Gmail usando Zapier come intermediario
- Come schedulare task ricorrenti su Cowork collegati a ClickUp
- Come aggiungere più tool al server MCP di Zapier (Google Forms, Docs, Excel, Zoom, ecc.)

## Timeline demo (sintesi, vedi lesson-analysis.md per dettaglio)

Whiteboard (API vs MCP) → documentazione ufficiale ClickUp MCP → Claude Connectors settings (permessi granulari 23 tool) → creazione task ClickUp da chat (permission prompt live) → scheduling Cowork → Zapier MCP "Add tools" (Gmail, Sheets, Notion, ecc.) → invio email reale da Claude.

## Prompt osservati verbatim

- ClickUp task: "Creo un task su ClickUp sotto la general B2C, general B2C, che dice inviare una mail a Marco. Metti come due date domani e delegalo ad Andrei, ovvero me stesso."
- Email Zapier: "mandare una email ad andrei@apsales.eu con il testo ciao come stai?"

## Workflow ufficiali citati

1. Aggiungere un connector esistente a Claude
2. Aggiungere un connector custom (non presente in Browse Connectors)
3. Creare un task su ClickUp direttamente da Claude
4. Collegare Zapier MCP per inviare email da Claude
5. Schedulare task ricorrenti con Cowork + ClickUp

## Link utili

Claude.ai, ClickUp, ClickUp MCP Server (docs), Zapier, Zapier MCP, n8n, Make, Stripe, Gmail, Figma, Miro, Notion, Asana, Squarespace.
