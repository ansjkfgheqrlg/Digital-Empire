
import React from 'react';

export const LuxDividerGreen: React.FC = () => {
  return (
    // Top Divider: Sits above the Trust section. Creates an upward curve (Hill).
    <div className="relative w-full h-[100px] md:h-[150px] z-40 pointer-events-none -mt-[100px] md:-mt-[150px] flex items-end justify-center">
      
      {/* 1. GRAIN BACKGROUND CONTAINER (CLIPPED TO CURVE) */}
      <div 
        className="absolute inset-0 w-full h-full z-0"
        style={{ clipPath: 'url(#luxGreenTopClip)' }}
      >
           {/* Background Color (Deep Green) */}
           <div className="absolute inset-0 bg-[#031c16]"></div>
           
           {/* Grain 1: Heavy Film Grain */}
           <div 
             className="absolute inset-0 opacity-[0.4]" 
             style={{ 
                backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                filter: 'contrast(350%) brightness(100%)',
                mixBlendMode: 'overlay' 
             }} 
           />
           
           {/* Grain 2: Digital Noise */}
           <div 
             className="absolute inset-0 opacity-[0.3] mix-blend-screen"
             style={{
                backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.7' numOctaves='5' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                backgroundSize: '100px 100px', 
                filter: 'contrast(160%) brightness(50%)'
             }} 
           />
           
           {/* Grid Pattern */}
           <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.02)_1px,transparent_1px)] bg-[size:60px_60px] opacity-10" />
      </div>

      {/* 2. SVG STROKE (BORDER) & CLIP DEFINITION */}
      <svg 
        className="absolute inset-0 w-full h-full overflow-visible z-10" 
        preserveAspectRatio="none" 
        viewBox="0 0 1200 120"
      >
        <defs>
          {/* 
            Clip Path for the Hill Shape.
            M 0,1 (Bottom Left) -> Q 0.5,0 (Top Center) -> 1,1 (Bottom Right) -> Close
          */}
          <clipPath id="luxGreenTopClip" clipPathUnits="objectBoundingBox">
             <path d="M 0,1 Q 0.5,0 1,1 V 1.1 H 0 Z" />
          </clipPath>

          <linearGradient id="luxHighResGradientGreen" x1="0%" y1="0%" x2="100%" y2="0%">
             <stop offset="0%" stopColor="#94A3B8" />
             <stop offset="20%" stopColor="#E2E8F0" />
             <stop offset="45%" stopColor="#E3C878" />
             <stop offset="50%" stopColor="#FFFFFF" />
             <stop offset="55%" stopColor="#E3C878" />
             <stop offset="80%" stopColor="#E2E8F0" />
             <stop offset="100%" stopColor="#94A3B8" />
          </linearGradient>
        </defs>

        {/* GOLD STROKE - Matching Curve */}
        <path 
          d="M -50,120 Q 600,0 1250,120"
          stroke="url(#luxHighResGradientGreen)"
          strokeWidth="3" 
          fill="none"
          strokeLinecap="round"
          vectorEffect="non-scaling-stroke" 
        />
        
        {/* INNER GLOW STROKE */}
        <path 
          d="M -50,120 Q 600,0 1250,120"
          stroke="#FFFFFF"
          strokeWidth="1" 
          strokeOpacity="0.5"
          fill="none"
          vectorEffect="non-scaling-stroke"
          style={{ mixBlendMode: 'overlay' }}
        />
      </svg>
    </div>
  );
};
