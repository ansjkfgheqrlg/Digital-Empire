import { Activity, MapPin, Mail, Phone, Linkedin, Instagram, Github } from "lucide-react";

export function Footer() {
  return (
    <footer
      aria-label="Footer"
      className="bg-ink-2 relative z-[3] border-t border-white/8"
    >
      <div className="container-wide py-10 md:py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 md:gap-12">
          {/* BRAND */}
          <div className="col-span-1 md:col-span-2 lg:col-span-1">
            <div className="flex items-center gap-2.5 mb-4">
              <span
                className="grid place-items-center rounded-lg w-10 h-10 text-[#0a0a0a] font-display font-bold text-base tracking-[0.08em]"
                style={{
                  background:
                    "linear-gradient(180deg, #1a4090 0%, #062155 100%)",
                  boxShadow:
                    "0 0 20px rgba(6,33,85,0.40), inset 0 1px 0 rgba(237,238,190,0.30)",
                }}
              >
                DE
              </span>
              <div className="flex flex-col leading-none">
                <span className="font-display tracking-[0.18em] text-[0.85rem] font-bold text-silver-white">
                  DIGITAL EMPIRE
                </span>
                <span className="text-[0.65rem] tracking-[0.20em] text-white/40 mt-0.5 uppercase">
                  AI Workflow Agency
                </span>
              </div>
            </div>
            <p className="text-[0.92rem] leading-relaxed text-white/55 max-w-xs">
              Implementiamo AI Workflow per imprenditori e agenzie. Outreach, content e operatività — automatizzati al 100%.
            </p>
          </div>

          {/* SERVIZI */}
          <div>
            <h6 className="text-[0.7rem] uppercase tracking-[0.28em] font-semibold text-gold-pure mb-5">
              Servizi
            </h6>
            <ul className="flex flex-col gap-2.5 text-[0.92rem] text-white/65">
              <li><a className="hover:text-white transition-colors" href="#servizi">Outreach Workflow</a></li>
              <li><a className="hover:text-white transition-colors" href="#servizi">Content Workflow</a></li>
              <li><a className="hover:text-white transition-colors" href="#servizi">Landing Page Premium</a></li>
              <li><a className="hover:text-white transition-colors" href="#metodo">Metodo FLOW</a></li>
            </ul>
          </div>

          {/* CONTATTI */}
          <div>
            <h6 className="text-[0.7rem] uppercase tracking-[0.28em] font-semibold text-gold-pure mb-5">
              Contatti
            </h6>
            <ul className="flex flex-col gap-3 text-[0.92rem] text-white/65">
              <li className="flex items-start gap-2.5">
                <Mail className="h-4 w-4 mt-0.5 shrink-0 text-white/40" />
                <a
                  href="mailto:hq@digitalempire.team"
                  className="hover:text-white transition-colors"
                >
                  hq@digitalempire.team
                </a>
              </li>
              <li className="flex items-start gap-2.5">
                <MapPin className="h-4 w-4 mt-0.5 shrink-0 text-white/40" />
                
              </li>
              <li className="flex items-start gap-2.5">
                <Phone className="h-4 w-4 mt-0.5 shrink-0 text-white/40" />
                <span>+39 02 369 369</span>
              </li>
            </ul>
          </div>

          {/* TECH-CHARM */}
          <div>
            <h6 className="text-[0.7rem] uppercase tracking-[0.28em] font-semibold text-gold-pure mb-5">
              HQ Status
            </h6>
            <ul className="flex flex-col gap-2.5 font-mono text-[0.78rem] text-white/45">
              <li className="flex items-center gap-2">
                <Activity className="h-3.5 w-3.5 text-emerald-400 animate-pulse" />
                <span>System Load: <span className="text-emerald-400">Optimal</span></span>
              </li>
              <li>Uptime 2026: <span className="text-white/65">99.98%</span></li>
              <li>Node: <span className="text-gold-pure">EMPIRE_01</span></li>
            </ul>
            <div className="flex items-center gap-2 mt-5">
              <a aria-label="LinkedIn" href="#" className="grid place-items-center w-9 h-9 rounded-lg border border-white/12 bg-white/4 text-white/55 hover:text-white hover:border-gold-pure/50 transition-colors">
                <Linkedin className="h-4 w-4" />
              </a>
              <a aria-label="Instagram" href="#" className="grid place-items-center w-9 h-9 rounded-lg border border-white/12 bg-white/4 text-white/55 hover:text-white hover:border-gold-pure/50 transition-colors">
                <Instagram className="h-4 w-4" />
              </a>
              <a aria-label="Github" href="#" className="grid place-items-center w-9 h-9 rounded-lg border border-white/12 bg-white/4 text-white/55 hover:text-white hover:border-gold-pure/50 transition-colors">
                <Github className="h-4 w-4" />
              </a>
            </div>
          </div>
        </div>

        {/* BOTTOM STRIP */}
        <div className="mt-8 pt-6 md:mt-12 md:pt-8 border-t border-white/6 flex flex-col md:flex-row gap-3 justify-between items-center text-[0.78rem] text-white/35">
          <div>
            © 2026 Digital Empire S.r.l. · Tutti i diritti riservati.
          </div>
          <div className="font-mono uppercase tracking-[0.2em] text-[0.7rem]">
            Codificato per il dominio assoluto.
          </div>
        </div>
      </div>
    </footer>
  );
}
