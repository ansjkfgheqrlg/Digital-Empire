# ingestion-archive / memory-wiki-bridge

**Ruolo:** Sincronizza `company/Memory/` (REGOLA ZERO — checkpoints, STATO-EMPIRE, decisions/ADR)
con `second-brain-vault/wiki/` (REGOLA FONDAMENTALE). E' il gemello di wiki-syncer ma per il
lavoro INTERNO di Digital Empire, non per i contenuti ingeriti da Empire Studio.

## Perche' esiste
wiki-syncer si attiva solo a fine ingestione Empire Studio (video/tiktok/web/repo). Il lavoro
interno (checkpoint chiusi, ADR, decisioni in STATO-EMPIRE) non passava MAI da nessun agente di
sync — risultato: due sistemi di memoria paralleli, uno sempre rispettato (company/Memory) e uno
quasi mai (wiki). Buco reale trovato il 2026-08-23 (16gg, 16 checkpoint mai in wiki).

## Quando si attiva
- Su comando esplicito `/sync-wiki-totale`.
- (Se in futuro cablato) a chiusura di ogni checkpoint, come da REGOLA ZERO CLAUDE.md.

## Principi
- Stessa tracciabilita' di wiki-syncer: ogni pagina nasce da un checkpoint/ADR/entry STATO-EMPIRE
  preciso (file:riga), mai riassunta a caso.
- Doppio salvataggio invariato: company/Memory resta la fonte di verita' operativa, la wiki e'
  la vista pubblica/navigabile con grafo.
- MAI sovrascrivere: se la pagina esiste, aggiorna/appendi.
