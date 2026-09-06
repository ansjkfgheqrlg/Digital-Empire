# Scelta degli strumenti — criterio e sorveglianza

> Regola `A4-L00-01`, imparata da **AI TUBE PRO / Metodo AI Tube / L00** (Pietro Gangemi),
> minuto 04:48, verificata a schermo in `frame-0141.png`.
> Prima di questa scheda la fabbrica **non aveva nessun criterio scritto** per scegliere uno
> strumento: Fliki e Arena erano stati scelti una volta e mai più rimessi in discussione.

---

## Il criterio, in una riga

**Uno strumento entra in produzione solo se ha uno storico dimostrabile e fa ciò che dichiara.
La novità non è un merito.**

Il corso lo dice così: si cercano i «verificati» e i «popolari», perché *«vuol dire che hanno
già uno storico e che fanno esattamente quello che dicono di fare»*. Un catalogo di strumenti
AI aggiunge decine di voci al giorno — 26 in un giorno solo, misurato dal relatore a schermo —
e la quasi totalità non arriva a sei mesi.

## Le quattro domande, prima di adottare qualsiasi cosa

| # | Domanda | Se la risposta manca |
|---|---|---|
| 1 | **Da quanto esiste, e chi lo usa in produzione?** | non entra: nessuno storico, nessuna prova |
| 2 | **Cosa succede alla fabbrica il giorno che sparisce o raddoppia il prezzo?** | non entra finché non c'è un piano B nominato |
| 3 | **Quanto costa per video, davvero?** | non entra: un costo non misurato è un costo che scoprirai a fine mese |
| 4 | **Si comanda da riga di comando, o solo da browser?** | entra con riserva: quello che si comanda solo a click si rompe quando l'interfaccia cambia |
| 5 | **Con che titolo lo stiamo usando?** *(A4-L13-01 · 2026-09-06)* | non entra: uno strumento usato senza un titolo valido è un rischio legale travestito da risparmio |

## Gli strumenti in uso oggi, e perché

| Strumento | A cosa serve | Perché è dentro | Punto debole noto |
|---|---|---|---|
| **Fliki** | generazione del video (voce + immagini) | ha un'interfaccia programmabile vera, con stato interrogabile; costo per video misurabile | i lavori restano in coda anche 13 minuti senza che nulla lo spieghi; la rete verso di loro è caduta il 2026-09-04 e il controllo è morto — il lavoro si riaggancia con `fliki_poll_only.py`, non si rigenera |
| **Arena** (copertine) | generazione della miniatura | era l'unico modo automatico per adattare una copertina esistente | **fragile**: si comanda solo a click, e il 2026-09-04 ha fallito 3 tentativi di fila. Oggi la copertina la fa Max a mano — decisione sua, e la fabbrica è stata cambiata perché non ci riprovi da sola |
| **YouTube Studio** (via browser) | caricamento | non esiste alternativa: il caricamento passa di lì | l'interfaccia cambia sotto i piedi. Il 2026-09-04 è comparso uno step «Monetization» che ha bloccato due caricamenti |

**Nota che vale più della tabella:** due strumenti su tre si comandano solo a click, ed è
esattamente da lì che è arrivato ogni guasto della giornata del 2026-09-04. La domanda 4 non
è pignoleria: è il riassunto di quella giornata.

## La sorveglianza — regola `A4-L00-02`

**Una volta a settimana, 15-20 minuti, con il cronometro.** Mai «finché uno vuole».

Il corso avverte del **loop infinito**: questi cataloghi inducono a voler conoscere tutto, e
conoscere tutto non è mai stato l'obiettivo. Il consiglio originale è quotidiano, ma è tarato
su chi sta imparando; per una fabbrica che produce, la cadenza settimanale col tetto è
l'adattamento — dichiarato, non copiato.

**Dove si guarda:** futurepedia.io · futuretools.io · aifinder.info — più i canali dove le
novità arrivano prima dei cataloghi: server Discord, gruppi Telegram e Facebook di settore.

**Cosa si cerca** — non «le novità», ma tre cose precise:
1. un sostituto per uno strumento che ci ha dato problemi (oggi: le copertine);
2. un modo di fare a meno di un passaggio manuale;
3. una nicchia nuova (vedi `A4-L00-03`: i cataloghi si interrogano anche per argomento).

**Cosa NON si fa:** adottare qualcosa il giorno che lo si scopre. Fra la scoperta e la
produzione ci stanno le quattro domande qui sopra.


---

## Il criterio messo alla prova: i sintetizzatori vocali (A4-L03-04 · 2026-09-04)

Il primo caso concreto in cui questo criterio è servito davvero. Cercando **text to speech** nei
cataloghi: **52 strumenti** su Futurepedia, una categoria intera su FutureTools, e su Google i
nomi grossi che nei cataloghi non compaiono nemmeno (Amazon Polly, Google Cloud TTS, Speechify).

Davanti a decine di strumenti che fanno la stessa cosa, l'ordine di scelta è questo:

1. **Realismo della voce**, ascoltato sullo stesso paragrafo per tutti i candidati. La differenza
   fra una voce gratuita e una buona si sente in tre secondi, e non si recupera dopo.
2. **Controllo fine**: pause su una parola scelta, velocità di lettura, **dizionario di
   pronuncia**. Uno strumento senza queste tre leve costringe a rifare l'audio a mano ogni volta
   che sbaglia un accento.
3. **Lingua vera, non tradotta**: voci native italiane, non una voce inglese che legge italiano.
4. **Costo per ora di parlato**, non il prezzo dell'abbonamento: cinque ore a 24 dollari sono un
   numero confrontabile, «piano Pro» non lo è.
5. **Novità: mai un criterio.** Vale qui la regola `A4-L00-01` — verificati e popolari, non
   l'ultimo uscito. Lo dice anche l'autore del corso davanti al suo strumento preferito: «magari
   questo diventerà il più importante al mondo, come potrebbe scomparire dall'oggi al domani».

Perché non abbiamo cambiato strumento: usiamo **Fliki**, che copre voce e montaggio in un solo
passaggio e sta già dentro la catena via API. Un sintetizzatore migliore sulla singola voce ci
costringerebbe a rimettere insieme audio e video a mano — un guadagno sul pezzo, una perdita
sulla catena.

---

## La quinta domanda: il vaglio della licenza (A4-L13-01 · 2026-09-06)

**Perché è stata aggiunta.** Le prime quattro domande guardavano storico, piano B, costo e
comandabilità. **Nessuna chiedeva che titolo avessimo per usare quello strumento** — un buco che
si vede solo quando qualcuno propone la scorciatoia.

L'ha fatto il corso: A4/L13 insegna ad avere **Final Cut Pro (350 €) «gratis per sempre»**
eseguendo nel Terminale una stringa che **azzera il contatore della prova di 90 giorni**, ripetibile
all'infinito. Non è un *crack* di terzi: è **manomissione del meccanismo di licenza**, e **viola
l'EULA**. L'autore stesso chiude con «**non so quanto durerà questo metodo**» [08:01], dopo aver
ripetuto tre volte che «bisogna premiare gli sviluppatori».

**La regola, in una riga:** *uno strumento entra in produzione solo per la porta d'ingresso — piano
gratuito dichiarato dal fornitore, prova ufficiale entro la sua durata, o licenza pagata.*

Le tre risposte ammesse alla domanda 5:

| titolo | ammesso | nota |
|---|---|---|
| **Licenza pagata** (abbonamento o una tantum) | ✅ | il caso normale in produzione |
| **Piano gratuito o prova ufficiale**, usati come il fornitore li offre | ✅ | ma vale la domanda 2: cosa succede quando scade |
| **Aggiramento del meccanismo di licenza** (reset del contatore, *crack*, chiave condivisa) | ❌ | **mai**, nemmeno per una prova, nemmeno «solo per vedere se serve» |

**Le tre ragioni, in ordine di peso** — e la prima non è quella che ci si aspetta:

1. **È un guasto con la data già fissata.** Uno strumento che sta in piedi su un trucco «che non so
   quanto durerà» fallirà in un giorno che non decidiamo noi, probabilmente **mentre la fabbrica
   sta producendo**. È esattamente il rischio che la domanda 2 esiste per intercettare.
2. **Rischio legale e reputazionale sproporzionato.** 350 € contro l'esposizione di un'azienda che
   pubblica col proprio nome: il conto non torna nemmeno se andasse tutto bene.
3. **Non è nemmeno un risparmio vero.** Il tempo speso a rimettere in piedi il trucco a ogni
   scadenza è lavoro manuale ricorrente — la cosa che questa fabbrica esiste per non fare.

**Nota di metodo:** questa regola non nasce da uno strumento che ci serviva. Non usiamo Final Cut e
non lo useremo mai (la fabbrica non apre editor video). Nasce dall'aver visto **la manovra**, e vale
per qualunque strumento futuro si presenti con la stessa porta.
