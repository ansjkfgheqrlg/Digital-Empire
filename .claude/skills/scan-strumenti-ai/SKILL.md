---
name: scan-strumenti-ai
description: "Interroga i cataloghi di strumenti AI e dice se esiste qualcosa di meglio di cio' che Digital Empire usa gia' per fare video, voce, copertine e trascrizioni. Usala quando uno strumento in produzione fallisce ripetutamente, prima di rinnovare un abbonamento, quando si apre un gate di categoria dello studio AI TUBE PRO, quando qualcuno propone di comprare un tool nuovo, o ogni volta che serve rispondere alla domanda che nessuno pone mai — cio' che usiamo e' ancora il migliore disponibile."
---

# SCAN STRUMENTI AI

> **Il problema che questa skill esiste per risolvere.**
> La fabbrica YouTube gira su Fliki e su Arena. **Nessun processo, in tutta Digital Empire,
> si e' mai chiesto se siano ancora i migliori.** Non e' una svista: e' che non esiste il
> comando che pone la domanda. Nel frattempo la copertina automatica su Arena e' fallita
> **tre volte** senza che nessuno cercasse un'alternativa — si e' riparato lo strumento
> rotto, mai chiesto se fosse lo strumento giusto.
>
> Riparare a oltranza cio' che si ha e' la forma piu' cara di fedelta'.

## 1. COSA FA

Interroga i cataloghi pubblici di strumenti AI per le **sole categorie che ci riguardano**,
e scrive un rapporto datato con cio' che ha trovato e cosa farebbe meglio di cio' che
usiamo oggi.

**Le categorie sono quattro, e non si allargano** — un catalogo di 12.000 strumenti letto
per intero e' rumore, non ricerca:

| Categoria | Cosa usiamo oggi | Dove fa male |
|---|---|---|
| generazione video da testo | Fliki | il vincolo piu' grosso della fabbrica |
| voce sintetica | Fliki (voci incluse) | pronuncia, accenti, naturalezza |
| copertine e miniature | Arena | tre fallimenti registrati |
| trascrizione | faster-whisper locale | funziona, si controlla solo se c'e' di meglio |

**I cataloghi da interrogare:** futurepedia, futuretools, aifinder e simili. Non e' un
elenco chiuso: se ne compare uno nuovo si aggiunge, e si scrive nel rapporto quali sono
stati letti quel giorno.

## 2. COME SI USA

```
/scan-strumenti-ai                      # tutte e quattro le categorie
/scan-strumenti-ai copertine            # una sola categoria
```

Il rapporto viene scritto in
`company/Memory/studi/STRUMENTI-AI-<AAAAMMGG>.md`, con la data nel nome. **I rapporti
vecchi non si sovrascrivono**: il valore di questa skill nasce dal confronto fra due date —
uno strumento che compare, sale e poi sparisce dice piu' di una fotografia singola.

## 3. COSA DEVE CONTENERE OGNI RIGA DEL RAPPORTO

Cinque colonne, e la quinta e' quella che rende il rapporto utile invece che una lista:

| Colonna | Cosa ci va |
|---|---|
| nome | lo strumento |
| categoria | una delle quattro sopra |
| verificato / popolare | come lo marca il catalogo, non come sembra a noi |
| cosa fa | una riga, dalle parole del catalogo |
| **cosa farebbe meglio di cio' che usiamo** | **il confronto con Fliki o Arena. Se non c'e', si scrive "niente" e si passa oltre** |

Uno strumento che non batte cio' che abbiamo su nulla **non entra nel rapporto**. Una lista
di alternative equivalenti e' lavoro sprecato per chi la legge.

## 4. IL TETTO DI TEMPO — dichiarato, non a piacere

Massimo **20 minuti** per esecuzione completa. Il tetto non e' pigrizia: e' cio' che rende
la sorveglianza ripetibile invece di un progetto che si fa una volta e poi mai piu'. Se il
tempo finisce, si scrive il rapporto **parziale** dichiarando quali categorie non sono state
guardate — mai un rapporto che sembra completo e non lo e'.

## 5. QUANDO LA FONTE NON RISPONDE

- **Un catalogo offline** — si scrive il rapporto con gli altri, e si nomina quello che non
  ha risposto. Non si conclude "nessuna novita'": si conclude "due cataloghi su tre letti".
- **Tutti i cataloghi offline** — nessun rapporto vuoto. Si scrive un file che dice solo la
  data e che la scansione **non e' avvenuta**, cosi' la prossima esecuzione sa che quel
  giorno non e' coperto.
- **Un catalogo che cambia struttura** — si registra cosa non si e' trovato dove ci si
  aspettava, invece di dedurre che il contenuto non esista piu'.

## 6. COSA QUESTA SKILL NON FA

**Non compra e non cambia niente.** Produce un rapporto. Sostituire uno strumento in
produzione tocca il motore e passa dal gate di categoria
([ADR-029](../../../company/Memory/decisions/ADR-029-doppio-binario-studio-fabbrica.md)).

**Non prova gli strumenti.** Riferisce cio' che il catalogo dichiara, con la fonte. Un
provino vero e' un lavoro a parte, che questo rapporto puo' motivare ma non sostituisce.

**Non tocca credenziali.** Nessuna chiave, nessun account, nessun abbonamento aperto
(B-020/B-021/B-023).

## 7. QUANDO ESEGUIRLA

- Quando uno strumento in produzione fallisce **due volte sulla stessa cosa** — la terza
  volta e' gia' tardi, come per le copertine.
- Prima di rinnovare un abbonamento, coi costi davanti.
- All'apertura di un gate di categoria dello studio AI TUBE PRO.
- Quando qualcuno propone di comprare qualcosa, per vedere il campo intero e non solo la
  proposta.

## 8. LEGAMI

- `03-AGENTI-E-RUOLI/supporto/self-improver.md` — aveva questo compito scritto nel playbook
  come «sorveglianza periodica», e non e' mai stato eseguito: un'istruzione a un
  agente-lettore non e' un comando che gira.
- `04-SKILLS-E-REFERENCE/references/scelta-strumenti.md` — il criterio con cui si sceglie
  (licenza compresa). Questa skill trova i candidati, quel documento li giudica.
- `.claude/skills/fliki-capability-audit/SKILL.md` — la domanda gemella rivolta all'interno
  invece che al mercato: non "esiste di meglio", ma "cio' che gia' paghiamo, lo usiamo tutto".
- `company/Memory/studi/aitubepro/regole/A4-metodo-ai-tube/RIPASSO_COSTRUTTIVO.py` — regola
  `A4-RC-05`.
