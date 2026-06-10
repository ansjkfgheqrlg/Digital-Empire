# 18.2 — Spiegazione Espansa
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-5- > capitolo-18-plan-mode-]]

## Content

Il Flusso del Plan Mode 
text 
FLUSSO COMPLETO: 
 
FASE 1 — INPUT 
Utente scrive un prompt con la richiesta completa 
     ↓ 
 
FASE 2 — ANALISI 
Claude Code analizza: 
├── Il prompt dell'utente 
├── Il CLAUDE.md del progetto 
├── I file esistenti nel progetto 
├── Le rules nella cartella .claude 
├── Le risorse disponibili (API, tools, MCP) 
└── Le skill applicabili 
     ↓ 
 
FASE 3 — PIANIFICAZIONE 
Claude Code produce una checklist strutturata: 
├── Subtask 1: [descrizione] 
├── Subtask 2: [descrizione] 
├── Subtask 3: [descrizione] 
├── ... 
├── Subtask N: [descrizione] 
└── Ordine di esecuzione e dipendenze 
     ↓ 
 
FASE 4 — REVISIONE 
L'utente rivede la checklist: 
├── ✅ "Questo va bene" 
├── ✅ "Questo va bene" 
├── ❌ "Questo non va bene — cambia così" 
├── ⚠️ "Qui manca qualcosa — aggiungi questo" 
├── ✅ "Questo va bene ma potremmo migliorarlo — cambialo" 
└── Feedback inviato a Claude Code 
     ↓ 
 
FASE 5 — REVISIONE ITERATIVA 
Claude Code aggiorna il piano in base al feedback 
L'utente rivede di nuovo 
Si ripete fino a quando l'utente è soddisfatto 
     ↓ 
 
FASE 6 — APPROVAZIONE 
L'utente approva il piano finale 
     ↓ 
 
FASE 7 — ESECUZIONE 
Claude Code esegue il piano (tipicamente in Accept Edits o Bypass Permission) 
L'autore è molto chiaro sull'approccio alla revisione: "Plan mode significa semplicemente: continuiamo ad insistere fino 
alla morte sulla nostra checklist fino a che non siamo soddisfatti. E poi, una volta che abbiamo pianificato il tutto, allora 
muoviamoci ad accettare gli edits e ad andare a costruire." 
La parola chiave è "fino alla morte" — non è un'esagerazione. La qualità del piano è direttamente proporzionale al 
tempo investito nella sua revisione.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
