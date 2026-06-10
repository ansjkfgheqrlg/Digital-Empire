
import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, CheckCircle2, ChevronRight, Activity } from 'lucide-react';
import { Service } from '../../types';

export type ThemeColor = 'cyan' | 'purple' | 'emerald';

const MotionDiv = motion.div as any;

interface ServiceModalProps {
  service: Service | null;
  isOpen: boolean;
  onClose: () => void;
  themeColor?: ThemeColor;
}

export const ServiceModal: React.FC<ServiceModalProps> = ({ service, isOpen, onClose }) => {
  if (!service) return null;

  const silverStyle = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 25%, #CBD5E1 50%, #94A3B8 75%, #475569 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <div className="fixed inset-0 z-[60] flex items-center justify-center p-4">
          {/* Backdrop */}
          <MotionDiv
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="absolute inset-0 bg-black-deep/98 backdrop-blur-md"
          />

          {/* Modal Content */}
          <MotionDiv
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.95 }}
            className="relative w-full max-w-4xl bg-black-900 border border-white/10 overflow-hidden shadow-[0_50px_100px_rgba(0,0,0,0.8)]"
          >
            {/* Top Security Line */}
            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-gold-500/50 to-transparent z-30" />
            
            <button 
              onClick={onClose}
              className="absolute top-6 right-6 text-gray-500 hover:text-white transition-colors z-40 bg-white/5 p-2 rounded-full border border-white/5"
            >
              <X size={20} />
            </button>

            <div className="flex flex-col md:flex-row">
              <div className="flex-grow p-8 md:p-16">
                <div className="mb-10">
                   <span className="text-[10px] font-mono text-gold-500 uppercase tracking-[0.5em] font-black block mb-4">SPECIFICHE PROTOCOLLO</span>
                   <h2 
                    style={silverStyle as any}
                    className="font-serif text-3xl md:text-5xl text-white font-black leading-tight uppercase tracking-tighter mb-8"
                   >
                     {service.title}
                   </h2>
                   
                   <div className="relative pl-8 py-2 border-l border-white/10">
                      <p className="text-gray-300 text-lg md:text-xl font-bold leading-relaxed">
                        {service.fullDescription}
                      </p>
                   </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-10 mt-12">
                   <div>
                      <h4 className="text-[10px] font-mono uppercase tracking-[0.3em] font-black text-gray-500 mb-6">Asset Inclusi</h4>
                      <div className="space-y-4">
                        {service.details.map((detail, index) => (
                          <div key={index} className="flex items-start gap-3">
                            <CheckCircle2 className="text-gold-500 w-5 h-5 flex-shrink-0" strokeWidth={3} />
                            <span className="text-gray-400 text-sm font-bold tracking-tight">{detail}</span>
                          </div>
                        ))}
                      </div>
                   </div>

                   <div className="flex flex-col justify-between">
                      <div>
                        <h4 className="text-[10px] font-mono uppercase tracking-[0.3em] font-black text-gray-500 mb-6">Stack Tecnico</h4>
                        <div className="flex flex-wrap gap-2">
                          {service.techSpecs?.map((spec, i) => (
                             <span key={i} className="px-3 py-1.5 bg-white/5 text-white text-[9px] font-black uppercase tracking-widest border border-white/10">
                               {spec}
                             </span>
                          ))}
                        </div>
                      </div>
                      
                      <div className="mt-12">
                         <a 
                           href="#contact" 
                           onClick={onClose}
                           className="group flex items-center justify-center gap-4 bg-gold-500 text-black-950 px-8 py-5 font-black text-[11px] uppercase tracking-[0.2em] hover:bg-white transition-all shadow-2xl"
                         >
                           Inizia Configurazione <ChevronRight size={16} className="group-hover:translate-x-1 transition-transform" />
                         </a>
                      </div>
                   </div>
                </div>
              </div>
            </div>
          </MotionDiv>
        </div>
      )}
    </AnimatePresence>
  );
};
