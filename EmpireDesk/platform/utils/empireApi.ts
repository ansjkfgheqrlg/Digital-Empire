/**
 * empireApi.ts — bridge verso il backend Python di Empire Desk (app.py).
 * Owner: Max (UI/UX) — parte del pivot Aureus (dossier 17 §0-bis, fase 2 / U1).
 *
 * Aureus è SEMPRE servita dall'HTTP server locale di app.py (sia motore chrome-app che
 * pywebview: entrambi caricano url=http://127.0.0.1:<porta>/ — vedi app.py::main_webview),
 * quindi qui basta same-origin fetch, nessun bridge dual-mode necessario.
 *
 * Se l'app viene aperta fuori da Empire Desk (es. `vite dev` puro, anteprima statica),
 * le chiamate falliscono in modo pulito: ogni funzione ritorna un risultato "non disponibile"
 * invece di lanciare un'eccezione non gestita — i componenti mostrano lo stato reale.
 */

export interface EmpireTile {
  id: string;
  icon: string;
  name: string;
  desc: string;
  kind: 'bat' | 'py' | 'node' | 'readonly';
  input: 'url' | 'path' | null;
  running: boolean;
  exit_code: number | null;
}

export interface LaunchResult {
  ok: boolean;
  error?: string;
}

export interface PollResult {
  lines: string[];
  running: boolean;
  exit_code: number | null;
  error: string | null;
}

async function post<T>(route: string, payload?: unknown): Promise<T> {
  const res = await fetch(`/api/${route}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload ?? {}),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status} su /api/${route}`);
  return res.json();
}

export const EmpireApi = {
  /** True se il backend risponde (Aureus servita da Empire Desk, non da un'anteprima isolata). */
  isAvailable: async (): Promise<boolean> => {
    try {
      await post('tiles');
      return true;
    } catch {
      return false;
    }
  },

  getTiles: async (): Promise<EmpireTile[]> => {
    const d = await post<{ tiles: EmpireTile[] }>('tiles');
    return d.tiles;
  },

  launch: (id: string, input?: string | null): Promise<LaunchResult> =>
    post('launch', { id, input }),

  poll: (id: string): Promise<PollResult> => post('poll', { id }),
};
