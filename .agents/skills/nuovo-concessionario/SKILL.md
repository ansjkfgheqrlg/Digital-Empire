---
name: nuovo-concessionario
description: "Fabbrica una nuova app PreventivoForge per un concessionario nuovo. Clona il workflow esistente cambiando SOLO nome, dati (P.IVA/sede/contatti), logo, prezzo e colori del preventivo: il motore resta uno solo. Ogni concessionario ottiene la SUA app identica, col suo nome e i preventivi col suo stile. Usa quando Max dice 'ho un nuovo concessionario', 'nuovo cliente concessionario', 'aggiungi la concessionaria X', 'crea l'app per <nome>', '/nuovo-concessionario'. Gestisce anche la LICENZA/abbonamento: se Max dice 'X non paga / ha pagato', blocca/sblocca l'app di quel concessionario + email."
---

# nuovo-concessionario — Fabbrica app per concessionario + gestione abbonamenti

Workflow su disco: `Clienti/Prof Autocad/preventivo-forge/` (è il MOTORE condiviso).
Script fabbrica: `nuovo_concessionario.py` · Console licenze: `gestione-licenze.py`.

## Principio (spiegarlo se serve)
UN motore, tanti concessionari. NON si copia il codice per ogni cliente (un bug si
correggerebbe N volte). Per ogni concessionario cambia SOLO:
- **nome** (titolo dell'app + ragione sociale nel PDF)
- **dati** legali/contatti (P.IVA, sede, telefono, email, PEC)
- **logo**
- **prezzo** (pct + 2 fissi, se diverso)
- **colori** del preventivo (accent + highlight)
Tutto il resto è identico.

## A) NUOVO CONCESSIONARIO — procedura
1. **Raccogli i dati.** Servono: nome/ragione sociale, P.IVA, sede, telefono, email, PEC,
   file logo (png), e — se diversi dai default — pct/fisso1/fisso2 e colori. Chiedi ciò che manca.
   Scegli un `id` slug minuscolo senza spazi (es. "Acme Auto srl" → `acme`).
2. **Crea config + cartella cliente + app brandizzata:**
   ```bash
   cd "Clienti/Prof Autocad/preventivo-forge"
   python nuovo_concessionario.py --id acme --nome "Acme Auto srl" \
     --piva 01234567890 --sede "via Roma 1, Milano, 20100" \
     --tel "02 1234567" --email info@acme.it --pec acme@pec.it \
     --logo "<percorso logo.png>" [--pct 3 --f1 1500 --f2 1500] \
     [--accent "#2b2b2b" --highlight "#f2a200"] --build
   ```
   Output: `concessionarie/acme/` (config+logo), `Clienti/Acme Auto srl/App/PreventivoForge/`
   (app col suo nome), `Clienti/Acme Auto srl/CONSEGNA.md`.
   (`--build` copia il motore già costruito in `dist/PreventivoForge` + stampa `brand.json`.
   Se `dist/` non esiste, costruisci prima il motore: `build_exe.bat`.)
3. **Attiva l'abbonamento (licenza):**
   ```bash
   python gestione-licenze.py aggiungi acme
   ```
   (registra il concessionario come `active` nella lista online — richiede il Gist creato una volta.)
4. **Verifica** (facoltativo ma consigliato): genera un preventivo di prova per quel dealer
   `python run.py --manual tests/fixtures/<annuncio>.html --foto <foto> --dealer acme`
   e controlla che nel PDF ci siano nome/logo/colori giusti + 6 gate verdi.
5. **Consegna** la cartella `Clienti/<Nome>/App/PreventivoForge/` al concessionario
   (requisiti sul suo PC: Google Chrome + linea normale; vedi `CONSEGNA-NOVACAR.md`).

## B) ABBONAMENTO — quando Max dice "X non paga" / "X ha pagato"
1. **Blocca** (non paga): `python gestione-licenze.py sospendi <id>` → l'app di X si blocca
   al prossimo preventivo (entro ~1 min). Poi **manda l'email** di sospensione
   (template `templates/email-sospensione.txt`, via Gmail).
2. **Sblocca** (ha pagato): `python gestione-licenze.py attiva <id>` + email riattivazione.
3. **Stato di tutti:** `python gestione-licenze.py stato`.

## Cosa cambia vs cosa resta (checklist chirurgica)
| Cambia per concessionario | Resta identico (motore) |
|---|---|
| `concessionarie/<id>/config.json` (nome, dati, prezzo, colori) | scraper, parser, pricer, cdp, run.py |
| `concessionarie/<id>/logo.png` | template PDF (parametrico su colori/logo) |
| `brand.json` (titolo app + dealer) | gate A/B/C/D/IMG/R + REGOLE-SACRE |
| voce in lista licenze | licenza.py (kill-switch) |

## File chiave
- Fabbrica: `preventivo-forge/nuovo_concessionario.py`
- Licenze: `preventivo-forge/gestione-licenze.py` + `templates/email-*.txt`
- Doc completa: `preventivo-forge/FABBRICA-CONCESSIONARI.md`
- Motore/regia: `preventivo-forge/run.py` · Config: `concessionarie/<id>/config.json`
