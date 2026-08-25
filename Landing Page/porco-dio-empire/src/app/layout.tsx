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
  title: "Claude Code Mastery | Il Framework I.C.R.O.",
  description: "Il framework in 4 step che trasforma Claude Code nel tuo collaboratore perfetto. 12 pagine, 1 template pronto. Gratis.",
  robots: { index: false, follow: false },
  openGraph: {
    title: "Claude Code Mastery | Il Framework I.C.R.O.",
    description: "Il metodo in 1 pagina che trasforma Claude Code nel tuo collaboratore perfetto. Scaricalo gratis.",
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
