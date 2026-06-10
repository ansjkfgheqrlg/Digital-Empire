# skill-news-scout

> Source: File system (`SKILL & Agenti\SKILL\Skill - script video lancio CCM\skill-news-scout.md`)
> Collected: 2026-05-06
> Published: Unknown

---
name: skill-news-scout
description: >
  Skill per l'Agente Scout (Web Researcher).
  Forza l'interazione web preventiva per trovare notizie fresche,
  trend dal canale di @gianma.ai e release AI prima di generare script.
---

# SCOUT NEWS & TREND ANALYZER — STEP 0
# by Digital Empire
# Versione: 1.0 (Web Integrated)

═══════════════════════════════════════════════════════════════
## OBIETTIVO
═══════════════════════════════════════════════════════════════
Prima di generare qualsiasi batch di script, tu (Intelligenza Artificiale) devi usare il tuo tool browser / web search per fare "Web Scouting". L'obiettivo è estrarre dalle testate o da Instagram *almeno un trend scottante o una novità tecnica di nicchia*, affinché 1-2 script del batch siano sempre sulla "cresta dell'onda" (novità).

═══════════════════════════════════════════════════════════════
## FONTI PRIMARIE DI RICERCA
═══════════════════════════════════════════════════════════════

### 1. INSTAGRAM (@gianma.ai)
- **URL Obbligatorio:** `https://www.instagram.com/gianma.ai?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==`
- L'analisi del suo profilo è **obbligatoria**.
- **Nota Tecnica per l'AI:** Instagram spesso blocca i browser bot con schermi di login. Se non riesci ad accedere o vedere i feed video, **NON ti fermare**. Estrai i meta-tag, le preview e poi incrocia i dati, oppure salta immediatamente al punto 2 senza farti bloccare e senza gettare la spugna.

### 2. RICERCHE WEB AGGIUNTIVE (Fallback & Integrazione)
Se IG è inacessibile o non ha novità rilevanti, devi usare la ricerca semantica / query string per trovare le vere novità, cercando:
- "Novità su Claude Code di questa settimana"
- "Ultimi update Anthropic"
- "Agenti AI novità / trend tech"
- "Tool open source AI rilasciati di recente GitHub"

═══════════════════════════════════════════════════════════════
## COSA COSTITUISCE UNA "NEWS FRESCA"?
═══════════════════════════════════════════════════════════════

Le novità che devi prendere non sono "L'AI cambierà il mondo". Roba generica è bannata. Le novità devono essere "tecniche":
- Hanno appena aumentato i limiti dei token a 200k.
- Qualcuno ha pubblicato un tool su GitHub (es. un orchestratore) poche ore fa.
- È stato rilasciato un nuovo aggiornamento che integra un terminale invisibile.
- Una polemica o un blocco dell'API (es. "Claude ha bloccato gli account per scraping").

═══════════════════════════════════════════════════════════════
## FASE OPERATIVA 
═══════════════════════════════════════════════════════════════

1. **TRIGGER:** Appena l'utente digita "Generami 5 script", tu NON devi mai partire stampando a schermo il testo. Devi eseguire la Web Search ORA.
2. **ANALISI:** Entra nella pagina di @gianma.ai o fai la search su Claude updates.
3. **ISOLAMENTO DEL FOCUS:** Scegli 1 O 2 concetti chiave (tool appena emersi, update freschi) e trasformali negli Argomenti Tecnici degli Script "News-based".
4. **FORMATO:** Assegna a questi argomenti il Formato "DISCOVERY/NEWS" presente in `Skill.md`, usando il Pattern "Qualcuno ha appena rilasciato...".
5. **INTEGRAZIONE:** Procedi alla stesura dei 5 script. I primi 1/2 dovranno essere la diretta conseguenza della tua ricerca reale sul web.
