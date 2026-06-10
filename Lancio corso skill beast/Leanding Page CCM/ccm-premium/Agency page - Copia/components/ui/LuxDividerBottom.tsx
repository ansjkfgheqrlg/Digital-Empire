
import React from 'react';

export const LuxDividerBottom: React.FC = () => {
  return (
    <div className="relative w-full h-[100px] md:h-[150px] z-40 pointer-events-none -mt-[2px] flex items-start justify-center overflow-hidden bg-[#020202]">
      
      {/* 
         LAYER 1: FILL SHAPE (THE V-WEDGE)
         This fills the V-shape at the top with the PREVIOUS SECTION's color (#FFFFFF - BIANCO PURO).
         The rest of the container background (#020202) shows through on the sides/bottom, matching the NEXT section.
         This effectively extends the white section down into a point.
      */}
      <svg 
        className="w-full h-full overflow-visible" 
        preserveAspectRatio="none" 
        viewBox="0 0 1200 120"
      >
        <defs>
          <linearGradient id="luxHighResGradientBottom" x1="0%" y1="0%" x2="100%" y2="0%">
             <stop offset="0%" stopColor="#94A3B8" />
             <stop offset="20%" stopColor="#E2E8F0" />
             <stop offset="45%" stopColor="#E3C878" />
             <stop offset="50%" stopColor="#FFFFFF" />
             <stop offset="55%" stopColor="#E3C878" />
             <stop offset="80%" stopColor="#E2E8F0" />
             <stop offset="100%" stopColor="#94A3B8" />
          </linearGradient>
        </defs>

        <path 
          d="M -2000,0 L 600,120 L 3200,0 Z"
          fill="#FFFFFF"
          stroke="none"
        />

        <path 
          d="M -2000,0 L 600,120 L 3200,0"
          stroke="url(#luxHighResGradientBottom)"
          strokeWidth="3" 
          fill="none"
          strokeLinecap="square"
          vectorEffect="non-scaling-stroke" 
        />
        
        <path 
          d="M -2000,0 L 600,120 L 3200,0"
          stroke="#FFFFFF"
          strokeWidth="1" 
          strokeOpacity="0.7"
          fill="none"
          vectorEffect="non-scaling-stroke"
          style={{ mixBlendMode: 'overlay' }}
        />
      </svg>
    </div>
  );
};
