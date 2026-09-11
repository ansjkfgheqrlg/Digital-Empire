# MISURA-DOPO — Sito Agency Vivo, 2026-09-11 sera

Stesso strumento del "prima" (`site_capture.py`), stesse metriche. Prima = il live catturato alle 19:55
(`61-agency-baseline`); Dopo = il sito nuovo catturato sul dev server con le immagini di anteprima
(`62-agency-dopo`), poi verificato sul live dopo il deploy.

| Misura | Prima (live) | Sorgente locale v1 | **Dopo** | Obiettivo | Esito |
|---|---|---|---|---|---|
| Altezza desktop | 21.215 px | 43.359 px | **14.827 px** (live: 14.798) | ≤ 24.000 | ✅ −30% sul live, −66% sul sorgente |
| Altezza mobile (390) | 32.482 px | 70.173 px | **21.335 px** | — | ✅ −34% |
| CTA verso la chiamata | 7 | 11 | **10** nelle sezioni dichiarate (N1, N4, N5, N7, N8, N10, N12, N14, N16, N18) + navbar + sticky | 10 a temperatura | ✅ |
| Fotografie | 0 | 0 | **12 AURA + 2 ritratti + 1 oggetto-icona** (in dev); in produzione: segnaposto finché i file non arrivano | 14 | ✅ composizione / ⏳ file |
| `alt` vuoti sulle foto | — | — | **0 / 12** | 0 | ✅ |
| Dimensioni tipografiche distinte | 90 | 195 | **~16** (11 del canone v3 + 5 residue in navbar/sticky/prenota, componenti v1 non riscritti) | ≤ 12 | ⚠️ deroga: i tre componenti legacy restano fuori da questo cantiere (B-069) |
| Sfondi di sezione | 10 | 48 | **3 + 1 fascia** (ink, carta, stanza, arancione) | 3 + 1 | ✅ |
| H1 | 1 | 1 | **1** (ASCOLTA BENE. è manifesto fuori gerarchia) | 1 | ✅ |
| Heading totali | 56 | 125 | **20** | — | ✅ |
| Divider | 16 | 16 | **0** (cucitura fotografica o alternanza piatta) | 0 | ✅ |
| Link che risolvono | — | — | **13/13** sul live, 0 rotti | 100% | ✅ |
| Lighthouse mobile a11y / SEO / best-practices | — | — | **100 / 100 / 96** | ≥ 95 | ✅ |
| Lighthouse mobile performance | — | — | **77-78** (LCP 3,9 s) | ≥ 85 | ❌ deroga dichiarata: font 900 + motion; i 404 delle foto non ancora generate pesano sul punteggio. B-068 |
| `gate_siti.py` sull'export | — | — | **PASS** (5 controlli vivi; 6 WARN sugli anni, che sono date di fatti) | PASS | ✅ |
| `gate_voce.py` sul copy | — | — | **PASS** (19 sezioni, lista nera 0, Barnum 0, provocazioni pagate) | PASS | ✅ |
| `aura_prep.py --check` | — | — | **PASS** (0 originali in `public/`) | PASS | ✅ |
| Overflow orizzontale mobile | — | — | scrollWidth 390 = viewport | 0 | ✅ |
| Target touch < 44 px | — | — | 0 dopo la correzione delle frecce del carosello | 0 | ✅ |

**Le due leggi di Max, verificate a occhio sullo screenshot intero (desktop 1440 + mobile 390):** grana su
ogni superficie (4 strati fissi + locale su ink/carta/stanza/fascia/foto/cucitura); ogni riga su foto su
banda scura, leggibile. Un difetto trovato e corretto prima del deploy: "EMPIRE" copriva il titolo.

**Cosa dipende da Max (non blocca, il sito è vivo):** i 12 file generati (brief nel manifest) + il suo
ritratto + quello di Gael in `public/aura/` con i nomi del manifest — a quel punto le foto compaiono
senza toccare una riga di codice; P.IVA e indirizzo in `src/lib/legal.ts`.
