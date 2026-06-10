"use client";

import { useActionState } from "react";
import { useFormStatus } from "react-dom";
import { signUp, type AuthState } from "../actions";

export default function SignupForm({ redirectTo }: { redirectTo?: string }) {
  const [state, formAction] = useActionState<AuthState, FormData>(signUp, null);

  if (state?.message) {
    return (
      <div
        className="rounded-2xl px-6 py-7 text-sm text-center"
        style={{
          background:
            "linear-gradient(180deg, rgba(255,255,255,0.7) 0%, rgba(255,220,200,0.45) 100%)",
          border: "1px solid rgba(251,70,4,0.45)",
          boxShadow:
            "inset 0 1px 0 rgba(255,255,255,0.9), 0 12px 32px -18px rgba(0,0,0,0.25)",
        }}
      >
        <div className="text-3xl mb-3">📬</div>
        <div
          className="text-lg font-extrabold tracking-tight mb-1.5"
          style={{ color: "#13111a", letterSpacing: "-0.015em" }}
        >
          Controlla la tua email
        </div>
        <p className="leading-relaxed" style={{ color: "rgba(19,17,26,0.75)" }}>
          {state.message}
        </p>
      </div>
    );
  }

  return (
    <form action={formAction} className="space-y-4">
      <input type="hidden" name="redirect" value={redirectTo ?? "/dashboard"} />

      <Field
        label="Nome"
        name="name"
        type="text"
        autoComplete="name"
        placeholder="Come vuoi essere chiamato"
      />
      <Field
        label="Email"
        name="email"
        type="email"
        autoComplete="email"
        required
        placeholder="tu@esempio.it"
      />
      <Field
        label="Password"
        name="password"
        type="password"
        autoComplete="new-password"
        required
        hint="Almeno 8 caratteri"
        placeholder="••••••••"
      />

      {state?.error && (
        <div
          className="rounded-xl px-4 py-3 text-sm font-medium"
          style={{
            background:
              "linear-gradient(180deg, rgba(239,68,68,0.14) 0%, rgba(239,68,68,0.05) 100%)",
            border: "1px solid rgba(200,30,30,0.45)",
            color: "#8a1515",
            boxShadow: "inset 0 1px 0 rgba(255,255,255,0.35)",
          }}
        >
          {state.error}
        </div>
      )}

      <SubmitButton>Crea account</SubmitButton>

      <p
        className="text-xs text-center mt-4 font-medium"
        style={{ color: "rgba(19,17,26,0.55)" }}
      >
        Registrandoti accetti i{" "}
        <span style={{ color: "rgba(19,17,26,0.75)" }}>Termini</span> e la{" "}
        <span style={{ color: "rgba(19,17,26,0.75)" }}>Privacy Policy</span>.
      </p>
    </form>
  );
}

function Field({
  label,
  name,
  type,
  autoComplete,
  required,
  placeholder,
  hint,
}: {
  label: string;
  name: string;
  type: string;
  autoComplete?: string;
  required?: boolean;
  placeholder?: string;
  hint?: string;
}) {
  return (
    <label className="block">
      <span className="field-silver-label">{label}</span>
      <input
        name={name}
        type={type}
        autoComplete={autoComplete}
        required={required}
        placeholder={placeholder}
        className="field-silver"
      />
      {hint && <span className="field-silver-hint">{hint}</span>}
    </label>
  );
}

function SubmitButton({ children }: { children: React.ReactNode }) {
  const { pending } = useFormStatus();
  return (
    <button
      type="submit"
      disabled={pending}
      className="btn-orange btn-orange--lg w-full justify-center disabled:opacity-60 disabled:cursor-not-allowed"
    >
      {pending ? "Attendere..." : children}
    </button>
  );
}
