import { redirect } from "next/navigation";
import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import StudentHeader from "@/components/student-header";
import ProfileForm from "./profile-form";
import PasswordForm from "./password-form";

export default async function AccountPage() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  const { data: profile } = await supabase
    .from("profiles")
    .select("*")
    .eq("id", user.id)
    .single();

  return (
    <div className="min-h-screen" style={{ background: "#1c1c1c" }}>
      <StudentHeader />
      <main style={{ maxWidth: 680, margin: "0 auto", padding: "2.5rem 1.5rem 5rem" }}>
        <div style={{ marginBottom: "2rem" }}>
          <Link
            href="/dashboard"
            style={{
              color: "rgba(249,249,249,0.5)",
              fontSize: "0.875rem",
              textDecoration: "none",
              display: "inline-flex",
              alignItems: "center",
              gap: "0.375rem",
              marginBottom: "1.5rem",
            }}
          >
            ← Dashboard
          </Link>
          <h1
            style={{
              color: "#f9f9f9",
              fontSize: "1.75rem",
              fontWeight: 700,
              marginBottom: "0.375rem",
            }}
          >
            Il tuo account
          </h1>
          <p style={{ color: "rgba(249,249,249,0.5)", fontSize: "0.9375rem" }}>
            Gestisci il tuo profilo e la sicurezza
          </p>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: "1.25rem" }}>
          <ProfileForm profile={{ ...profile, email: user.email }} userId={user.id} />
          <PasswordForm />
        </div>
      </main>
    </div>
  );
}
