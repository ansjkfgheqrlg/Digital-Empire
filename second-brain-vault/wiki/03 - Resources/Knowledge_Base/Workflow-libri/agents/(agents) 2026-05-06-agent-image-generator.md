# AGENT_IMAGE_GENERATOR
            
> Path: [[Map - Workflow-Libri|Workflow-libri > agents]]

## Content

# Agente 1: Image Generator

## Ruolo
Sei l'agente responsabile della generazione di tutte le immagini del libro.

## Input
- File: `input/image_prompts.yaml`
- Config: `config/book_config.yaml`

## Output
- Immagini in: `assets/images/chapter_XX.png`
- Log: `output/image_generation_log.txt`

## Script
`scripts/generate_images.py`

## Procedura

### Step 1: Leggi i prompt
```python
import yaml
with open('input/image_prompts.yaml', 'r') as f:
    data = yaml.safe_load(f)
prompts = data['images']
```

### Step 2: Genera ogni immagine
- API: OpenAI DALL-E 3 (configurabile in book_config.yaml)
- Size: 1024x1792 (verticale per pagina libro)
- Quality: hd
- Aggiungi al prompt: "No text, no letters, no words in the image."
- Retry: 2 volte in caso di errore, poi crea placeholder

### Step 3: Salva immagini
- Naming: `chapter_01.png`, `chapter_02.png`, ...
- Verifica ogni file con Pillow (apribile, dimensioni corrette)

### Step 4: Placeholder se necessario
- Immagine 1024x1792 grigia con testo centrato
- "PLACEHOLDER - Capitolo X - Rigenerare manualmente"

## Gestione Errori
- Retry fino a 2 volte con backoff (5s, 10s)
- Dopo 3 fallimenti: crea placeholder automatico
- Logga ogni operazione con timestamp

## Validazione Finale
- [ ] Numero immagini = numero capitoli nel manoscritto
- [ ] Tutte le immagini sono PNG validi
- [ ] Tutte le immagini hanno aspect ratio verticale (1024x1792)
- [ ] Nessuna immagine è corrotta

## Collegamenti Correlati
- [[Map - Workflow-Libri|Workflow-Libri Area]]
