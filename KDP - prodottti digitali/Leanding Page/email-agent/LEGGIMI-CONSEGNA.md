# Consegna automatica dopo il pagamento

Il webhook che era cablato su un solo ebook ora serve **piu' prodotti**.
Il codice non sa piu' cosa vende: lo legge da `prodotti.json`.

| File | Cosa fa |
|---|---|
| `main.py` | Riceve il webhook Stripe, riconosce il prodotto, spedisce |
| `catalogo.py` | Risoluzione prodotto + composizione email. Nessuna rete, testabile |
| `prodotti.json` | Il catalogo. **Qui non entra nessun link e nessun segreto** |
| `test_consegna.py` | Test offline, non manda email e non chiama Stripe |
| `consegne-fallite.log` | Ogni consegna non riuscita, una riga. Ignorato da git |

---

## 1. Cosa mettere nel `.env`

Parti da `.env.example`. Rispetto a prima cambia **una riga sola**:

```
MANUALE_CC_DOWNLOAD_URL=https://.../manuale-claude-code.pdf
```

Il link del PDF del Manuale sta **solo li'**. Non nel codice, non nel catalogo,
non su git. `EBOOK_DOWNLOAD_URL` resta com'era: le 48 Leggi continuano a
funzionare identiche a oggi, stesso oggetto e stesso testo.

## 2. Come si avvia

Nessun cambiamento:

```
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

In produzione ci pensa il `Procfile`. Controllo di vita: `GET /health`.

Prima di deployare, il test (gira offline, non manda niente):

```
python test_consegna.py
```

## 3. Come riconosce il prodotto

Nell'ordine, dal piu' certo al meno certo — **tutto letto dall'evento, zero
chiamate a Stripe dentro il webhook**:

1. **`metadata.prodotto`** della sessione. E' il criterio buono: si imposta una
   volta sul Payment Link in dashboard (*Metadata* -> chiave `prodotto`, valore
   `manuale-claude-code`) e da li' in poi viaggia su ogni pagamento.
2. **Id del Payment Link** (`plink_...`). E' il rail previsto dal
   `checkout.config.json` del Manuale, e Stripe lo mette nell'evento gratis.
3. **Price id**, ma solo se i `line_items` sono gia' nel payload. Non li andiamo
   a espandere: costerebbe una chiamata di rete dentro il webhook.

**L'importo pagato non e' mai un criterio.** Due prodotti possono costare uguale
(67 e 97 oggi, ma il bump e' 27 e domani cambia) e sbagliare vorrebbe dire
mandare il libro sbagliato a chi ha pagato.

### Il fallback, e la trappola da conoscere

Finche' nel catalogo **nessun** prodotto ha un `payment_link_ids` o un
`price_ids` valorizzato, esiste di fatto un solo prodotto vendibile: una
sessione senza identificatori va alle 48 Leggi (`"fallback": true`) e tutto
funziona come oggi.

**Appena arm il primo rail, il fallback si spegne da solo.** Quindi:

> Quando incolli il `plink_...` del Manuale, **incolla anche quello delle
> 48 Leggi** nella stessa passata. Altrimenti le 48 Leggi smettono di essere
> consegnate: non partiranno email sbagliate, ma non partiranno nemmeno quelle
> giuste — le trovi tutte in `consegne-fallite.log`, con dentro l'id da
> incollare per farlo funzionare.

E' voluto: meglio non consegnare che consegnare il prodotto sbagliato.
Con `FALLBACK_PRODUCT_KEY=none` nel `.env` il fallback non esiste mai.

## 4. Quando qualcosa non va

Niente si perde in silenzio. `consegne-fallite.log`, una riga per evento:

```
data | motivo | email cliente | prodotto | session id | dettaglio
```

I motivi: `PRODOTTO_NON_RICONOSCIUTO` (dettaglio = gli identificatori visti, da
incollare in `prodotti.json`), `INVIO_FALLITO` (Gmail ha detto no — Stripe
ritenta da solo perche' rispondiamo 500), `NON_PAGATO`, `EMAIL_CLIENTE_ASSENTE`.
Ogni riga basta a rifare la consegna a mano.

## 5. Aggiungere un terzo prodotto

Non si tocca il codice. Tre gesti:

1. **`prodotti.json`** — un blocco nuovo:

```json
"nome-prodotto": {
  "nome": "Nome leggibile",
  "oggetto": "Oggetto della email",
  "corpo": "Ciao {nome},\n\n...\n\n{link}\n\nMax",
  "download_env": "NOME_PRODOTTO_DOWNLOAD_URL",
  "fallback": false,
  "riconoscimento": {
    "metadata_prodotto": ["nome-prodotto"],
    "payment_link_ids": ["plink_..."],
    "price_ids": []
  }
}
```

`{nome}` e `{link}` sono gli unici due segnaposto.

2. **`.env`** — `NOME_PRODOTTO_DOWNLOAD_URL=https://...`
3. **`test_consegna.py`** — un caso in piu', poi `python test_consegna.py`.
