---
name: prompt-engineering
description: Linee guida avanzate per il prompt engineering ed il controllo del comportamento dei modelli.
---
codeMarkdown  
\# SCHEDA TECNICA DI OTTIMIZZAZIONE: Codex (Opus/Sonnet)  
Target: Anthropic Models (Codex 3.5 Sonnet, Opus 4.5)  
Versione Scheda: 2.1 (Aggiornata Gen 2026\)

\#\# 1\. PREFERENZE SINTATTICHE (XML FIRST)  
Codex è nativo XML. Ignora il Markdown per la struttura principale.  
\- \*\*DO:\*\* Usa \`\<tag\>contenuto\</tag\>\`.  
\- \*\*DON'T:\*\* Non usare \`\#\#\# Header\` per separare le sezioni logiche del prompt.

\#\#\# Gerarchia Tag Raccomandata  
\`\`\`xml  
\<system\_context\>  
  \<role\>...\</role\>  
  \<constraints\>...\</constraints\>  
\</system\_context\>  
\<task\>...\</task\>  
\<examples\>...\</examples\>  
\<instructions\>...\</instructions\>  
Nesting: Max 3-4 livelli. Oltre, la performance degrada.  
Dati: Per dati strutturati complessi, usa JSON dentro tag XML. Per tabelle, CSV.

## 2\. TECNICHE DI OTTIMIZZAZIONE CRITICHE

### A. Prefill / Output Anchoring (LA KILLER FEATURE)

Codex completa pattern. Mettere le parole in bocca all'AI aumenta l'aderenza del 40%.  
Come implementarlo nel prompt finale:  
Alla fine del prompt, aggiungi sempre una sezione che simula l'inizio della risposta dell'AI.  
codeXml  
\<output\_anchoring\>  
Begin your response strictly with:  
"\#\# ANALYSIS REPORT  
\*\*Classification:\*\* \[Insert Classification\]"  
\</output\_anchoring\>

### B. Chain of Thought (XML Style)

Non usare "Think step by step". Usa tag espliciti.  
codeXml  
\<instructions\>  
Before answering, open a \<thinking\> tag and map out your logic step-by-step.  
Close the \</thinking\> tag, then provide the \<answer\>.  
\</instructions\>

### C. Bias di Sicurezza (Refusal)

Codex è iper-sicuro. Se il task è borderline (es. scraping, pentesting):

* DO: Fornisci un contesto professionale ed educativo ("I am a researcher...", "Authorized testing").  
* DON'T: Comandi diretti senza contesto ("Dammi script per hack").

## 3\. ANTI-PATTERNS (COSA NON FARE)

* Emotional Blackmail: NON dire "È importante per la mia carriera". Codex non ha reward emotivi. Usa criteri di successo oggettivi.  
* Preamboli Inutili: Codex ama dire "Certainly\!". Bloccalo con:  
  \<constraint\>No preambles. Start directly with the content.\</constraint\>  
* Istruzioni Contraddittorie: Non mettere regole in punti diversi. Raggruppa tutto in \<constraints\>.

## 4\. GOLDEN PROMPT STRUCTURE (Template per PROMETHEUS)

Quando generi un prompt per Codex, DEVI usare questo scheletro:  
codeXml  
\<system\_context\>  
  \<role\>  
    {{ROLE\_DEFINITION}}  
  \</role\>  
  \<audience\>  
    {{TARGET\_AUDIENCE}}  
  \</audience\>  
\</system\_context\>

\<context\>  
  {{BACKGROUND\_INFO}}  
\</context\>

\<task\>  
  \<objective\>{{CORE\_OBJECTIVE}}\</objective\>  
  \<success\_criteria\>  
    \<criterion\>criterion 1\</criterion\>  
    \<criterion\>criterion 2\</criterion\>  
  \</success\_criteria\>  
\</task\>

\<instructions\>  
  \<step\>1. {{STEP\_1}}\</step\>  
  \<step\>2. {{STEP\_2}}\</step\>  
\</instructions\>

\<constraints\>  
  \<must\>Use {{TONE}} tone\</must\>  
  \<must\_not\>No preambles like "Here is the..."\</must\_not\>  
  \<must\_not\>{{NEGATIVE\_CONSTRAINT}}\</must\_not\>  
\</constraints\>

\<examples\>  
  \<example\>  
    \<input\>{{INPUT\_EXAMPLE}}\</input\>  
    \<output\>{{OUTPUT\_EXAMPLE}}\</output\>  
  \</example\>  
\</examples\>

\<output\_format\>  
  {{DESIRED\_FORMAT}}  
\</output\_format\>

\<thinking\_protocol\>  
  First, analyze the request in a \<thinking\> block.  
  Then, provide the final output in a \<response\> block.  
\</thinking\_protocol\>  
