> Fonte: PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md sez. 2 (L4 — T-AVATAR, reparto L2.1)

# T-AVATAR — Target Avatar Builder

> Funzione L4 · Reparto: L2.1 Copywriting · Ecosistema: 04-MARKETING
> Ecosistema: `company/Ecosistemi/04-MARKETING/ECOSISTEMA.md`

---

## Identità

| Campo | Valore |
|---|---|
| ID funzione | T-AVATAR |
| Reparto owner | L2.1 Copywriting |
| Ruolo | Costruzione buyer persona completa per ICP — prerequisito di ogni copy |
| Usato da | MKT-Conductor (spawna T-AVATAR se icp mancante nel contratto), A2 Target Analyst, tutti i workflow |
| Tier modello | sonnet |

---

## Responsabilità

1. **Prerequisito non derogabile:** nessun copy si scrive senza avatar. Se il contratto arriva senza `icp`, MKT-Conductor spawna T-AVATAR come primo step.
2. Produrre avatar completo: demografia, obiettivi, frustrazioni, obiezioni, linguaggio tipico, awareness level, canali frequentati, trigger di acquisto.
3. Generare la **language map**: le parole esatte che l'ICP usa per descrivere il suo problema (anti-AI-slop: le headline e i copy usano queste parole, non generici).
4. Salvare l'avatar nel namespace `marketing/avatars/{icp}` per riuso cross-ecosistema.
5. Aggiornare l'avatar quando arrivano nuovi dati da AN4 (Insight Distiller) o da 08-INTELLIGENCE.

---

## I/O

**Input:**
- Brief ICP (minimo: settore, prodotto/servizio, obiettivo del copy)
- Eventuali dati esistenti da 08-INTELLIGENCE (ricerca ICP, trend)
- Proof e case study disponibili (segnali di chi ha già comprato)

**Output:**
```json
{
  "icp_id": "slug-icp",
  "demografia": "...",
  "obiettivi": ["..."],
  "frustrazioni": ["..."],
  "obiezioni_top5": ["..."],
  "awareness_level": "unaware | problem-aware | ...",
  "language_map": {"problema": "parole esatte", "desiderio": "parole esatte"},
  "trigger_acquisto": ["..."],
  "canali": ["..."],
  "avatar_path": "marketing/avatars/{icp}"
}
```

---

## Come ragiona

1. Parte dai dati disponibili (briefing, research 08-INTEL, testimonianze). Mai inventare tratti senza evidenza.
2. Classifica l'awareness level (unaware → most-aware): determina quanto APSOC pesa su A+P vs O+CTA.
3. Costruisce la language map da fonti reali (recensioni, forum, exit survey, testimonianze).
4. Segnala i gap conoscitivi ("mancano dati su trigger di acquisto — suggerito: exit survey o call con 3 clienti").

---

## KPI

| KPI | Definizione |
|---|---|
| Avatar con language map completa | % avatar che includono parole esatte dell'ICP (non generiche) |
| Riuso avatar cross-ecosistema | n. namespace `marketing/avatars/{icp}` letti da altri agenti |

---

## Connessioni

- `company/Ecosistemi/04-MARKETING/Reparti/L2-1-Copywriting.md` — reparto owner
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-A2-target-analyst.md` — agente L5 che esegue
- `company/Ecosistemi/04-MARKETING/Agenti/MKT-0-conductor.md` — spawna T-AVATAR se icp mancante
- `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md` §1.2 (contratto), §2 (L2.1 — T-AVATAR), §7 (namespace)

*Fonte: dossier 04 §1.2, §2 (L2.1), §7 · Aggiornato: 2026-06-12*
