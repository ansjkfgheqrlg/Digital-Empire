# 18.4 — Interpretazione Pratica: Domande Intelligenti del Piano
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-5- > capitolo-18-plan-mode-]]

## Content

Durante il Plan Mode, Claude Code non si limita a creare un piano. Pone anche domande strategiche che aiutano a 
raffinare il progetto. L'autore mostra due esempi concreti dalla costruzione dell'app Trello: 
Domanda 1 — Scelta tecnica: 
Claude: "Quale metodo di autenticazione preferisci? 
         A) Magic Link — l'utente riceve un'email e si autentica da lì 
         B) Login diretto — l'utente inserisce credenziali e entra subito" 

--- PAGE 64 ---
Questa domanda è importante perché la scelta tecnica influenza l'architettura dell'intera applicazione. Prenderla nella 
fase di pianificazione evita di dover ristrutturare l'app in seguito. 
Domanda 2 — Sicurezza: 
Claude: "La chiave Stripe che hai condiviso è una chiave live di produzione. 
         Vuoi usare chiavi test per lo sviluppo? 
         Le chiavi test iniziano con sk_test_" 
Claude Code identifica un rischio di sicurezza nel prompt dell'utente e lo segnala proattivamente. Questo tipo di 
feedback è uno dei valori aggiunti del Plan Mode.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Formazzione|Formazzione Area]]
