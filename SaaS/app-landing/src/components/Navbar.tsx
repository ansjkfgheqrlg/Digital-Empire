"use client";

import Link from "next/link";
import { Sparkles } from "lucide-react";
import { motion } from "framer-motion";

export function Navbar() {
  return (
    <div className="fixed top-8 left-0 right-0 z-50 flex items-center justify-between px-10 pointer-events-none">
      
      {/* Logo Floating Button */}
      <motion.div 
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        className="pointer-events-auto liquid-glass px-5 py-3 rounded-2xl flex items-center gap-3 group cursor-pointer"
      >
        <Sparkles className="w-5 h-5 text-primary group-hover:rotate-12 transition-transform" />
        <span className="font-sans font-bold text-sm tracking-widest uppercase text-zinc-100">LandingForge</span>
      </motion.div>

      {/* Nav links Floating Group */}
      <motion.div 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="hidden md:flex items-center gap-1 pointer-events-auto liquid-glass p-1.5 rounded-2xl"
      >
        <Link href="#product" className="px-6 py-2.5 rounded-xl text-[11px] font-bold uppercase tracking-widest text-zinc-400 hover:text-white hover:bg-white/5 transition-all">Product</Link>
        <Link href="#resources" className="px-6 py-2.5 rounded-xl text-[11px] font-bold uppercase tracking-widest text-zinc-400 hover:text-white hover:bg-white/5 transition-all">Resources</Link>
        <Link href="#pricing" className="px-6 py-2.5 rounded-xl text-[11px] font-bold uppercase tracking-widest text-zinc-400 hover:text-white hover:bg-white/5 transition-all">Pricing</Link>
        <Link href="#community" className="px-6 py-2.5 rounded-xl text-[11px] font-bold uppercase tracking-widest text-zinc-400 hover:text-white hover:bg-white/5 transition-all">Community</Link>
      </motion.div>

      {/* CTA Floating Button */}
      <motion.div 
        initial={{ opacity: 0, x: 20 }}
        animate={{ opacity: 1, x: 0 }}
        className="pointer-events-auto"
      >
        <Link href="#waitlist">
          <button className="liquid-glass px-6 py-3 rounded-2xl text-[11px] font-black uppercase tracking-[0.2em] text-white hover:bg-white/10 transition-all shadow-[0_0_20px_rgba(168,85,247,0.3)] hover:shadow-[0_0_40px_rgba(168,85,247,0.5)] active:scale-95">
            Join Waitlist
          </button>
        </Link>
      </motion.div>

    </div>
  );
}

