import assert from 'node:assert/strict';
import test from 'node:test';
import { RufloBridge } from '../src/bridge.js';
import type { Json, McpClientPort, McpTool } from '../src/types.js';
import { schemaHash } from '../src/validator.js';

class FakeClient implements McpClientPort {
  started = false;
  closed = false;
  calls: string[] = [];
  constructor(
    readonly tools: McpTool[],
    readonly executeResult: Record<string, Json> = {
      success: true, output: '{"ok":true}', model: 'test-model', usage: { totalTokens: 10 },
    },
  ) {}
  async start() { this.started = true; }
  async listTools() { return this.tools; }
  async callTool(name: string): Promise<Record<string, Json>> {
    this.calls.push(name);
    if (name === 'swarm_init') return { success: true, swarmId: 'swarm-1' };
    if (name === 'agent_spawn') return { success: true, agentId: 'a' };
    if (name === 'agent_execute') return this.executeResult;
    return { success: true };
  }
  async close() { this.closed = true; }
}

const schemas: Record<string, Record<string, Json>> = {
  swarm_init: { type: 'object' },
  agent_spawn: { type: 'object', required: ['agentType'] },
  agent_execute: { type: 'object', required: ['agentId', 'prompt'] },
  agent_terminate: { type: 'object', required: ['agentId'] },
  swarm_shutdown: { type: 'object', required: ['swarmId'] },
};
const tools = Object.entries(schemas).map(([name, inputSchema]) => ({ name, inputSchema }));
const expected = Object.fromEntries(tools.map((tool) => [tool.name, schemaHash(tool.inputSchema)]));

const assignment = {
  workflowId: 'w', taskId: 't', role: 'planner' as const,
  prompt: 'plan', systemPrompt: 'system', maxTokens: 100, timeoutMs: 1000,
};

test('bridge validates schemas and normalizes successful execution', async () => {
  const client = new FakeClient(tools);
  const bridge = new RufloBridge(client, expected);
  await bridge.start();
  assert.equal(bridge.supervisor.state, 'READY');
  const result = await bridge.execute(assignment);
  assert.equal(result.status, 'SUCCEEDED');
  assert.equal(result.model, 'test-model');
  assert.deepEqual(client.calls, ['swarm_init', 'agent_spawn', 'agent_execute', 'agent_terminate']);
  await bridge.close();
  assert.equal(client.closed, true);
});

test('schema drift blocks startup', async () => {
  const client = new FakeClient(tools);
  const bridge = new RufloBridge(client, { ...expected, agent_execute: 'wrong' });
  await assert.rejects(() => bridge.start(), /RUN_SCHEMA_DRIFT/);
  assert.notEqual(bridge.supervisor.state, 'READY');
  await client.close();
});

test('provider execution failure is normalized and cleanup still runs', async () => {
  const client = new FakeClient(tools, { success: false, error: 'provider auth' });
  const bridge = new RufloBridge(client, expected);
  await bridge.start();
  const result = await bridge.execute(assignment);
  assert.equal(result.status, 'FAILED');
  assert.equal(result.failure?.code, 'RUN_EXECUTION_FAILED');
  assert.equal(client.calls.at(-1), 'agent_terminate');
  await bridge.close();
});
