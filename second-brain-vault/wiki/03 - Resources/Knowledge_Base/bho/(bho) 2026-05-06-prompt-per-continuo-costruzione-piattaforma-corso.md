# prompt per Continuo costruzione piattaforma corso.
            
> Path: [[Map - Bho|bho]]

## Content

Continuiamo lo sviluppo della piattaforma Formazione Empire in:
c:/Users/Utente/Desktop/qui tutto/Digital Empire/Lancio corso skill beast/Sale pag/Siti CCM/formazione-empire

Prima di toccare qualsiasi cosa leggi questi 2 file per assorbire lo stato:
1. HANDOFF.md in root del progetto (tutto lo stato, regole, bug noti, piano residuo)
2. C:/Users/Utente/.claude/projects/c--Users-Utente-Desktop-qui-tutto-Digital-Empire-Lancio-corso-skill-beast-Sale-pag-Siti-CCM/memory/formazione-empire-stato-ui.md

REGOLA NON NEGOZIABILE: zero dark-on-dark. Ogni card/form/pannello su fondo scuro
DEVE usare .card-fill-silver o .card-fill-silver-orange (definite in src/app/globals.css).
Mai usare .card-dark su bg-ink / bg-ink-2 / #1c1c1c / #2a2a2a.

Il corso si chiama "Da AI User a System Architect" (NON più "Claude Code Mastery"),
slug URL rimane claude-code-mastery.

Dopo aver letto HANDOFF.md e la memoria, fai un audit nel seguente ordine:
1. Grep "card-dark" in src/app/corsi/** e src/app/(auth)/** e src/components/** → segnala residui
2. Apri src/app/corsi/[courseSlug]/moduli/[moduleSlug]/[lessonSlug]/page.tsx
   e elenca ogni blocco ancora dark-on-dark da convertire (descrizione, mark-complete, risorse, drawer)
3. Ispeziona src/components/video-player.tsx e segnala cosa manca per il restyle orange premium
4. Verifica src/components/student-header-client.tsx e admin-shell.tsx per dark-on-dark
5. Proponi l'ordine di attacco delle task della sezione 3 di HANDOFF.md

Poi aspetta le mie istruzioni prima di modificare qualcosa.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Lancio_Corso_Skill_Beast|Lancio Corso Skill Beast Area]]
