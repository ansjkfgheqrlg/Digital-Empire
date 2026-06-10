import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft, ArrowRight, Clock } from "lucide-react";
import StudentHeader from "@/components/student-header";
import VideoPlayer from "@/components/video-player";
import ResourceCard from "@/components/resource-card";
import LessonDrawer from "@/components/lesson-drawer";
import { fetchLesson } from "@/lib/data.server";
import { formatDuration } from "@/lib/utils";
import { createClient } from "@/lib/supabase/server";
import MarkCompleteButton from "./mark-complete";

export default async function LessonPage({ params }: { params: Promise<{ courseSlug: string; moduleSlug: string; lessonSlug: string }> }) {
  const { courseSlug, moduleSlug, lessonSlug } = await params;
  const data = await fetchLesson(courseSlug, moduleSlug, lessonSlug);
  if (!data) notFound();
  const { course, module, lesson } = data;

  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  let isCompleted = false;
  let completedIds = new Set<string>();
  if (user) {
    const { data: progress } = await supabase
      .from("lesson_progress")
      .select("lesson_id, completed")
      .eq("user_id", user.id)
      .in("lesson_id", module.lessons.map((l) => l.id));
    completedIds = new Set(
      progress?.filter((p) => p.completed).map((p) => p.lesson_id) ?? []
    );
    isCompleted = completedIds.has(lesson.id);
  }

  const lessonIndex = module.lessons.findIndex((l) => l.id === lesson.id);
  const prevLesson = module.lessons[lessonIndex - 1];
  const nextLesson = module.lessons[lessonIndex + 1];

  return (
    <>
      <StudentHeader inCourseTheme />

      <main className="container-wide pt-8 pb-32">
        <nav className="flex items-center gap-2 text-sm mb-6 flex-wrap" style={{ color: "rgba(250,250,246,0.55)" }}>
          <Link href="/dashboard" className="hover:text-white transition-colors">Dashboard</Link>
          <span>/</span>
          <Link href={`/corsi/${course.slug}`} className="hover:text-white transition-colors">{course.title}</Link>
          <span>/</span>
          <span style={{ color: "#fafaf6" }}>Modulo {module.index}</span>
        </nav>

        <div className="max-w-5xl mx-auto">
          <div className="flex flex-wrap items-center gap-3 mb-5">
            <span className="bubble-orange text-xs">Lezione {lessonIndex + 1} di {module.lessons.length}</span>
            <span className="text-xs font-semibold uppercase tracking-widest flex items-center gap-1.5" style={{ color: "rgba(250,250,246,0.55)" }}>
              <Clock size={12} />
              {formatDuration(lesson.duration)}
            </span>
            <span className="text-xs font-semibold uppercase tracking-widest" style={{ color: "rgba(250,250,246,0.55)" }}>
              Modulo {module.index} · {module.title}
            </span>
          </div>

          <h1 className="text-3xl md:text-5xl lg:text-6xl font-extrabold tracking-tight leading-[1.05] mb-5">
            <span className="text-silver-orange">{lesson.title}</span>
          </h1>
          <p className="text-lg leading-relaxed max-w-3xl mb-10" style={{ color: "rgba(250,250,246,0.72)" }}>
            {lesson.description}
          </p>

          <div
            className="mb-12 relative rounded-[24px] overflow-hidden"
            style={{
              boxShadow: "0 60px 120px -30px rgba(0,0,0,0.85), 0 0 0 1px rgba(251,70,4,0.18)",
            }}
          >
            <span aria-hidden className="absolute -inset-[1px] rounded-[24px] pointer-events-none" style={{
              background: "linear-gradient(135deg, rgba(251,70,4,0.35) 0%, transparent 40%, transparent 60%, rgba(251,70,4,0.25) 100%)",
              WebkitMask: "linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0)",
              WebkitMaskComposite: "xor",
              maskComposite: "exclude",
              padding: 1,
            }} />
            <VideoPlayer title={lesson.title} videoUrl={lesson.videoUrl ?? undefined} />
          </div>

          <div
            className="relative rounded-3xl overflow-hidden p-8 md:p-10 mb-12"
            style={{
              background:
                "linear-gradient(180deg, #ffffff 0%, #f4f1f7 45%, #e8e3ef 100%)",
              border: "1px solid rgba(255,255,255,0.9)",
              boxShadow:
                "0 40px 80px -32px rgba(0,0,0,0.55), inset 0 2px 0 rgba(255,255,255,0.95), inset 0 -2px 0 rgba(138,133,148,0.18), 0 0 0 1px rgba(138,133,148,0.18)",
            }}
          >
            <span aria-hidden className="absolute inset-0 pointer-events-none rounded-3xl" style={{
              backgroundImage:
                "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.4' numOctaves='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")",
              mixBlendMode: "multiply",
              opacity: 0.5,
            }} />
            <div className="relative">
              <div className="text-xs font-semibold uppercase tracking-widest mb-4" style={{ color: "#c9370a" }}>
                Contenuto della lezione
              </div>
              <h2 className="text-2xl md:text-3xl font-bold mb-5" style={{ color: "#1c1c1c" }}>
                Cosa troverai in questa lezione
              </h2>
              <p className="text-base md:text-lg leading-relaxed whitespace-pre-line" style={{ color: "rgba(28,28,28,0.78)" }}>
                {lesson.longDescription}
              </p>

              <div className="mt-8 pt-6 border-t flex flex-wrap items-center gap-4" style={{ borderColor: "rgba(28,28,28,0.1)" }}>
                <MarkCompleteButton
                  lessonId={lesson.id}
                  courseSlug={courseSlug}
                  moduleSlug={moduleSlug}
                  lessonSlug={lessonSlug}
                  initialCompleted={isCompleted}
                />
                {nextLesson && (
                  <Link
                    href={`/corsi/${course.slug}/moduli/${module.slug}/${nextLesson.slug}`}
                    className="text-sm font-semibold flex items-center gap-2 transition-colors"
                    style={{ color: "rgba(28,28,28,0.7)" }}
                  >
                    Prossima lezione <ArrowRight size={14} />
                  </Link>
                )}
              </div>
            </div>
          </div>

          {lesson.resources.length > 0 && (
            <div className="mb-12">
              <span className="bubble-orange mb-3">Materiale</span>
              <h2 className="text-2xl md:text-3xl font-extrabold tracking-tight mb-5" style={{ color: "#fafaf6" }}>
                Risorse della <span className="text-silver-orange">lezione</span>
              </h2>
              <div className="grid md:grid-cols-2 gap-3">
                {lesson.resources.map((r) => (
                  <ResourceCard key={r.id} resource={r} dark />
                ))}
              </div>
            </div>
          )}

          <div className="flex flex-col md:flex-row gap-3 pt-6 border-t" style={{ borderColor: "rgba(249,249,249,0.1)" }}>
            {prevLesson ? (
              <Link
                href={`/corsi/${course.slug}/moduli/${module.slug}/${prevLesson.slug}`}
                className="relative overflow-hidden rounded-2xl p-5 flex items-center gap-4 flex-1 group transition-all hover:-translate-y-0.5"
                style={{
                  background: "linear-gradient(180deg, #ffffff 0%, #f4f1f7 50%, #e8e3ef 100%)",
                  border: "1px solid rgba(255,255,255,0.85)",
                  boxShadow: "0 18px 40px -22px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.95), 0 0 0 1px rgba(138,133,148,0.18)",
                }}
              >
                <span aria-hidden className="absolute inset-0 pointer-events-none rounded-2xl" style={{
                  backgroundImage:
                    "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.4' numOctaves='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")",
                  mixBlendMode: "multiply",
                  opacity: 0.45,
                }} />
                <div className="relative w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0" style={{ background: "rgba(28,28,28,0.08)", color: "rgba(28,28,28,0.7)" }}>
                  <ArrowLeft size={16} />
                </div>
                <div className="relative min-w-0">
                  <div className="text-xs uppercase tracking-widest mb-1" style={{ color: "rgba(28,28,28,0.55)" }}>Precedente</div>
                  <div className="font-semibold truncate text-sm" style={{ color: "#1c1c1c" }}>{prevLesson.title}</div>
                </div>
              </Link>
            ) : (
              <div className="flex-1" />
            )}
            {nextLesson ? (
              <Link
                href={`/corsi/${course.slug}/moduli/${module.slug}/${nextLesson.slug}`}
                className="relative overflow-hidden rounded-2xl p-5 flex items-center gap-4 flex-1 group transition-all hover:-translate-y-0.5 md:text-right"
                style={{
                  background: "linear-gradient(180deg, #ffffff 0%, #f4f1f7 50%, #e8e3ef 100%)",
                  border: "1px solid rgba(255,255,255,0.85)",
                  boxShadow: "0 18px 40px -22px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.95), 0 0 0 1px rgba(138,133,148,0.18)",
                }}
              >
                <span aria-hidden className="absolute inset-0 pointer-events-none rounded-2xl" style={{
                  backgroundImage:
                    "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.4' numOctaves='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.5 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")",
                  mixBlendMode: "multiply",
                  opacity: 0.45,
                }} />
                <div className="relative min-w-0 flex-1">
                  <div className="text-xs uppercase tracking-widest mb-1" style={{ color: "rgba(28,28,28,0.55)" }}>Successivo</div>
                  <div className="font-semibold truncate text-sm" style={{ color: "#1c1c1c" }}>{nextLesson.title}</div>
                </div>
                <div className="relative w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0" style={{ background: "rgba(251,70,4,0.18)", color: "#c9370a", border: "1px solid rgba(251,70,4,0.35)" }}>
                  <ArrowRight size={16} />
                </div>
              </Link>
            ) : (
              <div className="flex-1" />
            )}
          </div>
        </div>
      </main>

      <LessonDrawer
        course={{ slug: course.slug, title: course.title }}
        module={module}
        activeLessonId={lesson.id}
        completedIds={completedIds}
      />
    </>
  );
}
