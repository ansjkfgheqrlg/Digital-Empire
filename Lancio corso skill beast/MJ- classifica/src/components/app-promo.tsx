import { Reveal } from "@/components/reveal";
import { Smartphone, Download, Star } from "lucide-react";

export function AppPromo() {
  return (
    <section className="section bg-ink-2 relative overflow-hidden section-border-t">
      {/* Background Glows */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-gradient-to-br from-purple/20 via-silver-purple/5 to-transparent blur-[120px] rounded-full z-0 pointer-events-none"></div>

      <div className="max-w-6xl mx-auto px-6 relative z-10 flex flex-col md:flex-row items-center gap-16 lg:gap-24">
        
        {/* Left Text */}
        <div className="flex-1 text-center md:text-left">
          <Reveal>
            <span className="pre-headline mb-6">In Arrivo</span>
          </Reveal>
          
          <Reveal delay={0.1}>
            <h2 className="text-5xl md:text-7xl font-bold mb-6 tracking-tight">
              <span className="text-silver-white">L'App Ufficiale.</span><br/>
              <span className="text-purple-bold">Presto Disponibile.</span>
            </h2>
          </Reveal>
          
          <Reveal delay={0.2}>
            <p className="text-lg md:text-xl text-gray-400 mb-10 max-w-2xl font-medium leading-relaxed">
              Tutta la potenza della Classifica Globale direttamente nelle tue mani. Ricevi notifiche in tempo reale sui sorpassi, monitora i tuoi idoli e accedi a dati esclusivi <span className="hl-block">solo sull'app</span>.
            </p>
          </Reveal>
          
          <Reveal delay={0.3}>
            <div className="flex flex-col sm:flex-row items-center justify-center md:justify-start gap-4">
              <div className="btn-ghost opacity-70 cursor-not-allowed group">
                <Download className="w-5 h-5" />
                <div className="text-left">
                  <div className="text-[10px] uppercase tracking-wider text-gray-400">Presto disponibile su</div>
                  <div className="font-bold text-sm">App Store</div>
                </div>
              </div>
              <div className="btn-ghost opacity-70 cursor-not-allowed group">
                <Download className="w-5 h-5" />
                <div className="text-left">
                  <div className="text-[10px] uppercase tracking-wider text-gray-400">Presto disponibile su</div>
                  <div className="font-bold text-sm">Google Play</div>
                </div>
              </div>
            </div>
          </Reveal>
        </div>

        {/* Right Graphic (Mockup Placeholder) */}
        <div className="flex-1 w-full flex justify-center">
          <Reveal delay={0.4} className="relative w-full max-w-md">
            <div className="relative z-10 card-dark flex flex-col items-center justify-center p-12 h-[500px] shadow-2xl rounded-[40px] border-t border-purple/30">
              <Smartphone className="w-24 h-24 text-silver-purple mb-8" />
              <div className="text-center">
                <div className="text-2xl font-black text-silver-white mb-2">MJ Classifica</div>
                <div className="text-purple-bright font-medium tracking-widest text-sm uppercase">Digital Empire</div>
              </div>
              
              {/* Floating elements inside mockup */}
              <div className="absolute top-16 -right-6 bubble-purple shadow-2xl animate-bounce">
                <Star className="w-3 h-3" fill="currentColor" /> Live
              </div>
            </div>
            
            {/* Corner Brackets on the Mockup */}
            <div className="corner-bracket corner-tl"></div>
            <div className="corner-bracket corner-tr"></div>
            <div className="corner-bracket corner-bl"></div>
            <div className="corner-bracket corner-br"></div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
