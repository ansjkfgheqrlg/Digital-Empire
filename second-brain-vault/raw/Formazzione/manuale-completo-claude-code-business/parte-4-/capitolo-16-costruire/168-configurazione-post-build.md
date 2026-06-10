# 16.8 — Configurazione Post-Build

Dopo che Claude Code ha costruito l'applicazione, c'è una fase di configurazione manuale necessaria: 
text 
PASSI DI CONFIGURAZIONE MANUALE: 
 
1. Aggiornare il file .env con le chiavi reali: 
   • NEXT_PUBLIC_SUPABASE_URL = [URL dal dashboard Supabase] 
   • NEXT_PUBLIC_SUPABASE_ANON_KEY = [chiave Anon da Supabase] 
 
2. Eseguire lo schema SQL in Supabase: 
   • Dashboard Supabase → SQL Editor 
   • Copiare il contenuto del file schema (generato da Claude) 

--- PAGE 51 ---
   • Premere "Run" 
   • Verificare: "Success, no rows returned" 
 
3. Disabilitare email confirmation in Supabase: 
   • Settings → Authentication → Sign in providers 
   • Disattivare "Enable email confirmations" 
   • Salvare 
 
4. Avviare il server di sviluppo: 
   • Chiedere a Claude: "Per favore run il comando npm run dev 
     e dimmi cos'altro devo avere per testare l'app. 
     Se è tutto a posto, dammi il localhost."

