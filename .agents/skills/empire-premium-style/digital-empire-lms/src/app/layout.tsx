import type { Metadata, Viewport } from "next";
import { Onest } from "next/font/google";
import "./globals.css";
import { SmoothScrollProvider } from "@/components/common/smooth-scroll-provider";
import { Reveal } from "@/components/common/reveal";

const onest = Onest({
  subsets: ["latin"],
  variable: "--font-sans",
  weight: ["300", "400", "500", "600", "700", "800"],
  display: "swap",
});

export const viewport: Viewport = {
  themeColor: "#1c1c1c",
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  title: "Digital Empire Mastery | The Architecture of Premium AI Platforms",
  description: "Il percorso definitivo per costruire piattaforme digitali di lusso con l'AI.",
  robots: { index: false, follow: false },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="it" className="dark scroll-smooth">
      <body className={`${onest.variable} font-sans antialiased grain-fine`}>
        <SmoothScrollProvider>
          {children}
        </SmoothScrollProvider>
      </body>
    </html>
  );
}
