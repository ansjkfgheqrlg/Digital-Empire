# ✂ CRITICA 3 — VERITÀ E OMISSIONI

> **Oggetto:** `V1-PIANO-GENERALE.md` (522 righe, letto per intero)
> **Angolo:** la verità delle affermazioni e ciò che manca — numeri, prove, contraddizioni coi censimenti chiusi, omissioni, legge L1/L7
> **Revisore:** indipendente, non l'autore del piano
> **Data:** 2026-09-06
> **Metodo:** ogni rilievo scritto appena formulato (append), ogni rilievo con prova misurata

---

### R-1 — V1 rimanda due volte a un §30 che non esiste  [MEDIO]
- **Tipo:** NUMERO SBAGLIATO (riferimento interno mal citato)
- **Dove:** V1 riga 41 («È dichiarato qui e ripreso in §30») e riga 391 («per il limite di sessione (§30)»)
- **Cosa dice il piano:** che la ripresa dei censimenti incompleti e la caduta del doom bot dell'addestramento sono trattate «in §30».
- **Cosa dice la realtà:** V1 finisce a §27 («Cosa V1 NON copre»). Non esistono §28, §29 né §30 — verificato con `grep -n "^## " V1-PIANO-GENERALE.md`: ultima sezione a riga 507.
- **Perché conta:** in un piano che sarà riletto da forze diverse in sessioni diverse, un puntatore interno rotto manda a cercare una sezione che non c'è. È esattamente la «REGOLA PUNTATORI: MAI STALE» del CLAUDE.md di questo repo.
- **Cosa proporresti:** correggere i due rimandi in «§27» (o nella sezione reale che tratta la ripresa).

