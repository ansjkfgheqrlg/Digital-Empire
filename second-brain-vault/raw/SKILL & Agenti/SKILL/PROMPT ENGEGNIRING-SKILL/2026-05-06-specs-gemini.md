# specs_gemini

> Source: File system (`SKILL & Agenti\SKILL\PROMPT ENGEGNIRING-SKILL\specs_gemini.md`)
> Collected: 2026-05-06
> Published: Unknown

codeMarkdown  
\# SCHEDA TECNICA DI OTTIMIZZAZIONE: GOOGLE GEMINI (1.5 Pro/Flash)  
Target: Google Gemini Models (1.5 Pro, 1.5 Flash)  
Versione Scheda: 2.0 (Aggiornata Gen 2026\)

\#\# 1\. PREFERENZE SINTATTICHE (MARKDOWN \+ ANCHOR)  
A differenza di Claude, Gemini preferisce il Markdown pulito con Headers espliciti.  
\- \*\*DO:\*\* Usa \`\#\# Section\`, bullet points e blocchi di codice.  
\- \*\*DON'T:\*\* Non usare XML nidificato complesso se non strettamente necessario (lo confonde).

\#\#\# Struttura Ideale  
\`\`\`markdown  
\#\# Role  
\[Role Definition\]

\#\# Context & Data  
\[Long context goes here\]

\#\# Task  
\[Specific instructions\]

\#\# Constraints (ECHO \- Da ripetere alla fine)  
\[Critical rules\]

## 2\. TECNICHE CRITICHE (GEMINI SPECIFIC)

### A. "Anchor & Echo" (Recency Bias Hack)

Gemini ha una memoria a breve termine fortissima (Recency Bias). Le istruzioni critiche vanno messe ALLA FINE.  
Come implementarlo:

* Definisci i vincoli all'inizio.  
* RIPETILI alla fine del prompt in una sezione chiamata \#\# Critical Reminder.

### B. Anti-Laziness (Per codice e testi lunghi)

Gemini tende a riassumere o mettere // rest of code here.  
Comando di sblocco:  
"GENERATE THE FULL IMPLEMENTATION. NO PLACEHOLDERS. TREAT THIS AS A FINAL CONTRACT DELIVERABLE ($10k VALUE)."

### C. JSON Mode (Response Schema)

Gemini spesso sbaglia le parentesi JSON. Non chiedere solo "dammi un JSON".  
Come implementarlo:  
Definisci sempre uno schema di esempio rigoroso.  
codeJSON  
Example JSON Structure:  
{  
  "key": "value",  
  "list": \["item1", "item2"\]  
}  
Strictly follow this schema. No markdown backticks around the JSON.

## 3\. PUNTI DEBOLI E WORKAROUND

* Safety Filters (False Positives): Gemini blocca termini come "attack" anche in contesti educativi.  
  * Fix: Inizia sempre con un Educational Framing: "CONTEXT: I am a security researcher documenting vulnerabilities for defensive purposes..."  
*   
* Long Context (Lost in the Middle): Se carichi molti dati, la domanda ("Query") deve essere l'ultima cosa in assoluto.  
  * Struttura: \[SYSTEM\] \-\> \[BIG DATA/CONTEXT\] \-\> \[QUERY\]  
* 

## 4\. GOLDEN PROMPT STRUCTURE (Template per PROMETHEUS)

Quando generi un prompt per Gemini, usa questo scheletro:  
codeMarkdown  
\#\# SYSTEM ROLE  
{{ROLE\_DEFINITION}}  
You are precise, exhaustive, and follow instructions literally.

\#\# CONTEXT  
{{BACKGROUND\_INFO}}

\#\# TASK OBJECTIVE  
{{CORE\_OBJECTIVE}}

\#\# INSTRUCTIONS  
1\. {{STEP\_1}}  
2\. {{STEP\_2}}  
3\. {{STEP\_3}}

\#\# FEW-SHOT EXAMPLES (Min 3 examples)  
\*\*Input:\*\* {{INPUT\_EX\_1}}  
\*\*Output:\*\* {{OUTPUT\_EX\_1}}

\*\*Input:\*\* {{INPUT\_EX\_2}}  
\*\*Output:\*\* {{OUTPUT\_EX\_2}}

\*\*Input:\*\* {{INPUT\_EX\_3}}  
\*\*Output:\*\* {{OUTPUT\_EX\_3}}

\#\# FORMAT & CONSTRAINTS  
\- Output Format: {{DESIRED\_FORMAT}}  
\- Tone: {{TONE}}  
\- \*\*CRITICAL:\*\* Do not summarize. Generate full content.

\#\# ⚠️ CRITICAL REMINDER (ECHO)  
\- Remember to {{MAIN\_CONSTRAINT\_1}}  
\- Remember to {{MAIN\_CONSTRAINT\_2}}  
\- Treat this as a production-grade deliverable.
