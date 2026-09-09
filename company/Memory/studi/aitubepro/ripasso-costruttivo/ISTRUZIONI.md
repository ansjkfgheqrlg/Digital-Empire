# RIPASSO COSTRUTTIVO — istruzioni comuni (2026-09-10)

## Perche' esisti
Le 23 lezioni gia' chiuse del corso AI TUBE PRO sono state lette con un contratto che ammetteva
solo UNA domanda: «quale documento esistente cambio?». Risultato misurato: 69 regole, 64 su file
`.md`, 5 sul codice, **zero agenti nuovi, zero skill, zero script, zero flussi ridisegnati**.
Max ha corretto il mandato: lo studio deve MIGLIORARE LA FABBRICA in tutto, non produrre regole.

## Il tuo compito
Rileggere il materiale gia' scritto delle lezioni del tuo blocco (appunti, report, rapporti
grezzi — **NON i video, non servono**) e porre le QUATTRO domande che non sono mai state poste:

1. **AGENTE** — questa lezione dimostra che alla fabbrica manca un ruolo che nessun agente copre?
2. **SKILL / COMANDO** — serve un comando invocabile che oggi non esiste?
3. **FLUSSO** — un flusso esistente va RIDISEGNATO (non ritoccato)? quale, e come deve diventare?
4. **CODICE** — serve uno script nuovo, una funzione nuova, o una funzione esistente da rifare?

## Cosa NON devi fare
- **Non riproporre cose che esistono gia'.** L'inventario della fabbrica e' in `INVENTARIO.md`
  accanto a questo file: leggilo PRIMA di proporre. Se proponi un doppione, il lavoro e' sprecato.
- **Non riscrivere le 69 regole gia' fatte.** Sono in `../regole/<categoria>/L*.py`. Leggile per
  sapere cosa e' gia' coperto, mai per copiarle.
- **Non applicare niente.** Tu proponi e provi. Applica il coordinatore, dopo la validazione.
- **Non toccare `02-AUTOMAZIONI-E-SCRIPTS/`** — e' il motore in produzione (ADR-003/ADR-029):
  ogni proposta che lo tocca nasce sul **binario B**, che si applica solo a gate di categoria.

## La legge sulla prova (non negoziabile)
Ogni proposta porta **dove l'hai vista**: file di origine + lezione + minuto o citazione letterale
presa dal materiale. Una proposta senza prova e' un'opinione con l'uniforme, e viene scartata dal
coordinatore senza discussione. Se il materiale non basta a provarla, **dillo** invece di riempire.

## Formato di consegna
Scrivi in **append** nel TUO file (te lo dice il prompt), **ogni 3 lezioni**, mai tutto alla fine:
una sessione che muore con il lavoro solo in testa butta tutto. Per ogni proposta:

```markdown
### P-<tuo blocco>-<progressivo> · <tipo: agente|skill|flusso|script|funzione>
- **Lezione:** <categoria>/<Lnn> — <titolo>
- **Prova:** <file di origine> — «<citazione letterale>» @ <minuto se c'e'>
- **Cosa manca oggi:** <il buco, in una frase, verificato contro l'inventario>
- **Cosa nasce:** <percorso del file che deve esistere> — <cosa fa, in 2-3 righe>
- **Perche' vale:** <cosa smette di rompersi o cosa inizia a produrre>
- **Binario:** A (fuori dal motore) | B (tocca 02-AUTOMAZIONI-E-SCRIPTS)
- **Misura:** <come si vede, sul disco, che e' stato fatto davvero>
```

Chiudi il file con una riga `## FINITO — <n> proposte, lezioni ripassate: <elenco>`.

## Idempotenza
Se il tuo file esiste gia' e contiene proposte, **NON ricominciare da zero**: leggi quali lezioni
hai gia' ripassato e riparti dalla prima non fatta. Il conteggio si legge sul disco, mai a memoria.

## Onesta'
Se in una lezione non c'e' NIENTE di costruttivo da tirare fuori, scrivilo:
`### <Lnn> — nessuna proposta, e perche'`. Una lezione a vuoto dichiarata vale piu' di una
proposta inventata per riempire la casella.
