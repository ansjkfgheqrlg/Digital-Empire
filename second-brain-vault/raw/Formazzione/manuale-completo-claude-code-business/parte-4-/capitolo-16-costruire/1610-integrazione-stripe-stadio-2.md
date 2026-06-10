# 16.10 — Integrazione Stripe (Stadio 2)

Per l'integrazione Stripe, l'autore utilizza il meccanismo di memoria per trasferire il contesto alla nuova sessione: 
text 
PROCESSO DI TRANSIZIONE SESSIONE: 
 
1. Nella sessione corrente (contesto al 66%): 
   "Sei al 66% del contesto, il che significa che comincerai 
   a perdermi a livello di performance. Salvare le cose in 
   memoria in modo che nel nuovo contesto possa continuare." 
 
2. Claude salva in memoria: 
   • Struttura del progetto 
   • File modificati 
   • Configurazioni 
   • Stato attuale 
   • Cosa manca (integrazione Stripe) 
 
3. Nuova sessione: 
   "Continua con integrazione Stripe" 
 
4. Claude legge la memoria e riprende il lavoro 
L'integrazione Stripe richiede passaggi specifici: 
text 
CONFIGURAZIONE STRIPE: 
 
1. Creare il prodotto su Stripe: 
   • Dashboard Stripe → Product Catalog → Add Product 

--- PAGE 53 ---
   • Nome: "Canboard Pro" (o il nome dell'app) 
   • Pricing: Standard, Recurring, $9/mese, Monthly 
   • Save Product 
 
2. Copiare il Price ID: 
   • Nella pagina del prodotto, sotto Pricing 
   • Copiare il codice che inizia con "price_" 
 
3. Fornire il Price ID a Claude Code 
 
4. Claude Code integra Stripe nell'app: 
   • Pagina di pagamento 
   • Form "Subscribe Now" 
   • Bottone "Pay and Subscribe"

