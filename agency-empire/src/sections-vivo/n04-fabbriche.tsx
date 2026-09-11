import { ArrowRight } from "lucide-react";
import { Aura } from "@/components/vivo/aura";

/* N4 — Le due fabbriche (tavola 4). Cucitura fotografica: una sola --foto attraversa .cuc-a e .cuc-b.
   L'oggetto-icona (la dashboard) si posa sul bordo e torna in filigrana in N18.
   Copy: COPY-V2 §N4. Pattern: cucitura-fotografica + oggetto-che-si-posa. */
const BASE = process.env.NEXT_PUBLIC_AURA_BASE ?? "/aura/";

export function Dashboard({ className }: { className?: string }) {
  return (
    <div className={`dash ${className ?? ""}`} aria-label="Dashboard Outreach Factory, oggi">
      <div className="h"><span>outreach · oggi</span><b>● ALL SYSTEMS ONLINE</b></div>
      <div className="rows">
        <div><span>07:41</span><span>Autocentro Rossi · WhatsApp</span><span>inviato</span></div>
        <div><span>07:41</span><span>Garage Bianchi · IG DM</span><span>inviato</span></div>
        <div><span>07:42</span><span>Novacar · follow-up ×2</span><span>risposto</span></div>
      </div>
      <div className="bar"><i style={{ width: "73%" }} /></div>
      <div className="mt-2">312 / 430 · 3 risposte in coda</div>
    </div>
  );
}

export function Fabbriche() {
  return (
    <section
      id="fabbriche"
      className="cuc"
      style={{ ["--foto" as string]: `url(${BASE}n4-outreach.webp)` }}
      aria-labelledby="fabbriche-h2"
    >
      <div className="cuc-a">
        <div className="container-default pt-16 pb-10 md:pt-20 md:pb-14">
          <p className="sv-eyebrow">Facciamo due cose. Per scelta.</p>
          <h2 id="fabbriche-h2" className="sv-h2 mt-3 max-w-[16ch]">
            Alle 7:40 ha già mandato <span style={{ color: "var(--sv-orange)" }}>300 messaggi.</span>
          </h2>
          <p className="sv-lead sv-muted mt-5 max-w-[50ch]">
            <b className="text-white">Outreach Factory.</b> Sessioni browser reali, proxy residenziali, velocità di
            digitazione umana. Trova i contatti giusti, scrive un messaggio diverso per ognuno, fa tre follow-up,
            e ti mette in Areus, su Slack o nel tuo CRM solo chi ha risposto. Tu leggi le risposte. Non scrivi le domande.
          </p>
          <p className="sv-mono mt-5" style={{ color: "var(--sv-silver-dim)" }}>
            Email · DM Instagram · WhatsApp · follow-up ×3 · lead qualificati nel CRM · dashboard live
          </p>
        </div>
      </div>

      <div className="cuc-b">
        <div className="container-default relative min-h-[420px] pt-20 pb-24 md:pb-28">
          <p className="riga riga--libera">
            Tu stai facendo colazione.
          </p>
          <Dashboard className="mt-8 md:absolute md:right-6 md:bottom-[-18px] md:w-[min(420px,46%)]" />
        </div>
      </div>

      {/* Content Factory — seconda foto, sezione piatta (mai due foto di fila senza testo: qui il testo sta in mezzo) */}
      <div className="sv sv-ink-piatto">
        <div className="container-default grid md:grid-cols-[1fr_320px] gap-10 items-center py-16 md:py-20">
          <div>
            <h3 className="sv-h2 max-w-[16ch]">
              Un argomento entra.{" "}
              <span className="sv-it" style={{ color: "var(--sv-silver)" }}>Carosello, reel, caption escono.</span>
            </h3>
            <p className="sv-lead sv-muted mt-5 max-w-[52ch]">
              <b className="text-white">Content Factory.</b> Scrivi un argomento. Il sistema scrive il copy di ogni
              slide col metodo APSOC, apre un browser vero e monta le grafiche, scrive lo script del reel e la
              caption con gli hashtag, e carica tutto su Drive diviso per data. Pubblichi ogni giorno anche nelle
              settimane in cui non pubblicheresti.
            </p>
            <p className="sv-mono mt-5" style={{ color: "var(--sv-silver-dim)" }}>
              Caroselli con copy CRO su ogni slide · script reel 30-60&quot; · caption + hashtag · grafiche via browser · Drive ordinato
            </p>
            <a href="/prenota" className="btn-gold mt-8" data-cta="fabbriche">
              Vediamo la tua, in chiamata <ArrowRight className="h-4 w-4" />
            </a>
          </div>
          <Aura
            file="n4-content.webp"
            alt="Uomo con occhiali al lavoro, braccia conserte, luce fredda"
            riga="Senza toccare niente."
            className="aspect-[3/4] rounded-[4px]"
            objectPosition="50% 15%"
          />
        </div>
      </div>
    </section>
  );
}
