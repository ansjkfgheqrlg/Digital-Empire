# Brief Miniatura — RUN-20260723-001 (F5)

## Elemento emotivo cardine
Il video promette "5 minuti reali, cronometro alla mano" — la miniatura deve comunicare
**velocità/facilità** contro la paura del terminale, non genericamente "tecnologia AI".

## Regola dei 3 elementi
1. **Sfondo**: terminale scuro (VS Code / iTerm dark theme) con testo `npm install` visibile e
   leggibile anche in miniatura piccola.
2. **Elemento focale**: icona/badge cronometro digitale rosso in un angolo con "5 MIN".
3. **Testo in sovraimpressione (max 3 parole, NON ripete il titolo):** "5 MINUTI. FATTO."

## Colori
Sfondo scuro (coerente con lo screencast reale, non fabbricato) + testo bianco/giallo alto
contrasto per il badge cronometro (rosso/giallo su nero — combinazione standard alta CTR per
contenuti "veloce/urgente").

## Prompt per generatore AI (sfondo/elemento grafico, NON il testo terminale reale)
```
Dark terminal / code editor background, cinematic lighting, subtle blue-orange glow,
minimalist tech aesthetic, high contrast, photorealistic screen glow, 8k, no readable text
in the generated background (il testo terminale reale va sovrapposto separatamente dallo
screenshot vero, non generato dall'AI — altrimenti il codice mostrato sarebbe falso)
```
**Nota importante:** il contenuto del terminale nella miniatura deve essere uno **screenshot
reale** del comando vero (`npm install -g @anthropic-ai/claude-code`), non testo generato da AI
— altrimenti la miniatura mostra un comando falso/diverso da quello del video (violerebbe
l'invariante #3, "copi il successo non gli errori": qui l'errore sarebbe l'onestà del contenuto).

## Correzione rispetto al cluster (F1/F2)
I tutorial "installazione" del cluster spesso usano miniature con solo il logo Claude generico
(basso CTR, si confonde con altri video AI). Differenziale: badge cronometro + testo "FATTO"
crea curiosità/urgenza specifica, non genericamente "tema AI".

## ⚠️ thumbnail_analyzer.py — non eseguibile in questo run
Lo script analizza contrasto/luminosità di un **file immagine renderizzato**. Non esiste ancora
(la miniatura si crea dopo il render del video, in Fliki o Canva). Da eseguire su output reale
prima della pubblicazione — non forzato qui.