# 15 — LANCI

> **Porta un prodotto già pubblicabile da pubblicato a venduto e misurato.**
> Nato il 2026-09-10. Decisione: [ADR-025](../../Memory/decisions/ADR-025-ecosistema-lanci.md),
> firmata da Max l'08/09/2026. Sigla: `LAN`.

---

## Perché esiste

Fra gli ecosistemi c'era un tratto che non copriva nessuno.

**ULTIMO METRO** ([ADR-016](../../Memory/decisions/ADR-016-ultimo-metro.md)) porta un
prodotto da *finito* a *pubblicato*. **TESORERIA**
([ADR-020](../../Memory/decisions/ADR-020-reparto-tesoreria.md)) conta l'euro una volta che
è nei conti. In mezzo — da *pubblicato* a *venduto e misurato* — non c'era niente, e si
vede nei numeri: al 2026-09-05 l'azienda **non poteva incassare un euro**, il bottone
d'acquisto era un indirizzo di posta, e il canale che doveva portare pubblico al Manuale
era spento dal 29/07/2026.

Il Manuale Claude Code è rimasto fermo sei mesi senza che nessuno se ne accorgesse. Non
perché mancasse il prodotto: perché mancava l'organo che porta un prodotto finito davanti a
qualcuno che paga, e perché **nessun comando poteva dire che era fermo**.

---

## Il mandato, in una riga

Porta un prodotto già pubblicabile da **pubblicato** a **venduto e misurato**.

Non produce il prodotto (è di ULTIMO METRO). Non contabilizza l'euro (è di TESORERIA).
Copre il tratto in mezzo, e nessun altro ecosistema lo copre.

---

## Come è fatto: l'artefatto, non il reparto

Il centro dell'architettura sono **tredici artefatti tipizzati**, non un organigramma.
Ognuno ha uno schema che lo valida, un produttore unico, un giudice **diverso** dal
produttore, un gate che lo blocca, gli artefatti da cui dipende, e un ramo di fallimento
mai vuoto.

| | | |
|---|---|---|
| `ART-PUB` pubblico | `ART-DEC` decisione | `ART-CRT` certificato |
| `ART-RIC` ricerca | `ART-PRV` previsione | `ART-OFF` offerta |
| `ART-CPY` copy | `ART-FNL` funnel | `ART-EDT` editoriale |
| `ART-BDG` budget | `ART-APE` apertura | `ART-CNS` consuntivo |
| `ART-DBR` debrief | | |

**La fonte di verità è il registro, non la prosa.** Se un documento contraddice il registro,
ha torto il documento.

📂 **Registro e schemi:** [`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/`](../../../PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/)
— `registro.yaml` è l'unica fonte, validato da `valida_registro.py` (**832 controlli**, deve
uscire **0 prima di ogni build**, non dopo).

Il registro **non è stato spostato qui** di proposito: è il cuore del pacchetto di piano che
lo documenta, ed è citato per percorso in nove documenti. Duplicarlo creerebbe due fonti di
verità, che è esattamente la malattia che la decisione 3 di ADR-025 vieta (ADR-003: si
avvolge, non si sposta).

---

## Due invarianti che non si negoziano

- **INV-01** — per ogni artefatto, **giudice ≠ produttore**. Chi produce non approva mai.
- **INV-09** — l'agente giudice `lan-gate` **non ha `Write` né `Edit`**. I verbali dei gate
  li scrive lo script che lo invoca, mai l'agente.

Le verifica `valida_registro.py` prima di ogni build.

---

## Lo stato di adesso, misurato

| | |
|---|---|
| Scaglione raggiunto | **S0, aperto** — la catena dell'incasso non è chiusa |
| Lanci in corso | nessuno |
| Costruzione | `TASK-LANCI-BUILD-W3`, frantumata in 12 micro-task |

**S0 è il gesto zero e non è negoziabile** (decisione 6 di ADR-025): finché un euro non
entra, non arriva il prodotto, non torna indietro l'euro, e i tre fatti non sono leggibili
in un pannello, **non si costruisce nient'altro dell'ecosistema.**

Tre delle prime quattro micro-task sono **mani umane** — servono il pannello del servizio di
posta, un conto su un fornitore di pagamento e una carta vera. Nessuna sessione può farle.

---

## Struttura

```
15-LANCI/
├── ECOSISTEMA.md              questo file
├── BACKBONE.md                l'architettura portante
├── 01-FLUSSI-E-PIANI/         i dieci flussi, 42 fasi
├── 02-AUTOMAZIONI-E-SCRIPTS/  la macchina a stati e il comando `lancio`
├── 03-AGENTI-E-RUOLI/         i quindici agenti `lan-*`
├── 04-SKILLS-E-REFERENCE/     reference operative
├── 05-TEMPLATES-E-KIT/        gli schemi compilati d'esempio
├── 06-DASHBOARD-E-METRICHE/   `lancio blocchi`, `lancio costi`
└── lanci/                     un lancio vero per cartella
```

---

## Il tetto di spesa

**15,00 $ per lancio**, ereditato dal registro (`ponte.tetto_spesa_per_lancio_usd`). Al
raggiungimento del tetto il lancio **si ferma dov'è, salvato, e riprende** — non ricomincia.

Ogni invocazione di agente porta una tassa fissa di harness di **0,08-0,11 $** misurata in
[ADR-014](../../Memory/decisions/), indipendente dal contenuto: il numero di agenti è un
moltiplicatore di costo, non un indicatore di capacità.

---

## Connessioni

- [[ADR-025-ecosistema-lanci]] — la decisione che lo fa nascere
- [[ADR-016-ultimo-metro]] — l'ecosistema a monte (prodotto → pubblicato)
- [[ADR-020-reparto-tesoreria]] — l'ecosistema a valle (l'euro nei conti)
- [[ADR-026]] — una task assegnata è già autorizzazione completa
- [`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md`](../../../PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md) — il piano, v4
- `company/Memory/tasks/micro/TASK-LANCI-BUILD-W3/` — le dodici micro-task della costruzione
