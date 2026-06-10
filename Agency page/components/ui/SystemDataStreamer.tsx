
import React from 'react';
import { motion } from 'framer-motion';
import { Activity, Cpu, ShieldCheck, Zap, Globe, Database } from 'lucide-react';

const MotionDiv = motion.div as any;

const DATA_POINTS = [
  { label: "EMPIRE_NODE", value: "01_MILAN", icon: Globe },
  { label: "NEURAL_LATENCY", value: "0.002ms", icon: Activity },
  { label: "UPTIME", value: "99.99%", icon: ShieldCheck },
  { label: "CONVERSION_INDEX", value: "4.8x", icon: Zap },
  { label: "DATABASE_SYNC", value: "ACTIVE", icon: Database },
  { label: "AI_CORE_LOAD", value: "12%", icon: Cpu },
  { label: "PROTOCOL", value: "EMPIRE_v4.5", icon: ShieldCheck },
  { label: "SECURITY", value: "ENCRYPTED", icon: ShieldCheck },
];

export const SystemDataStreamer: React.FC = () => {
  return (
    <div className="w-full h-14 md:h-16 bg-black-950/40 backdrop-blur-xl border-y border-white/5 relative z-30 overflow-hidden flex items-center">
      {/* Scanner light effect */}
      <MotionDiv 
        animate={{ x: ["-100%", "200%"] }}
        transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
        className="absolute inset-y-0 w-1/3 bg-gradient-to-r from-transparent via-gold-500/10 to-transparent skew-x-[-25deg] pointer-events-none"
      />
      
      <MotionDiv 
        className="flex gap-12 md:gap-24 whitespace-nowrap px-10 items-center"
        animate={{ x: ["0%", "-50%"] }}
        transition={{ duration: 40, repeat: Infinity, ease: "linear" }}
      >
        {[...Array(2)].map((_, i) => (
          <React.Fragment key={i}>
            {DATA_POINTS.map((item, idx) => (
              <div key={idx} className="flex items-center gap-3 group cursor-default">
                <item.icon size={14} className="text-gold-500/50 group-hover:text-gold-500 transition-colors" />
                <span className="text-[9px] md:text-[10px] font-mono font-black tracking-[0.2em] text-gray-500 group-hover:text-gray-300 transition-colors">
                  {item.label}: <span className="text-white">{item.value}</span>
                </span>
                <div className="w-1 h-1 bg-white/10 rounded-full mx-2" />
              </div>
            ))}
          </React.Fragment>
        ))}
      </MotionDiv>
    </div>
  );
};
