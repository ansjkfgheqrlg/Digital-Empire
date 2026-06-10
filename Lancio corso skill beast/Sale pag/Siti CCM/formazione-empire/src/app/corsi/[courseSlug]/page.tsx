import Link from "next/link";
import { notFound } from "next/navigation";
import StudentHeader from "@/components/student-header";
import CourseBannerHero from "@/components/course-banner-hero";
import StickyProgressBar from "@/components/sticky-progress-bar";
import ModulesAccordion from "@/components/modules-accordion";
import ResourceCard from "@/components/resource-card";
import { getCourse, getCourseProgress } from "@/lib/data";

const NOISE_COARSE =
  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.15' numOctaves='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.6 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")";

const NOISE_FINE =
  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='2.1' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.45 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")";

export default async function CoursePage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const course = getCourse(courseSlug);
  if (!course || !course.owned) notFound();

  const progress = getCourseProgress(course);

  return (
    <>
      <StudentHeader inCourseTheme />
      <StickyProgressBar
        pct={progress.percentage}
        completed={progress.completed}
        total={progress.total}
        courseTitle={course.title}
      />

      {/* 1. Base bianco-argento perlato + macchie luce arancioni */}
      <div aria-hidden className="fixed inset-0 pointer-events-none" style={{
        zIndex: 101,
        background: `
          radial-gradient(ellipse 55% 42% at 72% 28%, rgba(255,170,110,0.48) 0%, rgba(255,170,110,0.18) 35%, transparent 65%),
          radial-gradient(ellipse 48% 38% at 22% 78%, rgba(251,70,4,0.32) 0%, rgba(251,70,4,0.12) 38%, transparent 68%),
          radial-gradient(ellipse 40% 30% at 90% 85%, rgba(255,138,74,0.28) 0%, transparent 60%),
          linear-gradient(135deg, #ffffff 0%, #faf7f3 22%, #efe8df 45%, #f4ece2 65%, #fbfaf8 100%)
        `,
      }} />
      {/* 2. Grana fine overlay */}
      <div aria-hidden className="fixed inset-0 pointer-events-none" style={{
        zIndex: 102,
        backgroundImage: NOISE_FINE,
        opacity: 0.5,
        mixBlendMode: "overlay",
      }} />
      {/* 3. Mini coarse multiply bassissimo */}
      <div aria-hidden className="fixed inset-0 pointer-events-none" style={{
        zIndex: 103,
        backgroundImage: NOISE_COARSE,
        opacity: 0.10,
        mixBlendMode: "multiply",
      }} />

      <main className="relative pb-24" style={{ zIndex: 120 }}>
        <CourseBannerHero course={course} />

        <div className="container-wide pt-12 md:pt-16 relative">
          <nav className="flex items-center gap-2 text-sm mb-10" style={{ color: "rgba(10,10,10,0.72)" }}>
            <Link href="/dashboard" className="hover:text-black transition-colors">Dashboard</Link>
            <span style={{ color: "rgba(10,10,10,0.4)" }}>/</span>
            <span style={{ color: "#1c1c1c", fontWeight: 600 }}>{course.title}</span>
          </nav>

          <div id="moduli" className="max-w-4xl mx-auto scroll-mt-28">
            <div className="flex items-end justify-between flex-wrap gap-4 mb-8">
              <div>
                <span className="pre-headline mb-3" style={{ color: "#c9370a" }}>
                  Mappa del corso
                </span>
                <h2 className="text-3xl md:text-5xl font-extrabold tracking-tight mt-3 leading-[1.05]" style={{ color: "#0a0a0a" }}>
                  <span className="text-silver-black">I tuoi </span>
                  <span className="text-silver-orange italic">moduli</span>
                </h2>
                <p className="text-sm md:text-base max-w-xl mt-3" style={{ color: "rgba(10,10,10,0.72)" }}>
                  Clicca un modulo per espanderlo e aprire le lezioni. Il prossimo da guardare è già aperto per te.
                </p>
              </div>
              <div className="text-right hidden md:block">
                <div className="text-xs font-bold uppercase tracking-[0.18em]" style={{ color: "rgba(10,10,10,0.55)" }}>
                  Avanzamento
                </div>
                <div className="text-4xl font-extrabold leading-none mt-1" style={{ color: "#c9370a" }}>
                  {progress.percentage}%
                </div>
                <div className="text-xs mt-1" style={{ color: "rgba(10,10,10,0.6)" }}>
                  {progress.completed} di {progress.total} lezioni
                </div>
              </div>
            </div>

            <ModulesAccordion course={course} />
          </div>

          {course.globalResources.length > 0 && (
            <section className="max-w-4xl mx-auto relative rounded-3xl py-14 px-6 md:px-10 mt-20 overflow-hidden" style={{
              background: "linear-gradient(180deg, #0a0a0a 0%, #050505 100%)",
              border: "1px solid rgba(255,255,255,0.06)",
              boxShadow: "0 40px 80px -30px rgba(0,0,0,0.85)",
            }}>
              <div aria-hidden className="absolute inset-0 pointer-events-none" style={{
                background: "radial-gradient(circle at 20% 10%, rgba(251,70,4,0.18) 0%, transparent 55%), radial-gradient(circle at 85% 90%, rgba(255,106,46,0.12) 0%, transparent 55%)",
              }} />
              <div className="relative">
                <div className="text-center mb-8">
                  <span className="bubble-orange mb-3">Libreria</span>
                  <h2 className="text-3xl md:text-4xl font-extrabold tracking-tight mt-3" style={{ color: "#fafaf6" }}>
                    Risorse <span className="text-silver-orange italic">premium</span>
                  </h2>
                  <p className="text-sm mt-3 max-w-xl mx-auto" style={{ color: "rgba(250,250,246,0.6)" }}>
                    Framework, script e template scaricabili inclusi nel corso.
                  </p>
                </div>
                <div className="max-w-3xl mx-auto grid md:grid-cols-2 gap-3">
                  {course.globalResources.map((r) => (
                    <ResourceCard key={r.id} resource={r} dark />
                  ))}
                </div>
              </div>
            </section>
          )}
        </div>
      </main>
    </>
  );
}
