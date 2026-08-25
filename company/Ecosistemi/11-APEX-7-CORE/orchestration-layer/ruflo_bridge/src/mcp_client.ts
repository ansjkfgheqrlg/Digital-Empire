import { spawn, type ChildProcessWithoutNullStreams } from 'node:child_process';
import readline from 'node:readline';
import type { Json, McpClientPort, McpTool } from './types.js';

interface Pending {
  resolve: (value: Record<string, Json>) => void;
  reject: (error: Error) => void;
  timer: NodeJS.Timeout;
}

export class RufloMcpClient implements McpClientPort {
  private child: ChildProcessWithoutNullStreams | undefined;
  private readonly pending = new Map<number, Pending>();
  private nextId = 1;
  private stderrTail = '';

  constructor(
    private readonly version: string,
    private readonly cwd: string,
    private readonly requestTimeoutMs = 30_000,
    private readonly allowProviderCredentials = false,
  ) {}

  async start(): Promise<void> {
    if (this.child) throw new Error('MCP client already started');
    const childEnv: NodeJS.ProcessEnv = {
      ...process.env,
      NO_COLOR: '1',
      CLAUDE_FLOW_TELEMETRY_ENABLED: 'false',
    };
    if (!this.allowProviderCredentials) {
      delete childEnv.ANTHROPIC_API_KEY;
      delete childEnv.OPENROUTER_API_KEY;
      delete childEnv.OLLAMA_API_KEY;
    }
    this.child = spawn('npx', ['--yes', `ruflo@${this.version}`, 'mcp', 'start'], {
      cwd: this.cwd,
      stdio: ['pipe', 'pipe', 'pipe'],
      env: childEnv,
    });
    this.child.stderr.setEncoding('utf8');
    this.child.stderr.on('data', (chunk: string) => {
      this.stderrTail = (this.stderrTail + chunk).slice(-16_000);
    });
    this.child.once('exit', (code, signal) => {
      const error = new Error(`Ruflo MCP exited code=${code} signal=${signal}`);
      for (const pending of this.pending.values()) {
        clearTimeout(pending.timer);
        pending.reject(error);
      }
      this.pending.clear();
      this.child = undefined;
    });
    const lines = readline.createInterface({ input: this.child.stdout });
    lines.on('line', (line) => this.onLine(line));
    const initialized = await this.request('initialize', {
      protocolVersion: '2024-11-05', capabilities: {},
      clientInfo: { name: 'ocp-ruflo-bridge', version: '0.1.0' },
    });
    if (initialized.error) throw new Error(`MCP initialize failed: ${JSON.stringify(initialized.error)}`);
    this.notify('notifications/initialized', {});
  }

  async listTools(): Promise<McpTool[]> {
    const response = await this.request('tools/list', {});
    if (response.error) throw new Error(`tools/list failed: ${JSON.stringify(response.error)}`);
    const result = response.result as { tools?: McpTool[] } | undefined;
    return result?.tools ?? [];
  }

  async callTool(name: string, args: Record<string, Json>): Promise<Record<string, Json>> {
    const response = await this.request('tools/call', { name, arguments: args });
    if (response.error) throw new Error(`tool ${name} failed: ${JSON.stringify(response.error)}`);
    const result = response.result as { content?: Array<{ type: string; text?: string }> } | undefined;
    const text = result?.content?.find((item) => item.type === 'text')?.text;
    if (!text) return (response.result as Record<string, Json>) ?? {};
    try { return JSON.parse(text) as Record<string, Json>; }
    catch { return { text }; }
  }

  async close(): Promise<void> {
    const child = this.child;
    if (!child) return;
    child.stdin.end();
    await new Promise<void>((resolve) => {
      const timer = setTimeout(() => { child.kill('SIGKILL'); resolve(); }, 5_000);
      child.once('exit', () => { clearTimeout(timer); resolve(); });
    });
  }

  getStderrTail(): string { return this.stderrTail; }

  terminate(signal: NodeJS.Signals = 'SIGTERM'): boolean {
    return this.child?.kill(signal) ?? false;
  }

  private request(method: string, params: Record<string, Json>): Promise<Record<string, Json>> {
    if (!this.child) return Promise.reject(new Error('MCP client is not started'));
    const id = this.nextId++;
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`MCP timeout: ${method}`));
      }, this.requestTimeoutMs);
      this.pending.set(id, { resolve, reject, timer });
      this.child!.stdin.write(JSON.stringify({ jsonrpc: '2.0', id, method, params }) + '\n');
    });
  }

  private notify(method: string, params: Record<string, Json>): void {
    this.child?.stdin.write(JSON.stringify({ jsonrpc: '2.0', method, params }) + '\n');
  }

  private onLine(line: string): void {
    let message: Record<string, Json>;
    try { message = JSON.parse(line) as Record<string, Json>; }
    catch { return; }
    const id = typeof message.id === 'number' ? message.id : undefined;
    if (id === undefined) return;
    const pending = this.pending.get(id);
    if (!pending) return;
    clearTimeout(pending.timer);
    this.pending.delete(id);
    pending.resolve(message);
  }
}
