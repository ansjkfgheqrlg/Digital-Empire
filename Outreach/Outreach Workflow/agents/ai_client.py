"""
AI Client Factory — Digital Empire Outreach
Gestisce la rotazione dei modelli: Groq (primary) → OpenRouter (fallback).
"""

import os
import time
import openai
from openai import OpenAI


def build_rotation(openrouter_api_key: str) -> list:
    """
    Rotazione interleaved Groq → OpenRouter → Groq → OpenRouter.
    Se Groq è rate-limited, il prossimo tentativo è subito OpenRouter (non un altro Groq
    con lo stesso budget TPM esaurito). Riduce i fallimenti a cascata.
    """
    groq_key = os.getenv("GROQ_API_KEY", "").strip()

    if groq_key and openrouter_api_key:
        groq = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=groq_key, timeout=45)
        or_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_api_key, timeout=60)
        return [
            # OpenRouter prima (rate limit più generosi) — Groq in fondo come backup
            (or_client, "meta-llama/llama-3.3-70b-instruct:free"),
            (or_client, "nousresearch/hermes-3-llama-3.1-405b:free"),
            (or_client, "openai/gpt-oss-120b:free"),
            (or_client, "nvidia/nemotron-3-super-120b-a12b:free"),
            (or_client, "deepseek/deepseek-v4-flash:free"),
            (or_client, "qwen/qwen3-14b:free"),
            (or_client, "qwen/qwen3-8b:free"),
            (or_client, "google/gemma-3-27b-it:free"),
            (or_client, "mistralai/mistral-7b-instruct:free"),
            (or_client, "microsoft/phi-4-reasoning:free"),
            (or_client, "google/gemma-2-9b-it:free"),
            (or_client, "thudm/glm-4-9b:free"),
            (or_client, "mistralai/devstral-small:free"),
            (groq,      "llama-3.1-8b-instant"),   # Groq in fondo — TPM basso
            (groq,      "llama-3.3-70b-versatile"),
        ]

    if groq_key:
        groq = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=groq_key, timeout=45)
        return [
            (groq, "llama-3.1-8b-instant"),
            (groq, "llama-3.3-70b-versatile"),
        ]

    if openrouter_api_key:
        or_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_api_key, timeout=60)
        return [
            (or_client, "meta-llama/llama-3.3-70b-instruct:free"),
            (or_client, "nousresearch/hermes-3-llama-3.1-405b:free"),
            (or_client, "openai/gpt-oss-120b:free"),
            (or_client, "nvidia/nemotron-3-super-120b-a12b:free"),
            (or_client, "deepseek/deepseek-v4-flash:free"),
            (or_client, "qwen/qwen3-14b:free"),
            (or_client, "qwen/qwen3-8b:free"),
            (or_client, "google/gemma-3-27b-it:free"),
            (or_client, "mistralai/mistral-7b-instruct:free"),
            (or_client, "microsoft/phi-4-reasoning:free"),
            (or_client, "google/gemma-2-9b-it:free"),
            (or_client, "thudm/glm-4-9b:free"),
            (or_client, "mistralai/devstral-small:free"),
        ]

    return []


def call_ai(rotation: list, messages: list, max_tokens: int,
            temperature: float = 0.5, label: str = "AI") -> str | None:
    """
    Chiama il modello AI con retry automatico su tutta la rotation.
    Restituisce il testo della risposta, o None se tutti falliscono.
    """
    for attempt, (client, model) in enumerate(rotation):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            msg = response.choices[0].message
            content = msg.content or getattr(msg, "reasoning", None) or getattr(msg, "reasoning_content", None)
            if content:
                return content.strip()

        except openai.APITimeoutError:
            provider = "Groq" if "groq" in str(client.base_url) else "OpenRouter"
            print(f"[{label}] Timeout {provider}/{model.split('/')[-1]} — passo al prossimo modello")

        except (openai.RateLimitError, openai.APIStatusError) as e:
            if isinstance(e, openai.APIStatusError) and getattr(e, "status_code", 0) != 429:
                print(f"[{label}] Errore API {e.status_code}: {e}")
                break
            wait = min(15 * (attempt + 1), 60)
            provider = "Groq" if "groq" in str(client.base_url) else "OpenRouter"
            print(f"[{label}] Rate limit {provider}/{model.split('/')[0]} "
                  f"(tentativo {attempt+1}/{len(rotation)}), attendo {wait}s...")
            time.sleep(wait)

        except Exception as e:
            if attempt < len(rotation) - 1:
                time.sleep(3)
            else:
                print(f"[{label}] Errore: {e}")

    return None
