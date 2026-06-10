"use client";

import { Reveal } from "@/components/reveal";
import { CallCTA } from "@/components/call-cta";
import { ArrowRight, Crown, Compass, Flame } from "lucide-react";

export function AboutStory() {
  return (
    <>
      <section className="bg-paper section section-border-t relative overflow-hidden">
        <div className="max-w-5xl mx-auto px-6 text-center relative">
          <Reveal>
            <span className="bubble-orange mb-8">Capitolo II · Dietro le quinte</span>
          </Reveal>

          <Reveal delay={0.1}>
            <p className="text-ink/65 text-[11px] uppercase tracking-[0.28em] font-black mb-6">
              → Adesso che hai visto cosa installiamo, ti racconto da dove veniamo
            </p>
          </Reveal>

          <Reveal delay={0.2}>
            <h2
              className="text-[40px] md:text-[68px] font-black leading-[1.02] tracking-tight mb-10"
              style={{ letterSpacing: "-0.025em" }}
            >
              <span className="text-silver-black">Noi siamo </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                }}
              >
                Digital Empire.
              </span>
            </h2>
          </Reveal>

          <Reveal delay={0.3}>
            <p className="text-ink/75 text-[18px] md:text-[20px] leading-relaxed max-w-3xl mx-auto font-medium">
              Un&apos;agenzia nata a <strong className="text-ink">Gennaio 2026</strong>. Un team di tre persone che ha
              deciso di smettere di osservare la rivoluzione AI{" "}
              <em
                className="text-orange-pure"
                style={{ fontFamily: "var(--font-serif), Georgia, serif" }}
              >
                e di costruirla.
              </em>
            </p>
          </Reveal>

          <Reveal delay={0.4}>
            <div className="mt-12 flex flex-wrap justify-center gap-3">
              {["Trasparenti", "Operativi", "Senza fuffa", "Senza intermediari"].map((t, i) => (
                <span
                  key={i}
                  className="px-4 py-2 rounded-full text-[11px] uppercase tracking-[0.22em] font-black text-ink/70"
                  style={{
                    background: "rgba(28,28,28,0.05)",
                    border: "1px solid rgba(28,28,28,0.12)",
                  }}
                >
                  {t}
                </span>
              ))}
            </div>
          </Reveal>
        </div>
      </section>

      <section className="bg-ink section section-border-t relative overflow-hidden">
        <div
          aria-hidden="true"
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              "radial-gradient(circle at 15% 20%, rgba(251,70,4,0.10) 0%, transparent 50%)",
          }}
        />

        <div className="max-w-3xl mx-auto px-6 relative">
          <Reveal>
            <span className="bubble-orange mb-8">La storia · in prima persona</span>
          </Reveal>

          <Reveal delay={0.1}>
            <h2
              className="text-[36px] md:text-[56px] font-black leading-[1.05] tracking-tight mt-6 mb-12"
              style={{ letterSpacing: "-0.025em" }}
            >
              <span className="text-silver-white">Sei anni fa ero un ragazzo </span>
              <span
                className="text-silver-orange"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                }}
              >
                ossessionato da Internet.
              </span>
            </h2>
          </Reveal>

          <div className="space-y-7 text-white/80 text-[17px] leading-[1.7] font-medium">
            <Reveal delay={0.2}>
              <p>
                Tutto è iniziato con <strong className="text-silver-white">YouTube</strong>. Poi, come capita a chi entra
                in questo mondo da curioso, ho attraversato la mia fase di tutto-provare:
                marketing, libretti su Amazon, dropshipping, infoprodotti.{" "}
                <span className="text-silver-orange">Ho provato tutto.</span> Non per dispersione — per affamato bisogno
                di capire come funzionano davvero le cose.
              </p>
            </Reveal>

            <Reveal delay={0.25}>
              <p>
                Poi ho incontrato il <strong className="text-silver-white">copywriting</strong>. E lì qualcosa si è
                bloccato. Ho capito che ogni parola di una pagina, ogni frase di uno script, ogni riga di una mail{" "}
                <em>non è scrittura</em> — è{" "}
                <span className="text-silver-orange font-semibold">architettura della decisione</span>. Vendere con le
                parole. Spostare scelte. Cambiare il comportamento di un essere umano usando solo testo.
              </p>
            </Reveal>

            <Reveal delay={0.3}>
              <p>
                Da quel momento ho fatto una cosa che pochi fanno: ho preso l&apos;intelligenza artificiale e l&apos;ho
                messa{" "}
                <em
                  className="text-silver-white"
                  style={{ fontFamily: "var(--font-serif), Georgia, serif" }}
                >
                  dentro ogni singolo passo del mio lavoro.
                </em>{" "}
                Non per &ldquo;velocizzare i task&rdquo;. Per moltiplicare la mia capacità di pensare, ricercare,
                produrre. Pianificazione, analisi di mercato, scrittura, esecuzione — tutto orchestrato.
              </p>
            </Reveal>

            <Reveal delay={0.35}>
              <div
                className="relative my-10 p-7 rounded-2xl overflow-hidden"
                style={{
                  background:
                    "linear-gradient(160deg, #2c2a27 0%, #1c1a17 50%, #0d0c0b 100%)",
                  border: "1px solid rgba(251,70,4,0.4)",
                  boxShadow:
                    "inset 0 1px 0 rgba(255,255,255,0.08), 0 15px 40px -10px rgba(251,70,4,0.25)",
                }}
              >
                <p className="text-[18px] md:text-[20px] leading-relaxed text-white">
                  Il principio l&apos;ho capito presto:{" "}
                  <strong className="text-orange-pure">
                    usare l&apos;intelligenza artificiale per costruire sistemi AI che lavorano al posto tuo.
                  </strong>{" "}
                  Non una chat. Un sistema. Non un aiuto. Un&apos;infrastruttura.
                </p>
              </div>
            </Reveal>

            <Reveal delay={0.4}>
              <p>
                Mentre l&apos;AI correva, io le sono rimasto attaccato.{" "}
                <strong className="text-silver-white">Ogni release. Ogni modello. Ogni feature.</strong> Da chat
                personalizzate sono passato agli agenti. Dagli agenti ai workflow multi-step. Dai workflow ai{" "}
                <span className="text-silver-orange">System AI completi</span> che oggi fanno outreach, scrivono copy,
                gestiscono knowledge base — al posto dei nostri clienti.
              </p>
            </Reveal>

            <Reveal delay={0.45}>
              <p className="text-silver-orange font-semibold text-[18px]">
                Non c&apos;è competenza più strategica oggi. Punto. Saperlo fare bene non è un &ldquo;plus&rdquo; — è la
                differenza tra chi guida il prossimo decennio e chi lo subisce.
              </p>
            </Reveal>
          </div>
        </div>
      </section>

      <section className="bg-grey section section-border-t relative overflow-hidden">
        <div className="max-w-4xl mx-auto px-6 text-center relative">
          <Reveal>
            <span className="bubble-orange mb-8">Gennaio 2026 · La svolta</span>
          </Reveal>

          <Reveal delay={0.1}>
            <h2
              className="text-[36px] md:text-[58px] font-black leading-[1.05] tracking-tight mt-6 mb-10"
              style={{ letterSpacing: "-0.025em" }}
            >
              <span className="text-silver-black">Poi un giorno ho deciso </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                }}
              >
                di non lavorare più da solo.
              </span>
            </h2>
          </Reveal>

          <Reveal delay={0.2}>
            <p className="text-ink/75 text-[17px] md:text-[18px] leading-[1.7] max-w-2xl mx-auto font-medium">
              Avevo il metodo. Avevo i sistemi. Avevo i clienti che bussavano.
              Mancava una cosa sola: <strong className="text-ink">un team con cui costruire qualcosa di più
              grande di me.</strong>
            </p>
          </Reveal>

          <Reveal delay={0.3}>
            <p className="text-ink/75 text-[17px] md:text-[18px] leading-[1.7] max-w-2xl mx-auto font-medium mt-6">
              Da bambino sognavo di avere{" "}
              <em
                className="text-orange-pure"
                style={{ fontFamily: "var(--font-serif), Georgia, serif" }}
              >
                la mia agenzia.
              </em>{" "}
              Non un&apos;azienda qualunque — un posto dove le persone giuste costruiscono cose che contano. A Gennaio
              2026 quella idea ha preso un nome:{" "}
              <strong className="text-ink">
                Digital <span className="text-orange-pure">Empire</span>
              </strong>
              .
            </p>
          </Reveal>

          <Reveal delay={0.4}>
            <p className="mt-10 text-[12px] uppercase tracking-[0.26em] font-black text-ink/65">
              → Il sogno non è realizzato. Lo sto ancora realizzando, ogni giorno.
            </p>
          </Reveal>
        </div>
      </section>

      <section className="bg-ink-2 section section-border-t relative overflow-hidden">
        <div
          aria-hidden="true"
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              "radial-gradient(circle at 50% 0%, rgba(251,70,4,0.10) 0%, transparent 55%)",
          }}
        />

        <div className="max-w-6xl mx-auto px-6 relative">
          <div className="text-center mb-16">
            <Reveal>
              <span className="bubble-orange mb-6">Le persone · 3 + zero rumore</span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2
                className="text-[36px] md:text-[58px] font-black leading-[1.05] tracking-tight mt-6 max-w-3xl mx-auto"
                style={{ letterSpacing: "-0.025em" }}
              >
                <span className="text-silver-white">Tre persone. </span>
                <span
                  className="text-silver-orange"
                  style={{
                    fontFamily: "var(--font-serif), Georgia, serif",
                    fontStyle: "italic",
                    fontWeight: 400,
                  }}
                >
                  Zero filtri tra te e <span style={{ whiteSpace: "nowrap" }}>chi costruisce.</span>
                </span>
              </h2>
            </Reveal>
            <Reveal delay={0.2}>
              <p className="text-white/85 text-[16px] max-w-2xl mx-auto mt-6 leading-relaxed">
                Niente sales junior. Niente account manager. Quando lavori con noi,{" "}
                <strong className="text-silver-orange">parli con chi ha le mani sul codice e sui prompt.</strong>
              </p>
            </Reveal>
          </div>

          <div className="grid md:grid-cols-3 gap-5">
            <Reveal delay={0.25}>
              <div
                className="relative rounded-2xl p-7 h-full overflow-hidden hover-lift"
                style={{
                  background:
                    "linear-gradient(160deg, #3a2a20 0%, #2a1a10 50%, #1a0d08 100%)",
                  border: "1px solid rgba(251,70,4,0.5)",
                  boxShadow:
                    "inset 0 1px 0 rgba(255,210,180,0.18), 0 15px 50px -15px rgba(251,70,4,0.4)",
                }}
              >
                <div className="flex items-center gap-3 mb-6">
                  <div
                    className="w-12 h-12 rounded-xl flex items-center justify-center"
                    style={{
                      background:
                        "radial-gradient(circle at 30% 30%, #fb4604, #8f2a02)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.25), 0 4px 14px -2px rgba(251,70,4,0.5)",
                    }}
                  >
                    <Crown className="h-5 w-5 text-white" strokeWidth={1.8} />
                  </div>
                  <span className="text-[10px] uppercase tracking-[0.28em] font-black text-orange-pure">
                    Founder
                  </span>
                </div>
                <h3 className="text-[26px] font-black text-silver-white mb-3 leading-tight">
                  Maximilian
                </h3>
                <p className="text-white/88 text-[14.5px] leading-relaxed">
                  Sei anni di marketing. Tre di AI a tempo pieno. È la testa dietro ogni System AI che installiamo —
                  architetto dei flussi, voce del copy, ossessionato dai dettagli che gli altri non vedono.
                </p>
              </div>
            </Reveal>

            <Reveal delay={0.35}>
              <div
                className="relative rounded-2xl p-7 h-full overflow-hidden hover-lift"
                style={{
                  background:
                    "linear-gradient(160deg, #2c2a27 0%, #1c1a17 50%, #0d0c0b 100%)",
                  border: "1px solid rgba(220,220,218,0.22)",
                  boxShadow:
                    "inset 0 1px 0 rgba(240,235,225,0.12), 0 10px 40px -15px rgba(0,0,0,0.7)",
                }}
              >
                <div className="flex items-center gap-3 mb-6">
                  <div
                    className="w-12 h-12 rounded-xl flex items-center justify-center"
                    style={{
                      background:
                        "linear-gradient(160deg, #d9d6cf 0%, #8a8378 100%)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.5), 0 4px 14px -2px rgba(0,0,0,0.4)",
                    }}
                  >
                    <Compass className="h-5 w-5 text-ink" strokeWidth={2} />
                  </div>
                  <span className="text-[10px] uppercase tracking-[0.28em] font-black text-silver-orange">
                    Socio · Pari grado
                  </span>
                </div>
                <h3 className="text-[26px] font-black text-silver-white mb-3 leading-tight">
                  Gael
                </h3>
                <p className="text-white/88 text-[14.5px] leading-relaxed">
                  Il mio socio alla pari. La persona con cui mi confronto su{" "}
                  <em className="text-silver-white">ogni</em> decisione che conta. Ci siamo conosciuti sotto un cielo
                  d&apos;estate al campeggio Tahiti di Follonica — non lo scriviamo per nostalgia, ma perché certe
                  partnership nascono lontano dagli uffici.
                </p>
              </div>
            </Reveal>

            <Reveal delay={0.45}>
              <div
                className="relative rounded-2xl p-7 h-full overflow-hidden hover-lift"
                style={{
                  background:
                    "linear-gradient(160deg, #2c2a27 0%, #1c1a17 50%, #0d0c0b 100%)",
                  border: "1px solid rgba(220,220,218,0.22)",
                  boxShadow:
                    "inset 0 1px 0 rgba(240,235,225,0.12), 0 10px 40px -15px rgba(0,0,0,0.7)",
                }}
              >
                <div className="flex items-center gap-3 mb-6">
                  <div
                    className="w-12 h-12 rounded-xl flex items-center justify-center"
                    style={{
                      background:
                        "linear-gradient(160deg, #d9d6cf 0%, #8a8378 100%)",
                      boxShadow:
                        "inset 0 1px 0 rgba(255,255,255,0.5), 0 4px 14px -2px rgba(0,0,0,0.4)",
                    }}
                  >
                    <Flame className="h-5 w-5 text-ink" strokeWidth={2} />
                  </div>
                  <span className="text-[10px] uppercase tracking-[0.28em] font-black text-silver-orange">
                    Team Empire
                  </span>
                </div>
                <h3 className="text-[26px] font-black text-silver-white mb-3 leading-tight">
                  Leonardo
                </h3>
                <p className="text-white/88 text-[14.5px] leading-relaxed">
                  Una delle tre teste di Digital Empire. Energia, esecuzione, presenza costante nelle stanze dove si
                  decide cosa spediamo e come. Quando lavori con noi, anche lui è uno di quelli con cui ti troverai a
                  costruire.
                </p>
              </div>
            </Reveal>
          </div>

          <Reveal delay={0.55}>
            <p className="text-center text-white/80 text-[15px] max-w-2xl mx-auto mt-14 leading-relaxed">
              <span className="text-silver-orange">→</span> Tre persone, una visione, zero burocrazia.{" "}
              <strong className="text-silver-white">Per scelta, non per limite.</strong>
            </p>
          </Reveal>
        </div>
      </section>

      <section className="bg-paper section section-border-t relative overflow-hidden">
        <div className="max-w-5xl mx-auto px-6 relative">
          <div className="text-center mb-14">
            <Reveal>
              <span className="bubble-orange mb-6">Cosa facciamo · Oggi</span>
            </Reveal>
            <Reveal delay={0.1}>
              <h2
                className="text-[36px] md:text-[58px] font-black leading-[1.05] tracking-tight mt-6 max-w-3xl mx-auto"
                style={{ letterSpacing: "-0.025em" }}
              >
                <span className="text-silver-black">Installiamo sistemi AI che </span>
                <span
                  className="text-orange-pure"
                  style={{
                    fontFamily: "var(--font-serif), Georgia, serif",
                    fontStyle: "italic",
                    fontWeight: 400,
                  }}
                >
                  lavorano mentre dormi.
                </span>
              </h2>
            </Reveal>
          </div>

          <div className="grid md:grid-cols-3 gap-5 mb-16">
            {[
              {
                t: "Outreach Factory",
                d: "300+ email e DM Instagram personalizzati al giorno, automatici, con qualificazione AI e follow-up. Il codice è tuo.",
              },
              {
                t: "Content Factory",
                d: "Caroselli Instagram, script Reels, caption e hashtag generati su richiesta e uploadati su Drive in automatico.",
              },
              {
                t: "Second Brain",
                d: "Knowledge base aziendale AI: ogni domanda sulla tua operatività risposta in tempo reale. Zero dispersione informativa.",
              },
            ].map((s, i) => (
              <Reveal key={i} delay={0.2 + i * 0.1}>
                <div
                  className="relative rounded-2xl p-7 h-full hover-lift"
                  style={{
                    background:
                      "linear-gradient(160deg, #ffffff 0%, #f5f3ee 100%)",
                    border: "1px solid rgba(28,28,28,0.1)",
                    boxShadow:
                      "0 10px 40px -15px rgba(0,0,0,0.15)",
                  }}
                >
                  <div className="text-[10px] uppercase tracking-[0.22em] font-black text-orange-pure mb-4">
                    0{i + 1}
                  </div>
                  <h3 className="text-[18px] font-black text-ink mb-3 leading-tight">{s.t}</h3>
                  <p className="text-[14px] text-ink/82 leading-relaxed">{s.d}</p>
                </div>
              </Reveal>
            ))}
          </div>

          <Reveal delay={0.5}>
            <div
              className="relative max-w-3xl mx-auto rounded-2xl p-10 md:p-12 text-center overflow-hidden"
              style={{
                background:
                  "linear-gradient(155deg, #ebe7e0 0%, #d4cec3 50%, #a8a093 100%)",
                border: "1px solid rgba(255,255,255,0.5)",
                boxShadow:
                  "inset 0 1px 0 rgba(255,255,255,0.7), 0 20px 50px -15px rgba(0,0,0,0.3)",
              }}
            >
              <div className="text-[11px] uppercase tracking-[0.26em] font-black text-ink/70 mb-5">
                La nostra missione
              </div>
              <p
                className="text-[24px] md:text-[34px] font-black text-ink leading-[1.2]"
                style={{ letterSpacing: "-0.02em" }}
              >
                Dare valore vero.{" "}
                <em
                  className="text-orange-pure"
                  style={{
                    fontFamily: "var(--font-serif), Georgia, serif",
                    fontStyle: "italic",
                    fontWeight: 400,
                  }}
                >
                  E dominare in questo campo.
                </em>
              </p>
              <p className="mt-6 text-ink/80 text-[15px] leading-relaxed max-w-xl mx-auto">
                Non &ldquo;essere conosciuti&rdquo;. Non &ldquo;crescere&rdquo;. Dominare. Perché chi domina può
                permettersi di restare onesto, trasparente, e mettere il cliente prima del fatturato.
              </p>
            </div>
          </Reveal>
        </div>
      </section>

      <section className="bg-paper section section-border-t relative overflow-hidden">
        <div
          aria-hidden="true"
          className="pointer-events-none absolute inset-0"
          style={{
            background:
              "radial-gradient(circle at 50% 100%, rgba(251,70,4,0.10) 0%, transparent 60%)",
          }}
        />

        <div className="max-w-4xl mx-auto px-6 text-center relative">
          <Reveal>
            <span className="bubble-orange mb-8">Adesso ci conosci</span>
          </Reveal>

          <Reveal delay={0.1}>
            <h2
              className="text-[40px] md:text-[64px] font-black leading-[1.02] tracking-tight mt-6 mb-10"
              style={{ letterSpacing: "-0.025em" }}
            >
              <span className="text-silver-black">Vuoi entrare in </span>
              <span
                className="text-orange-pure"
                style={{
                  fontFamily: "var(--font-serif), Georgia, serif",
                  fontStyle: "italic",
                  fontWeight: 400,
                }}
              >
                Empire?
              </span>
            </h2>
          </Reveal>

          <Reveal delay={0.2}>
            <p className="text-ink/75 text-[17px] md:text-[19px] leading-[1.6] max-w-xl mx-auto mb-12 text-balance">
              C&apos;è una porta sola. <strong className="text-orange-pure">Prenota una chiamata strategica.</strong>
            </p>
          </Reveal>

          <Reveal delay={0.3}>
            <div className="flex flex-col sm:flex-row gap-3 items-center justify-center">
              <CallCTA variant="light" />
            </div>
          </Reveal>

          <Reveal delay={0.4}>
            <p className="mt-8 text-[12px] uppercase tracking-[0.24em] font-black text-ink/65">
              → 30 minuti · Gratuita · Nessun impegno
            </p>
          </Reveal>
        </div>
      </section>
    </>
  );
}
