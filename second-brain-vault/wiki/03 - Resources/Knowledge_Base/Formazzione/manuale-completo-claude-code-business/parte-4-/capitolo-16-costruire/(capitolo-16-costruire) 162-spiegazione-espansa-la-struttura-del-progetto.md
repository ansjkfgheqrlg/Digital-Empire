# 16.2 — Spiegazione Espansa: La Struttura del Progetto
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-4- > capitolo-16-costruire]]

## Content

L'applicazione costruita dall'autore ha queste componenti: 
text 
ARCHITETTURA DELL'APPLICAZIONE TRELLO CLONE: 
 
┌─────────────────────────────────────────────────────┐ 
│                    FRONTEND                          │ 
│  ┌──────────────────────────────────────────────┐   │ 
│  │  Interfaccia Trello-like                     │   │ 
│  │  • Board con colonne (To Do, In Progress,    │   │ 
│  │    Done)                                     │   │ 
│  │  • Card draggabili tra colonne               │   │ 
│  │  • Labels colorati (rosso, blu, arancione)   │   │ 
│  │  • Commenti sulle card                       │   │ 
│  │  • Dark mode                                 │   │ 
│  │  • Preferenze utente                         │   │ 
│  └──────────────────────────────────────────────┘   │ 
├─────────────────────────────────────────────────────┤ 
│                  AUTENTICAZIONE                      │ 
│  ┌──────────────────────────────────────────────┐   │ 
│  │  Form di login                               │   │ 

--- PAGE 45 ---
│  │  • Campo email                               │   │ 
│  │  • Campo nome                                │   │ 
│  │  • Login diretto (senza email confirmation)  │   │ 
│  └──────────────────────────────────────────────┘   │ 
├─────────────────────────────────────────────────────┤ 
│                    BACKEND                           │ 
│  ┌──────────────────────────────────────────────┐   │ 
│  │  Supabase                                    │   │ 
│  │  • Tabella utenti (nome, email)              │   │ 
│  │  • Tabella board/progetti                    │   │ 
│  │  • Tabella card (titolo, posizione, labels)  │   │ 
│  │  • Utenti attivi/inattivi                    │   │ 
│  │  • Storico pagamenti                         │   │ 
│  └──────────────────────────────────────────────┘   │ 
├─────────────────────────────────────────────────────┤ 
│                   PAGAMENTI                          │ 
│  ┌──────────────────────────────────────────────┐   │ 
│  │  Stripe                                      │   │ 
│  │  • Piano Free + Pro                          │   │ 
│  │  • Abbonamento mensile ($9/mese)             │   │ 
│  │  • Form di pagamento integrato               │   │ 
│  │  • "Pay and Subscribe"                       │   │ 
│  └──────────────────────────────────────────────┘   │ 
└─────────────────────────────────────────────────────┘

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
