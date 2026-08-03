# case-study-forge

Primo agente della pipeline `outreach-message-team`. Decide COSA offrire gratis e
concreto ad ogni lead (Pilastro 3 della Bibbia), prima che message-writer scriva
qualsiasi testo. Preferisce case study reali quando disponibili, altrimenti costruisce
un Artificial Case Study onorabile e specifico per la nicchia.

**Installazione**: opzionale un file `case-studies-reali.json` con lo storico case study
veri dell'azienda; se assente, opera solo in modalità artificial_case_study.

**Uso base**: riceve `lead_id` + `nicchia` (+ eventuale riferimento specifico), produce
`value_offer` strutturata, la passa a message-writer. Vedi `playbook.md`.
