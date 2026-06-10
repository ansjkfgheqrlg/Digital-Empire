"use client";
import Link from "next/link";
import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { ChevronDown, Play, Clock, Download } from "lucide-react";
import type { Course } from "@/lib/data";
import { getModuleProgress } from "@/lib/data";
import { formatDuration } from "@/lib/utils";

export default function ModulesAccordion({ course }: { course: Course }) {
  const firstUnfinished =
    course.modules.find((m) => m.lessons.some((l) => !l.completed))?.id ?? course.modules[0]?.id ?? null;
  const [openId, setOpenId] = useState<string | null>(firstUnfinished);

  return (
    <div className="flex flex-col gap-4">
      {course.modules.map((mod) => {
        const mp = getModuleProgress(mod);
        const expanded = openId === mod.id;
        const duration = mod.lessons.reduce((a, l) => a + l.duration, 0);

        return (
          <div
            key={mod.id}
            className="card-fill-silver !p-0 overflow-hidden transition-colors"
            style={{
              borderColor: expanded ? "rgba(251,70,4,0.45)" : undefined,
              boxShadow: expanded ? "0 30px 70px -24px rgba(251,70,4,0.28)" : undefined,
            }}
          >
            <button
              onClick={() => setOpenId(expanded ? null : mod.id)}
              aria-expanded={expanded}
              className="w-full flex items-center gap-5 p-5 md:p-6 text-left cursor-pointer group"
            >
              <div
                className="flex-shrink-0 w-14 h-14 md:w-16 md:h-16 rounded-2xl flex items-center justify-center text-xl font-extrabold"
                style={{
                  background: mp.isDone
                    ? "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)"
                    : "linear-gradient(135deg, rgba(251,70,4,0.2) 0%, rgba(251,70,4,0.08) 100%)",
                  color: mp.isDone ? "#fff" : "#ff8a4a",
                  border: mp.isDone ? "1px solid #c9370a" : "1px solid rgba(251,70,4,0.38)",
                  boxShadow: mp.isDone ? "0 16px 36px -12px rgba(251,70,4,0.55)" : undefined,
                }}
              >
                {mp.isDone ? (
                  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                ) : (
                  mod.index.toString().padStart(2, "0")
                )}
              </div>

              <div className="flex-1 min-w-0">
                <div className="text-[11px] font-semibold tracking-[0.18em] uppercase mb-1.5" style={{ color: "rgba(251,70,4,0.9)" }}>
                  Modulo {mod.index}
                </div>
                <h3 className="text-lg md:text-xl font-bold leading-snug mb-1.5 group-hover:text-orange-pure transition-colors" style={{ color: "#fafaf6" }}>
                  {mod.title}
                </h3>
                <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs" style={{ color: "rgba(250,250,246,0.55)" }}>
                  <span>{mod.lessons.length} lezioni</span>
                  <span>·</span>
                  <span>{formatDuration(duration)}</span>
                  {mp.percentage > 0 && (
                    <>
                      <span>·</span>
                      <span className="font-semibold" style={{ color: mp.isDone ? "#fb4604" : "#ff8a4a" }}>
                        {mp.percentage}% completato
                      </span>
                    </>
                  )}
                </div>
              </div>

              <div className="hidden sm:flex items-center gap-4 flex-shrink-0">
                {!mp.isDone && mp.percentage > 0 && (
                  <div className="w-28">
                    <div className="progress-track" style={{ background: "rgba(249,249,249,0.08)", height: 5 }}>
                      <div className="progress-fill-orange" style={{ width: `${mp.percentage}%`, height: 5 }} />
                    </div>
                  </div>
                )}
                <div
                  className="w-9 h-9 rounded-full flex items-center justify-center transition-transform"
                  style={{
                    background: "rgba(251,70,4,0.14)",
                    border: "1px solid rgba(251,70,4,0.35)",
                    color: "#ff8a4a",
                    transform: expanded ? "rotate(180deg)" : "none",
                  }}
                >
                  <ChevronDown size={16} />
                </div>
              </div>
            </button>

            <AnimatePresence initial={false}>
              {expanded && (
                <motion.div
                  key="body"
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: "auto", opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  transition={{ duration: 0.32, ease: [0.22, 1, 0.36, 1] }}
                  style={{ overflow: "hidden" }}
                >
                  <div className="border-t px-4 md:px-6 py-5" style={{ borderColor: "rgba(249,249,249,0.08)", background: "rgba(249,249,249,0.02)" }}>
                    {mod.subtitle && (
                      <p className="text-sm mb-5 max-w-3xl" style={{ color: "rgba(250,250,246,0.68)" }}>
                        {mod.subtitle}
                      </p>
                    )}
                    <div className="flex flex-col gap-2">
                      {mod.lessons.map((l, i) => (
                        <Link
                          key={l.id}
                          href={`/corsi/${course.slug}/moduli/${mod.slug}/${l.slug}`}
                          className="group/lesson flex items-center gap-4 p-3.5 rounded-xl transition-all hover:-translate-y-0.5"
                          style={{
                            background: "rgba(249,249,249,0.035)",
                            border: "1px solid rgba(249,249,249,0.06)",
                          }}
                        >
                          <div
                            className="w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0"
                            style={{
                              background: l.completed ? "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)" : "rgba(251,70,4,0.1)",
                              color: l.completed ? "#fff" : "#ff8a4a",
                              border: l.completed ? "1px solid #c9370a" : "1px solid rgba(251,70,4,0.3)",
                            }}
                          >
                            {l.completed ? (
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                                <polyline points="20 6 9 17 4 12" />
                              </svg>
                            ) : (
                              <Play size={13} fill="currentColor" />
                            )}
                          </div>
                          <div className="flex-1 min-w-0">
                            <div className="text-sm md:text-base font-semibold group-hover/lesson:text-orange-pure transition-colors truncate" style={{ color: "#fafaf6" }}>
                              <span className="mr-2 text-xs" style={{ color: "rgba(250,250,246,0.4)" }}>L{i + 1}.</span>
                              {l.title}
                            </div>
                            <div className="text-xs truncate mt-0.5" style={{ color: "rgba(250,250,246,0.5)" }}>
                              {l.description}
                            </div>
                          </div>
                          <div className="hidden sm:flex items-center gap-3 text-xs flex-shrink-0" style={{ color: "rgba(250,250,246,0.5)" }}>
                            <span className="flex items-center gap-1"><Clock size={12} />{formatDuration(l.duration)}</span>
                            {l.resources.length > 0 && (
                              <span className="flex items-center gap-1"><Download size={12} />{l.resources.length}</span>
                            )}
                          </div>
                        </Link>
                      ))}
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        );
      })}
    </div>
  );
}
