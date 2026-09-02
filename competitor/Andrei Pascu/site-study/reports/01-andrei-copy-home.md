---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #site-study #design-system #copy-teardown #apsales
Created: 2026-09-01
Last updated: 2026-09-01
---

# STUDIO SITO 01 — andrei-copy.com (home)

**URL:** https://www.andrei-copy.com/
**Titolo pagina (tag `<title>`):** `AP Formazione`
**Lingua:** `it-IT` · **Altezza:** 3.384px desktop · **Blocchi testuali:** 44 · **CTA:** 10 · **Media:** 20
**Catturato:** 2026-09-01 — Playwright, viewport 1440×900 e 390×844, DOM renderizzato
**Fonti grezze:** `capture/01-andrei-copy-home/` (4 slice desktop, 6 mobile, `design-tokens.json`, `copy-integrale.md`, `dom-blocks.json`)

> **Nota onesta trovata sul sito stesso:** un badge fisso in basso a sinistra dice *"Stiamo aggiornando il brand — Potresti trovare colori strani, font sbagliati, o simili."* Quindi questa cattura fotografa un brand **in transizione**, non un design system stabilizzato. Alcune incoerenze rilevate sotto sono dichiarate dal proprietario, non sviste da imputargli.

---

## 1. IDENTITÀ E POSIZIONAMENTO DELLA PAGINA

Non è una sales page. È un **hub di smistamento**: manda il traffico verso risorse gratuite, blog, storia personale e, in alto a destra, l'area riservata. Il prodotto non viene mai venduto in questa pagina — la vendita è delegata alle pagine figlie (`/funnel-operator`, `/copy`, `/manuale-del-copywriter`).

Struttura logica in 5 movimenti:
1. **Hero** — chi sono + prova sociale numerica sulla foto
2. **Risorse** — 3 card gratuite (corso, tool, attrezzatura)
3. **Blog** — collezione di articoli
4. **La mia storia** — legittimazione personale con foto 2019 → 2026
5. **Footer blu** — brand APsales, navigazione, disclaimer legale pesante

Il salto brand è vistoso: il `<title>` dice **AP Formazione**, il footer dice **APsales**, la nav in alto a sinistra dice **Claude Speedrun** (un altro prodotto), il dominio dice **andrei-copy.com**. Quattro nomi su una pagina sola.

---

## 2. PALETTE — hex esatti dal DOM, con conteggio d'uso

### Colori di testo
| Hex | Occorrenze | Ruolo |
|-----|-----------|-------|
| `#fafafa` | 27 | **Testo primario** — bianco sporco, mai bianco puro |
| `#111111` | 6 | Testo su fondo chiaro (dentro i bottoni bianchi delle card) |
| `#0062ff` | 5 | **Accento** — eyebrow label e link inline |
| `#f9f9f9` | 3 | Titoli delle card (impercettibilmente diverso da `#fafafa`) |
| `#ababab` | 3 | Testo secondario / descrizioni card |
| `#ebe9e0` | 2 | Testo legale nel footer (bianco caldo) |
| `#a8a8a8` | 1 | Testo disattivato ("Gestisci cookies") |

### Colori di sfondo
| Hex | Occorrenze | Ruolo |
|-----|-----------|-------|
| `#1b1b1d` | 10 | **Fondo dominante** — nero con virata calda, non nero puro |
| `#0062ff` | 7 | Bottoni primari + intero blocco footer |
| `#111111` | 3 | Card su fondo scuro (un gradino più scuro del fondo) |
| `#000000` | 3 | Nero puro, usato per pochi blocchi |
| `#f9f9f9` | 3 | Bottoni chiari dentro le card |
| `#a8a8a8` | 1 | `body` (mai visibile: coperto ovunque) |

**Lettura:** palette a **tre colori veri** — nero caldo, bianco sporco, un solo blu elettrico. Zero colori secondari, zero gradienti nel testo, zero pastelli. La disciplina è il punto: `#0062ff` compare **solo** su elementi cliccabili o su eyebrow che annunciano una categoria. Non è mai decorativo.

**Quattro grigi quasi identici** (`#fafafa`, `#f9f9f9`, `#ababab`, `#a8a8a8`) — la differenza tra `#fafafa` e `#f9f9f9` è invisibile a occhio: è debito tecnico da migrazione, non intenzione. Da non copiare.

**La mossa forte:** il footer non è "un footer scuro con link". È un **blocco pieno `#0062ff` a piena larghezza**, con dentro un'illustrazione dithered monocroma della statua di un condottiero a braccia alzate. Chiude la pagina con un colpo di colore invece di spegnerla. È l'unico punto in cui il blu diventa superficie e non accento — e per questo funziona.

---

## 3. TIPOGRAFIA — quattro famiglie, con lavori diversi

| Font | Occorrenze | Lavoro |
|------|-----------|--------|
| `elza-8u3n84` | 21 | **Titoli e corpo primario** — grotesque geometrica (Adobe Fonts) |
| `"Azeret Mono", monospace` | 9 | **Etichette, eyebrow, testo dei bottoni secondari** |
| `plus-jakarta-sans-o8l9cc` | 7 | Testo di sistema / componenti Framer |
| `"DM Sans"` | 6 | Residuo di migrazione |
| `Poppins` | 1 | Residuo isolato |

### Scala tipografica misurata
| Dimensione | Line-height | Peso | Dove |
|-----------|------------|------|------|
| **92,9px** | — | 700 | `h1` "Risorse" |
| **60,8px** | — | 700 | `h1` "Blog" |
| **48px** | 52,99px | 700 | Titolo hero, `h2` "La mia storia" |
| **20px** | 22,8px | 700 | `h3` titoli card |
| **16px** | 28,8px | 300 | **Corpo di testo** — line-height 1,8 |
| 16px | 28,8px | 700 | Grassetto dentro il corpo |
| 14px | 22,4px | 300 | Descrizioni card |
| **11px** | 28,8px | 300 uppercase | Eyebrow mono blu |
| 12px | — | 300 uppercase | Testo dei bottoni mono |
| 12,54px | 22,58px | 300 | Testo legale footer |

**Le due cose da rubare:**
1. **Line-height 1,8 sul corpo a peso 300.** Testo sottile e molto arioso su fondo nero: si legge senza affaticare, e fa sembrare la pagina più costosa di quanto sia. Digital Empire usa spesso peso 400 con lh più stretto — questo è meglio su dark.
2. **Il monospace come voce separata.** Azeret Mono non è usato per il corpo: è la voce delle **etichette di sistema** (`CORSO GRATUITO`, `INIZIA IL CORSO`, `+280K FOLLOWERS`). Crea due registri visivi — uno umano (elza) e uno tecnico (mono) — che comunicano "questo tizio è un tecnico" senza dirlo in copy.

**Salto di scala brutale:** 92,9px → 16px senza gradini intermedi frequenti. Un solo elemento enorme per schermata, tutto il resto piccolo. Nessuna via di mezzo.

---

## 4. LAYOUT E POSIZIONE DEGLI ELEMENTI

### Header (sticky, `#1b1b1d`, alto ~90px)
Tre zone: **"Claude Speedrun"** a sinistra (x≈320) · **logo a freccia bianca** centrato (x≈717) · **"Accedi"** a destra (x≈1096). Nessun menu di navigazione principale. Nessuna voce prodotto. Solo un cross-sell e un login.
Il logo è una **freccia spezzata bianca su nero**, geometrica, senza wordmark — la wordmark completa (`APsales` + simbolo) appare solo nel footer.

### Hero (y 90 → 749) — split 50/50
- **Sinistra (x=320, larghezza ~320px di testo):** `h1` 48px/700 su 4 righe → paragrafo 16px/300 → bottone blu.
- **Destra (x=825, box 341×490):** foto in bianco e nero di Andrei, **dentro una cornice a filo sottile** che sborda dall'immagine — la cornice non contiene la foto, la incornicia con margine visibile.
- **Sfondo:** pattern dithered scurissimo (mezzatinta a punti), quasi invisibile, che dà grana senza rumore.

**Le 3 etichette flottanti sulla foto** — il pezzo migliore di tutta la pagina:
| Etichetta | Posizione | Stile |
|-----------|-----------|-------|
| `+280K FOLLOWERS` | alto-destra, fuori dalla foto | fondo bianco, testo nero, mono |
| `+1M GENERATO COL COPYWRITING` | sinistra, sovrapposta alla foto | **fondo `#0062ff`, testo bianco**, mono |
| `+3700 ORDINI SUL SITO` | basso-destra, fuori dalla foto | fondo bianco, testo nero, mono |

Ognuna è collegata alla foto da una **linea sottile con un punto terminale** — come le didascalie di uno schema tecnico o di un'infografica medica. Il numero più importante (**il fatturato**) è l'unico in blu: gerarchia dentro la gerarchia.

### Sezione Risorse (y 839 → 1600)
`h1` "Risorse" a **92,9px** — il testo più grande della pagina, e sta su una sezione **gratuita**, non su un prodotto.
Sotto, **3 card in griglia** (330×462 ciascuna, gap ~24px, allineate da x=203 a x=1237):
```
[ immagine wireframe 330×186 ]   ← illustrazione 3D a fil di ferro, monocroma
  EYEBROW MONO BLU 11px          ← CORSO GRATUITO / TOOLS & AI / ATTREZZATURA
  Titolo 20px/700
  Descrizione 14px/300 #ababab   ← 2-3 righe, mai di più
  [ BOTTONE BIANCO MONO 12px ↗ ] ← INIZIA IL CORSO / ESPLORA LO STACK / SCOPRI IL SETUP
```
La card intera è cliccabile (rilevata come CTA da 330×462), non solo il bottone. Fondo card `#111111` su fondo pagina `#1b1b1d`: **un solo gradino di stacco**, niente bordi, niente ombre. La card si distingue per differenza di luminanza, non per decorazione.

Le immagini delle card sono **rendering wireframe** (un laptop con scritto "LE BASI", un'icona a raggiera, una fotocamera Sony) in bianco su nero, con reticolo a punti. Stile coerente, prodotto apposta — non stock.

### Sezione Blog (y 1726 → 2100)
Layout asimmetrico: a sinistra `h1` "Blog" 60,8px + paragrafo + bottone blu. A destra una **colonna di card orizzontali** con thumbnail quadrata + titolo in mono maiuscolo (`COS'È UN FUNNEL OPERATOR?`, `STAI PARLANDO DAVVERO CON ANDREI PASCU?`). Le card scorrono con animazione allo scroll.

### Sezione "La mia storia" (y 2128 → 2679)
Split invertito rispetto all'hero: **immagini a sinistra, testo a destra**. Due foto **ruotate di pochi gradi e sovrapposte**, ognuna con una targhetta d'angolo con l'anno — `2019` (targhetta bianca) e `2026` (targhetta blu). La foto del 2019 è dietro, in giacca e cravatta; quella del 2026 davanti, con bordo blu, in polo e occhiali.

Il messaggio è visivo e non scritto: **prima ero un altro, adesso sono questo**. Il bordo blu marca il "presente" senza una parola.

### Footer (y 2679 → 3384) — blocco `#0062ff` pieno
Wordmark `APsales` grande in bianco con il simbolo a freccia · 4 icone social · 5 link in colonna (La mia storia, Store, Recensioni, Risorse, Blog) · a destra l'illustrazione dithered del condottiero · in basso, separato da una linea sottile, **il disclaimer legale**.

---

## 5. COPY — teardown sezione per sezione, con il perché

### 5.1 Headline hero
> **"Formazione tecnica per professionisti di marketing"**

Cinque parole di lavoro. Nessuna promessa di guadagno, nessun numero, nessuna urgenza.
- **"tecnica"** — squalifica in anticipo chi cerca motivazione. È un filtro, non un vezzo.
- **"per professionisti di marketing"** — dichiara il destinatario e con esso il livello. Chi non si sente professionista o si tira indietro o si sente promosso: entrambe le reazioni lavorano a favore.
- Cosa **non** dice: quanto guadagni, in quanto tempo, quanto è facile. Su un mercato info-product italiano saturo di promesse, la sobrietà è essa stessa posizionamento.

### 5.2 Sottotitolo
> "AP Sales è un'agenzia di marketing… E qui insegniamo **il nostro scientifico** e **preciso** approccio per fare marketing online."

La struttura è: **prova di mestiere prima della proposta di valore**. Non "ti insegno il marketing" ma "sono un'agenzia che lavora, e ti insegno quello che facciamo".
I due grassetti cadono su `scientifico` e `preciso` — aggettivi da laboratorio, non da guru. Coerenti con "tecnica" della headline.
*(Difetto reale: la frase è spezzata male, `il nostro scientifico e preciso approccio` legge storto in italiano. Nel DOM i due `<strong>` sono separati, quindi non è un artefatto della cattura: la frase è così.)*

### 5.3 Le tre etichette sulla foto — **la prova sociale come dato, non come vanto**
> `+280K FOLLOWERS` · `+1M GENERATO COL COPYWRITING` · `+3700 ORDINI SUL SITO`

Tre metriche, tre categorie diverse, zero aggettivi:
- **audience** (280K) — dimostra attenzione
- **risultato economico** (1M) — dimostra competenza
- **trazione commerciale propria** (3700 ordini) — dimostra che qualcuno *paga davvero*

Il terzo è il più intelligente e il più raro: quasi nessuno pubblica il numero di ordini. Dice "non sono un influencer con un corso, sono uno che vende da tempo". Ed è **verificabile e specifico** (3700, non "migliaia").
Sono scritte in **monospace maiuscolo**, come output di un terminale: il font fa metà del lavoro di credibilità. Un numero in mono legge come *misurato*; lo stesso numero in un font morbido legge come *dichiarato*.

### 5.4 Copy delle CTA — tutte verbo + oggetto, mai "Clicca qui"
| CTA | Dove | Registro |
|-----|------|----------|
| `Scopri di più →` | hero, bottone blu | generico — **il punto debole della pagina** |
| `INIZIA IL CORSO ↗` | card 1, bottone bianco mono | verbo d'azione + oggetto |
| `ESPLORA LO STACK ↗` | card 2 | verbo curioso, non impegnativo |
| `SCOPRI IL SETUP ↗` | card 3 | idem |
| `Leggi gli articoli` | blog, bottone blu | letterale |
| `Leggi la mia storia` | storia, bottone blu | letterale |

**Il pattern:** due sistemi di bottone con due lavori distinti.
- **Bottone blu pieno, font elza, freccia →** = navigazione del sito, azione morbida
- **Bottone bianco, mono maiuscolo, freccia ↗ (diagonale)** = ingresso in una risorsa vera

La freccia diagonale ↗ segnala "esci da qui / si apre altro". È una convenzione da documentazione tecnica, ed è coerente con il posizionamento "tecnico" della headline.

**Errore vero:** `Scopri di più` è la CTA della hero, cioè quella che riceve più attenzione di tutte, ed è la più vuota della pagina. Non dice dove porta né cosa ottieni. Tutte le altre CTA della pagina sono migliori di quella principale.

### 5.5 Eyebrow delle card
> `CORSO GRATUITO` · `TOOLS & AI` · `ATTREZZATURA`

Mono, 11px, maiuscolo, **blu**. Fanno tre lavori insieme: categorizzano, prezzano (`GRATUITO` toglie l'attrito prima ancora che si legga il titolo), e danno alla griglia un ritmo visivo. La parola *gratuito* sta sopra al titolo, non sotto: la prima informazione che ricevi è che non paghi.

### 5.6 Descrizioni delle card — la formula si ripete
> "Il punto di partenza: fondamenta, framework e metriche che ogni marketer deve padroneggiare **prima di scalare**."
> "Lo stack di strumenti AI, editing e automazione che sta dietro **ogni contenuto e ogni campagna di AP Sales**."
> "Fotocamere, microfoni e setup con cui produciamo i video e i contenuti **che vedi ogni giorno**."

Struttura identica in tutte e tre: **[cosa è] + [aggancio a qualcosa che il lettore già conosce o desidera]**.
Le ultime due sono la stessa mossa: *quello che ti do è quello che uso davvero io*. "Che vedi ogni giorno" trasforma i contenuti che il visitatore ha già consumato su Instagram in prova che il setup funziona. Il lead magnet è credibile perché il lettore ha già visto il risultato prima di arrivare qui.

### 5.7 "La mia storia"
> "Sono Andrei Pascu, titolare di **AP Sales**, un'agenzia di marketing based in Italia. Sono qui per insegnare il marketing **per come lo vedo io**."

Due frasi, due lavori: **credenziale** (titolare di un'agenzia vera, con link) e **inquadramento soggettivo** ("per come lo vedo io"). La seconda è una mossa difensiva intelligente: chi dichiara di dare un'opinione personale non deve difendere una verità universale, e disinnesca in anticipo il "ma non è l'unico modo".

### 5.8 Disclaimer legale — da studiare, non da saltare
> "Questo sito e i consigli contenuti al suo interno sono opinioni personali a scopo educativo… I suoi risultati non sono tipici e i tuoi potrebbero variare… Andrei Pascu e i suoi collaboratori non fanno e non trattano argomenti come crypto, personal finance, fiscalità, risorse umane, recruiting, network marketing o in genere metodi di arricchimento veloce."

Sta scritto piccolo (12,54px) sul footer blu, **con contrasto basso su blu** — presente ma non gridato. La lista di esclusione (`crypto, personal finance, network marketing…`) fa due cose insieme: copre legalmente **e** posiziona per differenza. Dice "non sono quella roba lì" mentre adempie a un obbligo. È una difesa che vende.

---

## 6. COMPONENTI RICORRENTI — inventario riusabile

| Componente | Specifiche misurate |
|-----------|---------------------|
| **Bottone primario** | bg `#0062ff`, testo `#fafafa`, 16px/w600, raggio **10px**, altezza **53px**, larghezza a contenuto (161-183px), freccia `→` in coda |
| **Bottone su card** | bg `#f9f9f9`, testo `#111111`, mono 12px/w300 **uppercase**, raggio 0, freccia `↗` |
| **Card risorsa** | 330×462, bg `#111111`, raggio 0, nessun bordo, nessuna ombra; immagine 330×186 in testa |
| **Eyebrow** | mono 11px/w300 uppercase, colore `#0062ff`, sopra al titolo |
| **Etichetta dato flottante** | mono maiuscolo, bg bianco o `#0062ff`, collegata con linea sottile + punto |
| **Targhetta anno** | rettangolo pieno all'angolo della foto, bianco (passato) o blu (presente) |
| **Cornice a filo** | contorno sottile che sborda dall'immagine, non la contiene |
| **Raggio d'angolo** | **10px, unico valore su tutto il sito** (6 occorrenze). Tutto il resto è a spigolo vivo |

**Il raggio unico è la lezione di sistema:** un solo valore, applicato solo ai bottoni e ai contenitori di UI. Card, foto, cornici, etichette sono tutte a 0. Nessuna incoerenza possibile.

---

## 7. TRATTAMENTO DELLE IMMAGINI

Tre trattamenti distinti, ognuno con un lavoro:
1. **Foto persona** — bianco e nero, contrasto alto, incorniciate da filo sottile. Mai a colori. Mai a tutta larghezza.
2. **Illustrazione tecnica** — rendering wireframe/dithered monocromi (laptop, fotocamera, raggiera, statua del condottiero). Fatti su misura, coerenti tra loro, mai stock.
3. **Sfondi** — pattern a mezzatinta scurissimo, appena percepibile: dà materia al nero senza aggiungere rumore.

**Zero immagini a colori su tutta la pagina.** L'unico colore del sito è il blu, e il blu appartiene all'interfaccia, non alle foto. È la ragione per cui una palette a tre colori non risulta povera.

---

## 8. MOBILE (390×844)

La pagina passa da 4 a 6 schermate. Le 3 card risorsa si impilano in colonna. L'hero perde la foto a fianco e va in verticale. Le etichette dati flottanti restano sulla foto ma rimpiccioliscono. Impianto invariato: stesso nero, stesso blu, stessa griglia a una colonna.

---

## 9. DIFETTI REALI (utili quanto i pregi)

1. **Quattro nomi di brand su una pagina** — `andrei-copy.com` / `AP Formazione` / `APsales` / `Claude Speedrun`. Un visitatore nuovo non sa come si chiama questa cosa.
2. **`Scopri di più` come CTA principale** — la posizione più preziosa della pagina ha il copy più debole della pagina.
3. **Quattro grigi indistinguibili** (`#fafafa`/`#f9f9f9`, `#ababab`/`#a8a8a8`) e **cinque famiglie di font** — debito da migrazione, ammesso dal badge "Stiamo aggiornando il brand".
4. **Frase hero grammaticalmente storta** — "il nostro scientifico e preciso approccio".
5. **Nessuna testimonianza in home** — c'è un link "Recensioni" nel footer, ma zero prova sociale di studenti sopra la piega. Coincide con il rilievo del vecchio audit del 09/03/2026 (`MARKETING-REPORT-andrei-copy-com.pdf`: 51/100, "assenza totale di social proof da studenti").
6. **Cookie banner enorme e badge brand fissi** occupano permanentemente l'angolo in basso a sinistra su ogni schermata.

---

## 10. COSA VALE PER DIGITAL EMPIRE

**Da rubare subito:**
- **Etichette-dato in monospace collegate alla foto con linea + punto.** Il modo più efficiente visto finora per mettere tre prove sociali nella hero senza scrivere un paragrafo. Il font mono fa il lavoro di credibilità da solo.
- **Doppio sistema di bottoni con due frecce diverse** (`→` navigazione morbida / `↗` ingresso in risorsa). Convenzione muta che riduce l'attrito di scelta.
- **Un solo raggio d'angolo su tutto il sito.** Regola di sistema a costo zero che elimina un'intera classe di incoerenze.
- **L'eyebrow che prezza prima del titolo** (`CORSO GRATUITO` sopra al nome del corso).
- **Il footer come blocco di colore pieno** invece che come zona spenta.
- **La lista di esclusione nel disclaimer** che posiziona mentre copre legalmente.

**Da non copiare:**
- La CTA `Scopri di più`.
- La proliferazione di font e di grigi.
- L'assenza di prova sociale di terzi sopra la piega.

**Punto di attrito col nostro design system:** il nostro riferimento aureo (`ccm-premium`) usa arancione `#fb4604` su ink/paper con grana doppia; qui la logica è la stessa (**un solo accento saturo su fondo scuro caldo, zero colori secondari**) con un blu al posto dell'arancione. Il metodo è compatibile, il colore no. Confermare l'arancione, adottare la disciplina.

---

## Connessioni

- [[Source_Andrei_Pascu_Importanza_Landing]] — video 5 cat2: la teoria della landing minima. Qui la vediamo applicata *(nota: questa home è un hub, non la landing bio-link — quella è `linktr.ee/andrei.bsns`, studio 09)*
- [[Source_Andrei_Pascu_10_Lead_Magnet]] — video 4: le 3 card risorsa sono lead magnet in senso stretto (corso gratuito, stack tool, lista attrezzatura = idea #10 "liste e raccolte")
- [[02-funnel-operator]] — la sales page vera, 24.019px, dove il prodotto viene venduto
- `second-brain-vault/raw/Agenti/2026-05-06-marketing-report-andrei-copy-com.md` — audit marketing del 09/03/2026, 51/100
