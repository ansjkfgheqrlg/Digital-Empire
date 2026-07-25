# Reference Library

Fonti operative curate per guidare decisioni tecniche e di prodotto. REF deve verificare sempre la pagina specifica prima di citarne una versione, requisito o compatibilità.

| ID | Tema | Fonte primaria | Uso |
|---|---|---|---|
| REF-WCAG | Accessibilità web | W3C WCAG 2.1: https://www.w3.org/TR/WCAG21/ | ACC, UX, FE |
| REF-ARIA | Semantica/accessibilità | WAI-ARIA Authoring Practices: https://www.w3.org/WAI/ARIA/apg/ | ACC, FE |
| REF-OWASP | Sicurezza applicativa | OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/ | SEC, BE, QA |
| REF-API | API HTTP | RFC 9110: https://www.rfc-editor.org/rfc/rfc9110 | ARC, BE, INT |
| REF-REST | API design | Microsoft REST API Guidelines: https://github.com/microsoft/api-guidelines | ARC, BE |
| REF-FASTAPI | FastAPI | https://fastapi.tiangolo.com/ | BE |
| REF-PYTHON | Python | https://docs.python.org/3/ | BE, QA, REL |
| REF-PYDANTIC | Validation/settings | https://docs.pydantic.dev/ | BE |
| REF-SQLA | SQLAlchemy | https://docs.sqlalchemy.org/ | BE, DATA |
| REF-POSTGRES | PostgreSQL | https://www.postgresql.org/docs/ | DATA, BE |
| REF-PYTEST | Python testing | https://docs.pytest.org/ | QA, BE |
| REF-RUFF | Python quality | https://docs.astral.sh/ruff/ | QA, BE |
| REF-DOCKER | Containers | https://docs.docker.com/ | REL |
| REF-OPENAPI | OpenAPI | https://spec.openapis.org/oas/latest.html | ARC, INT |
| REF-GDPR | Privacy EU | EUR-Lex GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj | SEC, LEG |
| REF-NIST | Secure development | NIST SSDF: https://csrc.nist.gov/Projects/ssdf | SEC, REL |
| REF-ISO8601 | Date/time | ISO 8601 overview: https://www.iso.org/iso-8601-date-and-time-format.html | UX, BE, DATA |

## Uso obbligatorio

- REF copia nel registro memoria solo riferimenti realmente consultati per una decisione.
- La libreria è una mappa iniziale, non una prova che un contenuto sia stato verificato per il progetto.
- Per licenze, prezzi, API, SDK e norme, registrare sempre data di consultazione e URL della pagina esatta.

## Extended reference catalogue

| ID | Topic | Primary source | Typical agents |
|---|---|---|---|
| REF-WCAG22 | Current accessibility standard | https://www.w3.org/TR/WCAG22/ | ACC, UX, FE |
| REF-HTML | HTML semantics | https://html.spec.whatwg.org/ | FE, ACC |
| REF-CSS | CSS standards | https://www.w3.org/Style/CSS/ | FE, DSN |
| REF-WEBPERF | Core Web Vitals | https://web.dev/articles/vitals | PERF, FE, SEO |
| REF-MDN | Web platform reference | https://developer.mozilla.org/ | FE, INT |
| REF-RFC3986 | URI syntax | https://www.rfc-editor.org/rfc/rfc3986 | INT, FE |
| REF-RFC9457 | Problem Details error format | https://www.rfc-editor.org/rfc/rfc9457 | ARC, BE |
| REF-RFC7519 | JWT | https://www.rfc-editor.org/rfc/rfc7519 | SEC, BE |
| REF-OAUTH | OAuth 2.0 | https://datatracker.ietf.org/doc/html/rfc6749 | SEC, INT |
| REF-OIDC | OpenID Connect | https://openid.net/developers/specs/ | SEC, INT |
| REF-OWASP-TOP10 | OWASP Top 10 | https://owasp.org/www-project-top-ten/ | SEC, QA |
| REF-OWASP-API | OWASP API Security | https://owasp.org/www-project-api-security/ | SEC, BE, INT |
| REF-OWASP-MAS | Mobile security | https://mas.owasp.org/ | SEC, MOB |
| REF-CWE | Weakness taxonomy | https://cwe.mitre.org/ | SEC, REV |
| REF-CVSS | Vulnerability severity | https://www.first.org/cvss/ | SEC, GRC |
| REF-SLSA | Supply-chain integrity | https://slsa.dev/ | REL, SEC |
| REF-SBOM | SBOM practice | https://www.cisa.gov/sbom | REL, SEC, GRC |
| REF-NIST-PRIV | Privacy Framework | https://www.nist.gov/privacy-framework | PRIV, GRC |
| REF-EDPB | EU privacy guidance | https://www.edpb.europa.eu/ | PRIV, LEG |
| REF-EAA | European Accessibility Act | https://ec.europa.eu/social/main.jsp?catId=1202 | ACC, LEG |
| REF-ISO27001 | Information security management | https://www.iso.org/isoiec-27001-information-security.html | SEC, GRC |
| REF-ISO25010 | Software quality model | https://iso25000.com/index.php/en/iso-25000-standards/iso-25010 | QA, ARC |
| REF-12FACTOR | Service configuration/operations | https://12factor.net/ | ARC, REL |
| REF-OPENTELEMETRY | Observability | https://opentelemetry.io/docs/ | SRE, REL |
| REF-PROMETHEUS | Metrics/alerting | https://prometheus.io/docs/ | SRE |
| REF-K8S | Kubernetes | https://kubernetes.io/docs/ | REL, CLOUD |
| REF-TERRAFORM | Infrastructure as code | https://developer.hashicorp.com/terraform/docs | CLOUD, REL |
| REF-GHA | GitHub Actions | https://docs.github.com/actions | REL |
| REF-GIT | Git | https://git-scm.com/doc | REL, REV |
| REF-SEMVER | Versioning | https://semver.org/ | ARC, REL, DOC |
| REF-CONVENTIONAL | Commit convention | https://www.conventionalcommits.org/ | REL, DOC |
| REF-ADR | Architecture decision records | https://adr.github.io/ | ARC, ORCH |
| REF-C4 | Architecture diagrams | https://c4model.com/ | ARC |
| REF-MERMAID | Diagrams as code | https://mermaid.js.org/ | ARC, DOC |
| REF-EVENTS | Event naming/tracking | https://www.snowplow.io/blog/what-is-a-data-taxonomy | ANA, PM |
| REF-STRIPE | Payment integration reference | https://docs.stripe.com/ | PAY, INT, SEC |
| REF-PCI | Payment security standard | https://www.pcisecuritystandards.org/ | PAY, SEC, LEG |
| REF-APPLE-HIG | Apple UI guidelines | https://developer.apple.com/design/human-interface-guidelines/ | MOB, UX |
| REF-MATERIAL | Android/Material guidance | https://m3.material.io/ | MOB, UX, FE |
| REF-I18N | W3C internationalization | https://www.w3.org/International/ | L10N, CNT, FE |
| REF-SCHEMA | Structured data | https://schema.org/ | SEO, FE |
| REF-GOOGLESEO | Search essentials | https://developers.google.com/search/docs/fundamentals/seo-starter-guide | SEO |
| REF-LLM-NIST | AI risk management | https://www.nist.gov/itl/ai-risk-management-framework | AI, LEG, GRC |
| REF-MLFLOW | ML lifecycle | https://mlflow.org/docs/latest/ | MLOPS, AI |
| REF-ONNX | Model interoperability | https://onnx.ai/ | AI, MLOPS |
| REF-UXNIELSEN | Usability heuristics | https://www.nngroup.com/articles/ten-usability-heuristics/ | UX, UXR |
| REF-JOBS | Jobs To Be Done | https://www.intercom.com/blog/jobs-to-be-done-framework/ | PM, DISC |

### Source quality rules

Use the official source above as the first stop. For critical legal, payment, security, accessibility, pricing or API-version decisions, REF must also record the exact page revision/date and flag any uncertainty. Secondary sources may explain; they cannot override primary standards or vendor documentation.
