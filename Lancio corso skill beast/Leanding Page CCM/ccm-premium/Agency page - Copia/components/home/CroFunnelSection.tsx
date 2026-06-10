
import React from 'react';
import { EducationalBridge, HopeIsNoStrategy, CroCalculator, ApsocProtocol, CroEditorialSection } from './CroFunnelParts';
import { DustCanvas } from '../ui/DustCanvas';

export const CroFunnelSection: React.FC = () => {

    // Gradienti Tipografici
    const goldGradient = {
        backgroundImage: 'linear-gradient(180deg, #FDE68A 0%, #D4AF37 50%, #B45309 100%)',
        WebkitBackgroundClip: 'text',
        backgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
        filter: 'drop-shadow(0px 2px 4px rgba(212,175,55,0.2))'
    };

    const silverGradient = {
        backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 60%, #94A3B8 100%)',
        WebkitBackgroundClip: 'text',
        backgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
    };

    return (
        <section className="relative z-20 pb-32 overflow-hidden bg-black -mt-20 pt-20">

            {/* Background Decorativo che continua dalla hero */}
            <div className="absolute top-0 left-0 w-full h-full pointer-events-none z-0">
                <div className="absolute inset-0 bg-gradient-to-b from-black via-[#050505] to-black opacity-100"></div>
                <DustCanvas />
            </div>

            <div className="container mx-auto px-6 max-w-7xl relative z-10">
                <EducationalBridge />
                <HopeIsNoStrategy />
                <CroCalculator goldGradient={goldGradient} silverGradient={silverGradient} />
                <CroEditorialSection />
            </div>
        </section>
    );
};
