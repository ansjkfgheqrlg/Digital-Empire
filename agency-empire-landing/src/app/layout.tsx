import type { Metadata, Viewport } from "next";
import { Onest, Instrument_Serif } from "next/font/google";
import "./globals.css";
import "./vivo.css";
import { SmoothScrollProvider } from "@/components/smooth-scroll-provider";
import { GrainLayers } from "@/components/grain-layers";
import { EmpireAnalytics } from "@/components/analytics";
import { SITE_TITLE, SITE_DESCRIPTION } from "@/lib/constants";

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

const SITE_URL = "https://agency-empire-landing.vercel.app";
const TITLE = SITE_TITLE;
const DESCRIPTION = SITE_DESCRIPTION;
// Dossier 37 v2, C2.2: l'anteprima GitHub Pages (GH_PAGES_BASE valorizzato) non si indicizza mai —
// sarebbe contenuto duplicato. Su Vercel (base vuota) il sito si indicizza: la porta d'uscita è /prenota/,
// col brand giusto, quindi il vecchio TODO(F1-E4) è chiuso.
const ANTEPRIMA = Boolean(process.env.GH_PAGES_BASE);

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/" },
  robots: ANTEPRIMA ? { index: false, follow: false } : { index: true, follow: true },
  openGraph: {
    type: "website",
    locale: "it_IT",
    url: SITE_URL,
    siteName: "Digital Empire",
    title: TITLE,
    description: DESCRIPTION,
  },
  twitter: {
    card: "summary_large_image",
    title: TITLE,
    description: DESCRIPTION,
  },
};

export const viewport: Viewport = { themeColor: "#0a0a0a", width: "device-width", initialScale: 1 };

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="it"
      suppressHydrationWarning
      className={`${onest.variable} ${instrumentSerif.variable} h-full antialiased dark`}
    >
      <body className="min-h-full flex flex-col bg-[#0a0a0a] text-white font-sans grain-fine">
        <a href="#main" className="sr-only focus:not-sr-only fixed top-4 left-4 z-[400] sv-btn">Salta al contenuto</a>
        <GrainLayers />
        {/* Enable scroll-reveal animations only when JS is running.
            Runs before paint so content never flashes; if JS is
            disabled/paused the page stays fully visible. */}
        <script
          dangerouslySetInnerHTML={{
            __html: "document.documentElement.classList.add('js')",
          }}
        />
        <SmoothScrollProvider>{children}</SmoothScrollProvider>
        <EmpireAnalytics />
      </body>
    </html>
  );
}
