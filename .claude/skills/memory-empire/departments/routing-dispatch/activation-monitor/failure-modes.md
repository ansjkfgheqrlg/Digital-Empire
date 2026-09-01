# Failure Modes — activation-monitor

## FM-01: Path Empire Studio errato
**Causa:** empire-studio root path diverso dal previsto
**Fix:** Cerca `runs/<run-id>` partendo da `.`, poi da `SKILL & Agenti/Empire Studio Suite/empire-studio/`

## FM-02: Frame estratti 0 (manifest.json vuoto)
**Causa:** frame_extractor fallito silenziosamente
**Fix:** Segnala "failed" anche se manifest.json esiste ma ha frames=[]
