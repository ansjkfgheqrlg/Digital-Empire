# CHECKLIST-CONSEGNA — PreventivoForge

Procedura fissa per produrre e consegnare una build. Seguire in ordine, senza saltare passi.
(Motivo di ogni passo: vedi `REGISTRO-ERRORI.md`.)

## Prima di ricostruire l'exe
- [ ] **Chiudere l'app** (`PreventivoForge.exe`) + i Chrome automatici. Se resta aperta, build e zip falliscono in silenzio (E8, E9).
- [ ] `git pull --rebase` (allineamento con Gael).

## Build
- [ ] `python -m PyInstaller --noconfirm --clean preventivo-forge.spec`
- [ ] Verificare **`BUILD_EXIT=0`** e che l'**exe abbia timestamp fresco** (non quello vecchio).

## Preparazione pacchetto (accanto all'exe, in `dist/PreventivoForge/`)
- [ ] Ripristinare `.env` con le righe `TRANSLATE_AI_*` (chiave riserva AI).
- [ ] Ripristinare `LEGGIMI.txt`.

## Verifica
- [ ] `PreventivoForge.exe --selftest <fixture.html> <foto>` → **EXIT=0**, gate verdi, PDF creato.
- [ ] **Test live su 2-3 auto DIVERSE** (marche/anni diversi): 0 residui tedeschi, PDF ok, ~30-60s.

## Pulizia + zip
- [ ] Rimuovere da `dist/PreventivoForge/`: `runs/ logs/ selftest.log browser-profile/ archivio/ preventivi_*`.
- [ ] `Compress-Archive` → `Consegna-Novacar/PreventivoForge-Novacar.zip`. Verificare la **dimensione** (~120 MB, non 0).

## Consegna
- [ ] Guida: `COME-CONSEGNARE-A-NOVACAR.md`. Requisiti PC cliente: Google Chrome + linea normale (no VPN).
- [ ] Aggiornare `STATO-EMPIRE.md` + push.

## Regola d'oro
**Ogni errore nuovo → scriverlo in `REGISTRO-ERRORI.md` con la regola per non ripeterlo.**
