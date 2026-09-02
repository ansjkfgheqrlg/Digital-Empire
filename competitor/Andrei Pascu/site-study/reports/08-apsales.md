---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #site-study #agenzia #cro #b2b #copy-teardown #concorrente-diretto
Created: 2026-09-02
Last updated: 2026-09-02
---

# STUDIO SITO 08 — apsales.eu (agenzia CRO B2B/SaaS)

**URL:** https://apsales.eu/
**Titolo SEO:** `Agenzia CRO per B2B e SaaS | AP Sales`
**Meta:** *"AP Sales è l'agenzia di Conversion Rate Optimization per B2B e SaaS: landing page, tracciamento e statistica per abbassare il CPL e alzare il ritorno delle ads."*
**Prezzi:** **nessuno in pagina** — solo dentro la FAQ (`Quanto costa?`)
**Altezza:** 12.565px desktop · 15.354px mobile (+22,3%) · **Blocchi:** 168 · **CTA:** 12 · **Media:** 50
**Catturato:** 2026-09-01 — 14 slice desktop 1440×900 + 19 mobile 390×844
**Fonti grezze:** `capture/08-apsales/`

> 🔴 **Questo è il concorrente diretto dell'agenzia di Digital Empire.** Non un adiacente: la stessa cosa. Agenzia di Conversion Rate Optimization italiana, target B2B/SaaS, servizio landing page + consulenza, niente retainer, garanzia sul lavoro. È anche **l'unica pagina dell'intero ecosistema Andrei Pascu costruita con un design system vero** — e l'unica che offre una garanzia.

---

## 1. LE TRE COSE CHE CAMBIANO TUTTO RISPETTO ALLE ALTRE 7 PAGINE

### 1.1 Qui esiste una garanzia. Sulle pagine info-prodotto non esiste mai.
Misurato: su `funnel-operator`, `outheadline`, `outfunnel`, `copy`, `manuale-del-copywriter`, `claude-speedrun` — **zero garanzie di rimborso**. Qui, dentro la card del servizio landing page:

> *"Se le conversioni non aumentano, **rimettiamo mano alla pagina. Gratis, a condizioni chiare.**"*

e ripetuta nella tabella comparativa (`Modifiche se la pagina rende poco → ✓ Sì, incluse`) e nella FAQ (`E se le conversioni non aumentano?`).

**Non è una garanzia di rimborso: è una garanzia di lavoro.** Non restituisce soldi, restituisce ore. Per un'agenzia è la forma più difendibile: il costo marginale di rimettere mano a una pagina è tempo, non cassa, e chi la accetta non chiede il rimborso — chiede il lavoro.
**Regola estratta:** *il B2B compra la garanzia di rimedio, il B2C compra la garanzia di rimborso.* Andrei tratta i due mercati con due strumenti diversi, coscientemente.

### 1.2 L'etica è un asse competitivo, non un valore dichiarato
La parola *etica* compare nell'headline di sottotesto (*"numeri e **persuasione etica**"*), poi diventa una **riga della tabella comparativa**:

| | AP Sales | Agenzia generalista | Freelancer | Team interno |
|---|---|---|---|---|
| Timer finti, recensioni finte, dark pattern | **✓ Mai** | ✕ Alcune sì | ✕ Capita | ~ Dipende da chi assumi |

e chiude la pagina come ultima riga assoluta, sotto la CTA finale: *"Nessun impegno. **Niente countdown finti.**"*

**Perché è forte:** trasforma un'affermazione morale (non verificabile) in una **specifica di prodotto** (verificabile: apri la pagina e guarda se c'è un countdown). Chi lo dice a parole fa branding; chi lo mette in una riga di tabella accanto ai concorrenti fa posizionamento.

### 1.3 Il sito è tecnicamente un'altra azienda
| | andrei-copy.com | **apsales.eu** |
|---|---|---|
| Costruito con | Squarespace | build custom (colori `oklch`, stack tipo Tailwind v4) |
| Raggi | 10px + 6 valori di deriva | **solo `50%`** su 2 elementi — **tutto il resto è a spigolo vivo** |
| Font | 5 famiglie, `body: sans-serif` | 4 famiglie coerenti, `body: Elza, Inter, ui-sans-serif…` |
| Banner "stiamo aggiornando il brand" | **sì** | **no** |
| Colori | hex fissi | `oklch` / `oklab` con scala di opacità |

Come `claude-speedrun.com` (report 07): **quando Andrei fa sul serio, lascia Framer/Squarespace e costruisce.** Ora sono due su nove. Non è più un'eccezione, è un pattern: i due prodotti recenti hanno un design system, i sette storici no.

---

## 2. PALETTE — misurata

Il sito usa **`oklch`/`oklab`**, non hex. Conversioni indicative in fondo alla tabella.

### Testo
| Colore | Usi | Equivalente | Ruolo |
|---|---|---|---|
| `oklch(0.9821 0 0)` | **273** | ≈ `#fafafa` | Bianco-carta: **il testo di default** |
| `oklab(0.9821 0 0 / .45)` | 27 | bianco 45% | Etichette mono 11px |
| `.5` / `.35` | 19 + 19 | | Testo terziario, colonne dei concorrenti nella tabella |
| `.6` | 16 | | Corpo secondario |
| `oklch(0.556 0.2453 261.33)` | **13** | **≈ `#0062ff`** | **Il blu di sistema**: numeri 01-04, frecce, accenti |
| `.7` | 12 | | Corpo |
| `oklch(0.2273 0.0038 286.09)` | 6 | ≈ `#37373d` | Testo scuro nella sezione chiara |

**19 livelli di opacità dello stesso bianco.** Non è una palette: è **una scala di gerarchia costruita sull'alfa**. Un solo colore di testo, dodici pesi di presenza. È il modo più economico di gerarchizzare senza introdurre colori.

### Sfondi
| Colore | Usi | Equivalente | Ruolo |
|---|---|---|---|
| `oklch(0.1448 0.002 285)` | **20** | ≈ `#0a0a0c` | Nero-blu: il fondo dominante |
| `oklch(0.556 0.2453 261.33)` | **13** | **≈ `#0062ff`** | Bottoni primari + **footer a tutta pagina** |
| `oklch(0.1776 0 0)` | 10 | ≈ `#131313` | Card, un gradino sopra il fondo |
| `oklab(0.556 … / .04)` e `/.08` `/.1` | 9 | blu al 4-10% | Velo blu sulle celle vincenti della tabella |
| `oklch(0.9821 0 0)` | 2 | `#fafafa` | **La sezione team, invertita** |

**Il blu `#0062ff` regge da solo tutta la marca.** È lo stesso blu dell'hub `andrei-copy.com` (scoperta trasversale #1: il blu è il colore dell'azione dell'ecosistema), qui però non è un accento fra tanti: **è l'unico colore della pagina**. Tre soli usi che contano: bottoni, numeri di processo, footer.

**La mossa più raffinata:** le celle della colonna *AP Sales* nella tabella comparativa hanno un fondo blu al **4%** (`oklab(0.556 … / 0.04)`). Non si vede come colore — si vede come **una colonna che sta un millimetro più avanti delle altre**. La preferenza è suggerita dal contrasto, non dichiarata.

---

## 3. TIPOGRAFIA — la scoperta più imitabile della pagina

**Famiglie: 4.**
| Font | Usi | Dove |
|---|---|---|
| **`DM Mono`** | **240** | **Il font più usato della pagina** |
| `Elza, Inter, ui-sans-serif…` | 109 | Titoli e corpo (è il font del brand) |
| `Plus Jakarta Sans` | 73 | Corpo secondario |
| `DM Sans` | 13 | Tutti i bottoni |

**Il font dominante di un'agenzia di CRO è un monospaziato.** 240 usi su 435. Non per il codice: per le **micro-etichette** (`GA4`, `Meta Pixel`, `Clarity`, `GTM`, `Consent Mode`, `Heatmap`, `Session replay`, `Scroll depth`, `Funnel`, `Copy`, `Design`, `Dev`, `A/B test`, `Baseline`, `CVR`, `CPL`, `ROAS`, `Attenzione`, `Click`, `Scroll`, `Rage click`, `Uscite`) e per i numeri.

**Perché è la mossa più intelligente del sito:** il monospaziato è il font degli strumenti di misura — terminali, log, fogli di calcolo, dashboard. Usarlo per le etichette significa dire *"qui si misura"* **senza scriverlo**. L'headline dice *"Metodo statistico. Non opinioni."*; il font lo dimostra 240 volte prima ancora che tu legga l'headline.

### Scala misurata
| Dimensione | lh | Peso | Usi | Ruolo |
|---|---|---|---|---|
| **80px** | 76,8 | 600 / **900** | 4 + 2 | Hero e CTA finale — il 900 solo sulla parola in corsivo |
| 60px | 60 | 600 / **900** | 13 + 4 | H2 di sezione |
| 45px | 45–48,6 | 400 / 600 / 700 | 5 | Il paragrafo-manifesto centrato |
| 34px | 39,1 | 600 | 10 | H3 e domande FAQ |
| 25px | 31,25–35 | 700 / 400 | 21 | Titoli di card, numeri di processo |
| 22,3px | 33,5 | 500 | 4 | Etichette dei guerrieri |
| 17px | 27,2 | 400–700 | 37 | Corpo principale |
| 15px | 22,5 | 400 / 500 | **94** | Corpo delle liste, celle di tabella, footer |
| **12,96px** | 12,96 | 400 | **218** | **DM Mono: il livello più usato in assoluto** |
| 11px | 14,3 | 500 | 22 | Chip mono dentro le card |

**Pesi:** 400 (320) · 500 (57) · 600 (31) · 700 (21) · **900 (6)**.
**Il grassetto vero (900) esiste 6 volte in 12.565px**, e sempre sulla stessa figura retorica: la parola in **corsivo nero** dentro un titolo (*convertono*, *soluzione*, *due cose*, *Nessuno dei tre.*, *Standard alti*, *lavorare insieme*). Un solo effetto tipografico, ripetuto sei volte, sempre sulla parola che porta il senso.

Contro le pagine info-prodotto: lì il grassetto è al 60-80% dei blocchi, qui il peso dominante è **400 al 74%**. **Il B2B si scrive leggero.**

### Raggi
`50%` × 2. **Nient'altro.** Zero border-radius su bottoni, card, tabelle, input. Su un mercato dove ogni SaaS ha angoli da 12px, lo spigolo vivo è una firma — e costa zero.

---

## 4. STRUTTURA E POSIZIONE DEGLI ELEMENTI

| y (px) | % | Sezione | Note di layout |
|---|---|---|---|
| 0–64 | 0% | **Nav**: logo APsales a sinistra · `Carriere` + `Menu ☰` a destra, due bottoni fantasma bordati | Nessun link di navigazione esposto: il menu è chiuso |
| 177–402 | 1–3% | **H1 80px su 4 righe** — `convertono` in corsivo 900 | Colonna sinistra, x=184 |
| 223–581 | 2–5% | **Occhio in ASCII/inchiostro** 358×358 (`/ascii/occhio.webp`) | Colonna destra |
| 605–790 | 5–6% | **Mini-tabella KPI**: `CVR ↑ più conversioni` (blu) · `CPL ↓ costo per lead` · `Spesa in ads = la stessa` | Sotto l'immagine, righe divise da filetti |
| 720–780 | 6% | **CTA doppia**: `Voglio aumentare le conversioni →` (blu pieno 340×58) + `Vedi i servizi` (fantasma 163×60) | |
| 812 | 6% | **Riga di qualificazione**: *"Solo per B2B e B2B SaaS che investono da €5.000 a €100.000 al mese in ads."* | 17px al 50% di opacità |
| 1003–1600 | 8–13% | **Scena dei 5 guerrieri** spartani (`/warriors/w2…w6.webp`) etichettati `design` · `statistica` · **`APsales`** · `vendita` · `persuasione`, collegati da linee tratteggiate; campo di rumore ASCII sullo sfondo; globo 3D 158×158 in alto a destra | La sola sezione puramente iconografica |
| 1812–1930 | 14–15% | **Fila loghi clienti** (10 loghi, h=48px, marquee) + *"Si fidano di noi aziende in Italia e in Europa."* | |
| 2156–2250 | 17% | **Paragrafo-manifesto 45px centrato** | Unico blocco centrato della pagina |
| 2744–3250 | 22–26% | **Il problema / La soluzione** — due colonne speculari, 3 bullet ciascuna | Bullet quadrati blu a destra |
| 3300–3450 | 26–27% | **3 card KPI**: `Spesa pubblicitaria = La stessa` · `Costo di acquisizione ↓ Più basso` · `Ritorno sulle ads ↑ Più alto` | Frecce blu 36px |
| 3699–4861 | 29–39% | **"Facciamo solo due cose. Per scelta."** → 2 card servizio (Landing page · Consulenza), 3 bullet + CTA fantasma ciascuna | |
| 5189–5700 | 41–45% | **"Metodo statistico. Non opinioni."** → 4 step numerati `01`–`04` in blu, ognuno con chip mono | Griglia a 4 colonne |
| 5799–6100 | 46–49% | **"Quello che vediamo"** — wireframe di pagina con heatmap blu luminescente, 5 chip mono | Card a 2 colonne 50/50 |
| 6383–6800 | 51–54% | **"Non facciamo solo pagine. Orchestriamo la conversione."** → 3 colonne (Offerta · Coerenza ads ↔ pagina · Fiducia) | |
| 7075–7790 | 56–62% | **Tabella comparativa 4×6** | Colonna AP Sales con velo blu 4% |
| 8109–8800 | 65–70% | **Sezione team, invertita su `#fafafa`**: 3 numeri + foto founder 328×640 + 2 card verticali collassate (`Impatto`, `Team`, 64px di larghezza) | Unica sezione chiara |
| 9152–9400 | 73–75% | **"Deleghiamo. Ma mai a caso."** | |
| 9738–10500 | 78–84% | **FAQ**, 7 domande da 34px in accordion | |
| 10818–11200 | 86–89% | **CTA finale**: `Vediamo se ha senso lavorare insieme.` + `Parla con noi →` + *"Nessun impegno. Niente countdown finti."* | |
| 11400–12565 | 91–100% | **Footer blu pieno** con guerriero in **ASCII art**, wordmark gigante, 8 link, P.IVA, © 2026 | |
| **fisso** | — | **CTA flottante `Prenota una chiamata →`** 252×55, blu, ombra `0 16px 40px -12px rgba(0,0,0,.8)`, in basso a destra su **tutte** le schermate | |

**Griglia:** allineamento a sinistra su margine `x=184` (12,8% di 1440), colonne piene fino a `x=1256`. Nessun contenuto centrato tranne il paragrafo-manifesto. È l'opposto di `andrei-copy.com`, dove tutto è centrato.

---

## 5. COMPONENTI — inventario con misure

### 12 CTA, tre livelli gerarchici
| Livello | Esempio | Misure | Stile |
|---|---|---|---|
| **Primario** | `Voglio aumentare le conversioni →` (y=721) · `Parla con noi →` (y=11119) · `Prenota una chiamata →` (fisso) | 340×58 · 191×58 · 252×55 | Fondo blu, testo `#ffffff`, **raggio 0**, DM Sans 500 17px, padding 16/32 |
| **Fantasma** | `Vedi i servizi` · `Come funziona` · `Fai una consulenza` · `Conosci il team ↗` | 163–213 × 60 | Trasparente, bordo bianco al 25%, raggio 0 |
| **Utility** | `Carriere` · `Menu` | 91–103 × 40 | Bordo al 20%, 15px |

**Nessun raggio, nessun gradiente, nessuna trasformazione maiuscola su nessuno dei 12.** L'unica ombra dell'intera pagina è sotto la CTA flottante — che è anche l'unico elemento che deve staccarsi dal fondo.

**Le frecce sono parte del testo, non icone**: `→` dentro l'etichetta. Sopravvive a qualunque font, si copia-incolla, non richiede SVG.

### Media (50)
`occhio.webp` 358×358 · 5 `warriors/*.webp` (137–235 × 276–447) · 10 loghi cliente h=48 · video 158×158 (globo) · wireframe heatmap · **guerriero in ASCII art nel footer** · il resto SVG di interfaccia.
**Nessuna foto di prodotto, nessuno screenshot di dashboard, nessun grafico di risultato.** L'unica foto reale è il ritratto del founder.

### Le card verticali collassate — componente da rubare
Nella sezione team: la card `Founder` è aperta (328×640) e mostra la foto; accanto, `Impatto` e `Team` sono **collassate a 64px di larghezza con il titolo ruotato di 90°**. Tre schede, una aperta, due di taglio.
Costo: un contenitore flex e una `writing-mode`. Resa: densità informativa alta in orizzontale senza carosello, senza JS.

---

## 6. COPY — teardown sezione per sezione

### 6.1 Headline
```
Il traffico si compra. I clienti si convertono.
```
**Antitesi in due frasi da quattro parole.** La prima concede una verità che il cliente conosce già e su cui sta spendendo (il traffico si compra: è ciò che fa ogni giorno). La seconda sposta il problema dove l'agenzia lavora. Non promette risultati, **ridefinisce dove sta il problema** — che è la mossa di apertura corretta quando vendi un servizio a chi sta già comprando qualcos'altro (ads).

`convertono` in corsivo 900: l'unica parola pesante in quattro righe da 80px.

Sottotesto:
> *"Siamo AP Sales, agenzia di Conversion Rate Optimization. Usiamo **numeri e persuasione etica** per aumentare quante persone ti contattano e comprano, **con la stessa spesa pubblicitaria**."*

L'ultima clausola è tutta la proposta di valore: *stesso budget, più clienti*. Non chiede budget nuovo — cioè non compete con l'agenzia ads già in carico, si ci **affianca**. Per un'agenzia CRO è la posizione commerciale corretta: nessuno deve essere licenziato perché tu entri.

### 6.2 La riga di qualificazione
> *"Solo per B2B e B2B SaaS che investono da €5.000 a €100.000 al mese in ads."*

Subito sotto la CTA principale, al 50% di opacità. Fa tre cose insieme:
1. **Squalifica** chi è sotto i 5.000 €/mese (e sono la maggioranza di chi arriva da Instagram).
2. **Dichiara il prezzo senza dichiararlo**: chi spende 5-100k in ads sa quanto costa un'agenzia per quel volume.
3. **È una prova sociale implicita**: se il tetto è 100.000 €/mese, esistono clienti in quella fascia.

Nell'ecosistema info-prodotto lo stesso autore fa l'opposto (nessun filtro, si vende a chiunque). **Il filtro esiste solo dove il servizio è vincolato dal tempo delle persone.**

### 6.3 I 5 guerrieri
Cinque spartani con etichette collegate: `design` · `statistica` · **APsales** (il guerriero centrale, in armatura completa, più grande) · `vendita` · `persuasione`. Sfondo di rumore ASCII, globo 3D.

Il messaggio è: *l'agenzia è la somma di quattro discipline*. Lo dice senza una parola di copy — solo etichette. **Ma non regge l'esame che il sito stesso impone al cliente** (*"Creatività con un perché"*): i guerrieri non sono un'informazione, sono un'atmosfera. È l'unica sezione decorativa di un sito che ha costruito tutto il resto sul principio opposto. Rimane il pezzo più "info-marketer" di una pagina B2B.

### 6.4 Problema / Soluzione — colonne speculari 1:1
| Il problema | La soluzione |
|---|---|
| *Il CPL sale ogni trimestre. E la risposta di tutti è "spendi di più".* | *Prima il tracciamento compliant: GA4, Meta Pixel, Clarity. Poi le opinioni.* |
| *La tua pagina parla del tuo prodotto. Ma al cliente interessa il suo problema, non il tuo prodotto.* | *Copy e design costruiti su psicologia e standard di marketing. Creatività con un perché.* |
| *Le modifiche al sito si decidono con "a me piace il blu". Zero dati.* | *Ogni modifica confrontata con una baseline. Se non migliora, si cambia.* |

**Ogni problema è una frase che il cliente ha già pronunciato**, tra virgolette: *"spendi di più"*, *"a me piace il blu"*. Non descrive il problema: **cita il cliente**. È il livello di specificità che separa un copy generico da uno scritto dopo aver fatto call vere.

E la soluzione non promette risultati: promette **un ordine di operazioni** (*prima il tracciamento, poi le opinioni*). Vendere un metodo invece di un risultato è ciò che permette di non avere numeri di caso studio in pagina — vedi difetto #2.

### 6.5 *"Facciamo solo due cose. Per scelta."*
La restrizione di scopo come prova di competenza. Due servizi soli:

| Landing page | Consulenza con Andrei Pascu |
|---|---|
| *Audit e tracciamento compliant: GA4, Meta Pixel, Microsoft Clarity. Vediamo dove perdi conversioni, prima di scrivere una riga.* | *Riduci la confusione a un solo problema da risolvere in maniera permanente.* |
| *Analisi statistica di competitor, dati e storico → poi copy, design e sviluppo. **Go live in media in 25 giorni**.* | *Esci con un piano a step per il trimestre, sulle tue risorse reali: persone, budget, tempo.* |
| ***Se le conversioni non aumentano, rimettiamo mano alla pagina. Gratis, a condizioni chiare.*** | *Logica e **teoria dei vincoli**. Niente motivazione, solo decisioni.* |

Tre dettagli che valgono:
- **"Go live in media in 25 giorni"** — un numero di tempo verificabile al posto di un numero di risultato non verificabile. Se non puoi pubblicare i CVR dei clienti, pubblica la durata.
- **"prima di scrivere una riga"** — dichiara l'ordine, di nuovo. Il metodo è il prodotto.
- **"teoria dei vincoli"** (Goldratt) citata per nome in una card di vendita B2B: filtra chi non sa cos'è e certifica presso chi lo sa.
- **"Niente motivazione, solo decisioni"** — si separa esplicitamente dal suo stesso mondo (il formatore che motiva). Lo stesso movimento di *"Non un guru"*.

### 6.6 *"Metodo statistico. Non opinioni."* — i 4 step
`01 Tracciamo` → `02 Guardiamo` → `03 Costruiamo` → `04 Misuriamo`, numeri in blu, ogni step con una frase e i suoi strumenti in chip monospaziati.

| Step | La frase | Cosa fa davvero |
|---|---|---|
| 01 | *Strumenti compliant: GA4, Meta Pixel, Microsoft Clarity. **Prima di toccare qualsiasi cosa**.* | Mette la conformità prima della creatività: parla al legale del cliente |
| 02 | *Heatmap, registrazioni di sessione, dati delle ads. **Cosa fanno davvero le persone. Non cosa dicono nei meeting**.* | La frase migliore della pagina: chiunque abbia lavorato in un'azienda con più di 5 persone la riconosce |
| 03 | *Copy e design sulla base dei tuoi numeri. Psicologia e standard di marketing, applicati.* | |
| 04 | *Baseline concordata, CVR e CPL alla mano. **Se un'idea non regge i numeri, muore lì**.* | Include la possibilità che l'idea dell'agenzia sia sbagliata: costa nulla, vale molto |

**"Non cosa dicono nei meeting"** è l'appiglio politico interno: chi assume l'agenzia la userà per vincere una discussione interna. Scrivere per il compratore-in-azienda significa dargli l'argomento che userà con il suo capo.

### 6.7 La tabella comparativa — struttura da copiare
Quattro colonne (**AP Sales** · Agenzia generalista · Freelancer · Team interno), sei righe, tre simboli (`✓` `✕` `~`).

| Riga | AP Sales | Generalista | Freelancer | Team interno |
|---|---|---|---|---|
| Specializzati in CRO e landing page | ✓ Sì, facciamo solo questo | ✕ No, fanno tutto | ~ Raramente | ~ Da formare |
| Dati che puoi controllare | ✓ Sì, il tracciamento è tuo | ✕ Sei all'oscuro di cosa fanno | ~ Raramente | ~ Dipende dagli strumenti |
| Timer finti, recensioni finte, dark pattern | ✓ Mai | ✕ Alcune sì | ✕ Capita | ~ Dipende da chi assumi |
| Modifiche se la pagina rende poco | ✓ Sì, incluse | ✕ Solo se paghi | ✕ Solo se lo ritrovi | ~ Le fai tu |
| Costo fisso mensile | ✓ No, paghi una volta | ✕ Retainer | **✓ No** | ✕ Stipendio + oneri |
| Puoi parlarci ora | ✓ Sì, chiamata entro 24h | ✕ Form → newsletter | ~ Se risponde | ✕ Prima devi assumerlo |

**Tre scelte tecniche che la rendono credibile:**
1. **Non confronta con concorrenti nominati, ma con le tre alternative reali di acquisto** (agenzia generalista, freelancer, assumere). Chi valuta non sta scegliendo tra AP Sales e un'altra agenzia CRO: sta scegliendo *come risolvere il problema*. La tabella parla di quella decisione.
2. **Concede un punto all'avversario**: `Costo fisso mensile → Freelancer: ✓ No`. Un solo ✓ regalato converte la tabella da propaganda a confronto. È il dettaglio che fa leggere anche le altre cinque righe.
3. **Il terzo simbolo `~`** ("dipende", "raramente") evita il binario e rende le righe verosimili.

Titolo: *"Agenzia generalista, freelancer o assumere? **Nessuno dei tre.**"* — la domanda del cliente, e la risposta che crea una quarta categoria.

### 6.8 *"Piccola agenzia. Standard alti."* — la sezione invertita
Su fondo chiaro, la sola della pagina:
> *"Siamo **meno di 10 persone, per scelta**. L'AI ci dà la velocità di un team da 100. Il lavoro manuale lo teniamo dove decide la conversione: copy, analisi, decisioni."*
> *"AP Sales è fondata e diretta da Andrei Pascu. **Non un guru: uno che le pagine le scrive ancora**."*

Numeri: **250.000** follower organici · **100+** clienti seguiti · **1.500+** professionisti formati.

Tre mosse:
- **La piccolezza dichiarata come scelta** ("per scelta" compare due volte in pagina: qui e in "Facciamo solo due cose"). Anticipa l'obiezione "siete piccoli" e la converte in specifica.
- **L'AI dichiarata apertamente** come moltiplicatore, in una pagina B2B, nel 2026: *"velocità di un team da 100"*, con la delimitazione di dove resta l'uomo (copy, analisi, decisioni). Chi teme di comprare output automatico legge esattamente dove il lavoro è umano.
- **"Non un guru"** — attacca la categoria che lo ha reso noto. È la stessa figura del `manuale-del-copywriter` ("io non sono 'tanti autori'"), applicata a se stesso.

### 6.9 *"Deleghiamo. Ma mai a caso."*
> *"Su parte del lavoro ci appoggiamo a professionisti selezionati fuori dal team. Non è subappalto a basso costo: ognuno lavora dentro i nostri processi e le nostre SOP."*

**Dichiarare l'outsourcing invece di nasconderlo.** È l'obiezione numero uno contro le agenzie piccole; dirla per primi, con il nome tecnico della soluzione (SOP), la disinnesca. Nessuna delle altre otto pagine dell'ecosistema fa un'ammissione di questo tipo.

### 6.10 FAQ — 7 domande, tutte scomode
`Cos'è la CRO?` · `Con chi lavorate?` · `Che tipo di accordo offrite?` · **`E se le conversioni non aumentano?`** · **`Quanto costa?`** · **`Fate anche ads, social, SEO?`** · `Quanto tempo devo dedicarci io?`

Le tre in grassetto sono le domande che un'agenzia normalmente evita. `Fate anche ads, social, SEO?` esiste **per dire di no**: è la FAQ che difende il posizionamento "facciamo solo due cose". `Quanto tempo devo dedicarci io?` è l'unica che parla del costo non monetario — ed è quella che chiude i clienti B2B già oberati.

### 6.11 Chiusura
> **Vediamo se ha senso lavorare insieme.**
> *Chiamata conoscitiva: ci spieghi la tua impresa, ti diciamo dove la pagina perde clienti e se possiamo aiutarti. Risposta entro 24 ore.*
> `Parla con noi →`
> *Nessun impegno. Niente countdown finti.*

**"Vediamo SE ha senso"** — la CTA è condizionale e bilaterale. Su un servizio ad alto prezzo il rischio percepito non è il prezzo, è **il venditore che non ti mollerà più**. Una CTA che ammette la possibilità del no abbassa quel rischio meglio di qualunque sconto.
*"e **se possiamo aiutarti**"* ripete lo stesso concetto dentro la descrizione. *"Risposta entro 24 ore"* è l'unica promessa operativa, ed è ripetuta identica nella tabella.

---

## 7. DIFETTI REALI

1. 🔴 **Nessun risultato pubblicato. Su un sito che vende statistica.** Ci sono 10 loghi cliente e zero numeri di esito: nessun *"+38% CVR"*, nessun caso studio, nessun grafico prima/dopo, nessuna testimonianza. La pagina che dice *"Se un'idea non regge i numeri, muore lì"* non porta un solo numero dei propri clienti. **È il buco più grande del sito, ed è l'apertura competitiva per noi.**
2. **Incoerenza numerica tra i suoi stessi siti**: qui **250.000** follower organici, su `andrei-copy.com/manuale-del-copywriter` **"più di 270 mila persone tra i vari canali social"**. Due cifre per la stessa metrica, sullo stesso mese. Va ad aggiungersi alla scoperta trasversale #6 (`3700`/`3600+`/`3100` ordini; `1000+`/`1500+`/`2000+` studenti). **Ora sono otto cifre per quattro metriche.**
3. **Contrasto al limite.** Il corpo a 15px viene servito a opacità `0.5`–`0.6` su fondo `#0a0a0c`: sotto il 4,5:1 richiesto da WCAG AA per testo normale. Le colonne dei concorrenti nella tabella sono al 50%: leggibili con fatica, il che è comodo per il messaggio e scomodo per chi legge davvero.
4. **La sezione dei guerrieri non rispetta lo standard del sito stesso** (*"Creatività con un perché"*): è l'unico blocco senza funzione informativa, e occupa ~600px.
5. **`alt=""` su tutte le immagini decorative e sui guerrieri**; i loghi cliente hanno alt corretti. Nessuna descrizione per l'occhio ASCII né per il wireframe heatmap.
6. **La CTA flottante copre l'angolo in basso a destra su tutte le 14 schermate** — su desktop è tollerabile, su mobile (390px) mangia una fascia utile per l'intera navigazione.
7. **Menu chiuso di default**: la nav espone solo `Carriere` e `Menu`. Chi vuole `/servizi` o `/consulenza` deve aprire l'hamburger anche a 1440px. Scelta estetica pagata in click.
8. **Prezzi assenti** anche dalla card servizi: l'unico appiglio è la riga di qualificazione. Coerente col B2B, ma costringe alla chiamata chi vorrebbe solo un ordine di grandezza.

---

## 8. COSA SIGNIFICA PER L'AGENZIA DI DIGITAL EMPIRE

**Siamo sullo stesso mercato con lo stesso servizio.** Le differenze misurate:

| | AP Sales | Digital Empire |
|---|---|---|
| Posizionamento | *"Agenzia CRO per B2B e SaaS"* | *"L'agenzia progettata per essere licenziata"* |
| Modello | Progetto una tantum, **no retainer** | Sprint 2-4 settimane, **pay-on-performance** |
| Garanzia | Rimettiamo mano alla pagina, gratis | (da definire in pagina) |
| Filtro d'ingresso | 5.000–100.000 €/mese in ads | (da definire) |
| Prova | 10 loghi, **zero risultati numerici** | (il nostro spazio) |
| Tempi dichiarati | Go live in 25 giorni | (da dichiarare) |

**Tre mosse operative che ne derivano:**
1. **Pubblicare risultati misurati è l'unica cosa che loro non fanno.** Un solo caso studio con baseline, intervento e delta, con metodo dichiarato, ci mette sopra di loro sull'asse su cui *loro* hanno scelto di competere (la statistica). Non serve batterli sul design: serve portare i numeri che loro non portano.
2. **"Progettata per essere licenziata" è più radicale di "no retainer"** — ma solo se la pagina lo rende operativo come fa la loro tabella: una riga per ogni alternativa, con il ✓ e il ✕. Il nostro posizionamento oggi è uno slogan; il loro è una tabella.
3. **La riga di qualificazione va scritta anche da noi.** Senza un filtro dichiarato, ogni lead entra e il tempo si consuma nelle chiamate sbagliate.

### Le 9 mosse da portare dentro le skill
1. **Font monospaziato per ogni etichetta di misura.** Dice "qui si misura" senza scriverlo. → `empire-premium-style`
2. **Gerarchia con un colore solo e 12 livelli di opacità** invece di una palette. → `empire-premium-style`
3. **Velo dell'accento al 4%** sulla colonna/opzione preferita: la preferenza si suggerisce col contrasto, non si dichiara. → `market-landing`
4. **Tabella comparativa contro le alternative di acquisto** (fare-da-sé, freelance, assumere, generalista), non contro concorrenti nominati — e **concedere un punto** a un'alternativa. → `market-funnel`, `beast-preventivi`
5. **Citare il cliente tra virgolette** nella colonna "problema" (*"spendi di più"*, *"a me piace il blu"*) invece di descriverlo. → `cro-strategy-*`
6. **Vendere l'ordine delle operazioni** (*"prima il tracciamento, poi le opinioni"*) quando non puoi pubblicare risultati. → `market-strategy`
7. **Numero di tempo al posto del numero di risultato**: *"go live in media in 25 giorni"*. → `beast-preventivi`
8. **Riga di qualificazione sotto la CTA principale**: chi è fuori target lo legge prima di prenotare. → `market-landing`
9. **CTA finale condizionale e bilaterale** (*"Vediamo se ha senso lavorare insieme"*, *"e se possiamo aiutarti"*): abbassa il rischio percepito meglio di uno sconto. → `market-landing`

### E una da non copiare
**Sei guerrieri spartani su un sito che vende metodo statistico.** Se la regola è "creatività con un perché", ogni sezione deve superare l'esame. La nostra versione dello stesso errore sarebbe mettere un'estetica "impero" dove serve un dato.

---

## Connessioni

- [07-claude-speedrun.md](07-claude-speedrun.md) — l'altro sito costruito bene, stessa mano tecnica
- [01-andrei-copy-home.md](01-andrei-copy-home.md) — l'hub info-prodotto: stesso blu `#0062ff`, mondo opposto
- [06-manuale-del-copywriter.md](06-manuale-del-copywriter.md) — dove la stessa persona dichiara 270k follower invece di 250k
- [09-linktree.md](09-linktree.md) — il punto di raccolta che smista verso questa pagina
- `.claude/skills/market-landing/SKILL.md` · `market-funnel` · `beast-preventivi` — dove finiscono le 9 mosse
- [[Digital_Empire_Agency]] — il nostro posizionamento CRO, da mettere accanto a questa tabella
