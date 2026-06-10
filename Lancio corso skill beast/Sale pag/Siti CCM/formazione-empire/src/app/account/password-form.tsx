"use client";

import { useActionState } from "react";
import { changePassword } from "./actions";

export default function PasswordForm() {
  const [state, formAction, isPending] = useActionState(changePassword, null);

  return (
    <div
      className="card-fill-silver"
      style={{ padding: "1.5rem", borderRadius: "1rem" }}
    >
      <h2
        style={{
          color: "#13111a",
          fontSize: "1.125rem",
          fontWeight: 700,
          marginBottom: "1.25rem",
        }}
      >
        Cambia password
      </h2>
      <form
        action={formAction}
        style={{ display: "flex", flexDirection: "column", gap: "1rem" }}
      >
        <div>
          <label
            style={{
              display: "block",
              color: "#13111a",
              fontSize: "0.875rem",
              fontWeight: 500,
              marginBottom: "0.375rem",
            }}
          >
            Nuova password
          </label>
          <input
            name="password"
            type="password"
            className="input-field"
            placeholder="Minimo 8 caratteri"
            minLength={8}
            required
            style={{ color: "#13111a" }}
          />
        </div>
        <div>
          <label
            style={{
              display: "block",
              color: "#13111a",
              fontSize: "0.875rem",
              fontWeight: 500,
              marginBottom: "0.375rem",
            }}
          >
            Conferma password
          </label>
          <input
            name="confirmPassword"
            type="password"
            className="input-field"
            placeholder="Ripeti la password"
            required
            style={{ color: "#13111a" }}
          />
        </div>
        <button
          type="submit"
          disabled={isPending}
          className="btn-orange"
          style={{ alignSelf: "flex-start" }}
        >
          {isPending ? "Aggiornamento..." : "Aggiorna password"}
        </button>
        {state?.error && (
          <p style={{ color: "#ff8a8a", fontSize: "0.875rem" }}>{state.error}</p>
        )}
        {state?.success && (
          <p style={{ color: "#6fdca0", fontSize: "0.875rem" }}>{state.success}</p>
        )}
      </form>
    </div>
  );
}
