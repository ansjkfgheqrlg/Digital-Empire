# MISURA-DOPO — Sito Agency Vivo v2 su `agency-empire-landing` (F5, 2026-09-12)

Stesso strumento del "prima" (`site_capture.py`, 1440×900 desktop / 390 mobile), servito da `out/` (l'HTML che va in produzione),
**due volte** (C3.1/C3.4): manifest **vuoto** = quello che va online il giorno del deploy; manifest **pieno** = con le 10 immagini di
preview locale (mai in `public/`). Catture: `capture/64-agency-landing-dopo-vuoto/`, `capture/65-agency-landing-dopo-pieno/`.

| Misura | PRIMA (live, 63) | DOPO vuoto (64) | DOPO pieno (65) | Obiettivo | Esito |
|---|---|---|---|---|---|
| Altezza desktop | 38.683 px | **14.893 px** (−62%) | **17.063 px** (−56%) | ≤ 21.000 / ≤ 24.000 | PASS |
| Altezza mobile | 64.255 px | **18.370 px** | **22.942 px** | ≤ 36.000 / ≤ 40.000 | PASS |
| Sezioni | 37 + 5 divider | 20 + coda, 0 divider | idem | 20 + coda, 0 divider | PASS |
| CTA | 10 (metà verso `#prenota`, il resto in 3 salti sul brand del corso) | **14** = 10 di sezione + header + sticky + 2 «Non mi ritrovo»/ancora | idem | 10 di sezione, tutte a `/prenota/` via `<Link>` | PASS |
| Fotografie | 0 (143 icone) | 0 (composizione B ovunque) | **9** in pagina (+1 su N19 in filigrana se arriva la dashboard) | 15 posti, `alt` 15/15 | PASS (posti cablati; i file veri arrivano senza toccare codice) |
| Dimensioni tipografiche distinte | **64** (186 combinazioni) | **12** (26 combinazioni size/lh/peso) | 12 | ≤ 12 | PASS |
| Sfondi | 42 | 7 (ink, carta, marquee, DM ×2, arancione bottoni, hairline) — 3 sfondi + fascia | 7 | 3 + fascia | PASS |
| Famiglie di gradiente sulle card | 5 | **0** | 0 | 0 | PASS |
| Heading | 120 | 29 | 29 | — | — |
| Blocchi | 880 | 270 | 280 | — | — |
| Placeholder / numeri senza fonte | `TODO`, `IL_TUO_ID_LOOM`, "312·24·1.4k", "99,7%", "12 mesi", "50+ sistemi" | **0** (`gate_fatti.py` PASS, `gate_siti.py` PASS) | 0 | 0 | PASS |
| `netlify.app` / `#prenota` / `href="#"` in `src/` (fuori `_v1`) | 6 / 8 / 3 | **0 / 0 / 0** | — | 0 | PASS |
| Prezzi scritti a mano fuori da `listino.ts` | 11 in 3 file | **0** | — | 0 | PASS |
| `robots` | `index:false` | `index:true` su Vercel, `index:false` solo con `GH_PAGES_BASE` | — | — | PASS |

**Deroghe:** nessuna. **Note:** la scala 8,8 px è `small` dentro `.sv-btn` (sottotitolo del bottone principale) — dichiarata, sotto i 12.
Il gate `gate_siti.py` segna 5 WARN: «2026» nelle date del caso Novacar e degli aggiornamenti privacy/cookie (date di fatto, non scadenze),
e `data-prezzo` senza regola CSS di corpo (il corpo è `sv-stat`, non misurabile dal gate).
