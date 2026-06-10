
import React from 'react';

export const LuxTriangleDividerBottom: React.FC = () => {
  return (
    <div className="relative w-full h-[80px] z-40 pointer-events-none -mt-[1px] overflow-hidden">
        
      {/* 1. LAYER SOTTOSTANTE: NERO (Sezione Philosophy)
          Visibile ai lati.
      */}
      <div className="absolute inset-0 bg-[#020202]">
        {/* Texture Philosophy */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#111_1px,transparent_1px),linear-gradient(to_bottom,#111_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] pointer-events-none" />
      </div>

      {/* 2. LAYER V-SHAPE CENTRALE: BLU (Sezione Automation)
          Estende il blu in una punta verso il basso.
      */}
      <div 
        className="absolute inset-0 bg-[#020617]"
        style={{
            clipPath: 'polygon(0% 0%, 50% 100%, 100% 0%)'
        }}
      >
          {/* Texture Automation */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,#0f2e4a_0%,#020617_70%)] opacity-50" />
          <div 
            className="absolute inset-0 opacity-[0.35]"
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(170%) brightness(150%) invert(100%)' 
            }} 
          />
          <div 
            className="absolute inset-0 opacity-[0.3] mix-blend-screen"
            style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '150px 150px',
                filter: 'contrast(150%)'
            }}
          />
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#020617_100%)] opacity-80" />
      </div>

      {/* 3. LINEA DI CONFINE ARGENTO (Super Quality) */}
      <svg 
        className="absolute inset-0 w-full h-full overflow-visible z-50" 
        preserveAspectRatio="none" 
        viewBox="0 0 1200 80"
      >
        <defs>
            <linearGradient id="silverLineGradientBottom" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stopColor="rgba(255,255,255,0)" />
                <stop offset="15%" stopColor="rgba(255,255,255,0.4)" />
                <stop offset="50%" stopColor="#FFFFFF" />
                <stop offset="85%" stopColor="rgba(255,255,255,0.4)" />
                <stop offset="100%" stopColor="rgba(255,255,255,0)" />
            </linearGradient>
        </defs>
        <path 
          d="M 0,0 L 600,80 L 1200,0"
          stroke="url(#silverLineGradientBottom)"
          strokeWidth="1.5" 
          fill="none"
          strokeLinecap="round"
          strokeLinejoin="round"
          vectorEffect="non-scaling-stroke"
        />
      </svg>
    </div>
  );
};
