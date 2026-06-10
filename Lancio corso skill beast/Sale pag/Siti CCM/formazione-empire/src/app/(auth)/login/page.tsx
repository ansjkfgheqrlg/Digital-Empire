import Link from "next/link";
import LoginForm from "./login-form";

export const metadata = { title: "Accedi — Formazione Empire" };

export default async function LoginPage({
  searchParams,
}: {
  searchParams: Promise<{ redirect?: string; confirmed?: string }>;
}) {
  const { redirect, confirmed } = await searchParams;

  return (
    <div className="w-full max-w-md">
      <div className="card-fill-silver p-8 md:p-10">
        <div className="relative">
          <span className="eyebrow-silver-orange mb-4 block">Area studenti</span>
          <h1
            className="text-3xl md:text-4xl font-extrabold tracking-tight mb-2"
            style={{ color: "#13111a", letterSpacing: "-0.02em" }}
          >
            Bentornato.
          </h1>
          <p className="text-sm mb-7" style={{ color: "rgba(19,17,26,0.68)" }}>
            Accedi per continuare il tuo percorso.
          </p>

          {confirmed === "1" && (
            <div
              className="mb-5 rounded-xl px-4 py-3 text-sm font-medium"
              style={{
                background: "linear-gradient(180deg, rgba(76,175,80,0.14) 0%, rgba(76,175,80,0.04) 100%)",
                border: "1px solid rgba(76,175,80,0.45)",
                color: "#1f5a28",
              }}
            >
              ✓ Email confermata. Ora puoi accedere.
            </div>
          )}

          <LoginForm redirectTo={redirect} />

          <div
            className="mt-7 text-center text-sm font-medium"
            style={{ color: "rgba(19,17,26,0.62)" }}
          >
            Non hai ancora un account?{" "}
            <Link
              href={`/signup${redirect ? `?redirect=${encodeURIComponent(redirect)}` : ""}`}
              className="link-silver-orange"
            >
              Registrati
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
