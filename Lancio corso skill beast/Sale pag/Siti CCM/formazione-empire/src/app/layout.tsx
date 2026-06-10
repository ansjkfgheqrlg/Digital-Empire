import type { Metadata, Viewport } from "next";
import { Onest } from "next/font/google";
import "./globals.css";
import { SmoothScrollProvider } from "@/components/smooth-scroll-provider";

const onest = Onest({
  variable: "--font-sans",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700", "800"],
});

export const metadata: Metadata = {
  title: "Formazione Empire — La piattaforma per diventare AI Architect",
  description: "La piattaforma ufficiale di Digital Empire. Corsi premium per professionisti dell'intelligenza artificiale: Da AI User a System Architect, Launch Mastery, CRO Copy Mastery.",
  icons: { icon: "/favicon.svg" },
  robots: { index: false, follow: false },
  openGraph: {
    title: "Formazione Empire — La piattaforma per diventare AI Architect",
    description: "Corsi premium per professionisti dell'intelligenza artificiale.",
    type: "website",
    locale: "it_IT",
  },
};

export const viewport: Viewport = { themeColor: "#2a2a2a" };

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="it" className={`${onest.variable} h-full antialiased dark`}>
      <body className="min-h-full flex flex-col bg-[#2a2a2a] text-[#f9f9f9] font-sans grain-fine">
        <SmoothScrollProvider>{children}</SmoothScrollProvider>
      </body>
    </html>
  );
}
