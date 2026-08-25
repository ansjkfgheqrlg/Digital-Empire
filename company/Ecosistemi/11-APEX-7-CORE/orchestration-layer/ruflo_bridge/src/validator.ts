import { createHash } from 'node:crypto';
import type { McpTool } from './types.js';

export type ToolHashManifest = Record<string, string>;

export function schemaHash(schema: unknown): string {
  return createHash('sha256').update(JSON.stringify(schema)).digest('hex');
}

export function validateToolSchemas(tools: McpTool[], expected: ToolHashManifest): void {
  const byName = new Map(tools.map((tool) => [tool.name, tool]));
  for (const [name, hash] of Object.entries(expected)) {
    const tool = byName.get(name);
    if (!tool) throw new Error(`RUN_CAPABILITY_MISMATCH: missing ${name}`);
    const actual = schemaHash(tool.inputSchema);
    if (actual !== hash) {
      throw new Error(`RUN_SCHEMA_DRIFT: ${name} expected=${hash} actual=${actual}`);
    }
  }
}
