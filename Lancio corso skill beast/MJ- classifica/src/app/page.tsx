import { RankingBoard } from "@/components/ranking-board";
import { Reveal } from "@/components/reveal";
import { PlatformRankings } from "@/components/platform-rankings";
import { Methodology } from "@/components/methodology";
import { TopArtistSpotlight } from "@/components/top-artist-spotlight";
import { AppPromo } from "@/components/app-promo";
import { CommunityHub } from "@/components/community-hub";
import { Navbar } from "@/components/navbar";
import { ArrowRight, Star, Zap } from "lucide-react";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col overflow-hidden">
      <Navbar />
      {/* ... Hero Section remains the same ... */}
      <section className="section bg-ink-2 relative flex flex-col items-center justify-center min-h-[90vh]">

        {/* NEW: Hero Dust (Polvere viola/argento) */}
        <div className="hero-dust-container">
          <div className="hero-dust-1"></div>
          <div className="hero-dust-2"></div>
          <div className="hero-dust-particles"></div>
        </div>

        {/* Silver chips floating */}
        <div className="silver-chip float-a top-16 left-[8%]">
          <strong>#1</strong> Michael Jackson
        </div>
        <div className="silver-chip float-b top-24 right-[10%]">
          <strong>Top</strong> Artists
        </div>
        <div className="silver-chip float-c bottom-40 left-[18%]">
          <strong>Live</strong> Data
        </div>
        <div className="silver-chip float-d bottom-32 right-[10%]">
          <strong>Global</strong> Stream
        </div>

        <div className="max-w-5xl mx-auto px-6 text-center relative z-10 flex flex-col items-center">
          <Reveal delay={0.1} className="mb-8">
            <span className="pre-headline">Live Global Ranking</span>
          </Reveal>
          
          <Reveal delay={0.2}>
            <div className="relative">
              {/* Premium Background Splashes "Smash" */}
              <div className="absolute -top-32 -left-32 w-[600px] h-[600px] bg-gradient-to-br from-purple/25 via-silver-purple/10 to-transparent blur-[140px] rounded-full z-0 pointer-events-none opacity-60"></div>
              
              <h1 className="flex flex-col items-center text-center font-black mb-10 tracking-tight leading-tight relative z-10 px-20">
                <span className="text-silver-white text-5xl md:text-7xl lg:text-8xl pt-4 pb-4">The Digital</span>
                <span className="text-silver-white text-8xl md:text-[14rem] lg:text-[18rem] -mt-4 md:-mt-8 lg:-mt-12 py-2">Music</span>
                <span className="text-silver-purple text-6xl md:text-9xl lg:text-[10rem] -mt-4 md:-mt-10 lg:-mt-16 py-2">Superstars.</span>
              </h1>
            </div>
          </Reveal>

          <Reveal delay={0.3}>
            <p className="text-lg md:text-xl text-gray-400 mb-12 max-w-4xl mx-auto font-medium leading-relaxed">
              Il nostro <strong className="text-purple-bold">algoritmo proprietario</strong> monitora costantemente l'<strong className="text-purple-bold">impatto globale</strong> delle superstar musicali attraverso l'integrazione di <strong className="text-purple-bold">Spotify, YouTube, Apple Music, TikTok, Amazon Music, Twitch e Billboard</strong>. 
              Ogni secondo, milioni di datapoint vengono analizzati per garantirti una <strong className="text-purple-bold">visione cristallina</strong> e incontestabile del dominio digitale assoluto in <span className="hl-block">modalità live estrema</span>.
            </p>
          </Reveal>

          <Reveal delay={0.4}>
            <a href="#ranking" className="btn-purple btn-purple--lg group">
              <Zap className="w-5 h-5" />
              Vedi la Classifica Live
              <ArrowRight className="w-5 h-5 transition-transform group-hover:translate-x-1" />
            </a>
          </Reveal>
        </div>

        {/* Premium Marquee */}
        <div className="absolute bottom-0 left-0 w-full marquee-premium py-2 overflow-hidden z-20">
          <div className="flex w-max marquee items-center">
            {[...Array(12)].map((_, i) => (
              <span key={i} className="text-marquee-ink uppercase text-[10px] md:text-xs whitespace-nowrap flex items-center gap-4 pr-8">
                <Star className="w-3.5 h-3.5 text-black opacity-80" fill="currentColor" /> 
                DIGITAL EMPIRE PREMIUM <span className="opacity-40 px-2">•</span> 
                LIVE GLOBAL RANKING
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* Ranking Section */}
      <section id="ranking" className="section bg-paper section-border-t">
        <div className="max-w-6xl mx-auto px-6 relative z-10">
          <Reveal className="text-center mb-16">
            <h2 className="text-4xl md:text-6xl font-bold mb-6">
              <span className="text-silver-black">Classifica</span> <span className="text-purple-pure italic font-serif">in tempo reale</span>
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto font-medium">
              I punteggi si aggiornano costantemente in base agli stream globali, le vendite e l'impatto digitale. Solo il re della scena resta in cima.
            </p>
          </Reveal>

          <RankingBoard />
        </div>
      </section>

      {/* NEW: Top Artist Spotlight */}
      <TopArtistSpotlight />

      {/* Premium Divider */}
      <div className="h-2 w-full bg-silver-purple shadow-[0_0_25px_rgba(157,78,221,0.4)] relative z-20"></div>

      {/* NEW: Platform Rankings */}
      <PlatformRankings />

      {/* NEW: Community Hub & Blog */}
      <CommunityHub />

      {/* NEW: Methodology */}
      <Methodology />

      {/* NEW: App Promo */}
      <AppPromo />

      {/* Footer */}
      <footer className="bg-ink-2 py-12 section-border-t">
        <div className="max-w-6xl mx-auto px-6 flex flex-col items-center">
          <Reveal>
            <div className="text-2xl font-bold text-silver-white mb-4">MJ Classifica</div>
            <p className="text-gray-500 text-sm text-center">
              © {new Date().getFullYear()} Digital Empire Premium Style. Built for the King.
            </p>
          </Reveal>
        </div>
      </footer>
    </main>
  );
}
