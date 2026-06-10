import { useState } from "react";
import { Reveal } from "@/components/reveal";
import { X, Mail, Lock, User, Github, Chrome as Google, ArrowRight, ShieldCheck, ChevronLeft } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface AuthModalProps {
  isOpen: boolean;
  onClose: () => void;
}

type AuthMode = "login" | "signup" | "recovery";

export function AuthModal({ isOpen, onClose }: AuthModalProps) {
  const [mode, setMode] = useState<AuthMode>("login");

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-6">
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="absolute inset-0 bg-ink-2/90 backdrop-blur-md"
        onClick={onClose}
      />
      
      <motion.div
        initial={{ opacity: 0, scale: 0.9, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.9, y: 20 }}
        className="relative w-full max-w-lg bg-paper rounded-[32px] overflow-hidden shadow-[0_0_80px_rgba(0,0,0,0.5)] border border-white/20"
      >
        {/* Grain Overlay */}
        <div className="absolute inset-0 pointer-events-none opacity-[0.03] mix-blend-overlay bg-repeat grain-fine"></div>
        
        {/* Header Decoration */}
        <div className="absolute top-0 left-0 w-full h-2 bg-silver-purple"></div>

        <button 
          onClick={onClose}
          className="absolute top-6 right-6 w-10 h-10 rounded-full bg-grey flex items-center justify-center text-ink hover:bg-silver transition-colors z-20"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="p-8 md:p-12">
          <AnimatePresence mode="wait">
            {mode === "login" && (
              <motion.div
                key="login"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
              >
                <div className="mb-10">
                  <h3 className="text-3xl font-black text-ink mb-2 uppercase tracking-tight">Bentornato nell'Impero</h3>
                  <p className="text-gray-500 font-medium">Accedi per gestire la tua classifica e partecipare alla community.</p>
                </div>

                <div className="space-y-4 mb-8">
                  <button className="w-full flex items-center justify-center gap-4 py-4 rounded-2xl bg-white border border-gray-200 shadow-sm hover:shadow-md transition-all font-bold text-ink">
                    <Google className="w-5 h-5" /> Continua con Google
                  </button>
                </div>

                <div className="relative mb-8">
                  <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-gray-200"></div></div>
                  <div className="relative flex justify-center text-xs uppercase"><span className="bg-paper px-4 text-gray-400 font-black tracking-widest">Oppure Email</span></div>
                </div>

                <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
                  <div className="space-y-2">
                    <label className="text-[10px] font-black uppercase tracking-widest text-gray-400 ml-4">Email</label>
                    <div className="relative">
                      <Mail className="absolute left-5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input type="email" placeholder="nome@esempio.com" className="w-full bg-grey border-2 border-transparent focus:border-purple/20 focus:bg-white rounded-2xl py-4 pl-14 pr-6 outline-none transition-all font-medium text-ink" />
                    </div>
                  </div>
                  <div className="space-y-2">
                    <div className="flex justify-between px-4">
                      <label className="text-[10px] font-black uppercase tracking-widest text-gray-400">Password</label>
                      <button type="button" onClick={() => setMode("recovery")} className="text-[10px] font-black uppercase tracking-widest text-purple-pure hover:text-purple-bright transition-colors">Dimenticata?</button>
                    </div>
                    <div className="relative">
                      <Lock className="absolute left-5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input type="password" placeholder="••••••••" className="w-full bg-grey border-2 border-transparent focus:border-purple/20 focus:bg-white rounded-2xl py-4 pl-14 pr-6 outline-none transition-all font-medium text-ink" />
                    </div>
                  </div>
                  <button type="submit" className="w-full btn-purple justify-center mt-4">
                    Accedi <ArrowRight className="w-5 h-5" />
                  </button>
                </form>

                <p className="mt-8 text-center text-gray-500 font-medium">
                  Non hai un account? <button onClick={() => setMode("signup")} className="text-purple-pure font-black hover:underline">Unisciti ora</button>
                </p>
              </motion.div>
            )}

            {mode === "signup" && (
              <motion.div
                key="signup"
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: -20 }}
              >
                <div className="mb-10">
                  <h3 className="text-3xl font-black text-ink mb-2 uppercase tracking-tight">Crea il tuo Account</h3>
                  <p className="text-gray-500 font-medium">Inizia a influenzare la classifica live oggi stesso.</p>
                </div>

                <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
                  <div className="space-y-2">
                    <label className="text-[10px] font-black uppercase tracking-widest text-gray-400 ml-4">Nome Completo</label>
                    <div className="relative">
                      <User className="absolute left-5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input type="text" placeholder="John Doe" className="w-full bg-grey border-2 border-transparent focus:border-purple/20 focus:bg-white rounded-2xl py-4 pl-14 pr-6 outline-none transition-all font-medium text-ink" />
                    </div>
                  </div>
                  <div className="space-y-2">
                    <label className="text-[10px] font-black uppercase tracking-widest text-gray-400 ml-4">Email Professionale</label>
                    <div className="relative">
                      <Mail className="absolute left-5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input type="email" placeholder="nome@azienda.com" className="w-full bg-grey border-2 border-transparent focus:border-purple/20 focus:bg-white rounded-2xl py-4 pl-14 pr-6 outline-none transition-all font-medium text-ink" />
                    </div>
                  </div>
                  <div className="space-y-2">
                    <label className="text-[10px] font-black uppercase tracking-widest text-gray-400 ml-4">Password</label>
                    <div className="relative">
                      <Lock className="absolute left-5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input type="password" placeholder="Minimo 8 caratteri" className="w-full bg-grey border-2 border-transparent focus:border-purple/20 focus:bg-white rounded-2xl py-4 pl-14 pr-6 outline-none transition-all font-medium text-ink" />
                    </div>
                  </div>
                  
                  <div className="flex items-start gap-3 p-4 bg-purple/5 rounded-2xl border border-purple/10">
                    <ShieldCheck className="w-5 h-5 text-purple-pure shrink-0 mt-0.5" />
                    <p className="text-[10px] text-gray-500 leading-relaxed">
                      Creando un account, accetti i nostri <strong>Termini di Servizio</strong> e la <strong>Privacy Policy</strong> dell'Impero Digitale.
                    </p>
                  </div>

                  <button type="submit" className="w-full btn-purple justify-center mt-4">
                    Crea Account <ArrowRight className="w-5 h-5" />
                  </button>
                </form>

                <p className="mt-8 text-center text-gray-500 font-medium">
                  Hai già un account? <button onClick={() => setMode("login")} className="text-purple-pure font-black hover:underline">Accedi</button>
                </p>
              </motion.div>
            )}

            {mode === "recovery" && (
              <motion.div
                key="recovery"
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.95 }}
              >
                <button 
                  onClick={() => setMode("login")}
                  className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-gray-400 mb-6 hover:text-ink transition-colors"
                >
                  <ChevronLeft className="w-4 h-4" /> Torna al Login
                </button>

                <div className="mb-10">
                  <h3 className="text-3xl font-black text-ink mb-2 uppercase tracking-tight">Recupero Password</h3>
                  <p className="text-gray-500 font-medium">Inserisci la tua email e ti invieremo un link per resettare la tua password.</p>
                </div>

                <form className="space-y-6" onSubmit={(e) => e.preventDefault()}>
                  <div className="space-y-2">
                    <label className="text-[10px] font-black uppercase tracking-widest text-gray-400 ml-4">Email Account</label>
                    <div className="relative">
                      <Mail className="absolute left-5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                      <input type="email" placeholder="nome@esempio.com" className="w-full bg-grey border-2 border-transparent focus:border-purple/20 focus:bg-white rounded-2xl py-4 pl-14 pr-6 outline-none transition-all font-medium text-ink" />
                    </div>
                  </div>
                  
                  <button type="submit" className="w-full btn-purple justify-center">
                    Invia Link di Recupero <ArrowRight className="w-5 h-5" />
                  </button>
                </form>

                <div className="mt-12 p-6 rounded-[24px] bg-grey border border-white flex flex-col items-center text-center">
                  <div className="w-12 h-12 rounded-full bg-white flex items-center justify-center mb-4 shadow-sm">
                    <ShieldCheck className="w-6 h-6 text-purple-pure" />
                  </div>
                  <h5 className="font-bold text-ink mb-1">Sicurezza Garantita</h5>
                  <p className="text-xs text-gray-500">I tuoi dati sono protetti da crittografia a 256-bit.</p>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </motion.div>
    </div>
  );
}
