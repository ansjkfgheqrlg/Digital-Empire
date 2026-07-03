# CONSEGNA — PreventivoForge per Novacar srl

Guida operativa per consegnare l'app al concessionario e per gestire l'abbonamento.

---

## 1. Cosa consegni

Una sola cartella: **`dist/PreventivoForge/`** (creata da `build_exe.bat`).
Dentro c'è `PreventivoForge.exe` + tutti i file che gli servono. È **portabile**:
la copi su una chiavetta o la zippi e la mandi. Il concessionario **non installa niente**
(niente Python, niente Claude).

## 2. Cosa serve sul PC del concessionario (requisiti)

| Requisito | Perché | Obbligatorio |
|---|---|---|
| **Windows 10 o 11** | l'app è Windows | ✅ sì |
| **Google Chrome installato** | motore di scraping mobile.de **e** di stampa PDF | ✅ **sì, critico** |
| **Connessione internet normale** (casa/ufficio/fibra) | mobile.de (Akamai) blocca datacenter/VPN | ✅ sì |
| WebView2 (Edge) | per la grafica premium | preinstallato su Win11; altrimenti parte comunque (fallback) |

⚠️ **NON usare VPN / hotspot aziendali "mascherati" / IP da server**: l'anti-bot di
mobile.de blocca. La normale linea del concessionario va benissimo.

## 3. Come si usa (per il concessionario)

1. Doppio click su **`PreventivoForge.exe`**.
2. Incolla il **link dell'annuncio mobile.de**.
3. Premi **Genera preventivo**.
4. Si apre Chrome (serve, è normale), l'app lavora ~1-2 minuti, poi **si apre il PDF**.
5. Il PDF è salvato anche in `runs/<data>/` accanto all'app.

### Primo avvio — SmartScreen di Windows
Un `.exe` non firmato può far comparire **"Windows ha protetto il PC"**.
→ Cliccare **"Ulteriori informazioni" → "Esegui comunque"**. Una volta sola.
(Per eliminarlo del tutto servirebbe un certificato di firma codice, ~a pagamento. Opzionale.)

---

## 4. ABBONAMENTO — come bloccare l'app se non paga (kill-switch)

L'app, **prima di ogni preventivo**, controlla online se il cliente è "attivo".
Se lo metti "sospeso", **si blocca al link successivo**. Serve internet (che l'app usa già).

### Attivazione (una volta sola — 3 minuti)

1. Vai su **gist.github.com** (accedi con GitHub, gratis).
2. **Nuovo gist PUBBLICO**: nome file `licenze.json`, contenuto:
   ```json
   {"novacar": "active"}
   ```
3. **Create public gist** → premi il bottone **Raw** → copia l'URL dalla barra.
   Togli l'eventuale codice lungo (hash) dopo `/raw/`, così punta sempre all'ultima versione:
   ```
   https://gist.githubusercontent.com/<tuo-utente>/<id-gist>/raw/licenze.json
   ```
4. Incolla quell'URL nel config del dealer:
   `dist/PreventivoForge/concessionarie/novacar/config.json` → aggiungi la riga:
   ```json
   "license_url": "https://gist.githubusercontent.com/.../raw/licenze.json",
   ```
   (In alternativa, in sviluppo: `LICENSE_URL=` nel file `.env`.)

### Sospendere un cliente (quando non paga)

Apri il gist → cambia `"active"` in `"suspended"` → **Update**.
Al prossimo "Genera" il concessionario vede: *"Abbonamento sospeso — contatta il fornitore"*.
Per riattivare: rimetti `"active"`.

### Perché è a prova di furbo
- Se stacca internet per aggirarlo → l'app usa l'**ultimo stato conosciuto**: se era "sospeso",
  **resta sospeso**. Non si sblocca offline.
- Se la rete è solo lenta/giù ma il cliente è in regola → **grace**: l'app funziona lo stesso
  (non blocchiamo mai chi paga per un problema di rete).
- Multi-cliente: un solo file, una riga per concessionario (`{"novacar":"active","altro":"suspended"}`).

### Perché NON un server tuo / SaaS
mobile.de blocca gli IP dei datacenter. L'app **deve** girare sul PC del concessionario
(col suo IP di casa) per superare l'anti-bot. Il controllo licenza online dà lo stesso potere
di spegnimento **senza** dover mantenere un server.

---

## 5. Cosa può rompersi (e cosa fare)

| Sintomo | Causa probabile | Fix |
|---|---|---|
| "scraping fallito (Akamai)" | VPN/IP datacenter, o link non valido | usare linea normale; ricontrollare il link |
| "Google Chrome non trovato" | Chrome non installato | installare Chrome |
| SmartScreen blocca l'avvio | exe non firmato | "Esegui comunque" (§3) |
| "Abbonamento sospeso" | stato = suspended nel gist | rimettere "active" |
| Grafica "base" (non premium) | manca WebView2 | funziona uguale; installare WebView2 per la resa bella |
| mobile.de cambia layout | aggiornamento del sito | aggiornare `parser.py` (lato nostro) |

## 6. Garanzia di funzionamento (onesta)

Testato **live** su annuncio reale (Mercedes GLA → PDF 18 pagine conforme).
**Prima della consegna reale**: provare l'exe su un **PC pulito** (senza Python/deps installati)
— è l'unico modo per certificare che gira sul PC del concessionario. Vedi test in corso.
