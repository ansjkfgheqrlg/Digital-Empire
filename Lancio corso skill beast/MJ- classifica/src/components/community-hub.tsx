import { Reveal } from "@/components/reveal";
import { MessageSquare, Users, TrendingUp, Heart, Share2, Star } from "lucide-react";

const COMMENTS = [
  {
    id: 1,
    user: "KingFan_99",
    avatar: "https://api.dicebear.com/7.x/avataaars/svg?seed=King",
    text: "Il nuovo biopic di Michael Jackson cambierà tutto. Ho visto le prime clip e la somiglianza è da brividi. MJ è eterno!",
    likes: "2.4k",
    time: "2 ore fa",
    isTop: true,
  },
  {
    id: 2,
    user: "ChartMaster",
    avatar: "https://api.dicebear.com/7.x/avataaars/svg?seed=Chart",
    text: "Incredibile come MJ domini ancora le classifiche digitali. Spotify sta registrando numeri da capogiro per Billie Jean questa settimana.",
    likes: "1.8k",
    time: "5 ore fa",
    isTop: false,
  },
  {
    id: 3,
    user: "Smooth_Criminal",
    avatar: "https://api.dicebear.com/7.x/avataaars/svg?seed=Smooth",
    text: "La sezione 'Platform Rankings' è utilissima. Finalmente un posto dove vedere i dati aggregati seriamente.",
    likes: "950",
    time: "10 ore fa",
    isTop: false,
  },
  {
    id: 4,
    user: "DigitalQueen",
    avatar: "https://api.dicebear.com/7.x/avataaars/svg?seed=Queen",
    text: "Ho appena creato l'account! La qualità di questo sito è assurda, non vedo l'ora di vedere i prossimi update.",
    likes: "3.2k",
    time: "30 min fa",
    isTop: true,
  },
];

export function CommunityHub() {
  return (
    <section id="community" className="section bg-ink-2 relative overflow-hidden section-border-t pt-32 pb-40">
      {/* Background Atmosphere */}
      <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_50%_0%,_rgba(123,44,191,0.12)_0%,_transparent_50%)] pointer-events-none"></div>
      
      <div className="max-w-7xl mx-auto px-6 relative z-10">
        
        {/* Header Section */}
        <div className="flex flex-col md:flex-row items-end justify-between gap-8 mb-20">
          <div className="max-w-2xl">
            <Reveal>
              <div className="pre-headline mb-6">Digital Empire Hub</div>
            </Reveal>
            <Reveal delay={0.1}>
              <h2 className="text-5xl md:text-7xl font-black tracking-tighter leading-tight mb-6">
                <span className="text-silver-white">Join the</span> <span className="text-purple-pure italic font-serif">Global Discussion.</span>
              </h2>
            </Reveal>
            <Reveal delay={0.2}>
              <p className="text-xl text-gray-400 font-medium leading-relaxed">
                Entra a far parte della community più esclusiva del panorama musicale. 
                Analisi, commenti e discussioni in tempo reale sulle superstar che dominano il mondo.
              </p>
            </Reveal>
          </div>
          
          <Reveal delay={0.3} className="shrink-0">
            <div className="flex items-center gap-4 bg-white/5 backdrop-blur-xl border border-white/10 p-2 rounded-2xl shadow-2xl">
              <div className="flex -space-x-3 p-2">
                {[1, 2, 3, 4, 5].map((i) => (
                  <div key={i} className="w-10 h-10 rounded-full border-2 border-ink-2 bg-purple flex items-center justify-center overflow-hidden">
                    <img src={`https://api.dicebear.com/7.x/avataaars/svg?seed=${i + 20}`} alt="User" />
                  </div>
                ))}
              </div>
              <div className="pr-4 py-2 border-l border-white/10 pl-4">
                <div className="text-white font-bold text-lg leading-none">12.4k+</div>
                <div className="text-gray-500 text-[10px] uppercase font-black tracking-widest mt-1">Empire Members</div>
              </div>
            </div>
          </Reveal>
        </div>

        {/* Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          
          {/* Left Column: Popular Comments & Chat Feed */}
          <div className="lg:col-span-8 space-y-8">
            <Reveal delay={0.4} className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-purple-pure/20 flex items-center justify-center border border-purple-pure/30">
                <TrendingUp className="w-5 h-5 text-purple-bright" />
              </div>
              <h3 className="text-2xl font-bold text-silver-white">Popular Discussions</h3>
            </Reveal>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {COMMENTS.map((comment, index) => (
                <Reveal key={comment.id} delay={0.5 + (index * 0.1)}>
                  <div className="card-dark group hover:border-purple-pure/40 h-full flex flex-col">
                    <div className="flex items-center justify-between mb-6">
                      <div className="flex items-center gap-3">
                        <div className="w-12 h-12 rounded-full border-2 border-purple-pure/30 p-0.5 overflow-hidden group-hover:scale-110 transition-transform duration-500">
                          <img src={comment.avatar} alt={comment.user} className="w-full h-full object-cover rounded-full" />
                        </div>
                        <div>
                          <div className="text-white font-bold text-sm leading-none mb-1 flex items-center gap-1.5">
                            @{comment.user}
                            {comment.isTop && <Star className="w-3 h-3 fill-purple-pure text-purple-pure" />}
                          </div>
                          <div className="text-gray-500 text-[10px] font-medium uppercase tracking-wider">{comment.time}</div>
                        </div>
                      </div>
                      <div className="bubble-ink scale-75 group-hover:bg-purple-pure transition-colors">
                        <Users className="w-3 h-3" />
                        {comment.likes}
                      </div>
                    </div>
                    
                    <p className="text-gray-300 font-medium leading-relaxed mb-8 flex-grow italic">
                      "{comment.text}"
                    </p>
                    
                    <div className="flex items-center gap-6 pt-6 border-t border-white/5">
                      <button className="flex items-center gap-2 text-xs font-bold text-gray-500 hover:text-purple-pure transition-colors">
                        <Heart className="w-4 h-4" /> Like
                      </button>
                      <button className="flex items-center gap-2 text-xs font-bold text-gray-500 hover:text-purple-pure transition-colors">
                        <MessageSquare className="w-4 h-4" /> Reply
                      </button>
                      <button className="flex items-center gap-2 text-xs font-bold text-gray-500 hover:text-purple-pure transition-colors">
                        <Share2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                </Reveal>
              ))}
            </div>

            <Reveal delay={0.8}>
              <div className="card-silver-purple p-8 flex flex-col md:flex-row items-center justify-between gap-8 group">
                <div className="flex items-center gap-6">
                  <div className="w-16 h-16 rounded-2xl bg-white shadow-xl flex items-center justify-center shrink-0 rotate-3 group-hover:rotate-0 transition-transform">
                    <MessageSquare className="w-8 h-8 text-purple-pure" />
                  </div>
                  <div>
                    <h4 className="text-2xl font-black text-ink mb-1 uppercase tracking-tight">Partecipa alla chat Live</h4>
                    <p className="text-ink/60 font-medium">Unisciti a migliaia di fan in tempo reale.</p>
                  </div>
                </div>
                <button className="btn-purple shrink-0">
                  Apri Community Chat
                </button>
              </div>
            </Reveal>
          </div>

          {/* Right Column: Featured Blog Posts / Artist Insights */}
          <div className="lg:col-span-4">
            <Reveal delay={0.6} className="flex items-center gap-3 mb-8">
              <div className="w-10 h-10 rounded-xl bg-silver/20 flex items-center justify-center border border-white/10">
                <Users className="w-5 h-5 text-silver" />
              </div>
              <h3 className="text-2xl font-bold text-silver-white">Empire Insights</h3>
            </Reveal>

            <div className="space-y-6">
              <Reveal delay={0.7}>
                <div className="card-premium p-0 overflow-hidden group cursor-pointer">
                  <div className="aspect-[4/3] relative overflow-hidden">
                    <img 
                      src="https://images.unsplash.com/photo-1514525253361-bee24387052b?q=80&w=800" 
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" 
                      alt="MJ Legacy" 
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-ink via-transparent to-transparent opacity-80"></div>
                    <div className="absolute bottom-4 left-4">
                      <div className="bubble-purple py-1 px-3 text-[10px] mb-2 uppercase font-black">Featured</div>
                    </div>
                  </div>
                  <div className="p-6">
                    <h5 className="text-xl font-bold text-white mb-2 leading-tight group-hover:text-purple-pure transition-colors">
                      Michael Jackson: Perché il biopic segnerà il 2026
                    </h5>
                    <p className="text-sm text-gray-400 font-medium mb-4">
                      Analizziamo l'impatto culturale del film "Michael" sul mercato dello streaming globale.
                    </p>
                    <div className="flex items-center gap-2 text-xs font-black uppercase text-purple-bright tracking-widest">
                      Leggi Articolo <TrendingUp className="w-3 h-3" />
                    </div>
                  </div>
                </div>
              </Reveal>

              <Reveal delay={0.8}>
                <div className="card-dark p-6 border-white/5 hover:border-white/10 cursor-pointer group">
                  <div className="flex items-start gap-4">
                    <div className="w-20 h-20 rounded-lg overflow-hidden shrink-0">
                      <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=300" className="w-full h-full object-cover group-hover:scale-110 transition-transform" alt="Vinyl" />
                    </div>
                    <div>
                      <div className="text-[10px] font-black text-purple-bright uppercase mb-1">Analisi Dati</div>
                      <h5 className="text-lg font-bold text-white leading-tight mb-2">I 5 motivi dietro l'esplosione di MJ su TikTok</h5>
                      <div className="text-xs text-gray-500 font-bold">5 minuti di lettura • 12 commenti</div>
                    </div>
                  </div>
                </div>
              </Reveal>

              <Reveal delay={0.9}>
                <div className="card-dark p-6 border-white/5 hover:border-white/10 cursor-pointer group">
                  <div className="flex items-start gap-4">
                    <div className="w-20 h-20 rounded-lg overflow-hidden shrink-0">
                      <img src="https://images.unsplash.com/photo-1493225255756-d9584f8606e9?q=80&w=300" className="w-full h-full object-cover group-hover:scale-110 transition-transform" alt="Artist" />
                    </div>
                    <div>
                      <div className="text-[10px] font-black text-purple-bright uppercase mb-1">Prossime Uscite</div>
                      <h5 className="text-lg font-bold text-white leading-tight mb-2">Nuove collaborazioni postume? Rumors e realtà.</h5>
                      <div className="text-xs text-gray-500 font-bold">8 minuti di lettura • 45 commenti</div>
                    </div>
                  </div>
                </div>
              </Reveal>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}
