"use client";

import { useActionState } from "react";
import { useFormStatus } from "react-dom";
import { signIn, type AuthState } from "../actions";

export default function LoginForm({ redirectTo }: { redirectTo?: string }) {
  const [state, formAction] = useActionState<AuthState, FormData>(signIn, null);

  return (
    <form action={formAction} className="space-y-4">
      <input type="hidden" name="redirect" value={redirectTo ?? "/dashboard"} />

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
        autoComplete="current-password"
        required
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

      <SubmitButton>Accedi</SubmitButton>
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
}: {
  label: string;
  name: string;
  type: string;
  autoComplete?: string;
  required?: boolean;
  placeholder?: string;
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
