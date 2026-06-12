> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A2 + sez. 5 (writer.py, humanizer.py)

# T-WRITER-APSOC — Writer Messaggi APSOC

> Funzione L4 di A2-ACQUISIZIONE · Worker · Agente: `AG-A2-WRITE-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A2

## Cosa fa

Scrive il messaggio outreach (email / LinkedIn / DM Instagram) per ogni lead, usando la struttura
APSOC e l'angolo fornito da T-STRATEGIST. Script: `writer.py`, `humanizer.py`, `copy_knowledge.py`.

## Struttura APSOC applicata al messaggio outreach

| Elemento | Cosa scrive |
|---|---|
| A (Attenzione) | hook: la situazione specifica del lead (angolo di T-STRATEGIST) |
| P (Problema) | il problema e il suo impatto — quantificato se possibile |
| S (Soluzione) | il prodotto DE adeguato: Outreach / Content / Second Brain |
| O (Obiezione) | la 1 obiezione più probabile per quel target, anticipata e risposta |
| C (CTA) | unica, chiara: `presentazione-empire.vercel.app` |

## Varianti per canale

| Canale | Lunghezza | Tono | Script |
|---|---|---|---|
| Email | 100-150 parole | professionale ma diretto | `writer.py` |
| LinkedIn (messaggio) | 50-80 parole | conversazionale | `writer.py` con profilo LinkedIn |
| Instagram DM | 40-60 parole | più casual, 2 messaggi: intro + link | `writer.py` DM mode |
| LinkedIn (commento) | 20-40 parole | valore, non pitch | `copy_knowledge.py` |

## Humanizer

`humanizer.py` post-processa il testo per ridurre i pattern AI rilevabili:
- varia la struttura delle frasi
- aggiunge micro-imperfezioni naturali
- adatta il registro al settore del lead

## Failure

| Evento | Risposta |
|---|---|
| Angolo non disponibile da T-STRATEGIST | T-writer-apsoc non produce; batch lead in attesa |
| Messaggio troppo lungo / fuori tono | T-bibbia-qa lo blocca con note specifiche → rework |
| Template esaurito (stessa struttura per N lead consecutivi) | T-writer-apsoc ruota tra varianti disponibili in agency/outreach |

## Connessioni

- [`./T-strategist.md`](./T-strategist.md) (fornitore angolo) · [`./T-bibbia-qa.md`](./T-bibbia-qa.md) (gate successivo)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
