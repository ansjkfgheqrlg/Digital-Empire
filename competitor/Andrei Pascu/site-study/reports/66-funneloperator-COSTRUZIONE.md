---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #costruzione #stack #funneloperator
Created: 2026-09-13
Last updated: 2026-09-13
---

# 66 — funneloperator.it: COSTRUZIONE (stack, metodo, componenti, performance, tracciamento)

Rapporto del Reparto Competitor Research su **come è costruito** `https://www.funneloperator.it/`
(cattura del 2026-09-13, cartella `capture/66-funneloperator-it/`). Non è un rapporto sul copy né
sul design: è la lettura del **codice servito** — 43 file JS + 1 CSS scaricati in `src/`, la
`scheda.json`, `media-inventario.md`, `dom-blocks.json`. Ogni affermazione cita il file; il codice
è copiato così com'è dal minificato (i nomi a una lettera sono del minificatore, non di Andrei).

Contesto già acquisito (`reports/11-armageddon.md` §0): Andrei costruisce con Claude Code, un
`CLAUDE.md` numerato, un `brand.css`, un mockup PDF misurato, un ticket system `AP-`. Questo
rapporto verifica se e come quel metodo riappare nel suo sito più grosso — una **web app completa**
(landing + area membri + admin), non una landing.

---

## 0. LE CINQUE COSE DA SAPERE PRIMA DI LEGGERE

1. **Non è una landing, è un'applicazione.** 105 chunk JS nel manifest (`__vite__mapDeps`), 22 rotte
   (`/`, `/auth`, `/member/*`, `/$adminSegmento`, `/post-checkout`…), Supabase per auth e dati,
   server functions TanStack Start. La pagina di vendita è la rotta `/` di un LMS fatto in casa.
2. **Il bundle contiene, in chiaro, l'intero ambiente di build Vercel**: repo GitHub
   `AP-Sales/FunOps`, autore `andrei pascu dio del marketing`, messaggio dell'ultimo merge
   («Sicurezza a 360° del lancio: 13 difetti chiusi…»), URL Supabase e chiave publishable, ID
   Clarity. È il punto §1.7 — ed è una lezione sul cosa NON fare.
3. **Design system proprio con prefisso `fo-`, tutto in italiano**: token OKLCH `--fo-*`,
   classi `.colonna`, `.corpo`, `.titolo-sezione`, `.interfaccia`, `.codice`, `.sezione-chiara`,
   `.bottone-che-lavora`, keyframes `fo-comparsa`, `fo-momento`, `fo-foglio-su`, `fo-rail`…
   Il vocabolario è coerente dal CSS ai props React (`tono`, `come`, `larghezza`, `sorgenteStretta`).
4. **Il prezzo è un dato solo** (`Ip={ATTUALE:434,VALUTA:"EUR",PROSSIMO:{importo:560,dal:"2026-10-12"}}`)
   e da lì nascono cifra in pagina, FAQ, countdown, `priceValidUntil` del JSON-LD. Il nostro §8
   (nessun dato duplicato) qui è applicato al livello più alto che abbiamo visto.
5. **Tracciamento first-party con consenso vero**: banner scritto in italiano chiaro, `fbq`/`gtag`/
   `clarity` caricati solo dopo «Accetta» e solo sulla rotta `/`; il conteggio visite passa da una
   server function propria (`type:"visit"`, referrer, UTM) con `visitorId` opzionale in `localStorage`
   (`fo-visitatore`). Meta Pixel e GA4 sono **predisposti ma spenti** (env var assenti): oggi gira
   solo Microsoft Clarity `yh4ehu2xkk`.

---

## 1. STACK

### 1.1 Framework: React 19 + TanStack Router/Start + Vite

Prove, tutte in `src/29-index-CLKYm5hM.js` (588.728 byte, il chunk applicativo):

```js
var Lp=n.version;if(Lp!==`19.2.5`)throw Error(o(527,Lp,`19.2.5`));
```
→ React DOM **19.2.5** (controllo di versione di react-dom).

```js
TSS_DEV_SERVER:`false`,TSS_DEV_SSR_STYLES_BASEPATH:`/`,TSS_DEV_SSR_STYLES_ENABLED:`true`,
TSS_DISABLE_CSRF_MIDDLEWARE_WARNING:`false`,TSS_INLINE_CSS_ENABLED:`false`,TSS_ROUTER_BASEPATH:``,
TSS_SERVER_FN_BASE:`/_serverFn/`
```
→ variabili `TSS_*` = **TanStack Start** (Start usa il prefisso TSS). `TSS_SERVER_FN_BASE:"/_serverFn/"`
è l'endpoint delle server functions.

```js
__vite__mapDeps=(i,m=__vite__mapDeps,d=(m.f||(m.f=["assets/termini-RfDyVE4l.js", ...105 voci... ])))=>i.map(i=>d[i]);
```
→ **Vite** (il preload map dei chunk dinamici è generato da Vite). Le chiavi `BASE_URL`, `DEV`,
`MODE`, `PROD`, `SSR` inlined sono `import.meta.env` di Vite.

```js
let e=`tanstack_router_reload:${i.message}`;sessionStorage.getItem(e)||...
var Xt=`tsr-scroll-restoration-v1_3`
```
→ **TanStack Router** (stringhe letterali del router; `tsr` = TanStack Router). Il file
`src/35-route-BYPzqRIj.js` è la classe `Route` del router (`_addFileChildren`, `lazy`, `redirect`,
`useLoaderData`, `useSearch`, `useParams`), `src/31-link-DiKj2Kcl.js` è il `Link`,
`src/40-useMatch`, `src/41-useNavigate`, `src/42-useRouter` sono gli hook.

`src/43-useStore-CmuWC2Bw.js` è `@tanstack/store` (deep-merge strutturale `f(e,t,n,r)`,
`useSyncExternalStore` via `src/37-shim-DoKe8bYx.js` = `use-sync-external-store/shim`).

Stato server: **@tanstack/react-query** (`queryKey`, `queryHash`, `fetchStatus`, 24 occorrenze;
`Od.useRouteContext()` restituisce `{queryClient}` e lo passa al provider `Cu`).

Validazione: **zod** (`this.name="ZodError"`, `vendor:"zod"`; `mp=fp({session_id:dp().optional()})`
valida la search `/post-checkout?session_id=`).

Rendering: **SSR + hydration** — `e.hydrateRoot=function(e,t,n)` e `shellComponent:U` che rende
`<html lang="it"><head>…</head><body>…</body></html>` da React:

```js
function U({children:e}){return(0,O.jsxs)(`html`,{lang:`it`,children:[(0,O.jsx)(`head`,{children:(0,O.jsx)(xr,{})}),(0,O.jsxs)(`body`,{children:[e,(0,O.jsx)(Sr,{})]})]})}
```

È lo stesso stack già misurato su `apsales.eu` (`reports/13-apsales-STACK-E-TOKEN.md` §1): React +
TanStack Start + Tailwind + shadcn/Radix. Andrei ha **uno stack solo** per i siti applicativi, e
vanilla per le landing di lancio (`11-armageddon.md` §1). Le due corsie della nostra Fabbrica
(ADR-023) sono la stessa scelta, fatta da lui prima.

### 1.2 UI kit: shadcn/ui sopra Radix, icone Lucide

- `src/02-accordion-BvtD-mDo.js`: Radix Accordion (`AccordionHeader`, `AccordionTrigger`, `--radix-accordion-content-height`) avvolto in shadcn con classi **sue**:
  ```js
  Z=g.forwardRef(({className:e,...t},n)=>(0,_.jsx)(he,{ref:n,className:i(`border-b border-fo-line`,e),...t}));
  Q=g.forwardRef(({className:e,children:t,chevron:n=!0,...r},a)=> ... `interfaccia text-fo-muted transition-colors`,`hover:text-fo-text data-[state=open]:text-fo-text`
  $=...`overflow-hidden corpo text-fo-muted data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down`,n.forceMount&&`data-[state=closed]:hidden`
  ```
  Nota il prop **`chevron`** aggiunto da lui (per sostituire la freccia con il «+» che ruota di 45°) e
  la gestione di `forceMount` (contenuto FAQ sempre nel DOM → indicizzabile).
- `src/12-dialog-PqngB_cI.js`: Radix Dialog + shadcn; overlay `bg-fo-velo`, contenuto
  `comparsa scheda-alta … max-w-(--finestra) gap-scheda-riga`, bottone chiudi con `aria-label:"Chiudi"`.
- `src/28-dropdown-menu-COwaHBxh.js`: Radix DropdownMenu (menu account nell'header).
- `src/03-avatar-JcsTr3Jb.js`: Radix Avatar (iniziali utente nel menu account).
- `src/01-Combination-8XuMgjkz.js`: `react-remove-scroll` (`[data-radix-focus-guard]`, importa `tslib`).
- `src/19-dist-BtDRIp4A.js`: `@floating-ui` (41 occorrenze di `floating`) usato da Radix Popper.
- `src/13..27-dist-*.js`: primitive Radix (Slot, Presence, Portal, Primitive, Collection, Direction…).
- `src/10-createLucideIcon-CLQ5Hlf7.js`, `06-check`, `07-chevron-right`, `08-circle`: **lucide-react**,
  un chunk per icona (tree-shaking spinto al singolo SVG).
- `src/09-clsx` + `src/44-utils-BC4DHlz2.js` (26 KB = **tailwind-merge**): il classico `cn()` di shadcn.
- `src/04-button-rHPgEXhH.js`: **class-variance-authority** riscritto inline (`u=(e,t)=>n=>{…variants…compoundVariants…}`) con varianti sue:
  ```js
  variants:{variant:{default:`bg-fo-action text-fo-on-action hover:bg-fo-action-hover active:bg-fo-action-press`,
  outline:`bg-fo-surface text-fo-text border-fo-line hover:bg-fo-elevated`,
  ghost:`text-fo-muted hover:bg-fo-surface hover:text-fo-text`,
  "ghost-bordo":`bg-transparent text-fo-text border-fo-text hover:bg-fo-elevated`,
  destructive:`bg-fo-error-solid text-fo-text hover:bg-fo-error-solid-hover`,
  link:`collegamento h-auto border-0 p-0`},
  size:{sm:`h-8 px-4`,default:`h-10 px-5`,lg:`h-12 px-6`,"icon-sm":`size-8 p-0`,icon:`size-10 p-0`,"icon-lg":`size-12 p-0`}}
  ```
  Una variante si chiama **`ghost-bordo`** — inglese e italiano nella stessa chiave: il kit shadcn è
  stato piegato al suo vocabolario, non sostituito.

### 1.3 CSS: Tailwind v4.2.4 + tema OKLCH + strato di classi italiane

`src/38-styles-Cm6i-gBj.css` (148.072 byte) apre con:
```css
/*! tailwindcss v4.2.4 | MIT License | https://tailwindcss.com */
@layer properties{…}
```
Tailwind **v4** (motore Oxide: `@layer properties`, `@property --tw-*`, `color-mix(in oklab …)`
per le opacità `/45`, `/95`). Il tema è nel blocco `:root,:host{…}` (posizione 2539):

```css
--font-sans:"Inter Tight", "Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
--font-display:"Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
--font-lapide:"Curseyt", "Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
--text-base:1.0625rem;--text-base--line-height:1.6;--text-lg:1.375rem;--text-lg--line-height:1.4;
--default-transition-duration:var(--moto-stato);
```
Il corpo del testo è **17px** (`1.0625rem`), non 16: scelta deliberata, coerente con la `.corpo`.

I 90 valori `oklch(...)` sono tutti nel blocco `:root` a posizione 136716 (palette `--fo-*`,
riportata in §2.2). Sopra ci sono anche i token shadcn di default (`--background`, `--card`,
`--sidebar-*`, `--chart-1..5`) **ricablati** ai suoi: `--ring:var(--fo-focus)`,
`--sidebar:var(--fo-surface)`. Lo scaffold shadcn è rimasto, ma punta al design system `fo`.

### 1.4 Font: self-hosted, subset latin/latin-ext, preload dei due principali

13 `@font-face` in `src/38-styles-Cm6i-gBj.css`, tutte da `/caratteri/*.woff2` (stesso dominio,
nessuna richiesta a Google Fonts):

```css
@font-face{font-family:Curseyt;src:url(/caratteri/curseyt.woff2)format("woff2");font-weight:400;font-style:normal;font-display:block}
@font-face{font-family:Inter Tight;font-style:normal;font-weight:400 700;font-display:swap;src:url(/caratteri/inter-tight-400-700-normal-latin.woff2)format("woff2");unicode-range:U+??,U+131,…}
@font-face{font-family:Plus Jakarta Sans;font-style:normal;font-weight:200 800;font-display:swap;src:url(/caratteri/plus-jakarta-sans-200-800-normal-latin.woff2)format("woff2");…}
@font-face{font-family:DM Mono;…font-weight:400;…src:url(/caratteri/dm-mono-400-normal-latin.woff2)…}
```

- **Variable font** (`font-weight:400 700`, `200 800`) → un file per famiglia/stile invece di uno per peso.
- **Split latin / latin-ext** con `unicode-range` → il browser scarica latin-ext solo se serve.
- **`font-display:block` solo su Curseyt**, il carattere del titolo «Un giorno morirai.» (classe
  `.lapide-uno`): per il display font accetta il FOIT per non far vedere il fallback; per i testi usa `swap`.
- Nel root route (`index` pos. 507432) preload dei due file critici:
  ```js
  {rel:`preload`,href:`/caratteri/inter-tight-400-700-normal-latin.woff2`,as:`font`,type:`font/woff2`,crossOrigin:`anonymous`},
  {rel:`preload`,href:`/caratteri/plus-jakarta-sans-200-800-normal-latin.woff2`,as:`font`,type:`font/woff2`,crossOrigin:`anonymous`}
  ```
  Curseyt e DM Mono **non** sono preloaded (sono sotto la piega / secondari).

### 1.5 Hosting: Vercel, repo GitHub `AP-Sales/FunOps`

Il blocco `import.meta.env` è stato inlined **quattro volte** nel bundle (posizioni 456616, 489109,
490913, 492722), e con lui tutte le variabili `VITE_VERCEL_*` che Vercel espone al build:

```js
VITE_VERCEL_BRANCH_URL:`fun-ops-git-main-ap-sales.vercel.app`,
VITE_VERCEL_DEPLOYMENT_ID:`dpl_ESZi11fYSeYEQVwCT8q8iG5GJNhR`,
VITE_VERCEL_ENV:`production`,
VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN:`andrei-bsns`,
VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME:`andrei pascu dio del marketing`,
VITE_VERCEL_GIT_COMMIT_MESSAGE:`Merge pull request #132 from AP-Sales/develop

Sicurezza a 360° del lancio: 13 difetti chiusi, avviso «quirks», pulizia utenti di prova`,
VITE_VERCEL_GIT_COMMIT_REF:`main`,
VITE_VERCEL_GIT_COMMIT_SHA:`51c300f08ceed939daecf1364ce83036c7d5ac9b`,
VITE_VERCEL_GIT_PROVIDER:`github`,
VITE_VERCEL_GIT_REPO_ID:`1312923994`,
VITE_VERCEL_GIT_REPO_OWNER:`AP-Sales`,
VITE_VERCEL_GIT_REPO_SLUG:`FunOps`,
VITE_VERCEL_PROJECT_ID:`prj_ADYjjuqo0JKBV1fRzjg08kbikVt8`,
VITE_VERCEL_PROJECT_PRODUCTION_URL:`www.funneloperator.it`,
VITE_VERCEL_URL:`fun-aah7fi2rv-ap-sales.vercel.app`
```

Cosa dice: hosting **Vercel** (team `ap-sales`, progetto `fun-ops`), repo **GitHub privato
`AP-Sales/FunOps`**, flusso **`develop` → PR → `main`** (PR numero 132: almeno 132 PR/issue sul repo),
messaggi di commit **in italiano**, e un conteggio esplicito di difetti («13 difetti chiusi»): il
ticket system `AP-138` visto su armageddon qui non compare come stringa, ma la pratica di contare i
difetti chiusi per release è la stessa. La riga `VITE_VERCEL_OBSERVABILITY_CLIENT_CONFIG` con
`analytics` e `speedInsights` dice che **Vercel Analytics e Speed Insights sono attivi sul progetto**
(lo script client però non è nel bundle: la raccolta vitals passa dall'iniezione Vercel a runtime).

Asset statici da path relativi allo stesso dominio: `/assets/*.js|css` (build Vite con hash),
`/vendita/*.webp` (immagini della pagina di vendita), `/marchi/*` (loghi), `/caratteri/*.woff2`,
`/immagini/anteprima-social.png`. **Nessun CDN esterno** per font, immagini o script (a parte i tag
di misurazione dopo consenso).

### 1.6 Backend: Supabase (auth + dati + realtime) via server functions

```js
VITE_SUPABASE_PROJECT_ID:`qnyftuszypcxsqtnrgcz`,
VITE_SUPABASE_PUBLISHABLE_KEY:`sb_publishable_gs-_B1MfSmh7cRBmFaeocQ_vdSOMP9D`,
VITE_SUPABASE_URL:`https://qnyftuszypcxsqtnrgcz.supabase.co`
```
Il client `supabase-js` è nel bundle (76 occorrenze; `realtime-js/2.112.3`, `storage-js/2.112.3`,
`GoTrueClient`). La rotta protetta lo usa direttamente:

```js
Fp=qn(`/_authenticated`)({beforeLoad:async()=>{let{data:e,error:t}=await Cl.auth.getUser();if(t||!e.user)throw a({to:`/auth`,replace:!0});let n;try{n=await jp()}catch{throw a({to:`/`,replace:!0})}if(n.secondoFattore===`richiesto`){…throw a({to:`/auth`,replace:!0,…})}return{user:e.user,passwordDaImpostare:n.passwordDaImpostare,hasAccess:n.hasAccess}}
```
→ `beforeLoad` controlla sessione Supabase, poi chiama la server function `jp` (con middleware
`Ap=wr({type:"function"})`) che restituisce `secondoFattore`, `passwordDaImpostare`, `hasAccess`.
C'è **un secondo fattore** e la chiusura sessione per `cambio-password` / `altro-dispositivo`
(session guard: chunk `session-guard-Cdm10FCQ.js`, `security.functions-C7eDRZLf.js` nel manifest).

### 1.7 Il difetto: il bundle espone l'ambiente

La chiave `sb_publishable_*` è pubblica per progetto (è l'anon key), quindi **non è un leak di
segreti**. Ma il bundle espone: URL del progetto Supabase, nome del repo, autore, ultimo messaggio
di commit, ID deployment e progetto Vercel, ID Clarity. È il risultato di aver scritto
`import.meta.env.VITE_X` in più punti e di un bundler che sostituisce l'intero oggetto invece della
singola chiave (probabilmente `import.meta.env` usato come oggetto: `{…}.VITE_META_PIXEL_ID`).
Lezione per noi: **mai leggere `import.meta.env`/`process.env` come oggetto intero nel codice
client**; una chiave per volta e solo quelle `NEXT_PUBLIC_*` strettamente necessarie.

### 1.8 Pagamenti: `buy-button` → server function → redirect a checkout esterno

`src/05-buy-button-DX_4IxaR.js` (655 byte, integrale):

```js
import{i as e,t}from"./jsx-runtime-DUAcabCT.js";import{t as n}from"./react-6OGjdfot.js";import{m as r}from"./index-CLKYm5hM.js";var i=e(n(),1),a=t();
function o({className:e,children:t=`Acquista il corso`}){let[n,o]=(0,i.useState)(!1),[s,c]=(0,i.useState)(null);
return(0,a.jsxs)(a.Fragment,{children:[(0,a.jsx)(`button`,{type:`button`,disabled:n,className:e,
onClick:async()=>{o(!0),c(null);try{let{url:e}=await r();window.location.href=e}catch{c(`Non riesco ad aprire il pagamento. Riprova fra un momento.`),o(!1)}},
children:n?`Apro il pagamento…`:t}),
s?(0,a.jsx)(`p`,{className:`mt-2 text-xs text-red-400`,role:`alert`,children:s}):null]})}export{o as t};
```

`r` è l'export `m` di `index` = `Mp`:
```js
Mp=p({method:`POST`}).handler(l(`60c7dcfe1450e2743599df1a67d997fda9aaa14b69e96323aa59d2c2b482d820`))
```
→ una **server function POST** (`createServerFn({method:"POST"}).handler(<hash>)`) il cui corpo vive
solo sul server; il client riceve `{url}` e fa `window.location.href=url`. Il provider di pagamento
**non è nel bundle** — la sessione viene creata lato server. Indizi convergenti su **Stripe Checkout**:
la rotta di ritorno valida `session_id` (`mp=fp({session_id:dp().optional()})` su `/post-checkout`),
che è il parametro standard `?session_id={CHECKOUT_SESSION_ID}` di Stripe; la FAQ dice «fino a 3 rate,
tramite Klarna o PayPal. Clicca il pulsante per comprare e al checkout scegli Klarna oppure PayPal»
(Klarna e PayPal sono metodi Stripe Checkout). Non è dimostrato al 100%: il nome «Stripe» non compare.

Tre stati UI in 655 byte: bottone normale → «Apro il pagamento…» disabilitato → errore in
`role="alert"` con retry. È il pattern minimo corretto per un bottone che parla con un server.

### 1.9 Server functions: quante e per cosa

Tutte con la firma `p({method}).handler(l("<sha256>"))` in `src/29-index-CLKYm5hM.js`:

| var | metodo | uso dedotto dal chiamante |
|---|---|---|
| `Eu` | POST | evento analytics `{type,path,email,lessonCode,referrer,utm*,isLanding,visitorId}` (`Tu=["visit","login","password_reset","lesson_completed"]`) |
| `Du` | GET | lettura lato consenso/analytics |
| `Ad` | GET | loader pagine legali: `loader:()=>Ad({data:{pagina:"cookie"}})` |
| `Zp` | GET | **loader della home** `em=qn("/")({loader:()=>Zp()})` → programma del corso per il `raccoglitore` |
| `Mp` | POST | **checkout** (buy-button) |
| `Tp` | POST | validazione segmento admin: `if(!(await Tp({data:{segmento:e.adminSegmento}})).valido)throw c()` |
| `jp` | GET + middleware | stato sessione/2FA per `/_authenticated` |
| `Cp`,`wp`,`Ep`,`Np`,`Pp`,`Dp`,`Op` | POST/GET | account, password, email (chunk `profile.functions`, `password-reset.functions`, `assistenza.functions`, `content-requests.functions`) |

Il client (`src/11-createServerFn-Dnzfrwdq.js`) chiama `/_serverFn/<id>` con header
`x-tsr-serverFn:true`, payload serializzato (seroval) e protocollo framed
`application/x-tss-framed`:
```js
function Kr(e){let t=`/_serverFn/`+e;return Object.assign((...e)=>{let n=l()?.serverFns?.fetch;return Br(t,e,n??fetch)},{url:t,serverFnMeta:{id:e},[n]:!0})}
…s.set(`x-tsr-serverFn`,`true`),o===`payload`&&s.set(`accept`,`${i}, application/x-ndjson, application/json`)
```

### 1.10 Routing: 22 rotte, una sola pubblica indicizzabile

Dall'albero `.update({id,path})` in `index` (pos. 585325 e seguenti) e dai `qn("/…")`:

```
/                              landing (component: routes-DT2uV_Ni.js, loader Zp)
/auth                          login  (noindex)
/assistenza                    supporto
/post-checkout?session_id=     ritorno pagamento (noindex)
/conferma-email  /annulla-cambio-email  /reset-password   (noindex)
/privacy  /termini  /cookie    pagine legali (loader Ad, chunk pagina-legale)
/cantiere                      pagina "cantiere" (staging visivo di componenti: importa select, checkbox, tooltip, sheet, skeleton…)
/$adminSegmento                admin con segmento segreto validato server-side, title "GoofyWorld666", noindex/noarchive/nosnippet
/_authenticated                layout protetto (beforeLoad Supabase)
  /member/                     lezioni
  /member/dashboard  /member/account  /member/extra-content
  /member/category/  /member/category/$categorySlug
  /member/lezione/$codice
  /member/promotion  /member/pre-promotion  /member/pre-consulenza
```

`Sd=new Set(["/","/auth","/assistenza","/post-checkout","/conferma-email","/annulla-cambio-email","/reset-password","/privacy","/termini","/cookie"])`
è l'insieme delle rotte che usano il **guscio pubblico** (header + footer + banner consenso); le
`/member/*` hanno un guscio diverso. Il layout pubblico:

```js
function xd({children:e,account:t}){let{bannerAperto:n}=qu();return(0,O.jsxs)(`div`,{className:`flex min-h-screen flex-col bg-fo-bg text-fo-text`,style:n?{paddingBottom:`var(--fo-banner-altezza, 16rem)`}:void 0,children:[(0,O.jsx)(vd,{account:t}),(0,O.jsx)(`div`,{className:`flex flex-1 flex-col [&>main]:min-h-0 [&>main]:flex-1`,children:e}),(0,O.jsx)(bd,{}),(0,O.jsx)(dd,{})]})}
```
→ quando il banner cookie è aperto, il layout aggiunge `padding-bottom:var(--fo-banner-altezza)`,
misurata con `ResizeObserver` sul banner stesso: **il banner non copre mai il footer**.

Code splitting: la home carica 43 JS su 105; ogni rotta è `import()` lazy con `__vite__mapDeps`;
Radix/lucide sono spezzati per primitiva. Il rovescio: **il chunk `index` da 589 KB** contiene
React DOM, TanStack Router/Start, react-query, zod, supabase-js intero (auth+realtime+storage) e
tutte le definizioni di rotta — anche per chi vede solo la landing.

---

## 2. IL METODO DI COSTRUZIONE

### 2.1 Tracce di Claude Code / CLAUDE.md / ticket

Grep su tutti i 44 file di `src/` per `/*`, `//`, `AP-`, `TODO`, `CLAUDE`, `§`, `regola`:

- **Commenti nel CSS**: due soli, entrambi non suoi (`/* fonte: … */` aggiunto dal nostro strumento di
  cattura e `/*! tailwindcss v4.2.4 */`). Tailwind v4 in produzione **cancella i commenti**: se il
  sorgente aveva note come su armageddon, qui non possono sopravvivere. Assenza di prova, non prova di assenza.
- **Commenti nel JS**: zero (minificatore). `AP-` compare 10 volte, sempre come `AP-Sales` (owner del
  repo) — **nessun ticket `AP-nnn`** in questo bundle.
- `regola` compare 1 volta in `routes`, nel copy («Rispetta quelle due regole e la call è tua»).
- `§` e `CLAUDE`: zero.

Le tracce del metodo stanno **altrove**, e sono più forti dei commenti:

1. Il messaggio di merge inlined (§1.5): «Sicurezza a 360° del lancio: **13 difetti chiusi**, avviso
   «quirks», pulizia utenti di prova» — release note in italiano, conteggio difetti, PR #132.
2. **Placeholder dichiarati nel codice**: `src/32-raccoglitore-Bj4iyfd5.js` spedisce dati finti con
   scritto che sono finti:
   ```js
   c=[{numero:`01`,nome:`Introduzione`,linguetta:`3.9%`,larghezza:`26.51%`,sommario:`Testo finto di prova — questa riga non è il corso.`,lezioni:[`Lezione finta — la prima`,`Lezione finta — la seconda`,`Lezione finta — una cosa lunga che va a capo perché serve vedere cosa succede quando va a capo`,`Lezione finta — la quarta`]}, …]
   ```
   «una cosa lunga che va a capo perché serve vedere cosa succede quando va a capo» è una **frase di
   test scritta in italiano da chi progetta il componente** (o dall'agente per lui): il componente è
   nato prima del contenuto, con dati di prova che descrivono il proprio scopo. In produzione i dati
   veri arrivano dal loader (`v(r("/").useLoaderData())` in `routes`) e il DOM catturato mostra
   «01 Intro / 02 Landing pages / 03 Trovare clienti / 04 Domande comuni» (`scheda.json` → `cta[2..5]`).
3. **Sezioni vuote spedite in produzione**: in `routes` ci sono tre array vuoti con la sezione già
   costruita che si spegne da sola:
   ```js
   var G=[];function Ee(){return G.length===0?null:(0,C.jsxs)(w,{tono:`scuro`,children:[(0,C.jsx)(T,{children:`Guardiamo i numeri`}),…
   var Y=[],X=[];function We(){return Y.length===0?null:… `Ecco come altri hanno trovato clienti grazie a noi` …
   function Ge(){return X.length===0?null:… `Funnel Operator: lista completa dei contenuti` …
   ```
   Testimonianze, numeri e lista contenuti sono **slot predisposti** per quando i dati arriveranno.
   La pagina è stata costruita a struttura completa e riempita per gradi.
4. **Video «da girare»**: il componente VSL ha un ramo esplicito per il video non ancora esistente:
   ```js
   t?null:(0,C.jsxs)(`span`,{className:`absolute bottom-3 left-4 codice text-fo-muted`,children:[e,` — da girare`]})
   ```
   Se `video` è undefined mostra «VSL 1 — da girare» in DM Mono. Oggi entrambi i video esistono
   (`S={principale:{sorgente:x("1226141162")…},consulenza:{sorgente:x("1226166880")…}}`), il ramo è
   rimasto: il codice **porta con sé la propria storia di produzione**.
5. La rotta **`/cantiere`** (chunk `cantiere-B8rNx0zW.js`, importa select/checkbox/tooltip/sheet/
   skeleton/badge/ResponsiveContainer): una pagina di **prova dei componenti** lasciata online, senza
   `head` (nessun title), non linkata. È il suo Storybook povero.
6. Convenzioni **uniformi dal CSS ai props**: `tono:"chiaro"|"scuro"`, `come:"h3"`, `larghezza/altezza`,
   `priorita`, `sorgenteStretta`, `fino:767`, `classNameGuscio`, `etichetta`, `voci`, `domanda/risposta`,
   `bannerAperto`, `identificativoSalvato`, `motivoChiusura`, `secondoFattore`, `passwordDaImpostare`.
   Nomi così coerenti su 105 chunk non escono da un team che improvvisa: escono da **una legge scritta
   che impone l'italiano nei nomi** (lo stesso CLAUDE.md numerato di armageddon, qui non citato ma agito).

### 2.2 Il design system `fo-`: token

Blocco `:root` in `src/38-styles-Cm6i-gBj.css` (pos. 136716), copiato:

```css
--fo-bg:oklch(17.8% 0 89.9);--fo-surface:oklch(22% 0 89.9);--fo-elevated:oklch(25.1% 0 89.9);
--fo-line:oklch(29.3% 0 89.9);--fo-line-forte:oklch(39.1% 0 89.9);
--fo-text:oklch(93.4% 0 89.9);--fo-muted:oklch(63.3% 0 89.9);
--fo-blue:oklch(65.6% .134 235.9);--fo-blue-hover:oklch(54.6% .143 246.7);--fo-blue-deep:oklch(45.9% .121 247.3);--fo-blue-light:oklch(80.8% .09 238.3);
--fo-chiaro-fondo:oklch(94.6% 0 89.9);--fo-chiaro-testo:oklch(17.8% 0 89.9);--fo-chiaro-muto:oklch(47.3% 0 89.9);--fo-chiaro-riga:oklch(87% 0 89.9);--fo-chiaro-superficie:oklch(100% 0 89.9);
--fo-chiaro-verde:oklch(59.8% .199 143.2);--fo-chiaro-blu:oklch(61% .14 240.1);--fo-chiaro-riga-foto:oklch(80.6% 0 89.9);--fo-chiaro-nero:oklch(0% 0 0);--fo-chiaro-testo-alzato:oklch(22% 0 89.9);--fo-chiaro-riga-scura:oklch(51.4% 0 89.9);
--fo-action:var(--fo-blue);--fo-action-hover:var(--fo-blue-light);--fo-action-press:var(--fo-blue-hover);--fo-on-action:var(--fo-bg);
--fo-link:var(--fo-blue);--fo-link-hover:var(--fo-blue-light);--fo-focus:var(--fo-blue-light);--fo-selected:var(--fo-blue-deep);
--fo-velo:oklch(17.8% 0 89.9/.72);
--fo-success-text:oklch(78% .15 155);--fo-success-line:oklch(60% .13 155);--fo-success-surface:oklch(24.5% .045 155);
--fo-warning-text:oklch(84% .145 85);--fo-warning-line:oklch(66% .13 85);--fo-warning-surface:oklch(25% .045 85);
--fo-error-text:oklch(72% .16 25);--fo-error-line:oklch(58% .19 25);--fo-error-surface:oklch(24.5% .06 25);--fo-error-solid:oklch(52% .21 27);--fo-error-solid-hover:oklch(46% .21 27);
--fo-info-text:var(--fo-blue-light);--fo-info-line:var(--fo-blue-hover);--fo-info-surface:oklch(25% .05 240);
--spento-fondo:var(--fo-surface);--spento-testo:var(--fo-muted);--riga-passaggio:var(--fo-elevated);
--spazio-blocchi:clamp(32px, 7.5vw, 48px);--spazio-sezioni:clamp(40px, 10vw, 64px);--spazio-vendita:clamp(56px, 15vw, 96px);--spazio-area:clamp(64px, 17.5vw, 112px);
--scheda-dentro:16px;--scheda-riga:8px;--colonna:832px;--modulo:400px;--finestra:520px;--barra:256px;--margine-pagina:24px;
--griglia-colonne:12;--griglia-colonna:40px;--griglia-canale:32px;
--bottone-minimo:7.5rem;--sagoma-luce:oklch(28.8% 0 89.9);--piede-campo:1.125rem;
--moto-stato:.12s;--moto-comparsa:.16s;--moto-momento:.32s;--moto-battuta:90ms;--curva:cubic-bezier(.2, 0, 0, 1)
```

Lettura:
- **Tutti i grigi hanno hue 89.9 e croma 0**: neutri puri in OKLCH, scala L = 17.8 / 22 / 25.1 / 29.3 / 39.1 / 63.3 / 93.4. Il tema chiaro è la stessa scala rovesciata (94.6 / 87 / 47.3 / 17.8).
- **Due livelli semantici**: primitive (`--fo-blue`, `--fo-blue-light`) e ruoli (`--fo-action`, `--fo-link`, `--fo-focus`, `--fo-selected`, `--fo-on-action`). Il bottone usa il ruolo, mai la primitiva.
- **Quattro stati semantici** (success/warning/error/info) ciascuno con `text / line / surface` (+ `solid` per l'errore).
- **Quattro spazi** con `clamp(px, vw, px)`: `blocchi < sezioni < vendita < area`. La pagina di vendita usa `--spazio-vendita` (`.py-vendita{padding-block:var(--spazio-vendita)}`) per ogni sezione.
- **Una colonna** `--colonna:832px` + `--margine-pagina:24px` → `.colonna{max-width:calc(var(--colonna) + var(--margine-pagina) * 2);padding-inline:var(--margine-pagina)}`. Tutte le sezioni della landing sono `<div class="colonna">`. Molti `basis-[calc(100%*428/832)]` in `routes`: **le larghezze sono frazioni della colonna 832**, come il `--u` di armageddon (che era frazione del mockup 826.46) — stesso metodo, numero diverso.
- **Quattro tempi** (`--moto-stato .12s`, `--moto-comparsa .16s`, `--moto-momento .32s`, `--moto-battuta 90ms`) e **una curva** (`cubic-bezier(.2,0,0,1)`, la "standard" Material) → `--default-transition-duration:var(--moto-stato)` rende ogni `transition-*` Tailwind da 120 ms senza scriverlo.

### 2.3 Il design system `fo-`: classi di testo e componenti (con cosa fa ciascuna)

Definizioni copiate da `src/38-styles-Cm6i-gBj.css`:

| classe | definizione | ruolo |
|---|---|---|
| `.corpo` | `font-family:Inter Tight…;font-size:1.0625rem;line-height:1.6;letter-spacing:.025em;font-weight:400` | paragrafo (17px) |
| `.interfaccia` | `font-size:.875rem;line-height:1.5;letter-spacing:.03em;font-weight:500` (Inter Tight) | testo UI: bottoni, header, footer |
| `.codice` | `font-family:DM Mono…;font-size:.875rem;letter-spacing:.03em` | etichette mono («FUNNEL OPERATOR», «giorni», «VSL 1 — da girare») |
| `.didascalia` | `font-size:.75rem;letter-spacing:.035em` | disclaimer FAQ |
| `.titolo-sezione` | `Plus Jakarta Sans;font-size:2.3125rem;line-height:1.2;letter-spacing:-.015em;font-weight:700` | h2 (37px) |
| `.titolo-blocco` | `font-size:1.375rem;line-height:1.4;letter-spacing:-.005em;font-weight:600` | h3 / titolo di card (22px) |
| `.titolo-gancio` | `letter-spacing:-.0376em;font-size:clamp(1.375rem,1.0361rem + 1.3487vw,2.25rem);font-weight:500;line-height:1.003` | le tre righe «Le aziende le vogliono.» |
| `.titolo-garanzia` | `letter-spacing:-.035em;font-size:clamp(1.6875rem,1.4454rem + .9634vw,2.3125rem);font-weight:500;line-height:1.003` | blocco garanzia |
| `.titolo-offerta` | `letter-spacing:-.06em;font-size:clamp(3.125rem,4.252rem - 1.2524vw,3.9375rem);font-weight:800;line-height:1.003` | «FUNNEL OPERATOR» nell'offerta (nota: **cresce al diminuire dello schermo**, coefficiente vw negativo) |
| `.titolo-chiusura` | `font-size:clamp(1.6875rem,1.155rem + 2.1195vw,3.0625rem);font-weight:700` | «cambiare vita» |
| `.titolo-gaia` | `font-weight:700;line-height:1.003;letter-spacing:-.036em!important` | h2/h3 della sezione «La realtà dei fatti?» (nome proprio: "gaia") |
| `.etichetta-confronto` | `font-size:2.0625rem;font-weight:700;letter-spacing:-.03em` | «Fare landing pages.» accanto al barrato |
| `.lapide-uno` / `.lapide-due` | `font-family:var(--font-lapide);font-size:min(29.85vw,220px)` / `min(29.85vw,290px);line-height:.67` | h1 «Un giorno morirai.» in Curseyt |
| `.collegamento` | `color:var(--fo-link);text-underline-offset:3px;text-decoration:underline;text-decoration-thickness:1px;transition:color var(--moto-stato) var(--curva)` | link nel testo |
| `.collegamento-solo` | `display:inline-flex;gap:.375rem;text-decoration:none;color:var(--fo-link)` | link nudo («Accedi →») |
| `.colonna` | vedi §2.2 | contenitore 832 |
| `.sezione-chiara` | ridefinisce `--fo-bg/--fo-text/--fo-muted/--fo-line/--fo-surface/--fo-elevated/--fo-link` con i valori `--fo-chiaro-*` | **tema chiaro per sezione** senza cambiare una classe figlia |
| `.scheda` | `border-radius:var(--radius);border:1px solid var(--fo-line);background:var(--fo-surface);padding:var(--scheda-dentro)` | card |
| `.bottone-che-lavora` | `min-width:var(--bottone-minimo)` (7.5rem) | il bottone che **cambia testo** («Apro il pagamento…») non deve saltare di larghezza |
| `.filo-sfumato` | `background-image:linear-gradient(90deg,#fff0,#ffffff7e 50.4808%,#fff0);height:1px` | separatore che sfuma ai lati |
| `.sagoma` | `background:linear-gradient(90deg,var(--fo-elevated),var(--sagoma-luce) 50%,var(--fo-elevated));background-size:200% 100%;animation:1.4s linear infinite fo-luccichio` | skeleton (area membri) |
| `.comparsa` | `animation:fo-comparsa var(--moto-comparsa) var(--curva)` | ingresso dialog |
| `.battuta` | `animation:fo-momento var(--moto-momento) var(--curva) both;animation-delay:calc(var(--battuta,0) * var(--moto-battuta))` | ingresso a cascata, indice via `--battuta` |
| `.girandola` | `border:2px solid;border-right-color:#0000;border-radius:9999px;width:.875rem;animation:.7s linear infinite fo-gira` | spinner |
| `.fo-rail` / `.fo-rail-track` | `will-change:transform;animation:70s linear infinite fo-rail` / `.fo-rail-track:hover .fo-rail{animation-play-state:paused}` | marquee infinito che si ferma al passaggio del mouse |
| `.fo-grain:after` | `opacity:.045;background-image:url("data:image/svg+xml,…feTurbulence baseFrequency='0.85' numOctaves='3'…");position:fixed;inset:0;z-index:50;pointer-events:none` | **grana** SVG inline (non usata nella landing: 0 occorrenze nel DOM; è nel CSS per l'area membri) |
| `.lezione …` | tipografia per il contenuto delle lezioni (`.lezione h2`, `.lezione li::marker{color:var(--fo-blue)}`, `.lezione blockquote`) | prosa dell'LMS |

Keyframes (tutti in CSS, pos. ~139700):
```css
@keyframes fo-comparsa{0%{opacity:0;transform:translateY(4px)}}
@keyframes fo-momento{0%{opacity:0;transform:translateY(8px)}}
@keyframes fo-foglio-su{0%{transform:translateY(0)}10%{transform:translateY(-2.2px)}20%{transform:translateY(-4.1px)}30%{transform:translateY(-5.6px)}40%{transform:translateY(-6.6px)}50%{transform:translateY(-7px)}60%{transform:translateY(-6.9px)}70%{transform:translateY(-6.4px)}80%{transform:translateY(-5.8px)}90%{transform:translateY(-5.3px)}to{transform:translateY(-5px)}}
@keyframes fo-gira{to{transform:rotate(360deg)}}
@keyframes fo-luccichio{to{background-position:-200% 0}}
@keyframes fo-rail{0%{transform:translate(0)}to{transform:translate(-50%)}}
@keyframes fo-dissolvenza{0%{opacity:0}}
```
`fo-foglio-su` è una curva **campionata a mano a 10 passi** (sale a -7px, rimbalza a -5px): un
overshoot scritto per punti invece che con `cubic-bezier` — il foglio del raccoglitore si "solleva"
al passaggio del mouse.

Cosa dice tutto questo del processo: un **design system nominato in italiano, con prefisso di
prodotto `fo-`**, tre livelli (token → ruoli → classi di composizione), e la scelta di tenere
**dentro Tailwind** le utility e **fuori** le classi che portano significato (`.corpo`, `.colonna`,
`.sezione-chiara`). È la stessa struttura del nostro `canone.css` + `.vivo` scopato, con un
vocabolario più stretto e un solo autore.

### 2.4 Il modello di sezione

Tutta la landing (`src/36-routes-DT2uV_Ni.js`) è composta da tre primitive:

```js
function w({tono:e,children:t,className:n=``,ariaLabel:r,id:i}){return(0,C.jsx)(`section`,{id:i,"aria-label":r,className:`${e===`chiaro`?`sezione-chiara`:`bg-fo-bg text-fo-text`} py-vendita ${n}`,children:(0,C.jsx)(`div`,{className:`colonna`,children:t})})}
function T({children:e,className:t=``,come:n=`h2`}){return(0,C.jsx)(n,{className:`titolo-sezione text-balance ${t}`,children:e})}
function E({children:e,className:t=``}){return(0,C.jsx)(`p`,{className:`corpo text-fo-text ${t}`,children:e})}
```
`w` = Sezione (con `tono`), `T` = Titolo (con `come` per il livello), `E` = Paragrafo. Trenta sezioni,
tre componenti. Le 30 `<section>` della `scheda.json` alternano `sezione-chiara.py-vendita` e
`bg-fo-bg.text-fo-text.py-vendita`: la **alternanza chiaro/scuro è un prop**, non una classe scritta
30 volte. La composizione finale è esplicita:

```js
function me(){…[se,le,ue,fe,pe]} function xe(){…[he,N,P,F,I,ve,be]} function tt(){…[Se,Ce,Te,Ee,De,je,Ne,Ie,Le,ze,Ve,He,Ue,We,Ge,Je,Ye,Z,Ze,et]}
function rt(){let{bannerAperto:e}=s();return(0,C.jsxs)(`main`,{className:`relative bg-fo-bg text-fo-text`,children:[(0,C.jsx)(me,{}),(0,C.jsx)(xe,{}),(0,C.jsx)(tt,{}),(0,C.jsx)(nt,{bannerAperto:e})]})}
```
Tre **atti** (`me` apertura, `xe` argomento, `tt` offerta+prove+FAQ) + il bottone fisso `nt`.

---

## 3. IL FILE `raccoglitore-*.js`: cos'è

**Non è tracking né form.** `raccoglitore` = "raccoglitore ad anelli": è il componente **programma
del corso** disegnato come un classificatore con quattro linguette sporgenti (sezione `#programma`,
`scheda.json` sezione 20, y=21140). `src/32-raccoglitore-Bj4iyfd5.js`, 4.985 byte, esporta `n` (mappa
dati reali → geometria) e `t` (componente).

Le parti chiave:

```js
// dati finti di default (vedi §2.1) + le posizioni delle 4 linguette
l=[`2.02%`,`4.19%`,`7.6%`,`10.39%`];
// n: prende le sezioni vere dal loader e le fonde con la geometria predisposta
function u(e){return c.slice(0,e.length).map((t,n)=>({numero:t.numero,linguetta:t.linguetta,larghezza:t.larghezza,nome:e[n].nome,lezioni:e[n].lezioni}))}
```
→ **geometria e contenuto separati**: `linguetta` (posizione orizzontale in %), `larghezza` (min-width in
%) restano nel componente; `nome` e `lezioni` arrivano da Supabase (`Zp()` nel loader della home).

Il contenitore usa **container queries** (`@container`, `cqw`) e variabili locali con nomi italiani:
```js
className:`@container relative mx-auto w-full max-w-[967px] flow-root [--gradino:max(48px,7.239cqw)] [--linguetta:max(46px,6.826cqw)] [--sporgenza:max(37px,5.481cqw)] [--taglio:calc(var(--linguetta)*0.246)] [--fianco:max(12px,3.5cqw)] [--corpo:max(13px,2.275cqw)] [--moto-foglio:calc(var(--moto-momento)*1.6)]`
```
`--gradino` (passo verticale fra fogli), `--linguetta` (altezza linguetta), `--sporgenza`, `--taglio`
(angolo smussato = 24,6% della linguetta), `--fianco`, `--corpo` (font-size). Tutto in `cqw` con
minimo in px → **scala con la colonna, non con lo schermo** (il nostro §2, con lo strumento giusto:
container query invece di `vw`).

La linguetta è un `<button>` con `clip-path` poligonale calcolato sulle variabili:
```js
clipPath:`polygon(0 100%, calc(var(--taglio) - 1.7px) 6.9px, calc(var(--taglio) - 0.5px) 4.1px, calc(var(--taglio) + 1.5px) 1.9px, calc(var(--taglio) + 4.1px) 0.5px, calc(var(--taglio) + 7.1px) 0, calc(100% - var(--taglio) - 7.1px) 0, … 100% 100%)`
```
(gli angoli arrotondati sono approssimati con 5 punti per lato: `clip-path` non ha raggi).

Interazione: al hover/focus il foglio si solleva (`motion-safe:has-[button:hover]:animate-[fo-foglio-su_var(--moto-foglio)_linear_forwards]`
— **`:has()` + `motion-safe`**: l'animazione parte sul genitore quando il figlio è hover, e solo se
l'utente non ha chiesto meno movimento); al click apre un **Dialog** Radix con `numero`, `nome`,
`sommario` e la lista `<ol>` delle lezioni numerate `01, 02…` in `.codice`, chiuso da
«N lezioni in questa sezione». Accessibilità: `"aria-label":`Apri ${e.numero} — ${e.nome}``.

In fondo al raccoglitore c'è il logo come "copertina":
```js
(0,s.jsx)(`img`,{src:`/marchi/funops-logo-bianco.png`,alt:`Funnel Operator`,width:804,height:240,loading:`lazy`,decoding:`async`,className:`w-[44.92%] brightness-0`})
```
(`brightness-0` rende nero il PNG bianco: **un asset solo per due colori**).

Lezione: un componente di **vendita** (mostrare il programma) costruito come un componente di
**prodotto** (dati dal DB, geometria in cqw, dialog accessibile). Il programma cambia dal database
senza toccare la landing.

---

## 4. COMPONENTI RICONOSCIBILI

| # | componente | dove | come è fatto | cosa insegna |
|---|---|---|---|---|
| 1 | **Hero "lapide"** | `routes` `se()` | `<h1 class="lapide-uno mix-blend-difference text-center text-white">Un giorno <span class="lapide-due text-[#BD0000]">morirai</span>…` + `<img src="/vendita/soldato-caduto.webp" srcSet="…-832.webp 832w, ….webp 1664w" sizes="(min-width: 832px) 832px, 100vw" loading="eager" decoding="sync" fetchPriority="high" class="… mix-blend-screen">` | LCP curato: unico `eager` + `fetchPriority:high` + `srcset` a 2 densità. Il rosso `#BD0000` è **hardcoded** (l'unico colore fuori token: `var Oe="#BD0000"` riusato per il barrato «L'AI ti ruba il lavoro») |
| 2 | **Tre carte sparse** | `le()` | array `k` con `posa:"lg:absolute lg:left-[265px] lg:top-0 lg:z-10"`, `lg:-rotate-3`, `lg:rotate-3`; `border-[#676767]`, `shadow-[7px_11px_39.5px_rgb(0_0_0/0.2)]`; spunta via `maskImage:url(/vendita/spunta.svg)` su `span.bg-fo-blue` | icona SVG come **maschera** → colore dal token, un file solo |
| 3 | **Rail (marquee)** ×4 | `fe()` numeri, `V()` esempi (2 righe, la seconda `[animation-direction:reverse]`), `je()` loghi AI, `ze()` consulenze | `<div class="fo-rail-track overflow-hidden [mask-image:linear-gradient(to_right,transparent,black_6%,black_94%,transparent)]"><div class="fo-rail flex w-max …">{A}<div aria-hidden>{A}</div></div></div>` | contenuto **duplicato una volta con `aria-hidden`** per il loop; `translate(-50%)`; pausa al hover; `mask-image` per i bordi sfumati; `will-change:transform`; spento in `prefers-reduced-motion` |
| 4 | **VSL a click** (2) | `D()` con `S.principale`, `S.consulenza` | prima del click: `<button aria-label="Guarda il video: VSL 1">` con copertina `.webp` 1600×900 `loading=lazy` e triangolo CSS; dopo: `<iframe src="https://player.vimeo.com/video/1226141162?title=0&byline=0&portrait=0&dnt=1&speed=1&pip=1&playsinline=1&transparent=0&autoplay=1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture" allowFullScreen>` | **facade pattern**: zero iframe al caricamento (0 `iframe` in `scheda.json`), Vimeo con `dnt=1` (no tracking) e `autoplay=1` aggiunto solo al click |
| 5 | **Come funziona (7 step)** | `N()` | `<ol>` con card `max-w-[288px]`, icone posizionate in % (`riquadro:"left-[-8.77%] top-[11.5px] h-[115px] w-[42.27%]"`), connettori tratteggiati `border-dashed border-fo-chiaro-nero` con `rounded-tl-[5px]`, frecce CSS `border-x-[2.9px] border-t-[5px]`, solo `lg:block` | connettori **disegnati in CSS**, spariscono sotto lg; il triangolo finale è border-trick |
| 6 | **Confronto barrato** | `P()` | `<s class="font-medium text-fo-muted">Fare siti</s>` + `<span class="etichetta-confronto text-fo-chiaro-verde">Fare landing pages.</span>` | HTML semantico (`<s>`) per il "prima" |
| 7 | **Carta leggendaria (4 colonne animate)** | `Ne()` | `setInterval` ogni `Me=1500` ms che avanza `e=(e+1)%q.length`; **`if(window.matchMedia("(prefers-reduced-motion: reduce)").matches){t(2);return}`**; gradiente `bg-[linear-gradient(90deg,#88C9F4_0%,#1E9CD7_33%,#0075BE_66%,#005B97_100%)]` con `transition-opacity duration-700 … motion-reduce:transition-none`; numeri `font-tech` (DM Mono) | il **JS si spegne** con reduced-motion (il nostro §7 applicato al JS, non solo al CSS) |
| 8 | **Offerta + prezzo + countdown** | `Ie()`, `Pe()`, `Fe()` | `l(ee.ATTUALE)` → «434 €» (`toLocaleString("it-IT")+"\u00a0€"`); countdown `setInterval(…,1e3)` su `d()`=`Vp()` che calcola giorni/ore/minuti/secondi fino a `2026-10-12T00:00:00+02:00`; `<p aria-live="off"><span class="sr-only">Il prezzo sale tra</span>…` con `suppressHydrationWarning` sulle cifre e `tabular-nums` | **un dato solo** (`Ip`) → prezzo, «Dal 12 ottobre 2026: 560 €», FAQ, JSON-LD `priceValidUntil` (= giorno prima); countdown **muto per screen reader** (`aria-live="off"`) con etichetta nascosta |
| 9 | **Buy button** ×2 («Iscriviti adesso», «Sono pronto») | §1.8 | `bottone-che-lavora` + `f({size:"lg"})` | stato di attesa + errore in linea |
| 10 | **CTA fissa «Ottieni accesso»** | `nt()` | tre `IntersectionObserver` (sentinella alta `100svh` in cima, `#offerta-azioni`, `footer`): visibile solo se `scrollato oltre il primo schermo && !offerta visibile && !footer visibile && !bannerAperto`; `inert` quando nascosta; `href="#prezzo"` con `scrollIntoView({behavior: reduce?"auto":"smooth", block:"center"})` + `focus({preventScroll:true})`; posizione `bottom-[calc(var(--margine-pagina)+env(safe-area-inset-bottom))]`; ombra `shadow-[0_6px_28px_color-mix(in_oklab,var(--fo-blue)_22%,transparent)]` | il floating CTA **sparisce quando è ridondante** (offerta o footer in vista) e **cede al banner cookie**; `inert` toglie il bottone dal tab order quando invisibile; ombra dal token via `color-mix` |
| 11 | **Raccoglitore** | §3 | dialog + cqw | — |
| 12 | **FAQ** (2 gruppi + consulenza) | `Q()`, `$()`, `et()` | Radix Accordion `type="single" collapsible`, trigger con `chevron:!1` e «+» lucide `rotate-45` da aperto, sottolineatura animata `bg-[length:0%_1px] … group-hover:bg-[length:100%_1px] [box-decoration-break:clone]`, **`forceMount`** sul contenuto | contenuto FAQ sempre nel DOM (SEO, `Ctrl+F`), sottolineatura che cresce da sinistra senza JS |
| 13 | **Banner consenso** | `dd()` in `index` | `<section role="dialog" aria-labelledby="consenso-titolo" data-consenso={stato}>`, focus sul titolo all'apertura, altezza pubblicata in `--fo-banner-altezza` via `ResizeObserver`, bottoni «Rifiuta» / accetta, link `/cookie` `/privacy` | vedi §6 |
| 14 | **Header / footer** | `vd()`, `bd()` | `<picture><source media="(max-width: 639px)" srcSet="/marchi/funops-logomark-bianco.svg"><img src="/marchi/funops-logo-bianco.png" alt="Funnel Operator" width=804 height=240 class="h-8 w-auto"></picture>`; footer con `nav aria-label="Legale"`, bottone «Preferenze cookie» (`onClick:Lu` riapre il banner), ragione sociale `Andrei Pascu Sales · P.IVA 02001850474 · Viale Giacomo Matteotti 15, 50121 Firenze (FI)` | logo → **logomark sotto 640px** via `<picture>`; riapertura consenso dal footer |
| 15 | **Menu account** (solo loggati) | `_d()` | Radix DropdownMenu + Avatar iniziali, `aria-label:"Il tuo account — {nome}"` | — |
| 16 | **404 / errore** | `Ed()`, `Dd()` | `<picture><source media="(orientation: portrait)" srcSet="/immagini/404-mobile.webp">` + `<h1>404</h1>`; errore con «È un problema nostro, non tuo. Prova a ricaricare» e `Riprova` (`router.invalidate()`) | copy dell'errore che si prende la colpa |
| 17 | **Immagine responsiva `O()`** | `routes` | `function O({src,alt,larghezza,altezza,priorita=false,className,sorgenteStretta,fino=767,classNameGuscio})` → `<img width height loading={priorita?"eager":"lazy"} decoding={priorita?"sync":"async"}>` avvolto in `<picture><source media="(max-width: 767px)" srcSet={sorgenteStretta}>` se c'è una versione stretta | **un solo componente immagine** per tutta la pagina: dimensioni obbligatorie (niente CLS), lazy di default, `<picture>` solo quando serve |

Nessun `<video>`, YouTube, Wistia o Loom: solo Vimeo, e solo dopo il click.

---

## 5. IMMAGINI E PERFORMANCE

### 5.1 Immagini (da `media-inventario.md`: 68 file unici, 2.511 KB)

- **Formato**: 59 WebP, 8 SVG (icone numeri/spunta/loghi), 1 PNG (`funops-logo-bianco.png`, 30 KB —
  l'unico PNG, ed è il logo nell'header: candidato a SVG).
- **2× esatto**: 38 file su 60 misurabili hanno rapporto originale/reso fra 1.9 e 2.1
  (`soldato-caduto.webp` 1664×1236 → 832×618; `carte-mano.webp` 1504×680 → 752×340;
  `andrei-tondo.webp` 248×248 → 124×124). I restanti sono icone rese a 1× (`consulenza-*.webp`
  321×181 → 321×181, `motivo-*.webp` 60×60) o immagini `object-cover` a riempimento (`carta-serpenti`
  1440×928 → 1440×928). Regola sua: **esporta al doppio della misura di resa, mai di più**.
- **Peso**: 2.511 KB totali; il più pesante `carte-mano.webp` 256 KB (illustrazione 1504×680),
  `soldato-caduto.webp` 218 KB (hero), `tessera.webp` 185 KB (840×1721). Le 5 più pesanti = 933 KB,
  il 37% del totale.
- **`loading="lazy"`**: **tutte** le `<img>` in `routes` hanno `loading:"lazy",decoding:"async"`,
  tranne l'hero (`loading:"eager",decoding:"sync",fetchPriority:"high"`) e il logo header (nessun
  attributo, quindi eager). Il pattern è imposto dal componente `O()` (default `priorita=false`).
- **`<picture>`**: 3 nel DOM (`scheda.json` → `media`: picture 3, img 119, iframe 0):
  1. header, `source media="(max-width: 639px)"` → logomark SVG al posto del logo orizzontale;
  2. `sito-apple.webp` con `sorgenteStretta:"/vendita/sito-apple-stretta.webp"` (830×220 è troppo
     largo e basso per un telefono: sotto 767px cambia ritaglio);
  3. `cambiare-vita.webp` con `sorgenteStretta:"/vendita/cambiare-vita-stretta.webp"`.
  Più il 404 (`orientation: portrait`), fuori dalla landing. **Art direction, non solo densità.**
- **`srcset`**: 2 casi, entrambi con `sizes`: hero (`832w, 1664w`) e tessera (`420w, 840w`,
  `sizes:"(min-width: 1024px) 272px, 92vw"`). Le altre immagini hanno un file solo a 2×.
- **`width`/`height` dichiarati**: sì su ogni `<img>` (`larghezza`/`altezza` obbligatori in `O()`,
  `width/height` espliciti nelle immagini scritte a mano, anche le icone 60×60 e 40×40) → il browser
  riserva lo spazio, **CLS da immagini praticamente zero**. Dove il layout è fluido usa `aspect-[402/496]`,
  `aspect-[297/373]`, `aspect-video`.
- **Sfondi**: 2 in CSS `bg-[url('/vendita/roccia.webp')]`, `bg-[url('/vendita/offerta-roccia.webp')] opacity-28`
  — non lazy per natura, ma sotto la piega.

### 5.2 Peso JS/CSS servito alla landing (da `src/_INDICE.json`)

| | file | byte |
|---|---|---|
| JS | 43 | **876.499** (856 KB non compressi) |
| CSS | 1 | **148.072** (145 KB) |
| di cui `index-CLKYm5hM.js` | 1 | 588.728 (67% del JS) |
| `routes-DT2uV_Ni.js` (la landing vera) | 1 | 68.476 |
| `createServerFn` | 1 | 36.292 |
| chunk sotto 1 KB | 12 | (icone lucide, hook router, clsx…) |

Manifest completo: **105 chunk**; la landing ne carica 43 (41%). Code splitting per rotta e per
primitiva Radix, ma l'`index` porta con sé supabase-js (auth + realtime + storage), react-query, zod
e tutte le definizioni di rotta anche a un visitatore anonimo. Stima brotli tipica per questo tipo di
bundle: ~200–240 KB di JS + ~20 KB di CSS trasferiti.

### 5.3 Lettura Lighthouse-like (qualitativa, senza numero inventato)

Punti a favore, misurati nel codice:
- LCP: hero con `fetchPriority="high"`, `srcset`, `eager`, `decoding="sync"`, dimensioni dichiarate; font critici in `preload`; CSS unico esterno con hash lungo (cache); SSR (HTML pieno prima dell'hydration).
- CLS: `width`/`height` su ogni immagine, `aspect-*` sui contenitori fluidi, il banner cookie **spinge** il layout con `padding-bottom` invece di coprirlo, il countdown usa `tabular-nums` e `min-w-[2.6em]`.
- Rete: zero terze parti al primo caricamento (Vimeo solo al click, tag di misura solo dopo consenso), font self-hosted subsettati.
- Immagini: WebP, 2× calibrato, lazy di default.

Punti contro:
- **~590 KB di JS non compresso in un chunk solo**, di cui gran parte inutile per la vendita
  (supabase realtime, react-query). TBT/INP ne risentono su mobile medio.
- 4 marquee `animation: 70s linear infinite` (2 a 45s) con `will-change:transform` sempre attivi → compositing continuo.
- 12 immagini `mix-blend-*` / `blur-[3.55px]` / `backdrop-blur` (hero `mix-blend-difference` sul testo, `mix-blend-screen` sull'immagine, `mix-blend-color-dodge`, `hard-light`) → costo di paint.
- Pagina lunga 32.807 px desktop / 36.630 px mobile con 119 immagini: il lazy loading è indispensabile e c'è.
- Un PNG di 30 KB per il logo dove basterebbe l'SVG che già esiste (`funops-logomark-*.svg`).

Verdetto qualitativo: **ottimo su LCP/CLS per una pagina così lunga, mediocre su TBT per colpa del
chunk applicativo**. È il prezzo di aver fuso landing e LMS nello stesso bundle.

---

## 6. TRACCIAMENTO E CONVERSIONE

### 6.1 Pixel e tag: predisposti tre, attivo uno

`src/29-index-CLKYm5hM.js` pos. 493700–495000:

```js
var ed=H({…env…}.VITE_META_PIXEL_ID), td=H({…env…}.VITE_GA4_MEASUREMENT_ID), nd=H({…env…}.VITE_CLARITY_PROJECT_ID),
rd=ed||td||nd?{meta:ed,ga4:td,clarity:nd}:null,
id=[ed?`Meta`:null,td?`Google`:null,nd?`Microsoft`:null].filter(e=>e!==null);
```
Nell'oggetto env inlined **non esistono** `VITE_META_PIXEL_ID` né `VITE_GA4_MEASUREMENT_ID` → `ed` e
`td` sono `null`; esiste `VITE_CLARITY_PROJECT_ID:"yh4ehu2xkk"` → oggi `rd={meta:null,ga4:null,clarity:"yh4ehu2xkk"}`.
**Meta Pixel e GA4: codice pronto, spenti. Microsoft Clarity: acceso** (registrazione sessioni).

Il caricamento è **condizionato al consenso e alla rotta**:
```js
function Td(){let e=od(),{stato:t}=qu(),n=rd!==null&&t===`accettato`&&e;
(0,D.useEffect)(()=>{!n||!rd||wd||(wd=!0,cd(rd))},[n]),
(0,D.useEffect)(()=>{!wd||n||(ld(),window.location.assign(window.location.pathname+window.location.search))},[n]),null}
```
`od()` = «la rotta corrente è `/`». Quindi i tag partono solo se `stato==="accettato"` **e** si è
sulla landing (mai nell'area corso, come promette il testo del banner). Se l'utente **revoca**, `ld()`
chiama `clarity("stop")` e la pagina **si ricarica** per pulire lo stato: il modo più onesto di
spegnere uno script già iniettato.

`cd(rd)` è l'installer classico: `fbq("init",id);fbq("track","PageView")`, `gtag("js",new Date);gtag("config",id)`
via `https://www.googletagmanager.com/gtag/js?id=`, `clarity` via `https://www.clarity.ms/tag/`.
**Nessun GTM container, nessun Hotjar, Plausible, PostHog.** Vercel Analytics/Speed Insights sono
attivi a livello progetto (§1.5) ma non nel bundle.

### 6.2 Analytics first-party (la sua)

```js
Tu=[`visit`,`login`,`password_reset`,`lesson_completed`],
Eu=p({method:`POST`}).handler(l(`bf40812c…`)),
Ou=`fo-consenso`,ku=`fo-visitatore`,Au=`misura`
```
- `localStorage["fo-consenso"]` = `"misura"` (accettato) | `"no"` (rifiutato) | assente (non risposto).
- `localStorage["fo-visitatore"]` = `crypto.randomUUID()` creato **solo se accettato**, cancellato al rifiuto.
- `sessionStorage["fo-atterraggio"]` marca la prima pagina della sessione: solo lì si leggono
  `document.referrer` (se esterno, troncato a 500), `utm_source/medium/campaign` (troncati a 200) e `isLanding:true`.
- A ogni cambio di `pathname` (`$u`) parte `Eu({data:{type:"visit",path,email:null,lessonCode:null,referrer,utm*,isLanding,visitorId}})`;
  `visitorId` è `null` sotto `/member` (niente ID anonimo dove l'utente è già loggato).
- `catch(()=>{})` ovunque: il tracking **non può rompere** la pagina.

Il testo del banner spiega esattamente questo, in italiano piano:
> «Per capire quante persone *diverse* visitano il sito salviamo un identificativo casuale nel tuo
> browser. Non contiene il tuo nome e non serve a riconoscerti altrove. Se preferisci di no, il sito
> funziona identico: contiamo comunque quante pagine vengono viste, ma senza questo identificativo.»

e, se ci sono tag terzi:
```js
function ud(e,t){let n=`registra come un filmato il movimento del puntatore e i clic su questa pagina`;
if(t.length===1)return`Su questa pagina, e solo su questa, accettando si attiva anche lo strumento di misurazione di ${t[0]}${e.clarity?`, che ${n}`:``}. Non entra nell'area del corso.`; …}
```
→ oggi il banner dice: «…si attiva anche lo strumento di misurazione di Microsoft, che registra come
un filmato il movimento del puntatore e i clic su questa pagina. Non entra nell'area del corso.»
La frase si **compone dai tag realmente configurati**: se domani accende Meta, il banner cambia da solo.

### 6.3 Cosa succede al click e dove porta ogni CTA

`scheda.json` → `cta`: 26 elementi cliccabili, **24 con `href:null`**. Ricostruiti dagli handler:

| CTA (testo) | quanti | tipo | cosa fa |
|---|---|---|---|
| «Iscriviti adesso» (offerta), «Sono pronto» (chiusura) | 2 | `<button>` buy-button | `await Mp()` → `{url}` → `window.location.href=url` (checkout esterno, sessione creata server-side) |
| «Cosa contiene il corso?» | 1 | `<a href="#programma">` | scroll al raccoglitore (`scroll-mt-24`) |
| «Ottieni accesso» (fissa) | 1 | `<a href="#prezzo">` | `scrollIntoView` su `#prezzo` (`tabIndex:-1`) + focus |
| «01 Intro» … «04 Domande comuni» | 4 | `<button aria-label="Apri 01 — Intro">` | apre Dialog con le lezioni |
| FAQ consulenza (4) + FAQ Funnel Operator (9) + FAQ pagamento (5) | 18 | Radix `AccordionTrigger` (`<button>`) | apre/chiude |
| «Accedi →» (header) | link | `Link to="/auth"` | login |
| Trustpilot, SEC, `bsns.it`, `apsales.eu` | link nel testo | `target="_blank" rel="noopener noreferrer"` | esterni |

**Punti di uscita verso il pagamento: 2 bottoni + 1 ancora che porta al prezzo** (la CTA fissa non
compra, porta al blocco offerta). Nessun form, nessuna email da lasciare, nessun lead magnet: la
pagina ha **una sola azione**, comprare, e tutte le altre interazioni restano dentro la pagina.
Nessun `id="offerta"` duplicato; `#prezzo`, `#offerta`, `#offerta-azioni`, `#programma` sono i
quattro ancoraggi.

### 6.4 Eventi di conversione: dove stanno

Nel client **non c'è** `fbq("track","InitiateCheckout")` né `gtag("event","purchase")`. Il click sul
buy-button non emette eventi: l'unico evento first-party è `visit`. La conversione, se tracciata, lo
è **lato server** (webhook del provider di pagamento → Supabase) — coerente con il fatto che il
provider stesso non è nel bundle. Dal punto di vista ads oggi la pagina misura **solo PageView di
Clarity** dopo consenso: o non sta facendo paid, o attribuisce dalla piattaforma di pagamento.

---

## 7. SEO E META

Dalla `scheda.json` (`meta`) e da `index` (`Od=ke()({head:…})` root + `em=qn("/")({head:…})`):

- `<html lang="it">` (shell React).
- **Title**: `Funnel Operator — Impara a fare landing pages per le aziende` (60 caratteri).
- **Description**: `Impara a fare landing pages per le aziende e a trovare i clienti che te le pagano. Accesso a vita, pagamento unico.` (117 caratteri).
- **Canonical** calcolato dalla rotta senza slash finale: `` `https://www.funneloperator.it${pathname.replace(/\/+$/,``)||`/`}` `` → `https://www.funneloperator.it/`.
- **OG/Twitter** nel root: `og:type website`, `og:url`, `og:locale it_IT`, `og:site_name`, `og:image https://www.funneloperator.it/immagini/anteprima-social.png` con `og:image:width 1200`, `og:image:height 630`, `og:image:alt`, `twitter:card summary_large_image`, `twitter:image`. La rotta `/` sovrascrive `og:title`/`og:description`/`twitter:title`/`twitter:description` con quelli della pagina. **Head per rotta con merge**: le pagine tecniche (`/auth`, `/post-checkout`, `/conferma-email`, `/annulla-cambio-email`, `/member/*`, `/$adminSegmento`) hanno `robots: noindex, nofollow` (+ `noarchive`, `nosnippet`, `googlebot` sull'admin).
- **Favicon**: `/favicon.svg` (`image/svg+xml`) + `/favicon.png` 32×32 + `apple-touch-icon` 180×180.
- **JSON-LD** (`scripts:[{type:"application/ld+json",children:JSON.stringify(Xp($p))}]`), un `@graph` con 6 nodi collegati per `@id`:
  ```js
  {"@type":"Organization","@id":"https://www.apsales.eu/#organization",name:"AP Sales",legalName:"Andrei Pascu Sales",url:"https://www.apsales.eu",vatID:"IT02001850474",address:{…Viale Giacomo Matteotti 15, 50121 Firenze, IT},founder:{"@id":qp},sameAs:["https://www.andrei-copy.com","https://bsns.it"]},
  {"@type":"Person","@id":"https://www.andrei-copy.com/#andrei-pascu",name:"Andrei Pascu",url:"https://www.andrei-copy.com",jobTitle:"Titolare AP Sales",worksFor:{"@id":Kp},sameAs:["https://www.instagram.com/andrei.bsns","https://bsns.it"]},
  {"@type":"WebSite","@id":"https://www.funneloperator.it/#website",…publisher:{"@id":Kp}},
  {"@type":"Course","@id":"…/#corso",name:"Funnel Operator",…isAccessibleForFree:false,provider:{"@id":Kp},author:{"@id":qp},teaches:["Fare landing pages per le aziende","Trovare i clienti che te le pagano","Usare l'AI per fare landing pages senza fare AI slop"],hasCourseInstance:[{"@type":"CourseInstance",courseMode:"Online",instructor:{"@id":qp}}],offers:{"@type":"Offer",url:"…/#offerta",price:String(Ip.ATTUALE),priceCurrency:Ip.VALUTA,availability:"https://schema.org/InStock",category:"Paid",...Yp()?{priceValidUntil:Yp()}:{}}},
  {"@type":"FAQPage","@id":"…/#faq",mainEntity:t},   // t = TUTTE le FAQ (Hp + Up() + Wp), 18 Question
  {"@type":"WebPage","@id":"…/#pagina",…isPartOf:{"@id":"…/#website"},about:{"@id":"…/#corso"}}
  ```
  Tre cose notevoli: (a) **entità cross-dominio** — l'Organization vive su `apsales.eu`, la Person
  su `andrei-copy.com`: tutti i suoi siti puntano alle stesse `@id` (knowledge graph coerente
  dell'ecosistema); (b) **`Offer.price` e `priceValidUntil` derivati dallo stesso `Ip`** del prezzo in
  pagina (`Yp()` = giorno prima del cambio prezzo); (c) le **FAQ del JSON-LD sono generate dagli stessi
  array** che rendono l'accordion (`Hp`, `Up()`, `Wp`) → zero divergenza fra testo visibile e markup.
- **Heading**: **1 solo `h1`** («Un giorno morirai.»), poi 33 `h2`/`h3` (`scheda.json` → `headings`).
  Ordine corretto: ogni `h3` sta sotto un `h2` (es. «L'evoluzione del copywriting» h3 sotto «La realtà
  dei fatti?» h2). Una stranezza: `Impara a fare landing page / Impara a trovare clienti / Chiudi un
  caso studio / Fatti pagare` sono 4 `h3` alla stessa y=19481 (le colonne della carta leggendaria) —
  legittimo. «FUNNEL OPERATOR» compare come `h2` (offerta) e come `h3` (etichetta gruppo FAQ): due
  heading identici, il secondo sarebbe meglio un `<p>`.

---

## 8. ACCESSIBILITÀ

- **Alt** (da `media-inventario.md`): 41 pieni, 27 vuoti su 68 file. I 27 vuoti sono: la hero
  `soldato-caduto.webp` (scelta discutibile: è l'immagine che dà senso al titolo), le 2 copertine VSL
  (dentro un `<button aria-label="Guarda il video: …">`, corretto), le 3 carte (`carta-*.webp`, il testo
  è nel `<p>` accanto), `stack-clienti.webp` (**compensato da un `<ol class="sr-only">` con le 4 voci**
  DM su Instagram / Loom / Call / Chiusura progetto: l'immagine è decorativa perché il contenuto è
  ripetuto in testo nascosto), tutte le icone `passo-*`, `motivo-*`, `ordini/studenti/apertura/trustpilot.svg`
  con `aria-hidden="true"` e testo accanto, `serpente-testa`, `carta-serpenti`, `aeroplano`, `telegram`
  decorativi con `aria-hidden`. Gli alt pieni sono **descrittivi e lunghi** («Avviso della U.S.
  Securities and Exchange Commission: «Gli investitori dovrebbero capire che…». SEC, ente governativo
  americano…» — l'alt trascrive il documento fotografato). Qualità alta.
- **Focus**: `:focus-visible{outline:2px solid var(--fo-focus);outline-offset:2px}` globale;
  `#prezzo` con `tabIndex:-1` + `focus({preventScroll:true})` dopo lo scroll della CTA fissa;
  banner consenso con `ref` che riceve `focus()` all'apertura; CTA fissa `inert` quando nascosta;
  raccoglitore `motion-safe:has-[button:focus-visible]:animate-[…]` (il foglio si solleva anche da tastiera).
- **`prefers-reduced-motion`** (4 occorrenze nel CSS, 2 nel JS di `routes`):
  ```css
  @media (prefers-reduced-motion:reduce){*,:before,:after{--tw-enter-translate-x:0!important;…}.comparsa{animation-name:fo-dissolvenza}.battuta{animation-name:fo-dissolvenza;animation-delay:0s}.animate-accordion-down,.animate-accordion-up,…{animation-duration:1ms}.fo-rail{animation:none}.sagoma{background:var(--fo-elevated);animation:none}.girandola{animation-duration:2s}}
  @media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
  ```
  Le animazioni di ingresso **non spariscono: diventano dissolvenze** (`fo-dissolvenza` = solo opacità).
  Lo spinner rallenta (0.7s → 2s) invece di fermarsi (sarebbe informazione persa). Il JS: il carousel
  a 4 colonne si ferma sulla colonna 3 (`t(2);return`), lo `scrollIntoView` diventa `auto`.
- **Contrasto** (dai token): testo `oklch(93.4%)` su fondo `oklch(17.8%)` ≈ 13:1; muto `oklch(63.3%)`
  su `17.8%` ≈ 5.5:1 (AA testo normale); tema chiaro `17.8%` su `94.6%` ≈ 13:1, muto `47.3%` su `94.6%`
  ≈ 5.6:1; azione `--fo-blue oklch(65.6% .134 235.9)` con testo `--fo-on-action` = fondo scuro `17.8%`
  ≈ 5.8:1 (AA). L'unica coppia debole: link `--fo-blue` su fondo scuro per testo 17px ≈ 5.8:1, ok.
  Il rosso `#BD0000` su fondo scuro (parola «morirai», 290px) ≈ 3.2:1 — accettabile solo perché è
  testo gigante (AA large ≥ 3:1).
- **Semantica**: `<section aria-label>` dove manca un heading (`"I numeri di AP Sales"`, `"Funnel Operator"`
  per la hero), `<nav aria-label="Principale">`, `<nav aria-label="Legale">`, `<ol>` per gli step e le
  lezioni, `<s>` per il barrato, `<dl>` predisposto per i numeri, `role="alert"` sull'errore del buy
  button, `role="dialog" aria-labelledby` sul banner, `aria-live="off"` sul countdown, `<span aria-hidden>↓</span>`
  sulle frecce decorative, duplicati del marquee in `aria-hidden`.
- **Touch**: bottoni `h-12` (48px) per `size:lg`, linguette raccoglitore `min-width` in % con `max(46px, …)`.

Giudizio: **accessibilità sopra la media delle pagine di vendita italiane**, costruita nel componente
e non aggiunta dopo.

---

## 9. COSA COPIARE NELLA NOSTRA FABBRICA SITI

Vincolo (CLAUDE-SITI §13, ADR-030): su `agency-empire-landing` (Next.js 16, `output:"export"`,
`images.unoptimized`, `trailingSlash`) si **aggiunge soltanto**: file nuovi in `src/sezioni-aggiunte/`,
CSS scopato sotto `.vivo` in `src/app/vivo.css`, inserimenti puri in `page.tsx`/`layout.tsx`.
Ogni regola qui sotto è formulata così.

| # | lui fa (file:posizione) | noi facciamo, nelle sezioni aggiunte |
|---|---|---|
| 1 | **Un dato prezzo solo** `Ip={ATTUALE:434,…PROSSIMO:{importo:560,dal:"2026-10-12"}}` → pagina, FAQ, countdown, JSON-LD (`index` 573572, 577200) | un modulo `src/sezioni-aggiunte/offerta.ts` che esporta `OFFERTA={prezzo, valuta, prossimo?}` e funzioni `formatta()`, `prossimoCambio()`; ogni cifra in `page.tsx`, FAQ e `<script type="application/ld+json">` la importa. Il `gate_siti.py` già controlla §8: aggiungiamo la regola «nessun letterale `€` seguito da cifra nei `.tsx` fuori dal modulo offerta» |
| 2 | **Componente immagine unico** `O({src,alt,larghezza,altezza,priorita,sorgenteStretta,fino})` → `width/height` obbligatori, lazy di default, `<picture>` solo se c'è la versione stretta (`routes` 3000–3600) | `src/sezioni-aggiunte/Immagine.tsx` con le stesse prop **obbligatorie** (TypeScript le rende obbligatorie davvero); `unoptimized` è già il nostro caso, quindi `<img>` puro come il suo. Gate: nessun `<img` senza `width`/`height` nei file di `sezioni-aggiunte/` |
| 3 | **Hero LCP**: `loading="eager" decoding="sync" fetchPriority="high" srcSet="…832w, …1664w" sizes="(min-width: 832px) 832px, 100vw"` (`routes` 3700) | nelle sezioni nuove **una sola** immagine con `priorita`; il canone Empire aggiunge `fetchPriority="high"` alla prop `priorita` del componente #2. Nessun `eager` altrove (gate: max 1 `fetchPriority` per pagina) |
| 4 | **Facade video**: `<button aria-label="Guarda il video: …">` con copertina WebP → `<iframe … autoplay=1 dnt=1>` solo al click (`routes` 1800–3000) | `src/sezioni-aggiunte/VideoAClick.tsx` per ogni embed (YouTube `youtube-nocookie.com`, Vimeo `dnt=1`): zero iframe al load, etichetta «— da girare» quando la sorgente manca (così il segnaposto è visibile in anteprima e non passa il gate). Gate: nessun `<iframe` statico nei `.tsx` |
| 5 | **Rail con duplicato `aria-hidden`, `mask-image`, pausa al hover, spento in reduced-motion** (`routes` 10500; CSS `.fo-rail`, `.fo-rail-track:hover .fo-rail{animation-play-state:paused}`, `@media (prefers-reduced-motion:reduce){.fo-rail{animation:none}}`) | pattern `pattern/rail.css` scopato `.vivo .rail-track`, `.vivo .rail`; il contenuto duplicato porta `aria-hidden`; tempi dal canone (`--durata-rail:70s`). Sostituisce qualunque marquee JS |
| 6 | **Reduced motion anche nel JS**: `if(window.matchMedia("(prefers-reduced-motion: reduce)").matches){t(2);return}` (`routes` 43000), `scrollIntoView({behavior:n?"auto":"smooth"})` | in `count-up.tsx` e `reveal.tsx` **esistenti non si tocca** (§13); nelle sezioni nuove ogni `useEffect` con timer/animazione apre con lo stesso `matchMedia`. Il nostro §7 lo dice già: qui c'è la forma esatta da copiare |
| 7 | **Reduced motion = dissolvenza, non sparizione**: `.comparsa{animation-name:fo-dissolvenza}` (CSS 140500) | in `vivo.css`: `@media (prefers-reduced-motion:reduce){.vivo .in{animation-name:vivo-dissolvenza}}` con `@keyframes vivo-dissolvenza{0%{opacity:0}}` — l'utente vede comunque un ingresso, senza movimento |
| 8 | **CTA fissa che sparisce quando è ridondante** (3 `IntersectionObserver`: sopra il primo schermo, `#offerta-azioni` in vista, `footer` in vista) + `inert` quando nascosta + `bottom:calc(var(--margine-pagina)+env(safe-area-inset-bottom))` (`routes` 62000) | `src/sezioni-aggiunte/CtaFissa.tsx`: stessa logica a tre sentinelle su `#prenota-azioni` e `footer`; `inert` via attributo; `env(safe-area-inset-bottom)` nel CSS scopato. Oggi il nostro `call-cta.tsx` non sparisce mai: **non lo modifichiamo**, aggiungiamo la versione nuova solo nelle pagine nuove (`/prenota/`) |
| 9 | **Tema per sezione con override di variabili**: `.sezione-chiara{--fo-bg:var(--fo-chiaro-fondo);--fo-text:…}` (CSS 41370) e prop `tono:"chiaro"|"scuro"` | in `vivo.css`: `.vivo .sezione-chiara{--vivo-bg:…;--vivo-testo:…}`; tutte le classi figlie leggono solo `var(--vivo-*)`. Un componente `Sezione({tono})` in `sezioni-aggiunte/` come il suo `w()`. Toglie ogni `bg-white text-black` scritto a mano |
| 10 | **Quattro spazi in clamp** `--spazio-blocchi:clamp(32px,7.5vw,48px)`, `--spazio-sezioni:clamp(40px,10vw,64px)`, `--spazio-vendita:clamp(56px,15vw,96px)`, `--spazio-area:clamp(64px,17.5vw,112px)` + utility `.py-vendita`, `.mt-blocchi` | `canone.css`: aggiungere la scala `--spazio-blocchi/sezioni/vendita/area` (valori nostri, ma **quattro e in clamp**), e in `vivo.css` le utility `.vivo .py-vendita`, `.vivo .mt-blocchi`. Elimina i `mt-[53px] md:mt-[97px]` sparsi (che lui stesso ha ancora: vedi §10 difetti) |
| 11 | **Consenso onesto e tag dopo il sì**: banner `role="dialog"` con testo che si compone dai tag configurati (`ud()`), `localStorage["fo-consenso"]`, tag iniettati solo se `accettato` e solo sulla rotta di vendita, `clarity("stop")+reload` alla revoca, «Preferenze cookie» nel footer (`index` 493700–496500) | `src/sezioni-aggiunte/Consenso.tsx` + `src/lib/misura.ts`: stessa macchina a stati (`non-risposto/accettato/rifiutato`), chiave `de-consenso`, un solo punto `attivaTag()` che legge `NEXT_PUBLIC_*` **una chiave per volta**; il testo del banner elenca i fornitori davvero configurati. La pagina `/cookie/` esiste già: si aggiunge il bottone «Preferenze cookie» nelle sezioni nostre, non nel footer esistente (§13) |
| 12 | **Analytics first-party minimale**: evento `visit` con `path, referrer (solo esterno, ≤500), utm_* (≤200), isLanding, visitorId opzionale`; `sessionStorage` per il primo atterraggio; `catch(()=>{})` (`index` 486000–488000) | per il sito statico: `navigator.sendBeacon` verso un endpoint nostro (Vercel Function o Supabase Edge) con lo stesso payload troncato; `visitorId` solo dopo consenso. Ci dà referrer+UTM senza terze parti: è il minimo che B-043 («DE non misura un solo euro») chiede |
| 13 | **JSON-LD generato dagli stessi dati della pagina**: FAQ da `[...Hp,...Up(),...Wp]`, prezzo da `Ip`, `@id` cross-dominio per Organization/Person (`index` 577200–579700) | `src/sezioni-aggiunte/schema.ts` che costruisce `@graph` (Organization Digital Empire, Person Max, WebSite, Service/Offer, FAQPage) **dagli array** che rendono le FAQ e dal modulo offerta (#1); `@id` stabili riusati su tutti i nostri domini. Inserimento puro in `layout.tsx` (+1 riga) |
| 14 | **Font self-hosted, variable, subset, preload dei due critici, `font-display:block` solo sul display font** (CSS `@font-face`; `index` 507432 `rel:preload as:font crossOrigin:anonymous`) | `public/caratteri/*.woff2` (già la nostra pratica per grana e brand): verificare che i due file usati above-the-fold abbiano `<link rel="preload" as="font" type="font/woff2" crossorigin>` in `layout.tsx` (+2 righe) e che il display font abbia `font-display:block`, il corpo `swap`. Gate: ogni `@font-face` in `vivo.css` deve avere `unicode-range` o essere già subset |
| 15 | **Placeholder che si dichiarano** («Testo finto di prova — questa riga non è il corso», «VSL 1 — da girare») e **sezioni che si spengono da sole se l'array è vuoto** (`G.length===0?null:…`) | nelle sezioni aggiunte ogni dato di prova porta il prefisso `FINTO —` e ogni sezione alimentata da lista esce `null` se la lista è vuota. `gate_siti.py`: FAIL se nella build compare `FINTO —` o `— da girare` (così il segnaposto è utile in anteprima e **non può** andare in produzione — la lezione del 12 settembre) |

E **una da non copiare**: l'inlining dell'intero `import.meta.env` (§1.7). Nel nostro Next `process.env.NEXT_PUBLIC_X`
va letto **per chiave**, mai destrutturato o loggato; il gate può cercare `process.env)` e `import.meta.env)` chiusi senza chiave.

---

## 10. DIFETTI REALI (misurati)

1. **Bundle espone build env** (§1.7): repo, autore, commit message, ID Vercel/Supabase/Clarity.
2. **589 KB di JS in un chunk** anche per il visitatore anonimo: supabase realtime/storage, react-query, zod, 22 definizioni di rotta.
3. **Numeri magici residui** nonostante i 4 spazi in clamp: `mt-[53px] md:mt-[97px]`, `mt-[45px]`, `gap-[54px]`, `lg:left-[265px] lg:top-[142px]`, `lg:h-[655px]`, `top-[60.3%] left-[53.1%]` (`routes`, decine). Il canone ha la scala, il codice non la usa sempre — stesso difetto già visto su `apsales.eu` (dossier 18-20). È la conferma che §6 («ogni numero non ovvio dichiara la sua origine») serve **anche a chi ha un CLAUDE.md**.
4. **Colore fuori token**: `#BD0000` (rosso hero e barrato), `#676767` (bordo carte), `#88C9F4/#1E9CD7/#0075BE/#005B97` (gradiente carta leggendaria), `#fff`/`white` sparsi. Il sistema `fo-` ha 59 colori e la pagina ne inventa 7.
5. **Logo PNG** 30 KB nell'header e nel footer con un SVG logomark già disponibile.
6. **Rotta `/cantiere` pubblica** senza `noindex`, senza title: pagina di test raggiungibile.
7. **Heading doppio** «FUNNEL OPERATOR» (h2 offerta + h3 etichetta FAQ).
8. **Hero `alt=""`** sull'immagine che dà senso al titolo.
9. Tre sezioni predisposte e vuote in produzione (numeri, testimonianze, lista contenuti): non un
   bug, ma il segno che la pagina è **uscita incompleta rispetto al progetto** — coerente con il
   commit «Sicurezza a 360° del lancio»: ha lanciato quando la cassa era sicura, non quando la pagina
   era finita. È la sua versione del nostro ULTIMO METRO (ADR-016).

---

## 11. FONTI

Cartella: `C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\site-study\capture\66-funneloperator-it\`

- `src/_INDICE.json` — 44 file, URL di origine e peso in byte.
- `src/29-index-CLKYm5hM.js` — chunk applicativo (588.728 B): env inlined (pos. 456616), analytics e consenso (485000–496500), layout/header/footer (503000–508000), rotte e head (566500–586000), prezzo `Ip` (573572), JSON-LD `Xp` (577200–579700).
- `src/36-routes-DT2uV_Ni.js` — la landing (68.476 B): primitive `w/T/E`, `O`, `D`, tutte le sezioni, CTA fissa `nt`.
- `src/32-raccoglitore-Bj4iyfd5.js` — programma del corso a linguette.
- `src/05-buy-button-DX_4IxaR.js` — bottone di acquisto.
- `src/04-button-rHPgEXhH.js` — varianti bottone (cva).
- `src/02-accordion-BvtD-mDo.js`, `src/12-dialog-PqngB_cI.js`, `src/28-dropdown-menu-COwaHBxh.js`, `src/03-avatar-JcsTr3Jb.js` — shadcn/Radix.
- `src/11-createServerFn-Dnzfrwdq.js` — client server functions TanStack Start (`/_serverFn/`, `x-tsr-serverFn`).
- `src/35-route-BYPzqRIj.js`, `src/31-link-DiKj2Kcl.js`, `src/43-useStore-CmuWC2Bw.js`, `src/37-shim-DoKe8bYx.js` — TanStack Router/Store.
- `src/38-styles-Cm6i-gBj.css` — Tailwind v4.2.4, tema (2539), token `--fo-*` (136716), classi italiane (varie), keyframes (~139700), reduced-motion (~140400).
- `scheda.json` — `meta`, `headings` (1 h1 + 33 h2/h3), `cta` (26), `media` (122: 119 img, 3 picture, 0 iframe), `sezioni` (30), `keyframes`, `effetti`, `caratteri`.
- `media-inventario.md` — 68 file, 2.511 KB, alt, misure originali/rese.
- `dom-blocks.json` — 386 blocchi di testo (solo testo: usato per conferma di href e ordine).
- `estratto-css.md`, `design-tokens.json`, `copy-integrale.md` — controprova di token e testi.
- Rapporti collegati: `reports/11-armageddon.md` §0–§1 (metodo Claude Code, corsia vanilla), `reports/13-apsales-STACK-E-TOKEN.md` §1 (stesso stack TanStack Start su apsales.eu), `reports/18-20-apsales-servizi-COSTRUZIONE.md`, `reports/02-funnel-operator.md` (studio precedente della stessa pagina, versione prima del relaunch).
- Legge nostra: `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` §1–§13; `agency-empire-landing/next.config.mjs` (`output:"export"`, `images.unoptimized`, `trailingSlash`).
