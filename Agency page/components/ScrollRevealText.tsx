
import React, { useRef } from 'react';
import { motion, useScroll, useTransform, useSpring } from 'framer-motion';

const textContent = "fondato su intelligenza, velocità e risultati reali. digital empire è l'ingegneria di nuova generazione alimentata dall'ai, progettata per chi esige un vantaggio competitivo sleale.";

const Word: React.FC<{ word: string, progress: any, range: [number, number] }> = ({ word, progress, range }) => {
  const opacity = useTransform(progress, range, [0.1, 1]);
  const y = useTransform(progress, range, [15, 0]); // Movimento leggero dal basso
  
  // Gradiente Argento Liquido/Satinato
  const silverGradient = "linear-gradient(180deg, #FFFFFF 0%, #CBD5E1 50%, #94A3B8 100%)";

  return (
    <motion.span
      style={{ 
        opacity, 
        y,
        backgroundImage: silverGradient,
        WebkitBackgroundClip: 'text',
        backgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
        display: 'inline-block'
      }}
      className="mr-[0.35em] mb-2 font-sans font-medium lowercase tracking-tight"
    >
      {word}
    </motion.span>
  );
};

export const ScrollRevealText: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const words = textContent.split(" ");
  
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start 0.8", "start 0.2"] // Attivazione ritardata per non sovrapporsi all'hero
  });

  const smoothProgress = useSpring(scrollYProgress, {
    stiffness: 40,
    damping: 30
  });

  return (
    <section 
      ref={containerRef} 
      className="relative pt-40 pb-32 bg-transparent flex flex-col items-center justify-center overflow-hidden z-20"
    >
      <div className="container mx-auto px-6 max-w-4xl text-center relative z-10">
        <div className="flex flex-wrap justify-center items-center">
          {words.map((word, i) => {
            const start = i / words.length;
            const end = start + (1 / words.length);
            return (
              <Word 
                key={i} 
                word={word} 
                progress={smoothProgress} 
                range={[start, end]} 
              />
            );
          })}
        </div>
      </div>

      <style>{`
        .container span {
          /* Dimensioni contenute ed eleganti */
          font-size: clamp(1.1rem, 2vw, 1.8rem);
          line-height: 1.6;
        }
      `}</style>
    </section>
  );
};
