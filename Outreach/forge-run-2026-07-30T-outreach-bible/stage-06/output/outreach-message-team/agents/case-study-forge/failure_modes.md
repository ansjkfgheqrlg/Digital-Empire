# Failure Modes — case-study-forge

| ID | Failure | Sintomo | Prevenzione | Rilevamento | Recupero |
|----|---------|---------|-------------|-------------|----------|
| fm-001 | Offerta vaga non concreta | "posso aiutarti con il marketing" invece di un'azione specifica | Vincolo esplicito "azione concreta, non generica" nel system_prompt | message-writer riceve un `descrizione` non azionabile, segnala ESCALATION indietro | Riformula con un'azione specifica e consegnabile |
| fm-002 | Dichiara un risultato non verificabile | "abbiamo aiutato 100 aziende" senza dato reale | Tool `lookup_real_case_studies` obbligatorio prima di dichiarare un real_case_study | Audit periodico dei case study dichiarati vs store reale | Declassa a artificial_case_study se non verificabile |
| fm-003 | Offerta non onorabile se il lead accetta | Promette un lavoro che il team non può davvero fare | Vincolo esplicito "deve essere consegnabile" | Segnalazione a valle se un'offerta accettata non viene mai consegnata | Non ripete il pattern per nicchie dove è successo, aggiorna il pattern |
| fm-004 | Nicchia nuova gestita con offerta a caso | Offerta non pertinente al problema reale della nicchia | Regola esplicita ESCALATION per nicchie non coperte | message-writer o rule-keeper notano un'offerta fuori contesto | ESCALATION esplicita invece di procedere |
| fm-005 | Ripete offerta identica per nicchie con problemi diversi | Stessa "audit SEO" offerta a un concessionario auto e a un e-commerce | Tabella pattern per nicchia nel system_prompt, non un default unico | Review periodica delle offerte per nicchia | Differenzia l'offerta per nicchia specifica |
