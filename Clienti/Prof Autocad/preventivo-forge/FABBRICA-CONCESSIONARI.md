# FABBRICA CONCESSIONARI — come replico un'app e come blocco chi non paga

Documento per Max. Spiega TUTTO, senza dare per scontato niente.

---

## 1. L'idea in una riga
**Un solo motore, tante app.** Il codice (scraping, prezzo, PDF, controlli) è UNO.
Ogni concessionario riceve la SUA app: identica, col suo nome e i preventivi col suo stile.
Quando correggo un bug, lo correggo una volta → vale per tutti.

Per ogni concessionario cambia SOLO: **nome · dati (P.IVA/sede/contatti) · logo · prezzo · colori**.

---

## 2. Nuovo concessionario — cosa faccio io quando me lo dici

Tu mi dici: *"Ho un nuovo concessionario: <nome>, P.IVA…, logo qui…"*.
Io eseguo un comando che fa tutto:

```
python nuovo_concessionario.py --id acme --nome "Acme Auto srl" \
  --piva 01234567890 --sede "via Roma 1, Milano" --tel "02 123" \
  --email info@acme.it --pec acme@pec.it --logo "logo-acme.png" \
  --accent "#123456" --highlight "#e08a00" --build
```

Cosa produce:
1. `concessionarie/acme/config.json` + `logo.png` → l'identità del dealer nel motore.
2. `Clienti/Acme Auto srl/App/PreventivoForge/PreventivoForge.exe` → **la sua app**, che
   nel titolo mostra "PreventivoForge — Acme Auto srl" e fa i preventivi coi suoi colori/logo.
3. `Clienti/Acme Auto srl/CONSEGNA.md` → nota di consegna.

Poi registro l'abbonamento (`gestione-licenze.py aggiungi acme`) e ti do la cartella da consegnare.
**Requisiti sul PC del concessionario:** Google Chrome + connessione normale (no VPN). Nient'altro.

---

## 3. KILL-SWITCH — come blocco chi non paga (spiegato per intero)

### Dov'è lo "switch"
Un file JSON online, ospitato su un **Gist GitHub segreto** (creato una volta sul tuo account
GitHub `ansjkfgheqrlg`). Segreto = raggiungibile solo da chi ha il link, non pubblico/cercabile.
Contiene lo stato di ogni concessionario, es:
```json
{ "novacar": "active", "acme": "suspended" }
```
Il suo indirizzo (URL) è cucito dentro ogni app (nel loro `config.json`, campo `license_url`).

### Cosa fa l'app
Prima di OGNI preventivo l'app legge quel file online.
- `active` → lavora normale.
- `suspended` → mostra "Abbonamento sospeso" e **rifiuta** di fare il preventivo.

### Cosa fai TU
Una frase. *"Novacar non paga."* Io eseguo:
```
python gestione-licenze.py sospendi novacar      # blocca
```
→ entro ~1 minuto, al prossimo link, la sua app si blocca. Poi ti preparo/mando l'email
di sospensione (`templates/email-sospensione.txt`).

Ha pagato? *"Novacar ha pagato."* →
```
python gestione-licenze.py attiva novacar        # sblocca
```
Vedere tutti gli stati: `python gestione-licenze.py stato`.

**Tu non apri file, non tocchi GitHub, non cambi niente.** Dici il nome. Faccio io.

### È a prova di furbo?
- Stacca internet per aggirarlo con stato "sospeso" → l'app usa l'ultimo stato noto (in cache):
  se era sospeso, **resta sospeso**. Non si sblocca offline.
- Rete lenta/giù ma cliente in regola → l'app funziona lo stesso (non blocco mai chi paga
  per colpa della rete). Il blocco vero scatta solo quando lo stato online dice "suspended".

### Setup una-tantum (serve il tuo OK una volta)
Devo creare il Gist segreto (pubblica un file online → serve il tuo consenso esplicito).
Dopo, salvo il suo id in `licenze.config.json` (locale) e scrivo l'URL nei config dei dealer.
Da lì in poi gestisco tutto io a comando.

---

## 4. Cosa cambia vs cosa resta (chirurgico)
| Cambia per concessionario | Resta identico (il motore) |
|---|---|
| `concessionarie/<id>/config.json` (nome, dati, prezzo, colori, `license_url`) | scraper · parser · pricer · cdp · run.py |
| `concessionarie/<id>/logo.png` | template PDF (parametrico su logo/colori) |
| `brand.json` accanto all'exe (titolo app + dealer) | gate A/B/C/D/IMG/R + REGOLE-SACRE |
| una riga nella lista licenze online | licenza.py (kill-switch) |

## 5. File del sistema
- `nuovo_concessionario.py` — fabbrica (crea config + cartella + app brandizzata).
- `gestione-licenze.py` — console abbonamenti (sospendi/attiva/stato).
- `licenze.config.json` — id del Gist (locale, gitignorato).
- `implementation/licenza.py` — il controllo dentro l'app (kill-switch).
- `templates/email-sospensione.txt` / `email-riattivazione.txt` — email pronte.
- Skill: `/nuovo-concessionario` (guida operativa passo-passo).
