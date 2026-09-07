# Pubblicazione YouTube — cosa il wizard offre e noi non usiamo

> Regole `A6-L00-01` e `A6-L00-02`, imparate da **AI TUBE PRO / YouTube Viral Mastery / L00 —
> Caricamento video su YouTube**, minuti 08:46-10:08, verificate confrontando il wizard reale
> con `02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py` riga per riga (in italiano E in
> inglese: un primo controllo solo in italiano aveva dichiarato assente un passo che invece è
> già automatizzato — vedi `A6-L00-03`).

---

## Cosa automatizziamo già (nessun delta)

`youtube_uploader_playwright.py` copre: monetizzazione On/Off del wizard, autocertificazione di
idoneità pubblicitaria (clic automatico su "None of the above" quando rileva il questionario),
il toggle separato "Watch Page ads" dopo l'upload, la dichiarazione "non per bambini". Tutti e
quattro verificati nel codice, non assunti.

## Cosa il wizard offre e non tocchiamo mai

Tre elementi video, tutti nella tab "Elementi video" del wizard, **zero righe di codice** in
tutto il reparto:

| Elemento | Cosa fa | Perché potrebbe contare |
|---|---|---|
| **Sottotitoli nativi** (traccia CC) | Diversi dal karaoke bruciato nel video da Fliki: una traccia separata che YouTube indicizza per la ricerca e offre a chi disattiva il video | SEO on-platform, accessibilità — non visibile a chi guarda con l'audio attivo |
| **Schermata finale** | Ultimi 5-20 secondi: elementi cliccabili (video successivo, iscriviti) | Watch-time della sessione, iscritti — il corso lo mostra ma non ne spiega l'impatto in questa lezione |
| **Schede** | Overlay cliccabile in un punto preciso del video (video/playlist/canale/link) | Stessa famiglia della schermata finale, agganciabile a un momento specifico del parlato |

**E una assegnazione che non facciamo mai:** nessun video viene messo in una playlist. Le
playlist raggruppano sessioni di visione per tema — YouTube le premia in watch-time complessivo
del canale, non del singolo video — e si creano/gestiscono **una volta per canale**, non ad ogni
pubblicazione. Il numero preciso, dichiarato dal corso come raccomandazione di YouTube stesso
(`A6-L01-02`, L01 @ 13:18): **almeno due playlist per video**, non una generica.

## Non ancora deciso

**Nessuno dei quattro è costruito.** Sono candidati (binario A: la scheda esiste, il motore no),
in coda a un ordine di priorità che si decide **a fine categoria A6**, con i dati reali di CTR
(L04) e crescita community (L08) davanti — costruire una schermata finale prima di sapere se il
problema del canale è il CTR o la ritenzione sarebbe indovinare, non decidere.

## La lezione di metodo, non di YouTube

**Verificare "non è gestito" in due lingue, sempre** (`A6-L00-03`). Il nostro Studio automatizzato
parla inglese (`"Inappropriate language"`, `"None of the above"`), il corso sorgente parla
italiano (`"Linguaggio inappropriato"`, `"Nessuno dei contenuti precedenti"`). Un grep in una
lingua sola ha prodotto oggi un falso negativo su un passo già coperto — corretto prima di
finire in un report, non dopo.
