
import React from 'react';
import { motion } from 'framer-motion';

export const LuxStraightDivider: React.FC = () => {
  return (
    <div className="relative w-full h-[3px] z-50 flex items-center justify-center bg-[#020202]">
      
      {/* 
         LINEA PRINCIPALE (CORE)
         Gradiente complesso Oro-Argento-Bianco-Argento-Oro
         Nessuna curva, precisione chirurgica.
      */}
      <div 
        className="w-full h-full"
        style={{
          background: `linear-gradient(90deg, 
            #020202 0%, 
            #94A3B8 20%, 
            #E3C878 40%, 
            #FFFFFF 50%, 
            #E3C878 60%, 
            #94A3B8 80%, 
            #020202 100%
          )`
        }}
      />

      {/* 
         RIMOSSO: BAGLIORE METALLICO (GLOW)
         Eliminato su richiesta ("elimina questa luce accanto la linea").
         La linea ora è nitida e senza alone.
      */}
      
      {/* Dettaglio centrale sottile (opzionale, per "ancorare" la linea, ma senza glow diffuso) */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-24 h-[1px] bg-white opacity-40 mix-blend-overlay"></div>
    </div>
  );
};
