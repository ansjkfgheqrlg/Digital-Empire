
import React, { useState, useEffect, useRef } from 'react';
import { NAV_ITEMS } from '../constants';
import { Menu, Bell, Search, Diamond, LogOut, Hexagon, User, Briefcase, CheckSquare, Box, Monitor, Wifi } from 'lucide-react';
import { User as UserType, Notification, Lead, Task, InfobusinessProduct } from '../types';

interface SearchData {
  leads: Lead[];
  tasks: Task[];
  products: InfobusinessProduct[];
}

interface LayoutProps {
  children: React.ReactNode;
  currentUser: UserType;
  onLogout: () => void;
  currentPath: string;
  onNavigate: (path: string) => void;
  notifications: Notification[];
  onClearNotifications: () => void;
  theme?: 'silver' | 'diamond';
  searchData?: SearchData; // Added for Global Search
}

export const Layout: React.FC<LayoutProps> = ({ 
  children, 
  currentUser, 
  onLogout, 
  currentPath, 
  onNavigate,
  notifications,
  onClearNotifications,
  theme = 'silver',
  searchData
}) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isNotifOpen, setIsNotifOpen] = useState(false);
  
  // Search State
  const [searchQuery, setSearchQuery] = useState('');
  const [isSearchFocused, setIsSearchFocused] = useState(false);
  const [searchResults, setSearchResults] = useState<{type: string, id: string, title: string, subtitle?: string, icon: any, path?: string}[]>([]);
  const searchRef = useRef<HTMLDivElement>(null);

  const getInitials = (name: string) => name.substring(0, 2).toUpperCase();
  const unreadCount = notifications.filter(n => !n.read).length;

  const isDiamond = theme === 'diamond';
  
  // Background logic - Deep Ambient
  const bgClass = isDiamond ? 'bg-[#050505]' : 'bg-[#020202]'; 
  const bgGradient = isDiamond 
    ? 'radial-gradient(circle at 50% 0%, rgba(34,211,238,0.05) 0%, transparent 60%)' 
    : 'radial-gradient(circle at 50% 0%, rgba(203,213,225,0.08) 0%, transparent 60%)';

  const logoIcon = isDiamond 
    ? <Diamond className="w-5 h-5 text-diamond-400" /> 
    : <Hexagon className="w-5 h-5 text-white" />;
    
  const logoText = isDiamond ? 'text-diamond-400' : 'text-transparent bg-clip-text bg-gradient-to-b from-white to-platinum-400';

  // Navigation Item Styles - "Ghost" Design
  const activeItemClass = isDiamond 
    ? 'opacity-100 text-diamond-400 font-bold drop-shadow-[0_0_8px_rgba(34,211,238,0.5)]' 
    : 'opacity-100 text-white font-bold drop-shadow-[0_0_8px_rgba(255,255,255,0.5)]';
    
  const inactiveItemClass = 'opacity-40 hover:opacity-100 text-platinum-200 transition-all duration-300 hover:scale-105';

  // Level Calculation for Sidebar
  const userLevel = currentUser.level || 1;
  const userXP = currentUser.xp || 0;
  const nextLevelXP = Math.pow(userLevel + 1, 2) * 100;
  const currentLevelBaseXP = Math.pow(userLevel, 2) * 100;
  const progressPercent = ((userXP - currentLevelBaseXP) / (nextLevelXP - currentLevelBaseXP)) * 100;

  // --- SEARCH LOGIC ---
  useEffect(() => {
      const handleClickOutside = (event: MouseEvent) => {
        if (searchRef.current && !searchRef.current.contains(event.target as Node)) {
          setIsSearchFocused(false);
        }
      };
      document.addEventListener("mousedown", handleClickOutside);
      return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  useEffect(() => {
      if (!searchQuery.trim() || !searchData) {
          setSearchResults([]);
          return;
      }
      
      const q = searchQuery.toLowerCase();
      const results = [];

      // 1. Pages
      NAV_ITEMS.forEach(item => {
          if (item.label.toLowerCase().includes(q)) {
              results.push({ type: 'PAGE', id: item.path, title: item.label, subtitle: 'Navigazione', icon: Box, path: item.path });
          }
      });

      // 2. Leads
      searchData.leads.forEach(l => {
          if (l.companyName.toLowerCase().includes(q) || l.contactPerson.toLowerCase().includes(q)) {
              results.push({ type: 'LEAD', id: l.id, title: l.companyName, subtitle: `Contatto: ${l.contactPerson}`, icon: User, path: '/crm' });
          }
      });

      // 3. Tasks
      searchData.tasks.forEach(t => {
          if (t.title.toLowerCase().includes(q)) {
              results.push({ type: 'TASK', id: t.id, title: t.title, subtitle: t.status, icon: CheckSquare, path: '/tasks' });
          }
      });

      // 4. Products
      searchData.products.forEach(p => {
          if (p.title.toLowerCase().includes(q)) {
              results.push({ type: 'PROD', id: p.id, title: p.title, subtitle: `€${p.price}`, icon: Briefcase, path: '/infobusiness' });
          }
      });

      setSearchResults(results.slice(0, 8)); // Limit to 8 results
  }, [searchQuery, searchData]);

  const handleSearchResultClick = (path?: string) => {
      if (path) {
          onNavigate(path);
          setIsSearchFocused(false);
          setSearchQuery('');
      }
  };

  return (
    <div className={`min-h-screen ${bgClass} text-platinum-200 flex overflow-hidden font-sans`} style={{ backgroundImage: bgGradient }}>
      
      {/* Sidebar - COMPLETAMENTE TRASPARENTE / GHOST */}
      <aside 
        className={`
          fixed md:relative z-30 h-full flex-shrink-0 transition-all duration-500 ease-out
          ${isSidebarOpen ? 'w-64 translate-x-0' : 'w-0 -translate-x-full md:w-20 md:translate-x-0'}
          flex flex-col border-r border-transparent
        `}
      >
        <div className="h-full flex flex-col">
          {/* Logo Area - CLICKABLE FOR BRAND LANDING */}
          <button 
            className={`h-24 flex items-center gap-4 px-8 mb-4 hover:opacity-80 transition-opacity`}
            onClick={() => onNavigate('/brand-home')} // NAVIGATE TO LANDING
          >
             <div className={`transition-transform duration-500 ${isSidebarOpen ? 'scale-100' : 'scale-125'}`}>
                {logoIcon}
             </div>
             {isSidebarOpen && (
               <span className={`font-bold text-lg tracking-[0.3em] ${logoText} animate-in fade-in duration-700`}>
                  {isDiamond ? 'INFO.BIZ' : 'AUREUS'}
               </span>
             )}
          </button>

          {/* Navigation - Ghost Items */}
          <nav className="flex-1 py-4 space-y-4 px-6 overflow-y-auto scrollbar-hide">
            {NAV_ITEMS.map((item) => {
              const isActive = currentPath === item.path;
              return (
                <button
                  key={item.path}
                  onClick={() => onNavigate(item.path)}
                  className={`
                    w-full flex items-center gap-4 px-2 py-2 text-sm rounded-lg
                    ${isActive ? activeItemClass : inactiveItemClass}
                  `}
                >
                  <item.icon className={`w-5 h-5 transition-transform duration-300 ${isActive ? 'scale-110' : 'scale-100'}`} strokeWidth={1.5} />
                  {isSidebarOpen && (
                    <span className={`tracking-wide animate-in fade-in slide-in-from-left-2 duration-300`}>
                      {item.label}
                    </span>
                  )}
                </button>
              );
            })}
          </nav>

          {/* User Profile - Ghost */}
          <div className={`p-8 mt-auto`}>
            <div className={`flex items-center gap-4 transition-all duration-300 opacity-60 hover:opacity-100 group`}>
              <div className={`w-8 h-8 rounded-full border border-white/20 flex items-center justify-center font-bold text-xs text-white bg-white/5 group-hover:border-diamond-400 group-hover:text-diamond-400 transition-colors`}>
                {getInitials(currentUser.name)}
              </div>
              {isSidebarOpen && (
                <div className="flex-1 overflow-hidden animate-in fade-in">
                  <p className="text-xs font-bold text-white truncate uppercase tracking-wider">{currentUser.name}</p>
                  
                  {/* XP Bar */}
                  <div className="flex items-center gap-2 mt-1">
                      <div className="w-full h-1 bg-white/10 rounded-full overflow-hidden">
                          <div className="h-full bg-diamond-500" style={{width: `${progressPercent}%`}}></div>
                      </div>
                      <span className="text-[8px] text-diamond-400 font-mono">LVL{userLevel}</span>
                  </div>
                </div>
              )}
              {isSidebarOpen && (
                <button 
                  onClick={onLogout}
                  className="text-platinum-500 hover:text-red-400 transition-colors"
                  title="Logout"
                >
                    <LogOut className="w-4 h-4" />
                </button>
              )}
            </div>
            
            {/* System Status Footer */}
            {isSidebarOpen && (
                <div className="mt-6 pt-6 border-t border-white/5 flex justify-between items-center text-[8px] text-platinum-600 font-mono uppercase tracking-widest">
                    <span className="flex items-center gap-1.5"><span className="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse shadow-[0_0_5px_#22c55e]"></span> System Online</span>
                    <span>v2.5.0</span>
                </div>
            )}
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col min-w-0 bg-transparent relative z-10">
        
        {/* Header */}
        <header className="h-24 flex items-center justify-between px-10 sticky top-0 z-20">
          <div className="flex items-center gap-4">
            <button 
              onClick={() => setIsSidebarOpen(!isSidebarOpen)}
              className="text-platinum-400 hover:text-white md:hidden"
            >
              <Menu className="w-6 h-6" />
            </button>
            
            {/* GLOBAL SEARCH BAR */}
            <div className="hidden md:block relative group" ref={searchRef}>
              <div className="flex items-center">
                  <Search className="w-4 h-4 text-platinum-600 absolute left-0 group-hover:text-platinum-300 transition-colors" />
                  <input 
                    type="text" 
                    placeholder={isDiamond ? "Ricerca Global Database..." : "Cerca nel sistema..."}
                    className="pl-8 pr-4 py-2 bg-transparent border-b border-platinum-800 w-64 text-sm text-platinum-100 focus:border-white/50 transition-all placeholder:text-platinum-700 !shadow-none !rounded-none focus:w-80"
                    value={searchQuery}
                    onChange={(e) => { setSearchQuery(e.target.value); setIsSearchFocused(true); }}
                    onFocus={() => setIsSearchFocused(true)}
                  />
              </div>

              {/* SEARCH RESULTS DROPDOWN */}
              {isSearchFocused && searchQuery && (
                  <div className="absolute top-full left-0 w-80 bg-[#0A0A0A] border border-white/10 shadow-2xl rounded-sm mt-2 overflow-hidden animate-in fade-in zoom-in-95 duration-200 z-50">
                      <div className="max-h-[300px] overflow-y-auto">
                          {searchResults.length > 0 ? (
                              searchResults.map((res, idx) => (
                                  <button 
                                    key={res.id + idx}
                                    onClick={() => handleSearchResultClick(res.path)}
                                    className="w-full text-left px-4 py-3 hover:bg-white/5 flex items-center gap-3 border-b border-white/5 last:border-0 transition-colors group/res"
                                  >
                                      <div className="p-2 bg-white/5 rounded-sm text-platinum-500 group-hover/res:text-white group-hover/res:bg-white/10">
                                          <res.icon className="w-4 h-4" />
                                      </div>
                                      <div>
                                          <div className="text-sm font-bold text-white">{res.title}</div>
                                          <div className="text-[10px] text-platinum-600 uppercase tracking-wide">{res.subtitle}</div>
                                      </div>
                                  </button>
                              ))
                          ) : (
                              <div className="p-4 text-center text-xs text-platinum-600 uppercase tracking-widest">
                                  Nessun risultato
                              </div>
                          )}
                      </div>
                      <div className="bg-[#050505] p-2 text-[9px] text-platinum-700 text-center uppercase tracking-widest border-t border-white/5">
                          Premi ESC per chiudere
                      </div>
                  </div>
              )}
            </div>
          </div>

          <div className="flex items-center gap-6">
             {/* Quick Actions - UPDATED TO NEW COLOR SCHEME */}
             <button 
                onClick={() => onNavigate('/war-room')}
                className="hidden md:flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-black hover:brightness-110 transition-all bg-gradient-to-b from-diamond-300 via-diamond-400 to-diamond-500 px-4 py-2 rounded-sm shadow-[0_0_15px_rgba(93,138,168,0.4)]"
                title="Open War Room"
             >
                 <Monitor className="w-4 h-4" /> War Room
             </button>

             {/* Notifications */}
            <div className="relative">
              <button 
                onClick={() => setIsNotifOpen(!isNotifOpen)}
                className={`relative p-2 text-platinum-400 hover:text-white transition-colors opacity-70 hover:opacity-100`}
              >
                <Bell className="w-5 h-5" strokeWidth={1.5} />
                {unreadCount > 0 && (
                  <span className="absolute top-1.5 right-1.5 w-1.5 h-1.5 bg-red-500 rounded-full shadow-[0_0_8px_rgba(239,68,68,0.8)] animate-pulse"></span>
                )}
              </button>

              {isNotifOpen && (
                <div className="absolute top-12 right-0 w-80 bg-[#0A0A0A] border border-white/10 shadow-2xl z-50 rounded-sm overflow-hidden animate-in fade-in zoom-in-95 duration-200">
                   <div className="p-4 border-b border-white/5 flex justify-between items-center bg-white/5">
                      <h3 className="text-[10px] font-bold text-white uppercase tracking-widest">Notifiche</h3>
                      {notifications.length > 0 && (
                         <button onClick={onClearNotifications} className="text-[10px] text-platinum-500 hover:text-white transition-colors">
                           PULISCI
                         </button>
                      )}
                   </div>
                   <div className="max-h-64 overflow-y-auto custom-scrollbar">
                      {notifications.length === 0 ? (
                        <div className="p-8 text-center text-platinum-600 text-[10px] uppercase tracking-widest">
                           Tutto tace
                        </div>
                      ) : (
                        notifications.map(n => (
                          <div key={n.id} className="p-4 border-b border-white/5 hover:bg-white/5 transition-colors">
                             <p className="text-xs text-platinum-200 leading-relaxed">{n.message}</p>
                             <p className="text-[9px] text-platinum-600 mt-2 font-mono">{n.date}</p>
                          </div>
                        ))
                      )}
                   </div>
                </div>
              )}
            </div>
          </div>
        </header>

        {/* Content Area */}
        <div className="flex-1 overflow-auto px-10 pb-10 relative scrollbar-hide">
            <div className="max-w-[1600px] mx-auto space-y-10">
              {children}
            </div>
        </div>
      </main>
    </div>
  );
};
