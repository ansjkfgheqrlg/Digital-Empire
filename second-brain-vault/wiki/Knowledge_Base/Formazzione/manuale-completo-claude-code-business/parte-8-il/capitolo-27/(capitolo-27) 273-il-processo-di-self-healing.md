# 27.3 — Il Processo di Self-Healing
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-8-il > capitolo-27]]

## Content

Definizione del Concetto 
Il self-healing (auto-guarigione) è il processo attraverso il quale una skill è in grado di auto-correggersi quando qualcosa 
va storto durante l'esecuzione. Questo processo è reso possibile dalla combinazione del file skill.md (che contiene le 
istruzioni per la gestione degli errori) e del CLAUDE.md (che contiene le regole generali del progetto). 
Spiegazione Approfondita 
Quando uno script all'interno di una skill fallisce o produce un risultato non conforme, il processo di self-healing si attiva: 
text 
PROCESSO DI SELF-HEALING 
════════════════════════ 
 
ESECUZIONE NORMALE: 
    skill.md → script_1.py → script_2.py → script_3.py → OUTPUT ✅ 
                                                           
QUANDO QUALCOSA VA STORTO: 
    skill.md → script_1.py → script_2.py ← ERRORE! ❌ 
                                │ 
                                ▼ 
                    ┌───────────────────────┐ 
                    │ SELF-HEALING ATTIVATO │ 
                    │                       │ 
                    │ 1. Claude legge il    │ 
                    │    CLAUDE.md per      │ 
                    │    capire cosa fare   │ 
                    │                       │ 
                    │ 2. Identifica         │ 
                    │    l'errore           │ 
                    │                       │ 
                    │ 3. Applica la         │ 
                    │    correzione         │ 
                    │                       │ 
                    │ 4. Aggiorna la        │ 
                    │    skill.md           │ 
                    │    (la checklist)     │ 
                    │                       │ 
                    │ 5. Ri-esegue lo      │ 
                    │    script corretto    │ 
                    └───────────┬───────────┘ 
                                │ 
                                ▼ 
                    script_2.py (corretto) → script_3.py → OUTPUT ✅ 
L'aspetto più importante del self-healing è il Passo 4: Claude aggiorna la checklist (skill.md) per includere la correzione. 
Questo significa che la prossima volta che la skill viene eseguita, l'errore non si ripresenterà perché la checklist è stata 
migliorata. 
Questo crea un ciclo virtuoso di miglioramento continuo: 
text 
CICLO DI MIGLIORAMENTO DELLA SKILL 
═══════════════════════════════════ 
 
    Esecuzione 1 → Errore A → Fix A → Skill aggiornata 
                                          │ 
    Esecuzione 2 → Errore B → Fix B → Skill aggiornata 
                                          │ 
    Esecuzione 3 → Nessun errore → Output perfetto 
                                          │ 
    Esecuzione 4 → Nessun errore → Output perfetto 

--- PAGE 133 ---
                                          │ 
    ...la skill diventa sempre più robusta nel tempo 
Perché il Self-Healing è Fondamentale 
Senza self-healing, ogni errore richiederebbe l'intervento umano. Con il self-healing: 
1.​
Riduzione dell'intervento umano: la skill si ripara da sola nella maggior parte dei casi 
2.​
Miglioramento continuo: ogni errore rende la skill più robusta 
3.​
Scalabilità: potete lanciare skill e andare a fare altro, sapendo che si auto-correggeranno 
4.​
Documentazione automatica: le correzioni vengono codificate nella checklist, creando documentazione 
vivente 
Il Ruolo del CLAUDE.md nel Self-Healing 
"Quand'è che il file skill.md entra in funzione? Quando qualcosa va storto. Molti confondono perché molti dicono 'La skill 
è il file markdown' — la skill non è il file markdown." 
Il CLAUDE.md fornisce il contesto generale che Claude usa per capire come reagire agli errori. La skill.md fornisce la 
procedura specifica per la skill corrente. Insieme, danno a Claude abbastanza informazioni per: 
●​
Diagnosticare cosa è andato storto 
●​
Decidere la strategia di correzione 
●​
Applicare il fix 
●​
Verificare che il fix funzioni 
●​
Aggiornare la documentazione per prevenire recidive

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
- [[Map - General|General Area]]
