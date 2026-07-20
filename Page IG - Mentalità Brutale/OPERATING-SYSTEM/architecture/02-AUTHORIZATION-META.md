# AUTHORIZATION — Instagram API ufficiale (decisione 2026-07-20)

> Fonte primaria: documentazione Meta aggiornata al 30 giugno 2026. Versione API corrente rilevata: **v25.0**. La versione resta configurabile (`MB_META_API_VERSION`) per evitare hard-code irreversibile.

## Decisione

Per `@mentalita.brutale`, account posseduto/gestito direttamente, usare **Instagram API with Business Login for Instagram**:

- non richiede una Pagina Facebook collegata;
- pubblica immagini, caroselli e Reel;
- espone Insights;
- usa host `graph.instagram.com` e token Instagram User;
- per un account proprio, Standard Access è sufficiente; Advanced Access + Business Verification + App Review servono quando l'app gestisce account non posseduti/non amministrati.

Facebook Login for Business resta alternativa futura se servono hashtag search, product tagging, partnership ads o altri componenti disponibili solo su quel percorso.

## Permessi minimi core

Richiedere solo:

1. `instagram_business_basic`
2. `instagram_business_content_publish`
3. `instagram_business_manage_insights`

Aggiungere in una fase separata, solo quando esiste il relativo workflow:

- `instagram_business_manage_comments`
- `instagram_business_manage_messages`

Least privilege evita di rallentare review e riduce l'impatto di un token compromesso.

## Setup chirurgico nel Meta App Dashboard

1. Verificare che `@mentalita.brutale` sia account **Business o Creator**.
2. Creare/selezionare una Meta app di tipo **Business**.
3. Aggiungere il prodotto Instagram e scegliere **API setup with Instagram business login**.
4. Configurare Business Login e gli scope core sopra.
5. Aggiungere l'account come tester/role dell'app se in Development/Standard Access.
6. Impostare OAuth redirect URI esatto; nessuna variante di slash.
7. Generare un token test dal Dashboard oppure completare il flow OAuth.
8. Scambiare il token short-lived con long-lived (60 giorni) lato server.
9. Salvare app secret e token solo in `.env` locale/secret manager; mai in Git, screenshot o prompt.
10. Eseguire `mbctl.py doctor --online` e verificare username/account_type/user_id.
11. Completare Page Publishing Authorization e 2FA se si sceglie in futuro Facebook Login con Page collegata.

## OAuth e ciclo token

- authorization code: valido 1 ora e una sola volta;
- short-lived token: valido circa 1 ora;
- long-lived token: valido 60 giorni;
- refresh: token valido, long-lived e vecchio di almeno 24h; refresh prima della scadenza;
- se scade da oltre 60 giorni non è più rinnovabile: rifare autorizzazione.

Comandi:

```bash
cd "Page IG - Mentalità Brutale/OPERATING-SYSTEM"
cp .env.example .env               # file ignorato da Git
python runtime/scripts/mbctl.py auth-url
python runtime/scripts/mbctl.py exchange-code --code "CODICE" --write-dotenv
python runtime/scripts/mbctl.py doctor --online
python runtime/scripts/mbctl.py refresh-token --write-dotenv
```

## Variabili segrete e non segrete

| Variabile | Segreta | Uso |
|---|---:|---|
| `MB_INSTAGRAM_APP_ID` | no | OAuth client id |
| `MB_INSTAGRAM_APP_SECRET` | **sì** | exchange short→long |
| `MB_IG_ACCESS_TOKEN` | **sì** | Graph API |
| `MB_IG_USER_ID` | no | account professionale target |
| `MB_OAUTH_REDIRECT_URI` | no | redirect esatto |
| `MB_WEBHOOK_VERIFY_TOKEN` | **sì** | fase webhooks |
| `MB_PUBLIC_MEDIA_BASE_URL` | no | URL HTTPS da cui Meta scarica asset |
| `MB_PUBLIC_MEDIA_DIR` | no | cartella server/mount corrispondente |
| `MB_LIVE_PUBLISH_ENABLED` | no | interlock; deve valere `YES` |

## Media staging — vincolo critico

Meta scarica (`cURL`) i media. Quindi:

- l'URL deve essere HTTPS e pubblico durante la pubblicazione;
- una pagina Google Drive non è un URL diretto valido;
- per le immagini il formato live previsto dalla guida Meta è JPEG;
- il carosello può avere fino a 10 elementi;
- il runtime converte/copia asset locali verso un mirror pubblico configurato e usa nomi content-addressed;
- il file può essere rimosso dal mirror solo dopo publish + post-check e finestra di sicurezza.

## Rate limit

Meta limita l'account a **100 post pubblicati via API in una finestra mobile di 24 ore**; un carosello conta come un post. MB-OS impone un cap interno molto più basso (3/giorno) e interroga `/<IG_ID>/content_publishing_limit` prima di ogni side effect.

## Checklist GO-LIVE

- [ ] Account professionale e owner role verificati.
- [ ] App Business configurata; scope minimi concessi.
- [ ] Password storiche ruotate dopo la bonifica Git.
- [ ] `.env` locale presente e non tracciato.
- [ ] `doctor --online` PASS.
- [ ] URL staging HTTPS raggiungibile da Internet e JPEG preflight PASS.
- [ ] 5 dry-run PASS.
- [ ] 1 publish canary in modalità SUPERVISED.
- [ ] permalink post-check PASS.
- [ ] Insights test PASS a +48h.
- [ ] Evidence di certificazione registrata; solo allora `CERTIFIED_AUTO`.

## Fonti ufficiali

- https://developers.facebook.com/documentation/instagram-platform/overview
- https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login
- https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/business-login
- https://developers.facebook.com/documentation/instagram-platform/content-publishing
- https://developers.facebook.com/documentation/instagram-platform/insights
- https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media/insights
- https://developers.facebook.com/documentation/instagram-platform/webhooks
