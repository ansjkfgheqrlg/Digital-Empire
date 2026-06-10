"use client";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import Reveal from "../reveal";

const faqs = [
  {
    q: "Come ricevo l'accesso dopo l'acquisto?",
    a: "Subito dopo il pagamento su Stripe ricevi un'email automatica con username, password e link diretto alla piattaforma. L'accesso è immediato, nessun tempo di attesa.",
  },
  {
    q: "Per quanto tempo ho accesso ai corsi?",
    a: "Per sempre. Chi compra un corso ha accesso a vita alla piattaforma, inclusi tutti gli aggiornamenti futuri di quel corso. Nessun rinnovo, nessuna subscription nascosta.",
  },
  {
    q: "Posso seguire il corso dal telefono?",
    a: "Sì, la piattaforma è completamente responsive. Video, descrizioni e risorse sono ottimizzate per mobile. L'esperienza è premium su ogni dispositivo.",
  },
  {
    q: "Cosa succede se dimentico la password?",
    a: "Dalla pagina di login clicchi su 'Password dimenticata', inserisci l'email e ricevi un link per impostarne una nuova. Il processo richiede meno di 2 minuti.",
  },
  {
    q: "C'è una community?",
    a: "Sì, c'è una community riservata su Telegram dove studenti, Max e il team rispondono ai dubbi. L'invito viene inviato via email dopo l'acquisto del primo corso.",
  },
  {
    q: "Posso chiedere un rimborso?",
    a: "Entro 14 giorni dall'acquisto, se il corso non fa per te, rimborso totale senza domande. L'obiettivo è che tu sia in classe solo se il corso ti sta davvero servendo.",
  },
];

export default function LandingFaq() {
  const [open, setOpen] = useState<number | null>(0);

  return (
    <section id="faq" className="section section-border-t bg-ink relative">
      <div className="container-narrow">
        <Reveal>
          <div className="text-center mb-12">
            <span className="bubble-ink mb-5 inline-flex">Domande frequenti</span>
            <h2 className="text-3xl md:text-5xl font-extrabold tracking-tight leading-[1.06]">
              <span className="text-silver-white">Le risposte che </span>
              <span className="text-silver-orange">contano davvero</span>
              <span className="text-silver-white">.</span>
            </h2>
          </div>
        </Reveal>

        <div className="flex flex-col gap-3">
          {faqs.map((faq, i) => (
            <Reveal key={i} delay={i * 0.04}>
              <button
                onClick={() => setOpen(open === i ? null : i)}
                className="w-full text-left card-dark !p-0 overflow-hidden hover:!translate-y-0"
                style={{ transition: "border-color 0.3s" }}
              >
                <div className="flex items-center justify-between px-7 py-6">
                  <h3 className="text-base md:text-lg font-semibold pr-6" style={{ color: "#f9f9f9" }}>
                    {faq.q}
                  </h3>
                  <motion.div
                    animate={{ rotate: open === i ? 45 : 0 }}
                    transition={{ duration: 0.3 }}
                    className="flex-shrink-0 w-9 h-9 rounded-full flex items-center justify-center"
                    style={{ background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)", color: "#ffffff", boxShadow: "0 4px 14px -4px rgba(251,70,4,0.5)" }}
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                      <line x1="12" y1="5" x2="12" y2="19" />
                      <line x1="5" y1="12" x2="19" y2="12" />
                    </svg>
                  </motion.div>
                </div>
                <AnimatePresence initial={false}>
                  {open === i && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: "auto", opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
                      className="overflow-hidden"
                    >
                      <div className="px-7 pb-7 pt-0 text-sm md:text-base leading-relaxed" style={{ color: "rgba(249,249,249,0.72)" }}>
                        {faq.a}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </button>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
