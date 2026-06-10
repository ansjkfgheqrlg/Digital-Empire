"use client";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import Reveal from "../reveal";
import { ccmCourse, vetrinaCourses } from "@/lib/data";
import { formatDuration } from "@/lib/utils";

export default function LandingCourses() {
  const allCourses = [ccmCourse, ...vetrinaCourses];

  return (
    <section id="corsi" className="section section-border-t bg-ink-2 relative">
      <div className="container-wide">
        <Reveal>
          <div className="text-center mb-14 max-w-3xl mx-auto">
            <span className="bubble-orange mb-5 inline-flex">
              I nostri corsi
            </span>
            <h2 className="text-3xl md:text-5xl font-extrabold tracking-tight leading-[1.08] mb-5">
              <span className="text-silver-white">Progettati per produrre </span>
              <span className="text-silver-orange">risultati misurabili</span>
              <span className="text-silver-white">.</span>
            </h2>
            <p className="text-base md:text-lg leading-[1.65]" style={{ color: "rgba(249,249,249,0.72)" }}>
              Ogni corso è un <span className="hl-block">sistema completo</span>:
              framework operativi, skill riutilizzabili, progetti reali{" "}
              <span className="text-silver-orange font-semibold">da mettere subito in produzione</span>.
              Niente filler, niente teoria stantìa.
            </p>
          </div>
        </Reveal>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {allCourses.map((course, i) => (
            <Reveal key={course.id} delay={i * 0.08}>
              <CourseCard course={course} />
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}

function CourseCard({ course }: { course: typeof ccmCourse }) {
  const isAvailable = course.status === "available";

  return (
    <div
      className={`${isAvailable ? "card-fill-silver-orange" : "card-fill-silver"} relative overflow-hidden flex flex-col min-h-[480px] transition-all duration-300`}
      style={!isAvailable ? { opacity: 0.95 } : undefined}
    >
      {isAvailable && (
        <div className="absolute top-6 right-6">
          <span
            className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider"
            style={{
              background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)",
              color: "#ffffff",
              boxShadow: "0 8px 20px -8px rgba(251,70,4,0.6), inset 0 1px 0 rgba(255,255,255,0.3)",
            }}
          >
            Disponibile ora
          </span>
        </div>
      )}
      {!isAvailable && (
        <div className="absolute top-6 right-6">
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
      )}

      <div
        className="flex items-center gap-2 mb-5 text-[0.7rem] uppercase tracking-widest font-semibold"
        style={{ color: isAvailable ? "#8a2a05" : "rgba(19,17,26,0.55)" }}
      >
        <span>Corso</span>
        <span className="w-1 h-1 rounded-full" style={{ background: isAvailable ? "rgba(19,17,26,0.45)" : "rgba(19,17,26,0.3)" }} />
        <span>{course.totalLessons} lezioni</span>
        <span className="w-1 h-1 rounded-full" style={{ background: isAvailable ? "rgba(19,17,26,0.45)" : "rgba(19,17,26,0.3)" }} />
        <span>{formatDuration(course.totalDuration)}</span>
      </div>

      <h3
        className="text-2xl md:text-3xl font-extrabold leading-tight mb-3 tracking-tight"
        style={{ color: "#13111a", letterSpacing: "-0.02em" }}
      >
        {course.title}
      </h3>

      <p
        className="text-sm leading-relaxed mb-5"
        style={{ color: "rgba(19,17,26,0.72)" }}
      >
        {course.description}
      </p>

      <div className="flex-1 flex flex-col justify-end gap-3">
        <div
          style={{
            height: 1,
            background:
              "linear-gradient(90deg, transparent 0%, rgba(201,55,10,0.35) 25%, rgba(201,55,10,0.35) 75%, transparent 100%)",
          }}
        />

        {isAvailable ? (
          <Link href="/signup" className="btn-orange w-full justify-center mt-3 group">
            Inizia il corso
            <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
          </Link>
        ) : (
          <Link
            href={course.salesPageUrl || "#"}
            className="inline-flex items-center justify-center gap-2 w-full mt-3 px-5 py-3 rounded-xl font-semibold text-sm transition-colors"
            style={{
              background: "rgba(19,17,26,0.06)",
              border: "1px solid rgba(19,17,26,0.16)",
              color: "#13111a",
            }}
          >
            Scopri di più
            <ArrowRight className="h-4 w-4" />
          </Link>
        )}
      </div>
    </div>
  );
}
