# 01 — E0a: LA MERCE

> Chi: **Max** (mani) · Ore V3: 1-1,5 · Tetto: 2,5 · Dipende da: **nessuno** · Percorsi in scrittura:
> Stripe (esterno), YouTube Studio (esterno), `Crea siti/Siti CCM/checkout.config.json`,
> `company/Memory/pubblicati.json` · Politica di guasto: **fail-open** (un pezzo che non si carica
> non ferma gli altri quattro; un Payment Link che non nasce non ferma il caricamento)
> STATO: COMPLETO (EMPERATOR, 2026-09-11 — scritto a mano dopo la caduta di 11 sentinelle su 11)

**Cosa fa questo scaglione, in una riga:** mette fuori la prima merce già pagata e fa nascere la
capacità di incassare — i due Payment Link e i primi 5 pezzi dei 26 caricabili — **senza aspettare
nessun altro scaglione**. È il giorno uno del piano (V2 §20, criterio 1: *prima l'euro che si può
incassare oggi*), e per V3 §2 è stato separato dalla rotazione delle chiavi (E0b) proprio perché
**non ha prerequisiti**: se Max ha un'ora, la spende qui.

**Il disco ha smentito il piano su un punto, e V4 lo corregge:** V2 §21-E0 scriveva il gate come
`python scripts/ultimo_metro.py --json | jq .caricabili`. **Il flag `--json` non esiste**
(`python scripts/ultimo_metro.py --help`, 2026-09-11: solo `--scrivi` e `--segna ID`). Il gate qui
usa l'output vero; il flag `--json` diventa un passo di `02-E0.5-AGGANCI.md` (serve al cruscotto
quotidiano, V2 §23), non un prerequisito di E0a.

---

## 0. Cosa NON è bloccato da questo scaglione (ADR-028)

Se Max non fa E0a oggi, **procede comunque tutto il resto del giorno uno**:
- `02-E0.5-AGGANCI.md` (EMPERATOR): nessun passo dipende dai Payment Link o dai pezzi caricati.
- `05-E0.6-REGOLE.md` (EMPERATOR + Max, ma solo decisioni): indipendente.
- `06-E0.7-HOOK.md`, `07-E1-PERIMETRO.md`, `09-F3-EMETTITORE.md`, `10-E3.0-RIACCENSIONE.md`:
  indipendenti.

**L'unico scaglione che aspetta E0a è `04-E0.9-ATTO-DI-VENDITA.md`** (aggancia il Payment Link al
prezzo, e non può agganciare un link che non esiste) — e anche lì solo il passo dell'aggancio:
il decreto del prezzo e il link nelle descrizioni video non aspettano.

**Cosa NON fa E0a**, dichiarato: non ruota chiavi (E0b), non decide il prezzo (E0.9 — anche se il
prezzo di lancio è già scritto nel config, vedi §1), non carica i libri KDP (E8: servono le
copertine di Max e la review Amazon, V2 §21-E8).

---

## 1. Prerequisiti — verificati con un comando, non dichiarati

| # | Prerequisito | Comando | Output atteso | Exit |
|---|---|---|---|---|
| P1 | Il magazzino è misurabile | `python scripts/ultimo_metro.py` | stampa `IL CONTO:` con `N pezzi finiti`, `M caricabili subito` (2026-09-11 17:53: **31 fermi, 26 caricabili, 5 a cui manca un pezzo, il più vecchio 143 gg**) | 0 |
| P2 | Il config della cassa esiste ed è leggibile | `python empire/tools/checkout.py --check` | `Placeholder residui: 0` · `tier 2 - fallback ordine attivo` · elenca `stripe_base` e `stripe_bump` come **non attivi** con la riga `MAX: crea Payment Link` | 0 |
| P3 | Il prezzo di lancio è già deciso sul disco | `python -c "import json;d=json.load(open('Crea siti/Siti CCM/checkout.config.json'));print(d['prezzo_lancio_eur'],d['prezzo_listino_eur'],d['bump_eur'])"` | `67 97 27` (misurato 2026-09-11) — **la decisione 8 di V3 §11 ha già un default sul disco: 67 € lancio, 97 € listino, 27 € bump.** E0.9 la ratifica o la cambia; E0a la usa | 0 |
| P4 | Max ha accesso a Stripe e a YouTube Studio | gesto umano, nessun comando | Max lo dichiara nel checkpoint di chiusura (§6) | — |
| P5 | Il registro dei pezzi usciti è scrivibile | `python -c "import json;print(json.load(open('company/Memory/pubblicati.json')))"` | un dizionario con la chiave `pubblicati` (oggi vuoto o assente: `ultimo_metro.py` lo crea al primo `--segna`, riga 73) | 0 |

**Un fatto scomodo trovato da P2, da sistemare in questo scaglione (passo 2.3):** `scadenza_lancio`
è **2026-07-31, già passata** — il conto alla rovescia in `pagamento.html` è sbagliato da 42 giorni.
`checkout.py --check` lo segnala testualmente. Non è un prerequisito: è un passo.

---

## 2. I passi — numerati, ognuno con il comando esatto

### 2.1 — I due Payment Link su Stripe (Max, 10 minuti)

1. Entrare su `dashboard.stripe.com` → **Payment Links** → **+ New**.
2. Link **base**: prodotto «Manuale Claude Code», prezzo **67,00 €** una tantum (il
   `prezzo_lancio_eur` del config, P3), valuta EUR, quantità fissa 1. Copiare l'URL (forma
   `https://buy.stripe.com/...`).
3. Link **bump**: prodotto «Manuale Claude Code — bump», prezzo **27,00 €** una tantum
   (`bump_eur`). Copiare l'URL.
4. Non attivare ancora nessun altro rail (`paypal_me`, `bonifico`): restano `attivo: false` per
   scelta (V2 §21-E0 parla di **2** Payment Link, non di quattro rail).

### 2.2 — Accendere i due rail nel config e propagarli nelle pagine (Max o EMPERATOR, 1 minuto)

```
python empire/tools/checkout.py --accendi-stripe "https://buy.stripe.com/<BASE>" "https://buy.stripe.com/<BUMP>"
```
- Scrive `rails.stripe_base.url`/`.attivo: true` e `rails.stripe_bump.url`/`.attivo: true` in
  `Crea siti/Siti CCM/checkout.config.json` e lancia `--apply` (inietta i link in
  `manuale.html`/`pagamento.html`, idempotente). È il comando dichiarato dal suo stesso `--help`
  come *«quello che porta dal tier 2 al tier 1»*.
- **Contratto d'innesto (V3 §4), compilato:** il file toccato è un JSON di configurazione e due
  pagine HTML statiche — nessun motore vivo li importa a runtime (verifica: `grep -rl
  "checkout.config.json" --include=*.py . | grep -v checkout.py` → solo `empire/controllo` lo
  legge, in sola lettura, per il gate INCASSO). Politica: fail-closed sul comando (se un URL non
  è `https://buy.stripe.com/...` il comando deve rifiutare — **se oggi non lo fa, è una riga da
  aggiungere in E0.5**). Rientro: `git checkout -- "Crea siti/Siti CCM/"`.

### 2.3 — Spostare la scadenza del prezzo di lancio (Max decide la data, 1 minuto)

```
python empire/tools/checkout.py --scadenza 2026-10-15
```
- Il comando **rifiuta date passate** (dal suo `--help`). La data è un default proposto (5
  settimane dal giorno uno, coerente col calendario di V3 §10 che mette E3 chiusa fra 4-6
  settimane); Max la cambia se vuole. Senza questo passo la pagina di pagamento mostra un conto
  alla rovescia scaduto da luglio — è la prima cosa che un cliente vede.

### 2.4 — Caricare i primi 5 pezzi (Max, 30-45 minuti)

I 5 pezzi sono scelti fra i 26 caricabili con un criterio scritto: **i più recenti del flusso
`VIDEO-PRONTI`** (hanno già `video.mp4` + `copy.md` + `metadata.json`, V2 memoria «Flusso
video: VIDEO-PRONTI/video-NN, uno alla volta», e la copertina la fa Max — regola bloccata nel
codice). I 16 pezzi ROSSI da 139-143 giorni in `Lancio corso skill beast/Page/Leo/da pubblicare`
**non** sono i primi 5: sono file `.mp4` sciolti senza copy né metadata, vanno in E8 con il loro
kit.

| # | ID esatto per `--segna` (forma `<percorso deposito>/<cartella>`, `ultimo_metro.py:205`) | Stato oggi |
|---|---|---|
| 1 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-07` | VERDE, 7 gg, 188 MB, caricabile |
| 2 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-06` | VERDE, 7 gg, 207 MB, caricabile |
| 3 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-05` | VERDE, 8 gg, 262 MB, caricabile |
| 4 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-04` | VERDE, 10 gg, 203 MB, caricabile |
| 5 | `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-01` | GIALLO, 19 gg, 275 MB, caricabile — il più vecchio del flusso vivo |

Per ognuno, nell'ordine:
1. Aprire la cartella (`YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-NN/`): dentro `video.mp4`,
   `copy.md` (titolo, descrizione, tag già scritti), `metadata.json`, e la copertina se Max l'ha
   già fatta (se manca, la fa ora: brief in `copy.md`, regola «la copertina la fa Max»).
2. Caricare su YouTube Studio come **Privato** (è il flusso stabilito: consegna automatica →
   copertina di Max → upload privato). Titolo/descrizione/tag da `copy.md`. **Nella descrizione,
   il link al prodotto lo aggiunge E0.9** (passo 3 di `04-E0.9-ATTO-DI-VENDITA.md`): se Max lo ha
   già sotto mano (`https://buy.stripe.com/<BASE>` dal passo 2.1), lo mette subito — risparmia un
   secondo giro.
3. Segnare il pezzo come uscito, così esce dalla lista e non viene ricaricato:
   ```
   python scripts/ultimo_metro.py --segna "YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI/video-07"
   ```
   (scrive `company/Memory/pubblicati.json`, `ultimo_metro.py:364-366`).

Un pezzo che fallisce l'upload (file corrotto, quota YouTube) **non ferma i successivi**
(fail-open): si segna nel checkpoint quale, e si passa al prossimo.

### 2.5 — Rileggere il conto

```
python scripts/ultimo_metro.py
```
Atteso: `26 caricabili subito` → **21** (o 22-25 se un upload è fallito: il numero vero si scrive
in §6, non quello sperato).

---

## 3. Il gate — comando, condizione di fallimento, exit code (L9)

```
# G1 - la cassa esiste (tier 1): entrambi i rail Stripe attivi con URL veri
python empire/tools/checkout.py --check
#   PASSA se stampa "tier 1" e NON elenca stripe_base/stripe_bump fra i "non attivi"
#   FALLISCE se resta "tier 2" (exit 0 comunque: il comando non fallisce, LEGGE l'output)

# G2 - la scadenza non e' nel passato
python -c "import json,datetime as d;c=json.load(open('Crea siti/Siti CCM/checkout.config.json'));s=c['scadenza_lancio'];import sys;sys.exit(0 if s>=d.date.today().isoformat() else 1)"
#   exit 0 = scadenza futura · exit 1 = ancora scaduta

# G3 - cinque pezzi usciti
python scripts/ultimo_metro.py | grep -E "^\s+[0-9]+ caricabili subito"
#   PASSA se il numero e' <= 21 (era 26 il 2026-09-11)
python -c "import json;p=json.load(open('company/Memory/pubblicati.json'))['pubblicati'];import sys;sys.exit(0 if len(p)>=5 else 1)"
#   exit 0 = almeno 5 ID in pubblicati.json · exit 1 = meno di 5

# G4 - il gate INCASSO e' ancora FINTO, e lo si dichiara
python -m empire controllo
#   la riga INCASSO legge il booleano rails.stripe_base.attivo (V2 §21-E0 nota): dopo G1 la
#   mostra "pronta" — ma e' un flag, non una prova. Il gate VERO (HTTP ai due Payment Link)
#   nasce in 02-E0.5-AGGANCI.md passo 8. Qui si scrive nel checkpoint: "INCASSO verde per flag,
#   non ancora per HTTP".
```

**Condizione di chiusura di E0a:** G1 tier 1 **e** G2 exit 0 **e** G3 ≥ 5. G4 non blocca (è una
dichiarazione di onestà, non un gate — V2 §21-E0 lo diceva già).

---

## 4. Politica di guasto e piano di rientro

| Guasto | Politica | Cosa si fa | Cosa si dichiara |
|---|---|---|---|
| Stripe non fa creare il link (KYC incompleto, conto non verificato) | fail-open | si carica lo stesso i 5 pezzi (2.4); G1 resta rosso; E0.9 aspetta solo per l'aggancio | riga in `STATO-EMPIRE.md` in cima (ADR-026): «G1 di E0a fermo su KYC Stripe — gesto di Max», con cosa NON è fermo |
| `--accendi-stripe` scrive URL sbagliati | fail-closed sul config | `git checkout -- "Crea siti/Siti CCM/"` e rilancio con gli URL giusti | nel checkpoint |
| Un upload YouTube fallisce | fail-open | si passa al pezzo successivo; il fallito resta nella lista di `ultimo_metro` (non si segna) | quale pezzo, perché |
| `--segna` su un ID sbagliato (refuso) | fail-closed | aprire `company/Memory/pubblicati.json`, togliere la chiave errata a mano, rilanciare con l'ID copiato dall'output di `ultimo_metro.py` | nel checkpoint |
| Max non ha tempo oggi | non è un guasto | §0: tutto il resto procede; E0a si fa il giorno che Max ha un'ora | riga in STATO-EMPIRE: «E0a rimandata a <data>, nulla fermo» |

**Il danno peggiore possibile di E0a:** zero. Non tocca motori vivi, non tocca chiavi, non tocca
clienti. È per questo che V3 §2 l'ha separata da E0b: la rotazione delle chiavi può spegnere
l'unico motore che contatta clienti veri (V2 §21-E0 ⚠️); caricare cinque video no.

---

## 5. Le forze — chi fa cosa, e il prompt d'ingaggio già scritto

**Nessuna forza.** Sono mani di Max (Stripe, YouTube Studio) più tre comandi che Max o EMPERATOR
lanciano in un minuto. Delegare a uno scagnozzo il caricamento su YouTube Studio non si può (serve
il login persistente di Max) e non serve.

**Unica delega possibile, e solo se Max la chiede:** EMPERATOR lancia 2.2, 2.3 e i cinque `--segna`
dopo che Max ha fatto i gesti sui pannelli e ha incollato i due URL in chat.

---

## 6. Cosa si scrive in Memory alla chiusura

- **Checkpoint:** `python scripts/checkpoint.py cp --titolo "E0a chiusa: 2 Payment Link vivi (tier 1), 5 pezzi fuori, scadenza lancio spostata"` — con dentro: i due URL (sì, sono pubblici per natura: un Payment Link è fatto per essere condiviso), i 5 ID segnati, il numero vero di caricabili dopo (21 atteso), gli upload falliti se ce ne sono, e la riga «INCASSO verde per flag, non per HTTP — il gate vero è E0.5 passo 8».
- **Riga per `STATO-EMPIRE.md`** (in cima): `## ✅ <data> — E0a: la cassa esiste (tier 1) e i primi 5 pezzi sono fuori — CP-...` + il numero di caricabili prima/dopo.
- **ADR:** nessuna. Il prezzo usato (67/97/27) è il default già sul disco; se Max lo cambia, la decisione si registra in E0.9, non qui.
- **I sei numeri del cruscotto (V2 §23), prima e dopo:**
  - `controllo x/6`: prima **2/6** (2026-09-10) → dopo: **3/6** atteso (INCASSO passa a flag verde)
  - `OPERATIVO %`: **61/439 = 13,9%** (invariato: E0a non tocca agenti)
  - `tracce (origine=hook)`: **0** (invariato: l'origine `hook` nasce con F3)
  - `byte entrate.jsonl`: **0** (invariato: la prima vendita è un esito di mercato, E0.9/E8)
  - `pezzi fermi (ultimo_metro)`: prima **31 fermi / 26 caricabili** → dopo **26 fermi / 21 caricabili** attesi
  - `vivo%`: non calcolabile (il comando nasce in E0.5)
