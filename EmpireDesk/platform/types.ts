
export type Department = 'SOCIAL' | 'EDITORIAL' | 'SALES' | 'INFOBUSINESS' | 'GENERAL';

export enum TaskStatus {
  TODO = 'TODO',
  IN_PROGRESS = 'IN_PROGRESS',
  REVIEW = 'REVIEW',
  DONE = 'DONE',
}

export type UserRole = 'ADMIN' | 'MEMBER' | 'CLIENT';

export interface User {
  id: string;
  name: string;
  role: UserRole;
  title: string;
  tags: string[]; 
  email?: string; 
  status?: 'ACTIVE' | 'INACTIVE'; 
  lastLogin?: string; 
  xp?: number;
  level?: number;
  accessCode?: string; // New field for Client Authentication
}

export interface Subtask {
  id: string;
  title: string;
  isCompleted: boolean;
}

export interface TaskComment {
  id: string;
  authorId: string;
  content: string;
  date: string;
}

export interface TaskAttachment {
  id: string;
  name: string;
  url: string;
  type: 'IMAGE' | 'DOC';
}

export interface Task {
  id: string;
  title: string;
  description?: string;
  status: TaskStatus;
  department: Department;
  assignee?: string;
  dueDate: string;
  priority: 'LOW' | 'MEDIUM' | 'HIGH';
  relatedLeadId?: string; 
  subtasks?: Subtask[];
  comments?: TaskComment[];
  attachments?: TaskAttachment[];
}

export enum LeadStage {
  NEW = 'NEW',
  CONTACTED = 'CONTACTED',
  PROPOSAL = 'PROPOSAL',
  NEGOTIATION = 'NEGOTIATION',
  CLOSED_WON = 'CLOSED_WON',
  CLOSED_LOST = 'CLOSED_LOST',
}

export type ActivityType = 'NOTE' | 'CALL' | 'EMAIL' | 'STATUS_CHANGE' | 'SYSTEM' | 'INVOICE' | 'PROPOSAL';

export interface LeadActivity {
  id: string;
  type: ActivityType;
  content: string;
  date: string;
  author: string;
}

export type ClientTier = 'STANDARD' | 'GOLD' | 'PLATINUM';

export interface Lead {
  id: string;
  companyName: string;
  contactPerson: string;
  role?: string; 
  value: number;
  stage: LeadStage;
  email: string;
  phone?: string;
  website?: string;
  serviceInterest: 'WEBSITE' | 'FUNNEL' | 'AUTOMATION' | 'CONSULTING';
  lastContact: string;
  sourceFunnelId?: string; 
  interestedProductId?: string;
  tags: string[];
  score: number; 
  notes: string;
  history: LeadActivity[];
  probability: number; 
  expectedCloseDate?: string;
  isClient?: boolean;
  clientTier?: ClientTier;
  onboardingDate?: string;
  ltv?: number; 
  vatNumber?: string;
}

export type InvoiceStatus = 'DRAFT' | 'SENT' | 'PAID' | 'OVERDUE';

export interface Invoice {
  id: string;
  number: string;
  date: string;
  dueDate: string;
  amount: number;
  status: InvoiceStatus;
  leadId: string; 
  items: { description: string; quantity: number; price: number }[];
}

export type ProposalStatus = 'DRAFT' | 'SENT' | 'ACCEPTED' | 'REJECTED';

export interface Proposal {
  id: string;
  title: string;
  leadId: string;
  date: string;
  validUntil: string;
  status: ProposalStatus;
  items: { productId: string; name: string; price: number; quantity: number }[];
  totalAmount: number;
  discount: number; 
  finalAmount: number;
}

export interface CRMDocument {
  id: string;
  title: string;
  type: 'PDF' | 'DOC' | 'IMG' | 'CONTRACT';
  uploadDate: string;
  leadId: string;
  size: string;
}

export interface Notification {
  id: string;
  message: string;
  date: string;
  read: boolean;
  type: 'INFO' | 'SUCCESS' | 'WARNING';
}

export interface Integration {
  id: string;
  name: string;
  provider: 'STRIPE' | 'GOOGLE' | 'SLACK' | 'WHATSAPP' | 'OPENAI';
  status: 'CONNECTED' | 'DISCONNECTED' | 'ERROR';
  lastSync?: string;
  icon?: string;
}

export interface BillingInvoice {
  id: string;
  date: string;
  amount: number;
  status: 'PAID' | 'PENDING';
  plan: string;
}

export type TriggerType = 'LEAD_CREATED' | 'LEAD_WON' | 'TASK_COMPLETED';
export type ActionType = 'CREATE_TASK' | 'SEND_EMAIL' | 'NOTIFY_SLACK';

export interface AutomationRule {
  id: string;
  name: string;
  active: boolean;
  trigger: TriggerType;
  action: ActionType;
  lastRun?: string;
  runCount: number;
}

export interface AutomationLog {
  id: string;
  ruleName: string;
  date: string;
  status: 'SUCCESS' | 'FAILED';
  details: string;
}

export type SocialPlatform = 'INSTAGRAM_REEL' | 'INSTAGRAM_POST' | 'INSTAGRAM_STORY';
export type SocialStatus = 'IDEA' | 'SCRIPTING' | 'EDITING' | 'READY' | 'APPROVED' | 'PUBLISHED';

export interface SocialPost {
  id: string;
  title: string;
  platform: SocialPlatform;
  status: SocialStatus;
  scheduledDate?: string;
  assignee?: string;
}

export type EditorialType = 'BOOK_CHAPTER' | 'PDF_MAGNET' | 'ARTICLE';
export type EditorialStatus = 'DRAFT' | 'REVIEW' | 'EDITING' | 'COMPLETED';

export interface EditorialItem {
  id: string;
  title: string;
  type: EditorialType;
  status: EditorialStatus;
  wordCount?: number;
  assignee?: string;
}

export interface CourseLesson {
  id: string;
  title: string;
  type: 'VIDEO' | 'TEXT' | 'QUIZ';
  status: 'DRAFT' | 'RECORDED' | 'PUBLISHED';
  duration?: string;
}

export interface CourseModule {
  id: string;
  title: string;
  status: 'PLANNED' | 'RECORDING' | 'EDITING' | 'UPLOADED';
  duration?: string;
  lessons: CourseLesson[]; 
}

export type ProductCategory = 'AGENCY' | 'INFO';
export type ServiceType = 'WEBSITE' | 'AUTOMATION' | 'SOCIAL_GROWTH' | 'CONSULTING';

export interface InfobusinessProduct {
  id: string;
  title: string;
  price: number;
  sales: number;
  modules: CourseModule[];
  category?: ProductCategory;
  serviceType?: ServiceType;
}

// --- ADVANCED FUNNEL TYPES ---

export type FunnelStepType = 'TRAFFIC' | 'LANDING' | 'OPTIN' | 'VSL' | 'CHECKOUT' | 'UPSELL' | 'DOWNSELL' | 'THANK_YOU' | 'EMAIL' | 'TAG_CRM' | 'WAIT' | 'CONDITION';

export interface FunnelPageElement {
  id: string;
  type: 'VIDEO' | 'IMAGE' | 'TEXT' | 'FORM' | 'BUTTON' | 'TIMER' | 'TESTIMONIAL' | 'FAQ' | 'BULLETS';
  label: string;
}

export interface FunnelSimulationMetrics {
  trafficIn: number;
  conversionRate: number; // 0-100 percentage
  trafficOut: number;
  revenue: number;
  cost: number;
  profit: number;
}

export interface FunnelStep {
  id: string;
  type: FunnelStepType;
  label: string;
  x: number;
  y: number;
  
  // Visual Customization
  elements?: FunnelPageElement[]; // The DNA of the page
  
  // Financial & Simulation Data
  metrics: FunnelSimulationMetrics;
  
  // Configuration
  config: {
    // Traffic
    trafficSource?: 'META' | 'GOOGLE' | 'TIKTOK' | 'ORGANIC' | 'EMAIL';
    cpc?: number; // Cost per Click
    
    // Product
    productId?: string;
    productName?: string;
    price?: number;
    
    // Page
    url?: string;
    isSplitTest?: boolean;
    
    // Logic
    delayHours?: number;
    tagName?: string;
    
    [key: string]: any;
  };
}

export type ConnectionType = 'STANDARD' | 'YES_PATH' | 'NO_PATH';

export interface FunnelConnection {
  id: string;
  fromStepId: string;
  toStepId: string;
  type: ConnectionType;
}

export interface Funnel {
  id: string;
  name: string;
  status: 'DRAFT' | 'ACTIVE' | 'PAUSED';
  steps: FunnelStep[];
  connections: FunnelConnection[];
  
  // Global Simulation
  totalRevenue?: number;
  totalCost?: number;
  totalProfit?: number;
  roas?: number;
}

export interface KPIMetric {
  label: string;
  value: string;
  trend: number;
  trendLabel: string;
  icon: string;
}

export interface ChartDataPoint {
  name: string;
  value: number;
  value2?: number;
}

export type LessonType = 'TEXT' | 'VIDEO' | 'PDF';

export interface AcademyLesson {
  id: string;
  moduleId: string;
  title: string;
  type: LessonType;
  content: string; 
  durationMinutes: number;
  isCompleted: boolean;
}

export interface AcademyModule {
  id: string;
  categoryId: string;
  title: string;
  description: string;
  lessons: AcademyLesson[];
}

export interface AcademyCategory {
  id: string;
  title: string;
  description: string;
  icon: string; 
  color: string; 
}

export type VaultItemType = 'FOLDER' | 'IMAGE' | 'PDF' | 'VIDEO' | 'DOC' | 'ARCHIVE';

export interface VaultItem {
  id: string;
  parentId: string | null; 
  name: string;
  type: VaultItemType;
  size?: string;
  updatedAt: string;
  owner?: string;
  isShared?: boolean;
  url?: string; 
}

export interface Badge {
  id: string;
  title: string;
  description: string;
  icon: string; 
  rarity: 'COMMON' | 'RARE' | 'EPIC' | 'LEGENDARY';
  earnedDate?: string;
}

export interface Quest {
  id: string;
  title: string;
  description: string;
  progress: number;
  total: number;
  rewardXp: number;
  isCompleted: boolean;
  type: 'DAILY' | 'WEEKLY';
}
