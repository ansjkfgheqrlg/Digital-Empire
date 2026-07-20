
import React, { useState } from 'react';
import { Task, SocialPost, Lead, TaskStatus } from '../types';
import { ChevronLeft, ChevronRight, Calendar as CalIcon, Filter } from 'lucide-react';

interface MasterCalendarProps {
  tasks: Task[];
  posts: SocialPost[];
  leads: Lead[];
}

type CalendarEventType = 'TASK' | 'SOCIAL' | 'LEAD';

interface CalendarEvent {
  id: string;
  date: string; // YYYY-MM-DD
  title: string;
  type: CalendarEventType;
  subType?: string;
  status?: string;
}

export const MasterCalendar: React.FC<MasterCalendarProps> = ({ tasks, posts, leads }) => {
  const [currentDate, setCurrentDate] = useState(new Date());
  const [filters, setFilters] = useState({ tasks: true, social: true, leads: true });

  const getDaysInMonth = (date: Date) => {
    const year = date.getFullYear();
    const month = date.getMonth();
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const days = [];
    
    const startDay = firstDay.getDay() || 7; // 1 (Mon) - 7 (Sun)
    for(let i=1; i<startDay; i++) days.push(null);
    for(let i=1; i<=lastDay.getDate(); i++) days.push(new Date(year, month, i));
    return days;
  };

  // Merge Data
  const getAllEvents = (): CalendarEvent[] => {
      let events: CalendarEvent[] = [];
      
      if (filters.tasks) {
          events = events.concat(tasks.filter(t => t.status !== TaskStatus.DONE).map(t => ({
              id: t.id, date: t.dueDate, title: t.title, type: 'TASK', status: t.status, subType: t.priority
          })));
      }
      
      if (filters.social) {
          events = events.concat(posts.map(p => ({
              id: p.id, date: p.scheduledDate || '', title: p.title, type: 'SOCIAL', status: p.status, subType: p.platform
          })));
      }

      if (filters.leads) {
          events = events.concat(leads.filter(l => l.stage !== 'CLOSED_WON' && l.stage !== 'CLOSED_LOST').map(l => ({
              id: l.id, date: l.lastContact, title: `Follow-up: ${l.companyName}`, type: 'LEAD', status: l.stage
          })));
      }

      return events;
  };

  const events = getAllEvents();

  const getEventsForDate = (date: Date) => {
    const dateStr = date.toISOString().split('T')[0];
    return events.filter(e => e.date === dateStr);
  };

  return (
    <div className="h-[calc(100vh-140px)] flex flex-col animate-in fade-in duration-500">
      
      {/* Calendar Header */}
      <div className="flex justify-between items-end mb-6">
        <div>
            <h1 className="text-3xl font-bold text-silver-gradient mb-2 tracking-tight">Master Calendar</h1>
            <p className="text-platinum-500 text-sm">Visione d'insieme di tutte le attività aziendali.</p>
        </div>
        
        <div className="flex items-center gap-6">
            {/* Filters */}
            <div className="flex items-center gap-2 bg-[#0A0A0A] border border-white/10 rounded-full px-4 py-2">
                <Filter className="w-3 h-3 text-platinum-500 mr-2" />
                <button 
                    onClick={() => setFilters(f => ({...f, tasks: !f.tasks}))}
                    className={`text-[10px] font-bold uppercase px-2 py-1 rounded-sm transition-colors border ${filters.tasks ? 'bg-blue-900/30 text-blue-400 border-blue-500/30' : 'text-platinum-600 border-transparent hover:text-white'}`}
                >Tasks</button>
                <button 
                    onClick={() => setFilters(f => ({...f, social: !f.social}))}
                    className={`text-[10px] font-bold uppercase px-2 py-1 rounded-sm transition-colors border ${filters.social ? 'bg-purple-900/30 text-purple-400 border-purple-500/30' : 'text-platinum-600 border-transparent hover:text-white'}`}
                >Social</button>
                <button 
                    onClick={() => setFilters(f => ({...f, leads: !f.leads}))}
                    className={`text-[10px] font-bold uppercase px-2 py-1 rounded-sm transition-colors border ${filters.leads ? 'bg-green-900/30 text-green-400 border-green-500/30' : 'text-platinum-600 border-transparent hover:text-white'}`}
                >CRM</button>
            </div>

            {/* Navigation */}
            <div className="flex items-center gap-4 bg-[#0A0A0A] border border-white/10 rounded-sm p-1">
                <button onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1))} className="p-2 hover:bg-white/10 rounded-sm text-white"><ChevronLeft className="w-4 h-4"/></button>
                <span className="text-sm font-bold text-white min-w-[120px] text-center uppercase tracking-wider">
                    {currentDate.toLocaleDateString('it-IT', { month: 'long', year: 'numeric' })}
                </span>
                <button onClick={() => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1))} className="p-2 hover:bg-white/10 rounded-sm text-white"><ChevronRight className="w-4 h-4"/></button>
            </div>
        </div>
      </div>

      {/* Calendar Grid */}
      <div className="flex-1 bg-[#0A0A0A] border border-white/10 rounded-sm flex flex-col overflow-hidden shadow-2xl">
          {/* Days Header */}
          <div className="grid grid-cols-7 border-b border-white/10 bg-[#0F0F0F]">
              {['LUN', 'MAR', 'MER', 'GIO', 'VEN', 'SAB', 'DOM'].map(day => (
                  <div key={day} className="py-3 text-center text-[10px] font-bold text-platinum-500 uppercase tracking-widest border-r border-white/5 last:border-r-0">
                      {day}
                  </div>
              ))}
          </div>

          {/* Days Grid */}
          <div className="flex-1 grid grid-cols-7 grid-rows-5 lg:grid-rows-5 gap-[1px] bg-white/5">
              {getDaysInMonth(currentDate).map((date, i) => {
                  if (!date) return <div key={i} className="bg-[#050505]"></div>;
                  
                  const isToday = new Date().toDateString() === date.toDateString();
                  const dayEvents = getEventsForDate(date);

                  return (
                      <div key={i} className={`bg-[#0A0A0A] p-3 relative group hover:bg-[#0F0F0F] transition-colors overflow-hidden flex flex-col ${isToday ? 'bg-white/5' : ''}`}>
                          {/* Day Number */}
                          <div className={`text-right text-xs font-mono mb-2 ${isToday ? 'text-silver-accent font-bold' : 'text-platinum-600'}`}>
                              {date.getDate()}
                          </div>

                          {/* Events List */}
                          <div className="flex-1 space-y-1 overflow-y-auto custom-scrollbar">
                              {dayEvents.map(event => {
                                  let colorClass = '';
                                  if (event.type === 'TASK') colorClass = 'bg-blue-900/20 text-blue-300 border-blue-500/20';
                                  if (event.type === 'SOCIAL') colorClass = 'bg-purple-900/20 text-purple-300 border-purple-500/20';
                                  if (event.type === 'LEAD') colorClass = 'bg-green-900/20 text-green-300 border-green-500/20';

                                  return (
                                      <div key={event.id} className={`text-[9px] px-1.5 py-1 rounded-sm border truncate font-medium cursor-pointer hover:brightness-125 transition-all ${colorClass}`}>
                                          {event.title}
                                      </div>
                                  );
                              })}
                          </div>
                          
                          {/* Add Button (Hover) */}
                          <button className="absolute bottom-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity bg-white text-black rounded-full w-6 h-6 flex items-center justify-center shadow-lg hover:scale-110">
                              <CalIcon className="w-3 h-3" />
                          </button>
                      </div>
                  );
              })}
          </div>
      </div>
    </div>
  );
};
