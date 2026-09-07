# Report — A6/L00 «Caricamento video su YouTube» (12:05)

- **Durata:** 12:05 · ~1.801 parole · **profondità ORO**
- **Letta:** parlato integrale + 42/363 frame unici (tutti guardati, nessun campionamento) —
  frame + parlato, non solo l'uno o l'altro
- **Rapporto grezzo:** [`appunti.md`](appunti.md) · frame: [`frame-scelti.md`](frame-scelti.md)

---

## 1. Cosa insegna

Il wizard di pubblicazione YouTube Studio **per intero**, passo per passo, su un canale già
monetizzato: caricamento file, naming, tab Monetizzazione (tipo annunci + autocertificazione di
idoneità pubblicitaria, quasi 4 dei 12 minuti), tab Elementi video (sottotitoli/schermata
finale/schede), tab Dettagli/Visibilità (playlist, pubblico "per bambini", licenza, categoria,
commenti), tab Controlli (check automatico copyright + idoneità), chiusura in bozza.

## 2. Cosa facciamo oggi

`youtube_uploader_playwright.py` automatizza l'upload end-to-end. Confrontato riga per riga (non
per assenza di una parola sola — vedi §3, un mio primo controllo era sbagliato):

| Passo del wizard | Nel nostro codice |
|---|---|
| Monetizzazione On/Off | ✅ `_gestisci_step_monetization` (riga 48) — sceglie sempre "On" |
| Autocertificazione idoneità annunci | ✅ stessa funzione, righe 129-138 — rileva "Inappropriate language" (EN) e clicca "None of the above" |
| Watch Page ads (toggle separato, spento di default) | ✅ `ads_on_after_upload` (riga 225), **dopo** l'upload |
| Dichiarazione "per bambini" | ✅ righe ~395-398, verificata dal vivo il 2026-08-17 |
| Titolo, descrizione, tag | ✅ (metadata passati dalla pipeline F4, non ispezionati riga per riga in questo giro) |
| Sottotitoli nativi (traccia CC) | ❌ zero righe, verificato in italiano e inglese |
| Schermata finale | ❌ zero righe, verificato in italiano e inglese |
| Schede (video/playlist/canale/link) | ❌ zero righe, verificato in italiano e inglese, e sull'intero reparto (non solo questo file) |
| Assegnazione a una playlist | ❌ zero righe in tutto `YOUTUBE-AUTOMATION-FACTORY/` |
| Licenza, incorporamento, categoria, commenti | non verificato in questo giro (fuori dal grep mirato) |

## 3. Delta

**Il delta più grande della lezione non è dove sembrava.** Il questionario di autocertificazione
(quasi un terzo del video) **è già coperto**: l'ho creduto assente per un primo grep solo in
italiano, corretto ricontrollando in inglese (la UI automatizzata è in EN). *Un grep in una sola
lingua misura la lingua del grep, non l'esistenza del codice* — variante della stessa lezione di
CP-20260907-PG43 (leggere la fonte vera, non fermarsi al primo esito comodo).

**Il delta vero, verificato in entrambe le lingue e su tutto il reparto:** tre elementi video del
wizard **non hanno alcuna automazione** — sottotitoli nativi (traccia CC separata dal karaoke
bruciato di Fliki), schermata finale, schede — e la **playlist non viene mai assegnata**. Nessuno
dei quattro è un bug: sono passi del wizard che la pipeline attuale salta interamente, senza
errore, perché non li tocca affatto.

## 4. Conflitti

Nessuno con le nostre scelte esistenti. Un conflitto interno **mio**, non del corso: il primo
controllo (§3) ha prodotto una conclusione falsa per un metodo incompleto (una lingua sola). Non
va in `CONFLITTI.md` (non è un conflitto corso-vs-fabbrica, è un errore di verifica corretto
prima di essere scritto in un report finale — la cosa che il gate A4 aveva già insegnato a
temere).

## 5. Regole estratte

Tre, tutte binario A (nessuna tocca il motore oggi — sono candidati, non applicazioni).

| id | regola in una riga | tocca |
|---|---|---|
| `A6-L00-01` | Tre elementi del wizard (sottotitoli nativi, schermata finale, schede) non sono mai automatizzati: candidati per `youtube_uploader_playwright.py`, priorità da stabilire a fine categoria coi dati di CTR/community di L04 e L08 | `04-SKILLS-E-REFERENCE/references/youtube-pubblicazione.md` (nuovo) |
| `A6-L00-02` | Nessun video viene mai assegnato a una playlist: la playlist raggruppa sessioni di visione e YouTube la premia in watch-time, ma va creata/gestita una volta per canale, non per video | stesso file |
| `A6-L00-03` | Verificare in due lingue (IT del corso, EN del nostro Studio automatizzato) prima di dichiarare un passo "non gestito": un grep in una lingua sola ha prodotto un falso negativo oggi stesso | procedura interna allo studio, non tocca la fabbrica |

## 6. Applicabilità

Alta sulla scoperta del metodo (verificare in due lingue), media sui tre elementi mancanti — utili
ma non bloccanti: i video pubblicano e guadagnano lo stesso senza schede/schermata
finale/playlist/sottotitoli nativi, sono leve di crescita in più, non un difetto che rompe
qualcosa. Bassa sul resto della lezione (naming file, consiglio "canale monetizzato pronto"): non
applicabile, sono canali già di nostra proprietà.
