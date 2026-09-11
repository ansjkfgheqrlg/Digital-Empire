# LEZIONE — cantiere agency-empire-vivo (Dossier 37)

**Data:** 2026-09-11 · **Corsia:** B (Next.js 16) · **URL vivo:** https://agency-empire-kohl.vercel.app ·
**Misure:** `agency-empire/cantiere/MISURA-DOPO.md` · **Piano:** `PIANO-MAESTRO/37-PIANO-SITO-AGENCY-VIVO.md`

## Cosa ha funzionato (candidati a pattern, §10: al secondo cantiere diventano pattern)
1. **Il manifest delle immagini come contratto** (`public/aura/manifest.json`): copy, alt, riga, sorgente e
   trattamento in una riga per foto; il componente `<Aura/>` legge solo il nome file. Cambiare corsia
   (originale → generata → ritratto vero) non tocca un componente. Riusabile per ogni sito con foto.
2. **`gate_voce.py`**: quattro controlli deterministici sul copy prima del layout. Ha trovato 13 difetti veri
   al primo giro (sezioni senza prima persona, provocazioni senza numero). Promosso a gate della Fabbrica.
3. **Superfici `.sv-*` con la grana dentro** (vivo.css): la grana fissa sopra un gradiente si perde; quella
   locale nello stack no. È la legge di Max resa CSS.
4. **La riga su banda scura** (`.riga`): un solo blocco CSS, riusato 12 volte, leggibile su ogni foto.
5. **Fallback a tre livelli per una foto che manca**: segnaposto con nome (team) / fondo AURA vuoto con la
   riga (generate non arrivate) / mai un'icona rotta. Il sito è deployabile PRIMA che le foto esistano.

## Errori fatti (§10: al secondo errore diventano controllo del gate)
1. **`next build` con `distDir: dist` ha spazzato `dist/dev` mentre il dev server girava** → 500 su tutte
   le pagine, cattura "dopo" a 15 px. Regola: mai `next build` con un `next dev` acceso sulla stessa
   `distDir`; oppure `distDir` diversa per il dev.
2. **`gate_siti.py` risolveva gli href root-relative (`/prenota`) dalla cartella della pagina**, non dalla
   radice: bocciava ogni sito Next. Corretto nel gate con commento e data (§9: si corregge il gate).
3. **`onError` di `<img>` non scatta se il 404 arriva prima dell'idratazione**: i segnaposto non
   comparivano. Controllo al mount (`complete && naturalWidth === 0`).
4. **La navbar v1 era blu navy** (`#062155`, fuori canone) e nessuno l'aveva notata finché non è stata
   accanto alle sezioni nuove: i componenti condivisi vanno passati al canone PRIMA delle sezioni.
5. **Il "prima" sbagliato**: il sorgente locale (43.359 px) non era il live (21.215 px). Il deploy era
   vecchio di un mese e mezzo. Misurare sempre il live, mai il sorgente.
6. **Numeri del sito v1 senza prova** ("40+ automazioni", "+300% produttività"): tolti, non ammorbiditi.

## Debito dichiarato (BACKLOG)
- B-068 perf mobile 77 → ≥ 85 (font 900, motion, 404 delle foto non ancora generate)
- B-069 navbar / sticky-cta / prenota: portare la scala tipografica al canone v3 (16 → ≤ 12 dimensioni)
- B-070 pagina-ponte `/ponte` (F7.5) — solo con la riga nella Bibbia dei Messaggi
- B-071 testimonianze con nome, foto e link (N13) quando esistono
