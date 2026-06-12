> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A2 + sez. 8 (Gate Bibbia) + sez. 5 (bibbia_team.py)

# T-BIBBIA-QA — Gate Bibbia (3-Checker)

> Funzione L4 di A2-ACQUISIZIONE (condivisa con A5) · Worker ×3 · Agenti: `AG-A2-BIBBIA-C1/C2/C3` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A2 + §8

## Cosa fa

Gate qualità **bloccante** su ogni messaggio outreach PRIMA dell'invio. Tre checker indipendenti
valutano il messaggio in parallelo: anche UN SOLO checker che boccia → il messaggio NON parte.
**Blocca, non suggerisce.** Script esistente: `bibbia_team.py` (usato-così, ADR-003).

## I 3 checker e i loro criteri

### Checker 1 (AG-A2-BIBBIA-C1) — Struttura APSOC

Verifica che il messaggio rispetti la struttura:
- Ha hook (Attenzione) che parla del problema specifico del target (non di DE)
- Ha problema con impatto (non generico: "il tuo sito è lento" → KO; "X% di rimbalzo = Y€ persi" → OK)
- Ha soluzione collegata al problema (non pitch generico)
- Ha UNA obiezione anticipata con risposta verificabile
- Ha UNA CTA: `presentazione-empire.vercel.app`
- KO immediato: più di 1 CTA, nessuna CTA, CTA diversa dalla standard

### Checker 2 (AG-A2-BIBBIA-C2) — Brand Voice e Promesse

Verifica conformità al Mandato Empire:
- Zero promesse di risultato non documentate ("ti porteremo 100 clienti al mese" → KO)
- Zero scarcity finta ("solo per oggi" se non è vero → KO)
- Brand voice: diretta, senza gergo vuoto, senza superlative non provati
- Firma conforme (nome + Digital Empire + link presentazione)
- Lunghezza nel range per il canale

### Checker 3 (AG-A2-BIBBIA-C3) — Personalizzazione e Unicità

Verifica che il messaggio sia personale, non generico:
- Il hook cita un segnale reale del lead (non "so che sei nel settore X" generico)
- Il tono è adeguato al canale (email vs LinkedIn vs DM)
- Non è identico a un messaggio inviato allo stesso lead in precedenza (check su agency/conversations)
- Humanizer ha processato: non pattern AI ovvi

## Output

```json
{
  "messaggio_id": "msg_001",
  "c1_pass": true,
  "c2_pass": true,
  "c3_pass": false,
  "c3_note": "Hook generico: 'so che sei nell'ecommerce' senza segnale specifico. Rivedere con angolo da T-STRATEGIST.",
  "gate_pass": false,
  "azione": "rework → T-WRITER-APSOC"
}
```

## Pattern condiviso (pattern #6)

T-BIBBIA-QA è usato sia da A2 (su ogni messaggio outreach) sia da A5 (su ogni template nuovo
prima del rollout). Il gate è UNO: non due versioni, non fork. Configurazione canale come
parametro in ingresso (`{canale: email|linkedin|instagram}`).

## Failure

| Evento | Risposta |
|---|---|
| Gate boccia lo stesso template ≥3 volte | alert a AG-A2-COORD → template sospeso + richiesta refresh ad A5 |
| bibbia_team.py non disponibile | STOP run del canale: il gate è obbligatorio, mai bypassato |

## Connessioni

- [`./T-writer-apsoc.md`](./T-writer-apsoc.md) (fornitore) · [`./T-sender.md`](./T-sender.md) (cliente: solo dopo PASS)
- [`../Reparti/A2-Acquisizione/`](../Reparti/A2-Acquisizione/) · [`../Reparti/A5-Copywriting-Interno/`](../Reparti/A5-Copywriting-Interno/)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
