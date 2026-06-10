import Link from "next/link";
import Wordmark from "./wordmark";

export default function ShellFooter() {
  return (
    <footer className="relative border-t bg-ink-2" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
      <div className="container-wide py-16">
        <div className="grid md:grid-cols-4 gap-10 mb-12">
          <div className="md:col-span-2">
            <Wordmark size="md" />
            <p className="mt-5 text-sm max-w-md leading-relaxed" style={{ color: "rgba(249,249,249,0.62)" }}>
              La piattaforma ufficiale di <strong className="text-orange-pure">Digital Empire</strong> per la formazione premium
              su <strong style={{ color: "#f9f9f9" }}>AI, business digitale, copywriting e launch</strong>.
              Corsi costruiti da chi il mercato lo ha già battuto.
            </p>
          </div>

          <div>
            <h4 className="text-sm font-semibold mb-4" style={{ color: "#f9f9f9" }}>Piattaforma</h4>
            <ul className="flex flex-col gap-3 text-sm" style={{ color: "rgba(249,249,249,0.62)" }}>
              <li><Link href="/#corsi">Corsi</Link></li>
              <li><Link href="/#metodo">Metodo</Link></li>
              <li><Link href="/#faq">FAQ</Link></li>
              <li><Link href="/login">Accedi</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="text-sm font-semibold mb-4" style={{ color: "#f9f9f9" }}>Legale</h4>
            <ul className="flex flex-col gap-3 text-sm" style={{ color: "rgba(249,249,249,0.62)" }}>
              <li><Link href="/privacy">Privacy Policy</Link></li>
              <li><Link href="/termini">Termini di servizio</Link></li>
              <li><Link href="/contatti">Contatti</Link></li>
            </ul>
          </div>
        </div>

        <div className="orange-divider mb-8" />

        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 text-xs" style={{ color: "rgba(249,249,249,0.45)" }}>
          <p>© {new Date().getFullYear()} Digital Empire. Tutti i diritti riservati.</p>
          <p className="flex items-center gap-2">
            <span className="inline-block w-1.5 h-1.5 rounded-full" style={{ background: "#fb4604" }} />
            Costruito con attenzione ossessiva al dettaglio
          </p>
        </div>
      </div>
    </footer>
  );
}
