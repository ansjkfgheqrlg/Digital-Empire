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
  title: "Infrastruttura Operativa Lanci AI — Digital Empire",
  description: "Due workflow AI custom ed una dashboard proprietaria per governare l'outreach ed il copywriting del tuo lancio.",
  robots: { index: false, follow: false },
  openGraph: {
    title: "Infrastruttura Operativa Lanci AI — Digital Empire",
    description: "Due workflow AI custom ed una dashboard proprietaria per governare l'outreach ed il copywriting del tuo lancio.",
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
