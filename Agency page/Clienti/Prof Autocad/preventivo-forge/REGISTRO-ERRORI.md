# REGISTRO-ERRORI — PreventivoForge (memoria di debug)

**Scopo:** ogni errore riscontrato va scritto QUI con causa radice + fix + **regola per non ripeterlo**.
Prima di modificare o consegnare: leggere questo file. **Nessun errore va commesso due volte.**
Vale per Max, Gael e Claude. (Allineato all'ISPETTORATO GENERALE — REGISTRO-ERRORI + gate anti-recidiva.)

---

## Regole permanenti (derivate dagli errori sotto)

1. **Un fetch è "riuscito" solo con i DATI, non solo perché "non è bloccato".** (E1)
2. **Non aprire una sessione browser nuova a ogni scrape**: riusa il profilo/cookie (anti-blocco IP). (E2)
3. **I gate bloccano SOLO su difetti NOSTRI** (prezzo/foto assenti o tagliate, tedesco nel titolo).
   Mai bloccare su qualità della SORGENTE (foto piccole del venditore, 1 parola rara). (E3, E4)
4. **Confronta numeri come numeri**, non come stringhe (0.0 ≠ "0" è un bug). (E5)
5. **La riserva AI copre TUTTI i campi**, e gira PRIMA di costruire i campi derivati + una passata finale. (E6)
6. **Glossario per sigle/enti** (TÜV, HU, AU…) + prompt AI "nessuna parola in tedesco". (E7)
7. **MAI rebuild/zip con l'app aperta** (blocca i file → build/zip falliscono in silenzio).
   Sempre: chiudere l'app → verificare `BUILD_EXIT=0` + timestamp exe fresco. (E8, E9)
8. **Ogni build va provata live su 2-3 auto diverse** prima di consegnarla (0 residui, PDF ok).
9. **L'app non deve MAI degradare in silenzio.** Se un componente serve all'esperienza promessa
   (es. WebView2 per l'interfaccia premium), va **incluso nel pacchetto e installato**, non aggirato
   con un fallback brutto. Un fallback silenzioso = il cliente riceve un prodotto diverso da quello approvato. (E10)
10. **Ogni build mostra la sua VERSIONE nell'interfaccia** (`APP_VERSION` nell'header). Senza, è impossibile
   distinguere una copia vecchia da una nuova e si perde tempo a inseguire il file sbagliato. (E10)
11. **"Funziona sul mio PC" non basta**: elencare le dipendenze dell'AMBIENTE CLIENTE (Chrome, WebView2, no VPN)
   e verificarne la presenza dal codice, non nel README. (E10)
12. **Non introdurre dipendenze d'ambiente che NON puoi testare tu.** Se un componente (es. WebView2) può
   mancare sul PC cliente e tu non riesci a riprodurre il guasto, cambia architettura verso qualcosa di
   GARANTITO e testabile (es. Chrome, già richiesto). "Quel che vedo io = quel che vede il cliente." (E11)
13. **Verifica il deliverable ESTRAENDO lo zip come il cliente**, non solo la cartella dist. Avvia QUELL'exe. (E11)
14. **La sorgente è di qualcun altro e cambia senza avvisare.** Il fallimento in campo di un'app che
   "funzionava da un mese" è, per default, un cambio del sito sorgente — non un guasto del PC cliente.
   Prima cosa da fare: riprodurre col LINK DEL CLIENTE sulla nostra macchina e leggere il log, non
   indagare sul suo PC. (E12)
15. **Mai legarsi a UN SOLO punto di estrazione dati.** Supportare più formati (vecchio + nuovo) e far
   dipendere il "successo" dai DATI ottenuti, non dal nome della variabile che li conteneva. (E12)
16. **Ogni campo di testo che arriva dalla sorgente va tradotto ALLA FONTE**, prima di costruire i
   campi derivati (titolo, descrizione, scheda). Un campo tradotto "a valle" riaffiora in tedesco
   negli altri punti che lo usano. (E13, stessa lezione di E6)
17. **Un gate verde non è la prova che il PDF è pulito**: verificare anche i campi che il gate non
   guarda (es. il titolo con prezzo prodotto da S4). Guardare il PDF, non solo i log. (E13)

---

## Errori registrati (2026-09-02) — guasto in campo Novacar

| ID | Sintomo | Causa radice | Fix | Regola |
|----|---------|--------------|-----|--------|
| **E12** | **Il cliente non genera più NESSUN preventivo** dopo un mese di funzionamento ("Non riuscito: scraping da mobile.de fallito (anti-bot Akamai o link non valido)"). Sembrava: build vecchia sul PC del cliente, oppure blocco Akamai, oppure licenza | **Nessuna delle tre. mobile.de è passato a Next.js (App Router) e ha ELIMINATO `window.__INITIAL_STATE__`**, dove stavano tutti i dati dell'auto. La pagina si scarica benissimo (nessun blocco), ma lo scraper cercava una variabile che non esiste più → `got_state` mai vero → 3 tentativi → errore con messaggio fuorviante che accusava Akamai. Riprodotto sul PC di Max con la v2.1: stesso fallimento, quindi NON era il PC del cliente | `scraper.py`: nuovo estrattore del payload RSC di Next.js (`self.__next_f.push([1,"…"])` → riga `"listing":{…}`), con risoluzione dei riferimenti flight (`"$43"` = descrizione), URL foto ricostruite (`?rule=mo-1600.jpg`, senza `.jpg` mobile.de serve AVIF) e normalizzazione alla vecchia forma `.ad` → **il parser S2 resta invariato**. Il vecchio formato resta supportato come primo tentativo. Condizione di successo (`_has_ad_payload`) ora accetta ENTRAMBI i formati | R14, R15 |
| **E13** | Preventivo bloccato dal Gate B ("tedesco residuo: Leder") e, una volta sbloccato, **titolo del PDF in tedesco**: "Smart ForTwo **Leder** 22.560 €" | L'allestimento (`trimLine` di mobile.de) non veniva tradotto: finiva grezzo in titolo, descrizione e scheda. In più `pricer.py` componeva `final_title` dai campi RAW pur avendo il titolo italiano già pronto (il commento diceva il contrario del codice) | `translate_copy.translate()` traduce `variant` **sulla fonte**, prima dei derivati; `pricer.price()` usa `content.title_it` quando esiste. Aggiunto a glossario `gepäckraumabtrennung` | R16, R17 |
| **E15** | Titolo del preventivo "Fiat **Andere** Ellenator" | `Andere` ("altro") è il SEGNAPOSTO che mobile.de mette quando il modello non è nel suo elenco: non è un nome, e finiva in titolo, descrizione e scheda | `build_title_it()` scarta i segnaposto (`andere/sonstige/other`); descrizione e scheda usano lo stesso nome → "Fiat Ellenator" | R16 |
| **E14** | Parole tedesche comuni intatte nel titolo ("MG MG3 … Navigatore **Kamera**") | `Kamera`, `Leder` ecc. stavano solo in `MORPHEMES`, tabella usata **soltanto** per scomporre i composti: una parola isolata che coincide con un morfema non veniva mai cercata lì | `_translate_words()`: ultimo tentativo su `MORPHEMES` per token ≥4 caratteri. Verificato che NON traduce sigle/inglese (GT Line, Business Edition, Style restano intatti) | R16 |

**Collaudo del fix (2026-09-02):** 4 auto diverse, pipeline completa fino a GATE_R:
Smart ForTwo (23 foto), MG MG3, Mercedes-Benz E 300, Volkswagen Polo GTI — **tutte verdi**, PDF generato.
Tempo scraping: ~16 s (prima: 60 s di tentativi e poi errore).

---

## Errori registrati (2026-07-05)

| ID | Sintomo | Causa radice | Fix (commit) | Regola |
|----|---------|--------------|--------------|--------|
| **E1** | Scraping "riuscito" ma PDF vuoto / falso "anti-bot" | bail a 20s afferrava la pagina PRIMA che il JS caricasse `window.__INITIAL_STATE__`; il check accettava la pagina senza dati | scraper aspetta `__INITIAL_STATE__` e lo PRETENDE per il successo; bail solo su vera challenge (`07d4886`) | R1 |
| **E2** | IP bloccato da mobile.de dopo molti scrape | profilo Chrome NUOVO a ogni scrape = tante "sessioni bot" dallo stesso IP | profilo persistente `browser-profile/` (riusa il cookie Akamai); tentativo1 fisso, retry freschi (`5045ecd`) | R2 |
| **E3** | Gate IMG blocca l'intero preventivo | 2 foto del VENDITORE sotto 300px → bloccava tutto (non è un difetto nostro; con `contain` si vede intera) | foto piccole/non scaricate = avviso; blocca solo su 0 foto/PDF senza foto/senza fit (`dff8a7d`) | R3 |
| **E4** | Gate B blocca "tedesco residuo" | bloccava su 1 sola parola rara in un optional | blocca solo se tedesco nel titolo o abbondante (>3); residuo minore = avviso (`d771d93`) | R3 |
| **E5** | Gate B "Chilometraggio 0 km vs 0" (auto nuova) | confronto stringhe: `str(0.0)`→`"00"` ≠ `"0"` | confronto numerico normalizzato (int) (`d771d93`) | R4 |
| **E6** | Tedesco residuo in descrizione/highlights (batch 10, #7) | riserva AI correggeva solo equipment/specs, MA descrizione/highlights costruiti PRIMA dalle fonti tedesche; rate-limit AI | AI sulle fonti PRIMA dei derivati + passata FINALE su TUTTI i campi + 4 tentativi con gestione 429 (`da9dfe6`) | R5 |
| **E7** | "TÜV" non tradotto | l'AI lo teneva come nome proprio (ente revisione DE) | glossario tüv/HU/AU→revisione ecc. + prompt AI localizza le sigle (`db286b1`) | R6 |
| **E8** | Rebuild fallito in silenzio (exe vecchio consegnato) | app aperta bloccava un file di log → PyInstaller `--clean` non completava, ma sembrava ok | chiudere l'app prima del rebuild; verificare `BUILD_EXIT=0` + timestamp exe | R7 |
| **E9** | Zip di consegna a 0 MB | app in esecuzione blocca `ClrLoader.dll` → `Compress-Archive` fallisce | zip solo con app chiusa | R7 |
| **E10** | **Il CLIENTE vede un'interfaccia "vecchia e brutta"** (funziona ma è un'altra GUI) — sembrava una build vecchia spedita per sbaglio | **NON era il file**: l'interfaccia premium (pywebview/EdgeChromium) richiede il **WebView2 Runtime** installato sul PC. Sul PC di Max c'è → premium. Sul PC del cliente mancava → pywebview alza eccezione → `app.py` ripiegava **in silenzio** sulla GUI **Tkinter** di riserva (brutta). Il pacchetto conteneva le librerie che *chiamano* WebView2, non il runtime | bootstrapper ufficiale Microsoft (`assets/MicrosoftEdgeWebview2Setup.exe`, firmato) incluso nel bundle + `_ensure_webview2()` in `app.py`: rileva il runtime e, se manca, lo installa al 1° avvio (per-utente, no admin, splash di attesa). + **stampo di versione** nell'header GUI (`APP_VERSION`) | R9, R10 |
| **E11** | **DEFINITIVO — la GUI premium NON deve dipendere da WebView2.** Anche col bootstrapper (E10) restava il rischio che l'install fallisse sul PC cliente → ancora GUI vecchia. Impossibile da diagnosticare per Max: sul suo PC WebView2 c'è, quindi ogni "fix" sembrava ok ma il cliente vedeva altro | pywebview su Windows dipende da un backend HTML esterno (WebView2/QtWebEngine) che può mancare | **Nuovo motore GUI `main_chrome_app()`**: la stessa `ui/index.html` è servita da un mini-server locale (127.0.0.1) e renderizzata in una finestra **Google Chrome `--app`** (senza barre). Chrome è GIÀ richiesto (scraping+PDF) → c'è sempre → GUI premium garantita, **zero WebView2**. Bridge JS↔Python via `POST /api/<metodo>`. Ordine motori: Chrome-app → pywebview → Tkinter. **Testabile da Max** (Chrome c'è anche da lui) → quel che vede lui = quel che vede il cliente. Verificato estraendo lo zip come Novacar | R9, R12 |

---

## Come si usa
- Nuovo errore → nuova riga in tabella (ID progressivo) + eventuale nuova regola sopra.
- Prima di un fix, controllare se la causa è già nota qui (evita di re-inventare la ruota).
- Prima di consegnare, ripassare la **checklist** in `CHECKLIST-CONSEGNA.md`.
