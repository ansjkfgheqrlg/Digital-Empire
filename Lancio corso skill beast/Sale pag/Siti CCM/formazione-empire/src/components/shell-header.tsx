"use client";
import Link from "next/link";
import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import Wordmark from "./wordmark";

export default function ShellHeader({ variant = "public" }: { variant?: "public" | "student" | "admin" }) {
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
      style={{
        backdropFilter: scrolled ? "saturate(140%) blur(14px)" : "saturate(120%) blur(6px)",
        background: scrolled ? "rgba(26, 26, 26, 0.82)" : "rgba(26, 26, 26, 0.4)",
        borderBottom: scrolled ? "1px solid rgba(249,249,249,0.08)" : "1px solid transparent",
      }}
    >
      <div className="container-wide flex items-center justify-between py-4">
        <Wordmark size="sm" />

        {variant === "public" && (
          <nav className="hidden md:flex items-center gap-8 text-sm">
            <Link href="/#corsi" className="transition-colors" style={{ color: "rgba(249,249,249,0.7)" }}>Corsi</Link>
            <Link href="/#metodo" className="transition-colors" style={{ color: "rgba(249,249,249,0.7)" }}>Metodo</Link>
            <Link href="/#faq" className="transition-colors" style={{ color: "rgba(249,249,249,0.7)" }}>FAQ</Link>
          </nav>
        )}

        <div className="hidden md:flex items-center gap-3">
          {variant === "public" ? (
            <>
              <Link href="/login" className="text-sm font-medium" style={{ color: "#f9f9f9" }}>Accedi</Link>
              <Link href="/signup" className="btn-orange text-sm">Inizia ora</Link>
            </>
          ) : (
            <Link href="/logout" className="text-sm font-medium" style={{ color: "rgba(249,249,249,0.7)" }}>Esci</Link>
          )}
        </div>

        <button
          className="md:hidden w-10 h-10 rounded-lg flex items-center justify-center"
          style={{ background: "rgba(249,249,249,0.06)", border: "1px solid rgba(249,249,249,0.1)" }}
          onClick={() => setMobileOpen(!mobileOpen)}
          aria-label="Menu"
        >
          <div className="flex flex-col gap-1.5">
            <span className="block w-5 h-0.5 transition-transform" style={{ background: "#f9f9f9", transform: mobileOpen ? "rotate(45deg) translate(4px, 4px)" : "none" }} />
            <span className="block w-5 h-0.5" style={{ background: "#f9f9f9", opacity: mobileOpen ? 0 : 1 }} />
            <span className="block w-5 h-0.5 transition-transform" style={{ background: "#f9f9f9", transform: mobileOpen ? "rotate(-45deg) translate(4px, -4px)" : "none" }} />
          </div>
        </button>
      </div>

      <AnimatePresence>
        {mobileOpen && variant === "public" && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            transition={{ duration: 0.25 }}
            className="md:hidden border-t overflow-hidden"
            style={{ borderColor: "rgba(249,249,249,0.08)", background: "rgba(26,26,26,0.96)" }}
          >
            <div className="container-wide py-6 flex flex-col gap-4 text-base" style={{ color: "#f9f9f9" }}>
              <Link href="/#corsi" onClick={() => setMobileOpen(false)}>Corsi</Link>
              <Link href="/#metodo" onClick={() => setMobileOpen(false)}>Metodo</Link>
              <Link href="/#faq" onClick={() => setMobileOpen(false)}>FAQ</Link>
              <div className="flex flex-col gap-3 pt-4 border-t" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
                <Link href="/login" className="btn-ghost w-full justify-center" onClick={() => setMobileOpen(false)}>Accedi</Link>
                <Link href="/signup" className="btn-orange w-full justify-center" onClick={() => setMobileOpen(false)}>Inizia ora</Link>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
