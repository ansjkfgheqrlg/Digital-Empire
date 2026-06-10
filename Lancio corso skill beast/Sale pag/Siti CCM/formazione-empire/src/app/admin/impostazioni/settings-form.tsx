"use client";

import { useActionState } from "react";
import { saveSettings } from "@/app/admin/actions";

function Label({ children }: { children: React.ReactNode }) {
  return (
    <label className="block text-xs font-semibold uppercase tracking-widest mb-2" style={{ color: "rgba(249,249,249,0.55)" }}>
      {children}
    </label>
  );
}

function Field({ label, name, defaultValue, type = "text", readOnly }: { label: string; name: string; defaultValue?: string; type?: string; readOnly?: boolean }) {
  return (
    <div>
      <Label>{label}</Label>
      <input
        name={name}
        type={type}
        defaultValue={defaultValue ?? ""}
        readOnly={readOnly}
        className="input-field"
        style={readOnly ? { background: "rgba(249,249,249,0.03)", fontFamily: "monospace", fontSize: "0.85rem" } : undefined}
      />
    </div>
  );
}

export default function SettingsForm({ settings }: { settings: any }) {
  const [state, formAction, isPending] = useActionState(saveSettings, null);

  return (
    <form action={formAction} className="flex flex-col gap-6 max-w-2xl">
      <section className="card-dark">
        <h2 className="text-lg font-bold mb-5" style={{ color: "#f9f9f9" }}>Branding</h2>
        <div className="flex flex-col gap-4">
          <Field label="Nome piattaforma" name="platformName" defaultValue={settings?.platform_name ?? "Formazione Empire"} />
          <Field label="Email di supporto" name="supportEmail" defaultValue={settings?.support_email ?? ""} type="email" />
        </div>
      </section>

      <section className="card-dark">
        <h2 className="text-lg font-bold mb-2" style={{ color: "#f9f9f9" }}>Integrazione Stripe</h2>
        <p className="text-sm mb-5" style={{ color: "rgba(249,249,249,0.6)" }}>
          Le chiavi Stripe sono configurate nel file <code>.env.local</code> e non sono modificabili qui.
        </p>
        <div className="flex flex-col gap-4">
          <Field label="Stripe webhook URL" name="stripeWebhookUrl" defaultValue="https://formazione-empire.com/api/stripe/webhook" readOnly />
        </div>
      </section>

      <section className="card-dark">
        <h2 className="text-lg font-bold mb-2" style={{ color: "#f9f9f9" }}>Welcome email</h2>
        <p className="text-sm mb-5" style={{ color: "rgba(249,249,249,0.6)" }}>
          Template dell&apos;email inviata allo studente dopo l&apos;acquisto.
        </p>
        <div className="flex flex-col gap-4">
          <div>
            <Label>Corpo email</Label>
            <textarea
              name="welcomeEmailTemplate"
              rows={8}
              defaultValue={
                settings?.welcome_email_template ??
                `Ciao {{nome}},\n\ngrazie per aver scelto Formazione Empire.\n\nLink diretto: {{platform_url}}\n\nTi consigliamo di cambiare la password al primo accesso.`
              }
              className="input-field font-mono text-xs resize-none"
            />
          </div>
        </div>
      </section>

      <div className="flex items-center gap-3">
        <button type="submit" disabled={isPending} className="btn-orange">
          {isPending ? "Salvataggio..." : "Salva impostazioni"}
        </button>
      </div>
      {state?.error && <p style={{ color: "#ff8a8a", fontSize: "0.875rem" }}>{state.error}</p>}
      {state?.success && <p style={{ color: "#6fdca0", fontSize: "0.875rem" }}>{state.success}</p>}
    </form>
  );
}
