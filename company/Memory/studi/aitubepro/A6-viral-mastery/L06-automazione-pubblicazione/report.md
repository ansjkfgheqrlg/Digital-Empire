# Report — A6/L06 «Automazione della pubblicazione Video su YouTube» (07:20)

- **Durata:** 07:20 · ~1.164 parole · **profondità ORO**
- **Letta:** parlato integrale + 7/27 frame unici (tutorial a schermo condiviso)
- **Materiale grezzo:** appunti.md nella stessa cartella · frame scelti: frame-scelti.md

---

## 1. Cosa insegna

Uso dello scheduling nativo di YouTube Studio per programmare la pubblicazione: caricamento
multiplo con stato bozza, orario scelto in base agli analytics reali del pubblico del canale
(sezione Analytics > Pubblico, "quando è online"), motivazione algoritmica (l'interazione nelle
prime ore pesa sulla spinta del video), routine consigliata di batch (2-3 ore una volta a
settimana invece di pubblicazioni quotidiane manuali), ed eccezione esplicita per contenuti
trend/flash che vanno pubblicati subito, mai programmati.

## 2. Cosa facciamo oggi nella fabbrica

Verificato leggendo il codice, non assunto dal nome del file:
YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py:432-451 imposta
SEMPRE la visibilita a "Privato" ("Impostazione visibilita (Privato per sicurezza)..."), senza
eccezioni e senza alcuna logica di scheduling. Grep sul file: zero occorrenze di scheduling, di
lettura degli orari di picco del pubblico, di logica data/ora di programmazione. Nessun
collegamento fra la fabbrica e l'API/UI Analytics "pubblico" di YouTube Studio.

## 3. Delta

Questo e il delta piu pesante trovato nel giro di quattro lezioni, perche non tocca una rifinitura
(SEO, playlist) ma il cuore del problema gia misurato in BASELINE.md §4 e in ADR-016 (Ultimo
Metro): "solo 2 video su 8 hanno una destinazione tracciata", 6 prodotti e mai arrivati al
pubblico. La fabbrica sa produrre video (pipeline apex7 -> fliki -> uploader) ma l'uploader stesso
chiude ogni video in "Privato", quindi anche quando arriva fino in fondo alla catena tecnica NON
diventa mai pubblico automaticamente: serve sempre un intervento umano successivo per renderlo
visibile. **Verificato prima di proporre qualunque correzione**: "Privato" non e una dimenticanza,
e una policy dichiarata (`.claude/commands/avvia-yt.md:82`: "Visibilita sempre Private, mai
pubblico senza conferma esplicita di Max per quel video") — quindi il delta corretto non e
"manca lo scheduling", e "manca lo scheduling COME AZIONE SUCCESSIVA all'approvazione di Max": la
lezione mostra la funzione nativa (scheduling YouTube Studio) che oggi non esiste in nessun punto
della catena, nemmeno per i video gia approvati a mano. Un video approvato oggi resta comunque
privato finche' qualcuno non entra su YouTube Studio e lo pubblica manualmente — lo scheduling
data-driven per orario ottimale (letto dagli analytics del canale) non esiste in nessuna forma.

Delta secondario ma reale: nessuna distinzione nella fabbrica fra contenuto pianificabile
(evergreen, va bene programmato) e contenuto trend/flash (va pubblicato subito) — la lezione
tratta questa distinzione come ovvia e operativa, la fabbrica non ha nessun campo o flag che la
rappresenti.

## 4. Conflitti

Un conflitto reale, registrato in CONFLITTI.md come **C-008**: il corso insegna a programmare la
pubblicazione in autonomia; la fabbrica ha un gate esplicito e voluto ("mai pubblico senza
conferma esplicita di Max"). Non e un conflitto da risolvere scegliendo un vincitore assoluto —
il gate di Max resta (nessuna azienda automatizza la messa in pubblico senza controllo umano su
un canale reale), ma lo scheduling del corso si applica CORRETTAMENTE **dopo** quel gate, non al
posto suo: oggi manca anche quello, quindi anche un video che Max approva non ha nessun percorso
automatico per diventare pubblico a un orario scelto — resta un secondo passaggio manuale
identico a quello che il corso automatizza. Vedi CONFLITTI.md C-008 per l'arbitrato per esteso.

## 5. Regole estratte

Tre regole, la prima delle quali e la piu importante emersa in tutto questo giro di studio per
impatto operativo diretto — e progettata per NON toccare il gate di conferma di Max. Dettaglio con
prova in regole/A6-viral-mastery/L06_automazione_pubblicazione.py.

| id | tipo | regola in una riga | azione | tocca |
|---|---|---|---|---|
| A6-L06-01 | funzione | dopo l'approvazione di Max manca un percorso che programmi il video (Programmato, non solo Privato) invece di lasciarlo per un secondo intervento manuale | costruisci | 02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py |
| A6-L06-02 | funzione | l'orario di pubblicazione va scelto leggendo gli analytics "pubblico" del canale (quando e online), non fissato a caso | costruisci | 02-AUTOMAZIONI-E-SCRIPTS/ (nuova funzione orario_ottimale_da_analytics) |
| A6-L06-03 | parametro | serve un flag/campo che distingua contenuto pianificabile (programmato) da contenuto trend/flash (pubblicazione immediata) nel piano editoriale | costruisci | piano editoriale / coda_produzione.json |

## 6. Applicabilità

Alta su A6-L06-01: e la funzione nativa gia disponibile nell'interfaccia che l'uploader gia
automatizza (stesso wizard, stesso stepper "Visibilita") — non serve nessuno strumento nuovo, e
soprattutto non tocca il gate di conferma di Max, lo completa. Resta comunque binario B con gate
pieno per il rischio (tocca cosa diventa pubblico davvero). Alta anche su A6-L06-02, che dipende
pero dall'accesso via Playwright alla sezione Analytics (da verificare in un giro tecnico
separato, non in questo studio). Media su A6-L06-03, utile ma non bloccante.
