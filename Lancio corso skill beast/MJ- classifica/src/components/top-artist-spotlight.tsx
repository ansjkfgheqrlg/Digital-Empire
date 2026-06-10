import { Reveal } from "@/components/reveal";
import { Star, Film, Crown, Zap } from "lucide-react";

export function TopArtistSpotlight() {
  return (
    <section className="section bg-paper relative overflow-visible section-border-t pt-32 pb-32">
      {/* Background elements */}
      <div className="absolute top-0 right-0 w-full h-full bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-silver/40 via-transparent to-transparent pointer-events-none"></div>
      <div className="absolute -left-40 top-40 w-96 h-96 bg-purple/10 blur-[120px] rounded-full pointer-events-none"></div>

      <div className="max-w-7xl mx-auto px-6 relative z-10">
        <div className="flex flex-col lg:flex-row items-center justify-center gap-16 lg:gap-24">
          
          {/* Left Text */}
          <div className="flex-1 text-center lg:text-left order-2 lg:order-1">
            <Reveal>
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white border border-gray-200 shadow-sm mb-8">
                <Crown className="w-4 h-4 text-purple-bright" />
                <span className="text-xs font-bold uppercase tracking-widest text-ink">Top Artist Spotlight</span>
              </div>
            </Reveal>

            <Reveal delay={0.1}>
              <h2 className="font-black mb-10 tracking-tighter text-ink leading-[0.95] flex flex-col items-center lg:items-start text-center lg:text-left">
                <div className="flex flex-wrap items-baseline gap-x-3 justify-center lg:justify-start">
                  <span className="text-5xl md:text-7xl text-purple-pure whitespace-nowrap uppercase">Michael Jackson,</span>
                  <span className="text-2xl md:text-3xl lg:text-4xl text-ink font-bold mb-1 whitespace-nowrap">ritorna Primo</span>
                </div>
                <span className="text-5xl md:text-7xl text-purple-pure mt-2 whitespace-nowrap">in Classifica.</span>
              </h2>
            </Reveal>

            <Reveal delay={0.2}>
              <p className="text-lg md:text-xl text-gray-600 mb-10 font-medium leading-relaxed">
                Il Re del Pop riconquista la vetta globale a decenni di distanza. La spinta principale è l'attesa febbrile per <strong>"Michael"</strong>, il nuovo <span className="hl-block">film biopic ufficiale</span>, che ha generato un'onda anomala di stream senza precedenti in tutto il mondo.
              </p>
            </Reveal>

            <Reveal delay={0.3}>
              <ul className="space-y-6 text-left inline-block lg:block">
                <li className="flex items-start gap-5">
                  <div className="w-10 h-10 rounded-full bg-purple/10 flex items-center justify-center shrink-0 mt-0.5 border border-purple/20">
                    <Film className="w-5 h-5 text-purple" />
                  </div>
                  <div>
                    <h4 className="font-bold text-ink text-xl mb-1">Effetto Biopic</h4>
                    <p className="text-gray-500 font-medium">Incremento esponenziale degli ascolti spinto dalla diffusione delle prime immagini ufficiali e dal cast stellare del film.</p>
                  </div>
                </li>
                <li className="flex items-start gap-5">
                  <div className="w-10 h-10 rounded-full bg-purple/10 flex items-center justify-center shrink-0 mt-0.5 border border-purple/20">
                    <Zap className="w-5 h-5 text-purple" />
                  </div>
                  <div>
                    <h4 className="font-bold text-ink text-xl mb-1">Viralità Cross-Generazionale</h4>
                    <p className="text-gray-500 font-medium">Il Moonwalk e le sue inarrivabili coreografie dominano nuovamente i trend, catturando l'intera Generazione Z su TikTok.</p>
                  </div>
                </li>
                <li className="flex items-start gap-5">
                  <div className="w-10 h-10 rounded-full bg-purple/10 flex items-center justify-center shrink-0 mt-0.5 border border-purple/20">
                    <Star className="w-5 h-5 text-purple" />
                  </div>
                  <div>
                    <h4 className="font-bold text-ink text-xl mb-1">Risveglio del Catalogo</h4>
                    <p className="text-gray-500 font-medium">Hit storiche come "Billie Jean" e "Thriller" registrano numeri da record, rientrando di prepotenza nelle classifiche mondiali.</p>
                  </div>
                </li>
              </ul>
            </Reveal>
          </div>

          {/* Right Image - MONUMENTAL SCALE & DIVIDER ATTACH */}
          <div className="flex-1 w-full flex justify-center order-1 lg:order-2 self-center">
            <Reveal delay={0.4} className="relative w-full flex flex-col items-center justify-center overflow-visible">
              {/* Premium Background Glows */}
              <div className="absolute inset-0 bg-gradient-to-tr from-purple/40 via-purple-bright/20 to-transparent rounded-[60px] -rotate-3 scale-110 -z-10 blur-[100px] animate-pulse-premium"></div>
              <div className="absolute inset-0 bg-gradient-to-bl from-silver/20 to-transparent rounded-full rotate-12 scale-125 -z-10 blur-[120px]"></div>
              
              <div className="relative w-full flex items-center justify-center overflow-visible">
                <img 
                  src="/images/mj-transparent-birefnet.png" 
                  alt="Michael Jackson Performing" 
                  className="object-contain w-auto h-[820px] transition-all duration-1000 ease-out z-10"
                  style={{
                    maskImage: 'linear-gradient(to bottom, black 85%, transparent 100%)',
                    WebkitMaskImage: 'linear-gradient(to bottom, black 85%, transparent 100%)'
                  }}
                />
                
                {/* Subject Rim Light Glow */}
                <div className="absolute inset-0 bg-purple/15 blur-[100px] rounded-full mix-blend-screen pointer-events-none opacity-60 z-0"></div>
              </div>
              
              {/* Floating Element - REDESIGNED: Smaller, Elegant & Gradient */}
              <div className="absolute bottom-32 -left-4 md:-left-12 bg-silver-purple py-2.5 px-4 rounded-2xl animate-float shadow-[0_20px_50px_rgba(123,44,191,0.5)] z-30 border border-white/30 backdrop-blur-sm">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-white/20 backdrop-blur-md text-white flex items-center justify-center border border-white/40 shadow-inner">
                    <Star className="w-4 h-4 fill-current" />
                  </div>
                  <div className="flex flex-col">
                    <div className="text-[11px] font-black text-white uppercase tracking-widest leading-none mb-1">#1 Global</div>
                    <div className="text-[8px] text-white/90 font-bold tracking-[0.2em] uppercase opacity-90">Undisputed King</div>
                  </div>
                </div>
              </div>
            </Reveal>
          </div>

        </div>
      </div>
    </section>
  );
}
