# coda-legale

**Corsia A** | origine: `armageddon.css:814-860` (Andrei Pascu) **+ la correzione del suo difetto n.1**
canone: `.legal`, `--measure-legal`, `--t-42`, `--t-62`

## Quando
In fondo a qualunque pagina che **vende**. Non e' decorazione: e' cio' che distingue un'attivita' da
un annuncio.

## Quando NO
Mai "no". Una pagina di vendita senza firma e senza disclaimer e' un problema, non uno stile.

## Le tre regole

**1 - Il disclaimer e' PIU' LARGO del corpo.** 88ch contro 64ch. Il commento originale: *"it reads
as the fine print it is, but it is set wide enough to actually be read, the whole point of putting it
here."* Un legale strizzato in una colonna stretta e' un legale scritto per non essere letto.

**2 - Dice cosa NON e', per nome.** Il modello studiato elenca gli argomenti che non tratta (crypto,
finanza personale, fiscalita', recruiting, network marketing, arricchimento veloce). Enumerare
restringe la promessa, e una promessa ristretta e' piu' credibile di una vasta.

**3 - Nessun link col colore di default.** Il suo `mailto:help@...` e' `#0000ee`, **l'unico colore
fuori palette in 5.103 pixel** — in una pagina di due colori si vede come una macchia. Il canone
stila `a[href^="mailto:"]` e `a[href^="tel:"]`, ed e' il **gate 7**.

## La scala di opacita' al lavoro
| | opacita' | |
|---|---|---|
| voci di navigazione | `1` | sono destinazioni |
| link privacy | `--t-62` | e' un obbligo, non un invito |
| disclaimer e firma | `--t-42` | c'e', si legge, non compete |

E' la regola *"piu' un testo e' vicino al denaro, piu' e' opaco"* letta al contrario: qui siamo
lontanissimi.

## Cosa cade se sbagli
- **Disclaimer a 64ch** -> diventa un muro grigio che nessuno attraversa.
- **Nessuna partita IVA** -> in Italia non e' uno stile, e' un obbligo.
- **`mailto` non stilizzato** -> **FAIL al gate 7**, e si vede da lontano.
