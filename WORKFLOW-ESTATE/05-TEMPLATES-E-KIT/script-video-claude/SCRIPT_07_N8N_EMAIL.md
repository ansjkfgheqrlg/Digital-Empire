# SCRIPT_07_N8N_EMAIL.md

### 1. ARGOMENTO TECNICO
Collegamento avanzato tra n8n (automazione webhook/API) e Claude per classificare e rispondere alle email del supporto clienti in modo autonomo.

### 2. ANGOLO
Superare i limiti dei chatbot base: costruire un flusso "indistruttibile" (low-code + AI agent) che legge, decide e bozza le email per te.

### 3. LEVA EMOTIVA
"Passo tre ore al giorno a rispondere a email fotocopia, quando potrei avere un assistente che me le prepara in bozza prima ancora che io accenda il PC."

### 4. SCRIPT COMPLETO

Vuoi che Claude legga le tue email di supporto clienti, decida da solo cosa fare, e scriva una bozza di risposta in automatico con il tuo tono di voce?

Invece di rispondere a mano ogni volta, oggi colleghiamo n8n (il miglior tool di automazione low-code) direttamente a Claude creando un flusso indistruttibile.

La logica è questa: n8n ascolta la tua casella Gmail. Quando arriva un'email, n8n la prende e la manda a Claude con un System Prompt specifico che gli dice: "Sei un agente del supporto. Leggi questa mail. Se è una richiesta di rimborso, scrivi che ci dispiace e chiedi l'IBAN. Se è una richiesta tecnica, manda il link alle FAQ."

Claude analizza, decide, e rimanda il testo indietro a n8n, che a sua volta crea la bozza direttamente dentro la tua casella Gmail. Tu ti svegli la mattina, controlli le bozze generate, premi Invia ed è finita.

L'unico rischio di questo sistema è che l'AI scriva risposte errate o inventi policy inesistenti se non è configurata bene. Per questo servono dei filtri JSON specifici in n8n. 

Se non vuoi impazzire a configurarli, abbiamo preparato l'intero template del flusso n8n pronto da importare in un clic. È incluso come bonus esclusivo nel nostro Manuale Completo di Claude Code. Trovi il link in bio.

### 5. 3 HOOK VARIANTI

**Variante 1 (Discovery):** 
Ho appena costruito un sistema che legge le mie email aziendali e scrive le bozze di risposta per me, usando n8n e Claude.

**Variante 2 (Errore):** 
Se stai usando ChatGPT per farti scrivere le risposte alle email di lavoro facendo copia e incolla, ti stai perdendo l'80% dell'automazione. 

**Variante 3 (Risultato):** 
Ecco come ho azzerato le ore passate a rispondere alle email fotocopia del supporto clienti, usando un flusso low-code tra n8n e Claude.

### 6. CTA FINALE

**Versione Lunga:**
L'unico rischio di automatizzare le email è che l'AI scriva cose sbagliate ai clienti. Serve inserire dei filtri di controllo precisi nel webhook. Per farti saltare tutta la parte tecnica, abbiamo inserito il file JSON di n8n pronto da importare come bonus esclusivo nel nostro Manuale di Claude Code. Scaricalo dal link in bio.

**Versione Corta:**
Per evitare errori o allucinazioni, ti serve il nostro file JSON di n8n con i filtri di sicurezza già configurati. Lo trovi come bonus dentro il Manuale Claude Code. Link in bio.

### 7. CAPTION

**Versione TikTok:**
Come farsi gestire il supporto clienti da un Agente AI usando n8n e Claude. 🤖 Addio email fotocopia, benvenute bozze automatiche. Per importare il mio flusso n8n in un clic senza sbattimenti, scarica il bonus dentro il Manuale nel link in bio! #automazione #n8n #claudecode #intelligenzaartificiale #business

**Versione IG:**
Sei stanco di rispondere sempre alle stesse email di supporto clienti? 📧

Ecco l'architettura esatta per automatizzare tutto con n8n + Claude:
1️⃣ n8n ascolta via webhook le email in entrata
2️⃣ Il testo passa a Claude con un System Prompt specifico
3️⃣ L'AI classifica il problema (Reso, Domanda Tecnica, ecc.)
4️⃣ Claude scrive la risposta con il tuo tono
5️⃣ n8n salva la mail nella cartella "Bozze" di Gmail

Risultato? Non parti mai da zero. Trovi le risposte già scritte, le rileggi, e premi Invia. 

⚠️ Attenzione: senza filtri di sicurezza Claude potrebbe inventare regole aziendali che non esistono. 

Vuoi il nostro template JSON esatto per importare questo flusso su n8n in 1 clic (con i blocchi di sicurezza già attivi)? È incluso come bonus nel Manuale Completo di Claude Code. 

Link in bio! 🔗
#n8n #claudecode #automazionemarketing #freelanceita #ai

### 8. NOTE DI REGISTRAZIONE
1. **Ritmo:** Molto strutturato, deve dare l'idea di un'architettura solida passo-passo.
2. **Video:** Metti a schermo il grafo nodale di n8n per mostrare i vari step visivamente.
3. **Tono:** Rassicurante ma tecnico. Sei uno che risolve veri problemi di logistica aziendale.
4. **Pause:** Pausa netta prima di "Tu ti svegli la mattina, controlli le bozze generate..."
5. **Enfasi:** Sottolinea molto forte "filtri JSON specifici" e "bozza direttamente dentro la tua casella Gmail".
