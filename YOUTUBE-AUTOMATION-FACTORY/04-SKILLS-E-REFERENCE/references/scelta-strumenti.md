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
