import type { Metadata, Viewport } from "next";
import { Onest, Instrument_Serif } from "next/font/google";
import "./globals.css";
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

const SITE_URL = "https://agency-empire-landing.vercel.app";
const TITLE = "Digital Empire | Sistemi AI Proprietari per la Tua Operatività";
const DESCRIPTION =
  "Installiamo sistemi AI sul tuo server: Outreach Factory, Content Factory e Second Brain. Zero canoni mensili. Codice tuo per sempre. Setup in 7 giorni.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/" },
  // TODO(F1-E4): togliere `robots` quando la pagina di prenotazione avra' il brand
  // giusto. Indicizzare prima manderebbe traffico su "Claude Code Mastery".
  robots: { index: false, follow: false },
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
