import type { Metadata } from "next";
import { Onest } from "next/font/google";
import "./globals.css";

const onest = Onest({
  variable: "--font-sans",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700", "800", "900"],
});

export const metadata: Metadata = {
  title: "Proposta Commerciale · Digital Empire × EXPONIUM",
  description: "Proposta riservata per EXPONIUM. Infrastruttura AI per outreach e content su misura.",
  robots: { index: false, follow: false },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="it" className={`${onest.variable} h-full antialiased dark`}>
      <body className="min-h-full flex flex-col bg-[#0a0a0a] text-[#f9f9f9] font-sans grain-fine">
        {children}
      </body>
    </html>
  );
}
