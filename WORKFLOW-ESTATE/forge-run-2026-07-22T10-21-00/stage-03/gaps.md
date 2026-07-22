# Lacuna `g-001`: Soglia quantitativa esatta di handoff dal Closer A8 al sistema di billing automatico
- **Atomi correlati**: a-144
- **Raccomandazione**: Il sorgente menziona il ruolo di chiusura di Closer A8 ma non dettaglia l'integrazione API con Stripe/PayPal e l'innesco immediato di onboarding post-pagamento.

# Lacuna `g-002`: Rate limiting dinamico e rotazione IP/Proxy per prepare_outreach_emails.py e send_s1_whatsapp_auto.py
- **Atomi correlati**: a-031, a-065, a-122
- **Raccomandazione**: Gli script di invio massivo S1/outreach non documentano logiche di backoff esponenziale o gestione anti-ban, essenziale per non perdere il dominio estivo.

# Lacuna `g-003`: Sincronizzazione bi-direzionale tra lo status lead su file markdown (LISTA-LEAD.md) e CRM esterno per l'Agente Gael
- **Atomi correlati**: a-006, a-041, a-146
- **Raccomandazione**: Manca il protocollo di lock concorrenziale quando più script o agenti tentano di aggiornare contemporaneamente lo stato dei lead su disco.
