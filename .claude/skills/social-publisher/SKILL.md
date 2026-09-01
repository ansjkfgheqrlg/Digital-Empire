---
name: social-publisher
description: "Automatizza la pubblicazione dei contenuti gia approvati sui canali social di Digital Empire (Instagram, TikTok e altri) tramite script Python deterministici e API aggregatrici. Verifica che media e caption esistano, esegue il push e restituisce l'URL del post. Usala quando una cartella post e pronta e va pubblicata, non per creare il contenuto."
---
# Social Publisher Skill

**Scopo**
Questa skill automatizza la pubblicazione finale dei contenuti approvati su Instagram, TikTok e altri social. Si basa su un'infrastruttura Python deterministica che usa API Mediatrici (es. Zernio, Upload-Post o Ayrshare). 

**Knowledge**
- Usa gli script python presenti in `scripts/`.
- Conosce il formato JSON richiesto dai principali aggregatori di API social.
- Sa come recuperare file locali e file scaricati da Google Drive.

**Istruzioni (Checklist Operativa)**
1. **Verifica Input**: L'utente deve fornire il percorso della cartella del post (es. `2026-05-15-nome-carosello`).
2. **Scan**: Esegui `python scripts/check_ready.py --path <percorso>` per verificare che i file multimediali e la caption esistano e siano validi.
3. **API Publishing**: Se la verifica passa, esegui `python scripts/push_social.py --path <percorso> --brand <digital-empire | mentalita-brutale>`.
4. **Log**: Restituisci l'URL del post o l'esito di successo all'utente.

**Limiti**
- NON pubblicare MAI se `check_ready.py` fallisce o restituisce "Incompleto".
- NON usare le API ufficiali di Meta o TikTok, usa SOLO lo script python predisposto.

**Layout Output**
Se la pubblicazione ha successo:
```markdown
✅ **Pubblicazione Completata**
- Brand: [Nome Brand]
- Piattaforme: [Lista piattaforme]
- Link: [URL/ID se restituito dall'API]
```

**Self-Healing (Gestione Errori)**
- Se `push_social.py` fallisce per un errore di rete o di formato API: analizza l'output, correggi eventuali parametri passati male e riprova una volta.
- Se fallisce per "Immagine troppo grande", chiedi di eseguire uno script di resize.
