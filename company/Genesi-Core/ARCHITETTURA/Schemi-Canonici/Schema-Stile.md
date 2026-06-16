# SCHEMA CANONICO — Stile

> Forma LEGGERA (knowledge layer). Regole di coerenza visiva e/o di voce per un brand/prodotto.
> Motore reale: `empire-premium-style`, brand kit, `brand-guidelines`. NON è un eseguibile.

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando serve garantire coerenza di look-and-feel o di tono di voce (palette, tipografia,
  pattern UI, do/don't di copy/brand). È un riferimento di conformità, non un processo.
- **NO se** è una verità operativa generale → **Principio**. NO se è un sistema di componenti
  costruibile con codice e pipeline → **Skill** (es. `empire-premium-style`) o **Workflow**.
- **Trattamento LEGGERO**: niente org chart/KPI. Lo stile vive come riferimento + checklist.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Ambito**: cosa copre lo stile (visivo / voce / entrambi) e per quale brand/prodotto.
2. **Token / Pattern**: i valori concreti — palette (hex), tipografia, spaziature, oppure per la
   voce: registro, lessico ammesso/vietato, lunghezza frasi, persona.
3. **Regole Do / Don't**: tabella binaria con coppie "fai questo / non quello".
4. **Esempi conformi e NON conformi**: ≥1 conforme + ≥1 violazione, affiancati.
5. **Casi limite**: dark vs light, mobile vs desktop, lungo vs breve (dove lo stile cambia).
6. **Connessioni**.

## Template vuoto (copiabile)
```markdown
# Stile — <Nome Brand/Prodotto>
## Ambito
<visivo | voce | entrambi> · per <prodotto>
## Token / Pattern
- Palette: #...  · Tipografia: ... · Spaziatura: ...
- (Voce) Registro: ... · Lessico ammesso: ... · Vietato: ...
## Do / Don't
| Fai | Non fare |
|---|---|
| ... | ... |
## Esempi
- ✅ Conforme: <snippet/descrizione>
- ❌ Non conforme: <snippet> → perché viola
## Casi limite
- Dark bg → <regola> · Mobile → <regola>
## Connessioni
```

## Checklist di completezza (per struct-gate)
- [ ] **Ambito** dichiarato (visivo/voce/entrambi + brand).
- [ ] **Token/Pattern** con valori CONCRETI (hex, font, registro) — non aggettivi vaghi.
- [ ] Tabella **Do / Don't** con ≥3 coppie binarie.
- [ ] ≥1 esempio **conforme** E ≥1 **non conforme** con il motivo della violazione.
- [ ] ≥1 **caso limite** trattato.
- [ ] **Connessioni** ≥2.
- [ ] NESSUN apparato pesante improprio (no org chart/KPI/I-O JSON).

## Esempio minimo compilato
**Stile — Digital Empire (visivo).** Ambito: visivo, siti premium. Token: palette ink #1c1c1c /
paper / orange #fb4604; tipografia Onest variabile; grana fine doppio layer fissa. Do: `card-fill-silver`
su bg dark. Don't: `card-dark` su bg dark. ✅ hero con btn-orange + glow su ink. ❌ card-dark su
#1c1c1c → si fonde, invisibile. Caso limite: mobile → corner brackets ridotti. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- Token espressi come aggettivi ("colori caldi") senza valori → non verificabile, non riproducibile.
- Solo "Do" senza "Don't" → non si riconosce la violazione.
- Nessun esempio non-conforme → la regola resta astratta.
- Confondere Stile (riferimento di conformità) con la Skill che lo applica via codice.
- Espandere uno stile in un ecosistema → spreco, contro la FORMA GIUSTA.

## Connessioni
- [[Schema-Principio]] — forma leggera sorella (regola generale, non visiva/voce)
- [[Schema-Skill]] — quando lo stile diventa un applicatore eseguibile (es. empire-premium-style)
- [[README]] — il principio: forme leggere ≠ trattamento pesante
