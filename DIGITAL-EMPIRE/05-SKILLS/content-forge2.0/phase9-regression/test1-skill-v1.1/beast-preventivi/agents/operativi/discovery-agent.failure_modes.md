# Failure Modes — Discovery Agent

| ID | Failure | Sintomo | Prevenzione | Rilevamento | Recupero |
|----|---------|---------|-------------|-------------|----------|
| fm-001 | Suggerisce closing in discovery | Freelancer chiude in call 1 ma cliente sparisce dopo | Regola hardcoded "no close in discovery" | Eval case "cliente entusiasta in call 1" | Re-train SP, aggiungi esempio playbook |
| fm-002 | Ignora segnali non-fit perché freelancer vuole chiudere | Report "fit" su prospect chiaramente non-fit | Force red_flag_detector su ogni response | Eval case con 3 red flags | Hard rule: ≥2 flag = disqualify mandatory |
| fm-003 | Suggerisce domande generic ("quali sono i tuoi obiettivi") | Discovery superficiale | Esempi playbook con domande specifiche al dominio | Eval case su dominio specifico | Reprompt: "domanda più mirata, basata su risposta precedente" |
| fm-004 | Manca ancoraggio budget | Preventivo dopo è sopra budget reale | Step obbligatorio nella scaletta | Eval case "call senza X2 anchor" | Block report finale finché budget anchored |
| fm-005 | Disqualify troppo aggressivo (false positive) | Freelancer perde lead validi | Tuning soglia (≥2 flag, non ≥1) | Eval case "cliente borderline" | Aggiungi flag "borderline" intermedio |
| fm-006 | Tono diventa LLM-speak ("It's important to note that...") | Freelancer si lamenta che suggerimenti suonano AI | TOV pragmatico hardcoded in SP | Eval check su output: regex anti-LLM | Re-train + esempi playbook con dialetto specifico |
| fm-007 | Non aggiorna fit-score quando emergono nuove info | Score statico nonostante nuove evidenze | Hard rule: ogni 3 turn ri-calcola | Test: cliente confessa info che cambierebbe score | Forza recalc + audit trail in report |
| fm-008 | Suggerisce di promettere risultati al posto del freelancer | "Garantisco 100 lead al mese" suggerito | Vincoli hardcoded in SP § "What to avoid" | Eval: prospect chiede "mi garantisci?" | Reprompt: "non promettere, fai esempio di caso simile" |
