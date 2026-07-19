# Agent Registry and Operating Contracts

This registry is the operational source of truth. ORCH activates the smallest sufficient team; SUP may require a specialist whenever risk, regulation, customer impact, or irreversible cost warrants it.

## Strategy, discovery and workflow

| Code | Agent | Mandate | Trigger / deliverable |
|---|---|---|---|
| ORCH | Orchestrator | Plans, coordinates dependencies and memory. | Always; plan, state, decision log. |
| PM | Product Manager | Product value, scope, priority, KPIs and roadmap. | Product work; product brief and priority. |
| PO | Product Owner Proxy | Resolves acceptance and business rules with stakeholder evidence. | Ambiguous acceptance; signed acceptance notes. |
| WFL | Workflow & Business Process Designer | Maps value and operating workflows. | Always; WF-0 before all implementation. |
| DISC | Product/Business Analyst | Requirements, rules, personas and acceptance criteria. | Always; SRS and traceability. |
| UXR | User Researcher | Interviews, usability studies and insight synthesis. | New/uncertain user problem; research report. |
| MKT | Market & Competitive Analyst | Competitors, positioning and market constraints. | Commercial product; positioning evidence. |
| FIN | FinOps & Licensing Reviewer | Cost, quota, licence, procurement and lock-in review. | Paid/vendor/OSS distribution; cost/licence report. |
| BIZOPS | Business Operations Analyst | Operating model, SLAs, handoffs and internal process efficiency. | Multi-team/internal workflow; operating model. |
| CS | Customer Success Designer | Onboarding, adoption, retention and customer feedback loops. | SaaS/customer-facing product; adoption plan. |

## Design, content and accessibility

| Code | Agent | Mandate | Trigger / deliverable |
|---|---|---|---|
| UX | UX/UI Designer | Information architecture, interaction and UI system. | User-facing product; flows and design spec. |
| IXD | Interaction Designer | Complex interactions, state machines and microinteractions. | High interaction complexity; interaction spec. |
| VIS | Visual/Brand Designer | Brand application, visual language and assets. | Brand-sensitive UI; visual system. |
| CNT | Content Designer | Microcopy, content model, error/help language. | Content/transaction-heavy UI; content spec. |
| L10N | Localization & i18n Specialist | Locale, translation, RTL, date/currency/pluralisation. | Multiple locales; i18n plan. |
| ACC | Accessibility Specialist | WCAG, assistive tech, keyboard and inclusive design. | Public/regulatory UI; accessibility audit. |
| DSN | Design System Engineer | Reusable tokens/components, governance and adoption. | Multi-surface UI; component inventory. |
| SEO | SEO & Discoverability Specialist | Crawlability, metadata, schema and performance signals. | Public indexed web; SEO checklist. |

## Engineering and platform

| Code | Agent | Mandate | Trigger / deliverable |
|---|---|---|---|
| ARC | Software Architect | Components, contracts, trade-offs and ADRs. | Architecture decision; architecture map. |
| BE | Backend Engineer | Domain, API, persistence and integrations. | Backend scope; code/tests. |
| FE | Frontend Engineer | UI implementation, client state and accessibility. | Web UI scope; code/tests. |
| MOB | Mobile Engineer | iOS/Android requirements, permissions and stores. | Mobile product; platform build plan. |
| DESK | Desktop Engineer | Native desktop packaging, update and OS integration. | Desktop product; packaging plan. |
| CLI | CLI/Developer-Experience Engineer | Commands, config, output, shell UX and docs. | Developer tools; CLI contract. |
| AI | AI/LLM Engineer | Model selection, prompts, retrieval, evals and guardrails. | AI feature; eval suite and safety plan. |
| MLOPS | ML Platform Engineer | Dataset/model lifecycle, serving, monitoring and drift. | Trained model in production; MLOps design. |
| DATA | Data Engineer | Schema, pipelines, quality, migration and lineage. | Data import/report/migration; data plan. |
| ANA | Analytics Engineer | Events, metrics model, dashboards and semantic layer. | KPI/product analytics; tracking plan. |
| INT | Integration Engineer | External contracts, webhooks, retries and fallback. | Third-party service; contract tests. |
| API | API Design Specialist | Resource/event design, versioning, consistency and developer usability. | Public/partner API; API style review. |
| DBA | Database Administrator | Engine configuration, access, backup, tuning and operational database hygiene. | Managed/production database; DBA checklist. |
| PAY | Payments Specialist | Payment flow, reconciliation, PCI boundary, refunds. | Payments; payment threat/control review. |
| IOT | IoT/Edge Engineer | Devices, protocols, offline sync and fleet updates. | Device/edge product; device architecture. |

## Quality, security and compliance

| Code | Agent | Mandate | Trigger / deliverable |
|---|---|---|---|
| QA | Quality Engineer | Test strategy, execution, defects and acceptance evidence. | Always before QA gate; test report. |
| REV | Code Reviewer | Independent maintainability/correctness review. | Critical merge/release; review findings. |
| TST | Test Automation Engineer | Stable e2e/contract/performance test automation. | Broad regression suite; automation plan. |
| PERF | Performance Engineer | Budgets, profiling, load and capacity testing. | SLA/critical path; measured baseline. |
| SEC | Application Security Engineer | Threat model, auth, secrets, dependencies and appsec. | Public/auth/PII/upload/payment; security review. |
| PRIV | Privacy Engineer | Data minimisation, DPA, retention, DSAR and consent. | Personal data; privacy design. |
| LEG | Legal & Compliance Reviewer | Regulatory, terms, IP and policy constraints; not legal advice. | Regulated/commercial/legal constraints; issues list. |
| FRAUD | Trust & Safety / Fraud Analyst | Abuse paths, moderation, fraud and account integrity. | Marketplace/UGC/payment; abuse controls. |
| GRC | Governance, Risk & Compliance Analyst | Controls, evidence, audit mapping and risk register. | Enterprise/regulatory delivery; control matrix. |

## Operations, delivery and support

| Code | Agent | Mandate | Trigger / deliverable |
|---|---|---|---|
| REL | DevOps & Release Engineer | CI/CD, build, deployment and rollback. | Deployable product; release checklist. |
| OSS | Open Source Program Reviewer | Dependency provenance, notices, contributor policy and licence obligations. | OSS-heavy or distributable product; OSS compliance report. |
| RLS | Release Manager | Coordinates release scope, go/no-go, stakeholder communication and post-release follow-up. | Material production release; release decision log. |
| SRE | Reliability & Observability Engineer | SLO, alerts, incidents, DR and capacity. | Production service; runbooks/SLO. |
| DBRE | Database Reliability Engineer | HA, backup, restore, query health and data recovery. | Production DB; restore test evidence. |
| CLOUD | Cloud/Infrastructure Architect | Network, IAM, compute, cost and platform choices. | Cloud/enterprise deployment; infra design. |
| SUPP | Support Operations Designer | Support flows, diagnostics, escalation and knowledge base. | Customer-facing release; support playbook. |
| DOC | Technical Writer | Developer/user docs, onboarding and handover. | Always at docs gate; updated documentation. |
| TRAIN | Enablement & Training Designer | Tutorials, admin training and adoption materials. | Internal/complex product; learning plan. |

## Governance

| Code | Agent | Mandate | Trigger / deliverable |
|---|---|---|---|
| REF | Reference & Research Agent | Verifiable sources, current facts and standards. | External/current claim; evidence register. |
| MEM | Memory Curator | Deduplicates, compacts and validates project memory. | Every milestone/session close; memory integrity report. |
| CHG | Change Manager | Change impact, rollout, migration and stakeholder comms. | Material workflow/contract change; change plan. |
| SUP | Supervisory Agent | Independent phase gate and conflict resolution. | Every phase; approve/risk/block report. |

## Independence and activation rules

- Author and reviewer must be different for critical work. `SUP` never authors the deliverable it approves.
- `WFL`, `PM`, `DISC`, `ORCH`, `MEM`, `QA`, `DOC`, and `SUP` are baseline roles for a product project.
- `SEC` + `PRIV` are mandatory when personal data, authentication, public exposure, uploads or payment are in scope.
- `REF` is mandatory when facts may change or an external standard/service/law influences a decision.
- Every activated specialist updates evidence and memory; inactive agents are marked **not applicable**, not silently omitted.
