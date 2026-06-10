import type { Metadata, Viewport } from "next";
import { Onest } from "next/font/google";
import "./globals.css";
import { SmoothScrollProvider } from "@/components/smooth-scroll-provider";
import { Sidebar } from "@/components/sidebar";
import { MobileNav } from "@/components/mobile-nav";

const onest = Onest({
  variable: "--font-sans",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700", "800"],
});

export const metadata: Metadata = {
  title: "Outreach Command Center | Digital Empire",
  description: "Sistema interno di monitoraggio e gestione Outreach Engine.",
  robots: { index: false, follow: false },
};

export const viewport: Viewport = { themeColor: "#0a0a0a" };

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="it" className={`${onest.variable} h-full antialiased dark`}>
      <body className="min-h-full bg-ink text-[#f9f9f9] font-sans grain-fine flex flex-col md:flex-row overflow-x-hidden">
        <MobileNav />
        <Sidebar />
        <main className="flex-1 min-w-0">
          <SmoothScrollProvider>{children}</SmoothScrollProvider>
        </main>
      </body>
    </html>
  );
}
