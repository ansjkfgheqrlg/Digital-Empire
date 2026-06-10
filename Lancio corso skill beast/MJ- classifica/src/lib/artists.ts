export type Artist = {
  id: string;
  name: string;
  alias: string;
  score: number;
  previousRank: number;
  platforms: {
    spotify: string;
    youtube: string;
    apple: string;
    tiktok: string;
    amazon: string;
    twitch: string;
  };
  topSong: {
    title: string;
    year: string;
  };
  bio: string;
  artisticLife: string;
  personalLife: string;
};



const realArtistsData = [
  { name: "Michael Jackson", alias: "King of Pop", top: "Billie Jean" },
  { name: "The Weeknd", alias: "Starboy", top: "Blinding Lights" },
  { name: "Taylor Swift", alias: "T-Swizzle", top: "Anti-Hero" },
  { name: "Drake", alias: "Drizzy", top: "God's Plan" },
  { name: "Bad Bunny", alias: "El Conejo Malo", top: "Tití Me Preguntó" },
  { name: "Ariana Grande", alias: "Ari", top: "7 rings" },
  { name: "Justin Bieber", alias: "Biebs", top: "Stay" },
  { name: "Ed Sheeran", alias: "Teddy", top: "Shape of You" },
  { name: "Rihanna", alias: "RiRi", top: "Lift Me Up" },
  { name: "Beyoncé", alias: "Queen Bey", top: "Cuff It" },
  { name: "Harry Styles", alias: "Haz", top: "As It Was" },
  { name: "Bruno Mars", alias: "Brunito", top: "Uptown Funk" },
  { name: "Dua Lipa", alias: "Dua", top: "Levitating" },
  { name: "Eminem", alias: "Slim Shady", top: "Lose Yourself" },
  { name: "Post Malone", alias: "Posty", top: "Circles" },
  { name: "Billie Eilish", alias: "Billie", top: "Bad Guy" },
  { name: "Kendrick Lamar", alias: "K-Dot", top: "Humble" },
  { name: "SZA", alias: "Sosa", top: "Kill Bill" },
  { name: "Miley Cyrus", alias: "Miley", top: "Flowers" },
  { name: "Travis Scott", alias: "La Flame", top: "Sicko Mode" },
  { name: "Kanye West", alias: "Ye", top: "Stronger" },
  { name: "Lady Gaga", alias: "Mother Monster", top: "Bad Romance" },
  { name: "Doja Cat", alias: "Doja", top: "Paint The Town Red" },
  { name: "Morgan Wallen", alias: "Morgan", top: "Last Night" },
  { name: "Olivia Rodrigo", alias: "Liv", top: "Drivers License" },
  { name: "Adele", alias: "Adele", top: "Hello" },
  { name: "Shakira", alias: "Shaki", top: "Hips Don't Lie" },
  { name: "Karol G", alias: "La Bichota", top: "Provenza" },
  { name: "Coldplay", alias: "Coldplay", top: "Yellow" },
  { name: "Imagine Dragons", alias: "Dragons", top: "Believer" },
  { name: "J Balvin", alias: "Balvin", top: "Mi Gente" },
  { name: "David Guetta", alias: "Guetta", top: "Titanium" },
  { name: "Calvin Harris", alias: "Calvin", top: "One Kiss" },
  { name: "Maroon 5", alias: "Maroon", top: "Sugar" },
  { name: "Queen", alias: "Legendary", top: "Bohemian Rhapsody" },
  { name: "The Beatles", alias: "Fab Four", top: "Hey Jude" },
  { name: "Elton John", alias: "Rocket Man", top: "Rocket Man" },
  { name: "Katy Perry", alias: "Katy", top: "Roar" },
  { name: "Maluma", alias: "Papi Juancho", top: "Hawái" },
  { name: "Rosalía", alias: "La Rosalía", top: "Despechá" },
  { name: "Snoop Dogg", alias: "Snoop", top: "Drop It Like It's Hot" },
  { name: "Dr. Dre", alias: "Dre", top: "Still D.R.E." },
  { name: "Jay-Z", alias: "Hov", top: "Empire State of Mind" },
  { name: "J. Cole", alias: "Cole", top: "No Role Modelz" },
  { name: "Future", alias: "Pluto", top: "Mask Off" },
  { name: "Lana Del Rey", alias: "Lana", top: "Summertime Sadness" },
  { name: "Shawn Mendes", alias: "Shawn", top: "Señorita" },
  { name: "Camila Cabello", alias: "Camila", top: "Havana" },
  { name: "Selena Gomez", alias: "Sel", top: "Lose You To Love Me" },
  { name: "Nicki Minaj", alias: "Barbie", top: "Super Freaky Girl" },
  { name: "Cardi B", alias: "Bardi", top: "Bodak Yellow" },
  { name: "21 Savage", alias: "21", top: "Bank Account" },
  { name: "Metro Boomin", alias: "Metro", top: "Creepin'" },
  { name: "Central Cee", alias: "Cench", top: "Doja" },
  { name: "Burna Boy", alias: "African Giant", top: "Last Last" },
  { name: "Wizkid", alias: "Starboy", top: "Essence" },
  { name: "Feid", alias: "Ferxxo", top: "Classy 101" },
  { name: "Peso Pluma", alias: "Doble P", top: "Ella Baila Sola" },
  { name: "NewJeans", alias: "NewJeans", top: "Ditto" },
  { name: "BTS", alias: "BTS", top: "Dynamite" },
  { name: "Blackpink", alias: "BP", top: "How You Like That" },
  { name: "Jung Kook", alias: "JK", top: "Seven" },
  { name: "Ice Spice", alias: "Spice", top: "Munch" },
  { name: "Jack Harlow", alias: "Jack", top: "First Class" },
  { name: "Lil Nas X", alias: "Montero", top: "Old Town Road" },
  { name: "Sam Smith", alias: "Sam", top: "Unholy" },
  { name: "Hozier", alias: "Hozier", top: "Take Me To Church" },
  { name: "Noah Kahan", alias: "Noah", top: "Stick Season" },
  { name: "Tate McRae", alias: "Tate", top: "greedy" },
  { name: "Sabrina Carpenter", alias: "Sabrina", top: "Espresso" },
  { name: "Tyla", alias: "Tyla", top: "Water" },
  { name: "Gunna", alias: "Wunna", top: "fukumean" },
  { name: "Lil Baby", alias: "Baby", top: "Drip Too Hard" },
  { name: "Young Thug", alias: "Thugger", top: "Go Crazy" },
  { name: "Juice WRLD", alias: "Juice", top: "Lucid Dreams" },
  { name: "XXXTentacion", alias: "X", top: "SAD!" },
  { name: "Pop Smoke", alias: "Woo", top: "Dior" },
  { name: "A$AP Rocky", alias: "Lord Flacko", top: "Praise The Lord" },
  { name: "Tyler, The Creator", alias: "Tyler", top: "EARFQUAKE" },
  { name: "Frank Ocean", alias: "Frank", top: "Pink + White" },
  { name: "Childish Gambino", alias: "Bino", top: "Redbone" },
  { name: "The Kid LAROI", alias: "LAROI", top: "Stay" },
  { name: "Glass Animals", alias: "Glass", top: "Heat Waves" },
  { name: "Arctic Monkeys", alias: "Monkeys", top: "Do I Wanna Know?" },
  { name: "Tame Impala", alias: "Tame", top: "The Less I Know The Better" },
  { name: "Gorillaz", alias: "Gorillaz", top: "Feel Good Inc." },
  { name: "Daft Punk", alias: "Daft", top: "Get Lucky" },
  { name: "Avicii", alias: "Legend", top: "Wake Me Up" },
  { name: "Swedish House Mafia", alias: "SHM", top: "Don't You Worry Child" },
  { name: "Marshmello", alias: "Mello", top: "Happier" },
  { name: "Kygo", alias: "Kygo", top: "Firestone" },
  { name: "Tiësto", alias: "Tiësto", top: "The Business" },
  { name: "Zedd", alias: "Zedd", top: "Clarity" },
  { name: "The Chainsmokers", alias: "Chainsmokers", top: "Closer" },
  { name: "OneRepublic", alias: "Ryan Tedder", top: "Counting Stars" },
  { name: "Linkin Park", alias: "LP", top: "In The End" },
  { name: "Metallica", alias: "Metallica", top: "Enter Sandman" },
  { name: "Nirvana", alias: "Kurt", top: "Smells Like Teen Spirit" },
  { name: "AC/DC", alias: "Thunder", top: "Back In Black" },
  { name: "Guns N' Roses", alias: "Slash", top: "Sweet Child O' Mine" }
];

export const initialArtists: Artist[] = realArtistsData.map((data, i) => {
  const baseScore = 125000 - (i * 800);
  const id = data.name.toLowerCase().replace(/[^a-z0-9]/g, '-');
  
  return {
    id: i === 0 ? "mj" : id,
    name: data.name,
    alias: data.alias,
    score: i === 0 ? 125000 : baseScore,
    previousRank: i + 1,
    platforms: {
      spotify: `${(1500 - i * 12).toFixed(0)}M+`,
      youtube: `${(1000 - i * 8).toFixed(0)}M+`,
      apple: `${(500 - i * 4).toFixed(0)}M+`,
      tiktok: `${(3000 - i * 25).toFixed(0)}M+`,
      amazon: `${(400 - i * 3).toFixed(0)}M+`,
      twitch: `${(15 - i * 0.12).toFixed(1)}M+`
    },
    topSong: { title: data.top, year: i < 10 ? "2024" : "2023" },
    bio: `${data.name} è una delle figure più influenti della musica moderna, con un impatto globale che attraversa generazioni.`,
    artisticLife: i === 0 
      ? `Il Re del Pop assoluto. Autore di "Thriller", l'album più venduto della storia umana. I suoi tour leggendari come il "Dangerous World Tour" e l'"HIStory World Tour" hanno ridefinito il concetto di intrattenimento su scala planetaria, fondendo coreografie inarrivabili, illusionismo e una presenza scenica che ha cambiato per sempre l'industria dello spettacolo. Ogni sua performance è considerata un masterclass di genio e perfezione.`
      : i === 1 
      ? `Ha dominato l'era digitale con un sound oscuro e cinematografico. L'esibizione al Super Bowl LV ha consacrato la sua visione artistica, mentre hit mastodontiche come "Blinding Lights" hanno infranto ogni record su Billboard. La sua evoluzione da misterioso talento R&B a dominatore incontrastato del pop globale è senza precedenti.`
      : i === 2
      ? `L'artista dei record. Il suo "Eras Tour" è diventato il tour più redditizio della storia della musica, trasformando stadi di tutto il mondo in eventi sismici (letteralmente). Con una narrativa lirica senza pari e la capacità di reinventare costantemente il suo genere, le sue performance dal vivo sono ormai pilastri della cultura pop contemporanea.`
      : `${data.name}, conosciuto mondialmente come "${data.alias}", ha dominato le classifiche globali ridefinendo il sound della sua generazione. Con esibizioni in stadi sold-out in tutti i continenti, brani iconici come "${data.top}" continuano a infrangere ogni record. Le sue performance dal vivo sono un mix esplosivo di energia tecnica e magnetismo scenico.`,
    personalLife: i === 0
      ? `Dietro l'immensa figura pubblica si celava un animo incredibilmente sensibile e filantropico. Appassionato di arte classica, cinema d'animazione ed effetti speciali, Michael ha costruito "Neverland" come rifugio creativo. Amava i dettagli maniacali in ogni cosa che faceva e donò centinaia di milioni a cause benefiche in tutto il mondo, trasformando la sua vulnerabilità nel più grande dono per l'umanità.`
      : i === 1
      ? `Lontano dalle luci stroboscopiche, Abel è un profondo cinefilo. Il suo amore per i film horror classici, il cinema indipendente e le estetiche al neon anni '80 ispira non solo la sua musica ma il suo intero modo di vivere. Un introverso cronico che preferisce il silenzio della scrittura al caos della vita da VIP.`
      : i === 2
      ? `Al di là della sua immensa popolarità, è nota per il suo legame indissolubile con i suoi fan (gli Swifties) e per la sua vita privata costantemente sotto i riflettori, che lei abilmente trasforma in capolavori musicali. Appassionata di letteratura, gatti e baking, mantiene un forte attaccamento alle sue radici e alle piccole gioie quotidiane.`
      : `Lontano dal palco e dai microfoni, la vera identità dietro "${data.alias}" è ricca di sfumature inaspettate. Tra passioni private, interessi creativi trasversali, hobby insoliti e un costante impegno fuori dallo studio di registrazione, nasconde lati di una personalità magnetica che lo rendono ancora più affascinante per il suo fandom.`
  };
});


