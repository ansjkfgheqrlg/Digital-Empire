# Lancio: Manuale Claude Code

> Primo lancio dell'ecosistema. Scaglione **S1** compilato a mano il 2026-09-10,
> micro-task [`MT-9ADD`](../../../../Memory/tasks/micro/TASK-LANCI-BUILD-W3/).

---

## Lo stato, in una riga

**Il lancio non può partire, e i file lo dimostrano invece di dirlo.**

| Artefatto | Valido contro lo schema | Cosa dice |
|---|---|---|
| `pubblico.json` | ✅ | **0 persone raggiungibili verificate** |
| `certificato.json` | ✅ | **non-consegnabile**, 4 bandiere rosse su 6 |
| `previsione.json` | ✅ | ricavo atteso **0 €** in tutti e tre gli scenari |
| `offerta.PROPOSTA.json` | ❌ manca `firma` | prezzo proposto 67 €, aspetta Max |

Prova:

```bash
python company/Ecosistemi/15-LANCI/02-AUTOMAZIONI-E-SCRIPTS/valida_artefatti.py manuale-claude-code
```

---

## Perché il ricavo è zero, e perché non è pessimismo

La formula è scritta dentro il file, apposta perché chiunque possa rifare il conto a mano:

```
ricavo_lordo = pubblico_raggiungibile × tasso_visita × tasso_acquisto × prezzo
```

Con `pubblico_raggiungibile = 0`, **qualunque tasso si scelga il risultato è zero.** Non è
una previsione prudente: è aritmetica.

E il pubblico è zero perché **nessuno dei tre canali ha una prova**, non perché non ci sia
nessuno:

- **lista Brevo** — nessun accesso al pannello da questa sessione, e la chiave d'API va
  considerata bruciata (B-020). Contatti reali: sconosciuti.
- **canale YouTube** — dichiarato funnel morto e dirottato su un altro progetto il
  **29/07/2026**. È il fatto che ha fatto nascere questo artefatto.
- **Instagram** — nessun conteggio misurato in Memory, credenziale esposta (B-023).

> La regola dello schema è dura e va tenuta: **un numero senza prova vale zero nel totale.**
> Si può dichiarare di non sapere. Non si può contare ciò che non si sa.

**Basta un esporto della lista Brevo perché questo file cambi faccia.** È il gesto più
economico dell'intera settimana.

---

## Le quattro bandiere rosse, e quali fanno davvero male

Il certificato è in **modalità retroattiva**: il Manuale esiste da mesi e non deve
attraversare un flusso di produzione che non ha mai percorso. Serve a dire cosa gli manca.

| | |
|---|---|
| **RF4** contenuto non originale | 🔴 **Il nome proprio "Giovanni" compare 21 volte** nel sorgente, e un servizio personale di un terzo (`giovanni-beggiato--linkedin-post-generator.modal.run`) è presentato come RISULTATO di un esercizio. O il materiale deriva da una fonte di terzi e va attribuito o riscritto, oppure è un residuo di lavorazione e va tolto. **In nessuno dei due casi si vende così.** |
| **RF6** consegna non provata | 🔴 Nessuno ha mai comprato questo file e visto arrivare il file. La consegna è un'ipotesi. Si chiude con `MT-32RU` e `MT-CV7N`. |
| **RF5** link morti | 🟠 Due indirizzi `modal.run` di terzi, **non testati** (nessuna chiamata di rete da questa sessione: `codice: null`, non "funzionante"). Più un collegamento markdown malformato a riga 8689. |
| **RF3** promessa non mantenuta | 🟠 Non c'è ancora niente contro cui misurarla: `ART-CPY` è di S3, e la landing attuale promette *"il framework gratuito"*, non un manuale a pagamento. Si chiude da sé. |

Le due che passano: **RF1** e **RF2**. Il prodotto è denso e pratico — 55.680 parole,
257 titoli, 31 prompt pronti accompagnati da 37 riquadri di risultato. Il problema del
Manuale non è la qualità.

---

## Il prezzo: cinque fonti, mai messe sullo stesso tavolo

`prezzi_precedenti_trovati` fa la riconciliazione che nessuno aveva mai fatto:

| Fonte | Valore | Data |
|---|---|---|
| DEC-EST-001, lancio | 67 € | 21/07/2026 — **finestra scaduta il 31/07** |
| DEC-EST-001, listino | 97 € | 21/07/2026 |
| Catalogo prodotti | *"NON LO SO"* | 07/03/2026 |
| Wiki, pagina prodotto | 297-497 € | 29/04/2026 |
| Piano LANCI v3 | 47 € | 05/09/2026 |

Proposta: **67 € di apertura dal 22 al 29 settembre, poi listino a 97 €.**

**`GATE-OFF-1` fallirà su questo file, ed è giusto.** Il rapporto valore/prezzo è **1,0**
contro una soglia minima di 3, perché l'unico bonus previsto (pack template, 27 €) **non
esiste come file** e quindi vale zero. È il vincolo che impedisce di raggiungere il rapporto
inventando i bonus.

---

## Cosa serve da una persona

1. **Max: la firma sul prezzo.** Lo schema mette `firma` fra i campi obbligatori e **nessun
   agente ha permesso di scrittura su quell'oggetto** (INV-10). Un `offerta.json` prodotto da
   una sessione sarebbe un prezzo che nessuno ha approvato con l'aspetto di uno approvato.
   L'impronta a cui la firma si lega è in `offerta.PROPOSTA.sha256`: se la proposta viene
   rigenerata, l'impronta cambia e la firma decade.
2. **Chiunque: l'origine del materiale con dentro il nome di un terzo** (RF4).
3. **Gael: la catena dell'incasso**, `MT-32RU` e `MT-CV7N`.

---

## E la cosa che S1 doveva scoprire, l'ha scoperta

Il piano dice, testualmente:

> *"Se un lancio non supera S1, non serve nessun software: significa che il problema
> dell'azienda non è l'automazione."*

Questo lancio non supera S1. Non per il prodotto, che è buono. Per tre motivi che nessun
codice risolve: **non sappiamo a chi parlare, non abbiamo mai provato a consegnare, e c'è il
nome di un altro dentro la merce.**

Cinque ore di compilazione a mano lo hanno reso leggibile. Sono costate meno di un lancio
aperto e andato a vuoto.
