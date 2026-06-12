> Fonte: PIANO-MAESTRO/02-ECOSISTEMA-INFOBUSINESS.md sez. 2.1 (Team L4) + sez. 4a (WF-CORSO step 1)

# T-MKD — Team Master Knowledge Document

> Funzione L4 · Reparto: IB-R1-PRODOTTO · Ecosistema: 02-INFO-BUSINESS
> Riferimento ecosistema: `company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md`

---

## Missione

Eseguire il **content-forge** su tutto il materiale raw dell'ecosistema: convertire
registrazioni, PDF, manuali, transcript e note grezze in un **Master Knowledge Document**
(MKD) — documento strutturato che copre il 100% degli atomi informativi della fonte,
senza perdita, pronto per essere processato da `T-curriculum`.

---

## Agente proprietario

`ib-mkd-forger` (worker, tier Sonnet)

---

## Input accettati

- Cartelle raw: `Formazzione/Claude code/`, `Formazzione/Agency Scalping/`, `Formazzione/Storytelling/`, etc.
- File singoli: `.md`, `.pdf`, `.txt`, `.mp4` (transcript), `.html`
- Brief validato da `WF-VALIDAZIONE` (score ≥60/100)

---

## Output

- `MKD-[prodotto]-[data].md` — documento strutturato con sezioni, concetti chiave, esempi, citazioni originali
- Log copertura: checklist atomi fonte vs MKD (gate: 100% copertura)

---

## Gate di uscita obbligatorio

> "MKD copre il 100% degli atomi informativi della fonte (zero perdita)"
> Verifica: confronto atomo-per-atomo tra indice fonte e sezioni MKD.
> Fail → iterazione `ib-mkd-forger` sulla sezione mancante, non riscrittura totale.

---

## Skill utilizzate

`content-forge` (skill globale) — motore primario della trasformazione.

---

## Connessioni

- [[IB-R1-PRODOTTO]] — reparto di appartenenza
- [[T-CURRICULUM]] — funzione destinataria dell'MKD
- [[WF-CORSO]] — workflow che include questa funzione come step 1
