# 16.5 — Come Ottenere le API Key
            
> Path: [[Map - Formazzione|Formazzione > manuale-completo-claude-code-business > parte-4- > capitolo-16-costruire]]

## Content

L'autore mostra il processo pratico per ottenere le chiavi API necessarie: 
API Key di Stripe 
text 
PROCESSO: 
 
1. Andare su Stripe.com 
2. Navigare a: Developer → API Keys 
3. Selezionare: Standard API key → "Building your own integration" 
4. Premere: Create 
5. Verificare l'identità (email + codice telefono) 
6. Dare un nome alla chiave (es. "Giovanni YouTube Italia") 
7. Copiare la chiave generata 
 
⚠️ NOTA DI SICUREZZA: 

--- PAGE 48 ---
L'autore usa una chiave di produzione nel video per semplicità. 
In uno scenario reale, usare SEMPRE chiavi di TEST durante lo sviluppo. 
Le chiavi test iniziano con "sk_test_" 
Le chiavi live iniziano con "sk_live_" 
API Key di Supabase 
text 
PROCESSO: 
 
1. Andare su Supabase.com 
2. Aprire il progetto 
3. Navigare a: Settings → API 
4. Copiare: 
   • La URL del progetto (es. https://xxx.supabase.co) 
   • La chiave Anon/Public 
5. Per le chiavi segrete: Settings → API → Service Role Key 
 
⚠️ NOTA SUI NOMI: 
I nomi delle chiavi in Supabase possono contenere solo 
lettere minuscole e cifre (no maiuscole, no spazi, no caratteri speciali)

## Collegamenti Correlati
- [[Map - Formazzione|Formazzione Area]]
