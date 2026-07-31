#!/usr/bin/env python3
import json
import sys
import os

def validate_candidati_video(data):
    if not isinstance(data, dict):
        raise ValueError("L'input deve essere un dizionario (oggetto JSON).")
    if "channel" not in data or not isinstance(data["channel"], str):
        raise ValueError("Campo 'channel' mancante o non stringa.")
    if "videos" not in data or not isinstance(data["videos"], list):
        raise ValueError("Campo 'videos' mancante o non lista.")
    for idx, v in enumerate(data["videos"]):
        if not isinstance(v, dict):
            raise ValueError(f"Il video all'indice {idx} non è un oggetto.")
        for k in ["title", "url"]:
            if k not in v or not isinstance(v[k], str):
                raise ValueError(f"Video {idx}: campo '{k}' mancante o non stringa.")
        if "errors" in v and not isinstance(v["errors"], list):
            raise ValueError(f"Video {idx}: 'errors' deve essere una lista.")
    return True

def validate_seo_report(data):
    if not isinstance(data, dict):
        raise ValueError("L'input deve essere un dizionario (oggetto JSON).")
    if "videos" not in data or not isinstance(data["videos"], list):
        raise ValueError("Campo 'videos' mancante o non lista.")
    for idx, v in enumerate(data["videos"]):
        if not isinstance(v, dict):
            raise ValueError(f"Il video all'indice {idx} non è un oggetto.")
        if "title" not in v or not isinstance(v["title"], str):
            raise ValueError(f"Video {idx}: 'title' mancante o non stringa.")
        if "seo_score" not in v or not isinstance(v["seo_score"], (int, float)):
            raise ValueError(f"Video {idx}: 'seo_score' mancante o non numerico.")
        if "label" not in v or v["label"] not in ["A-upside", "B-sicurezza"]:
            raise ValueError(f"Video {idx}: 'label' non valida (deve essere 'A-upside' o 'B-sicurezza').")
    return True

def validate_produzione_spec(data):
    if not isinstance(data, dict):
        raise ValueError("L'input deve essere un dizionario (oggetto JSON).")
    required = ["video_id", "title", "voice", "music", "hook_type", "scene_count", "scenes"]
    for field in required:
        if field not in data:
            raise ValueError(f"Campo '{field}' mancante.")
    if not isinstance(data["scenes"], list):
        raise ValueError("Il campo 'scenes' deve essere una lista.")
    return True

def validate_brief_miniatura(data):
    """Schema aggiornato il 2026-07-31: la miniatura si ADATTA da quella reale del video
    sorgente (source_video_id/source_thumbnail) e il testo e' una LISTA di righe corte, come
    nelle copertine di @dosementale. Il vecchio schema (text_overlay + image_prompt singoli)
    apparteneva al flusso 'immagine inventata da una descrizione'."""
    if not isinstance(data, dict):
        raise ValueError("L'input deve essere un dizionario (oggetto JSON).")
    for field in ["title", "concept", "source_style"]:
        if field not in data or not isinstance(data[field], str):
            raise ValueError(f"Campo '{field}' mancante o non stringa.")
    righe = data.get("text_overlay_lines")
    if not isinstance(righe, list) or not righe or not all(isinstance(r, str) and r.strip() for r in righe):
        raise ValueError("Campo 'text_overlay_lines' mancante o non lista di stringhe non vuote.")
    evidenziate = data.get("text_overlay_highlight_lines", [])
    if not isinstance(evidenziate, list) or any(r not in righe for r in evidenziate):
        raise ValueError("'text_overlay_highlight_lines' deve essere una lista di righe presenti in 'text_overlay_lines'.")
    if "source_thumbnail" in data and data["source_thumbnail"] is not None \
            and not isinstance(data["source_thumbnail"], str):
        raise ValueError("Campo 'source_thumbnail' deve essere una stringa o null.")
    return True

def validate_metadati(data):
    if not isinstance(data, dict):
        raise ValueError("L'input deve essere un dizionario (oggetto JSON).")
    required = ["title", "description", "tags", "keyword", "thumbnail", "subtitles"]
    for field in required:
        if field not in data:
            raise ValueError(f"Campo '{field}' mancante.")
    if not isinstance(data["tags"], list):
        raise ValueError("Il campo 'tags' deve essere una lista.")
    if not isinstance(data["thumbnail"], bool):
        raise ValueError("Il campo 'thumbnail' deve essere booleano.")
    if not isinstance(data["subtitles"], bool):
        raise ValueError("Il campo 'subtitles' deve essere booleano.")
    return True

def validate_performance_logs(data):
    if not isinstance(data, list):
        raise ValueError("L'input dei log delle performance deve essere una lista di oggetti.")
    for idx, log in enumerate(data):
        if not isinstance(log, dict):
            raise ValueError(f"Log {idx} non è un oggetto.")
        required = ["video_id", "keyword", "voice", "hook_type", "metrics"]
        for field in required:
            if field not in log:
                raise ValueError(f"Log {idx}: campo '{field}' mancante.")
        metrics = log["metrics"]
        if not isinstance(metrics, dict):
            raise ValueError(f"Log {idx}: 'metrics' deve essere un oggetto.")
        metric_fields = ["views_per_hour", "ctr", "retention_rate", "curve_type"]
        for mf in metric_fields:
            if mf not in metrics:
                raise ValueError(f"Log {idx}: metrica '{mf}' mancante.")
    return True

def validate_learned_rules(data):
    if not isinstance(data, dict):
        raise ValueError("L'input delle regole apprese deve essere un dizionario.")
    required_lists = ["low_performing_keywords", "low_performing_voices", "successful_hook_types", "high_performing_tags"]
    for rl in required_lists:
        if rl not in data or not isinstance(data[rl], list):
            raise ValueError(f"Campo '{rl}' mancante o non è una lista.")
    if "dynamic_min_vph" not in data or not isinstance(data["dynamic_min_vph"], (int, float)):
        raise ValueError("Campo 'dynamic_min_vph' mancante o non numerico.")
    return True

SCHEMAS = {
    "candidati-video": validate_candidati_video,
    "seo-report": validate_seo_report,
    "produzione-spec": validate_produzione_spec,
    "brief-miniatura": validate_brief_miniatura,
    "metadati": validate_metadati,
    "performance-logs": validate_performance_logs,
    "learned-rules": validate_learned_rules
}

def main():
    if len(sys.argv) < 3:
        print("Uso: python validate_schemas.py <tipo_schema> <path_json>")
        print(f"Schemi supportati: {list(SCHEMAS.keys())}")
        return 1
        
    schema_type = sys.argv[1]
    json_path = sys.argv[2]
    
    if schema_type not in SCHEMAS:
        print(f"Errore: schema '{schema_type}' sconosciuto. Scegli tra: {list(SCHEMAS.keys())}")
        return 1
        
    if not os.path.exists(json_path):
        print(f"Errore: file '{json_path}' non trovato.")
        return 1
        
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        SCHEMAS[schema_type](data)
        print(f"PASS: Il file '{json_path}' è conforme allo schema '{schema_type}'.")
        return 0
    except json.JSONDecodeError as je:
        print(f"FAIL: Errore sintattico JSON in '{json_path}': {je}")
        return 2
    except ValueError as ve:
        print(f"FAIL: Errore di validazione dello schema '{schema_type}': {ve}")
        return 3

if __name__ == "__main__":
    sys.exit(main())
