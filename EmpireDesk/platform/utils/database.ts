import { 
  User, Task, Lead, Notification, SocialPost, EditorialItem, 
  InfobusinessProduct, Funnel, AcademyModule, AutomationRule, AutomationLog 
} from '../types';
import { 
  INITIAL_ACADEMY_MODULES, 
  MOCK_USERS 
} from '../constants';

// --- DEFAULTS (Defined locally to avoid circular deps or missing exports) ---
const DEFAULT_PRODUCTS: InfobusinessProduct[] = [
  {
    id: 'prod-1',
    title: 'YouTube Automation Mastery',
    price: 497,
    sales: 124,
    category: 'INFO',
    modules: []
  },
  {
    id: 'prod-2',
    title: 'Agency Scaling Systems',
    price: 997,
    sales: 58,
    category: 'INFO',
    modules: []
  },
  {
    id: 'serv-1',
    title: 'Sviluppo Funnel High-Ticket',
    price: 3000,
    sales: 12,
    category: 'AGENCY',
    serviceType: 'CONSULTING',
    modules: []
  }
];

const INITIAL_RULES: AutomationRule[] = [
  {
    id: 'rule-1',
    name: 'Benvenuto Nuovi Lead',
    active: true,
    trigger: 'LEAD_CREATED',
    action: 'SEND_EMAIL',
    runCount: 45,
    lastRun: 'Oggi, 10:30'
  },
  {
    id: 'rule-2',
    name: 'Notifica Slack Vendite',
    active: true,
    trigger: 'LEAD_WON',
    action: 'NOTIFY_SLACK',
    runCount: 12,
    lastRun: 'Ieri'
  }
];

// CHIAVI DEL DATABASE
const DB_KEYS = {
  USER: 'aureus_v2_user',
  TASKS: 'aureus_v2_tasks',
  LEADS: 'aureus_v2_leads',
  NOTIFICATIONS: 'aureus_v2_notifs',
  SOCIAL: 'aureus_v2_social',
  EDITORIAL: 'aureus_v2_editorial',
  PRODUCTS: 'aureus_v2_products',
  FUNNELS: 'aureus_v2_funnels',
  ACADEMY: 'aureus_v2_academy',
  AUTOMATIONS: 'aureus_v2_automations',
  LOGS: 'aureus_v2_logs'
};

// Funzione Helper Generica per il Caricamento
const load = <T>(key: string, fallback: T): T => {
  try {
    const serialized = localStorage.getItem(key);
    if (serialized === null) {
      return fallback;
    }
    return JSON.parse(serialized);
  } catch (error) {
    console.error(`Database Error: Failed to load ${key}`, error);
    return fallback;
  }
};

// Funzione Helper Generica per il Salvataggio
const save = <T>(key: string, data: T): void => {
  try {
    const serialized = JSON.stringify(data);
    localStorage.setItem(key, serialized);
  } catch (error) {
    console.error(`Database Error: Failed to save ${key}`, error);
  }
};

// --- IL MOTORE DATABASE ---
export const DB = {
  // Entità: Utente
  user: {
    get: () => load<User | null>(DB_KEYS.USER, null),
    save: (user: User | null) => save(DB_KEYS.USER, user),
  },

  // Entità: Tasks
  tasks: {
    getAll: () => load<Task[]>(DB_KEYS.TASKS, []),
    save: (tasks: Task[]) => save(DB_KEYS.TASKS, tasks),
  },

  // Entità: Leads (CRM)
  leads: {
    getAll: () => load<Lead[]>(DB_KEYS.LEADS, []),
    save: (leads: Lead[]) => save(DB_KEYS.LEADS, leads),
  },

  // Entità: Notifiche
  notifications: {
    getAll: () => load<Notification[]>(DB_KEYS.NOTIFICATIONS, []),
    save: (notifs: Notification[]) => save(DB_KEYS.NOTIFICATIONS, notifs),
  },

  // Entità: Social Media
  social: {
    getAll: () => load<SocialPost[]>(DB_KEYS.SOCIAL, []),
    save: (posts: SocialPost[]) => save(DB_KEYS.SOCIAL, posts),
  },

  // Entità: Editoriale
  editorial: {
    getAll: () => load<EditorialItem[]>(DB_KEYS.EDITORIAL, []),
    save: (items: EditorialItem[]) => save(DB_KEYS.EDITORIAL, items),
  },

  // Entità: Prodotti Info
  products: {
    getAll: () => load<InfobusinessProduct[]>(DB_KEYS.PRODUCTS, DEFAULT_PRODUCTS),
    save: (products: InfobusinessProduct[]) => save(DB_KEYS.PRODUCTS, products),
  },

  // Entità: Funnels
  funnels: {
    getAll: () => load<Funnel[]>(DB_KEYS.FUNNELS, []),
    save: (funnels: Funnel[]) => save(DB_KEYS.FUNNELS, funnels),
  },

  // Entità: Academy
  academy: {
    getAll: () => load<AcademyModule[]>(DB_KEYS.ACADEMY, INITIAL_ACADEMY_MODULES),
    save: (modules: AcademyModule[]) => save(DB_KEYS.ACADEMY, modules),
  },

  // Entità: Automazioni
  automations: {
    getRules: () => load<AutomationRule[]>(DB_KEYS.AUTOMATIONS, INITIAL_RULES),
    saveRules: (rules: AutomationRule[]) => save(DB_KEYS.AUTOMATIONS, rules),
    getLogs: () => load<AutomationLog[]>(DB_KEYS.LOGS, []),
    saveLogs: (logs: AutomationLog[]) => save(DB_KEYS.LOGS, logs),
  },

  // --- FUNZIONI DI SISTEMA (BACKUP & RIPRISTINO) ---
  
  // 1. Scarica Backup (Crea un file JSON fisico)
  downloadBackup: () => {
    const backupData = {
      timestamp: new Date().toISOString(),
      version: '2.0',
      data: {
        user: load(DB_KEYS.USER, null),
        tasks: load(DB_KEYS.TASKS, []),
        leads: load(DB_KEYS.LEADS, []),
        notifications: load(DB_KEYS.NOTIFICATIONS, []),
        social: load(DB_KEYS.SOCIAL, []),
        editorial: load(DB_KEYS.EDITORIAL, []),
        products: load(DB_KEYS.PRODUCTS, DEFAULT_PRODUCTS),
        funnels: load(DB_KEYS.FUNNELS, []),
        academy: load(DB_KEYS.ACADEMY, INITIAL_ACADEMY_MODULES),
        automations: load(DB_KEYS.AUTOMATIONS, INITIAL_RULES),
        logs: load(DB_KEYS.LOGS, [])
      }
    };

    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(backupData, null, 2));
    const downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href", dataStr);
    downloadAnchorNode.setAttribute("download", `Aureus_Backup_${new Date().toISOString().split('T')[0]}.json`);
    document.body.appendChild(downloadAnchorNode);
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
  },

  // 2. Ripristina Backup (Carica da file)
  restoreBackup: (file: File): Promise<boolean> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = (event) => {
        try {
          if (event.target?.result && typeof event.target.result === 'string') {
            const parsed = JSON.parse(event.target.result);
            if (parsed.data) {
              // Ripristina tutto in LocalStorage
              save(DB_KEYS.USER, parsed.data.user);
              save(DB_KEYS.TASKS, parsed.data.tasks);
              save(DB_KEYS.LEADS, parsed.data.leads);
              save(DB_KEYS.NOTIFICATIONS, parsed.data.notifications);
              save(DB_KEYS.SOCIAL, parsed.data.social);
              save(DB_KEYS.EDITORIAL, parsed.data.editorial);
              save(DB_KEYS.PRODUCTS, parsed.data.products);
              save(DB_KEYS.FUNNELS, parsed.data.funnels);
              save(DB_KEYS.ACADEMY, parsed.data.academy);
              save(DB_KEYS.AUTOMATIONS, parsed.data.automations);
              save(DB_KEYS.LOGS, parsed.data.logs);
              resolve(true);
            } else {
              reject(new Error("File di backup non valido"));
            }
          }
        } catch (e) {
          reject(e);
        }
      };
      reader.readAsText(file);
    });
  },

  // 3. Reset Totale (Factory Reset)
  factoryReset: () => {
    localStorage.clear();
    window.location.reload();
  }
};