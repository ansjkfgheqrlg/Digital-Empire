"use client";
import Reveal from "../reveal";

const pillars = [
  {
    num: "01",
    title: "Sistemi, non lezioni",
    desc: "Non vendiamo informazione. Vendiamo framework operativi già pronti — <strong>I.C.R.O., S.K.I.L.L., W.O.R.K., D.A.N.</strong> — che puoi applicare il giorno stesso del primo modulo. Zero intrattenimento. Solo esecuzione.",
  },
  {
    num: "02",
    title: "Costruito dal mercato",
    desc: "Ogni metodologia è stata raffinata lavorando sui <strong>clienti reali</strong>, non in aula. Se un framework non ha prodotto risultati misurabili fuori dal corso, non entra nei moduli. Chirurgia, non marketing.",
  },
  {
    num: "03",
    title: "Qualità ossessiva",
    desc: "Video registrati in <strong>studio professionale</strong>, descrizioni lunghe come veri articoli, risorse scaricabili per ogni lezione, skill pronte da copiare e incollare. Nessuna scorciatoia nella produzione.",
  },
  {
    num: "04",
    title: "Aggiornamenti continui",
    desc: "L'AI evolve ogni 2 mesi. I corsi anche. Chi compra oggi ha accesso agli <strong>update futuri a vita</strong> — senza sovrapprezzi, senza \"nuova edizione\", senza rimettere mano al portafoglio.",
  },
];

export default function LandingMethod() {
  return (
    <section id="metodo" className="section section-border-t bg-ink relative">
      <div className="container-wide">
        <Reveal>
          <div className="grid md:grid-cols-2 gap-10 md:gap-16 mb-14 items-end">
            <div>
              <span className="bubble-ink mb-5 inline-flex">Il metodo Empire</span>
              <h2 className="text-3xl md:text-5xl font-extrabold tracking-tight leading-[1.06]">
                <span className="text-silver-white">Perché questa piattaforma</span>
                <br />
                <span className="text-silver-orange">è diversa dal resto.</span>
              </h2>
            </div>
            <p className="text-base md:text-lg leading-[1.65]" style={{ color: "rgba(249,249,249,0.72)" }}>
              La maggior parte dei corsi online esiste <strong className="text-orange-pure">per vendere corsi</strong>.
              Noi costruiamo formazione che serve <span className="text-silver-orange font-semibold">per produrre risultati</span>.
              La differenza è tutto — e si vede, lezione dopo lezione, nei dettagli che normalmente nessuno cura.
            </p>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-2 gap-5">
          {pillars.map((p, i) => (
            <Reveal key={p.num} delay={i * 0.07}>
              <div className="relative card-dark overflow-hidden h-full">
                <div className="absolute top-5 right-5 text-6xl md:text-7xl font-extrabold opacity-[0.09] leading-none" style={{ color: "#fb4604" }}>
                  {p.num}
                </div>
                <div className="relative">
                  <div className="text-xs font-semibold tracking-widest uppercase mb-3" style={{ color: "#ff8a4a" }}>
                    {p.num} · Pilastro
                  </div>
                  <h3 className="text-xl md:text-2xl font-bold tracking-tight mb-3" style={{ color: "#f9f9f9" }}>
                    {p.title}
                  </h3>
                  <p
                    className="text-[0.95rem] leading-[1.65]"
                    style={{ color: "rgba(249,249,249,0.72)" }}
                    dangerouslySetInnerHTML={{ __html: p.desc }}
                  />
                </div>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
