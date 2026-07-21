---
id: RB-001
type: reasoning-bank
title: "edit-and-verify: grep/runtime check dopo ogni modifica a file critici"
created: 2026-07-21 13:46:06
trace: "RB-001#estate-2026"
project: ESTATE-2026-REVENUE
---

# RB-001 — edit-and-verify: grep/runtime check dopo ogni modifica a file critici

- **Pattern:** edit-and-verify: grep/runtime check dopo ogni modifica a file critici
- **Evidenza:** PERF-001: edit SUBDIRS non persistito; scoperto solo perche' test live fallito. Senza verify = bug silenzioso
- **Riutilizzo:** automatico nei WF futuri (WF-*-IMPROVE)

