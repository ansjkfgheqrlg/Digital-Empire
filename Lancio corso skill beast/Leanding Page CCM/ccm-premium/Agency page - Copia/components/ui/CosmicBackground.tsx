
import React from 'react';
import { motion } from 'framer-motion';

interface CosmicBackgroundProps {
    intensity?: number;
    showLightSpot?: boolean;
}

export const CosmicBackground: React.FC<CosmicBackgroundProps> = ({
    intensity = 1,
    showLightSpot = false
}) => {
    return (
        <div className="fixed inset-0 w-full h-full pointer-events-none z-0">
            {/* Layer 1: Base Nero Assoluto */}
            <div className="absolute inset-0 bg-[#000000]"></div>

            {/* Layer 2: Deep Void Purple Atmosphere */}
            <div
                className="absolute inset-0 opacity-60"
                style={{
                    background: 'radial-gradient(circle at 50% 50%, #1a0024 0%, #0a0012 40%, #000000 80%)'
                }}
            />

            {/* Layer 3: Heavy Film Grain */}
            <div
                className="absolute inset-0 opacity-[0.45]"
                style={{
                    backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")',
                    filter: `contrast(350%) brightness(60%) sepia(100%) hue-rotate(260deg) saturate(200%)`,
                    mixBlendMode: 'overlay'
                }}
            />

            {/* Layer 4: Digital Crisp Noise */}
            <div
                className="absolute inset-0 opacity-[0.3] mix-blend-screen"
                style={{
                    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.5' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='1'/%3E%3C/svg%3E")`,
                    backgroundSize: '100px 100px',
                    filter: 'contrast(180%) brightness(40%)'
                }}
            />

            {showLightSpot && (
                <div
                    className="absolute inset-0 opacity-30"
                    style={{
                        background: 'radial-gradient(circle at 50% 0%, #3a005c 0%, transparent 70%)'
                    }}
                />
            )}
        </div>
    );
};
