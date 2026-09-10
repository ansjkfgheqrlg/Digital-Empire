# Report — A6/L05 «Quanti video pubblicare, quanto devono durare e proporzione trend evergreen» (14:22)

- **Durata:** 14:22 · ~2.282 parole · **profondità ORO** (priorità dichiarata da Max, D-1)
- **Letta:** parlato integrale + 13/33 frame unici (talking-head con lavagna, campione motivato)
- **Materiale grezzo:** appunti.md nella stessa cartella · frame scelti: frame-scelti.md

---

## 1. Cosa insegna la lezione

Quattro risposte operative per la programmazione di un canale: (a) frequenza minima di
pubblicazione — 3 video/settimana, scalabile fino alla cadenza dei competitor migliori della
nicchia; (b) durata dei video — nessun numero fisso, dipende dal contenuto necessario per la
nicchia, con un floor consigliato di 4 minuti e una soglia opzionale di 8 minuti per la
monetizzazione mid-roll; (c) proporzione quantità/qualità — trade-off dichiarato, non risolvibile
con un numero; (d) proporzione trend/evergreen — 70/30 in condizioni normali, 85/15 se si vuole
spingere, con i primi 15 video dedicati all'evergreen; più tre traguardi di volume (33, 100, 500
video) come checkpoint di analisi/aspettativa.

## 2. Cosa facciamo oggi nella fabbrica

Verificato nel codice reale (non assunto), YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/:

| Cosa | Oggi | File |
|---|---|---|
| Durata minima video | 480s (8:00), fissa, uguale per ogni nicchia/canale | regolatori.py:270 |
| Durata massima video | 600s (10:00), fissa, uguale per ogni nicchia/canale | regolatori.py:271 |
| Lunghezza minima script | 2220 parole = circa 720s (12:00) a 185 parole/min | apex7_orchestrator.py:163-164 |
| Gate che controlla la durata finale | verifica_qualita() esiste ma è chiamata solo da CLI, mai dalla catena di produzione | regolatori.py:274 e :468 |
| Frequenza minima di pubblicazione | nessun gate, nessuna costante, nessun controllo | - |
| Proporzione trend/evergreen | nessuna logica, non esiste distinzione trend/evergreen nel codice di pianificazione | - |
| Checkpoint di volume (33/100/500) | nessuno, nessun contatore, nessun trigger di revisione a soglie di produzione | - |

## 3. Delta

Sulla durata (il punto per cui questa lezione è stata messa per prima): il delta non è "quale
numero manca", è "la nostra fabbrica ha un tetto universale dove il corso insegna che il tetto
non dovrebbe esistere". La lezione, a voce e a schermo (vedi appunti.md: la sezione "quanto
devono durare" resta senza risposta scritta per tutta la durata del video mentre le altre tre
domande la ricevono), dice esplicitamente che la durata è funzione della nicchia e del contenuto
necessario: un video di notizie flash può durare 1-2 minuti, un "telegiornale" 40. I soli numeri
dati sono un floor (4 minuti, motivato da retention) e una soglia opzionale di monetizzazione (8
minuti, esplicitamente non un obbligo). Nessuno dei due è un "numero ottimale universale" che
possa sostituire sia DURATA_MASSIMA_S=600 sia PAROLE_MINIME_SCRIPT (circa 720s) rendendoli
coerenti fra loro. Vedi §7 per la decisione su D-1.

Sulla frequenza: delta reale e concreto. Il corso dà un numero secco e ripetuto tre volte
("minimo", "assolutamente", "questo è il primo consiglio") — 3 video/settimana, 12-15/mese come
pavimento — e noi non abbiamo nessun controllo che lo verifichi: nessuna costante
FREQUENZA_MINIMA_SETTIMANALE, nessun agente che guardi il calendario editoriale e segnali un
canale sotto soglia. Il gap è più netto di quello sulla durata perché lì il corso stesso rifiuta
un numero fisso; qui invece lo dà e noi non lo usiamo.

Sulla proporzione trend/evergreen: delta reale. 70/30 (o 85/15 in spinta, coi primi 15 video in
evergreen) è un parametro pianificabile che oggi non esiste da nessuna parte nella fabbrica — non
nel piano editoriale, non nel niche-scout, non nell'orchestratore.

Sui checkpoint di volume: delta reale. 33/100/500 sono soglie di analisi dichiarate dal corso
("dopo 33 video abbiamo abbastanza data a disposizione su Google Analytics") e la fabbrica non ha
nessun contatore per canale né un trigger che dica "sei a 33, fermati e guarda i dati" — cosa
rilevante perché oggi abbiamo solo 8 video prodotti in tutto (BASELINE.md §4): siamo lontanissimi
dal primo checkpoint, e nemmeno lo misureremmo se lo raggiungessimo.

## 4. Conflitti

Nessun conflitto fra corso e fabbrica sul metodo — la fabbrica semplicemente non implementa
ancora nessuno dei quattro assi (durata flessibile, frequenza minima, proporzione trend/evergreen,
checkpoint di volume). Un solo punto di frizione interno alla fabbrica stessa, non col corso:
DURATA_MASSIMA_S e PAROLE_MINIME_SCRIPT si contraddicono a prescindere da cosa dica il corso — il
corso semmai conferma che avere un tetto universale è concettualmente sbagliato, aggravando (non
originando) D-1. Da registrare in CONFLITTI.md come C-008 con l'arbitrato.

## 5. Regole estratte

Sette regole: due parametriche (frequenza, floor durata), due costruttive nuove (script/funzione
per durata per-nicchia e per checkpoint di volume), una costruttiva per trend/evergreen, una
conferma/collegamento di D-2, una euristica di metodo. Dettaglio completo con prova in
regole/A6-viral-mastery/L05_durata_e_frequenza.py.

| id | tipo | regola in una riga | azione | tocca |
|---|---|---|---|---|
| A6-L05-01 | parametro | frequenza minima 3 video/settimana (12-15/mese), nessun gate oggi | costruisci | regolatori.py (nuova costante + check) |
| A6-L05-02 | vincolo | DURATA_MASSIMA_S/DURATA_MINIMA_S fissi e uguali per ogni nicchia contraddicono l'insegnamento "la durata dipende dal contenuto necessario" | ridisegna | regolatori.py, apex7_orchestrator.py |
| A6-L05-03 | funzione | serve una funzione che derivi il range di durata ammesso dal tipo di nicchia (flash/news vs evergreen/spiegazione), non una costante globale | costruisci | regolatori.py (nuova funzione range_durata_per_nicchia) |
| A6-L05-04 | parametro | floor di 4 minuti raccomandato per video corti "per natura", motivato da retention/algoritmo consigliati | costruisci | regolatori.py |
| A6-L05-05 | parametro | soglia 8 minuti = più inserzioni mid-roll, opzionale, da esporre come informazione non come vincolo | costruisci | regolatori.py o reference |
| A6-L05-06 | parametro | proporzione trend/evergreen 70/30 (85/15 in spinta), primi 15 video evergreen | costruisci | piano editoriale / niche-scout |
| A6-L05-07 | script | checkpoint di volume 33/100/500 video per canale, nessun contatore/trigger oggi | costruisci | nuovo milestone_tracker.py |

## 6. Applicabilità

Alta e concreta su frequenza, trend/evergreen e checkpoint di volume: sono numeri secchi dati dal
corso, assenti dalla fabbrica, immediatamente traducibili in costanti e controlli — a differenza
della SEO (L01), qui non c'è un bug da correggere ma una funzionalità intera da costruire
(coerente col mandato del 2026-09-10: non solo regole, anche pezzi di fabbrica mancanti).
Applicabilità alta ma diversa sulla durata: non "applico il numero del corso", ma "applico la sua
logica" — sostituire un tetto universale con un range per-nicchia è più lavoro di una costante, è
un ridisegno, e va sul binario B con collaudo pieno.

## 7. D-1 — la risposta diretta

D-1 NON si chiude con "il numero motivato dalla lezione", nel senso letterale in cui BASELINE.md
lo aspettava. La lezione, letta integralmente (parlato + schermo, con la prova a schermo più
forte possibile: il docente stesso lascia in bianco la voce "quanto devono durare i video?" nel
proprio riepilogo per tutti i 14:22, mentre risponde con un numero a tutte le altre tre domande)
insegna esplicitamente che non esiste una durata ottimale universale — dipende dalla nicchia e dal
contenuto necessario per esaurirla. Dichiararlo onestamente (come impone BASELINE.md stessa) è
più corretto che forzare uno dei due numeri disponibili (4 min floor, 8 min soglia
monetizzazione) a fare da "numero magico" che non è.

Quello che la lezione permette di fare, ed è comunque un passo avanti reale su D-1: dice perché
l'attuale coppia di costanti è sbagliata nell'impianto (un tetto fisso uguale per ogni nicchia non
ha senso per definizione, secondo il corso stesso) e dà due numeri reali da innestare in un
sistema per-nicchia: 4 minuti come floor (non più un vincolo a 480s/600s scollegato dal
contenuto) e 8 minuti come soglia informativa di monetizzazione, non come tetto. La proposta
concreta (regola A6-L05-02/A6-L05-03, gate A6): sostituire la coppia fissa con una funzione
range_durata_per_nicchia(niche_type) che per niche "flash/news" ammette 60s-4min, per niche
"standard" richiede minimo 4-8min senza tetto rigido, lasciando PAROLE_MINIME_SCRIPT coerente col
range scelto invece che fisso a 2220. Questo chiude la contraddizione interna (nessun video sarà
più impossibile da produrre) senza inventare un numero che la lezione non dà.
