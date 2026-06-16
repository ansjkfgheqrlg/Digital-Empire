> Fonte: PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md sez. 2 (L4 — T-OBJECTIONS, reparto L2.1)

# T-OBJECTIONS — Objections Forge

> Funzione L4 · Reparto: L2.1 Copywriting · Ecosistema: 04-MARKETING
> Ecosistema: `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md`

---

## Identità

| Campo | Valore |
|---|---|
| ID funzione | T-OBJECTIONS |
| Reparto owner | L2.1 Copywriting |
| Ruolo | Costruzione CPB (Claim → Proof → Benefit) per ogni obiezione dell'ICP |
| Usato da | WF-COPY-FULL (sezione O di APSOC), WF-COPY-SALES-PAGE, WF-COPY-VSL, WF-EMAIL-WINBACK |
| Tier modello | sonnet |

---

## Responsabilità

1. Mappare le obiezioni tipiche dell'ICP (10 categorie: prezzo, tempo, trust, tecnica, risultati, concorrenza, urgenza, capacità, rischio, valore).
2. Per ogni obiezione costruire il blocco CPB: **Claim** (la risposta diretta), **Proof** (evidenza: dato, case study, garanzia), **Benefit** (cosa guadagna il lettore superando l'obiezione).
3. Garantire che ogni proof sia reale e verificabile: "prove non promesse" — claim senza proof bloccato.
4. Produrre anche le obiezioni per il win-back: il churn è un'obiezione non gestita (coordina con E1 Lifecycle Architect per WF-EMAIL-WINBACK).

---

## I/O

**Input:**
- Avatar ICP + language map (da A2 Target Analyst / T-AVATAR)
- Proof disponibili (case study, testimonianze, garanzie, dati)
- Formato copy di destinazione (sales page, email, vsl, win-back)

**Output:**
- Lista obiezioni classificata per frequenza e impatto sull'ICP
- Blocco CPB per ogni obiezione (testo copy-ready)
- Flag obiezioni senza proof disponibile (bloccanti → escalation committente)

---

## Come ragiona

1. Estrae obiezioni dal language map dell'ICP: usa le parole esatte del target (Barnum anti-pattern: niente frasi universali).
2. Classifica per peso (alta/media/bassa frequenza nel funnel).
3. Per ogni obiezione: cerca proof nel materiale fornito. Proof mancante → segnala come gap, non inventa.
4. Genera il blocco CPB rispettando la sequenza O prima di CTA (regola APSOC: P→S→O→CTA).

---

## KPI

| KPI | Definizione |
|---|---|
| Obiezioni coperte / obiezioni ICP note | Copertura del gap obiezioni per ICP |
| CPB con proof reale | % blocchi con evidenza verificabile (target: 100%) |

---

## Connessioni

- `company/Ecosistemi/04-MARKETING/Reparti/L2-1-Copywriting.md` — reparto owner
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-A6-objections-handler.md` — agente L5 che esegue
- `company/Ecosistemi/04-MARKETING/Funzioni/T-AVATAR.md` — ICP di input
- `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md` — standard APSOC
- `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` §2 (L2.1 — T-OBJECTIONS), §4c (win-back)

*Fonte: dossier 04 §2 (L2.1), §4c · Aggiornato: 2026-06-12*
