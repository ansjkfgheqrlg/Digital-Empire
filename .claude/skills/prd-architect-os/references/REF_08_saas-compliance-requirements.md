# REF_08 — SaaS Compliance Requirements
## GDPR, SOC 2, HIPAA — Cosa Includere nel PRD

Questo file è il **reference operativo** per scrivere sezioni di compliance nei PRD SaaS.
Non è consulenza legale. È ingegneria della privacy: requisiti tecnici concreti da specificare nel prodotto.

---

## 1. Perché la Compliance Va nel PRD — Non Post-Lancio

Il momento peggiore per scoprire un requisito GDPR è quando il prodotto è già in produzione con 10.000 utenti.

Aggiungere la compliance dopo il lancio costa mediamente **4-8x** di più rispetto a integrarla in fase di design. Motivo: devi fare refactoring di schema DB, retroattivamente notificare utenti, cambiare architetture di logging che erano state pensate senza audit trail.

### Il costo reale dell'afterthought

| Requisito ignorato in PRD | Costo di fix post-lancio |
|---|---|
| Right-to-be-forgotten | Refactor di tutte le tabelle con FK, cascade delete, soft delete retroattivo |
| Audit logging | Aggiunta di middleware + tabelle di log + retroactive log import |
| Consenso granulare | Refactor del signup flow, aggiornamento DB, re-consento di tutti gli utenti esistenti |
| Data retention | Script di purge retroattivo + policy da comunicare agli utenti |
| Encryption at rest | Migrazione dati in produzione con downtime |

### Le 3 domande che il PRD deve rispondere

Prima di scrivere una singola riga di codice, il PRD deve rispondere a:

1. **Quali dati raccogliamo?** (categorie, sensibilità, obbligatorietà)
2. **Perché li raccogliamo?** (legal basis: contratto, consenso, legittimo interesse, obbligo legale)
3. **Per quanto li teniamo?** (data retention per tipo)

Se queste risposte non sono nel PRD, lo sviluppatore prende decisioni architetturali senza informazioni. E quelle decisioni costano.

---

## 2. GDPR — Obbligatorio per Qualsiasi SaaS che Processa Dati di Utenti EU

Il GDPR (General Data Protection Regulation) si applica a qualsiasi organizzazione che processa dati di persone fisiche residenti nell'Unione Europea, indipendentemente da dove ha sede l'azienda. Se il tuo SaaS ha un utente in Germania, il GDPR si applica.

### 2.1 Dati che Richiedono Protezione (Categorie)

**PII — Personally Identifiable Information**

Dati che identificano direttamente o indirettamente una persona fisica:

| Dato | Tipo | Note |
|---|---|---|
| Nome e cognome | Diretto | Anche solo nome se univoco nel contesto |
| Indirizzo email | Diretto | Anche alias come info@azienda.it |
| Numero di telefono | Diretto | |
| Indirizzo fisico | Diretto | |
| Indirizzo IP | Indiretto | Considerato PII dal GDPR — attenzione nei log |
| Device fingerprint | Indiretto | Combinazione user agent + screen + timezone |
| Cookie ID / session ID | Indiretto | Se usati per tracciamento utente |
| Username / handle | Indiretto | Se collegabile a identità reale |
| Dati di geolocalizzazione | Indiretto | Specialmente se precisi (<100m) |
| ID utente interno | Indiretto | Se mappabile a persona fisica |

**Dati Sensibili (Articolo 9 GDPR) — Trattamento Speciale**

Richiedono base legale esplicita (tipicamente: consenso esplicito o necessità vitale):

- Dati sanitari (diagnosi, farmaci, cartelle cliniche, parametri biometrici)
- Orientamento sessuale
- Opinioni politiche
- Credenze religiose o filosofiche
- Origine razziale o etnica
- Dati genetici o biometrici (scansioni del viso, impronte digitali)
- Appartenenza sindacale
- Condanne penali

**Regola**: Se il tuo SaaS anche solo _potrebbe_ raccogliere dati sensibili come side effect (es: un CRM dove l'utente scrive note sulla salute di un prospect), documentalo nel PRD e definisci come li gestisci.

**Dati Aziendali (B2B SaaS)**

In contesti B2B, i dati delle aziende clienti spesso contengono PII dei dipendenti di quell'azienda. Il fatto che l'interlocutore sia un'azienda non esonera dal GDPR se nel sistema ci finiscono dati di persone fisiche (lista contatti, email dipendenti, dati HR).

---

### 2.2 Requisiti Tecnici Obbligatori nel PRD

#### CONSENSO ESPLICITO

**Quando serve**: ogni volta che usi dati per uno scopo che non è strettamente necessario all'esecuzione del contratto.

Esempi: newsletter marketing, analytics comportamentale, condivisione con terze parti, retargeting pubblicitario.

**Come implementarlo nel PRD**:

```
User Story: Come utente, voglio poter scegliere per quali scopi i miei dati vengono usati,
in modo da avere controllo su ciò che mi viene inviato.

Acceptance Criteria:
- PASSA SE: al signup viene mostrata una lista di consensi separati e facoltativi (non un unico checkbox generico)
- PASSA SE: ogni consenso ha una descrizione leggibile di cosa comporta
- PASSA SE: il consenso è pre-deselezionato per impostazione predefinita (no dark patterns)
- PASSA SE: l'utente può modificare i consensi in qualsiasi momento dalla pagina Settings > Privacy
- PASSA SE: la data e versione del consenso è salvata nel DB per ogni utente
```

**Schema DB per il consenso**:
```sql
CREATE TABLE user_consents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  consent_type VARCHAR(50) NOT NULL, -- 'marketing_email', 'analytics', 'third_party_sharing'
  granted BOOLEAN NOT NULL,
  granted_at TIMESTAMPTZ,
  revoked_at TIMESTAMPTZ,
  consent_version VARCHAR(10) NOT NULL, -- '1.0', '2.1'
  ip_at_consent INET,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

#### RIGHT TO BE FORGOTTEN (Diritto alla Cancellazione)

**Scadenza**: entro 30 giorni dalla richiesta dell'utente.

**La sfida tecnica**: non puoi semplicemente fare `DELETE FROM users WHERE id = ?`. I dati dell'utente sono sparsi in decine di tabelle. Se hai FK senza cascade, la delete fallisce. Se hai backup automatici, i dati permangono lì.

**Come documentarlo nel PRD**:

```
Feature: Account Deletion + Data Erasure

Requisiti tecnici:
1. Hard delete vs Soft delete:
   - Default: soft delete (is_deleted = true, deleted_at = NOW())
   - GDPR request: hard delete completo (o anonymization irreversibile)
   
2. Cascade delete — tabelle da pulire (elenco esplicito nel PRD):
   - users → sessions, user_consents, user_settings, billing_details
   - Tabelle con FK verso users → CASCADE o SET NULL a seconda dei casi
   - Tabelle di audit log: anonimizzare (sostituire user_id con 'DELETED_USER')
   
3. Dati che NON vengono cancellati (eccezioni legali):
   - Fatture e transazioni finanziarie (obbligo fiscale 10 anni)
   - Log di sicurezza (potential fraud evidence — max 6 mesi)
   
4. Tempi:
   - Richiesta ricevuta → conferma email entro 24h
   - Cancellazione completata → entro 30 giorni
   - Notifica completamento all'utente → entro 48h dal completamento
   
5. Implementazione consigliata:
   - Endpoint: DELETE /api/user/me (richiede conferma password o MFA)
   - Job asincrono (queue) per il cascade delete
   - Audit entry: "USER_DELETION_REQUESTED" → "USER_DELETION_COMPLETED"
```

---

#### DATA PORTABILITY (Portabilità dei Dati)

L'utente ha diritto a ricevere i suoi dati in formato leggibile e machine-readable.

**Requisiti tecnici nel PRD**:

```
Feature: Data Export

Acceptance Criteria:
- PASSA SE: l'utente può richiedere l'export da Settings > Privacy > Export My Data
- PASSA SE: viene generato un file ZIP entro 24h dall'upload in un URL firmato
- PASSA SE: il file contiene: profilo utente (JSON), attività (CSV), contenuti creati (JSON/CSV)
- PASSA SE: il link scade dopo 7 giorni per sicurezza
- PASSA SE: viene inviata email con link al download

Formato minimo:
- profile.json → tutti i campi del profilo
- activity_log.csv → tutte le azioni dell'utente con timestamp
- [contenuto_principale].json → dati specifici del prodotto
```

---

#### DATA RETENTION POLICY

**Definizione nel PRD**: per ogni tipo di dato, quanti giorni/mesi/anni viene conservato e come viene cancellato.

**Template tabella da compilare nel PRD**:

| Tipo di Dato | Retention Period | Motivo | Metodo Cancellazione | Owner |
|---|---|---|---|---|
| Dati profilo utente | Vita account + 30 giorni | Contratto servizio | Hard delete + cascade | DB Admin |
| Log di accesso (IP, timestamp) | 90 giorni | Sicurezza | Auto-purge cron job | DevOps |
| Email di marketing | Vita account o fino a revoca consenso | Consenso | DELETE su revoca + account deletion | Marketing |
| Dati di pagamento (Stripe) | Gestito da Stripe | PCI DSS | Non memorizzati localmente | Stripe |
| Backup automatici | 30 giorni rolling | Business continuity | Rotazione automatica | DevOps |
| Dati analitici aggregati | Indefinito | Business analytics | N/A (anonimi) | Analytics |
| Cookie di sessione | 7 giorni (sliding) | UX | Scadenza automatica | Dev |
| Token di reset password | 1 ora | Sicurezza | Expire + delete on use | Dev |

---

#### PRIVACY BY DESIGN

Principi da applicare nell'architettura (documentali nel PRD):

**1. Row Level Security (RLS)**
In Supabase/PostgreSQL: ogni utente può accedere solo ai propri dati.
```sql
-- Esempio Supabase RLS
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can only see their own documents"
  ON documents FOR SELECT
  USING (auth.uid() = user_id);
```
Documentare nel PRD: "Tutte le tabelle con dati utente devono avere RLS abilitato. Nessuna query diretta al DB senza passare per l'auth layer."

**2. Data Minimization**
Principio: raccogli solo i dati che ti servono per lo scopo dichiarato.

PRD checkpoint: per ogni campo del form di signup, documenta:
- Perché è necessario
- Come viene usato
- Se può essere reso facoltativo

**3. Pseudonimizzazione**
Nei log e nei sistemi di analytics, sostituire l'email/nome con un ID interno non reversibile senza la chiave.

Esempio: nei log di PostHog o Mixpanel, passare `user_id` hash invece di email.

---

#### BREACH NOTIFICATION

Il GDPR impone notifica all'autorità (Garante Privacy in Italia) entro **72 ore** dalla scoperta di un data breach.

**Procedura da documentare nel PRD**:

```
Incident Response — Data Breach Protocol:

1. DETECTION (0-4h): 
   - Alert automatico se: accesso anomalo al DB, download massivo di dati, 
     accesso da IP sconosciuto con volume alto
   
2. ASSESSMENT (0-8h):
   - Quanti utenti coinvolti?
   - Quali dati esposti? (PII? Dati sensibili?)
   - È ancora in corso la violazione?
   
3. CONTAINMENT (0-12h):
   - Revocare access token compromessi
   - Bloccare IP/account sospetti
   - Snapshot del DB per analisi forensic
   
4. NOTIFICATION (entro 72h):
   - Se >250 utenti coinvolti → notifica Garante Privacy
   - Se rischio elevato per utenti → notifica diretta agli utenti coinvolti
   - Template notifica deve essere pronto PRIMA del lancio
   
5. DOCUMENTAZIONE:
   - Log dell'incidente (cosa/quando/chi/come)
   - Azioni correttive implementate
   - Registro violazioni interno (obbligatorio per legge)
```

---

### 2.3 Sezione Compliance Template — Blocco Pronto da Copiare nel PRD

```markdown
## 🔒 COMPLIANCE E DATA PRIVACY

### GDPR Status: OBBLIGATORIO (utenti EU)
**Data Protection Officer**: [nome o "da nominare se >250 dipendenti o trattamento su larga scala"]
**Legal Basis per tipo di trattamento**:
| Scopo | Base Legale | Note |
|---|---|---|
| Account e autenticazione | Esecuzione contratto (Art. 6.1.b) | Necessario per il servizio |
| Comunicazioni di servizio | Esecuzione contratto (Art. 6.1.b) | Notifiche critiche |
| Newsletter marketing | Consenso (Art. 6.1.a) | Opt-in esplicito richiesto |
| Analytics prodotto | Legittimo interesse (Art. 6.1.f) | Con opt-out disponibile |

### Diritti degli Utenti — Implementazione
| Diritto | Come viene soddisfatto | Tempo risposta | Owner |
|---|---|---|---|
| Accesso ai dati | Export automatico da Settings | Immediato (generazione <24h) | Dev |
| Rettifica | Modifica profilo in-app | Immediato | Dev |
| Cancellazione | Eliminazione account in Settings | Completata entro 30 giorni | Dev |
| Portabilità | ZIP export da Settings | <24h | Dev |
| Opposizione al trattamento | Revoca consensi da Settings > Privacy | Immediato | Dev |

### Data Retention Policy
| Tipo Dato | Retention | Metodo Cancellazione |
|---|---|---|
| [compilare per ogni categoria] | | |

### Audit Log Requirements
Azioni che devono essere loggiate obbligatoriamente:
- Login / Logout / Login fallito
- Modifica password o email
- Richiesta di export dati
- Richiesta di cancellazione account
- Modifica dei consensi privacy
- Accesso admin a dati utente

### Privacy by Design Checklist
- [ ] RLS abilitato su tutte le tabelle con dati utente
- [ ] Campi sensibili cifrati a livello applicativo (non solo DB encryption at rest)
- [ ] Log anonimizzati (nessuna PII nei log di sistema)
- [ ] Consensi separati e granulari nel signup flow
- [ ] Opt-out facilmente accessibile (non nascosto in Settings > Advanced > Privacy > Opt-out)
```

---

### 2.4 GDPR Checklist — 20 Punti per PRD Review

```
GDPR PRD REVIEW CHECKLIST

FONDAMENTALI
□ 1. È stata identificata la legal basis per ogni tipo di trattamento dati
□ 2. La privacy policy è linkata nel signup flow (non solo in footer)
□ 3. Il consenso marketing è separato dal consenso ai ToS
□ 4. I consensi sono pre-deselezionati per default
□ 5. È documentato un processo per ricevere e gestire richieste GDPR degli utenti

DATA ARCHITECTURE
□ 6. Ogni campo del DB ha una giustificazione ("perché raccogliamo questo dato?")
□ 7. È definita una retention policy per ogni tipo di dato
□ 8. Il cascade delete è documentato per tutte le tabelle collegate a user
□ 9. I log di sistema non contengono PII dirette (email, nome) ma solo ID interni
□ 10. RLS è pianificato per tutte le tabelle con dati utente

USER RIGHTS
□ 11. Il flusso "export my data" è progettato nel PRD
□ 12. Il flusso "delete my account" è progettato nel PRD (con hard delete GDPR)
□ 13. Il flusso "modifica consensi" è accessibile dall'utente senza contattare il supporto
□ 14. I tempi di risposta per le richieste sono documentati (max 30 giorni per cancellazione)

SICUREZZA
□ 15. I dati sensibili (password, payment) non sono mai in plaintext nel DB
□ 16. Le sessioni hanno un timeout ragionevole documentato
□ 17. I token di reset password hanno scadenza breve (<1h)
□ 18. Il breach notification protocol è documentato (entro 72h al Garante)

THIRD PARTIES
□ 19. Tutti i servizi terzi che ricevono dati utente sono elencati (Stripe, PostHog, SendGrid, etc.)
□ 20. Per ogni servizio terzo è verificata la conformità GDPR (Data Processing Agreement disponibile)
```

---

## 3. SOC 2 — Per SaaS B2B che Vende a Enterprise

SOC 2 (Service Organization Control 2) è uno standard di audit sviluppato dall'AICPA (American Institute of CPAs) per valutare la sicurezza dei sistemi di un'organizzazione che gestisce dati clienti.

**Non è una certificazione che si ottiene una volta sola.** È un report di audit che attesta il tuo stato di sicurezza in un determinato periodo.

### Cos'è — Trust Service Criteria

SOC 2 si basa su 5 Trust Service Criteria (TSC):

| Criterio | Cosa misura | Obbligatorio |
|---|---|---|
| **Security** (CC) | Protezione del sistema da accessi non autorizzati | SÌ — sempre |
| **Availability** (A) | Il sistema è disponibile come promesso nel SLA | Spesso richiesto |
| **Processing Integrity** (PI) | Il processing è completo, accurato e autorizzato | Per fintech/healthtech |
| **Confidentiality** (C) | I dati confidenziali sono protetti | Per B2B con dati strategici |
| **Privacy** (P) | Il trattamento dei dati personali rispetta i principi privacy | Se gestisci PII |

La maggior parte dei SaaS B2B fa SOC 2 Type II con focus su Security + Availability.

### Quando è Richiesto

SOC 2 non è obbligatorio per legge, ma diventa de facto obbligatorio in questi scenari:

- **Enterprise deals (>€50k ARR)**: il procurement del cliente richiede il SOC 2 report come prerequisito per firmare il contratto
- **Settore finance**: qualsiasi SaaS che tocca dati finanziari di istituti regolati
- **Settore healthcare**: partner di aziende sanitarie che richiedono garanzie oltre HIPAA
- **HR e payroll SaaS**: gestione dati dipendenti di grandi aziende
- **Settore governativo**: contratti con enti pubblici

**Regola pratica**: se vuoi vendere a un'azienda con >200 dipendenti nel settore finance, healthcare, o governo, preparati a fare SOC 2. Inizia almeno 12 mesi prima di quando ti serve il report.

### Requisiti Tecnici da Includere nel PRD

#### AUDIT LOGGING

Chi fa cosa quando. Questo è il cuore del SOC 2 dal punto di vista tecnico.

```
Requisito nel PRD:

Tutte le seguenti azioni devono generare un audit log entry:
- Accesso al sistema (login/logout)
- Modifiche a dati sensibili (update email, password, permessi)
- Accesso admin a dati clienti (impersonation, support access)
- Creazione/modifica/eliminazione di risorse critiche
- Export di dati
- Modifiche a configurazioni di sicurezza

Formato minimo audit log entry:
{
  "timestamp": "ISO 8601",
  "actor_id": "user o service account",
  "actor_role": "user | admin | system",
  "action": "RESOURCE_VERB (es: USER_PASSWORD_CHANGED)",
  "resource_type": "user | document | setting",
  "resource_id": "UUID",
  "ip_address": "IPv4/IPv6",
  "user_agent": "stringa",
  "result": "success | failure",
  "metadata": {} -- dati contestuali action-specific
}

Retention: audit log conservati 12 mesi minimi (SOC 2 standard).
Tamper-proof: i log non devono essere modificabili da admin normali.
```

#### ACCESS CONTROL — LEAST PRIVILEGE

Ogni utente/sistema accede solo a ciò di cui ha bisogno, niente di più.

**Requisiti da documentare nel PRD**:

```
IAM (Identity and Access Management) Requirements:

1. Ruoli e permessi:
   - Definire esplicitamente tutti i ruoli del sistema (admin, editor, viewer, etc.)
   - Ogni ruolo ha una lista esplicita di permessi (non "eredita tutto tranne X")
   - La matrice ruoli × permessi deve essere nel PRD
   
2. Admin access:
   - Gli accessi admin ai dati clienti devono essere loggati
   - Accesso "break glass" (emergenza) deve richiedere approvazione secondaria
   - Nessun admin ha accesso illimitato permanente — access review trimestrale
   
3. Service accounts:
   - Ogni integrazione (Stripe webhook, cron job) ha il proprio account con permessi minimi
   - Nessun service account condivide credenziali con account umani
   - Rotazione automatica delle API key ogni 90 giorni
   
4. MFA:
   - MFA obbligatorio per tutti gli account admin
   - MFA disponibile (e raccomandato) per tutti gli utenti
```

#### ENCRYPTION AT REST E IN TRANSIT

```
Requisiti nel PRD:

In Transit:
- TLS 1.2 minimo (TLS 1.3 raccomandato) per tutto il traffico
- HSTS header su tutti i domini
- Certificati rinnovati automaticamente (Let's Encrypt o equivalente)
- Nessun fallback a HTTP non cifrato

At Rest:
- DB: AES-256 (standard di tutti i managed DB cloud — documenta quale provider usi)
- File storage: AES-256 (S3 default encryption o equivalente)
- Backup: cifrati con la stessa policy del DB
- Dati particolarmente sensibili (es: API key salvate per conto dell'utente):
  cifratura a livello applicativo con chiave separata dalla chiave del DB
  
Gestione chiavi:
- Le chiavi di cifratura NON sono hardcoded nel codice
- Gestite tramite: AWS KMS / HashiCorp Vault / Doppler Secrets / [altro]
- Rotazione delle chiavi documentata
```

#### PENETRATION TESTING SCHEDULE

```
Requisito nel PRD:

- Penetration test esterno annuale (da registrare e documentare per SOC 2)
- Vulnerability scanning automatico (strumenti: Snyk, Dependabot, GitHub Security)
- OWASP Top 10 review prima di ogni major release
- Bug bounty program (opzionale ma apprezzato dai reviewer SOC 2)

Finding management:
- Critical: patch entro 24h
- High: patch entro 7 giorni
- Medium: patch entro 30 giorni
- Low: backlog con prioritizzazione trimestrale
```

#### INCIDENT RESPONSE PLAN

```
Da documentare nel PRD (o in documento collegato referenziato nel PRD):

1. Detection: come rileviamo un incidente (alerting, monitoring)
2. Classification: severity 1-4 con definizioni chiare
3. Response team: chi viene contattato per ogni severity
4. Communication: template per notifiche interne e verso clienti
5. Recovery: backup restore procedure, RTO/RPO documentati
6. Post-mortem: formato standard per analisi post-incidente
7. Evidence preservation: come preserviamo log e prove per eventuali audit
```

### Type I vs Type II — Differenza Pratica

| Tipo | Cosa attesta | Durata | Costo stimato | Quando usarlo |
|---|---|---|---|---|
| **SOC 2 Type I** | Controlli sono PROGETTATI correttamente a un certo momento | Point-in-time | €15k-30k | Prima milestone — "abbiamo i controlli" |
| **SOC 2 Type II** | Controlli hanno FUNZIONATO per un periodo (tipicamente 6-12 mesi) | Rolling period | €25k-60k | Richiesto per enterprise deals seri |

**Timeline realistica per SOC 2 Type II**:
- Mese 1-2: Gap assessment e implementazione controlli mancanti
- Mese 3-14: Observation period (i controlli devono funzionare per almeno 6 mesi)
- Mese 15-17: Audit con firma del CPA
- Mese 18: Report disponibile

---

## 4. HIPAA — Per SaaS con Dati Medici

### PHI — Protected Health Information

HIPAA definisce PHI (Protected Health Information) come qualsiasi informazione che:
1. Riguarda lo stato di salute, la fornitura di servizi sanitari o il pagamento di questi
2. **E** può essere associata a un individuo specifico

Esempi di PHI: cartelle cliniche, diagnosi, prescrizioni, risultati di laboratorio, immagini mediche, dati di wearable sanitari se associati a identità.

**Regola dei 18 identificatori**: anche dati non ovviamente medici diventano PHI se combinati con dati sanitari. Nome + diagnosi = PHI. IP + visite a pagine mediche = potenziale PHI.

### Business Associate Agreement (BAA)

Se il tuo SaaS gestisce PHI per conto di una covered entity (ospedale, studio medico, laboratorio), devi firmare un **Business Associate Agreement (BAA)** con ognuna di esse.

Il BAA definisce:
- Come puoi usare la PHI (solo per fornire il servizio)
- Come la proteggi
- Cosa fai in caso di breach
- Come la elimini al termine del contratto

**Implicazione PRD**: se stai costruendo un SaaS healthtech, documenta esplicitamente se sei un Business Associate e con quali covered entities hai BAA in essere.

### Requisiti Tecnici Mandatori

**Audit Trail**
Ogni accesso a PHI deve essere loggato: chi ha acceduto, quando, a quali dati. Non opzionale.

**Automatic Logoff**
Le sessioni con accesso a PHI devono scadere automaticamente dopo inattività. Standard comune: 15 minuti per accesso web, 30 minuti per applicazioni desktop. Documentare nel PRD il timeout scelto e la giustificazione.

**Encryption Mandatorio**
Diversamente da altri standard dove la crittografia è "best practice", per HIPAA è mandatoria:
- PHI in transito: TLS 1.2+ obbligatorio
- PHI a riposo: AES-128 minimo (AES-256 raccomandato)
- PHI su dispositivi mobili: cifratura del dispositivo + wipe remoto

**Emergency Access Procedure**
Documentare come si accede ai dati in emergenza (es: accesso break-glass) mantenendo la traccia.

### Nota Critica

Non affrontare lo sviluppo di un SaaS HIPAA-compliant senza un consulente legale specializzato in healthcare compliance. Le sanzioni per violazione HIPAA vanno da $100 a $50.000 per singola violazione, con massimale annuale di $1.9M. Le violazioni con negligenza dolosa iniziano da $50.000 a violazione.

**Nel PRD**: se il prodotto gestisce PHI, aggiungere una nota esplicita:
```
⚠️ HIPAA COMPLIANCE NOTE
Questo prodotto gestisce Protected Health Information (PHI).
Prima di procedere allo sviluppo:
1. Review legale con consulente HIPAA specializzato
2. BAA firmato con tutte le covered entities
3. Risk Assessment formale (richiesto da HIPAA Security Rule)
4. HIPAA-compliant infrastructure (AWS HIPAA BAA, o equivalente)
```

---

## 5. GDPR + Cookie Compliance

### Analytics: Come Implementare Consent-Aware

Il problema con Google Analytics 4 standard: raccoglie IP e device data prima del consenso. In EU è illegale.

**Soluzioni conformi**:

**Opzione A — PostHog Self-Hosted**
```
Vantaggio: nessun dato lascia la tua infrastruttura EU.
Setup nel PRD:
- Self-hosted su VPS EU (Hetzner, OVH, etc.)
- IP anonimizzato abilitato
- Session recording: solo con consenso esplicito
- Feature flags e analytics: OK senza consenso perché no PII
```

**Opzione B — PostHog Cloud EU Region**
```
Dati memorizzati in EU.
Setup nel PRD:
- Inizializzare PostHog DOPO il consenso analytics
- Passare distinct_id = hash dell'user_id (non email)
- Disabilitare session recording di default
```

**Opzione C — Plausible Analytics**
```
Privacy-first by design. Nessun cookie, nessun PII.
Non richiede banner cookie per analytics di base.
Limitazione: meno dettaglio per analisi avanzate.
```

**Implementazione consent-aware nel codice (da specificare nel PRD come requisito)**:
```javascript
// Pattern corretto: analytics si inizializza solo dopo il consenso
const initAnalytics = (consentGiven) => {
  if (!consentGiven) return;
  posthog.init(POSTHOG_KEY, {
    api_host: 'https://analytics.tuodominio.com',
    loaded: (posthog) => {
      if (user) posthog.identify(hashUserId(user.id)); // MAI email diretta
    }
  });
};
```

### Cookie Banner — Requisiti Tecnici

**Requisiti del banner per conformità GDPR/eprivacy italiana (Garante 2021)**:

```
Cookie Banner Requirements nel PRD:

1. Struttura:
   - Primo layer: descrizione sintetica + bottoni "Accetta tutti" / "Rifiuta tutti" / "Personalizza"
   - Secondo layer (personalizza): lista categorie con toggle per ognuna
   - NON usare dark patterns (es: "Accetta tutto" in verde prominente, "Rifiuta" in grigio piccolo)
   
2. Categorie standard:
   - Necessari (non togglable — sempre attivi)
   - Analytics / Performance
   - Marketing / Targeting
   - Funzionali / Preferenze
   
3. Comportamento tecnico:
   - Nessun cookie non-necessario viene settato PRIMA del consenso
   - Il consenso viene salvato in localStorage o cookie first-party
   - Il banner riappare se la policy cambia (versionamento del consenso)
   - L'utente può cambiare preferenze in qualsiasi momento (link nel footer)
   
4. Documentazione nel PRD:
   - Lista di tutti i cookie usati per categoria
   - Durata di ogni cookie
   - Prima o terza parte
   - Scopo specifico
```

**Esempio tabella cookie da includere nel PRD**:

| Cookie | Categoria | Durata | Prima/Terza parte | Scopo |
|---|---|---|---|---|
| session_id | Necessario | Sessione | Prima | Autenticazione |
| csrf_token | Necessario | Sessione | Prima | Sicurezza CSRF |
| consent_v2 | Necessario | 12 mesi | Prima | Memorizza scelte privacy |
| _posthog | Analytics | 1 anno | Prima (self-hosted) | Analytics prodotto |
| stripe_mid | Necessario | 12 mesi | Terza (Stripe) | Prevenzione frode pagamenti |

---

## 6. Template Sezione Compliance Completo per PRD

```markdown
## 🔒 COMPLIANCE E DATA PRIVACY

### Applicabilità
- [x] GDPR — utenti/dati EU (obbligatorio)
- [ ] SOC 2 — target enterprise B2B (pianificato per Fase 2 / data: ___)
- [ ] HIPAA — dati medici (non applicabile / applicabile)

---

### GDPR — Legal Basis per Tipo di Trattamento
| Scopo del Trattamento | Base Legale | Dati Coinvolti |
|---|---|---|
| Erogazione del servizio | Contratto (Art. 6.1.b) | Email, profilo, dati di utilizzo |
| Fatturazione | Obbligo legale (Art. 6.1.c) | Dati fiscali, storico pagamenti |
| Newsletter | Consenso (Art. 6.1.a) | Email |
| Analytics prodotto | Legittimo interesse (Art. 6.1.f) | Dati comportamentali anonimizzati |

---

### Data Retention Policy
| Tipo di Dato | Retention Period | Metodo di Cancellazione | Eccezioni |
|---|---|---|---|
| Dati profilo | Vita account + 30gg | Hard delete + cascade | — |
| Log di accesso | 90 giorni | Cron job purge | — |
| Fatture | 10 anni | Archiviazione read-only | Obbligo fiscale |
| Email log | 30 giorni | Auto-purge | — |
| Analytics aggregati | Indefinito | N/A — dati anonimi | — |
| Backup | 30 giorni rolling | Rotazione automatica | — |

---

### Audit Log Requirements
**Tabella eventi da loggare:**

| Evento | Chi | Quando | Dati nel Log | Retention |
|---|---|---|---|---|
| Login riuscito | Tutti | Ad ogni accesso | user_id, IP, timestamp, device | 90gg |
| Login fallito | Tutti | Ad ogni tentativo | IP, timestamp, email tentata | 90gg |
| Password change | Utente | Al cambio | user_id, IP, timestamp | 12 mesi |
| Data export richiesto | Utente | Alla richiesta | user_id, timestamp | 12 mesi |
| Account deletion | Utente | Alla richiesta | user_id, timestamp, motivo | 12 mesi |
| Admin data access | Admin | Ad ogni accesso | admin_id, user_id target, motivo | 12 mesi |
| Consent change | Utente | Ad ogni modifica | user_id, consent_type, old_val, new_val | Vita account |

---

### Cookie Policy
**Lista cookie per categoria:**

| Cookie | Categoria | Durata | Descrizione |
|---|---|---|---|
| [compilare] | | | |

**Implementazione banner**: [strumento scelto — es: Cookiebot, CookieYes, custom]

---

### User Rights Implementation
| Diritto GDPR | Endpoint / UI | Tempo Risposta | Automatico? |
|---|---|---|---|
| Accesso (Art. 15) | Settings > Export My Data | <24h | Sì |
| Rettifica (Art. 16) | Settings > Profile | Immediato | Sì |
| Cancellazione (Art. 17) | Settings > Account > Delete Account | <30 giorni | Parzialmente |
| Portabilità (Art. 20) | Settings > Export My Data | <24h | Sì |
| Opposizione (Art. 21) | Settings > Privacy > Consensi | Immediato | Sì |

---

### Breach Notification Protocol
- Responsabile: [nome/ruolo]
- Canale di detection: [monitoring tool]
- Soglia per notifica Garante: >250 utenti coinvolti O rischio elevato per gli individui
- Template notifica Garante: [link a documento interno]
- Template notifica utenti: [link a documento interno]
- Tempo massimo: **72 ore dal momento della scoperta**

---

### Third-Party Data Processors
| Fornitore | Scopo | Dati Trasmessi | GDPR Compliance | Link DPA |
|---|---|---|---|---|
| Stripe | Pagamenti | Email, nome, dati pagamento | Sì (DPA disponibile) | [link] |
| PostHog | Analytics | user_id hash, eventi | Sì (EU hosting) | [link] |
| SendGrid | Email transazionali | Email, nome | Sì (DPA disponibile) | [link] |
| Supabase | Database/Auth | Tutti i dati utente | Sì (EU region) | [link] |
```

---

## Quick Reference: Quale Standard per Quale Prodotto

| Tipo di SaaS | Standard Applicabile | Priorità |
|---|---|---|
| B2C qualsiasi con utenti EU | GDPR | Obbligatorio al lancio |
| B2B SMB | GDPR | Obbligatorio al lancio |
| B2B enterprise | GDPR + SOC 2 | GDPR al lancio, SOC 2 entro anno 1-2 |
| Healthtech / medical data | GDPR + HIPAA | Entrambi obbligatori prima del lancio |
| Fintech / banking data | GDPR + SOC 2 + PCI DSS | Consulenza specializzata necessaria |
| HR / payroll SaaS | GDPR + SOC 2 | GDPR al lancio, SOC 2 richiesto presto |
| EdTech (minori <16 anni) | GDPR + COPPA | Attenzione: consenso genitoriale richiesto |
