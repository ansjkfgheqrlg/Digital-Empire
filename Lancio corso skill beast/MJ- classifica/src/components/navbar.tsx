"use client";

import { useState, useEffect } from "react";
import { AuthModal } from "@/components/auth-modal";
import { User, LogIn, Menu, X, Crown } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import Link from "next/link";

export function Navbar() {
  const [isAuthOpen, setIsAuthOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <>
      <nav 
        className={`fixed top-4 left-1/2 -translate-x-1/2 w-[92%] max-w-5xl z-[80] transition-all duration-500 overflow-hidden ${
          mobileMenuOpen ? "rounded-[24px]" : "rounded-[24px] md:rounded-full"
        } ${
          scrolled 
            ? "py-2 md:py-2.5 bg-black/85 backdrop-blur-3xl border border-white/10 shadow-[0_10px_40px_rgba(0,0,0,0.8),inset_0_1px_1px_rgba(255,255,255,0.15)] saturate-[180%]" 
            : "py-3 md:py-3.5 bg-black/40 backdrop-blur-xl border border-white/10 shadow-[0_8px_30px_rgba(0,0,0,0.4)]"
        }`}
      >
        <div className="absolute inset-0 bg-gradient-to-b from-white/5 to-transparent pointer-events-none"></div>
        <div className="px-5 md:px-6 flex items-center justify-between relative z-10">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-2 group">
            <div className="w-8 h-8 rounded-lg bg-purple-pure flex items-center justify-center shadow-[0_0_15px_rgba(123,44,191,0.5)] group-hover:scale-110 transition-transform duration-500">
              <Crown className="w-4 h-4 text-white" />
            </div>
            <span className="text-lg font-black tracking-tighter text-silver-white uppercase">MJ <span className="text-purple-pure">Classifica</span></span>
          </Link>

          {/* Desktop Nav */}
          <div className="hidden md:flex items-center gap-8">
            <Link href="#ranking" className="text-[11px] font-black uppercase tracking-widest text-gray-400 hover:text-purple-pure transition-colors">Classifica</Link>
            <Link href="#community" className="text-[11px] font-black uppercase tracking-widest text-gray-400 hover:text-purple-pure transition-colors">Community</Link>
            <Link href="#methodology" className="text-[11px] font-black uppercase tracking-widest text-gray-400 hover:text-purple-pure transition-colors">Metodologia</Link>
            
            <div className="h-4 w-px bg-white/10 mx-1"></div>
            
            <button 
              onClick={() => setIsAuthOpen(true)}
              className="btn-purple !py-2 !px-5 text-xs shadow-[0_0_15px_rgba(123,44,191,0.3)] hover:shadow-[0_0_25px_rgba(123,44,191,0.5)]"
            >
              <LogIn className="w-3.5 h-3.5" /> Accedi
            </button>
          </div>

          {/* Mobile Toggle */}
          <button 
            className="md:hidden text-white/80 hover:text-white p-2 transition-colors"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>

        {/* Mobile Menu */}
        <AnimatePresence>
          {mobileMenuOpen && (
            <motion.div 
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              exit={{ opacity: 0, height: 0 }}
              className="md:hidden bg-ink-2 border-b border-white/10 overflow-hidden"
            >
              <div className="px-6 py-8 flex flex-col gap-6">
                <Link href="#ranking" onClick={() => setMobileMenuOpen(false)} className="text-sm font-bold text-gray-400">Classifica</Link>
                <Link href="#community" onClick={() => setMobileMenuOpen(false)} className="text-sm font-bold text-gray-400">Community</Link>
                <Link href="#methodology" onClick={() => setMobileMenuOpen(false)} className="text-sm font-bold text-gray-400">Metodologia</Link>
                <button 
                  onClick={() => {
                    setMobileMenuOpen(false);
                    setIsAuthOpen(true);
                  }}
                  className="btn-purple justify-center"
                >
                  Accedi
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </nav>

      <AnimatePresence>
        {isAuthOpen && (
          <AuthModal isOpen={isAuthOpen} onClose={() => setIsAuthOpen(false)} />
        )}
      </AnimatePresence>
    </>
  );
}
