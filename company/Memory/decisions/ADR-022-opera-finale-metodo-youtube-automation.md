# ADR-022 — Lo studio di AI TUBE PRO si chiude con un'opera, non con un archivio

- **Data:** 2026-09-05
- **Stato:** ACCETTATA
- **Deciso da:** Max (ordine diretto)
- **Perimetro:** missione `EMP-V6DE` — studio delle 167 lezioni di AI TUBE PRO
- **Tocca:** `company/Memory/plans/PIANO-STUDIO-AITUBEPRO.md` §16, `company/Memory/studi/aitubepro/`

## Contesto

Il piano di studio, fino a oggi, produceva materiale **sparso per lezione**: `appunti.md`,
`report.md`, regole a contratto, e un `REPORT-CATEGORIA.md` a fine categoria. Tutto
verificabile, tutto tracciabile — e tutto illeggibile come corpo unico. Chi arriva domani e
chiede «qual è il metodo YouTube Automation?» deve aprire 167 cartelle.

C'è anche un precedente che pesa: ADR-016 (Ultimo Metro). Digital Empire produce e non
consegna. Uno studio che finisce in cartelle interne sarebbe l'ennesimo pezzo finito e mai
uscito.

## Decisione

Lo studio si chiude con **un'opera ufficiale e pubblica**: `IL METODO YOUTUBE AUTOMATION`.

1. **Tre formati, un solo sorgente** — `.md` (fonte di verità versionata), `.py` (il metodo
   interrogabile dalla macchina: fasi, regole, soglie e checklist come strutture dati, nella
   stessa forma dei file in `studi/aitubepro/regole/`), `.pdf` (il documento da consegnare,
   **standard-oro dossier 28** per §6.19, costruito col motore condiviso
   `PIANO-MAESTRO/scripts/pdf_engine_empire.py`).
1-bis. **Il PDF ha il suo doppione** in `documentazione Empire/Piani/YouTube Automation
   Factory/` (legge §6.17): copia identica, mai spostamento, riallineata ad ogni rigenerazione.
   Quel PDF vive accanto al dossier 28: **la stessa qualità, sempre**, mai un documento di
   servizio impaginato in fretta.
2. **Struttura fissa** — parte finanziaria e modello di business, poi la sintesi stretta di
   tutte le fasi, poi la parte estesa integrale: regole primarie, fasi, tutti i metodi e il
   metodo migliore dichiarato, SEO, ricerca, analisi, l'intera formazione.
3. **Ogni affermazione è tracciabile** alla lezione e al minuto da cui viene. Il documento si
   costruisce dai materiali già prodotti, mai a memoria.
4. **Si assembla a nastro**: ogni categoria chiusa rende scrivibile la sua sezione. L'ultima
   categoria fa scattare l'assemblaggio finale, la parte finanziaria e la sintesi.
5. **La missione non è chiusa finché mancano i tre formati.**

## Conseguenze

**A favore:**
- Lo studio produce un bene consegnabile, non solo una fabbrica migliorata.
- Il `.py` rende il metodo leggibile dagli agenti: la conoscenza entra nella macchina, non
  solo negli occhi di chi legge.
- La struttura «soldi → sintesi → esteso» mette davanti la domanda che conta.

**Contro, dichiarato:**
- Costo reale in fondo alla missione: l'assemblaggio non è gratis. Mitigato dalla costruzione
  a nastro (§16), che sposta il grosso del lavoro dentro le categorie.
- Rischio di duplicazione fra il documento e i `report.md`: il documento **cita e organizza**,
  non riscrive; i report restano la fonte.

**Vincolo ereditato:** il corso è materiale a pagamento di terzi. L'opera è **il nostro metodo
verificato sulla nostra fabbrica**, con le fonti citate — non la ridistribuzione del corso.
Prima della pubblicazione esterna serve la verifica di questo punto, esplicita e scritta.

## Alternative scartate

- **Solo `.md` interno** — è quello che facciamo già, ed è ciò che ADR-016 punisce.
- **Documento scritto in un colpo alla fine** — a 167 lezioni di distanza dalla prima, si
  scrive a memoria. Scartata: si assembla a nastro.
