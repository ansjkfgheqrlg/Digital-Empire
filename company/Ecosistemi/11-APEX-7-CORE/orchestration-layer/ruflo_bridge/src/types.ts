export type Json = null | boolean | number | string | Json[] | { [key: string]: Json };

export interface McpTool {
  name: string;
  description?: string;
  inputSchema: Record<string, Json>;
}

export interface TaskAssignment {
  workflowId: string;
  taskId: string;
  role: 'planner' | 'implementer' | 'critic' | 'gate';
  prompt: string;
  systemPrompt: string;
  maxTokens: number;
  timeoutMs: number;
}

export interface BridgeResult {
  taskId: string;
  status: 'SUCCEEDED' | 'FAILED';
  output?: string;
  model?: string;
  usage?: Record<string, Json>;
  failure?: { code: string; detail: string };
}

export interface McpClientPort {
  start(): Promise<void>;
  listTools(): Promise<McpTool[]>;
  callTool(name: string, args: Record<string, Json>): Promise<Record<string, Json>>;
  close(): Promise<void>;
}
