"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { List, X, Play } from "lucide-react";
import type { Module } from "@/lib/data";
import { formatDuration } from "@/lib/utils";

export default function LessonDrawer({
  course,
  module,
  activeLessonId,
  completedIds = new Set(),
}: {
  course: { slug: string; title: string };
  module: Module;
  activeLessonId: string;
  completedIds?: Set<string>;
}) {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, []);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => { document.body.style.overflow = ""; };
  }, [open]);

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="fixed bottom-6 right-6 z-40 flex items-center gap-2 px-4 py-3 rounded-full font-semibold text-sm shadow-lg transition-transform hover:-translate-y-0.5"
        style={{
          background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)",
          color: "#fff",
          boxShadow: "0 20px 40px -12px rgba(251,70,4,0.55)",
        }}
        aria-label="Lezioni del modulo"
      >
        <List size={16} />
        <span className="hidden sm:inline">Lezioni del modulo</span>
      </button>

      <AnimatePresence>
        {open && (
          <>
            <motion.div
              key="overlay"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.2 }}
              onClick={() => setOpen(false)}
              className="fixed inset-0 z-50"
              style={{ background: "rgba(0,0,0,0.65)", backdropFilter: "blur(6px)" }}
            />
            <motion.aside
              key="drawer"
              role="dialog"
              aria-label="Lezioni del modulo"
              initial={{ x: "100%" }}
              animate={{ x: 0 }}
              exit={{ x: "100%" }}
              transition={{ duration: 0.32, ease: [0.22, 1, 0.36, 1] }}
              className="fixed top-0 right-0 bottom-0 z-50 w-full sm:w-[420px] flex flex-col"
              className="card-fill-silver" style={{
                borderLeft: "1px solid rgba(251,70,4,0.2)",
                boxShadow: "-30px 0 80px -20px rgba(0,0,0,0.8)",
              }}
            >
              <div className="flex items-center justify-between p-5 border-b" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
                <div className="min-w-0">
                  <div className="text-[10px] font-semibold tracking-widest uppercase" style={{ color: "#ff8a4a" }}>Modulo {module.index}</div>
                  <h3 className="text-base font-bold truncate" style={{ color: "#fafaf6" }}>{module.title}</h3>
                </div>
                <button
                  onClick={() => setOpen(false)}
                  className="w-9 h-9 rounded-full flex items-center justify-center flex-shrink-0"
                  style={{ background: "rgba(249,249,249,0.06)", color: "#fafaf6" }}
                  aria-label="Chiudi"
                >
                  <X size={16} />
                </button>
              </div>
              <div className="flex-1 overflow-y-auto p-3 flex flex-col gap-1.5">
                {module.lessons.map((l, i) => {
                  const active = l.id === activeLessonId;
                  return (
                    <Link
                      key={l.id}
                      href={`/corsi/${course.slug}/moduli/${module.slug}/${l.slug}`}
                      onClick={() => setOpen(false)}
                      className="flex items-center gap-3 p-3 rounded-xl transition-colors"
                      style={
                        active
                          ? { background: "rgba(251,70,4,0.16)", border: "1px solid rgba(251,70,4,0.45)" }
                          : { background: "rgba(249,249,249,0.03)", border: "1px solid rgba(249,249,249,0.06)" }
                      }
                    >
                      <div
                        className="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 text-xs font-bold"
                        style={{
                          background: completedIds.has(l.id) ? "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)" : "rgba(251,70,4,0.12)",
                          color: completedIds.has(l.id) ? "#fff" : "#ff8a4a",
                          border: completedIds.has(l.id) ? "1px solid #c9370a" : "1px solid rgba(251,70,4,0.3)",
                        }}
                      >
                        {completedIds.has(l.id) ? (
                          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                            <polyline points="20 6 9 17 4 12" />
                          </svg>
                        ) : active ? (
                          <Play size={11} fill="currentColor" />
                        ) : (
                          i + 1
                        )}
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="text-sm font-semibold truncate" style={{ color: active ? "#fafaf6" : "rgba(250,250,246,0.85)" }}>{l.title}</div>
                        <div className="text-[11px]" style={{ color: "rgba(250,250,246,0.5)" }}>{formatDuration(l.duration)}</div>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </motion.aside>
          </>
        )}
      </AnimatePresence>
    </>
  );
}
