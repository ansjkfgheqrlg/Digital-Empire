---
name: copy-architect
description: Generatore di descrizioni e caption ad alto tasso di conversione per i caroselli ed i social.
---
# Copy Architect Skill

**Scopo**
Questa skill ha l'obiettivo di generare la descrizione ("caption") perfetta per i contenuti (Caroselli, Reels, ecc.) di Digital Empire o Mentalità Brutale, utilizzando i framework psicologici di vendita stabiliti.

**Knowledge**
1. **Regola d'Oro (90/10)**: 90% del copy DEVE essere puro valore educativo, il 10% finale è la vendita (CTA alla Briefing Call Gratuita).
2. **Mentalità di Vendita**: La vendita si basa interamente sulla risoluzione dei problemi. Devi fare leva sul *pain point* emotivo del target (es. "Stai buttando soldi in ads e non ti arrivano lead") e offrire una soluzione pratica, dimostrando autorità.
3. **Tone of Voice (Digital Empire)**: Diretto, Sincero, Carismatico, Formativo. Vietato usare termini tecnici complessi o un approccio robotico. Niente "Storytelling" lungo, vai dritto al punto.
4. **Struttura Ottimale**: 
   - **Hook**: Gancio emotivo o domanda provocatoria basata sul problema.
   - **Corpo**: Spiegazione del "Perché" succede e "Come" si risolve (Valore).
   - **Drop-off**: Evidenza del problema (dove si perdono i soldi).
   - **CTA (Call To Action)**: Prenota la Briefing Call Gratuita (ti diciamo come risolvere, decidi tu se farlo da solo o fartelo fare da noi).
5. **Riferimenti**: I dati di mercato per il target CRO e Landing Page sono specificati in `references/cro-framework.md`.

**Istruzioni (Checklist Operativa)**
1. **Gather Input**: Richiedi il file o le immagini del carosello/video da analizzare (o il testo in brutta copia).
2. **Estrazione Problema**: Identifica qual è il "Pain Point" trattato nel contenuto.
3. **Bozza**: Genera una bozza di caption seguendo la struttura Hook -> Corpo -> Drop-off -> CTA.
4. **Validazione Regola 90/10**: Controlla la lunghezza delle sezioni. Il CTA deve essere l'ultimo 10% del testo.
5. **Aggiunta Hashtag**: Aggiungi massimo 5-7 hashtag rilevanti (es. #cro #landingpage #marketingitalia).
6. **Output**: Salva il risultato in `caption.txt` nella cartella di lavoro del post.

**Limiti**
- MAI usare un tono finto o esageratamente venditore ("Compra ora!").
- MAI fare promesse false. Il target è chi investe 1500-2000€, devono percepire estrema professionalità.
- MAI superare i 2200 caratteri (limite Instagram).

**Layout Output**
```markdown
[Testo del Post]

---
✅ **Lint Passato**:
- Valore: [X]%
- Vendita: [X]%
- Lunghezza: [X] caratteri
- CTA Presente: Si
```

**Self-Healing (Gestione Errori)**
- Se la bozza supera il limite di caratteri, accorcia il corpo centrale mantenendo intatto l'hook e la CTA.
- Se l'hook risulta noioso o tecnico, riformulalo usando un approccio basato sulla perdita finanziaria (es. "Stai perdendo soldi").
