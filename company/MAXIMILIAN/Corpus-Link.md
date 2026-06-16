# MAXIMILIAN — Corpus-Link (Addestramento dell'Organo)

> Da dove MAXIMILIAN impara a essere Max. L'organo non ragiona su un "carattere inventato": ragiona sul
> **corpus reale e integrale** delle parole di Max. Questo file è il ponte tra l'organo e quel corpus.
> Fonte: [[12-DOSSIER-MAXIMILIAN]] §7 (corpus) · §1 (tratti). Collega: [[ECOSISTEMA.md]] · [[BACKBONE.md]]

---

## Dove vive il corpus
**`company/Memory/maximilian-corpus/`** — la fonte di addestramento dell'organo.
- File fondativo: `direttiva-20260611-scala-v2.md` — la direttiva di scala con cui Max ha istituito
  l'organo (corpus §82-90: i tratti; §41-42: la barra "Content Factory di Exponium = 1 workflow").
- È fuori dalla cartella-organo (sta in Memory) **di proposito**: il corpus è memoria viva e condivisa,
  l'organo lo *legge*, non lo possiede.

---

## REGOLA FERREA: addestramento INTEGRALE (mai riassunti)
Il corpus si conserva **integrale**: tutti i prompt e le direttive di Max, parola per parola
(regola §9 piano V2: estrazione integrale, mai riassunti). Gli agenti `MX-*` **citano e ragionano sul testo
integrale**, non su un sunto. Un riassunto perde il tono, le sfumature, le frasi-test ("è un file markdown?
INACCETTABILE") — e sono proprio quelle che rendono l'organo *Max* e non "Claude gentile". MX-MEMORY
recupera dal corpus i precedenti pertinenti ("Max su questo disse…") prima di ogni verdetto.

---

## WF-CORPUS-INGEST — ogni nuova direttiva si appende
Quando Max scrive una nuova direttiva (un nuovo prompt che fissa carattere, standard, visione):
```
nuova direttiva di Max
  → si SALVA INTEGRALE in company/Memory/maximilian-corpus/<data>-<tema>.md   (append, mai overwrite)
  → si indicizza in maximilian/corpus-index (BACKBONE)
  → da quel momento gli agenti MX-* ragionano anche su di essa
```
Il corpus **cresce**, non si riscrive: backup → append → log (pattern Memory-first, ADR-002).
Nessuna direttiva di Max va persa o compressa.

---

## WF-CALIBRAZIONE — le correzioni di Max affinano i test §1
Quando Max **corregge un verdetto** dell'organo (ribalta un APPROVA/RIFAI, o dice "qui avrei deciso così"):
```
correzione reale di Max
  → entra nel corpus (WF-CORPUS-INGEST) E in maximilian/calibrazione (BACKBONE)
  → i test §1 (i criteri di giudizio) si AFFINANO su quel caso
  → il prossimo verdetto è più vicino a Max
```
È il loop di miglioramento: **l'organo si avvicina a Max nel tempo**, invece di restare fermo a un'istantanea.

---

## I tratti distillati §1 — chiave di lettura, NON sostituto del corpus
Il dossier §1 distilla 8 tratti in tabella — **Scala, Standard chirurgico, Visibilità totale, Velocità senza
minuzie, Ambizione disciplinata, Delega aggressiva, Anticipazione, "Fai di più del chiesto"** — ognuno con il
suo test ("è grande quanto dovrebbe? o è un giocattolo?"). Quei tratti sono una **mappa veloce** per orientare
il giudizio, **non un rimpiazzo** del corpus: il verdetto finale si motiva citando il testo integrale, non lo
slogan. La tabella aiuta a *leggere* il corpus; il corpus resta la verità. Se tratto e corpus divergono,
**vince il corpus** (e WF-CALIBRAZIONE aggiorna il tratto).

---

## Navigazione
- Porta d'ingresso → [[ECOSISTEMA.md]] · Infrastruttura → [[BACKBONE.md]]
- Corpus reale → `company/Memory/maximilian-corpus/` · Indice → `maximilian/corpus-index` (BACKBONE)
- Fonte di verità → [[12-DOSSIER-MAXIMILIAN]] §7 (corpus) · §1 (tratti) · §8 (state/calibrazione)
- Agenti che leggono il corpus → `Agenti/` (MX-MEMORY in primis) · Skill → `Skill/maximilian-voice`
