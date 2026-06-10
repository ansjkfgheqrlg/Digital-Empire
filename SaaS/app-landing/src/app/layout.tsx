import type { Metadata } from "next";
import { Inter, Playfair_Display } from "next/font/google";
import "./globals.css";

const fontSans = Inter({
  variable: "--font-sans",
  subsets: ["latin"],
});

const fontSerif = Playfair_Display({
  variable: "--font-serif",
  subsets: ["latin"],
  style: ["normal", "italic"],
});

export const metadata: Metadata = {
  title: "LandingForge | Costruisci Landing Page che Convertono",
  description: "Crea landing page ad altissima conversione per i tuoi prodotti in pochi secondi.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="it"
      className={`${fontSans.variable} ${fontSerif.variable} dark antialiased`}
    >
      <body className="bg-background text-foreground min-h-screen flex flex-col overflow-x-hidden">
        {children}
      </body>
    </html>
  );
}
