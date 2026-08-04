# COME CONSEGNARE PREVENTIVOFORGE A NOVACAR — passo per passo (per Max)

Hai **UN solo file** da consegnare:
`Clienti/Prof Autocad/Consegna-Novacar/PreventivoForge-Novacar-AGGIORNATA-9lug.zip`

Dentro c'è tutto. Novacar **non deve installare Python né altro**. Serve solo Google Chrome.

> ⚠️ **Se hai già mandato una versione vecchia:** rimanda QUESTO file e di' a Novacar di
> **cancellare la vecchia cartella `PreventivoForge`** prima di estrarre la nuova — altrimenti
> restano due copie e continua ad aprire quella sbagliata (interfaccia vecchia).

## 🔴 REGOLA N.1 — VA ESTRATTA TUTTA LA CARTELLA
L'app **non è un file singolo**: è `PreventivoForge.exe` **+ la cartella `_internal`** accanto
(dentro c'è il motore, l'**interfaccia grafica** `ui/index.html`, il template PDF, la licenza).

- ❌ **MAI** doppio-click sull'exe **dentro lo zip** (Windows chiede "Estrai o Esegui" → se scegli
  "Esegui", tira fuori SOLO l'exe senza `_internal` → non parte, o parte con l'interfaccia base/brutta).
- ✅ **SEMPRE**: tasto destro sullo **ZIP** → "Estrai tutto" → poi aprire l'exe **dalla cartella estratta**.

**Verifica**: accanto a `PreventivoForge.exe` DEVE esserci la cartella **`_internal`**. Se non c'è → non ha estratto.

---

## PRIMA — controlla 2 cose sul PC di Novacar
1. **Google Chrome installato.** (Apri Chrome: se si apre, ok. Altrimenti scaricalo da google.com/chrome.)
2. **Connessione internet normale** (di casa/ufficio). **Niente VPN.**

Nient'altro.

---

## OPZIONE A — di persona, con chiavetta USB  ⭐ (la più semplice)
1. Copia `PreventivoForge-Novacar-AGGIORNATA-9lug.zip` su una **chiavetta USB**.
2. Infila la chiavetta nel PC di Novacar.
3. Copia lo zip sul **Desktop** del loro PC.
4. **Tasto destro** sullo zip → **"Estrai tutto"** → **"Estrai"**. Esce una cartella `PreventivoForge`.
5. Apri la cartella `PreventivoForge` → **doppio click su `PreventivoForge.exe`**.
6. **Prima volta**, Windows dice *"Windows ha protetto il tuo PC"*:
   → clicca **"Ulteriori informazioni"** → **"Esegui comunque"**. (Solo la prima volta.)
7. Si apre l'app. **Incolla un link mobile.de** → **"Genera preventivo"** → dopo 1-2 minuti **esce il PDF**. ✅

---

## OPZIONE B — a distanza, con WeTransfer (gratis, no registrazione)
1. Vai su **wetransfer.com** → "I agree".
2. Clicca **"+"** → scegli `PreventivoForge-Novacar-AGGIORNATA-9lug.zip`.
3. Nel campo email metti quella di Novacar (**novacarsrl.info@gmail.com**) → **"Transfer"**.
4. Novacar riceve un'email con un link → **scarica** lo zip.
5. Novacar poi fa: **Estrai tutto** → doppio click `PreventivoForge.exe` → (SmartScreen) **Esegui comunque**.

*(In alternativa: carica lo zip su Google Drive e condividi il link con Novacar.)*

---

## La cartella pesa ~300 MB — è normale
Contiene tutto il necessario per girare **senza installare niente**.

## Se qualcosa non va sul loro PC
| Problema | Soluzione |
|---|---|
| "Chrome non trovato" | installare Google Chrome |
| Scraping fallito | togliere la VPN (usare linea normale) |
| Avviso blu di Windows | "Ulteriori informazioni" → "Esegui comunque" |
| Grafica base | funziona lo stesso; su Windows 11 è al massimo |

## Abbonamento (kill-switch) — già dentro
L'app è già collegata al controllo abbonamento. Quando vuoi:
- **"Novacar non paga"** → dico io: la blocco in 10 secondi + email.
- **"Novacar ha pagato"** → la riattivo.

## Traduzione — già a posto
Glossario + riserva AI gratuita (dentro il pacchetto): traduce tutto, non consegna mai tedesco. €0.
