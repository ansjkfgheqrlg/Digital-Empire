
import React from 'react';

export const LuxTriangleDividerTop: React.FC = () => {
  return (
    <div className="relative w-full h-[80px] z-40 pointer-events-none -mt-[1px] overflow-hidden">
      
      {/* 1. LAYER SOTTOSTANTE: BLU (Sezione Automation) 
          Visibile ai lati della V.
      */}
      <div className="absolute inset-0 bg-[#020617]">
          {/* Texture Automation */}
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,#0f2e4a_0%,#020617_70%)] opacity-100" />
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
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#020617_100%)] opacity-50" />
      </div>

      {/* 2. LAYER V-SHAPE CENTRALE: NERO (Sezione Social Funnel)
          Tagliato a forma di V che punta in basso.
      */}
      <div 
        className="absolute inset-0 bg-[#000000]"
        style={{
            clipPath: 'polygon(0% 0%, 50% 100%, 100% 0%)'
        }}
      >
          {/* Texture Social Funnel */}
          <div 
            className="absolute inset-0 opacity-[0.35]"
            style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(170%) brightness(150%) invert(100%)' 
            }} 
          />
          <div 
            className="absolute inset-0 opacity-[0.25] mix-blend-screen"
            style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.6' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '150px 150px',
                filter: 'contrast(150%)'
            }}
          />
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_0%,#000000_100%)] opacity-40" />
      </div>

      {/* 3. LINEA DI CONFINE ARGENTO (Super Quality) 
          Senza ombre/bagliori. Solo linea pulita con gradiente metallico.
      */}
      <svg 
        className="absolute inset-0 w-full h-full overflow-visible z-50" 
        preserveAspectRatio="none" 
        viewBox="0 0 1200 80" 
      >
        <defs>
            <linearGradient id="silverLineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stopColor="rgba(255,255,255,0)" />
                <stop offset="15%" stopColor="rgba(255,255,255,0.4)" />
                <stop offset="50%" stopColor="#FFFFFF" />
                <stop offset="85%" stopColor="rgba(255,255,255,0.4)" />
                <stop offset="100%" stopColor="rgba(255,255,255,0)" />
            </linearGradient>
        </defs>
        <path 
          d="M 0,0 L 600,80 L 1200,0"
          stroke="url(#silverLineGradient)"
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
