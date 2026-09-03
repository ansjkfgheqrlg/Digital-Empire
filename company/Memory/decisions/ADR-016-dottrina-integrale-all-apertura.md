# ADR-016 — Dottrina integrale all'apertura, sveglia leggera per messaggio

**Data:** 2026-09-03 · **Stato:** ATTIVO · **Deciso da:** Max
**Supera:** la "doppia scrittura" del mattino (emperator.md §6.13 v1)

## Contesto (misurato, non stimato)
La dottrina di Emperator viaggiava come stringa compressa dentro `scripts/emperator_hook.py`,
reiniettata ad OGNI messaggio contenente il nome:
- promemoria per messaggio: **34.762 caratteri**
- libro vero `.claude/agents/emperator.md`: **57.159 caratteri**

Due conseguenze, entrambe gravi:
1. **Chi diceva "Emperator" riceveva il ~60% di Emperator.** Vale per Max, Gael e Neri.
2. Quel 60% veniva **ripetuto ad ogni messaggio**: una chat da 30 messaggi pagava
   ~1.040.000 caratteri della stessa dottrina.

## Decisione
**Il libro intero, una volta sola, all'apertura della sessione.**
- Nuovo `scripts/emperator_boot.py` (hook SessionStart) inietta `.claude/agents/emperator.md`
  per intero + ancoraggi + dottrina riservata. Registrato in `.claude/settings.json`.
- `scripts/emperator_hook.py` diventa **sveglia leggera**: identita', fotografia fresca
  dell'Impero, stato del caricamento, ordine di rileggere il libro se non e' piu' visibile.
  La stringa `DOTTRINA` (27.552 byte) e' stata rimossa.
- `.claude/agents/emperator.md` e' da adesso **l'unica fonte di verita'**.

## Numeri
| | Prima | Adesso |
|---|---|---|
| all'apertura | 0 | 67.127 caratteri |
| per messaggio | 34.762 | 2.008 |
| chat da 30 messaggi | ~1.042.900 | ~127.400 |
| quanto e' Emperator | 60% | **100%** |

Il pareggio arriva al **terzo messaggio**: da li' in poi e' sempre piu' conveniente.

## Rischio e mitigazione
- **Niente piu' copia di riserva.** Se il libro sparisce, non c'e' un secondo corpo.
  Mitigazione: `emperator_boot.py` inietta un GUASTO esplicito e ordina di dichiararlo.
- **Contesto compattato**: il libro puo' uscire dalla conversazione. Mitigazione: il boot
  lascia un file-spia nella cartella temporanea di sistema (mai nel repo, ADR-013); la
  sveglia lo legge e, se manca, ordina di riaprire e rileggere il libro subito.
- **Hook di apertura non partito**: stessa mitigazione del punto sopra.

## Verifica eseguita
```
py -3 -c "ast.parse(...)" su entrambi gli script      -> SYNTAX OK
printf '{"source":"startup"}' | py -3 scripts/emperator_boot.py | wc -c  -> 67127
printf '{"prompt":"emperator"}' | py -3 scripts/emperator_hook.py | wc -c -> 2008
printf '{"prompt":"ciao"}'      | py -3 scripts/emperator_hook.py | wc -c -> 0
```
