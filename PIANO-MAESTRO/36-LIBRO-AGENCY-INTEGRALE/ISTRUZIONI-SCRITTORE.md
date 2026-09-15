# ISTRUZIONI PER LO SCRITTORE DI UN CAPITOLO — Il Libro dell'Agency, Edizione Integrale

Lavori in italiano. Scrivi UN capitolo (o una parte di capitolo) del libro. Il libro precedente
è stato bocciato dal proprietario con queste parole: *"veramente schifoso a livello di contenuti
[...] deve esserci tutta la formazione acquisita, tutta la conoscenza, tutto su ogni argomento"*.
Non riassumere mai. Espandi sempre.

BASE: `C:\Users\Utente\Desktop\qui tutto\Digital Empire\PIANO-MAESTRO\36-LIBRO-AGENCY-INTEGRALE\`

## 1. Cosa ricevi

`capitoli-input\<FASCICOLO>.json` — contiene:
- `titolo`, `libro_titolo`, `parte_n`/`parti_totali`
- `atomi`: la lista COMPLETA degli atomi di conoscenza del capitolo, ognuno con `uid`, `peso`,
  `contenuto`, `ancora` (citazione letterale della fonte, se c'è), `fonte`, `relazioni`,
  `detto_anche_da` (altre fonti che dicono la stessa cosa)
- `fonti_integrali`: per ogni run, i file di testo INTEGRALE da cui gli atomi provengono.
  **Aprili e leggili** (almeno le parti attorno agli atomi): l'atomo è un segnalibro, il
  contenuto vero sta lì. Chi scrive solo dall'atomo produce il libro bocciato.
- `marcatori_richiesti`: gli uid che DEVONO comparire nel testo.

## 2. Cosa scrivi

`capitoli\<FASCICOLO>.md` — Markdown puro (titoli `###`/`####`, paragrafi, elenchi, tabelle,
citazioni `>`). Niente frontmatter. Niente titolo `#` di primo livello (lo mette il costruttore).

**Organizzazione per argomento, non per fonte.** Il lettore vuole imparare *il tema del
capitolo*, con dentro tutto ciò che le fonti dicono — in conflitto dove sono in conflitto. Non
scrivere "il video X dice… il video Y dice…": scrivi l'argomento e cita le fonti dentro.

**Per ogni atomo PORTANTE:**
- metti il marcatore `[[uid]]` (doppie parentesi quadre, uid copiato carattere per carattere)
  dentro il blocco di testo dove l'atomo entra;
- attorno a quel marcatore, nello stesso blocco (paragrafo o gruppo di paragrafi senza riga
  vuota in mezzo), **almeno 150 parole**: cosa dice la fonte, perché conta, come si applica in
  un'agenzia, un esempio concreto, i collegamenti con gli altri atomi (`relazioni`);
- **riporta la citazione letterale** del campo `ancora`, tra virgolette: almeno 6 parole
  consecutive identiche all'originale, meglio la frase intera. Se `ancora` è vuoto, cita
  comunque la fonte (`fonte`) per nome.

**Per ogni atomo di SUPPORTO:** entra come citazione o inciso dentro un paragrafo, col
marcatore `[[uid]]`. Non serve la soglia di 150 parole, ma deve dire qualcosa, non solo esistere.

**Gli atomi di CONTESTO non entrano nel corpo:** finiscono in appendice, generata da codice.
Non citarli.

**Chiusura obbligatoria** — l'ultimo blocco del file è esattamente:

```
#### Cosa fa Digital Empire su questo punto

<testo>
```

Qui dici cosa l'Impero ha già costruito o deciso su questo tema: skill in
`C:\Users\Utente\Desktop\qui tutto\Digital Empire\.claude\skills\<nome>\SKILL.md` e in
`C:\Users\Utente\.claude\skills\`, agenti in `.claude\agents\`, decisioni in
`company\Memory\decisions\ADR-*.md`. Apri i file che citi. Se l'Impero non ha ancora niente su
questo punto, **scrivilo**: "Digital Empire non ha ancora un pezzo su questo" è una frase
legittima; inventare non lo è.

## 3. Vietato

- Un target di lunghezza. Non esiste. Esiste la lista degli atomi.
- Marcatori di lavoro non finito: TODO, TBD, "da completare", `[...]`.
- Inglese, salvo termini tecnici e citazioni letterali.
- Frasi di riempimento ("in questo capitolo vedremo…", "come abbiamo visto…").
- Inventare numeri, nomi, risultati non presenti nelle fonti.

## 4. Il gate — non consegni finché non passa

Dopo aver scritto, esegui:

```
cd "C:\Users\Utente\Desktop\qui tutto\Digital Empire"
python PIANO-MAESTRO\scripts\gate_densita_libro.py --elenco <CAPITOLO>
```

(`<CAPITOLO>` è il codice senza la lettera di parte: per `V.9-b` è `V.9`. Se il capitolo ha più
parti, il gate le legge insieme: se stai scrivendo la parte `b` e la `a` non è ancora scritta,
gli atomi mancanti della `a` sono normali — tu guarda SOLO i tuoi `marcatori_richiesti`, i
tuoi MAGRO e le tue SENZA ANCORA.)

Il gate stampa per nome ogni atomo che manca, ogni portante con meno di 150 parole attorno
(MAGRO), ogni ancora non riportata. **Correggi e rilancia** finché i tuoi atomi sono tutti a
posto. Poi consegna.

## 5. Cosa rispondi alla fine

In italiano, in 5 righe: parole scritte, atomi coperti / richiesti, esito del gate sui tuoi
atomi, quali fonti integrali hai aperto davvero, e una cosa che nel materiale ti è sembrata
sbagliata o in conflitto (se c'è).
