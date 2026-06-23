---
Type: SCRIPTS
Status: Active
Tags: #scripts #CF-R7 #wrapper #orchestratori #publish #pre-publish-check #post-publish
Created: 2026-06-23
Last updated: 2026-06-23
---

# Scripts — CF-R7 Pubblicazione & Distribuzione

> **[WRAPPA] orchestratori Python ATTIVI — runtime NON modificato (ADR-003)**
> I file `main_orchestrator.py` e `mentalita_orchestrator.py` non si toccano mai.
> Questi script sono wrapper e utility che SI AGGIUNGONO attorno ai motori esistenti.

---

## Motori wrappati (ADR-003)

| Motore | Path originale | Canali | Stato |
|---|---|---|---|
| `main_orchestrator.py` | `SKILL & Agenti/Workflow pubblicazione automatica/` | IG, TikTok, LinkedIn, Drive | ATTIVO — non modificare |
| `mentalita_orchestrator.py` | `SKILL & Agenti/Workflow pubblicazione automatica/` | IG brand Mentalità Brutale | ATTIVO — non modificare |

**REGOLA:** qualsiasi script in questa cartella che interagisce con i motori sopra deve:
1. Dichiarare `[WRAPPA] orchestratore Python — runtime non modificato` nell'intestazione.
2. Non modificare nessun parametro interno del motore.
3. Passare solo i parametri esterni previsti dall'interfaccia (vedi contratto sotto).

---

## Contratto wrapper (interfaccia CF-R7 → orchestratori)

Ogni wrapper espone le operazioni seguenti:

```bash
# Verifica connettività e token
check_token <canale> <brand_slug>
# → "VALIDO" | "SCADUTO" | "ERRORE"

# Piano pubblicazione senza effetti reali (dry-run)
dry_run_plan <order_id> <canale> <asset_path> <caption_path>
# → JSON piano pubblicazione (cosa/dove/quando) a zero effetti

# Pubblicazione effettiva (solo dopo review umana documentata)
publish <order_id> <canale> <asset_path> <caption_adattata>
# → URL post pubblicato | codice errore strutturato
```

---

## Script 1 — pre-publish-checker

**File target:** `pre-publish-checker.sh`
**Uso:** Eseguito da CF-R7-QA prima di ogni pubblicazione.
**Funzione:** Verifica le tre condizioni pre-publish (gate verdi + review umana + token).

```bash
#!/usr/bin/env bash
# [WRAPPA] usa check_token() del wrapper — orchestratori non modificati (ADR-003)
# Uso: ./pre-publish-checker.sh <order_id> <canali_csv> <state_json_path>

ORDER_ID=$1
CANALI=$2          # es. "instagram,linkedin"
STATE_PATH=$3

# Check 1: gate verdi in state.json
gate_formato=$(jq -r '.["05-qa"].gate_formato' "$STATE_PATH")
gate_brand=$(jq -r '.["05-qa"].gate_brand' "$STATE_PATH")
gate_copy=$(jq -r '.["05-qa"].gate_copy' "$STATE_PATH")
gate_mandato=$(jq -r '.["05-qa"].gate_mandato' "$STATE_PATH")

if [ "$gate_formato" != "PASS" ] || [ "$gate_brand" != "PASS" ] || \
   [ "$gate_copy" != "PASS" ] || [ "$gate_mandato" != "PASS" ]; then
  echo '{"esito":"FAIL","motivo":"gate CF-R6 non tutti PASS"}'
  exit 1
fi

# Check 2: review umana
review=$(jq -r '.review_umana.eseguita' "$STATE_PATH")
if [ "$review" != "true" ]; then
  echo '{"esito":"FAIL","motivo":"review_umana.eseguita non true"}'
  exit 1
fi

# Check 3: token canali
IFS=',' read -ra CANALE_LIST <<< "$CANALI"
for canale in "${CANALE_LIST[@]}"; do
  token_status=$(./wrap-main-orchestrator.sh check_token "$canale" "$ORDER_ID")
  if [ "$token_status" != "VALIDO" ]; then
    echo "{\"esito\":\"FAIL\",\"motivo\":\"token $canale: $token_status\"}"
    exit 1
  fi
done

echo '{"esito":"PASS","tutti_gate_verdi":true,"review_umana":true,"token_ok":true}'
exit 0
```

---

## Script 2 — channel-adapter

**File target:** `channel-adapter.sh`
**Uso:** Eseguito da CF-R7-ADAPT per adattare caption e formato per ogni canale.
**Funzione:** Applica le regole di lunghezza, hashtag e handle per ogni piattaforma.

```bash
#!/usr/bin/env bash
# Uso: ./channel-adapter.sh <caption_base_path> <brand_kit_path> <canale> <output_path>

CAPTION_BASE=$1
BRAND_KIT=$2
CANALE=$3
OUTPUT=$4

# Carica limiti per canale
case "$CANALE" in
  instagram) MAX_CHAR=2200; MAX_HASHTAG=30; CTA_PATTERN="link in bio" ;;
  linkedin)  MAX_CHAR=3000; MAX_HASHTAG=5;  CTA_PATTERN="link diretto" ;;
  tiktok)    MAX_CHAR=2200; MAX_HASHTAG=5;  CTA_PATTERN="link bio" ;;
  youtube)   MAX_CHAR=5000; MAX_HASHTAG=10; CTA_PATTERN="descrizione" ;;
  *)         echo '{"esito":"FAIL","motivo":"canale non riconosciuto"}'; exit 1 ;;
esac

# Legge handle canale da brand_kit
HANDLE=$(jq -r ".handle.$CANALE // empty" "$BRAND_KIT")

# Applica adattamento (logica in output JSON)
python3 - <<PYEOF
import json, sys

caption = open("$CAPTION_BASE").read().strip()
brand_kit = json.load(open("$BRAND_KIT"))
hashtags = brand_kit.get("hashtag_${CANALE}", brand_kit.get("hashtag_default", []))

# Tronca se necessario (mantiene hashtag in fondo)
body = caption[:${MAX_CHAR}-200]
hashtag_str = " ".join(["#" + h for h in hashtags[: ${MAX_HASHTAG}]])
final = f"{body}\n\n{hashtag_str}"

result = {
    "canale": "$CANALE",
    "caption": final[:${MAX_CHAR}],
    "char_count": len(final),
    "hashtag_count": len(hashtags[: ${MAX_HASHTAG}]),
    "handle": "$HANDLE",
    "cta_note": "$CTA_PATTERN"
}
json.dump(result, open("$OUTPUT", "w"), ensure_ascii=False, indent=2)
print(json.dumps({"esito": "OK", "output": "$OUTPUT"}))
PYEOF
```

---

## Script 3 — post-publish-verifier

**File target:** `post-publish-verifier.sh`
**Uso:** Eseguito da CF-R7-CHECK dopo ogni pubblicazione.
**Funzione:** Verifica HTTP che l'URL del post sia attivo; registra in trace.jsonl.

```bash
#!/usr/bin/env bash
# Uso: ./post-publish-verifier.sh <order_id> <canale> <url> <trace_jsonl_path>

ORDER_ID=$1
CANALE=$2
URL=$3
TRACE_PATH=$4

TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Verifica HTTP (timeout 30s)
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 30 "$URL")

if [ "$HTTP_STATUS" = "200" ] || [ "$HTTP_STATUS" = "301" ] || [ "$HTTP_STATUS" = "302" ]; then
  ESITO="URL_ATTIVO"
else
  ESITO="FAIL"
fi

# Append a trace.jsonl
echo "{\"ts\":\"$TS\",\"agent\":\"cf-r7-check\",\"event\":\"post_check\",\"canale\":\"$CANALE\",\"url\":\"$URL\",\"http_status\":$HTTP_STATUS,\"esito\":\"$ESITO\"}" >> "$TRACE_PATH"

echo "{\"order_id\":\"$ORDER_ID\",\"canale\":\"$CANALE\",\"url\":\"$URL\",\"http_status\":$HTTP_STATUS,\"esito\":\"$ESITO\",\"ts\":\"$TS\"}"

[ "$ESITO" = "URL_ATTIVO" ] && exit 0 || exit 1
```

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — architettura wrapper e gate
- [[principi/PRINCIPI]] · `principi/PRINCIPI.md` — principio ADR-003 e review umana
- [[cf-r7-publish]] · `agenti/cf-r7-publish.md` — usa wrap-main e wrap-mentalita
