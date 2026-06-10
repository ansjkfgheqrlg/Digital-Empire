# Esempio pronto numero 2 (2)

> Source: File system (`SKILL & Agenti\SKILL\PROMPT ENGEGNIRING-SKILL\Esempio pronto numero 2 (2).pdf`)
> Collected: 2026-05-06
> Published: Unknown

# Prompt per Gemini - Piattaforma SocialFlow di Auto-Pubblicazione Instagram 
 
Voglio che tu crei una web application completa chiamata "SocialFlow" con le seguenti 
caratteristiche: 
 
## Design e Layout 
 
- **Colori**: Sfondo nero (#000000), testo bianco, accenti arancione (#FF6B35 o simile) 
- **Stile**: Moderno, minimale, con elementi glassmorphism 
- **Font**: Sans-serif moderno (come Inter o Poppins) 
 
## Struttura della UI 
 
**Header:** 
- Logo "SocialFlow" in alto a sinistra (icona "S" arancione + testo) 
- Indicatore "SISTEMA ONLINE" in alto a destra con pallino rosso/verde 
 
**Badge centrale piccolino** 
- Badge arancione con testo "⚡ BRIDGE DI AUTOMAZIONE N8N" 
 
**Titolo principale:** 
- "Auto-Pubblicazione" (bianco). Deve esssere grande, H1 
- "Ridefinita." (arancione, font bold) 
 
**Sottotitolo:** 
- "Carica i tuoi contenuti video e lascia che la nostra pipeline gestisca la distribuzione su 
Instagram istantaneamente." 
 
## Funzionalità Principali 
 
### 1. Sezione Configurazione Webhook 
- Campo URL webhook: `METTI_IL_TUO_WEBHOOK_QUI` 
- Label "MODALITÀ TEST" con toggle 
- Pulsante "Verifica" per testare la connessione webhook (invia un ping senza dati) 
- Indicazione "METODO: POST" e "CAMPO: file, caption" 
 
### 2. Sezione Upload Video 
- Area drag-and-drop con icona upload centrale 
- Testo "Carica Video Sorgente" 
- Sottotesto "Trascina il file qui o clicca per selezionare. Supporta MP4, MOV, AVI." 
- Badge "⚡ TRASFERIMENTO BINARIO PRONTO" 
 
### 3. Workflow Funzionale 
 
**Step 1 - Upload Video:** 
- L'utente carica un video (max 100MB) 
- Mostra preview del video caricato 
 

**Step 2 - Descrizione Contenuto:** 
- Appare un campo di testo: "Di cosa tratta questo video?" 
- Input testuale dove l'utente descrive il contenuto 
 
**Step 3 - Generazione Caption:** 
- Usa l'API di Gemini 2.5 Flash per generare una caption Instagram basata sulla descrizione 
- Prompt interno da usare: "Genera una caption coinvolgente per Instagram per un video che 
tratta di: [descrizione utente]. Includi emoji pertinenti, hashtag rilevanti e un tono 
professionale ma friendly. Massimo 2200 caratteri." 
- Mostra la caption generata in un textarea editabile 
 
**Step 4 - Invio a Webhook:** 
- Pulsante "Pubblica su Instagram"  
- Invia POST request al webhook n8n con: 
  - `file`: video in formato binario/base64 
  - `caption`: testo della caption 
- Mostra feedback di successo/errore 
 
## Specifiche Tecniche 
 
- **Framework**: Usa React con Hooks 
- **Styling**: Tailwind CSS 
- **API Gemini**: Integra `@google/generative-ai` per la generazione caption 
- **File Upload**: Gestisci file fino a 100MB 
- **Formato invio webhook**: multipart/form-data o JSON con base64 
 
## Funzioni Extra 
 
1. **Verifica Webhook**: Pulsante che invia un ping al webhook per verificare che sia online 
(risposta 200 OK) 
2. **Loading States**: Spinner durante generazione caption e upload 
3. **Error Handling**: Messaggi chiari per errori di rete, file troppo grandi, etc. 
4. **Responsive**: Funziona su mobile e desktop 
 
## Note Importanti 
 
- NON usare localStorage (usa solo state React) 
- Gestisci gli errori dell'API Gemini con try-catch 
- Mostra sempre feedback visivo all'utente (loading, success, error) 
- La caption deve essere completamente editabile prima dell'invio 
 
Crea un'applicazione React completa, funzionante e pronta all'uso con tutto il codice 
necessario in un singolo artifact. 
 
# Nota Finale 
 
LA PIATTAFORM DEVE ESSRE ESTRAMENTE ELEGANTE, DEVE ESSERE SEMBRATA 
FATTA DA UNA WEB AGENCY CON 10 ANNI DI ESPERIENZA
