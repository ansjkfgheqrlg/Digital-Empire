
import React, { useState, useEffect } from 'react';
import { Layout } from './components/Layout';
import { LoginScreen } from './components/LoginScreen';
import { DashboardHome } from './components/DashboardHome';
import { KanbanBoard } from './components/KanbanBoard';
import { SalesPipeline } from './components/SalesPipeline';
import { TeamManagement } from './components/TeamManagement';
import { SocialMedia } from './components/SocialMedia';
import { Editorial } from './components/Editorial';
import { Infobusiness } from './components/Infobusiness';
import { Academy } from './components/Academy';
import { Guide } from './components/Guide';
import { Settings } from './components/Settings';
import { Analytics } from './components/Analytics';
import { MasterCalendar } from './components/MasterCalendar';
import { CommandPalette } from './components/CommandPalette';
import { AureusAI } from './components/AureusAI';
import { Automations } from './components/Automations';
import { Finance } from './components/Finance';
import { Vault } from './components/Vault';
import { WarRoom } from './components/WarRoom';
import { ClientPortal } from './components/ClientPortal';
import { TheArena } from './components/TheArena';
import { BrandLanding } from './components/BrandLanding'; // Importato BrandLanding
import { User, Task, Lead, Notification, SocialPost, EditorialItem, InfobusinessProduct, TaskStatus, Funnel, SocialStatus, EditorialStatus, AcademyModule, AcademyCategory, AcademyLesson, AutomationRule, TriggerType, AutomationLog, LeadActivity } from './types';
import { INITIAL_ACADEMY_CATEGORIES } from './constants';
import { Hexagon } from 'lucide-react';
import { DB } from './utils/database';

const App: React.FC = () => {
  // PERSISTENT USER SESSION via DB
  const [currentUser, setCurrentUser] = useState<User | null>(() => DB.user.get());
  const [currentPath, setCurrentPath] = useState('/');
  const [isBooting, setIsBooting] = useState(true);

  // --- STATE INITIALIZATION FROM DB ---
  const [tasks, setTasks] = useState<Task[]>(() => DB.tasks.getAll());
  const [leads, setLeads] = useState<Lead[]>(() => DB.leads.getAll());
  const [notifications, setNotifications] = useState<Notification[]>(() => DB.notifications.getAll());
  const [socialPosts, setSocialPosts] = useState<SocialPost[]>(() => DB.social.getAll());
  const [editorialItems, setEditorialItems] = useState<EditorialItem[]>(() => DB.editorial.getAll());
  const [products, setProducts] = useState<InfobusinessProduct[]>(() => DB.products.getAll());
  const [funnels, setFunnels] = useState<Funnel[]>(() => DB.funnels.getAll());
  const [academyModules, setAcademyModules] = useState<AcademyModule[]>(() => DB.academy.getAll());
  const [automationRules, setAutomationRules] = useState<AutomationRule[]>(() => DB.automations.getRules());
  const [automationLogs, setAutomationLogs] = useState<AutomationLog[]>(() => DB.automations.getLogs());

  // --- ROBUST SAVING EFFECTS (Save on every change) ---
  useEffect(() => { DB.user.save(currentUser); }, [currentUser]);
  useEffect(() => { DB.tasks.save(tasks); }, [tasks]);
  useEffect(() => { DB.leads.save(leads); }, [leads]);
  useEffect(() => { DB.notifications.save(notifications); }, [notifications]);
  useEffect(() => { DB.social.save(socialPosts); }, [socialPosts]);
  useEffect(() => { DB.editorial.save(editorialItems); }, [editorialItems]);
  useEffect(() => { DB.products.save(products); }, [products]);
  useEffect(() => { DB.funnels.save(funnels); }, [funnels]);
  useEffect(() => { DB.academy.save(academyModules); }, [academyModules]);
  useEffect(() => { 
      DB.automations.saveRules(automationRules);
      DB.automations.saveLogs(automationLogs); 
  }, [automationRules, automationLogs]);

  // Boot Effect
  useEffect(() => {
      const timer = setTimeout(() => setIsBooting(false), 2000);
      return () => clearTimeout(timer);
  }, []);

  // --- HELPER: Notifications ---
  const addNotification = (message: string, type: 'INFO' | 'SUCCESS' | 'WARNING' = 'INFO') => {
      const newNotif: Notification = {
          id: `n-${Date.now()}-${Math.random()}`,
          message,
          date: new Date().toISOString(),
          read: false,
          type
      };
      setNotifications(prev => [newNotif, ...prev]);
  };

  // --- AUTOMATION ENGINE ---
  const triggerAutomation = (trigger: TriggerType, payload: any) => {
      const activeRules = automationRules.filter(r => r.active && r.trigger === trigger);
      
      if (activeRules.length === 0) return;

      activeRules.forEach(rule => {
          let details = '';
          
          // 1. Execute Action
          if (rule.action === 'CREATE_TASK') {
              const newTask: Task = {
                  id: `auto-task-${Date.now()}`,
                  title: `Onboarding: ${payload.companyName || 'Nuovo Cliente'}`,
                  status: TaskStatus.TODO,
                  department: 'GENERAL',
                  priority: 'HIGH',
                  dueDate: new Date().toISOString().split('T')[0],
                  description: 'Task generata automaticamente dal sistema di automazione.',
                  subtasks: [
                      { id: 'sub-1', title: 'Inviare contratto', isCompleted: false },
                      { id: 'sub-2', title: 'Setup cartella Drive', isCompleted: false },
                      { id: 'sub-3', title: 'Kickoff Call', isCompleted: false }
                  ]
              };
              setTasks(prev => [newTask, ...prev]);
              details = `Task creata per ${payload.companyName || 'Unknown'}`;
              addNotification(`⚡ Automazione: ${details}`, 'SUCCESS');
          } 
          else if (rule.action === 'NOTIFY_SLACK') {
              details = `Messaggio inviato al canale #sales`;
              addNotification(`💬 Slack: ${details}`, 'INFO');
          }
          else if (rule.action === 'SEND_EMAIL') {
              // REAL LOGIC FOR EMAIL AUTOMATION
              const leadEmail = payload.email;
              
              if (leadEmail) {
                  details = `Email di benvenuto inviata a ${leadEmail}`;
                  addNotification(`📧 Automazione: ${details}`, 'SUCCESS');
                  
                  // UPDATE CRM HISTORY TO REFLECT EMAIL SENT
                  if (trigger === 'LEAD_CREATED' && payload.id) {
                      setLeads(currentLeads => currentLeads.map(l => {
                          if (l.id === payload.id) {
                              const emailActivity: LeadActivity = {
                                  id: `auto-mail-${Date.now()}`,
                                  type: 'EMAIL',
                                  content: `[AUREUS BOT] Inviata Email di Benvenuto automatica a ${leadEmail}.\nOggetto: "Benvenuto in Aureus - I prossimi step"`,
                                  date: new Date().toISOString(),
                                  author: 'System'
                              };
                              return {
                                  ...l,
                                  history: [emailActivity, ...(l.history || [])]
                              };
                          }
                          return l;
                      }));
                  }
              } else {
                  details = "Fallito: Email mancante nel Lead";
                  addNotification(`⚠️ Errore Automazione: ${details}`, 'WARNING');
              }
          }

          // 2. Update Stats
          setAutomationRules(prev => prev.map(r => 
              r.id === rule.id 
              ? { ...r, runCount: r.runCount + 1, lastRun: 'Adesso' } 
              : r
          ));

          // 3. Log Execution
          const newLog: AutomationLog = {
              id: `log-${Date.now()}-${Math.random()}`,
              ruleName: rule.name,
              date: new Date().toLocaleTimeString(),
              status: details.includes('Fallito') ? 'FAILED' : 'SUCCESS',
              details: details
          };
          setAutomationLogs(prev => [newLog, ...prev].slice(0, 50)); // Keep last 50 logs
      });
  };

  const handleTestRule = (ruleId: string) => {
      const rule = automationRules.find(r => r.id === ruleId);
      if (!rule) return;
      
      const mockPayload: any = {
          companyName: 'Azienda Test SRL',
          email: 'cliente.test@demo.com',
          title: 'Task di Prova',
          contactPerson: 'Mario Rossi',
          id: 'test-lead-id' 
      };

      let details = '';
      if (rule.action === 'CREATE_TASK') {
          setTasks(prev => [{
              id: `test-task-${Date.now()}`,
              title: `[TEST] Onboarding: ${mockPayload.companyName}`,
              status: TaskStatus.TODO, department: 'GENERAL', priority: 'LOW', dueDate: new Date().toISOString().split('T')[0],
              subtasks: [], comments: []
          }, ...prev]);
          details = `[TEST MODE] Task creata per ${mockPayload.companyName}`;
          addNotification(`⚡ Test Riuscito: ${rule.name}`, 'SUCCESS');
      } else if (rule.action === 'NOTIFY_SLACK') {
          details = `[TEST MODE] Messaggio inviato a Slack`;
          addNotification(`💬 Test Riuscito: ${rule.name}`, 'SUCCESS');
      } else if (rule.action === 'SEND_EMAIL') {
          details = `[TEST MODE] Email inviata a ${mockPayload.email}`;
          addNotification(`📧 Test Riuscito: ${rule.name}`, 'SUCCESS');
      }

      const newLog: AutomationLog = {
          id: `log-${Date.now()}`,
          ruleName: rule.name,
          date: new Date().toLocaleTimeString(),
          status: 'SUCCESS',
          details: details
      };
      setAutomationLogs(prev => [newLog, ...prev]);

      setAutomationRules(prev => prev.map(r => r.id === ruleId ? { ...r, runCount: r.runCount + 1, lastRun: 'Adesso (Test)' } : r));
  };

  // --- ACTIONS ---

  // ... (Mapping Helpers)
  const mapTaskToSocialStatus = (status: TaskStatus): SocialStatus => {
    if (status === TaskStatus.DONE) return 'PUBLISHED';
    if (status === TaskStatus.REVIEW) return 'READY';
    if (status === TaskStatus.IN_PROGRESS) return 'SCRIPTING';
    return 'IDEA';
  };

  const mapSocialToTaskStatus = (status: SocialStatus): TaskStatus => {
    if (status === 'PUBLISHED') return TaskStatus.DONE;
    if (status === 'APPROVED') return TaskStatus.DONE; 
    if (status === 'READY') return TaskStatus.REVIEW;
    if (status === 'EDITING' || status === 'SCRIPTING') return TaskStatus.IN_PROGRESS;
    return TaskStatus.TODO;
  };

  const mapTaskToEditorialStatus = (status: TaskStatus): EditorialStatus => {
    if (status === TaskStatus.DONE) return 'COMPLETED';
    if (status === TaskStatus.REVIEW) return 'REVIEW';
    if (status === TaskStatus.IN_PROGRESS) return 'EDITING';
    return 'DRAFT';
  };

  const mapEditorialToTaskStatus = (status: EditorialStatus): TaskStatus => {
    if (status === 'COMPLETED') return TaskStatus.DONE;
    if (status === 'REVIEW') return TaskStatus.REVIEW;
    if (status === 'EDITING') return TaskStatus.IN_PROGRESS;
    return TaskStatus.TODO;
  };

  // 1. ADD TASK 
  const handleAddTask = (task: Task) => {
    setTasks(prev => [...prev, task]);
    addNotification(`Nuova task creata: ${task.title}`);
    
    // Sync Logic... (Kept same)
    if (task.department === 'SOCIAL') {
       if (!socialPosts.find(p => p.id === task.id)) {
           const newPost: SocialPost = {
               id: task.id, title: task.title, platform: 'INSTAGRAM_REEL', 
               status: mapTaskToSocialStatus(task.status), scheduledDate: task.dueDate, assignee: task.assignee
           };
           setSocialPosts(prev => [...prev, newPost]);
       }
    }
    if (task.department === 'EDITORIAL') {
       if (!editorialItems.find(i => i.id === task.id)) {
           const newItem: EditorialItem = {
               id: task.id, title: task.title, type: 'BOOK_CHAPTER', 
               status: mapTaskToEditorialStatus(task.status), wordCount: 0, assignee: task.assignee
           };
           setEditorialItems(prev => [...prev, newItem]);
       }
    }
    
    triggerAutomation('TASK_COMPLETED', task); 
  };

  // 2. UPDATE TASK
  const handleUpdateTask = (updatedTask: Task) => {
    setTasks(tasks.map(t => t.id === updatedTask.id ? updatedTask : t));
    
    if (updatedTask.status === TaskStatus.DONE) {
       // Only trigger if it wasn't already done
       const prevTask = tasks.find(t => t.id === updatedTask.id);
       if (prevTask && prevTask.status !== TaskStatus.DONE) {
           addNotification(`Task completata: ${updatedTask.title}`, 'SUCCESS');
           triggerAutomation('TASK_COMPLETED', updatedTask);
       }
    }

    // Sync Logic... (Kept same)
    if (updatedTask.department === 'SOCIAL') {
        setSocialPosts(prev => prev.map(p => p.id === updatedTask.id ? { ...p, status: mapTaskToSocialStatus(updatedTask.status) } : p));
    }
    if (updatedTask.department === 'EDITORIAL') {
        setEditorialItems(prev => prev.map(i => i.id === updatedTask.id ? { ...i, status: mapTaskToEditorialStatus(updatedTask.status) } : i));
    }
  };

  // ... (Social/Editorial Handlers)
  const handleAddPost = (post: SocialPost) => {
    setSocialPosts(prev => [...prev, post]);
    addNotification(`Nuovo post pianificato: ${post.title}`);
    if (!tasks.find(t => t.id === post.id)) {
        const newTask: Task = {
            id: post.id, title: post.title, department: 'SOCIAL',
            status: mapSocialToTaskStatus(post.status), dueDate: post.scheduledDate || new Date().toISOString().split('T')[0],
            priority: 'MEDIUM', assignee: post.assignee
        };
        setTasks(prev => [...prev, newTask]);
    }
  };

  const handleUpdatePostStatus = (id: string, status: SocialStatus) => {
    setSocialPosts(socialPosts.map(p => p.id === id ? { ...p, status } : p));
    setTasks(prev => prev.map(t => t.id === id ? { ...t, status: mapSocialToTaskStatus(status) } : t));
  };

  const handleAddItem = (item: EditorialItem) => {
    setEditorialItems(prev => [...prev, item]);
    addNotification(`Nuovo progetto editoriale: ${item.title}`);
    if (!tasks.find(t => t.id === item.id)) {
        const newTask: Task = {
            id: item.id, title: item.title, department: 'EDITORIAL',
            status: mapEditorialToTaskStatus(item.status), dueDate: new Date().toISOString().split('T')[0],
            priority: 'MEDIUM', assignee: item.assignee
        };
        setTasks(prev => [...prev, newTask]);
    }
  };

  const handleUpdateItemStatus = (id: string, status: EditorialStatus) => {
    setEditorialItems(editorialItems.map(i => i.id === id ? { ...i, status } : i));
    setTasks(prev => prev.map(t => t.id === id ? { ...t, status: mapEditorialToTaskStatus(status) } : t));
  };

  // ... (Product/Funnel Handlers)
  const handleAddProduct = (prod: InfobusinessProduct) => { setProducts(prev => [...prev, prod]); addNotification(`Nuovo prodotto creato: ${prod.title}`); };
  const handleAddFunnel = (funnel: Funnel) => { setFunnels(prev => [...prev, funnel]); addNotification(`Nuovo funnel creato: ${funnel.name}`); };
  const handleUpdateFunnel = (updatedFunnel: Funnel) => { setFunnels(funnels.map(f => f.id === updatedFunnel.id ? updatedFunnel : f)); };

  // 7. LEAD ACTIONS (UPDATED WITH AUTOMATION)
  const handleAddLead = (lead: Lead) => {
    setLeads(prev => [...prev, lead]);
    addNotification(`Nuovo lead inserito: ${lead.companyName}`);
    triggerAutomation('LEAD_CREATED', lead);
  };

  const handleUpdateLead = (updatedLead: Lead) => {
    const prevLead = leads.find(l => l.id === updatedLead.id);
    setLeads(prev => prev.map(l => l.id === updatedLead.id ? updatedLead : l));
    
    if (updatedLead.stage === 'CLOSED_WON' && prevLead?.stage !== 'CLOSED_WON') {
        addNotification(`Lead convertito! ${updatedLead.companyName}`, 'SUCCESS');
        triggerAutomation('LEAD_WON', updatedLead);
    }
  };

  // 8. ACADEMY & AUTOMATION HANDLERS
  const handleToggleLessonComplete = (moduleId: string, lessonId: string) => {
      setAcademyModules(prev => prev.map(mod => {
          if (mod.id !== moduleId) return mod;
          return { ...mod, lessons: mod.lessons.map(les => les.id !== lessonId ? les : { ...les, isCompleted: !les.isCompleted }) };
      }));
  };
  const handleAddModule = (categoryId: string, title: string) => {
      const newModule: AcademyModule = { id: `mod-${Date.now()}`, categoryId, title, description: 'Nuovo modulo in costruzione.', lessons: [] };
      setAcademyModules(prev => [...prev, newModule]);
      addNotification('Modulo creato. Aggiungi lezioni.', 'SUCCESS');
  };
  const handleUpdateModule = (moduleId: string, updates: Partial<AcademyModule>) => { setAcademyModules(prev => prev.map(m => m.id === moduleId ? { ...m, ...updates } : m)); };
  const handleDeleteModule = (moduleId: string) => { setAcademyModules(prev => prev.filter(m => m.id !== moduleId)); addNotification('Modulo eliminato.'); };
  const handleAddLesson = (moduleId: string, title: string) => {
      const newLesson: AcademyLesson = { id: `les-${Date.now()}`, moduleId, title, type: 'TEXT', content: '# Nuovo Titolo\nScrivi qui la tua guida...', durationMinutes: 10, isCompleted: false };
      setAcademyModules(prev => prev.map(m => m.id !== moduleId ? m : { ...m, lessons: [...m.lessons, newLesson] }));
  };
  const handleUpdateLesson = (moduleId: string, lessonId: string, updates: Partial<AcademyLesson>) => {
      setAcademyModules(prev => prev.map(m => m.id !== moduleId ? m : { ...m, lessons: m.lessons.map(l => l.id === lessonId ? { ...l, ...updates } : l) }));
  };
  const handleDeleteLesson = (moduleId: string, lessonId: string) => {
      setAcademyModules(prev => prev.map(m => m.id !== moduleId ? m : { ...m, lessons: m.lessons.filter(l => l.id !== lessonId) }));
  };

  // Automation Management Handlers
  const handleToggleRule = (id: string) => {
      setAutomationRules(prev => prev.map(r => r.id === id ? { ...r, active: !r.active } : r));
  };
  
  const handleAddRule = (rule: AutomationRule) => {
      setAutomationRules(prev => [...prev, rule]);
      addNotification('Nuova regola di automazione creata.');
  };

  // --- RENDERING ---

  if (!currentUser) {
    return <LoginScreen onLogin={setCurrentUser} />;
  }

  if (isBooting) {
      return (
          <div className="min-h-screen bg-black flex flex-col items-center justify-center font-mono text-platinum-500">
              <Hexagon className="w-16 h-16 text-white mb-8 animate-pulse" strokeWidth={1} />
              <div className="w-64 h-1 bg-gray-800 rounded-full overflow-hidden mb-2">
                  <div className="h-full bg-white animate-[width_2s_ease-in-out_forwards]" style={{width: '0%'}}></div>
              </div>
              <p className="text-xs tracking-widest uppercase">Initializing Aureus Database...</p>
          </div>
      );
  }

  if (currentUser.role === 'CLIENT') {
      return <ClientPortal currentUser={currentUser} onLogout={() => setCurrentUser(null)} posts={socialPosts} tasks={tasks} onUpdatePostStatus={handleUpdatePostStatus} />;
  }

  if (currentPath === '/brand-home') {
      return <BrandLanding onNavigate={setCurrentPath} />;
  }

  if (currentPath === '/war-room') {
      return (
          <>
            <WarRoom leads={leads} tasks={tasks} onNavigate={setCurrentPath} />
            <CommandPalette onNavigate={setCurrentPath} />
          </>
      );
  }

  const theme = currentPath.startsWith('/infobusiness') ? 'diamond' : 'silver';

  const renderContent = () => {
    switch (currentPath) {
      case '/': return <DashboardHome currentUser={currentUser} tasks={tasks} leads={leads} products={products} />;
      case '/tasks': return <KanbanBoard tasks={tasks} onAddTask={handleAddTask} onUpdateTask={handleUpdateTask} />;
      case '/crm': return <SalesPipeline leads={leads} funnels={funnels} products={products} tasks={tasks} onAddLead={handleAddLead} onUpdateLead={handleUpdateLead} />;
      case '/social': return <SocialMedia posts={socialPosts} onAddPost={handleAddPost} onUpdateStatus={handleUpdatePostStatus} />;
      case '/editorial': return <Editorial items={editorialItems} onAddItem={handleAddItem} onUpdateStatus={handleUpdateItemStatus} />;
      case '/infobusiness': return <Infobusiness products={products} onAddProduct={handleAddProduct} funnels={funnels} onAddFunnel={handleAddFunnel} onUpdateFunnel={handleUpdateFunnel} />;
      case '/academy': return <Academy categories={INITIAL_ACADEMY_CATEGORIES} modules={academyModules} isAdmin={currentUser.role === 'ADMIN'} onToggleLessonComplete={handleToggleLessonComplete} onAddModule={handleAddModule} onUpdateModule={handleUpdateModule} onDeleteModule={handleDeleteModule} onAddLesson={handleAddLesson} onUpdateLesson={handleUpdateLesson} onDeleteLesson={handleDeleteLesson} />;
      case '/team': return <TeamManagement currentUser={currentUser} tasks={tasks} />;
      case '/guide': return <Guide />;
      case '/settings': return <Settings currentUser={currentUser} />;
      case '/analytics': return <Analytics leads={leads} tasks={tasks} products={products} />;
      case '/calendar': return <MasterCalendar tasks={tasks} posts={socialPosts} leads={leads} />;
      case '/automations': return <Automations rules={automationRules} logs={automationLogs} onToggleRule={handleToggleRule} onAddRule={handleAddRule} onTestRule={handleTestRule} />;
      case '/finance': return <Finance />;
      case '/vault': return <Vault />;
      case '/arena': return <TheArena currentUser={currentUser} tasks={tasks} leads={leads} />;
      default: return <DashboardHome currentUser={currentUser} tasks={tasks} leads={leads} products={products} />;
    }
  };

  return (
    <Layout 
      currentUser={currentUser} 
      onLogout={() => setCurrentUser(null)}
      currentPath={currentPath}
      onNavigate={setCurrentPath}
      notifications={notifications}
      onClearNotifications={() => setNotifications([])}
      theme={theme}
      searchData={{ leads, tasks, products }}
    >
      {renderContent()}
      <AureusAI />
      <CommandPalette onNavigate={setCurrentPath} />
    </Layout>
  );
};

export default App;
