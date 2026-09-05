# CONFLITTI — dove il corso e la nostra fabbrica dicono cose opposte

> Aperto il **2026-09-05**, alla lezione A4/L05. Fino a L04 non era servito: il corso e la casa
> erano d'accordo, o il corso taceva.
>
> **Regola di arbitrato (piano §6.4):** l'ultima lezione non vince per anzianità, e la nostra
> fabbrica non vince per orgoglio. Vince l'argomento migliore, scritto — e se vince il corso, si
> cambia noi.

---

## C-001 · L'età minima di un video sorgente — **il corso sceglie ciò che noi scartiamo**

| | |
|---|---|
| **Chi** | `A4/L05` (01:09 → 01:18) contro `03-AGENTI-E-RUOLI/operatori/video-analyst.md:31-32` |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — vinciamo noi, ma con una correzione** |

**Cosa dice il corso.** Il video da replicare si sceglie dalla home di YouTube guardando il
«numero magico»: l'esempio scelto in diretta ha **5.700 like, 89.000 visualizzazioni, 13 ore fa**.
La freschezza *è* il segnale.

**Cosa diciamo noi.** `video-analyst`, alla voce «Maturità»:

> «Sotto le 24 ore la velocity è rumore: un video di 2 ore con 200 viste segna 100 views/ora, un
> dato che non si manterrà. **Scarta tutto ciò che è più giovane di 24 ore.**»

Con la nostra regola, **il video su cui il corso costruisce l'intera lezione madre sarebbe stato
buttato**.

**Arbitrato.** Hanno ragione tutti e due su metà della cosa, e la nostra metà è scritta male.

Il nostro esempio interno smonta la nostra stessa soglia: *«un video di 2 ore con 200 viste»* è
rumore **per via delle 200 viste**, non per via delle 2 ore. 89.000 viste non sono un campione
piccolo a nessuna età. Abbiamo scritto un filtro **temporale** per difenderci da un problema di
**volume**, e così buttiamo via i candidati migliori delle nicchie dove la freschezza è il
prodotto (notizie, gossip, attualità, cronaca).

Ma il corso, dall'altra parte, non ha alcuna difesa: prende ciò che è caldo **adesso**, e con quel
criterio il video di 2 ore con 200 viste entrerebbe eccome.

**Decisione: la soglia delle 24 ore resta, ma diventa condizionale al volume.** Sotto le 24 ore un
candidato entra **solo se il numero assoluto di viste è abbastanza grande da rendere credibile la
velocity**. La soglia di volume la fissa `video-analyst`, e va dichiarata nel file, non lasciata
al buon senso.

Regola che ne nasce: **`A4-L05-01`** (binario A).

---

## C-002 · Una sola fonte, riscritta — **il corso lo fa, noi lo vietiamo**

| | |
|---|---|
| **Chi** | `A4/L05` (01:18, 01:58, 05:14) contro `03-AGENTI-E-RUOLI/operatori/transcript-collector.md` §8-§9 (regola `A4-L01-02`) |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — vinciamo noi, senza attenuanti** |

**Cosa dice il corso.** Si scarica il sottotitolo di **un** video, lo si dà a ChatGPT
(«riscrivimi questo testo da zero aggiungendo qualche dettaglio… e rendilo originale») e il
risultato diventa il video. Detto due volte come pregio del metodo: **«non so assolutamente nulla
di cosa tratta questo video»**, «non so neanche di cosa parla la notizia».

**Cosa diciamo noi.** `transcript-collector` conta le parole del materiale e, **sotto ~1.500
parole di transcript**, il pacchetto non parte finché non contiene **almeno 2 fonti esterne** sul
tema. La fabbrica pretende **2.220 parole di script finito**.

**Arbitrato — quattro ragioni, e nessuna è di gusto.**

1. **Il corso si contraddice da solo, sedici minuti dopo.** A 05:53 dice: *«vi ricordo che abbiamo
   già visto come prendere tutte le informazioni da siti, blog, da altri video: potremmo fare un
   testo della durata anche di 10, 12, 15, 20 minuti… se io inserissi altre parti di testo, tutto
   questo sarebbe ancora meglio»*. **La via a più fonti la conosce, la dichiara migliore, e non la
   usa nella dimostrazione.** Noi teniamo quella che lui stesso chiama migliore.
2. **Il fatto smentisce la promessa.** Con una fonte sola il video prodotto in diretta dura
   **2:34** (`frame-113.png`), contro i «10-20 minuti» annunciati. La fonte singola non regge la
   durata che il metodo stesso si pone come obiettivo.
3. **La lezione è di aprile 2023** (`frame-042.png`, ChatGPT su GPT-3.5). Le regole di YouTube sul
   **contenuto riutilizzato** e sui contenuti generati sono state riscritte da allora: un metodo
   che parafrasa un singolo video altrui non è più un rischio teorico. Vedi
   `references/monetizzazione-compliance.md`.
4. **«Rendilo originale» è un'istruzione a un modello, non una proprietà del contenuto.** La
   differenza fra un testo che *sembra* diverso a un lettore e un contenuto che una piattaforma
   considera originale non viene sfiorata in tutta la lezione.

**Decisione: la regola di casa resta e non si tocca.** Il metodo a fonte singola si registra come
**scartato**, con la motivazione, così che nessuna lezione successiva possa reintrodurlo di
straforo. Quello che **prendiamo** dal corso è la sua stessa frase migliore: la durata si costruisce
**aggiungendo fonti**, non allungando il prompt.

Regola che ne nasce: **`A4-L05-03`** (binario A, azione `scarta`).

---

## C-003 · «Prima la quantità» — **una gerarchia che noi abbiamo già rovesciata**

| | |
|---|---|
| **Chi** | `A4/L05` (04:00) contro `ADR-016` (Ultimo Metro) e l'intero apparato di gate |
| **Aperto** | 2026-09-05 |
| **Esito** | **ARBITRATO — vinciamo noi, ma il corso ci ricorda un difetto vero** |

**Cosa dice il corso.** «Se vogliamo lavorare sulla **quantità**, che è fondamentale — poi
ovviamente sappiamo benissimo che anche la qualità deve esserci.» La qualità arriva come postilla
dopo la congiunzione.

**Cosa facciamo noi.** Tre gate bloccanti (`niche-gate`, `qa-audio-video`, `seo-gate`), regolatori
sulla configurazione, e uno standard di script a 2.220 parole.

**Arbitrato.** Sulla gerarchia vinciamo noi: un canale che pubblica cento video sbagliati non ha
cento occasioni, ha cento prove che il canale è sbagliato.

**Ma il corso ci mette il dito su una piaga documentata.** Il suo metro è **5 minuti per video**.
Il nostro, ad oggi, non è scritto da nessuna parte: `BASELINE.md` misura i test e i difetti, non
il **tempo per video**. E `ADR-016` dice che abbiamo **25 pezzi finiti mai pubblicati**, il più
vecchio fermo da 135 giorni. Un apparato di qualità che produce e non pubblica non è più severità:
è un altro modo di non consegnare.

**Decisione:** la gerarchia resta la nostra, **ma il tempo per video entra fra le misure.** Se non
sappiamo quanto ci costa un video, non possiamo dire di aver scelto la qualità: possiamo solo dire
di essere lenti e chiamarlo standard.

Regola che ne nasce: **`A4-L05-04`** (binario A).
