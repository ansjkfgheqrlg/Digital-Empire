import Link from "next/link";
import { redirect } from "next/navigation";
import { ArrowRight } from "lucide-react";
import StudentHeader from "@/components/student-header";
import Reveal from "@/components/reveal";
import { getEnrolledCourses, fetchCourseProgress } from "@/lib/data.server";
import { vetrinaCourses } from "@/lib/data";
import { formatDuration } from "@/lib/utils";
import { createClient } from "@/lib/supabase/server";

export default async function DashboardPage() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  const { data: profile } = await supabase.from("profiles").select("name").eq("id", user.id).single();
  const displayName = profile?.name ?? user?.email?.split("@")[0] ?? "Studente";

  const enrolledCourses = await getEnrolledCourses(user.id);
  const primaryCourse = enrolledCourses[0] ?? null;
  const primaryProgress = primaryCourse
    ? await fetchCourseProgress(primaryCourse.id, user.id)
    : { completed: 0, total: 0, percentage: 0 };

  return (
    <div className="min-h-screen" style={{ background: "#1c1c1c" }}>
      <StudentHeader />

      <main className="container-wide pt-10 pb-20">
        {/* Welcome strip */}
        <Reveal>
          <div className="mb-10">
            <p className="text-sm font-semibold tracking-widest uppercase mb-2" style={{ color: "#ff8a4a" }}>
              Benvenuto in Formazione Empire
            </p>
            <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight" style={{ color: "#f9f9f9" }}>
              Ciao, <span className="text-silver-orange">{displayName}</span>.
            </h1>
            <p className="text-base mt-3 max-w-xl leading-[1.6]" style={{ color: "rgba(249,249,249,0.72)" }}>
              Riprendi da dove hai lasciato. La tua progressione è <strong className="text-orange-pure">salvata in automatico</strong> — video,
              lezioni completate e risorse scaricate, sempre allineati su ogni dispositivo.
            </p>
          </div>
        </Reveal>

        {/* Continue learning - featured silver+orange card */}
        <Reveal delay={0.1}>
          {primaryCourse ? (
            <div className="card-fill-silver-orange relative overflow-hidden mb-16 p-8 md:p-10">
              <div className="relative grid md:grid-cols-[1fr_auto] gap-8 items-end">
                <div>
                  <div
                    className="inline-flex items-center gap-2 px-3 py-1 rounded-full mb-5"
                    style={{ background: "rgba(19,17,26,0.08)", border: "1px solid rgba(19,17,26,0.15)" }}
                  >
                    <span className="w-1.5 h-1.5 rounded-full" style={{ background: "#c9370a", boxShadow: "0 0 8px rgba(201,55,10,0.6)" }} />
                    <span className="text-xs font-bold uppercase tracking-widest" style={{ color: "#8a2a05" }}>Corso in corso</span>
                  </div>
                  <h2 className="text-2xl md:text-4xl font-extrabold tracking-tight mb-3 leading-[1.08]" style={{ color: "#13111a", letterSpacing: "-0.02em" }}>
                    {primaryCourse.title}
                  </h2>
                  <p className="text-base md:text-lg leading-[1.6] max-w-xl mb-6" style={{ color: "rgba(19,17,26,0.72)" }}>
                    {primaryCourse.subtitle}
                  </p>
                  <div className="flex flex-wrap items-center gap-5 text-sm mb-6 font-medium" style={{ color: "rgba(19,17,26,0.6)" }}>
                    <span className="flex items-center gap-1.5"><span style={{ color: "#c9370a" }}>●</span> {primaryCourse.modules.length} moduli</span>
                    <span className="flex items-center gap-1.5"><span style={{ color: "#c9370a" }}>●</span> {primaryCourse.totalLessons} lezioni</span>
                    <span className="flex items-center gap-1.5"><span style={{ color: "#c9370a" }}>●</span> {formatDuration(primaryCourse.totalDuration)}</span>
                  </div>
                  <div className="max-w-md mb-6">
                    <div className="flex items-baseline justify-between mb-2">
                      <span className="text-xs font-bold uppercase tracking-widest" style={{ color: "rgba(19,17,26,0.6)" }}>Progressione</span>
                      <span className="text-sm font-extrabold" style={{ color: "#c9370a" }}>{primaryProgress.percentage}%</span>
                    </div>
                    <div className="progress-track-dark">
                      <div className="progress-fill-dark" style={{ width: `${primaryProgress.percentage}%` }} />
                    </div>
                    <div className="text-xs mt-2 font-medium" style={{ color: "rgba(19,17,26,0.55)" }}>
                      {primaryProgress.completed} di {primaryProgress.total} lezioni completate
                    </div>
                  </div>
                  <Link href={`/corsi/${primaryCourse.slug}`} className="btn-orange group">
                    Riprendi il corso
                    <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                  </Link>
                </div>
                <div className="hidden md:block relative">
                  <div
                    className="w-48 h-48 rounded-2xl relative overflow-hidden"
                    style={{ background: "linear-gradient(135deg, #fb4604 0%, #c9370a 100%)", boxShadow: "0 40px 80px -20px rgba(251,70,4,0.55), 0 0 0 1px rgba(255,255,255,0.4)" }}
                  >
                    <div className="absolute inset-0 flex items-center justify-center">
                      <span className="text-4xl font-extrabold text-white tracking-tight">
                        {primaryCourse.title.split(" ").map((w: string) => w[0]).join("").slice(0, 3).toUpperCase()}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            <div className="card-fill-silver mb-16 p-8 text-center">
              <h2 className="text-2xl font-extrabold mb-3" style={{ color: "#13111a" }}>Nessun corso ancora</h2>
              <p className="mb-6" style={{ color: "rgba(19,17,26,0.65)" }}>Acquista il tuo primo corso per iniziare.</p>
              <Link href="/" className="btn-orange">Scopri i corsi</Link>
            </div>
          )}
        </Reveal>

        {/* Vetrina altri corsi */}
        <Reveal delay={0.15}>
          <div className="flex items-end justify-between mb-8">
            <div>
              <h2 className="text-2xl md:text-3xl font-extrabold tracking-tight" style={{ color: "#f9f9f9" }}>
                Altri corsi <span className="text-silver-orange">Empire</span>
              </h2>
              <p className="text-sm mt-2" style={{ color: "rgba(249,249,249,0.62)" }}>
                In arrivo — clicca per scoprire di più.
              </p>
            </div>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-2 gap-5">
          {vetrinaCourses.map((c, i) => (
            <Reveal key={c.id} delay={0.2 + i * 0.05}>
              <Link href={c.salesPageUrl || "#"} className="block group">
                <div className="card-fill-silver h-full relative overflow-hidden">
                  <div className="absolute top-5 right-5">
                    <span
                      className="px-3 py-1 rounded-full text-[11px] font-bold uppercase tracking-wider"
                      style={{
                        background: "rgba(19,17,26,0.08)",
                        color: "rgba(19,17,26,0.65)",
                        border: "1px solid rgba(19,17,26,0.12)",
                      }}
                    >
                      In arrivo
                    </span>
                  </div>
                  <div className="text-xs font-bold tracking-widest uppercase mb-4" style={{ color: "#8a2a05" }}>
                    {c.tagline}
                  </div>
                  <h3
                    className="text-xl md:text-2xl font-extrabold tracking-tight mb-3 transition-colors"
                    style={{ color: "#13111a", letterSpacing: "-0.02em" }}
                  >
                    {c.title}
                  </h3>
                  <p className="text-sm leading-[1.6] mb-5" style={{ color: "rgba(19,17,26,0.72)" }}>
                    {c.description}
                  </p>
                  <div
                    className="flex items-center gap-5 text-sm pt-4 font-medium"
                    style={{ color: "rgba(19,17,26,0.6)", borderTop: "1px solid rgba(19,17,26,0.12)" }}
                  >
                    <span>{c.totalLessons} lezioni</span>
                    <span>{formatDuration(c.totalDuration)}</span>
                    <span
                      className="ml-auto font-bold flex items-center gap-1"
                      style={{ color: "#c9370a" }}
                    >
                      Scopri di più
                      <ArrowRight className="h-3.5 w-3.5" />
                    </span>
                  </div>
                </div>
              </Link>
            </Reveal>
          ))}
        </div>
      </main>
    </div>
  );
}
