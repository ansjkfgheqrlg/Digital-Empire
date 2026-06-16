# WF-ANTICIPAZIONE
## Il "fai di più del chiesto" — brief di anticipazione a inizio fase

> Organo: MAXIMILIAN (LX) · Owner: MX-ANTICIPATE + MX-VISION · Sintesi: MX-PRIME · Stato: DEFINED
> Trasforma il tratto §1 "Anticipazione" da buona volontà in PASSO ESEGUIBILE: dato lo scope di
> una fase, deduce cosa Max vorrà DOPO e lo prepara prima che lo chieda. Corpus §70-72: *"Fai
> anche DI PIÙ di quello che ti ho chiesto… devi IMMAGINARE le altre [modifiche] che probabilmente
> voglio… pensa a me: Max probabilmente lo vorrebbe…"* Fonte: `12-DOSSIER-MAXIMILIAN.md` §3·§1·§8.

---

## Trigger
- **Automatico**: a INIZIO fase, subito DOPO lo SPEC (passo 1) e prima del PRE-MORTEM (passo 2)
  del ciclo a 9 passi. Arricchisce lo SPEC prima che il BUILD parta.
- **Manuale**: Max apre una nuova direzione → l'organo anticipa le fasi-figlie che ne derivano.
- **Natura**: consigliato per ogni fase non banale. NON bloccante (a differenza di WF-REVIEW):
  produce arricchimento, non veto. Il veto arriva dopo, al passo 5-bis.

---

## Input (JSON)
```json
{
  "anticip_id": "MX-ANT-2026-0617-007",
  "fase_id": "V2-4-MANDATO",
  "spec_ref": "company/Memory/checkpoints/CP-20260617-NNN.md#spec",
  "scope_dichiarato": ["costruire ecosistema Mandato", "Sentinelle con più workflow"],
  "dossier_ref": "PIANO-MAESTRO/13-DOSSIER-MANDATO.md",
  "committente": "conductor-di-fase | Max"
}
```

---

## Pipeline (passi · agente owner)
```
1. APERTURA RECORD                        (MX-PRIME)
   └── registra maximilian/anticipazioni/<anticip_id> stato=OPEN; carica SPEC + scope + dossier.

2. RECUPERO PRECEDENTI                     (MX-MEMORY)
   └── cerca nel corpus i pattern di "cosa Max ha voluto in più" in fasi analoghe → corpus_refs[]
        (es. §36-38: "per OGNI reparto un team + workflow"; §44-58: "deve diventare un GIGANTE").

3. PROIEZIONE PARALLELA                    (MX-ANTICIPATE ‖ MX-VISION)
   ├── MX-ANTICIPATE: "cosa vorrà DOPO questo scope?" → lista deduzioni dirette (l'ovvio non detto)
   └── MX-VISION:     "lo scope è abbastanza GRANDE?" → spinge scala (1 unità v1 = 1 componente v2)
        Output combinato: candidati[] = [{voce, perche, tratto §1, urgenza ALTA|MEDIA|BASSA}].

4. CLASSIFICA URGENZA                      (MX-FAST)
   └── ALTA → arricchisce lo SPEC della fase (slot pronti, scope esteso ora).
        MEDIA/BASSA → alimenta il BACKLOG (ADR-005): non urgenti, non fermano la costruzione.

5. SINTESI BRIEF NELLA VOCE DI MAX         (MX-PRIME)
   └── "Max, oltre a questo, probabilmente vorrai anche X, Y, Z perché…" — diretto, con citazioni.
        Marca record CLOSED; scrive l'esito + quali anticipazioni si avvereranno (per calibrazione).
```

---

## Gate
- **G-ANT1 (no-vuoto):** un brief con 0 candidati su una fase non banale → MX-VISION rilancia
  ("se non c'è nulla da anticipare, lo scope è troppo piccolo" — è esso stesso un segnale di scala).
- **G-ANT2 (ancoraggio):** ogni candidato ALTA deve citare un tratto §1 + (dove possibile) il corpus;
  niente anticipazioni "a sensazione" non riconducibili agli standard di Max.
- **G-ANT3 (non-bloccante):** questo workflow NON ferma la fase; se in dubbio, declassa a BACKLOG e
  procede (tratto Velocità §1 — le minuzie non bloccano MAI la costruzione).

---

## Output (JSON)
```json
{
  "anticip_id": "MX-ANT-2026-0617-007",
  "fase_id": "V2-4-MANDATO",
  "brief": "Max, oltre allo scope dichiarato, probabilmente vorrai anche…",
  "arricchimento_spec": [
    "ogni Sentinella con ≥2 workflow (corpus §55-56), non uno solo"
  ],
  "verso_backlog": [
    "dashboard di osservabilità del Mandato — utile ma non per questa fase"
  ],
  "candidati_scartati": ["rinominare i record — minuzia, BACKLOG"],
  "tratti_applicati": ["Anticipazione", "Scala", "fai di più"],
  "corpus_refs": ["direttiva-20260611-scala-v2.md:52-58"],
  "record_tracciato": "maximilian/anticipazioni/MX-ANT-2026-0617-007"
}
```

---

## Innesto nel ciclo 9 passi
Si inserisce tra il passo 1 SPEC e il passo 2 PRE-MORTEM ([[10-METODO-CICLO-FASE]]). Il suo
`arricchimento_spec` rientra nello SPEC della fase (slot pronti) PRIMA del BUILD; il
`verso_backlog` finisce in `company/Memory/BACKLOG.md`. A valle, al passo 5-bis, WF-REVIEW-MAXIMILIAN
verifica se gli slot anticipati sono stati onorati. Anticipazione (qui) e veto (5-bis) sono le due
facce dello stesso tratto: prevedere prima, esigere dopo.

---

## Dry-run
Fase "costruisci ecosistema Mandato", scope dichiarato minimale. MX-MEMORY recupera dal corpus
*"il Mandato deve diventare un GIGANTE… ogni Sentinella deve avere più workflow… il Mandato deve
essere proprio un ecosistema"* (§52-58). MX-VISION segnala che lo scope v1 è troppo piccolo;
MX-ANTICIPATE deduce: team di gestione del Mandato, calibrazione, osservabilità. MX-FAST: i primi
due ALTA → SPEC; il terzo MEDIA → BACKLOG. MX-PRIME emette il brief nella voce di Max. Record
ricostruibile a freddo da `maximilian/anticipazioni/<anticip_id>` (test-amnesia).

---

## Connessioni
- [[WF-REVIEW-MAXIMILIAN]] — il passo 5-bis che dopo verifica se gli slot anticipati sono onorati
- [[maximilian-standard-gate]] — riusa i test §1 anche come metro delle anticipazioni
- [[maximilian-voice]] — usata da MX-PRIME per il tono del brief
- [[10-METODO-CICLO-FASE]] passi 1-2 — il punto d'innesto (tra SPEC e PRE-MORTEM)
- [[12-DOSSIER-MAXIMILIAN]] §1 (Anticipazione + Scala) · §3 (questo workflow) · §8 (anticipazioni)
- ADR-005 (minuzie → BACKLOG) · ADR-006 (ciclo 9 passi) · ADR-007 (pivot V2)
