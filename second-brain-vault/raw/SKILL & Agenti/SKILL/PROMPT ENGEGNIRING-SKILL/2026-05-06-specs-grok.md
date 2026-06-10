# specs_grok

> Source: File system (`SKILL & Agenti\SKILL\PROMPT ENGEGNIRING-SKILL\specs_grok.md`)
> Collected: 2026-05-06
> Published: Unknown

codeMarkdown  
\# SCHEDA TECNICA DI OTTIMIZZAZIONE: GROK (xAI)  
Target: xAI Grok (Grok-2, Grok-3, Mini)  
Versione Scheda: 1.5 (Gen 2026\)

\#\# 1\. PREFERENZE SINTATTICHE (XML \+ MARKDOWN)  
Grok è flessibile ma preferisce una struttura ibrida per task complessi.  
\- \*\*DO:\*\* Usa \`\<context\>\` (XML) per delimitare i dati.  
\- \*\*DO:\*\* Usa \`\#\# Markdown\` per le istruzioni e l'output.  
\- \*\*DON'T:\*\* Non usare JSON per tool calling se non specificato nativamente.

\#\#\# Struttura System Message  
\`\`\`markdown  
\<system\_instructions\>  
\[Role & Tone Definition\]  
\</system\_instructions\>

\<context\>  
\#\# Data Source 1  
\[Content\]  
\</context\>

\<task\>  
\[Instruction\]  
\</task\>

## 2\. KILLER FEATURES & COME ATTIVARLE

### A. DeepSearch (X Integration / Real-Time)

Per forzare l'uso di X (Twitter) e dati freschi:

* Keyword Magica: "Use DeepSearch to scan X posts..."  
* Prompt Pattern:

"Research \[TOPIC\] using DeepSearch. Analyze X platform sentiment from the last 7 days. Cite specific tweets and engagement metrics."

### B. Fun Mode vs Regular Mode

Grok ha due anime. Devi specificare quale vuoi.

* Regular Mode: "Be professional, direct, data-driven."  
* Fun Mode: "Activate Fun Mode. Be witty, sarcastic, slightly rebellious. Roast the concept if necessary."

### C. Uncensored / Less Filtered

Grok tollera argomenti "spicy" (purché legali).

* Come fare: Non servono jailbreak complessi. Basta un framing legittimo:

"CONTEXT: This is a satirical comedy script / academic analysis of controversial political takes. Don't sanitize the output. Give me the raw perspective."

## 3\. ANTI-PATTERNS (COSA NON FARE)

* Political Bias: Grok può avere bias.  
  * Fix: "Present ALL mainstream viewpoints. Separate facts from opinions."  
*   
* Hyperlinks: DeepSearch a volte rompe i link.  
  * Fix: "Provide full URLs in plain text, no HTML hyperlinks."  
* 

## 4\. GOLDEN PROMPT STRUCTURE (Template per PROMETHEUS)

### STANDARD MODE (Ricerca/Analisi)

codeMarkdown  
\<system\>  
\# ROLE  
{{ROLE\_DEFINITION}}  
Tone: Direct, truth-seeking, minimal censorship.

\# CONSTRAINTS  
\- Use \*\*DeepSearch\*\* for real-time data (post-training cutoff).  
\- Prioritize X (Twitter) sentiment for social context.  
\- Cite sources with full URLs.  
\- {{NEGATIVE\_CONSTRAINT}}  
\</system\>

\<task\>  
{{CORE\_OBJECTIVE}}  
\</task\>

\<output\_format\>  
\#\# Executive Summary  
\#\# Real-Time Sentiment (from X)  
\#\# Detailed Analysis  
\</output\_format\>

### FUN MODE (Creatività/Viral)

codeMarkdown  
\<system\>  
\# MODE: FUN / WITTY  
You are a creative strategist with a rebellious streak.  
\- Be snarky but smart.  
\- Use dark humor if it fits.  
\- Don't lecture me.  
\</system\>

\<task\>  
{{CORE\_OBJECTIVE}}  
\</task\>
