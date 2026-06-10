import Link from "next/link";
import AdminShell from "@/components/admin-shell";
import { createClient } from "@/lib/supabase/server";

export default async function AdminCoursesPage() {
  const supabase = await createClient();
  const { data: courses } = await supabase
    .from("courses")
    .select("id, slug, title, subtitle, status, sort_order")
    .order("sort_order");

  return (
    <AdminShell
      title="Corsi"
      subtitle="Gestisci i corsi pubblicati sulla piattaforma"
      actions={<Link href="/admin/corsi/nuovo" className="btn-orange">+ Nuovo corso</Link>}
    >
      <div className="flex flex-col gap-4">
        {courses?.map((c) => (
          <Link
            key={c.id}
            href={`/admin/corsi/${c.slug}`}
            className="card-dark flex items-center gap-6 group transition-transform"
          >
            <div
              className="w-20 h-20 rounded-2xl flex items-center justify-center text-2xl font-extrabold flex-shrink-0"
              style={
                c.status === "available"
                  ? { background: "linear-gradient(135deg, #fb4604 0%, #c9370a 100%)", color: "#fff" }
                  : { background: "linear-gradient(135deg, #ff8a4a 0%, #fb4604 100%)", color: "#ffffff" }
              }
            >
              {c.title
                .split(" ")
                .map((w: string) => w.charAt(0))
                .join("")
                .slice(0, 3)
                .toUpperCase()}
            </div>
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2 mb-1">
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
              <h3 className="text-xl font-bold mb-1" style={{ color: "#f9f9f9" }}>{c.title}</h3>
              <p className="text-sm truncate" style={{ color: "rgba(249,249,249,0.6)" }}>{c.subtitle}</p>
            </div>
            <svg
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              style={{ color: "rgba(249,249,249,0.4)" }}
              className="flex-shrink-0 group-hover:translate-x-1 transition-transform"
            >
              <line x1="5" y1="12" x2="19" y2="12" />
              <polyline points="12 5 19 12 12 19" />
            </svg>
          </Link>
        ))}
        {(!courses || courses.length === 0) && (
          <div className="card-dark text-center py-10" style={{ color: "rgba(249,249,249,0.4)" }}>
            Nessun corso ancora. Creane uno!
          </div>
        )}
      </div>
    </AdminShell>
  );
}
