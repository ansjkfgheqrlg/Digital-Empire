# Tools

## read_file

- **Description**: Legge il contenuto di un file dal filesystem dell'utente. Usalo quando l'utente referenzia un prompt esistente, un eval set, una doc.
- **When to use**: Solo se l'utente menziona esplicitamente un file (path o nome). Non leggere file "speculativamente".
- **Input schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "path": {"type": "string", "description": "Absolute or relative path"}
    },
    "required": ["path"]
  }
  ```
- **Output schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "content": {"type": "string"},
      "lines": {"type": "integer"},
      "size_bytes": {"type": "integer"}
    }
  }
  ```
- **Side effects**: nessuno (read-only)
- **Errors possible**: `file_not_found`, `permission_denied`, `too_large` (>5MB)
- **Example invocation**:
  ```json
  {"path": "./prompts/email_classifier_v3.txt"}
  ```

## web_search

- **Description**: Cerca sul web per recuperare informazioni recenti su paper, tecniche, best practices. Usalo solo se non hai info sufficiente nel context.
- **When to use**:
  - L'utente cita un paper specifico che potrebbe non essere nel tuo training
  - Tecnica menzionata che non riconosci (potrebbe essere nuova)
  - L'utente chiede "le best practices attuali per X"
- **DO NOT use**: per concetti basic che conosci già (sprecando token e latency)
- **Input schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "query": {"type": "string", "description": "Search query (be specific)"},
      "max_results": {"type": "integer", "default": 3, "maximum": 10}
    },
    "required": ["query"]
  }
  ```
- **Output schema**:
  ```json
  {
    "type": "object",
    "properties": {
      "results": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "title": {"type": "string"},
            "url": {"type": "string"},
            "snippet": {"type": "string"}
          }
        }
      }
    }
  }
  ```
- **Side effects**: rate limit (10 req/min)
- **Errors possible**: `rate_limited`, `no_results`, `timeout`
- **Example invocation**:
  ```json
  {"query": "lost in the middle Liu et al. 2023", "max_results": 3}
  ```
