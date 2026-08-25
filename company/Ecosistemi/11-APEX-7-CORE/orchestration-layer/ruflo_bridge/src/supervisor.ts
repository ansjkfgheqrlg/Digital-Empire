export type SupervisorState =
  | 'STOPPED' | 'STARTING' | 'HANDSHAKING' | 'READY'
  | 'DEGRADED' | 'RESTARTING' | 'OPEN';

export class BridgeSupervisor {
  state: SupervisorState = 'STOPPED';
  private failures: number[] = [];
  private openedAt: number | undefined;

  constructor(
    private readonly threshold = 3,
    private readonly windowMs = 300_000,
    private readonly openMs = 30_000,
  ) {}

  transition(target: SupervisorState): void {
    const allowed: Record<SupervisorState, SupervisorState[]> = {
      STOPPED: ['STARTING'],
      STARTING: ['HANDSHAKING', 'OPEN'],
      HANDSHAKING: ['READY', 'DEGRADED', 'OPEN'],
      READY: ['DEGRADED', 'RESTARTING', 'STOPPED'],
      DEGRADED: ['RESTARTING', 'OPEN', 'STOPPED'],
      RESTARTING: ['STARTING', 'OPEN'],
      OPEN: ['RESTARTING', 'STOPPED'],
    };
    if (!allowed[this.state].includes(target)) {
      throw new Error(`Illegal bridge transition ${this.state}->${target}`);
    }
    this.state = target;
  }

  recordFailure(now = Date.now()): void {
    this.failures = this.failures.filter((value) => value >= now - this.windowMs);
    this.failures.push(now);
    if (this.failures.length >= this.threshold) {
      this.state = 'OPEN';
      this.openedAt = now;
    }
  }

  canRestart(now = Date.now()): boolean {
    return this.state !== 'OPEN' || (!!this.openedAt && now - this.openedAt >= this.openMs);
  }

  recordSuccess(): void {
    this.failures = [];
    this.openedAt = undefined;
    this.state = 'READY';
  }
}
