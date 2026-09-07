# ADR-024 — Canone v2, primo strato: cosa entra dalle onde A e B

- **Stato:** ATTIVO
- **Data:** 2026-09-07
- **Ordinato da:** Max — *"vai continua"* (checkpoint EMP-J8X2), dentro l'ordine permanente
  *"si prende tutto da tutti"*
- **Dossier:** `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` (lo studio) ·
  `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` (dove finisce)
- **Legge che cambia:** `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` — **si aggiungono §11 e §12**
- **Nasce da:** onda A (9 pagine) e onda B (8 pagine) dello studio totale, catturate e misurate il
  2026-09-07
- **Sostituisce:** niente. **Estende** ADR-023.

---

## 1. Il fatto che obbliga a decidere

Il pre-mortem dell'esecuzione, scritto stamattina, ha misurato questo:

> **`reports/` conteneva 16 documenti e ~2.400 righe. In `CLAUDE-SITI.md` i riferimenti a tutto
> l'ecosistema studiato erano 5 righe. Rapporto fra ciò che sappiamo e ciò che la Fabbrica ha
> incassato: circa 1 a 400.**

Il modo di rottura era già scritto nel piano — *"torno a trattare il tutto come dodici documenti"* —
ed è accaduto lo stesso. Un rischio previsto a parole e non presidiato da un gate **non è
presidiato**. Questo ADR è il presidio: **nessuna onda si chiude senza travaso nella legge.**

---

## 2. Cosa entra nella legge (due articoli nuovi)

### §11 — La cassa ha un gradino

**Misurato su `andrei-copy.com/outfunnel-1` e `/armadeggon-strp` (catture 28 e 27, 2026-09-07).**
Un prodotto one-shot non manda mai dal bottone di vendita direttamente al pagamento. In mezzo sta
una pagina di pre-cassa, alta meno di uno schermo e mezzo (1.512 px e 1.752 px misurati), con una
forma fissa:

| Ordine | Elemento | Testo misurato |
|---|---|---|
| 1 | occhiello in corsivo | «Stai acquistando…» |
| 2 | nome del prodotto, grande | «outFunnel», 68,3 px |
| 3 | istruzione + **codice sconto** | «Ricorda di usare il codice sconto "CWSHOP" per avere il 20% di sconto.» |
| 4 | cifra isolata | «98,00 €», 35,2 px |
| 5 | condizione | «Una tantum» |
| 6 | bottone | «Acquista outFunnel» |

**La regola, e il perché.** Il codice sconto vive **lì e non prima**: messo nella pagina di vendita
abbassa il prezzo percepito mentre il lettore sta ancora decidendo; messo dopo il clic, toglie
attrito quando ha già deciso. «Una tantum» attaccato alla cifra uccide il sospetto
dell'abbonamento nel punto esatto in cui nasce.

**Il difetto da non copiare:** «CWSHOP» è pubblico e permanente su una pagina indicizzabile. Uno
sconto che c'è sempre non è uno sconto, è il prezzo — il listino vero di outFunnel è 78,40 €.
Nella Fabbrica il codice della pre-cassa è **a scadenza o legato alla sessione**, mai eterno.

### §12 — L'accento si spende una volta

**Misurato su quattro pagine dello stesso guscio (catture 24, 25, 27, 28).** Guscio identico —
fondo `#a8a8a8`, testo `#fafafa`, piede `#ebe9e0` — e su ognuna **un solo colore d'azione, con
conteggio d'uso nel DOM pari a 1**:

| Pagina | Accento | Usi | Su cosa |
|---|---|---|---|
| `/define` | `#efab00` | 1 | la parola «copywriting» |
| `/asa` | `#06a506` | 1 | la parola «monetizzare» |
| `/outfunnel-1` | `#13989a` | 1 | le tre lettere «out» del nome |
| `/armadeggon-strp` | nessuno | 0 | — |

**La regola.** Una pagina accende **un** accento e lo spende su **una** parola: quella che porta i
soldi, non quella che descrive il mestiere (su `/asa` è evidenziato *monetizzare*, non
*copywriting*). Il canone diceva «colore d'azione sotto il 10%»; qui la misura è
**un'occorrenza su quattordici, il 7%**, e il risultato è più forte di qualunque bottone acceso.

---

## 3. Cosa entra come pattern (due nuovi, entrambi con due usi)

La legge §10 dice: *due usi = pattern*. Entrambi lo soddisfano.

| Pattern | Dimostrato da | Cos'è |
|---|---|---|
| `pre-cassa` | `/outfunnel-1` · `/armadeggon-strp` | il gradino di §11, in forma costruibile |
| `pagina-ponte` | `/define` · `/asa` | una sezione, un video, **un solo bottone**, zero prezzo, zero prova (35-36 blocchi di testo contro i 259 di una pagina di vendita). Serve a spostare, non a convincere. Porta dentro la riga di controllo del consumo: *«Ti consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.»* |

Restano **in attesa di un secondo uso** (registrati, non ancora pattern): il calcolatore/diagnostico
data-driven di `apsales.eu` — struttura `{title, steps, constraint, effect}`, la Teoria dei Vincoli
resa componente — e il blocco di copy *«Lavori da solo? Vale lo stesso. Al posto del team, il
vincolo sei tu.»*, riusato identico su `/servizi` e `/consulenza` (prova che AP Sales stessa lo
tratta come pezzo di libreria).

---

## 4. Cosa entra nel gate (quattro controlli, per `gate_siti.py`, Fase 4)

1. **Gradino di cassa:** se il sito vende un prodotto one-shot e il bottone d'acquisto porta dritto
   al pagamento, FAIL finché non è dichiarata la deroga con motivo.
2. **Accento speso una volta:** il colore d'azione compare più di N volte nel DOM → WARN con il
   conteggio (soglia da fissare in `canone.json`).
3. **Coerenza `og:image`:** stessa immagine social su più pagine con `meta.description` diverso →
   FAIL. *(difetto misurato su tutte e tre le pagine di `apsales.eu`: stesso placeholder targato
   `lovable.app`.)*
4. **Onestà dell'input:** una sezione con campi editabili in cui un campo non entra nel calcolo
   mostrato → FAIL. *(difetto misurato nel calcolatore ROI di `apsales.eu/landing-page`.)*

I controlli 3 e 4 nascono da **difetti veri trovati addosso a un concorrente**, non da teoria: è la
regola dei quattro strati — anche i difetti degli altri diventano gate.

---

## 5. Cosa NON entra, e perché

- **Lo stack di `apsales.eu`** (React + TanStack Start): è un gradino sopra il nostro per le pagine
  con stato server, ma ADR-023 ha già deciso le due corsie e non si riapre per una pagina di
  servizio. Registrato, non adottato.
- **L'architettura «un solo kit condiviso»** di `apsales.eu` (un modulo con `Section`-a-tono,
  Heading, Deck, Card, Button×2, Highlight×2, Footer, importato da ogni pagina, zero stili scritti
  a mano nelle sezioni): **entra nella Corsia B come struttura di scaffolding**, non come articolo
  di legge — §1 già dice la stessa cosa sui valori, e un articolo che ripete un articolo indebolisce
  entrambi.
- **Il rispetto sistematico di `prefers-reduced-motion`** trovato su ogni animazione di apsales:
  è già §7. Vale come **conferma esterna** che l'articolo è giusto, non come articolo nuovo.

---

## 6. Cosa si rompe

- Il gate non esiste ancora (Fase 4): i quattro controlli sono **debito dichiarato**, non attivi.
  Finché il gate non c'è, §11 e §12 valgono come legge letta dagli agenti, non come blocco automatico.
- I pattern nuovi portano la galleria da 8 a 10: `scripts/galleria.py` va rilanciato dopo la loro
  scrittura, o la galleria diventa un puntatore stale.

---

## 7. Come si verifica che questo ADR sia stato applicato

```
python "competitor/Andrei Pascu/site-study/scripts/stato_onde.py"
grep -c "§11\|§12" .claude/skills/fabbrica-siti/CLAUDE-SITI.md
ls .claude/skills/fabbrica-siti/pattern/pre-cassa .claude/skills/fabbrica-siti/pattern/pagina-ponte
```

---

## Connessioni
- [[ADR-023-fabbrica-siti-due-corsie]] — la decisione che questo ADR estende
- [[PRE-MORTEM-ESECUZIONE]] — la misura 1:400 che ha reso obbligatorio il travaso
- `competitor/Andrei Pascu/site-study/reports/24-25-27-28-macchina-del-funnel.md`
- `competitor/Andrei Pascu/site-study/reports/18-20-apsales-servizi-COSTRUZIONE.md`
- `competitor/Andrei Pascu/site-study/reports/18-20-apsales-servizi-COPY.md`
