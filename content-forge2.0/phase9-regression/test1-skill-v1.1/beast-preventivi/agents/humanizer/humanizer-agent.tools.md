# Tools — humanizer-agent

## sample_tool_1

- **Description**: Strumento principale di humanizer-agent per operazione X
- **When to use**: Sempre al primo step del task
- **Input schema**:
```json
{
  "type": "object",
  "properties": {
    "input_data": {"type": "string"}
  },
  "required": ["input_data"]
}
```
- **Output schema**:
```json
{
  "type": "object",
  "properties": {
    "result": {"type": "string"},
    "confidence": {"type": "number"}
  }
}
```
- **Side effects**: nessuno
- **Errors possible**: `invalid_input`, `timeout`
- **Example invocation**:
```json
{"input_data": "esempio"}
```
- **Example response**:
```json
{"result": "processed", "confidence": 0.92}
```
