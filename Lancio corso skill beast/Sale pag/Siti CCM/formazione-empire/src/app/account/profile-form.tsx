"use client";

import { useActionState } from "react";
import { updateProfile } from "./actions";

export default function ProfileForm({
  profile,
  userId,
}: {
  profile: any;
  userId: string;
}) {
  const [state, formAction, isPending] = useActionState(updateProfile, null);

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
        Profilo
      </h2>
      <form
        action={formAction}
        style={{ display: "flex", flexDirection: "column", gap: "1rem" }}
      >
        <input type="hidden" name="userId" value={userId} />
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
            Nome
          </label>
          <input
            name="name"
            defaultValue={profile?.name ?? ""}
            className="input-field"
            placeholder="Il tuo nome"
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
            Email
          </label>
          <input
            value={profile?.email ?? ""}
            readOnly
            className="input-field"
            style={{ color: "#13111a", opacity: 0.6 }}
          />
          <p
            style={{
              color: "#13111a",
              opacity: 0.5,
              fontSize: "0.75rem",
              marginTop: "0.25rem",
            }}
          >
            L&apos;email non è modificabile
          </p>
        </div>
        <button
          type="submit"
          disabled={isPending}
          className="btn-orange"
          style={{ alignSelf: "flex-start" }}
        >
          {isPending ? "Salvataggio..." : "Salva profilo"}
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
