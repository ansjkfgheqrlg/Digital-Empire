import Link from "next/link";
import SignupForm from "./signup-form";

export const metadata = { title: "Registrati — Formazione Empire" };

export default async function SignupPage({
  searchParams,
}: {
  searchParams: Promise<{ redirect?: string }>;
}) {
  const { redirect } = await searchParams;

  return (
    <div className="w-full max-w-md">
      <div className="card-fill-silver p-8 md:p-10">
        <div className="relative">
          <span className="eyebrow-silver-orange mb-4 block">Nuovo account</span>
          <h1
            className="text-3xl md:text-4xl font-extrabold tracking-tight mb-2"
            style={{ color: "#13111a", letterSpacing: "-0.02em" }}
          >
            Inizia adesso.
          </h1>
          <p className="text-sm mb-7" style={{ color: "rgba(19,17,26,0.68)" }}>
            Crea il tuo account per accedere al percorso.
          </p>

          <SignupForm redirectTo={redirect} />

          <div
            className="mt-7 text-center text-sm font-medium"
            style={{ color: "rgba(19,17,26,0.62)" }}
          >
            Hai già un account?{" "}
            <Link
              href={`/login${redirect ? `?redirect=${encodeURIComponent(redirect)}` : ""}`}
              className="link-silver-orange"
            >
              Accedi
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
