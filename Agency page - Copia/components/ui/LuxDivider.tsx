
import React from 'react';

export const LuxDivider: React.FC = () => {
  return (
    <div className="relative w-full h-[100px] md:h-[150px] z-40 pointer-events-none -mt-[2px] flex items-end justify-center overflow-hidden bg-transparent">
      
      {/* 
         LAYER 1: SOLID FILL MATCHING NEXT SECTION (BIANCO PURO)
         Color: #FFFFFF
      */}
      <svg 
        className="absolute inset-0 z-0 w-full h-full overflow-visible" 
        preserveAspectRatio="none" 
        viewBox="0 0 1200 120"
      >
          <path 
            d="M 0,500 L 0,30 L 600,0 L 1200,30 L 1200,500 Z"
            fill="#FFFFFF"
            stroke="none"
          />
      </svg>

      {/* 
         LAYER 2: GRID PATTERN (CSS)
         Clip-Path sincronizzato.
      */}
      <div 
        className="absolute inset-0 z-10 bg-transparent"
        style={{
           clipPath: 'polygon(0% 100%, 0% 25%, 50% 0%, 100% 25%, 100% 100%)'
        }}
      >
         {/* GRID PATTERN (Darker for visibility on light bg) */}
         <div className="absolute inset-0 bg-[linear-gradient(rgba(30,41,59,0.05)_1px,transparent_1px),linear-gradient(90deg,rgba(30,41,59,0.05)_1px,transparent_1px)] bg-[size:50px_50px]"></div>
      </div>

      {/* 
         LAYER 3: GOLD STROKE (SVG VECTOR PERFECT)
      */}
      <svg 
        className="relative z-20 w-full h-full overflow-visible" 
        preserveAspectRatio="none" 
        viewBox="0 0 1200 120"
      >
        <defs>
          <linearGradient id="luxHighResGradient" x1="0%" y1="0%" x2="100%" y2="0%">
             <stop offset="0%" stopColor="#94A3B8" />
             <stop offset="20%" stopColor="#E2E8F0" />
             <stop offset="45%" stopColor="#E3C878" />
             <stop offset="50%" stopColor="#FFFFFF" />
             <stop offset="55%" stopColor="#E3C878" />
             <stop offset="80%" stopColor="#E2E8F0" />
             <stop offset="100%" stopColor="#94A3B8" />
          </linearGradient>
        </defs>

        {/* LINEA PRINCIPALE (Il confine metallico) */}
        <path 
          d="M -50,32.5 L 0,30 L 600,0 L 1200,30 L 1250,32.5"
          stroke="url(#luxHighResGradient)"
          strokeWidth="3" 
          fill="none"
          strokeLinecap="square"
          vectorEffect="non-scaling-stroke" 
        />
        
        {/* LINEA SECONDARIA (Highlight interno) */}
        <path 
          d="M -50,32.5 L 0,30 L 600,0 L 1200,30 L 1250,32.5"
          stroke="#FFFFFF"
          strokeWidth="1" 
          strokeOpacity="0.9"
          fill="none"
          vectorEffect="non-scaling-stroke"
          style={{ mixBlendMode: 'overlay' }}
        />
      </svg>
    </div>
  );
};
