import type { Metadata, Viewport } from "next";
import { Onest, Instrument_Serif } from "next/font/google";
import "./globals.css";
import "./vivo.css"; // solo per le sezioni aggiunte: ogni regola è scopata sotto .vivo
import "./aggiunte-hero.css"; // D1/D2/A02 (ordini di Max 13/09): classi nuove + la sola regola D2 sul padding dell'hero
import "./aggiunte-a.css"; // Atto II/III (D3, D4, D5, A05, A07, A08)
import "./aggiunte-b.css"; // Atto III/IV (A09, A10+A20, A11, A12)
import "./aggiunte-c.css"; // Atto V/VI (A14-A22)
import "./rifatte-a.css"; // sezioni di giugno RIFATTE (stesso testo): VSL, ContentOutput, ToolStack — ordine di Max 13/09
import "./rifatte-b.css"; // sezioni di giugno RIFATTE (stesso testo): SystemsShowcase, Objections, Competitors, FinalOffer
import "./ritocchi.css"; // ritocchi in solo CSS alle sezioni di giugno (ordine di Max 13/09) - dossier 39B par.2
import "./scala.css"; // de-ingrandimento (ordine di Max 13/09) - dossier 39B par.1.3; DEVE restare ultimo
import "./f4-hero.css"; // F4 (dossier 40): hero pulito, card fluttuanti, nastro sottile — dopo scala.css su ordine di Max
import "./f4-colori.css"; // F4: --grad-max, card Tre sistemi + 7gg/300+/0€, titolo largo, grana Numeri/Per chi, frase barrata, freccia #02
import "./f4-storia.css"; // F4: sezione nuova «storia dei preventivi»
import "./f4-brain.css"; // F4: Due tipi con texture grana-fuoco, Second Brain blu + 3 card, cervello
import "./f5-hero.css"; // F5: hero a sinistra, foto di Max a destra, ombre dietro le scritte
import "./f5-card.css"; // F5: card fluttuanti nello stile dell'all. 02 (illustrazioni granulose)
import "./f5-frecce.css"; // F5: frecce dai blocchi Tre sistemi, freccia #02 corretta, foto di riferimento con freccia
import "./f5-cta.css"; // F5: le tre pagine CTA (una per prodotto)
import { SmoothScrollProvider } from "@/components/smooth-scroll-provider";

const onest = Onest({
  variable: "--font-sans",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700", "800"],
});

const instrumentSerif = Instrument_Serif({
  variable: "--font-serif",
  subsets: ["latin"],
  weight: "400",
  style: ["normal", "italic"],
});

export const metadata: Metadata = {
  title: "Digital Empire | Sistemi AI Proprietari per la Tua Operatività",
  description: "Installiamo sistemi AI sul tuo server: Outreach Factory, Content Factory e Second Brain. Zero canoni mensili. Codice tuo per sempre. Setup in 7 giorni.",
  robots: { index: false, follow: false },
  // AGGIUNTA 2026-09-12 (solo aggiunte): anteprima quando il link viene condiviso (WhatsApp, LinkedIn, IG, Telegram).
  // Prima: solo titolo e descrizione, nessuna immagine. `public/og.jpg` è nuovo, 1200×630, grana + argento + un accento.
  metadataBase: new URL("https://agency-empire-landing.vercel.app"),
  openGraph: {
    type: "website",
    locale: "it_IT",
    siteName: "Digital Empire",
    title: "Digital Empire | Sistemi AI Proprietari per la Tua Operatività",
    description: "Installiamo sistemi AI sul tuo server: Outreach Factory, Content Factory e Second Brain. Zero canoni mensili. Codice tuo per sempre. Setup in 7 giorni.",
    images: [{ url: "/og.jpg", width: 1200, height: 630, alt: "Digital Empire — Sistemi AI che girano sul tuo server. Zero canoni." }],
  },
  twitter: { card: "summary_large_image", images: ["/og.jpg"] },
};

export const viewport: Viewport = { themeColor: "#2a2a2a" };

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="it"
      suppressHydrationWarning
      className={`${onest.variable} ${instrumentSerif.variable} h-full antialiased dark`}
    >
      <body className="min-h-full flex flex-col bg-[#2a2a2a] text-[#f9f9f9] font-sans grain-fine">
        {/* Enable scroll-reveal animations only when JS is running.
            Runs before paint so content never flashes; if JS is
            disabled/paused the page stays fully visible. */}
        <script
          dangerouslySetInnerHTML={{
            __html: "document.documentElement.classList.add('js')",
          }}
        />
        <SmoothScrollProvider>{children}</SmoothScrollProvider>
      </body>
    </html>
  );
}
