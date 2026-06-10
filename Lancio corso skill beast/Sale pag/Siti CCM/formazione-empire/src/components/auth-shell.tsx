"use client";
import Link from "next/link";
import Wordmark from "./wordmark";
import { motion } from "framer-motion";
import { Sparkles } from "lucide-react";
import type { ReactNode } from "react";

type Props = {
  title: string;
  subtitle: string;
  children: ReactNode;
  footer?: ReactNode;
};

export default function AuthShell({ title, subtitle, children, footer }: Props) {
  return (
    <div className="min-h-screen grid lg:grid-cols-[1fr_minmax(0,520px)]" style={{ background: "#1c1c1c" }}>
      {/* Left: brand panel with orange radial */}
      <div
        className="hidden lg:flex relative overflow-hidden flex-col justify-between p-12"
        style={{
          background: "linear-gradient(160deg, #1c1c1c 0%, #161616 45%, #1a0f0a 100%)",
        }}
      >
        <div
          aria-hidden
          className="absolute inset-0 opacity-60 pointer-events-none"
          style={{
            backgroundImage:
              "radial-gradient(circle at 20% 25%, rgba(251,70,4,0.35) 0%, transparent 50%), radial-gradient(circle at 80% 75%, rgba(255,138,74,0.18) 0%, transparent 48%)",
          }}
        />
        <div
          aria-hidden
          className="absolute inset-0 opacity-[0.07] pointer-events-none"
          style={{
            backgroundImage:
              "linear-gradient(rgba(251,70,4,0.4) 1px, transparent 1px), linear-gradient(90deg, rgba(251,70,4,0.4) 1px, transparent 1px)",
            backgroundSize: "64px 64px",
          }}
        />

        <div className="relative z-10">
          <Link href="/" className="inline-flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl flex items-center justify-center font-extrabold text-xl" style={{ background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 50%, #c9370a 100%)", color: "#ffffff", boxShadow: "0 8px 24px -8px rgba(251,70,4,0.5)" }}>
              F
            </div>
            <span className="text-2xl font-extrabold tracking-tight" style={{ color: "#f9f9f9" }}>
              Formazione <span className="text-silver-orange">Empire</span>
            </span>
          </Link>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: [0.22, 1, 0.36, 1] }}
          className="relative z-10 max-w-md"
        >
          <span className="bubble-orange mb-6 inline-flex">
            <Sparkles className="h-3.5 w-3.5" />
            Accesso riservato agli studenti
          </span>
          <h2 className="text-3xl md:text-4xl font-extrabold leading-[1.06] mb-5">
            <span className="text-silver-white">Entra nella tua</span>
            <br />
            <span className="text-silver-orange">piattaforma premium.</span>
          </h2>
          <p className="text-base leading-[1.65]" style={{ color: "rgba(249,249,249,0.72)" }}>
            Tutti i tuoi corsi, le risorse e la tua progressione — in <strong className="text-orange-pure">un unico posto</strong>,
            costruito con <span className="text-silver-orange font-semibold">attenzione ossessiva al dettaglio</span>.
          </p>
        </motion.div>

        <div className="relative z-10 flex items-center gap-6 text-xs" style={{ color: "rgba(249,249,249,0.5)" }}>
          <span className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full" style={{ background: "#fb4604" }} />
            Crittografia end-to-end
          </span>
          <span className="flex items-center gap-2">
            <span className="w-1.5 h-1.5 rounded-full" style={{ background: "#fb4604" }} />
            Accesso a vita
          </span>
        </div>
      </div>

      {/* Right: auth form panel */}
      <div className="flex flex-col min-h-screen" style={{ background: "#1c1c1c", borderLeft: "1px solid rgba(249,249,249,0.06)" }}>
        <div className="lg:hidden p-6 border-b" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
          <Wordmark size="sm" />
        </div>

        <div className="flex-1 flex items-center justify-center p-6 md:p-10">
          <motion.div
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
            className="w-full max-w-md"
          >
            <h1 className="text-2xl md:text-3xl font-extrabold tracking-tight mb-2" style={{ color: "#f9f9f9" }}>
              {title}
            </h1>
            <p className="text-sm md:text-base mb-8 leading-[1.6]" style={{ color: "rgba(249,249,249,0.6)" }}>
              {subtitle}
            </p>

            {children}

            {footer && (
              <div className="mt-8 pt-6 border-t text-sm text-center" style={{ borderColor: "rgba(249,249,249,0.08)", color: "rgba(249,249,249,0.62)" }}>
                {footer}
              </div>
            )}
          </motion.div>
        </div>

        <div className="p-6 text-center text-xs" style={{ color: "rgba(249,249,249,0.4)" }}>
          © {new Date().getFullYear()} Digital Empire · <Link href="/privacy">Privacy</Link> · <Link href="/termini">Termini</Link>
        </div>
      </div>
    </div>
  );
}
