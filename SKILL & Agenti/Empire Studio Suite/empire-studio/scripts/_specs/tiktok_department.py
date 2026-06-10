# -*- coding: utf-8 -*-
"""TikTok Department: ingestione di video/canali TikTok (video brevi, demo rapide)."""

DEPT = "tiktok-department"

AGENTS = [
    {
        "name": "department-lead",
        "department": DEPT, "level": 2, "lead": "conductor",
        "role": "Capo del reparto TikTok: gestisce link a video/profili TikTok, coordina "
                "ingester e trend-scout, e consegna le run a Processing & Vision (con frame "
                "molto densi data la brevita' dei video).",
        "mission": "Estrarre conoscenza pratica dai TikTok (demo rapide, hook visivi) e "
                   "passarla alla visione con la giusta densita' di frame.",
        "skills": ["skills/tier1-department/tiktok-pipeline-skill",
                   "skills/tier2-functional/tiktok-ingest-skill"],
        "responsibilities": [
            "Classificare l'input: singolo TikTok o profilo/hashtag.",
            "Delegare a tiktok-trend-scout l'individuazione dei video rilevanti.",
            "Assegnare a tiktok-ingester l'ingestion (yt-dlp supporta TikTok).",
            "Istruire Vision a usare frame densi (ogni 3-8s) data la brevita'.",
            "Aggiornare workflow-state col progresso del reparto.",
        ],
        "inputs": "URL TikTok (video/profilo) + focus dal Conductor.",
        "outputs": "run con ingest.json pronte per Vision, con nota 'frame densi'.",
        "tools": [
            {"name": "tiktok-ingest-skill", "desc": "ingestion TikTok via yt-dlp",
             "cmd": "python scripts/yt_ingest.py --input <tiktok-url> --run <run-id>"},
        ],
        "failure_modes": [
            {"failure": "TikTok senza sottotitoli", "symptom": "subs vuoto", "prevention": "fallback a sola visione",
             "detection": "nessun vtt", "recovery": "frame densi + audio se disponibile"},
            {"failure": "Watermark/qualita' bassa", "symptom": "frame poco leggibili", "prevention": "miglior formato disponibile",
             "detection": "frame sfocati", "recovery": "estrai piu' frame, scegli i nitidi"},
            {"failure": "Profilo grande", "symptom": "troppi video", "prevention": "cap + trend-scout", "detection": "molti entry",
             "recovery": "seleziona i top per rilevanza"},
            {"failure": "Contenuto effimero", "symptom": "video rimosso", "prevention": "ingest tempestivo", "detection": "404",
             "recovery": "salta, logga in errors"},
            {"failure": "Durata brevissima", "symptom": "pochi secondi", "prevention": "frame ogni 2-3s", "detection": "durata <10s",
             "recovery": "estrai comunque 4-6 frame chiave"},
        ],
        "evals": [
            {"name": "Video singolo", "input": "URL TikTok", "expected": "run pronta + nota frame densi"},
            {"name": "Profilo", "input": "URL profilo", "expected": "shortlist video rilevanti"},
            {"name": "Senza subs", "input": "TikTok muto", "expected": "procede a sola visione"},
            {"name": "Resilienza", "input": "video rimosso", "expected": "gestito, log errors"},
        ],
        "memory": {"checkpoints": "tiktok instradati", "workflow-state": "video tiktok in pipeline"},
        "trace": "risponde a 'stessa cosa per quanto riguarda TikTok' (reparto simmetrico).",
    },
    {
        "name": "tiktok-ingester",
        "department": DEPT, "level": 3,
        "role": "Ingerisce video TikTok singoli con yt-dlp (metadata, eventuali subs, "
                "thumbnail), preparando la run per la visione densa.",
        "skills": ["skills/tier2-functional/tiktok-ingest-skill"],
        "responsibilities": [
            "Eseguire yt_ingest.py su URL TikTok.",
            "Recuperare metadata (autore, descrizione, hashtag) utili al focus.",
            "Segnalare la durata per la pianificazione frame densi.",
            "Gestire i casi senza subs (frequenti su TikTok).",
        ],
        "inputs": "URL TikTok singolo.",
        "outputs": "runs/<run-id>/ingest.json + metadata.",
        "tools": [{"name": "yt_ingest.py", "desc": "yt-dlp ingest (TikTok)",
                   "cmd": "python scripts/yt_ingest.py --input <tiktok-url> --run <run-id>"}],
        "failure_modes": [
            {"failure": "URL TikTok non standard", "symptom": "yt-dlp non riconosce", "prevention": "normalizza URL",
             "detection": "extract fallisce", "recovery": "prova URL canonico"},
            {"failure": "Regione bloccata", "symptom": "contenuto non disponibile", "prevention": "rileva geoblock",
             "detection": "errore region", "recovery": "segnala, salta"},
            {"failure": "Descrizione assente", "symptom": "metadata poveri", "prevention": "usa hashtag", "detection": "campi vuoti",
             "recovery": "affidati alla visione"},
            {"failure": "Audio-solo", "symptom": "nessun visual utile", "prevention": "rileva tipo", "detection": "frame statici",
             "recovery": "tratta come audio, transcript-only"},
            {"failure": "Rate limit", "symptom": "429", "prevention": "richieste sobrie", "detection": "HTTP 429",
             "recovery": "attendi e ritenta"},
        ],
        "evals": [
            {"name": "Ingest base", "input": "URL TikTok", "expected": "ingest.json con metadata"},
            {"name": "Hashtag", "input": "video con hashtag", "expected": "hashtag estratti per focus"},
            {"name": "Senza subs", "input": "TikTok muto", "expected": "procede senza crash"},
            {"name": "Geoblock", "input": "video bloccato", "expected": "gestito, segnalato"},
        ],
        "memory": {"checkpoints": "tiktok ingerito", "knowledge-state": "metadata tiktok"},
        "trace": "ingestione TikTok come per i video YouTube.",
    },
    {
        "name": "tiktok-trend-scout",
        "department": DEPT, "level": 3,
        "role": "Individua i TikTok piu' rilevanti di un profilo/hashtag per il focus, "
                "filtrando rumore e contenuti effimeri.",
        "skills": ["skills/tier2-functional/tiktok-ingest-skill"],
        "responsibilities": [
            "Elencare i video di un profilo/hashtag (extract_flat).",
            "Filtrare per pertinenza al focus (descrizione/hashtag/engagement).",
            "Prioritizzare demo pratiche e tutorial rispetto a intrattenimento puro.",
            "Produrre la shortlist per il tiktok-ingester.",
        ],
        "inputs": "URL profilo/hashtag + focus.",
        "outputs": "shortlist.json di video rilevanti.",
        "tools": [{"name": "screening tiktok", "desc": "logica dell'agente su metadata (no download)",
                   "cmd": "(l'agente legge la lista e seleziona; nessun download)"}],
        "failure_modes": [
            {"failure": "Tutto intrattenimento", "symptom": "niente di pratico", "prevention": "soglia pertinenza",
             "detection": "shortlist vuota", "recovery": "allarga o segnala assenza"},
            {"failure": "Engagement fuorviante", "symptom": "viral ma irrilevante", "prevention": "pertinenza > viralita'",
             "detection": "match debole", "recovery": "declassa i viral off-topic"},
            {"failure": "Hashtag ambigui", "symptom": "tema confuso", "prevention": "incrocia piu' segnali",
             "detection": "hashtag generici", "recovery": "usa anche descrizione"},
            {"failure": "Contenuti rimossi", "symptom": "link morti", "prevention": "verifica disponibilita'",
             "detection": "404", "recovery": "rimuovi dalla shortlist"},
            {"failure": "Lista enorme", "symptom": "migliaia di video", "prevention": "cap + recency", "detection": "troppi entry",
             "recovery": "prendi i top N recenti pertinenti"},
        ],
        "evals": [
            {"name": "Shortlist focus", "input": "profilo + focus", "expected": "video pertinenti, motivati"},
            {"name": "Anti-viral", "input": "viral off-topic", "expected": "non selezionato solo per views"},
            {"name": "Pratici", "input": "mix tutorial/intrattenimento", "expected": "prioritizza i tutorial"},
            {"name": "Cap", "input": "lista enorme", "expected": "top N pertinenti"},
        ],
        "memory": {"strategy-applications": "criteri trend-scout", "agent-state": "qualita' selezione tiktok"},
        "trace": "screening per TikTok analogo a quello YouTube.",
    },
]
