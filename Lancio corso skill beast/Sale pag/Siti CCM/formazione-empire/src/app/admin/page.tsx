import Link from "next/link";
import AdminShell from "@/components/admin-shell";
import { createClient } from "@/lib/supabase/server";

export default async function AdminHome() {
  const supabase = await createClient();
  const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString();

  const [
    { count: totalStudents },
    { count: activeStudents },
    { data: recentEnrollments },
    { data: courses },
  ] = await Promise.all([
    supabase.from("enrollments").select("*", { count: "exact", head: true }),
    supabase
      .from("lesson_progress")
      .select("user_id", { count: "exact", head: true })
      .gte("completed_at", thirtyDaysAgo)
      .eq("completed", true),
    supabase
      .from("enrollments")
      .select("enrolled_at, profiles(name, email), courses(title, slug)")
      .order("enrolled_at", { ascending: false })
      .limit(5),
    supabase.from("courses").select("id, title, slug, status, modules(count)").order("sort_order"),
  ]);

  const stats = [
    { label: "Studenti totali", value: (totalStudents ?? 0).toString(), delta: "iscrizioni totali", tone: "orange" as const },
    { label: "Attivi (30 gg)", value: (activeStudents ?? 0).toString(), delta: "lezioni completate", tone: "mute" as const },
    { label: "Corsi attivi", value: (courses?.filter((c) => c.status === "available").length ?? 0).toString(), delta: `${courses?.length ?? 0} totali`, tone: "mute" as const },
  ];

  return (
    <AdminShell title="Dashboard" subtitle="Panoramica della tua piattaforma">
      {/* Stats grid */}
      <div className="grid md:grid-cols-3 gap-4 mb-10">
        {stats.map((s) => (
          <div key={s.label} className="card-dark !p-5">
            <div className="text-xs font-semibold tracking-widest uppercase mb-2" style={{ color: "rgba(249,249,249,0.55)" }}>
              {s.label}
            </div>
            <div
              className={`text-3xl font-extrabold mb-1 ${s.tone === "orange" ? "text-silver-orange" : ""}`}
              style={s.tone === "mute" ? { color: "#f9f9f9" } : undefined}
            >
              {s.value}
            </div>
            <div className="text-xs" style={{ color: s.tone === "orange" ? "#ff8a4a" : "rgba(249,249,249,0.55)" }}>
              {s.delta}
            </div>
          </div>
        ))}
      </div>

      {/* Recent activity */}
      <div className="grid lg:grid-cols-[1.4fr_1fr] gap-6 mb-10">
        <div className="card-dark">
          <div className="flex items-center justify-between mb-5">
            <h2 className="text-lg font-bold" style={{ color: "#f9f9f9" }}>Iscrizioni recenti</h2>
            <Link href="/admin/studenti" className="text-xs font-semibold" style={{ color: "#ff8a4a" }}>
              Vedi tutti →
            </Link>
          </div>
          <div className="flex flex-col gap-3">
            {recentEnrollments && recentEnrollments.length > 0 ? (
              recentEnrollments.map((e: any, i: number) => (
                <div
                  key={i}
                  className="flex items-center gap-4 p-3 rounded-xl"
                  style={{ background: "rgba(249,249,249,0.03)", border: "1px solid rgba(249,249,249,0.06)" }}
                >
                  <div
                    className="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm flex-shrink-0"
                    style={{ background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)", color: "#ffffff" }}
                  >
                    {(e.profiles?.name ?? e.profiles?.email ?? "?").charAt(0).toUpperCase()}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="text-sm font-semibold truncate" style={{ color: "#f9f9f9" }}>
                      {e.profiles?.name ?? e.profiles?.email ?? "Utente"}
                    </div>
                    <div className="text-xs truncate" style={{ color: "rgba(249,249,249,0.55)" }}>
                      {e.courses?.title ?? "—"} · {new Date(e.enrolled_at).toLocaleDateString("it-IT")}
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <p style={{ color: "rgba(249,249,249,0.4)", fontSize: "0.875rem" }}>Nessuna iscrizione ancora.</p>
            )}
          </div>
        </div>

        <div className="card-dark">
          <h2 className="text-lg font-bold mb-5" style={{ color: "#f9f9f9" }}>Azioni rapide</h2>
          <div className="flex flex-col gap-3">
            {courses?.[0] && (
              <Link href={`/admin/corsi/${courses[0].slug}`} className="btn-orange w-full justify-between">
                Modifica {courses[0].title}
                <span aria-hidden>→</span>
              </Link>
            )}
            <Link href="/admin/corsi" className="btn-ghost w-full justify-between">
              Tutti i corsi
              <span aria-hidden>→</span>
            </Link>
            <Link href="/admin/studenti" className="btn-ghost w-full justify-between">
              Gestisci studenti
              <span aria-hidden>→</span>
            </Link>
            <Link href="/admin/risorse" className="btn-ghost w-full justify-between">
              Upload risorse
              <span aria-hidden>↑</span>
            </Link>
          </div>
        </div>
      </div>

      {/* Courses list */}
      <div>
        <div className="flex items-center justify-between mb-5">
          <h2 className="text-lg font-bold" style={{ color: "#f9f9f9" }}>I tuoi corsi</h2>
          <Link href="/admin/corsi" className="text-xs font-semibold" style={{ color: "#ff8a4a" }}>
            Gestisci corsi →
          </Link>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {courses?.map((c) => (
            <Link key={c.id} href={`/admin/corsi/${c.slug}`} className="card-dark block transition-transform">
              <div className="flex items-center justify-between mb-3">
                <span
                  className={c.status === "available" ? "bubble-orange text-xs" : "px-3 py-1 rounded-full text-xs font-semibold"}
                  style={
                    c.status !== "available"
                      ? { background: "rgba(249,249,249,0.08)", color: "rgba(249,249,249,0.65)", border: "1px solid rgba(249,249,249,0.12)" }
                      : undefined
                  }
                >
                  {c.status === "available" ? "Pubblicato" : "Draft"}
                </span>
              </div>
              <h3 className="text-base font-bold mb-1" style={{ color: "#f9f9f9" }}>{c.title}</h3>
            </Link>
          ))}
        </div>
      </div>
    </AdminShell>
  );
}
