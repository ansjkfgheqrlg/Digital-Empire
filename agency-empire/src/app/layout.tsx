import type { Metadata, Viewport } from "next";
import { Onest, Cinzel, Playfair_Display } from "next/font/google";
import "./globals.css";
import { SmoothScrollProvider } from "@/components/smooth-scroll-provider";
import { GrainLayers } from "@/components/grain-layers";

const onest = Onest({
  variable: "--font-onest",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700", "800"],
  display: "swap",
});

const cinzel = Cinzel({
  variable: "--font-cinzel",
  subsets: ["latin"],
  weight: ["400", "700", "900"],
  display: "swap",
});

const playfair = Playfair_Display({
  variable: "--font-playfair",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  style: ["normal", "italic"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://agency-empire-kohl.vercel.app"),
  title: "Digital Empire · AI Workflow Agency · Outreach & Content Automation",
  description:
    "Implementiamo AI Workflow per imprenditori e agenzie. Outreach automatizzato, content al 100%, zero operatività manuale. Demo gratuita in 30 minuti.",
  openGraph: {
    title: "Digital Empire · AI Workflow Agency",
    description:
      "Outreach e Content Workflow AI — consegnati chiavi in mano. 40+ automazioni, +300% produttività, demo gratuita.",
    type: "website",
    locale: "it_IT",
    url: "https://agency-empire-kohl.vercel.app",
  },
  robots: { index: true, follow: true },
};

export const viewport: Viewport = {
  themeColor: "#0a0a0a",
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="it"
      className={`${onest.variable} ${cinzel.variable} ${playfair.variable} h-full antialiased dark`}
    >
      <body className="min-h-full flex flex-col bg-ink text-white font-sans grain-fine">
        <a
          href="#main"
          className="sr-only focus:not-sr-only fixed top-4 left-4 z-[400] btn-gold"
        >
          Salta al contenuto
        </a>
        <GrainLayers />
        <SmoothScrollProvider>{children}</SmoothScrollProvider>
      </body>
    </html>
  );
}
