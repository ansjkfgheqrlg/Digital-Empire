# 16.12 — Errori Comuni
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-4- > capitolo-16-costruire]]

## Content

Errore 1: Cercare di costruire tutto in un colpo solo​
La strategia a due stadi (prima senza Stripe, poi con Stripe) è intenzionale. Costruire tutto simultaneamente aumenta la 
probabilità di errori difficili da debuggare. 
Errore 2: Non salvare in memoria prima di cambiare sessione​
Se il contesto è al 60-70% e si continua senza salvare, le performance degradano. L'autore chiede esplicitamente a 
Claude di salvare in memoria e poi apre una nuova sessione. 
Errore 3: Non eseguire lo schema SQL manualmente​
Claude Code genera lo schema SQL ma non può sempre eseguirlo direttamente su Supabase. L'utente deve copiare lo 
schema e eseguirlo manualmente nel SQL Editor di Supabase. 
Errore 4: Usare chiavi API di produzione durante lo sviluppo​
L'autore lo fa per semplicità nel video ma avverte che è una pratica rischiosa. Le chiavi test sono sempre preferibili 
durante lo sviluppo. 
Errore 5: Non verificare che Supabase abbia salvato i dati​
Dopo la prima registrazione, l'autore va nel dashboard Supabase per verificare che i dati siano effettivamente stati 
salvati nelle tabelle. Questo è un passaggio di verifica che non dovrebbe essere saltato.

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
