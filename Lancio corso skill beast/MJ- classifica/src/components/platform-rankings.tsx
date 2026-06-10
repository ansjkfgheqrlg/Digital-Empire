import { Reveal } from "./reveal";
import { Headphones, Youtube, Music, Radio, Music2, Tv } from "lucide-react";

const platforms = [
  {
    name: "Spotify",
    icon: Headphones,
    color: "border-l-[#1DB954]",
    artists: [
      { name: "Drake", value: "1.4B" },
      { name: "Taylor Swift", value: "1.3B" },
      { name: "Michael Jackson", value: "1.2B" }
    ]
  },
  {
    name: "YouTube",
    icon: Youtube,
    color: "border-l-[#FF0000]",
    artists: [
      { name: "Justin Bieber", value: "1.2B" },
      { name: "Michael Jackson", value: "850M" },
      { name: "The Weeknd", value: "600M" }
    ]
  },
  {
    name: "Apple Music",
    icon: Music,
    color: "border-l-[#FB233B]",
    artists: [
      { name: "Drake", value: "600M" },
      { name: "Taylor Swift", value: "450M" },
      { name: "Bad Bunny", value: "400M" }
    ]
  },
  {
    name: "TikTok",
    icon: Radio,
    color: "border-l-[#000000]",
    artists: [
      { name: "Taylor Swift", value: "3.1B" },
      { name: "Bad Bunny", value: "2.8B" },
      { name: "Michael Jackson", value: "2.5B" }
    ]
  },
  {
    name: "Amazon Music",
    icon: Music2,
    color: "border-l-[#00A8E1]",
    artists: [
      { name: "Taylor Swift", value: "500M" },
      { name: "Bad Bunny", value: "450M" },
      { name: "The Weeknd", value: "400M" }
    ]
  },
  {
    name: "Twitch",
    icon: Tv,
    color: "border-l-[#9146FF]",
    artists: [
      { name: "Michael Jackson", value: "15M" },
      { name: "Drake", value: "12M" },
      { name: "Bad Bunny", value: "9M" }
    ]
  }
];

export function PlatformRankings() {
  return (
    <section className="section bg-grey section-border-t">
      <div className="max-w-6xl mx-auto px-6 relative z-10">
        <Reveal className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            <span className="text-silver-black">Dominio per</span> <span className="text-purple-pure italic font-serif">Piattaforma</span>
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto font-medium">
            Analisi granulare dei leader su ogni singolo ecosistema digitale.
          </p>
        </Reveal>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {platforms.map((platform, idx) => (
            <Reveal key={platform.name} delay={idx * 0.1}>
              <div className={`card-premium p-6 border-l-4 ${platform.color} h-full`}>
                <div className="flex items-center gap-3 mb-6 relative z-10">
                  <platform.icon className="w-5 h-5 text-gray-400" />
                  <h3 className="font-bold text-xl text-black uppercase tracking-wider">{platform.name}</h3>
                </div>
                <div className="space-y-4">
                  {platform.artists.map((artist, i) => (
                    <div key={artist.name} className="flex justify-between items-center group">
                      <div className="flex items-center gap-3">
                        <span className="text-xs font-bold text-gray-300 font-mono">0{i + 1}</span>
                        <span className="text-sm font-bold text-black group-hover:text-purple transition-colors">{artist.name}</span>
                      </div>
                      <span className="text-xs font-mono font-bold bg-gray-100 px-2 py-1 rounded text-black">
                        {artist.value}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
