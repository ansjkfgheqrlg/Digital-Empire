"use client";

import { useState, FormEvent } from "react";
import { ArrowRight, Shield } from "lucide-react";
import { CourseCTA } from "@/components/course-cta";

const API_KEY =
  "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";
const LIST_ID = 3;
const REDIRECT_URL = "https://clever-cannoli-3a583d.netlify.app/";

export function OptinForm({ id = "optin" }: { id?: string }) {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState<{ msg: string; err?: boolean }>({ msg: "" });
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    const n = nome.trim();
    const em = email.trim();
    if (!n) return setStatus({ msg: "inserisci il tuo nome.", err: true });
    if (!em || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em))
      return setStatus({ msg: "inserisci un indirizzo email valido.", err: true });

    setLoading(true);
    setStatus({ msg: "controllo in corso..." });
    try {
      const res = await fetch("https://api.brevo.com/v3/contacts", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          "api-key": API_KEY,
        },
        body: JSON.stringify({
          email: em,
          attributes: { FIRSTNAME: n },
          listIds: [LIST_ID],
          updateEnabled: true,
        }),
      });
      if (res.ok || res.status === 204) {
        window.location.href = REDIRECT_URL;
      } else {
        setStatus({ msg: "errore. riprova.", err: true });
        setLoading(false);
      }
    } catch {
      setStatus({ msg: "errore di connessione. riprova.", err: true });
      setLoading(false);
    }
  }

  return (
    <div className="optin-silver rounded-2xl p-6 md:p-8">
      <p className="text-center text-[11px] uppercase tracking-[0.18em] text-[#1c1c1c]/65 mb-5 font-semibold">
        scarica il PDF gratuito
      </p>
      <form onSubmit={onSubmit} className="flex flex-col gap-3" noValidate>
        <label htmlFor={`${id}-nome`} className="sr-only">
          Il tuo nome
        </label>
        <input
          id={`${id}-nome`}
          type="text"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
          placeholder="il tuo nome"
          autoComplete="given-name"
          required
          className="w-full rounded-lg border border-[#1c1c1c]/15 bg-white/70 px-4 py-3.5 text-[#1c1c1c] placeholder:text-[#1c1c1c]/45 focus:border-orange-pure focus:bg-white focus:outline-none focus:ring-2 focus:ring-orange-pure/25 transition shadow-[inset_0_1px_0_rgba(255,255,255,0.9),inset_0_-1px_0_rgba(138,133,148,0.18)]"
        />
        <label htmlFor={`${id}-email`} className="sr-only">
          La tua email migliore
        </label>
        <input
          id={`${id}-email`}
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="la tua email migliore"
          autoComplete="email"
          required
          className="w-full rounded-lg border border-[#1c1c1c]/15 bg-white/70 px-4 py-3.5 text-[#1c1c1c] placeholder:text-[#1c1c1c]/45 focus:border-orange-pure focus:bg-white focus:outline-none focus:ring-2 focus:ring-orange-pure/25 transition shadow-[inset_0_1px_0_rgba(255,255,255,0.9),inset_0_-1px_0_rgba(138,133,148,0.18)]"
        />
        <button
          type="submit"
          disabled={loading}
          className="btn-orange btn-orange--lg group mt-1 justify-center disabled:opacity-60"
        >
          {loading ? "invio in corso..." : "scarica il framework gratuito"}
          <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
        </button>
      </form>
      <p className="text-center text-xs text-[#1c1c1c]/60 mt-4">
        niente spam. cancellati quando vuoi.
      </p>
      <div className="mt-3">
        <CourseCTA variant="light" />
      </div>
      {status.msg && (
        <p
          role="alert"
          aria-live="polite"
          className={`text-center text-sm mt-2 ${
            status.err ? "text-red-400" : "text-orange-pure"
          }`}
        >
          {status.msg}
        </p>
      )}
      <div className="flex items-center justify-center gap-2 mt-5 text-xs text-[#1c1c1c]/60">
        <Shield className="h-3.5 w-3.5" />
        <span>i tuoi dati sono al sicuro. li usiamo solo per inviarti il PDF.</span>
      </div>
    </div>
  );
}
