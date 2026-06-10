import { initialArtists } from "@/lib/artists";
import { Reveal } from "@/components/reveal";
import { ArrowLeft, Headphones, Youtube, Music, Radio, Trophy, Sparkles, TrendingUp, Music2, Tv, Star, User } from "lucide-react";
import Link from "next/link";
import { notFound } from "next/navigation";


export async function generateStaticParams() {
  return initialArtists.map((artist) => ({
    id: artist.id,
  }));
}

export default async function ArtistPage({ params }: { params: Promise<{ id: string }> }) {

  const { id } = await params;
  const artist = initialArtists.find((a) => a.id === id);

  if (!artist) {
    notFound();
  }

  return (
    <main className="min-h-screen bg-ink-2 relative overflow-hidden">
      {/* Artist Page Glow */}
      <div className="hero-dust-container opacity-60">
        <div className="hero-dust-1"></div>
        <div className="hero-dust-2"></div>
        <div className="hero-dust-particles opacity-40"></div>
      </div>

      {/* Back Button */}
      <div className="absolute top-8 left-8 z-50">
        <Link href="/" className="group flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-gradient-to-r from-[#d9d4e1]/10 to-[#7B2CBF]/20 border border-white/10 hover:border-purple/40 hover:from-[#d9d4e1]/20 hover:to-[#7B2CBF]/30 transition-all text-xs font-semibold tracking-wide text-gray-300 hover:text-white backdrop-blur-md shadow-[0_4px_20px_-5px_rgba(123,44,191,0.3)]">
          <ArrowLeft className="w-3.5 h-3.5 transition-transform group-hover:-translate-x-0.5" />
          Torna alla Classifica
        </Link>
      </div>

      {/* Hero Section Artist */}
      <section className="section pt-32 pb-20 relative grain-overlay">
        <div className="max-w-6xl mx-auto px-6 relative z-10">
          <Reveal>
            <div className="flex flex-col md:flex-row items-end gap-8 mb-12">
              <div className="flex-1">
                <div className="bubble-purple mb-6">
                  <Sparkles className="w-4 h-4" />
                  <span>Profilo Superstar Verificato</span>
                </div>
                <div className="relative">
                  {/* Premium Background Splashes "Smash" */}
                  <div className="absolute -top-32 -left-32 w-[600px] h-[600px] bg-gradient-to-br from-purple/25 via-silver-purple/10 to-transparent blur-[140px] rounded-full z-0 pointer-events-none opacity-60"></div>
                  
                  <h1 className="text-6xl md:text-[7.5rem] font-black mb-6 tracking-tight leading-[0.75] relative z-10">
                    <span className="text-silver-white inline-block pb-6 mb-[-1.5rem]">{artist.name.split(' ')[0]}</span>
                    <br />
                    <span className="text-silver-purple text-7xl md:text-[10rem] inline-block pt-2">{artist.name.split(' ').slice(1).join(' ')}</span>
                  </h1>
                </div>
                <p className="text-2xl text-gray-400 font-medium italic">
                  "{artist.alias}"
                </p>
              </div>
              <div className="flex flex-col items-end gap-2">
                <div className="text-8xl font-mono font-black text-purple/20 absolute -right-4 -top-12 opacity-50 select-none">
                  RANK #1
                </div>
                <div className="card-purple p-6 flex flex-col items-center gap-2 min-w-[200px]">
                  <Trophy className="w-8 h-8 text-white animate-bounce" />
                  <span className="text-sm font-bold uppercase tracking-widest text-white/60">Punteggio Live</span>
                  <span className="text-4xl font-mono font-bold text-white">{artist.score.toLocaleString()}</span>
                </div>
              </div>
            </div>
          </Reveal>

          {/* Stats Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-20">
            <Reveal delay={0.1}>
                <div className="card-premium p-8 flex flex-col gap-4 border-l-4 border-l-green-500 hover:translate-y-[-5px] transition-transform relative overflow-hidden">
                  <div className="relative z-10">
                    <div className="w-12 h-12 rounded-xl bg-green-500/20 flex items-center justify-center mb-4">
                      <Headphones className="w-6 h-6 text-green-500" />
                    </div>
                    <div>
                      <h4 className="text-gray-600 text-xs font-bold uppercase tracking-widest mb-1">Spotify Streams</h4>
                      <p className="text-3xl font-mono font-bold text-black">{artist.platforms.spotify}</p>
                    </div>
                  </div>
                </div>
            </Reveal>
            <Reveal delay={0.2}>
              <div className="card-premium p-8 flex flex-col gap-4 border-l-4 border-l-red-500 hover:translate-y-[-5px] transition-transform relative overflow-hidden">
                <div className="relative z-10">
                  <div className="w-12 h-12 rounded-xl bg-red-500/20 flex items-center justify-center mb-4">
                    <Youtube className="w-6 h-6 text-red-500" />
                  </div>
                  <div>
                    <h4 className="text-gray-600 text-xs font-bold uppercase tracking-widest mb-1">YouTube Views</h4>
                    <p className="text-3xl font-mono font-bold text-black">{artist.platforms.youtube}</p>
                  </div>
                </div>
              </div>
            </Reveal>
            <Reveal delay={0.3}>
              <div className="card-premium p-8 flex flex-col gap-4 border-l-4 border-l-pink-500 hover:translate-y-[-5px] transition-transform relative overflow-hidden">
                <div className="relative z-10">
                  <div className="w-12 h-12 rounded-xl bg-pink-500/20 flex items-center justify-center mb-4">
                    <Music className="w-6 h-6 text-pink-500" />
                  </div>
                  <div>
                    <h4 className="text-gray-600 text-xs font-bold uppercase tracking-widest mb-1">Apple Music</h4>
                    <p className="text-3xl font-mono font-bold text-black">{artist.platforms.apple}</p>
                  </div>
                </div>
              </div>
            </Reveal>
            <Reveal delay={0.4}>
              <div className="card-premium p-8 flex flex-col gap-4 border-l-4 border-l-blue-400 hover:translate-y-[-5px] transition-transform relative overflow-hidden">
                <div className="relative z-10">
                  <div className="w-12 h-12 rounded-xl bg-blue-400/20 flex items-center justify-center mb-4">
                    <Radio className="w-6 h-6 text-blue-400" />
                  </div>
                  <div>
                    <h4 className="text-gray-600 text-xs font-bold uppercase tracking-widest mb-1">TikTok Impact</h4>
                    <p className="text-3xl font-mono font-bold text-black">{artist.platforms.tiktok}</p>
                  </div>
                </div>
              </div>
            </Reveal>
            <Reveal delay={0.5}>
              <div className="card-premium p-8 flex flex-col gap-4 border-l-4 border-l-cyan-500 hover:translate-y-[-5px] transition-transform relative overflow-hidden">
                <div className="relative z-10">
                  <div className="w-12 h-12 rounded-xl bg-cyan-500/20 flex items-center justify-center mb-4">
                    <Music2 className="w-6 h-6 text-cyan-500" />
                  </div>
                  <div>
                    <h4 className="text-gray-600 text-xs font-bold uppercase tracking-widest mb-1">Amazon Music</h4>
                    <p className="text-3xl font-mono font-bold text-black">{artist.platforms.amazon}</p>
                  </div>
                </div>
              </div>
            </Reveal>
            <Reveal delay={0.6}>
              <div className="card-premium p-8 flex flex-col gap-4 border-l-4 border-l-purple-600 hover:translate-y-[-5px] transition-transform relative overflow-hidden">
                <div className="relative z-10">
                  <div className="w-12 h-12 rounded-xl bg-purple-600/20 flex items-center justify-center mb-4">
                    <Tv className="w-6 h-6 text-purple-600" />
                  </div>
                  <div>
                    <h4 className="text-gray-600 text-xs font-bold uppercase tracking-widest mb-1">Twitch Live</h4>
                    <p className="text-3xl font-mono font-bold text-black">{artist.platforms.twitch}</p>
                  </div>
                </div>
              </div>
            </Reveal>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 mt-10">
            {/* Artistic Life */}
            <Reveal delay={0.5}>
              <div className="card-premium h-full flex flex-col gap-6 relative overflow-hidden group">
                {/* Background image/gradient inside card */}
                <div className="absolute -top-32 -right-32 w-80 h-80 bg-purple/20 blur-[80px] rounded-full group-hover:bg-purple/30 transition-colors pointer-events-none"></div>
                <div className="relative z-10 flex items-center gap-4">
                  <div className="w-14 h-14 rounded-full bg-purple/10 flex items-center justify-center border border-purple/20 shadow-inner">
                    <Star className="w-6 h-6 text-purple-bright" />
                  </div>
                  <div>
                    <h2 className="text-3xl md:text-4xl font-black text-ink">Il Dominio Scenico</h2>
                    <p className="text-purple uppercase tracking-widest text-xs font-bold mt-1">Carriera e Performance</p>
                  </div>
                </div>
                <p className="text-lg text-gray-700 leading-relaxed font-medium relative z-10">
                  {artist.artisticLife}
                </p>
                <div className="mt-auto pt-6 border-t border-purple/10 relative z-10">
                  <h3 className="text-purple font-bold uppercase tracking-widest text-sm mb-4">La Traccia Suprema</h3>
                  <div className="flex items-center gap-6">
                    <div className="text-5xl font-black text-purple/20 font-mono">01</div>
                    <div>
                      <p className="text-2xl font-bold text-ink">{artist.topSong.title}</p>
                    </div>
                  </div>
                </div>
              </div>
            </Reveal>

            {/* Personal Life */}
            <Reveal delay={0.6}>
              <div className="card-dark h-full flex flex-col gap-6 relative overflow-hidden group border-white/5">
                <div className="absolute -bottom-32 -left-32 w-80 h-80 bg-silver-purple/5 blur-[80px] rounded-full group-hover:bg-silver-purple/10 transition-colors pointer-events-none"></div>
                <div className="relative z-10 flex items-center gap-4">
                  <div className="w-14 h-14 rounded-full bg-white/5 flex items-center justify-center border border-white/10 shadow-inner">
                    <User className="w-6 h-6 text-silver-white" />
                  </div>
                  <div>
                    <h2 className="text-3xl md:text-4xl font-black text-silver-white">Oltre il Sipario</h2>
                    <p className="text-gray-400 uppercase tracking-widest text-xs font-bold mt-1">La Persona Dietro l'Artista</p>
                  </div>
                </div>
                <p className="text-lg text-gray-400 leading-relaxed font-medium relative z-10">
                  {artist.personalLife}
                </p>
              </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Footer minimal */}
      <footer className="py-20 border-t border-white/10 text-center">
        <p className="text-gray-600 text-sm font-medium">
          Dati elaborati in tempo reale dal motore MJ Ranking &copy; 2026
        </p>
      </footer>
    </main>
  );
}
