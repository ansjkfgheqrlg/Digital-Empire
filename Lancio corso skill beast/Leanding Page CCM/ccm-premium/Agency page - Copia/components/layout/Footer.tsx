
import React from 'react';
import { Instagram, Linkedin, Twitter, Mail, MapPin, Phone, ShieldCheck } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-transparent border-t border-white/5 pt-24 pb-12 relative z-10">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 mb-24">
          
          {/* Brand Column */}
          <div className="lg:col-span-1">
            <div className="flex items-center gap-3 mb-8">
               <div className="w-10 h-10 bg-gold-500 flex items-center justify-center rounded-sm shadow-[0_0_25px_rgba(253,185,19,0.3)]">
                 <span className="font-serif font-black text-xl text-black-950">DE</span>
               </div>
               <span className="font-serif text-xl text-white tracking-[0.2em] uppercase font-black">EMPIRE</span>
            </div>
            <p className="text-gray-500 text-sm leading-relaxed mb-10 font-medium">
              Architetti di ecosistemi digitali d'élite. Fondiamo design d'avanguardia, intelligenza artificiale e strategie di marketing ad alto impatto per scalare business ambiziosi.
            </p>
            <div className="flex gap-4">
              {[Instagram, Linkedin, Twitter].map((Icon, i) => (
                <a key={i} href="#" className="w-12 h-12 bg-white/[0.03] border border-white/5 flex items-center justify-center rounded-sm hover:border-gold-500/50 hover:bg-gold-500/10 transition-all text-gray-500 hover:text-gold-500 group">
                  <Icon size={20} className="group-hover:scale-110 transition-transform" />
                </a>
              ))}
            </div>
          </div>
          
          {/* Services Column */}
          <div>
            <h4 className="text-white font-serif mb-8 uppercase tracking-[0.3em] text-xs font-black border-l-2 border-gold-500 pl-4">Servizi</h4>
            <ul className="space-y-4 text-sm text-gray-500 font-bold">
              <li className="hover:text-white transition-colors cursor-pointer flex items-center gap-3 group">
                <div className="w-1 h-1 bg-gold-500 rounded-full opacity-0 group-hover:opacity-100 transition-all" />
                Web Engineering
              </li>
              <li className="hover:text-white transition-colors cursor-pointer flex items-center gap-3 group">
                <div className="w-1 h-1 bg-gold-500 rounded-full opacity-0 group-hover:opacity-100 transition-all" />
                AI Autopilot Systems
              </li>
              <li className="hover:text-white transition-colors cursor-pointer flex items-center gap-3 group">
                <div className="w-1 h-1 bg-gold-500 rounded-full opacity-0 group-hover:opacity-100 transition-all" />
                Growth Marketing
              </li>
              <li className="hover:text-white transition-colors cursor-pointer flex items-center gap-3 group">
                <div className="w-1 h-1 bg-gold-500 rounded-full opacity-0 group-hover:opacity-100 transition-all" />
                Brand Architecture
              </li>
            </ul>
          </div>

          {/* Contact Column */}
          <div>
            <h4 className="text-white font-serif mb-8 uppercase tracking-[0.3em] text-xs font-black border-l-2 border-gold-500 pl-4">Contatti</h4>
            <ul className="space-y-6 text-sm text-gray-500 font-bold">
              <li className="flex items-center gap-4 group cursor-pointer">
                <div className="p-2 bg-white/[0.02] border border-white/5 rounded group-hover:border-gold-500/30 transition-colors">
                  <Mail size={16} className="text-gold-500" />
                </div>
                <span className="group-hover:text-white transition-colors">hq@digitalempire.team</span>
              </li>
              <li className="flex items-center gap-4 group cursor-pointer">
                <div className="p-2 bg-white/[0.02] border border-white/5 rounded group-hover:border-gold-500/30 transition-colors">
                  <MapPin size={16} className="text-gold-500" />
                </div>
                <span className="group-hover:text-white transition-colors">Milano, IT & Dubai, UAE</span>
              </li>
              <li className="flex items-center gap-4 group cursor-pointer">
                <div className="p-2 bg-white/[0.02] border border-white/5 rounded group-hover:border-gold-500/30 transition-colors">
                  <Phone size={16} className="text-gold-500" />
                </div>
                <span className="group-hover:text-white transition-colors">+39 02 369 369</span>
              </li>
            </ul>
          </div>

          {/* Status Column */}
          <div>
            <h4 className="text-white font-serif mb-8 uppercase tracking-[0.3em] text-xs font-black border-l-2 border-gold-500 pl-4">HQ STATUS</h4>
            <div className="p-6 bg-black-900/40 backdrop-blur-md border border-white/5 rounded-sm relative overflow-hidden group">
               <div className="absolute inset-0 bg-gradient-to-tr from-gold-500/5 to-transparent pointer-events-none" />
               <div className="flex items-center justify-between mb-5 relative z-10">
                  <span className="text-[10px] font-mono text-gray-600 uppercase tracking-widest font-black">System Load</span>
                  <span className="text-[10px] font-mono text-green-500 uppercase font-black animate-pulse">Optimal</span>
               </div>
               <div className="flex items-center justify-between mb-5 relative z-10">
                  <span className="text-[10px] font-mono text-gray-600 uppercase tracking-widest font-black">Uptime 2024</span>
                  <span className="text-[10px] font-mono text-white uppercase font-black">99.98%</span>
               </div>
               <div className="h-1.5 w-full bg-white/5 rounded-full overflow-hidden relative z-10">
                  <div className="h-full w-[94%] bg-gradient-to-r from-gold-700 to-gold-400"></div>
               </div>
               <div className="mt-6 pt-5 border-t border-white/5 flex items-center justify-between opacity-40 group-hover:opacity-100 transition-opacity relative z-10">
                  <span className="text-[8px] font-mono uppercase tracking-widest font-black text-gray-500">Node: EMPIRE_01</span>
                  <ShieldCheck size={12} className="text-gold-500" />
               </div>
            </div>
          </div>
        </div>
        
        {/* Bottom Bar */}
        <div className="pt-12 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8">
          <div className="flex flex-col md:flex-row items-center gap-4 md:gap-10">
            <p className="text-[10px] font-mono text-gray-600 uppercase tracking-[0.3em] font-black">
              © 2025 DIGITAL EMPIRE TEAM. ALL RIGHTS RESERVED.
            </p>
            <div className="h-4 w-[1px] bg-white/5 hidden md:block"></div>
            <p className="text-[9px] font-mono text-gray-700 uppercase tracking-[0.2em]">
              Codificato per il dominio assoluto.
            </p>
          </div>
          <div className="flex gap-10 text-[10px] font-mono text-gray-500 uppercase tracking-[0.2em] font-black">
            <a href="#" className="hover:text-gold-500 transition-colors">Privacy Policy</a>
            <a href="#" className="hover:text-white transition-colors">Cookie Protocol</a>
          </div>
        </div>
      </div>
    </footer>
  );
};
