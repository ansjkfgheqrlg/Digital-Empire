import React from 'react';

export const InclinedGoldLine: React.FC = () => {
    return (
        <div className="relative w-full overflow-hidden -mt-1 -mb-1 z-50 pointer-events-none">
            {/* 
           The Container needs to be tall enough to accommodate the slant.
           We use a skew transform on the line itself to create the inclination.
       */}
            <div className="relative w-full h-[60px] flex items-center justify-center">

                {/* The Slanted Line */}
                <div
                    className="absolute w-[120%] h-[4px] bg-gradient-to-r from-[#B45309] via-[#FDE68A] to-[#B45309]"
                    style={{
                        top: '50%',
                        left: '-10%',
                        transform: 'rotate(-2deg)', // Slight inclination
                        boxShadow: '0 0 15px rgba(253, 230, 138, 0.6), 0 0 30px rgba(180, 83, 9, 0.4)'
                    }}
                />

                {/* Shine Effect Animation (Optional for extra polish) */}
                <div
                    className="absolute top-1/2 left-0 w-full h-[20px] bg-white blur-[20px] opacity-20 -translate-y-1/2"
                    style={{
                        transform: 'rotate(-2deg) translateY(-50%)'
                    }}
                />
            </div>
        </div>
    );
};
