# 📊 DASHBOARD ESTATE-2026 (aggiornata EOD h19:00 da WF-MEM-EOD)
> Ordine: prima € e lead, poi diagnostica. Anti-vanity (P6).

## STATO — ultimo aggiornamento: 21/07 (bootstrap)

### 💰 Incassi & chiusure
| KPI | Oggi | Cumulato | Target 26/07 | Trend |
|---|---|---|---|---|
| € incassati S1 (anticipi) | 0 | 0 | >0 (minimo) · 2-3 anticipi | — |
| € incassati S2 (Manuale) | 0 | 0 | >0 | — |
| Anticipi chiusi | 0 | 0 | ≥1 | — |
| Vendite Manuale | 0 | 0 | ≥1 | — |

### 📈 Leading indicators
| KPI | Target cumulato | Oggi |
|---|---|---|
| s1_lead_contattati | 7 (entro 23/07 h12) | 0 |
| s1_risposte | ≥4 | 0 |
| s3_caroselli_pubblicati | ≥3 | 0 |

### 🚦 Gates
| Gate | Deadline | Stato |
|---|---|---|
| Gate-DEC (DEC-001 attiva) | 21/07 h20:00 | 🟡 veto in corso |
| Gate-FUNNEL (test €1) | 22/07 h20:00 | ⬜ |
| Gate-CONTATTI (7/7) | 23/07 h12:00 | ⬜ |
| Gate-S5 (Fliki test) | 23/07 h18:00 | ⬜ |
| Gate-S4 (E2E auto) | 24/07 h20:00 | ⬜ |
| Gate-REV (≥1 anticipo) | 26/07 | ⬜ |

### 🧵 Decisioni (memory)
- DEC-EST-001 prezzo Manuale — **veto scade OGGI h20:00** → poi ATTIVA (€67/€97)
- DEC-EST-002 nome = Preventa — veto 22/07 h12:00
- DEC-EST-004 nicchia YT = AI/Claude IT — veto 24/07 h18:00

---

# 🔁 PROTOCOLLO RETRO — domenica 26/07 (WF-MEM-RETRO, owner: strategy + memory-architect)
1. `python3 00-MEMORY/memory_manager.py status` + `search` → numeri veri.
2. Per stream S1..S6: ✅ funzionato / ⚠️ parziale / ❌ fallito + **causa radice** (1 riga, onesta).
3. Pattern vincenti → `pattern --title ... --evidence ...` (ReasoningBank): oggetti WA con più risposte, hook caroselli con più engagement, sequenze chiuse, argomenti che hanno sbloccato "ci sentiamo a settembre".
4. Errori → già in `errors/` se i reparti hanno rispettato il protocollo; completare fix.
5. Nuove decisioni per agosto/settembre → `decision`.
6. Sync: copiare CP settimanale + pattern nel second-brain (long-term).
7. Chiusura: `checkpoint --task RETRO-20260726`.
8. Output sintesi: una tabella €/lead per stream + 3 azioni per la settimana 27/07→02/08.
