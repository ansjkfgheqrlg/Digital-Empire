import Link from "next/link";
import Wordmark from "@/components/wordmark";

const NOISE =
  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.15' numOctaves='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.9 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")";

export default function AuthLayout({ children }: { children: React.ReactNode }) {
  return (
    <div
      className="relative min-h-screen flex flex-col"
      style={{
        background:
          "radial-gradient(ellipse 70% 55% at 25% 20%, rgba(251,70,4,0.22) 0%, transparent 55%), radial-gradient(ellipse 60% 50% at 85% 85%, rgba(255,138,74,0.14) 0%, transparent 60%), linear-gradient(180deg, #0a0a0a 0%, #050505 100%)",
      }}
    >
      <div
        aria-hidden
        className="fixed inset-0 pointer-events-none"
        style={{
          backgroundImage: NOISE,
          opacity: 0.35,
          mixBlendMode: "overlay",
          zIndex: 1,
        }}
      />

      <header className="relative z-10 py-6">
        <div className="container-wide flex items-center justify-between">
          <Wordmark size="sm" href="/" />
          <Link
            href="/"
            className="text-sm font-medium text-silver-mute transition-colors hover:text-silver-soft"
          >
            ← Torna al sito
          </Link>
        </div>
      </header>

      <main className="relative z-10 flex-1 flex items-center justify-center px-4 py-8">
        {children}
      </main>

      <footer className="relative z-10 py-6 text-center text-xs text-silver-dim">
        © Formazione Empire — Digital Empire
      </footer>
    </div>
  );
}
