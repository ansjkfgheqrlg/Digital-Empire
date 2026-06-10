import Link from "next/link";
import { ArrowRight, Play, Clock, BookOpen, Layers, Download } from "lucide-react";
import type { Course } from "@/lib/data";
import { getCourseProgress } from "@/lib/data";
import { formatDuration } from "@/lib/utils";

const GRAIN_HERO =
  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.2' numOctaves='4' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.5 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")";

const GRAIN_CHIP =
  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='1.6' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.2 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>\")";

function resolveResumeHref(course: Course): string {
  for (const m of course.modules) {
    const lesson = m.lessons.find((l) => !l.completed);
    if (lesson) return `/corsi/${course.slug}/moduli/${m.slug}/${lesson.slug}`;
  }
  const first = course.modules[0];
  const lesson = first?.lessons[0];
  if (!first || !lesson) return `/corsi/${course.slug}`;
  return `/corsi/${course.slug}/moduli/${first.slug}/${lesson.slug}`;
}

export default function CourseBannerHero({ course }: { course: Course }) {
  const progress = getCourseProgress(course);
  const resumeHref = resolveResumeHref(course);
  const titleWords = course.title.trim().split(/\s+/);
  const lastWord = titleWords.pop() ?? course.title;
  const firstWords = titleWords.join(" ");
  const ctaLabel = progress.completed > 0 ? "Riprendi il corso" : "Inizia il corso";

  return (
    <section
      className="relative w-full overflow-hidden"
      style={{
        background:
          "linear-gradient(180deg, #0a0a0a 0%, #060606 60%, #000000 100%)",
      }}
    >
      {/* Subtle radial orange highlight, very faint */}
      <div
        aria-hidden
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "radial-gradient(ellipse 45% 60% at 50% 20%, rgba(251,70,4,0.12) 0%, transparent 65%), radial-gradient(ellipse 40% 50% at 90% 80%, rgba(255,138,74,0.08) 0%, transparent 55%)",
        }}
      />
      {/* Heavy grain */}
      <div
        aria-hidden
        className="absolute inset-0 pointer-events-none"
        style={{ backgroundImage: GRAIN_HERO, opacity: 0.6, mixBlendMode: "overlay" }}
      />
      <div
        aria-hidden
        className="absolute inset-0 pointer-events-none"
        style={{ backgroundImage: GRAIN_HERO, opacity: 0.25, mixBlendMode: "soft-light" }}
      />
      {/* Bottom fade to blend into white section below */}
      <div
        aria-hidden
        className="absolute inset-x-0 bottom-0 pointer-events-none"
        style={{
          height: "40%",
          background:
            "linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.6) 60%, #000 100%)",
        }}
      />

      <div className="container-wide relative pt-14 md:pt-16 pb-14 md:pb-16">
        <div className="max-w-3xl">
          <div className="flex flex-wrap items-center gap-2 mb-5">
            <span
              className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-[10px] font-bold uppercase"
              style={{
                background: "rgba(255,255,255,0.06)",
                color: "#ff8a4a",
                letterSpacing: "0.22em",
                border: "1px solid rgba(255,138,74,0.22)",
              }}
            >
              <span
                className="w-1.5 h-1.5 rounded-full animate-pulse"
                style={{ background: "#fb4604", boxShadow: "0 0 6px #fb4604" }}
              />
              In corso
            </span>
            {course.tagline && (
              <span
                className="text-[10px] md:text-[11px] font-semibold uppercase"
                style={{ color: "rgba(220,220,215,0.55)", letterSpacing: "0.24em" }}
              >
                {course.tagline}
              </span>
            )}
          </div>

          <h1
            className="font-extrabold tracking-tight leading-[0.98] mb-4"
            style={{
              fontSize: "clamp(1.85rem, 4.2vw, 3.8rem)",
              textShadow: "0 10px 36px rgba(0,0,0,0.55)",
            }}
          >
            {firstWords && <span className="text-silver-white">{firstWords} </span>}
            <span className="text-silver-orange italic">{lastWord}</span>
          </h1>

          <p
            className="text-sm md:text-base mb-6 max-w-2xl leading-relaxed"
            style={{ color: "rgba(230,225,220,0.78)" }}
          >
            {course.subtitle}
          </p>

          <div className="flex flex-wrap items-center gap-2 mb-7">
            <SilverChip icon={<Layers size={11} />} label={`${course.modules.length} moduli`} />
            <SilverChip icon={<BookOpen size={11} />} label={`${course.totalLessons} lezioni`} />
            <SilverChip icon={<Clock size={11} />} label={formatDuration(course.totalDuration)} />
            {course.globalResources.length > 0 && (
              <SilverChip
                icon={<Download size={11} />}
                label={`${course.globalResources.length} risorse`}
              />
            )}
            <SilverChip
              icon={null}
              label={
                progress.percentage === 0
                  ? "Non iniziato"
                  : progress.percentage === 100
                  ? "Completato"
                  : `${progress.percentage}% completato`
              }
              accent
            />
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <Link href={resumeHref} className="btn-orange btn-orange--lg group">
              <Play size={14} fill="currentColor" />
              {ctaLabel}
              <ArrowRight
                size={15}
                className="transition-transform group-hover:translate-x-1"
              />
            </Link>
            <a
              href="#moduli"
              className="inline-flex items-center gap-2 px-4 py-2.5 rounded-xl font-semibold text-sm transition-colors"
              style={{
                background: "rgba(255,255,255,0.04)",
                border: "1px solid rgba(255,255,255,0.14)",
                color: "rgba(250,245,240,0.85)",
                backdropFilter: "blur(8px)",
              }}
            >
              Esplora i moduli
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}

function SilverChip({
  icon,
  label,
  accent,
}: {
  icon: React.ReactNode;
  label: string;
  accent?: boolean;
}) {
  return (
    <span
      className="relative inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] md:text-xs font-semibold overflow-hidden"
      style={{
        background: accent
          ? "linear-gradient(135deg, #ffffff 0%, #f0d9c2 22%, #fb4604 58%, #ff8a4a 82%, #ffffff 100%)"
          : "linear-gradient(135deg, #ffffff 0%, #e8e3ef 25%, #b8b3bd 52%, #d9d4e0 78%, #ffffff 100%)",
        color: "#1c1c1c",
        border: accent
          ? "1px solid rgba(255,255,255,0.55)"
          : "1px solid rgba(255,255,255,0.45)",
        boxShadow: accent
          ? "0 6px 16px -6px rgba(251,70,4,0.55), inset 0 1px 0 rgba(255,255,255,0.75)"
          : "0 6px 14px -6px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.65)",
        textShadow: "0 1px 0 rgba(255,255,255,0.4)",
      }}
    >
      <span
        aria-hidden
        className="absolute inset-0 pointer-events-none"
        style={{ backgroundImage: GRAIN_CHIP, mixBlendMode: "overlay", opacity: 0.75 }}
      />
      <span
        aria-hidden
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            "linear-gradient(180deg, rgba(255,255,255,0.22) 0%, transparent 50%, rgba(0,0,0,0.12) 100%)",
        }}
      />
      <span className="relative z-10 inline-flex items-center gap-1.5">
        {icon}
        {label}
      </span>
    </span>
  );
}
