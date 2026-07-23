---
name: skill-forge-factory
description: Trasforma appunti grezzi, idee, trascrizioni video e logiche operative non strutturate in file SKILL.md eseguibili perfetti che agenti AI (Gemini, Claude, GPT-4o) possono eseguire istantaneamente con frontmatter YAML, obiettivi, trigger, regole ferree e workflow operativo.
---

# OBIETTIVO
Convertire qualsiasi testo grezzo (appunti, transcript, brainstorming) in un file SKILL.md chirurgico, validato su 5 dimensioni di qualità (score ≥8.0) e immediatamente eseguibile da agenti AI senza ambiguità, con architettura autorizzata e ingegneristica.

# TRIGGER
Questa skill si attiva quando:
- L'utente incolla appunti grezzi e scrive "[INSERISCI QUI I TUOI APPUNTI GREZZI O IL TRANSCRIPT]" o frasi simili
- L'utente menziona: "crea skill", "trasforma in SKILL.md", "fabbrica delle skill", "skill-forge"
- Il Planner rileva intent = skill-forge con confidence >0.7
- Input contiene pattern: idee non strutturate + richiesta di struttura operativa
- L'Analyst identifica raw_notes_structure.line_count >20 e assenza di struttura operativa

# REGOLE FERREE
1. Output deve contenere ESCLUSIVAMENTE il blocco codice markdown del file SKILL.md - zero introduzioni, zero saluti, zero spiegazioni fuori dal file
2. Frontmatter YAML obbligatorio in testa con `name:` (kebab-case) e `description:` (una frase ad alto ROI)
3. Struttura obbligatoria: # OBIETTIVO, # TRIGGER, # REGOLE FERREE, # WORKFLOW OPERATIVO - nessuna mancante
4. WORKFLOW OPERATIVO deve avere passi numerati 1,2,3 con sotto-step 1.1, 1.2 ecc - ogni step deve dichiarare input, azione, output
5. Stile autoritativo, chirurgico, ingegneristico - vietato linguaggio motivazionale fuffa
6. Se appunti grezzi contengono placeholder [INSERISCI...] sostituiscili con inferenza contestuale e logga assunzione
7. Validazione finale: file deve superare critic su Completezza ≥8, Actionability ≥8, Coerenza ≥9

# WORKFLOW OPERATIVO

## STEP 1: INTAKE & PARSING CHIRURGICO
1.1 Ricevi testo grezzo: estrai tutto dopo "[INSERISCI QUI..." fino a fine input
1.2 Esegui parsing entità:
   - Input: raw_notes (string)
   - Azione: regex per estrarre obiettivi impliciti (verbi: creare, generare, trasformare), vincoli (deve, non, mai), soggetti (target, servizio)
   - Output: JSON {objectives:[], constraints:[], entities:{}}
1.3 Check Memory L3: cerca strategie con use_case=skill-forge e success_rate ≥8.0 - se match >0.8 riusa pattern
1.4 Classifica complessità: Conta token grezzi -> <500 bassa, 500-1500 media, >1500 alta (attiva swarm multi-agente)

## STEP 2: ARCHITETTURA FILE SKILL.md
2.1 Genera `name`: kebab-case dal concetto core (es. "lead-nurturing-engine" non "skill bella")
   - Input: objectives[0]
   - Azione: lowercase, replace spazi con -, rimuovi stopwords
   - Output: skill_name
2.2 Genera `description`: una frase [verbo trasformazione + input + output + beneficiario] max 25 parole
2.3 Definisci # OBIETTIVO: una frase misurabile con metrica (es. "Generare 3 email APSOC con score ≥8.0 in <60s")
2.4 Definisci # TRIGGER: lista bullet con 4-6 condizioni concrete con esempi di frasi utente esatte
2.5 Distilla # REGOLE FERREE: max 7 vincoli assoluti non negoziabili scritti come "MAI..." o "SEMPRE..."

## STEP 3: COSTRUZIONE WORKFLOW OPERATIVO
3.1 Progetta 3-4 STEP principali con logica sequenziale:
   - STEP 1: Intake & Decomposizione (sempre con check memory)
   - STEP 2: Architettura / Generazione Core
   - STEP 3: Validazione & Refinement (con loop critique)
   - STEP 4: Output & Persistenza (salvataggio memory)
3.2 Per ogni STEP specifica sotto-task 1.1, 1.2 con formato Input->Azione->Output
3.3 Assegna agent responsabile per ogni STEP (planner, writer, analyst, critic, refiner, meta)
3.4 Aggiungi gestione errori: se score <7.5 -> loop refinement max 3x, se <4.0 -> restart da STEP 1

## STEP 4: GENERAZIONE & VALIDAZIONE FINALE
4.1 Assembla file completo: frontmatter YAML + 4 sezioni
4.2 Esegui auto-critique interno su 5 dimensioni:
   - Completezza: tutte le sezioni presenti?
   - Precisione: name kebab-case, trigger concreti?
   - Actionability: workflow eseguibile senza chiedere chiarimenti?
   - Output SOLO blocco markdown con file
4.3 Se score <7.5: applica Refiner e torna a 4.2 (max 3 iterazioni)
4.4 Salva in L3 Strategy Store come nuova skill pattern con success_rate = score
4.5 Output finale: restituisci SOLO ```markdown\n---\nname:...\n``` con file completo
