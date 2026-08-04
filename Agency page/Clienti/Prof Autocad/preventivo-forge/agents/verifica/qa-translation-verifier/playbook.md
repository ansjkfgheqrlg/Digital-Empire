# Playbook — qa-translation-verifier

## Quando gira
Dopo S3 (prima di S4). Chiamata: `gate_b(ctx, dealer)`.

## Interpretare i risultati
| Issue | Significato | Azione |
|---|---|---|
| `N residui tedeschi in content: [...]` | termini non tradotti | estendi `glossary_de_it.py`, ri-esegui S3 |
| `equipment_it non allineato 1:1` | voci aggiunte/perse | correggi `translate_equipment` |
| `title_it non deve contenere il prezzo` | prezzo nel titolo | il prezzo va solo in `price.final_title` |
| `specs Anno/Km/Potenza alterato` | numero cambiato | non riscrivere i numeri: prendere verbatim |
| `highlights_it > 6` | troppi punti | limita a 6 |

## Loop di correzione
1. Rosso per residui → aggiungi i termini mancanti al glossario.
2. Ri-esegui `translate` → ri-esegui `gate_b`.
3. Ripeti finché verde. Se un termine è ambiguo dopo 2 giri → escalation a Gael.

## Riferimento verificato
Run BMW 320d → Gate B PASS dopo aver aggiunto gestione umlaut ASCII + traduzione colori.
