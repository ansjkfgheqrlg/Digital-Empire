import { Aura } from "@/components/vivo/aura";

/* N9 — La formula (speedrun T26 + T20): aritmetica esplicita al posto dell'aggettivo (V9),
   confronto ORA / CON IL SISTEMA. I numeri stanno UNA volta (§8): in DATI, letti dal markup.
   Copy: COPY-V2 §N9. Pattern Fabbrica: formula, ora-con. */
const DATI = {
  ora: { msg: 30, ore: 2.5, carosello_ore: 3 },
  con: { msg: 300, ore: 0 },
};

export function Formula() {
  const oraRate = Math.round(DATI.ora.msg / DATI.ora.ore); // 12
  const caroselloRate = (1 / DATI.ora.carosello_ore).toFixed(1).replace(".", ","); // 0,3
  return (
    <section id="formula" className="sv sv-carta" aria-labelledby="formula-h2">
      <div className="container-default grid md:grid-cols-[1fr_300px] gap-10 md:gap-14 items-center py-16 md:py-20">
        <div>
          <p className="sv-eyebrow">La produttività non è alzarsi alle 5</p>
          <h2 id="formula-h2" className="sv-h2 mt-3 max-w-[18ch]">
            Produttività ={" "}
            <span className="sv-it" style={{ color: "var(--sv-orange)", fontWeight: 600 }}>cose utili fatte / ore tue.</span>
          </h2>

          <div className="mt-8 grid sm:grid-cols-2 gap-px" style={{ background: "var(--sv-hair-light)" }}>
            <div className="p-5" style={{ background: "var(--sv-carta)" }}>
              <div className="sv-mono flex items-center gap-2" style={{ color: "#6f6a62" }}>
                <i className="inline-block w-3 h-3 rounded-full" style={{ border: "1px solid #6f6a62" }} /> Ora
              </div>
              <ul className="mt-3 grid gap-2 sv-body sv-muted list-none p-0 m-0">
                <li>{DATI.ora.msg} messaggi in {String(DATI.ora.ore).replace(".", ",")} ore = <b style={{ color: "#1c1c1c" }}>{oraRate} l&apos;ora</b></li>
                <li>un carosello in {DATI.ora.carosello_ore} ore = <b style={{ color: "#1c1c1c" }}>{caroselloRate} l&apos;ora</b></li>
                <li>follow-up: quelli che ti ricordi</li>
              </ul>
              <div className="mt-4 h-[6px] rounded-[3px]" style={{ background: "rgba(28,28,28,.12)" }}>
                <i className="block h-full rounded-[3px]" style={{ width: `${(DATI.ora.msg / DATI.con.msg) * 100}%`, background: "#6f6a62" }} />
              </div>
            </div>
            <div className="p-5" style={{ background: "var(--sv-carta)" }}>
              <div className="sv-mono flex items-center gap-2" style={{ color: "var(--sv-orange)" }}>
                <i className="inline-block w-3 h-3 rounded-full" style={{ background: "var(--sv-orange)" }} /> Con il sistema
              </div>
              <ul className="mt-3 grid gap-2 sv-body list-none p-0 m-0" style={{ color: "#1c1c1c" }}>
                <li><b>{DATI.con.msg} messaggi</b> in {DATI.con.ore} ore tue</li>
                <li><b>un carosello, un reel e una caption</b> al giorno in 0 ore tue</li>
                <li>follow-up: <b>tutti, tre volte</b></li>
              </ul>
              <div className="mt-4 h-[6px] rounded-[3px]" style={{ background: "rgba(28,28,28,.12)" }}>
                <i className="block h-full rounded-[3px]" style={{ width: "100%", background: "var(--sv-orange)" }} />
              </div>
            </div>
          </div>

          <p className="sv-mono mt-5 px-4 py-3 rounded-[4px]" style={{ background: "#1c1c1c", color: "#fff", letterSpacing: ".06em", textTransform: "none" }}>
            {DATI.con.msg} / {DATI.con.ore} non si può dividere. È il punto: le ore tue non sono più al denominatore.
          </p>
          <p className="sv-body sv-muted mt-5 max-w-[60ch]">
            E il metodo con cui scrive — APSOC: Attenzione, Problema, Promessa, Social proof, Obiezioni, CTA — è lo
            stesso che usiamo per le nostre pagine. Questa compresa.
          </p>
          <p className="sv-small mt-3" style={{ color: "#6f6a62" }}>I tool si pagano. I sistemi si possiedono.</p>
        </div>
        <Aura
          file="n9-formula.webp"
          alt="Uomo che conta banconote dentro un'asciugatrice"
          riga="Dodici canoni all'anno per un tool che non sa chi sei."
          tratt="carta"
          className="aspect-[3/4] rounded-[4px]"
        />
      </div>
    </section>
  );
}
