# REF_14 — Analytics Events Library
## Libreria Completa di Analytics Events per SaaS B2B e B2C

Questa libreria contiene oltre 120 eventi analytics pre-definiti, categorizzati per dominio, con proprietà, tipi di dato e note implementative. Usala come riferimento quando costruisci la sezione Analytics Events di un PRD.

**Tool di riferimento**: PostHog, Mixpanel, Amplitude, Segment, GA4
**Naming convention**: `snake_case` per tutti i nomi di eventi e proprietà
**Standard**: segue le specifiche Segment Spec dove applicabile

---

## CATEGORIA 1 — Authentication & Registration

### `user_signed_up`
```javascript
analytics.track('user_signed_up', {
  method: 'google' | 'github' | 'email' | 'magic_link',
  referral_source: string | null,     // utm_source o referrer
  invite_code: string | null,          // se da invito
  plan_at_signup: 'free' | 'trial' | 'paid',
  experiment_variant: string | null,   // se A/B test attivo
  timestamp: ISO8601
});
```
**Trigger**: completamento signup form + conferma email
**Non triggerare**: a ogni page reload / a ogni visita

---

### `user_signed_in`
```javascript
analytics.track('user_signed_in', {
  method: 'google' | 'github' | 'email' | 'magic_link' | 'sso',
  session_count: number,               // numero di sessioni totali
  days_since_last_login: number,
  is_mobile: boolean
});
```

---

### `user_signed_out`
```javascript
analytics.track('user_signed_out', {
  session_duration_minutes: number,
  actions_in_session: number           // proxy di engagement
});
```

---

### `password_reset_requested`
```javascript
analytics.track('password_reset_requested', {
  method: 'email_link' | 'sms'
});
```

---

### `email_verified`
```javascript
analytics.track('email_verified', {
  time_to_verify_hours: number,        // ore tra signup e verifica
  verification_attempt_count: number
});
```

---

## CATEGORIA 2 — Onboarding

### `onboarding_started`
```javascript
analytics.track('onboarding_started', {
  onboarding_version: string,          // es: 'v2' — per A/B test flussi
  total_steps: number
});
```

---

### `onboarding_step_completed`
```javascript
analytics.track('onboarding_step_completed', {
  step_number: number,
  step_name: string,                   // es: 'profile_setup', 'invite_team'
  time_spent_seconds: number,
  was_skipped: boolean
});
```

---

### `onboarding_completed`
```javascript
analytics.track('onboarding_completed', {
  steps_completed: number,
  steps_skipped: number,
  total_time_minutes: number,
  invited_team_members: boolean
});
```
**Metrica critica**: completion rate = onboarding_completed / onboarding_started

---

### `onboarding_abandoned`
```javascript
analytics.track('onboarding_abandoned', {
  last_step_reached: number,
  last_step_name: string,
  time_spent_before_abandon_minutes: number
});
```

---

### `first_action_completed`
```javascript
analytics.track('first_action_completed', {
  action_type: string,                 // es: 'first_project_created'
  time_since_signup_hours: number,
  completed_onboarding_first: boolean
});
```
**Note**: questo evento definisce il "activation" del prodotto. Definitelo con cura.

---

## CATEGORIA 3 — Core Product Usage

### Pattern generico per azioni CRUD

```javascript
// CREATE
analytics.track('[entity]_created', {
  entity_id: string,
  entity_type: string | null,          // se ci sono tipi diversi
  creation_method: 'manual' | 'template' | 'import' | 'duplicate',
  workspace_id: string,
  user_role: 'owner' | 'admin' | 'member' | 'viewer'
});

// UPDATED
analytics.track('[entity]_updated', {
  entity_id: string,
  fields_changed: string[],            // es: ['name', 'status', 'assignee']
  update_source: 'ui' | 'api' | 'automation'
});

// DELETED
analytics.track('[entity]_deleted', {
  entity_id: string,
  entity_age_days: number,
  was_soft_deleted: boolean,
  reason: string | null               // se mostri dialog con reason
});

// VIEWED
analytics.track('[entity]_viewed', {
  entity_id: string,
  view_source: 'list' | 'search' | 'notification' | 'direct_link',
  load_time_ms: number
});
```

---

### `search_performed`
```javascript
analytics.track('search_performed', {
  query_length: number,                // NON loggare la query per privacy
  results_count: number,
  search_type: 'global' | 'scoped' | 'filter',
  result_clicked: boolean,
  time_to_first_click_ms: number | null
});
```
**Nota Privacy**: MAI loggare il testo della query — usa solo metriche aggregate

---

### `filter_applied`
```javascript
analytics.track('filter_applied', {
  filter_type: string,                 // es: 'status', 'date_range', 'assignee'
  filter_count: number,                // quanti filtri attivi totali
  results_count: number
});
```

---

### `export_initiated`
```javascript
analytics.track('export_initiated', {
  format: 'csv' | 'xlsx' | 'pdf' | 'json',
  record_count: number,
  date_range_days: number | null
});
```

---

### `import_completed`
```javascript
analytics.track('import_completed', {
  format: 'csv' | 'xlsx' | 'api' | 'zapier',
  records_imported: number,
  records_failed: number,
  duration_seconds: number
});
```

---

## CATEGORIA 4 — Collaboration & Team

### `team_member_invited`
```javascript
analytics.track('team_member_invited', {
  invitee_role: 'admin' | 'member' | 'viewer',
  invitation_method: 'email' | 'link' | 'bulk_csv',
  team_size_before: number
});
```

---

### `team_member_joined`
```javascript
analytics.track('team_member_joined', {
  via_invite: boolean,
  time_from_invite_hours: number | null,
  role_assigned: string
});
```

---

### `comment_added`
```javascript
analytics.track('comment_added', {
  entity_type: string,
  entity_id: string,
  comment_length_chars: number,
  has_mention: boolean,
  has_attachment: boolean
});
```

---

### `mention_created`
```javascript
analytics.track('mention_created', {
  mention_type: 'user' | 'team',
  entity_type: string,
  is_in_comment: boolean
});
```

---

## CATEGORIA 5 — Subscription & Billing

### `plan_upgrade_started`
```javascript
analytics.track('plan_upgrade_started', {
  from_plan: string,
  to_plan: string,
  trigger: 'paywall' | 'settings' | 'feature_gate' | 'cta_banner',
  feature_that_triggered: string | null
});
```

---

### `plan_upgrade_completed`
```javascript
analytics.track('plan_upgrade_completed', {
  from_plan: string,
  to_plan: string,
  billing_cycle: 'monthly' | 'annual',
  mrr_change: number,
  payment_method: 'card' | 'paypal' | 'invoice',
  coupon_used: boolean
});
```
**Metrica critica**: conversion rate = upgrade_completed / upgrade_started

---

### `plan_downgrade_initiated`
```javascript
analytics.track('plan_downgrade_initiated', {
  from_plan: string,
  to_plan: string,
  reason_selected: string | null,      // da churn survey
  cancel_flow_step: string
});
```

---

### `subscription_cancelled`
```javascript
analytics.track('subscription_cancelled', {
  plan: string,
  tenure_months: number,
  reason: string,                      // da exit survey obbligatoria
  reactivation_offered: boolean,
  reactivation_accepted: boolean
});
```

---

### `payment_failed`
```javascript
analytics.track('payment_failed', {
  failure_reason: 'card_declined' | 'insufficient_funds' | 'expired' | 'other',
  retry_number: number,
  recovery_email_sent: boolean
});
```

---

### `feature_gate_hit`
```javascript
analytics.track('feature_gate_hit', {
  feature_name: string,
  user_plan: string,
  gate_type: 'hard_block' | 'soft_limit' | 'usage_cap',
  upsell_shown: boolean
});
```
**Insight**: gli eventi feature_gate_hit più frequenti indicano le feature da promuovere nell'upgrade flow

---

## CATEGORIA 6 — Notifications & Communication

### `notification_received`
```javascript
analytics.track('notification_received', {
  notification_type: string,
  channel: 'in_app' | 'email' | 'push' | 'slack',
  is_read: boolean
});
```

---

### `notification_clicked`
```javascript
analytics.track('notification_clicked', {
  notification_type: string,
  channel: string,
  time_to_click_minutes: number
});
```

---

### `email_opened` (solo con email tracking)
```javascript
analytics.track('email_opened', {
  email_type: string,                  // es: 'weekly_digest', 'invite', 'trial_expiry'
  days_since_sent: number,
  device_type: 'mobile' | 'desktop'
});
```

---

### `notification_preference_changed`
```javascript
analytics.track('notification_preference_changed', {
  channel: string,
  notification_type: string,
  action: 'enabled' | 'disabled'
});
```

---

## CATEGORIA 7 — Performance & Errors (automatici)

### `page_load_time` (automatico)
```javascript
analytics.track('page_load_time', {
  page: string,
  load_time_ms: number,
  connection_type: '4g' | '3g' | 'wifi' | 'offline',
  first_contentful_paint_ms: number,
  largest_contentful_paint_ms: number
});
```

---

### `error_encountered`
```javascript
analytics.track('error_encountered', {
  error_code: string,
  error_message: string,               // messaggio mostrato all'utente (non stack trace)
  page: string,
  action_attempted: string,
  was_recoverable: boolean
});
```

---

### `api_error` (lato server, non lato client)
```javascript
// Log strutturato, NON analytics event
logger.error('api_error', {
  endpoint: string,
  method: string,
  status_code: number,
  error_type: string,
  user_id: string | null,
  duration_ms: number
});
```

---

## CATEGORIA 8 — Integrations & API

### `integration_connected`
```javascript
analytics.track('integration_connected', {
  integration_name: string,            // es: 'slack', 'zapier', 'google_sheets'
  connection_method: 'oauth' | 'api_key' | 'webhook',
  workspace_id: string
});
```

---

### `api_key_created`
```javascript
analytics.track('api_key_created', {
  key_permissions: string[],
  expires_in_days: number | null
});
```

---

### `webhook_triggered`
```javascript
analytics.track('webhook_triggered', {
  event_type: string,
  destination_url_domain: string,      // solo dominio, non URL completa
  success: boolean,
  response_time_ms: number
});
```

---

## CATEGORIA 9 — Mobile-Specific

### `app_foregrounded`
```javascript
analytics.track('app_foregrounded', {
  session_number: number,
  days_since_install: number,
  notification_opened: boolean         // se aperto da notifica push
});
```

---

### `push_notification_received`
```javascript
analytics.track('push_notification_received', {
  notification_type: string,
  app_state: 'foreground' | 'background' | 'killed'
});
```

---

### `app_crash` (automatico via Sentry/Crashlytics)
```javascript
// Non implementare manualmente — usa Sentry o Crashlytics
{
  error: string,
  stack_trace: string,
  app_version: string,
  os_version: string,
  device_model: string
}
```

---

## Regole di Implementazione

### Naming Convention
```
✅ user_signed_up          (snake_case, passato, oggetto_verbo)
✅ project_created         (entità prima, azione dopo)
✅ payment_failed          (chiaro e specifico)

❌ UserSignedUp            (PascalCase — non usare)
❌ signup                  (troppo generico)
❌ trackUserSignup         (prefisso track — ridondante)
❌ user_did_sign_up        (verboso)
```

### Properties da includere SEMPRE
Queste properties vanno su OGNI evento, tipicamente come super properties:
```javascript
// Imposta come super properties in Mixpanel/PostHog
analytics.register({
  user_id: string,
  workspace_id: string | null,
  plan: string,
  app_version: string,
  platform: 'web' | 'ios' | 'android',
  environment: 'production' | 'staging'  // per filtrare nei report
});
```

### Properties da NON includere MAI
```
❌ password (ovvio)
❌ full_name (PII — usa user_id)
❌ email (PII — usa user_id)
❌ credit_card_last4 (PCI)
❌ full_query_text (privacy — usa query_length)
❌ file_content (privacy)
❌ ip_address (GDPR — usa geo_country max)
```

### Volume guidelines
- **Troppi eventi**: se superi 200 eventi distinti → consolidare
- **Troppo pochi**: se hai <20 eventi → stai perdendo insights critici
- **Regola 80/20**: 20 eventi core coprono 80% degli insights — parti da lì

---

## Template Quick Start (minimo per MVP)

Questi 12 eventi coprono il funnel critico di qualsiasi SaaS:

```javascript
// ACQUISITION
analytics.track('user_signed_up', { method, referral_source })
analytics.track('email_verified', { time_to_verify_hours })

// ACTIVATION
analytics.track('onboarding_completed', { steps_completed, total_time_minutes })
analytics.track('first_action_completed', { action_type, time_since_signup_hours })

// ENGAGEMENT
analytics.track('[core_entity]_created', { entity_id, creation_method })
analytics.track('search_performed', { results_count, result_clicked })

// RETENTION
analytics.track('user_signed_in', { days_since_last_login })
analytics.track('feature_gate_hit', { feature_name, gate_type })

// REVENUE
analytics.track('plan_upgrade_started', { from_plan, to_plan, trigger })
analytics.track('plan_upgrade_completed', { from_plan, to_plan, billing_cycle })
analytics.track('subscription_cancelled', { reason, tenure_months })

// ERRORS
analytics.track('error_encountered', { error_code, page, was_recoverable })
```

Implementa questi 12 prima di tutto il resto. Aggiungi altri in base ai gap di insight specifici.
