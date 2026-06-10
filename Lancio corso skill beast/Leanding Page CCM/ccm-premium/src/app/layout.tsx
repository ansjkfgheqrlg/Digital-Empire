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
  title: "Call Strategica 1:1 | Claude Code Mastery · Digital Empire",
  description:
    "45 minuti di formazione 1:1 su Claude Code con Digital Empire. 90% formazione, 10% pitch — carte scoperte.",
  robots: { index: false, follow: false },
  openGraph: {
    title: "Call Strategica 1:1 | Claude Code Mastery · Digital Empire",
    description: "45 minuti 1:1 con Digital Empire. Costruire con l'AI. Gratis, carte scoperte.",
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
