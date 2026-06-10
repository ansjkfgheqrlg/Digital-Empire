# 📋 SCHEMA_TEMPLATES — Formati Esatti delle Pagine

Quando creo pagine nella wiki, seguire questi template esattamente. Mantengono uniformità e coerenza.

---

## 1. SOURCE (Risorsa Esterna)

**Cartella**: `wiki/sources/`  
**Naming**: `[Titolo_Risorsa].md` (es: `Email_Marketing_Trends_2024.md`)

```markdown
# [Titolo Completo]

- **Tipo**: 🎥 Video / 📄 Articolo / 📚 Libro / 🎙️ Podcast / 📊 Ricerca / 🎓 Corso
- **Autore**: [Nome autore]
- **Data Pubblicazione**: YYYY-MM-DD
- **URL**: [https://...]
- **Tempo Lettura/Fruizione**: Xmin / Xh
- **Fonte Aggiunta**: YYYY-MM-DD (quando l'hai mandata tu)
- **Rilevanza per DE**: 🟢 Alta / 🟡 Media / 🔴 Bassa
- **Tags**: `#marketing` `#automation` `#ai`

## 🎯 Core Takeaway
[Una frase che riassume l'idea principale]

## 📌 Key Insights
1. Insight 1: [Spiegazione concisa]
2. Insight 2: [Spiegazione concisa]
3. Insight 3: [Spiegazione concisa]

## 🔗 Connessioni a Digital Empire
- Rilevante per [[Concept: Nome Concetto]] perché [motivo]
- Rientra in [[Progetto: Nome Progetto]] come [dove]
- [[Entity: Nome Entità]] sta già applicando questo

## 💡 Azioni Proposte
- **Azione 1**: [Descrizione] (Priorità: Alta/Media/Bassa)
- **Azione 2**: [Descrizione] (Priorità: Alta/Media/Bassa)

## 📝 Riassunto Dettagliato
[2-3 paragrafi che riassumono la risorsa con dettagli]

## 📍 Metadata
- **Date Added**: YYYY-MM-DD
- **Last Reviewed**: YYYY-MM-DD
- **Action Taken**: Sì/No — quale
- **Confidence**: Alta/Media/Bassa
```

---

## 2. ENTITY (Persone, Aziende, Tool, Competitor)

**Cartella**: `wiki/entities/`  
**Naming**: `[Tipo]_[Nome].md` (es: `Competitor_HeadStart.md`, `Person_Seth_Godin.md`)

```markdown
# [Nome Entità]

- **Tipo**: 👤 Persona / 🏢 Azienda / 🤖 Tool / 🔍 Competitor / 📦 Prodotto
- **Status**: ✅ Attivo / 👁️ Monitor / 📦 Archivio
- **Rilevanza per DE**: 🟢 Alta / 🟡 Media / 🔴 Bassa
- **Tags**: `#competitor` `#marketing` `#ai`

## 🏷️ Profilo
[2-3 frasi che descrivono chi/cosa è]

## 📊 Dettagli Chiave
- **Fondato/Nato**: [Data o anno]
- **Specializzazione**: [Cosa fa]
- **Metrica principale**: [Followers, ARR, user growth, ecc]
- **Posizione di mercato**: [Numero 1 in X, growing Y%, ecc]

## 🎯 Come Impatta Digital Empire
[Specifico: In che modo sono rilevanti? Sono competitor? Potenza partnership? Inspirazione?]

## 🔗 Relazioni
- Competitor di: [[Entity: ...]]
- Partner potenziale: [[Entity: ...]]
- Usa [[Concept: ...]]
- Appare in [[Synthesis: ...]]

## 📈 Timeline
- **[YYYY-MM-DD]**: Evento importante (es: "Ha lanciato feature X")
- **[YYYY-MM-DD]**: Evento importante

## 🧠 Strategie Osservate
- Strategia 1: [Descrizione di come operano]
- Strategia 2: [Descrizione di come operano]

## 💡 Lezioni per DE
[Cosa possiamo imparare da questa entità?]

## 📍 Metadata
- **Date Added**: YYYY-MM-DD
- **Last Updated**: YYYY-MM-DD
- **Confidence**: Alta/Media/Bassa
- **Data Quality**: Verificato/Presunto
```

---

## 3. CONCEPT (Framework, Teoria, Principio, Metodologia)

**Cartella**: `wiki/concepts/`  
**Naming**: `[Nome_Concetto].md` (es: `Funnel_Sales.md`, `Law_of_Compound_Interest.md`)

```markdown
# [Nome Concetto]

- **Categoria**: 📐 Framework / 💡 Principio / 🔧 Metodologia / 📖 Teoria
- **Origine**: [Da chi, da dove] (es: "Seth Godin", "Naval Ravikant", "Peter Drucker")
- **Facilità**: 🟢 Facile / 🟡 Intermedia / 🔴 Complessa
- **Applicabilità per DE**: [Breve frase: es "Funnel vendita corsi", "Positioning agenzia"]
- **Tags**: `#sales` `#marketing` `#psychology`

## 📖 Definizione
[Spiegazione chiara, come se insegnassi a chi non conosce l'argomento. 1-2 paragrafi]

## 🧬 Componenti Core
1. **Componente A**
   - Spiegazione
   - Come funziona
   
2. **Componente B**
   - Spiegazione
   - Come funziona
   
3. **Componente C**
   - Spiegazione
   - Come funziona

## 🎯 Come Lo Applichiamo in Digital Empire
[Caso d'uso concreto in DE. Es: "Nel funnel dei nostri corsi, il primo stadio è..."]

## ⚡ Varianti / Critiche
- **Variante 1**: [Nome variante] — come differisce
- **Obiezione 1**: [Critica comune] — come rispondere
- **Limite**: [Dove NON applicare questo]

## 📊 Metriche Associati
- [[Metric: Click-through rate]]
- [[Metric: Conversion rate]]

## 🔗 Correlazioni
- Collegato a [[Concept: ...]] perché [relazione]
- Usato in [[Project: ...]]
- Citato in [[Source: ...]]

## 💻 Tool che lo Implementano
- [[Tool: ...]] — come implementa questo

## 📍 Metadata
- **Date Added**: YYYY-MM-DD
- **Mastery Level**: 🟢 Esperto / 🟡 Intermedio / 🔴 Principiante
- **Use Count**: [Numero di volte che appare in progetti]
- **Confidence**: Alta/Media/Bassa
```

---

## 4. SYNTHESIS (Confronto, Analisi, Pattern Cross-Domain)

**Cartella**: `wiki/synthesis/`  
**Naming**: `[Tema]_[Tipo].md` (es: `Funnel_Agenzia_vs_Corsi.md`, `Pattern_Retention_Analysis.md`)

```markdown
# [Titolo Analisi]

- **Tipo**: 📊 Comparazione / 🔍 Pattern Analysis / 📈 Trend / 🎯 Synthesis
- **Data Creazione**: YYYY-MM-DD
- **Urgenza**: 🔴 Alta / 🟡 Media / 🟢 Bassa
- **Tags**: `#strategy` `#comparison` `#growth`

## 🎯 La Domanda Principale
[Che cosa stai analizzando? Quale domanda cerchi di rispondere?]

## 📊 Comparazione / Analisi
[Tabella, grafico testuale, o analisi strutturata]

### Dimensione 1: [Es: Revenue Model]
| Aspetto | Agenzia | Info Products | SaaS |
|---|---|---|---|
| Revenue per cliente | $ X | $ Y | $ Z |
| Acquisition cost | $ | $ | $ |
| Lifetime value | $ | $ | $ |

### Dimensione 2: [Es: Funnel]
[Analisi del funnel per ognuno]

## 💡 Pattern Emergenti
1. **Pattern 1**: [Descrizione] — Evidenza da [Sources/Projects]
2. **Pattern 2**: [Descrizione] — Evidenza da [Sources/Projects]
3. **Pattern 3**: [Descrizione] — Evidenza da [Sources/Projects]

## 🎯 Implicazioni Strategiche per DE
- **Implicazione 1**: [Cosa dovremmo fare?]
- **Implicazione 2**: [Cosa dovremmo testare?]
- **Implicazione 3**: [Dove è l'opportunità?]

## ⚠️ Contraddizioni o Eccezioni
[Se ci sono dati che non rientrano nel pattern, registrali qui]

## 🔗 Fonti
- [[Source: ...]]
- [[Project: ...]]
- [[Entity: ...]]
- [[Concept: ...]]

## 📍 Metadata
- **Date Created**: YYYY-MM-DD
- **Last Updated**: YYYY-MM-DD
- **Confidence Level**: Alta/Media/Bassa
- **Next Review**: YYYY-MM-DD
```

---

## 5. PROJECT (Progetto Attivo di DE)

**Cartella**: `wiki/projects/`  
**Naming**: `[Nome_Progetto]_[Status].md` (es: `SkillBeast_v2_Active.md`)

```markdown
# [Nome Progetto]

- **Status**: 🟢 Active / 🟡 Planning / 🔴 Paused / ✅ Shipped / 📊 Post-mortem
- **Timeline**: START (YYYY-MM-DD) → TARGET SHIP (YYYY-MM-DD)
- **Duration**: [Xx giorni / settimane]
- **Owner**: [Nome persona]
- **Type**: 🚀 Lancio / 📱 Prodotto / 📊 Campagna / 🎓 Corso / 🎯 Iniziativa
- **Budget**: 💰 [Importo o "Low/Medium/High"]
- **Tags**: `#launch` `#infoproduct` `#marketing`

## 🎯 Obiettivi SMART
- **Obiettivo 1**: [Specifico, misurabile, raggiungibile, rilevante, temporale]
- **Obiettivo 2**: [Specifico, misurabile, raggiungibile, rilevante, temporale]
- **Obiettivo 3**: [Specifico, misurabile, raggiungibile, rilevante, temporale]

## 📋 Scope
- **Incluso**: [Cosa entra nel progetto]
- **Escluso**: [Cosa NON entra nel progetto]

## 📊 Metriche di Successo
- **Metrica 1**: [Nome] → Target: [Valore]
- **Metrica 2**: [Nome] → Target: [Valore]
- **Metrica 3**: [Nome] → Target: [Valore]

## 📚 Conoscenza Rilevante
- **Concept**: [[Concept: Funnel]] — perché applicabile qui
- **Source**: [[Source: ...]] — ispirazione da
- **Entity**: [[Entity: Competitor X]] — benchmarking da
- **Metric**: [[Metric: Conversion rate precedenti corsi]]

## 📅 Milestones
- **2026-04-30**: Milestone 1
- **2026-05-15**: Milestone 2
- **2026-06-01**: Milestone 3

## 👥 Team & Responsabilità
- **[Persona 1]**: [Ruolo/Task]
- **[Persona 2]**: [Ruolo/Task]

## 🧠 Learnings in Tempo Reale
[Man mano che avanzi, aggiorna qui. Cosa stai imparando? Cosa funziona? Cosa no?]

- **[Data]**: Learning 1
- **[Data]**: Learning 2

## 🔍 Problemi / Blocchi
- **Blocco 1**: [Descrizione] — Come risolviamo?

## ✅ Outcome (Quando Terminato)
[Risultati finali, cosa è stato raggiunto]

## 📍 Metadata
- **Created**: YYYY-MM-DD
- **Last Updated**: YYYY-MM-DD
- **Next Checkpoint**: YYYY-MM-DD
```

---

## 6. METRIC (KPI, Dato, Misura)

**Cartella**: `wiki/metrics/`  
**Naming**: `[Metrica]_[Dominio].md` (es: `Conversion_Rate_Courses.md`, `CAC_Agency.md`)

```markdown
# [Nome Metrica]

- **Categoria**: 💵 Revenue / 📈 Growth / 👥 Engagement / 💸 Cost / ⚡ Efficiency
- **Dominio**: [Agenzia / Info Products / SaaS / Marketing]
- **Frequenza Misurazione**: 📅 Giornaliera / 📊 Settimanale / 📈 Mensile / 📍 Trimestrale
- **Owner**: [Chi traccia/misura]
- **Tags**: `#metrics` `#kpi` `#tracking`

## 📊 Valore Attuale
- **Valore**: X
- **Data Misurazione**: YYYY-MM-DD
- **Trend**: 📈 Crescente / 📉 Decrescente / → Stabile
- **Variazione vs periodo precedente**: +X% / -X%

## 🎯 Target
- **Target**: X
- **Timeline**: YYYY-MM-DD (quando vogliamo raggiungerlo)
- **Perché questo target**: [Rationale dietro il target]

## 📈 Historical Data
| Periodo | Valore | Nota |
|---|---|---|
| 2026-04 | X | — |
| 2026-03 | Y | Spike dovuto a [...]|
| 2026-02 | Z | — |

## 🔗 Cosa Influenza / È Influenzato
- **Causa di**: [[Metric: ...]]
- **Influenzato da**: [[Metric: ...]]
- **Collegato a**: [[Project: ...]]

## 💡 Insights & Analysis
[Cosa leggi da questi dati? Ci sono pattern? Preoccupazioni? Opportunità?]

## 🔧 Come Migliorare
[Azioni specifiche per muovere questa metrica]

## 📍 Metadata
- **First Tracked**: YYYY-MM-DD
- **Last Updated**: YYYY-MM-DD
- **Data Quality**: ✅ Verified / ⚠️ Estimated / ❌ Unreliable
- **Confidence**: Alta/Media/Bassa
```

---

## 7. TOOL (Software, Utility, Platform)

**Cartella**: `wiki/tools/`  
**Naming**: `[Nome_Tool].md` (es: `Obsidian.md`, `Stripe.md`, `Claude.md`)

```markdown
# [Nome Tool]

- **Categoria**: 💻 Software / 🌐 Platform / 🔌 Integration / 📊 Analytics
- **Cost**: 💚 Gratuito / 💛 Freemium / 💰 Paid / 💵 Enterprise
- **Purpose**: [Breve descrizione di cosa fa]
- **Tags**: `#automation` `#marketing` `#productivity`

## 🎯 Use Case in DE
[Come lo usiamo in Digital Empire?]

## ✅ Pros
- Pro 1: [Descrizione]
- Pro 2: [Descrizione]
- Pro 3: [Descrizione]

## ❌ Cons
- Con 1: [Descrizione]
- Con 2: [Descrizione]

## 🔗 Integra Con
- [[Tool: ...]]
- [[Tool: ...]]

## 📍 Metadata
- **First Used**: YYYY-MM-DD
- **Current Status**: ✅ In uso / 👁️ Valutazione / 📦 Archivio
- **Recommendation**: Sì / No / Dipende da [condizioni]
```

---

## 🎓 Quick Reference — Quando Creare Cosa

| Hai | Crea | In Cartella | Link a |
|---|---|---|---|
| Un articolo/libro/video | SOURCE | `sources/` | Concepts, Projects, Entities |
| Una persona/azienda/tool importante | ENTITY | `entities/` | Concepts, Projects, Syntheses |
| Un'idea/principio che riusi | CONCEPT | `concepts/` | Projects, Syntheses |
| Un confronto / pattern | SYNTHESIS | `synthesis/` | Sources, Concepts, Projects |
| Un progetto/lancio attivo | PROJECT | `projects/` | Concepts, Entities, Metrics |
| Un numero/KPI da tracciare | METRIC | `metrics/` | Projects, Entities |
| Un software/utility | TOOL | `tools/` | Projects, Concepts |

---

## 📏 Regola d'Oro

Ogni pagina deve avere:
✅ Un titolo chiaro  
✅ Metadata (tipo, data, tags)  
✅ 2-3 paragrafi di contenuto sostanziale  
✅ Almeno 2 link a altre pagine  
✅ Un timestamp di quando è stata creata/aggiornata

Se manca una di queste, la pagina è incompleta.

---

**Versione**: 1.0  
**Ultimo aggiornamento**: 2026-04-29  
**Uso**: Reference quando creiamo pagine
