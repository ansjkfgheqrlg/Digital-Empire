# Bonus 6 — Automatizzare processi con skills (Claude Speedrun 2)

**Fonte:** panoramica ufficiale + "Cosa hai imparato" (16 bullet) + 28 frame video visionati nativamente. Nessuna trascrizione .md. ULTIMA lezione del run.

---

## Panoramica ufficiale

In questa lezione impari a trasformare i tuoi processi ripetitivi in automazioni usando Claude. Parti dalla documentazione del tuo workflow con un diagram maker gratuito, identifichi quali step puoi delegare all'AI (sviluppo preventivi, client overview document, contesto per AI), e costruisci una skill completa in Obsidian con reference collegate. Vedi l'intero processo applicato al workflow di acquisizione e onboarding clienti: dalla discovery call fino alla delivery, con la creazione pratica di una skill per generare preventivi in PDF automaticamente tramite Claude.

## "Cosa hai imparato" (ufficiale, integrale)

- Perché hai bisogno di processi ripetitivi e standardizzati (SOP) prima di poter automatizzare qualsiasi cosa con l'AI
- Perché la maggior parte della gente non riesce a implementare l'AI: non ha un processo ripetuto che vale la pena automatizzare
- Terminologia business: cos'è una discovery call, una strategy/closing call e l'onboarding di un cliente
- Come è strutturato un processo di acquisizione clienti: dal prospect che dimostra interesse fino alla delivery del servizio
- Usare un diagram maker gratuito per documentare visivamente i tuoi processi con le forme corrette (processo, trigger, terminator, scelta/rombo, database)
- Come identificare dentro un flowchart documentato quali step sono automatizzabili con l'AI e quali no
- Il concetto di domain knowledge: perché devi essere esperto del processo prima di automatizzarlo, altrimenti l'automazione non porta risultati
- Come creare una skill in Obsidian con file skill.md, front matter, input/output definiti e reference collegate
- Dividere un workflow in step separati per l'AI invece di comprimere tutto in un singolo step — l'AI lavora meglio con step singoli e validati uno per uno
- Definire chiaramente quali documenti devono entrare nella skill (trascrizione discovery call, condizioni/prezzi) e cosa deve uscire (preventivo PDF)
- Creare file di reference separati: esempio.md (preventivo reale passato), struttura-preventivo.md (struttura delle pagine), brand-guidelines.json
- Usare la graph view di Obsidian per visualizzare come i documenti della skill sono collegati tra loro
- Come comprimere la cartella della skill, uploadarla su Claude e usarla in un nuovo chat per generare un preventivo
- Usare il parametro "effort max" per far usare a Claude il massimo effort solo sullo step di validazione
- Aggiungere asset (foto, immagini) dentro la cartella della skill per farli inserire automaticamente nel documento finale

## SKILL.md osservato per intero (verbatim, frame t14m00s)

```
---
name: sviluppo-preventivo
description: Serve per sviluppare preventivi per clienti. Usare quando l'utente chiede di fare un preventivo.
---

## Informazioni in entrata
Entreranno le seguenti informazioni con la seguente documentazione. Se queste info non
entrano, chiederle all'utente e rifiutarsi categoricamente di procedere senza le seguenti
documentazioni:
1. Trascrizione della discovery call
2. Ipotetica trascrizione della eventuale discovery call 2
3. Tabella o lista con le condizioni o i prezzi.

## Informazioni in uscita [cosa devi produrre tu, Claude]
Devi creare un preventivo finale in PDF seguendo le indicazioni sotto.

## Steps da seguire

### step 1
Creare un markdown con il copy del preventivo. Il preventivo è diviso nelle seguenti pagine e
puoi trovare un esempio in esempio.md in references.
```

(Testo troncato a step 1 nel frame visionato — gli step successivi non sono stati catturati nella densità di campionamento usata, dichiarato esplicitamente.)

## Timeline demo (sintesi, vedi lesson-analysis.md)

draw.io (flowchart vuoto) → flowchart processo acquisizione completo (trigger→discovery→preventivo AI→pagamento→onboarding→client overview→contesto AI) → Obsidian SKILL.md completo → struttura-preventivo.md → Claude genera preventivo (step 3 validazione con effort max, step 4 PDF finale) → flowchart finale con icone AI su tutti gli step automatizzati.

## Workflow ufficiali citati

1. Documentare un processo con un diagram maker
2. Processo di acquisizione e onboarding clienti
3. Creare una skill in Obsidian per automatizzare lo sviluppo di un preventivo

## Link utili

Claude.ai, Obsidian, Markdown Guide, Wispr Flow (dettatura vocale, già visto in lezione 13 e confermato anche qui via menu bar), Diagrams.net (draw.io), Miro.
