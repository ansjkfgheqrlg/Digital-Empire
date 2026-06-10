# 27.4 — Skill vs Script: La Natura Deterministica
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-8-il > capitolo-27]]

## Content

Definizione del Concetto 
Gli script all'interno di una skill sono deterministici — producono sempre lo stesso output dato lo stesso input. Questo è 
in contrasto con le risposte dell'LLM, che sono non deterministiche (possono variare anche con lo stesso prompt). 
Comprendere questa distinzione è fondamentale per costruire skill affidabili. 
Spiegazione Approfondita 
La guida originale introduce questo concetto quando parla degli hook e lo rafforza parlando delle skill: 
"Questi hook possono essere anche il momento in cui attiviamo un sub-workflow. Sono distaccati dal funzionamento 
dell'LLM. Non sono più legati alla token consumption. Partono ad evento e sono codice, quindi non sono qualcosa di 
non deterministico." 
Lo stesso principio si applica agli script delle skill. Quando Claude esegue uno script Python per caricare un video su 
YouTube, quel codice: 
●​
Non "interpreta" cosa fare — segue istruzioni precise 
●​
Non "allucinà" — esegue operazioni definite 
●​
Non "varia" il risultato — dato lo stesso input, produce lo stesso output 
●​
Non consuma token dell'LLM — è codice tradizionale 

--- PAGE 134 ---
Questo è il motivo per cui le skill sono così potenti: combinano la flessibilità dell'LLM (per capire cosa l'utente vuole e 
orchestrare il processo) con la affidabilità del codice tradizionale (per eseguire le operazioni effettive). 
text 
CONFRONTO: APPROCCIO LLM-ONLY vs SKILL 
═══════════════════════════════════════ 
 
APPROCCIO LLM-ONLY (senza skill): 
┌────────────────────────────────────────────┐ 
│ Utente: "Pubblica questo video su YouTube" │ 
│                                            │ 
│ Claude LLM:                                │ 
│ → Interpreta la richiesta (non determin.)  │ 
│ → Cerca di capire come fare (non determin.)│ 
│ → Prova a scrivere codice (non determin.)  │ 
│ → Esegue il codice (deterministico)        │ 
│ → Verifica il risultato (non determin.)    │ 
│                                            │ 
│ Risultato: VARIABILE ogni volta            │ 
│ Token consumati: MOLTI                     │ 
│ Tempo: LUNGO                               │ 
└────────────────────────────────────────────┘ 
 
APPROCCIO CON SKILL: 
┌────────────────────────────────────────────┐ 
│ Utente: "Usa la skill publish per YouTube" │ 
│                                            │ 
│ Claude + Skill:                            │ 
│ → Legge skill.md (checklist fissa)         │ 
│ → Valida gli input (checklist fissa)       │ 
│ → Esegue upload_youtube.py (determin.)     │ 
│ → Verifica il risultato (checklist fissa)  │ 
│                                            │ 
│ Risultato: CONSISTENTE ogni volta          │ 
│ Token consumati: POCHI                     │ 
│ Tempo: BREVE                               │ 
└────────────────────────────────────────────┘ 
L'Implicazione per la Costruzione di Skill 
Questa comprensione della dualità LLM/codice ha implicazioni dirette per come costruite le vostre skill: 
●​
Tutto ciò che può essere codificato come script, DEVE essere codificato come script: upload di file, chiamate 
API, trasformazioni di dati, manipolazione di file — tutto questo deve essere codice deterministico 
●​
Solo ciò che richiede ragionamento resta nell'LLM: interpretazione dell'input utente, decisioni creative, 
gestione degli errori imprevisti, personalizzazione del tono di voce 
●​
La skill.md fa da ponte: coordina quando usare l'LLM e quando usare gli script

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
