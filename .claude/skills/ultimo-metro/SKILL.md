---
name: ultimo-metro
description: "Trova tutto il lavoro di Digital Empire che e' finito ma non e' mai uscito - libri pronti mai caricati su Amazon, video montati mai pubblicati, caroselli fatti e mai usciti - e dice da quanti giorni e' fermo e cosa manca a ciascuno per uscire. Usala quando serve sapere cosa pubblicare oggi, quando si apre una sessione di lavoro e non si sa da dove partire, quando qualcuno chiede perche' l'azienda produce e non vende, o dopo aver finito un pezzo di contenuto per verificare che sia davvero uscito. Collega i pezzi pronti ai pubblicatori che gia' esistono in casa."
---

# ULTIMO METRO

> **Il problema che questa skill esiste per risolvere.**
> Digital Empire produce e non pubblica. Misurato il 2026-09-03: **25 pezzi finiti mai
> usciti, 2.137 MB di lavoro fermo, il piu' vecchio da 135 giorni.** Cinque libri completi
> di manoscritto, copertina e dati per Amazon, con la cartella `libri_pubblicati/` vuota.
> Sedici video in una cartella che si chiama, testualmente, `da pubblicare`, tre dei quali
> si chiamano *"Il nuovissimo pronto per la pubblicazione"*.
>
> **Non e' un problema di produzione: la macchina produce benissimo.** Non e' nemmeno un
> problema di strumenti: `social-publisher` e `workflow-pubblicazione-auto` funzionano.
> Il problema e' che **nessuno guardava**. Il lavoro finito era invisibile.

---

## 1. COSA FA

Apre i depositi dove si accumula il lavoro finito, riconosce cosa e' completo, incrocia
con il registro di cio' che e' gia' uscito, e restituisce **la lista di cosa caricare oggi**,
ordinata dal piu' vecchio — perche' il piu' vecchio e' quello che ci sta costando di piu'.

**Non pubblica niente.** Vede, e riferisce. La pubblicazione resta una decisione di Max,
e passa dai pubblicatori che gia' esistono (§4).

---

## 2. COME SI USA

```bash
# la lista di cosa e' fermo, a schermo
python scripts/ultimo_metro.py

# la stessa lista, scritta anche in company/Memory/ULTIMO-METRO.md
python scripts/ultimo_metro.py --scrivi

# quando un pezzo e' stato caricato davvero, si segna e sparisce dalla lista
python scripts/ultimo_metro.py --segna "percorso/deposito/nome-del-pezzo"
```

Il registro di cio' che e' uscito vive in `company/Memory/pubblicati.json`.
**Segnare e' obbligatorio**: se non si segna, il pezzo ricompare per sempre e la lista
smette di essere credibile. Una lista che mente non la guarda piu' nessuno.

---

## 3. COME LEGGERE IL RAPPORTO

| Semaforo | Significa |
|---|---|
| `[ROSSO]` | fermo da **60 giorni o piu'** — sta gia' costando |
| `[GIALLO]` | fermo da **14-59 giorni** — sta scivolando |
| `[VERDE]` | fermo da meno di 14 giorni — normale |

Il rapporto divide in due:

- **CARICABILI ADESSO** — non manca niente, si caricano oggi
- **MANCA UN PEZZO** — dice esattamente cosa manca (la copertina, il manoscritto, i dati
  per il negozio). Spesso e' mezz'ora di lavoro per sbloccare un mese di produzione ferma.

---

## 4. DOVE VANNO I PEZZI PRONTI — i pubblicatori esistono gia'

**Non costruire un nuovo pubblicatore.** Questa skill e' l'occhio, non la mano.
Quando un pezzo e' pronto, va a uno di questi, che sono gia' in casa e funzionano:

| Cosa | Chi lo pubblica | Come |
|---|---|---|
| Carosello / post Instagram, TikTok | skill `social-publisher` | `check_ready.py` poi `push_social.py --brand <digital-empire\|mentalita-brutale>` |
| Contenuto quotidiano multi-marca | skill `workflow-pubblicazione-auto` | il suo flusso, marca per marca |
| Video YouTube | `YOUTUBE-AUTOMATION-FACTORY` | il suo flusso di caricamento |
| Libro | **Amazon KDP, a mano** | ⚠️ nessun caricatore automatico esiste oggi (§6) |

---

## 5. I DEPOSITI SORVEGLIATI

Vivono in cima a `scripts/ultimo_metro.py`, nella lista `DEPOSITI`.
Ad oggi sono tre:

1. `company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/LIBRI/libri_pronti` → Amazon KDP
2. `YOUTUBE-AUTOMATION-FACTORY/VIDEO-PRONTI` → YouTube
3. `Lancio corso skill beast/Page/Leo/da pubblicare` → YouTube / Social

**Per sorvegliarne uno nuovo** si aggiunge una voce alla lista `DEPOSITI`: percorso, tipo,
canale, quali file servono perche' il pezzo sia "finito". Nient'altro da toccare.

Se un deposito sparisce (cartella spostata o rinominata) lo script **lo dichiara** invece di
tacere: un puntatore vecchio manda a sbattere, e qui non si tace mai su un puntatore rotto.

---

## 6. LIMITI NOTI — dichiarati, non nascosti

- **L'eta' e' quella dell'ultimo tocco, non della fine del lavoro.** Un pezzo finito ad
  agosto e sfiorato ieri (anche solo da un `git checkout`) risulta fermo da un giorno.
  Il semaforo va letto come **soglia di allarme**, non come data anagrafica certa.
- **"Finito" e' misurato sui file presenti, non sulla qualita' del contenuto.** Un libro
  con pdf, epub, copertina e dati per il negozio risulta al 100% anche se il testo dentro
  fosse da riscrivere. Il giudizio sulla qualita' spetta alle sentinelle, non a questa skill.
- **⚠️ VUOTO DI CONOSCENZA: non esiste oggi un caricatore automatico per Amazon KDP.**
  I libri vanno caricati a mano dal pannello KDP. Costruirlo o rinunciarci e' una decisione
  di Max che non e' ancora stata presa.
- **I caroselli non sono ancora sorvegliati**: sono sparsi in cartelle senza uno schema
  comune (`KDP - prodottti digitali/LIBRO */Caroselli/`, e altre). Serve prima decidere
  dove vive un carosello finito, poi aggiungere il deposito.

---

## 7. QUANDO ESEGUIRLA

- **All'inizio di una sessione di produzione** — prima di fabbricare il pezzo numero 26,
  guarda i 25 fermi. Fabbricarne un altro mentre 25 marciscono non e' produttivita': e'
  il modo piu' elegante di non pubblicare.
- **Dopo aver finito un contenuto** — per verificare che sia arrivato nel deposito giusto.
- **Nel rapporto settimanale** — il numero di pezzi fermi e l'eta' del piu' vecchio sono
  due indicatori di salute dell'azienda tanto quanto il fatturato.

---

## 8. LEGAMI

- **ADR-016** — l'organo Ultimo Metro (`company/Memory/decisions/`)
- **Mandato Art. 2** — verita' sull'Impero: prove, non promesse. Questa skill produce prove.
- **`coo-empire`, `cro-empire`, `ceo-empire-conductor`** — il problema dell'ultimo metro
  e' scritto nei loro file come problema numero uno del loro perimetro
- **`social-publisher`, `workflow-pubblicazione-auto`** — le mani, di cui questa e' l'occhio

---

*Creata il 2026-09-03 su ordine di Max, dopo la misurazione che ha reso visibile il collo
di bottiglia dell'azienda. Origine: due indagini indipendenti arrivate alla stessa conclusione.*
