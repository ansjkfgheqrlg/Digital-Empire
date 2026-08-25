import type { BridgeResult, Json, McpClientPort, TaskAssignment } from './types.js';
import { BridgeSupervisor } from './supervisor.js';
import { validateToolSchemas, type ToolHashManifest } from './validator.js';

const ROLE_TO_AGENT: Record<TaskAssignment['role'], string> = {
  planner: 'planner', implementer: 'coder', critic: 'reviewer', gate: 'reviewer',
};

export class RufloBridge {
  readonly supervisor = new BridgeSupervisor();
  private swarmId?: string;

  constructor(
    private readonly client: McpClientPort,
    private readonly expectedSchemas: ToolHashManifest,
  ) {}

  async start(): Promise<void> {
    this.supervisor.transition('STARTING');
    try {
      await this.client.start();
      this.supervisor.transition('HANDSHAKING');
      validateToolSchemas(await this.client.listTools(), this.expectedSchemas);
      this.supervisor.recordSuccess();
    } catch (error) {
      this.supervisor.recordFailure();
      throw error;
    }
  }

  async initializeSwarm(): Promise<string> {
    this.requireReady();
    const result = await this.client.callTool('swarm_init', {
      topology: 'hierarchical', maxAgents: 4, strategy: 'balanced',
      config: { communicationProtocol: 'message-bus', autoScaling: false },
    });
    if (result.success !== true || typeof result.swarmId !== 'string') {
      throw new Error(`RUN_PROTOCOL_ERROR: invalid swarm_init result`);
    }
    this.swarmId = result.swarmId;
    return result.swarmId;
  }

  async execute(assignment: TaskAssignment): Promise<BridgeResult> {
    this.requireReady();
    if (!this.swarmId) await this.initializeSwarm();
    const agentId = `ocp-${assignment.role}-${assignment.taskId}`;
    try {
      const spawned = await this.client.callTool('agent_spawn', {
        agentType: ROLE_TO_AGENT[assignment.role], agentId, swarmId: this.swarmId!,
        task: assignment.prompt,
      });
      if (spawned.success !== true) throw new Error('agent_spawn returned failure');
      const executed = await this.withTimeout(
        this.client.callTool('agent_execute', {
          agentId, prompt: assignment.prompt, systemPrompt: assignment.systemPrompt,
          maxTokens: assignment.maxTokens,
        }),
        assignment.timeoutMs,
      );
      if (executed.success !== true) {
        return {
          taskId: assignment.taskId, status: 'FAILED',
          failure: { code: 'RUN_EXECUTION_FAILED', detail: String(executed.error ?? 'unknown') },
        };
      }
      return {
        taskId: assignment.taskId,
        status: 'SUCCEEDED',
        output: typeof executed.output === 'string' ? executed.output : JSON.stringify(executed),
        ...(typeof executed.model === 'string' ? { model: executed.model } : {}),
        ...(executed.usage && typeof executed.usage === 'object'
          ? { usage: executed.usage as Record<string, Json> } : {}),
      };
    } catch (error) {
      this.supervisor.recordFailure();
      return {
        taskId: assignment.taskId, status: 'FAILED',
        failure: { code: this.failureCode(error), detail: String(error) },
      };
    } finally {
      try { await this.client.callTool('agent_terminate', { agentId, force: true }); }
      catch { /* cleanup is best-effort; canonical recovery is external */ }
    }
  }

  async close(): Promise<void> {
    if (this.swarmId) {
      try { await this.client.callTool('swarm_shutdown', { swarmId: this.swarmId, graceful: true }); }
      catch { /* best effort */ }
    }
    await this.client.close();
    this.supervisor.state = 'STOPPED';
  }

  private requireReady(): void {
    if (this.supervisor.state !== 'READY') throw new Error('RUN_UNAVAILABLE: bridge not ready');
  }

  private async withTimeout<T>(promise: Promise<T>, timeoutMs: number): Promise<T> {
    let timer: NodeJS.Timeout;
    return Promise.race([
      promise,
      new Promise<T>((_, reject) => {
        timer = setTimeout(() => reject(new Error('RUN_TIMEOUT')), timeoutMs);
      }),
    ]).finally(() => clearTimeout(timer!));
  }

  private failureCode(error: unknown): string {
    const text = String(error);
    if (text.includes('RUN_TIMEOUT')) return 'RUN_TIMEOUT';
    if (text.includes('SCHEMA_DRIFT')) return 'RUN_SCHEMA_DRIFT';
    if (text.includes('CAPABILITY_MISMATCH')) return 'RUN_CAPABILITY_MISMATCH';
    return 'RUN_UNAVAILABLE';
  }
}
