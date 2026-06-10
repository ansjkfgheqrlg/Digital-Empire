# layout.tsx — template

Crea `src/app/layout.tsx` così:

```tsx
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
  title: "<SITE TITLE>",
  description: "<SITE DESCRIPTION>",
  robots: { index: false, follow: false },
  openGraph: {
    title: "<SITE TITLE>",
    description: "<SITE DESCRIPTION>",
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
```

## REGOLE
- `dark` class sull'html è OBBLIGATORIA (il design è dark-first).
- `grain-fine` sul body è OBBLIGATORIO.
- `bg-[#2a2a2a]` di fallback dietro alle sezioni.
- `robots: { index: false, follow: false }` di default — cambia solo se l'utente dice che il sito è pubblico.
- `lang` da preservare dal source se diverso da "it".
- `themeColor` sempre `#2a2a2a`.
