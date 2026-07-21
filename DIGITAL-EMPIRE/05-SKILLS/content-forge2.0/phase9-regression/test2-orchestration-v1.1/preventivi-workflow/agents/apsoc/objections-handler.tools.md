# Tools — objections-handler

## main_tool

- **Description**: Strumento principale di objections-handler per operazione X nel dominio APSOC
- **When to use**: Sempre al primo step del task
- **Input schema**: `{"type":"object","properties":{"input":{"type":"string"}}}`
- **Output schema**: `{"type":"object","properties":{"result":{"type":"string"}}}`
- **Side effects**: nessuno
- **Errors possible**: `invalid_input`, `timeout`
