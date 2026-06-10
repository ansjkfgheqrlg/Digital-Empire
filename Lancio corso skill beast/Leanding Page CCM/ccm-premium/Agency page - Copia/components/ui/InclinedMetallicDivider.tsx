
import React from 'react';

export const InclinedMetallicDivider: React.FC = () => {
    return (
        <div className="relative w-full h-px z-50 pointer-events-none">
            <div
                className="absolute w-screen left-1/2 -translate-x-1/2 h-6 origin-center shadow-2xl overflow-hidden"
                style={{
                    transform: 'rotate(-2.5deg)',
                    background: `linear-gradient(90deg, 
             #8E9BAF 0%,       /* Cool Silver Edge (Start) */
             #C8B998 5%,       /* Transition to Gold */
             #D4AF37 20%,      /* Rich Gold */
             #FCEEB5 40%,      /* Light Gold Highight */
             #FFD700 50%,      /* Pure Bright Gold (Center) */
             #FCEEB5 60%,      /* Light Gold Highight */
             #D4AF37 80%,      /* Rich Gold */
             #C8B998 95%,      /* Transition to Silver */
             #8E9BAF 100%      /* Cool Silver Edge (End) */
           )`
                }}
            >
                {/* Top Highlight for 3D effect (Shininess) */}
                <div className="absolute top-0 left-0 w-full h-[1px] bg-white/90 opacity-90 mix-blend-overlay" />

                {/* Bottom Shadow for 3D effect (Depth) */}
                <div className="absolute bottom-0 left-0 w-full h-[1px] bg-[#594D2E] opacity-60" />

                {/* Inner metallic texture overlay for realism */}
                <div
                    className="absolute inset-0 opacity-10 mix-blend-overlay"
                    style={{ backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")' }}
                />
            </div>
        </div>
    );
};
