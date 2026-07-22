# 📥 BACKLOG — cose rimandabili (NON bloccano la costruzione)

> Regola (ADR-005): quando spunta un task minore/decisione non strutturale, finisce QUI,
> non ferma mai una fase. Si svuota nei momenti morti o quando una fase lo richiede davvero.
> Chiunque (Max, Gael, agenti) aggiunge righe; si spunta con data.

| # | Cosa | Note | Quando serve davvero | Stato |
|---|---|---|---|---|
| B-001 | Rinnovare token FB (scraper outreach) | developers.facebook.com/tools/explorer → .env | solo per run scraper FB reale (gli altri canali outreach girano) | ⬜ |
| B-002 | Prezzo "Manuale Claude Code" + ruolo (prodotto vs lead magnet) | NON si decide a mano: lo proporrà il **team prezzi** (B-003) | gate F6 (lancio reale) | ⬜ |
| B-003 | Team agenti PREZZI | skill `pricing` (installata) come motore + beast-preventivi; team L4 in 04-MARKETING/Analytics o 02-INFO-BUSINESS/Vendite; propone prezzi data-driven, Max approva | fase F5/F6 | ⬜ |
| B-004 | Gael: completare `git config user.email` reale | cosmetico (firma commit) | mai bloccante | ⬜ |
| B-005 | Estendere skill `empire-context` con references/ (Mandato esteso, brand guide, listino) | previsto da dossier 07 §3.2.1 | fase F2-bis/B3 backbone | ⬜ |
| B-006 | Pulire 5 stub v1 in `03-CONTENT-FACTORY/Reparti/` (Strategia, Produzione-Video, Produzione-Testuale, Visual-Design, Pubblicazione — README singoli del F1-bis 2026-06-11) | superati dalle cartelle v2 `CF-RN-*` complete; sono solo README orfani che sporcano il gate. Da archiviare/rimuovere con ok (non creati in questa sessione) | pulizia, non urgente | ⬜ |
| B-007 | PreventivoForge: normalizzare trattini/spazi nel match glossario S3 | Oggi `xenon-scheinwerfer` ≠ `xenonscheinwerfer` ≠ `xenon scheinwerfer`: servono voci separate. Un normalizzatore (togli `-`/spazi prima del lookup) coprirebbe tutte le varianti in un colpo. Vedi CP-20260702-001 | quando Gate B blocca spesso per varianti trattino | ⬜ |
| B-008 | Blob video ingestioni (SKILL & Agenti: frame+mp4, ~900MB history) → Git LFS o gitignore + storage locale | Il push del main completo muore (pack 899MB, rete instabile): oggi risolto con work-sync leggero 1b7842ad, ma ogni sync futuro con video ripropone il problema. Decidere: LFS, o ignore + backup locale | prima della prossima ingestione grossa | ⬜ |
| B-009 | **Collisione ID checkpoint: 3 volte in 15 minuti il 2026-07-22** | Max/Claude e Gael hanno creato CP-20260722-002 e CP-20260722-003 in parallelo → 3 conflitti add/add di fila, risolti a mano rinumerando in 005 e 006. Causa: l'ID si assegna contando i file a occhio. Fix già specificato: lock su file in `empire/memory/store.py` (GEM-02 §4, "Regola anti-collisione ID"), che legge il max NNN sia da atoms.jsonl sia dai nomi file in checkpoints/. Precedente: CP-20260719-006 (002/003 rinumerati 004/005) | chiuso da M-A (`empire/memory/`) — fino ad allora: `git pull` PRIMA di scrivere un checkpoint | ⬜ |
