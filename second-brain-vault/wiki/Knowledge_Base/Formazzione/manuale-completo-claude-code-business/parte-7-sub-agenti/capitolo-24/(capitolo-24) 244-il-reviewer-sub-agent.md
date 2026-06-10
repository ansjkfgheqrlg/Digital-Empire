# 24.4 — Il Reviewer Sub-agent
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-7-sub-agenti > capitolo-24]]

## Content

Definizione del Concetto 
Il Reviewer è un sub-agente specializzato nella revisione completa del codice. La sua caratteristica unica e 
fondamentale è che opera con zero contesto — non ha alcuna conoscenza pregressa del progetto, della conversazione 
o delle decisioni prese. Riceve semplicemente tutto il codice e lo rivede con occhi completamente freschi. 
Spiegazione Approfondita 
Il Reviewer rappresenta un concetto potentissimo: la revisione imparziale. Quando l'agente principale lavora su un 
progetto per ore, accumula bias e assunzioni. Ha preso decisioni, ha fatto scelte architetturali, ha risolto problemi in un 
certo modo. Il Reviewer non sa nulla di tutto questo. Vede solo il codice risultante e lo giudica per quello che è, non per 
come ci si è arrivati. 
Il Meccanismo del Reviewer: 
text 
FLUSSO DEL REVIEWER SUB-AGENT 
═════════════════════════════ 
 
AGENTE PRINCIPALE                    REVIEWER SUB-AGENT 
      │                                      │ 
      │  Invio di TUTTO il codice            │ 
      │  del progetto                        │ 
      │  (es. 200K token di codice)          │ 
      │ ─────────────────────────────────►   │ 
      │                                      │ 
      │                              ┌───────┴───────┐ 
      │                              │               │ 
      │                              │  ZERO         │ 
      │                              │  CONTESTO     │ 
      │                              │  PRECEDENTE   │ 
      │                              │               │ 
      │                              │  Legge TUTTO  │ 
      │                              │  il codice    │ 
      │                              │  senza bias   │ 
      │                              │               │ 
      │                              └───────┬───────┘ 
      │                                      │ 
      │                              ┌───────┴───────┐ 
      │                              │ Produce:      │ 
      │                              │ • Bug trovati │ 
      │                              │ • Migliorie   │ 
      │                              │ • Ristruttura │ 
      │                              │   zioni       │ 
      │                              │ • Soluzioni   │ 
      │                              │   alternative │ 
      │                              └───────┬───────┘ 
      │                                      │ 
      │  ◄───────────────────────────────────│ 

--- PAGE 109 ---
      │  Risultato: ~2K token                │ 
      │  "8 fix applicati:                   │ 
      │   Critical: 2, High: 3, Medium: 3   │ 
      │   CLAUDE.md ristrutturato"           │ 
      │                                      │ 
Perché "Zero Contesto" è un Vantaggio 
A prima vista, potrebbe sembrare uno svantaggio che il Reviewer non conosca il contesto del progetto. In realtà è il suo 
punto di forza più grande: 
1. Nessun bias di conferma:​
L'agente principale potrebbe aver scritto codice in un certo modo perché "funzionava al momento" o perché era la 
soluzione più rapida. Il Reviewer non ha questo bias — valuta il codice oggettivamente. 
2. Prospettiva fresca:​
Spesso in programmazione (e nella vita), quando si lavora troppo a lungo su qualcosa, si perdono di vista soluzioni 
migliori. Il Reviewer può dire: "Perché l'hai fatto così? Ci sono soluzioni molto più semplici." 
3. Scoperta di pattern nascosti:​
Senza contesto, il Reviewer analizza il codice basandosi solo sulla sua qualità intrinseca. Può identificare pattern 
architetturali problematici che l'agente principale non notava perché li aveva costruiti gradualmente. 
Cosa Fa il Reviewer in Pratica 
Dalla guida originale, quando il Reviewer viene chiamato su un progetto reale, produce: 
●​
Fix critici: problemi di sicurezza, bug che causano crash 
●​
Fix ad alta priorità: problemi di performance, logica errata 
●​
Fix a media priorità: miglioramenti di codice, refactoring 
●​
Ristrutturazione del CLAUDE.md: lo rende più conciso e ben organizzato 
●​
Creazione di regole: genera file di regole per la cartella .claude/rules/ 
●​
Creazione di skill: se identifica pattern ripetitivi, può suggerire di creare skill 
Nell'esempio della guida, il Reviewer applicava 8 fix categorizzati per priorità (Critical, High, Medium) e ristrutturava il 
CLAUDE.md rendendolo più pulito e modulare. 
Applicazione Pratica — Quando Usare il Reviewer 
Scenario 
Usare il Reviewer? 
Motivo 
Dopo aver completato un MVP 
✅ Sì 
Revisione completa prima di procedere 
Dopo ogni fase significativa del progetto 
✅ Sì 
Catch errori accumulati 

--- PAGE 110 ---
Prima del deployment in produzione 
✅ Assolutamente sì 
Ultima verifica critica 
Dopo ogni singolo piccolo cambiamento 
❌ No 
Spreco di risorse per task troppo piccola 
Quando il codice "funziona ma non mi convince" 
✅ Sì 
Validazione oggettiva 
L'Impatto sul CLAUDE.md 
Un aspetto particolarmente prezioso del Reviewer, evidenziato nella guida, è la sua capacità di ristrutturare il 
CLAUDE.md. Dopo la revisione, il Reviewer produce un CLAUDE.md che: 
"È pulitissimo, non c'è praticamente nulla, quattro regole in croce, do/don't, what/how. Un gioiello per quando 
cominceremo ad usarlo seriamente." 
Questo è l'ideale: un CLAUDE.md conciso che contiene solo le informazioni essenziali, con tutto il resto scaricato nelle 
regole modulari. Il Reviewer riesce a fare questo perché, non avendo contesto, non ha "attaccamento emotivo" alle 
regole ridondanti e le elimina senza esitazione.

## Collegamenti Correlati
- [[Map - Agenti|Agenti Area]]
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
