"use client";

import { useActionState, useState, useTransition } from "react";
import type { Course, Module, Lesson } from "@/lib/data";
import { formatDuration } from "@/lib/utils";
import {
  updateCourse,
  createModule,
  updateModule,
  deleteModule,
  createLesson,
  updateLesson,
  deleteLesson,
} from "@/app/admin/actions";

// ─── Feedback helper ─────────────────────────────────────────
function Feedback({ state }: { state: { error?: string; success?: string } | null }) {
  if (!state) return null;
  if (state.error) return <p style={{ color: "#ff8a8a", fontSize: "0.8rem", marginTop: "0.375rem" }}>{state.error}</p>;
  if (state.success) return <p style={{ color: "#6fdca0", fontSize: "0.8rem", marginTop: "0.375rem" }}>{state.success}</p>;
  return null;
}

// ─── Label + Field ────────────────────────────────────────────
function Label({ children }: { children: React.ReactNode }) {
  return (
    <label className="block text-xs font-semibold uppercase tracking-widest mb-2" style={{ color: "rgba(249,249,249,0.55)" }}>
      {children}
    </label>
  );
}

function Field({ label, name, defaultValue, textarea }: { label: string; name: string; defaultValue?: string; textarea?: boolean }) {
  return (
    <div>
      <Label>{label}</Label>
      {textarea ? (
        <textarea name={name} defaultValue={defaultValue ?? ""} rows={4} className="input-field resize-none" />
      ) : (
        <input name={name} defaultValue={defaultValue ?? ""} className="input-field" />
      )}
    </div>
  );
}

// ─── Lesson Edit Form ─────────────────────────────────────────
function LessonEditForm({ lesson, onClose }: { lesson: Lesson; onClose: () => void }) {
  const [state, formAction, isPending] = useActionState(updateLesson, null);
  return (
    <form action={formAction} className="flex flex-col gap-3 p-3 rounded-lg" style={{ background: "rgba(249,249,249,0.04)", border: "1px solid rgba(249,249,249,0.1)" }}>
      <input type="hidden" name="lessonId" value={lesson.id} />
      <Field label="Titolo" name="title" defaultValue={lesson.title} />
      <Field label="Descrizione" name="description" defaultValue={lesson.description} />
      <Field label="Contenuto completo" name="longDescription" defaultValue={lesson.longDescription ?? ""} textarea />
      <Field label="URL Video (YouTube o MP4)" name="videoUrl" defaultValue={lesson.videoUrl ?? ""} />
      <div className="flex gap-3">
        <div className="flex-1">
          <Label>Durata (min)</Label>
          <input name="duration" type="number" defaultValue={lesson.duration ?? ""} className="input-field" />
        </div>
      </div>
      <div className="flex items-center gap-3">
        <button type="submit" disabled={isPending} className="btn-orange text-sm py-2 px-4">
          {isPending ? "Salvataggio..." : "Salva lezione"}
        </button>
        <button type="button" onClick={onClose} className="btn-ghost text-sm py-2 px-4">Annulla</button>
      </div>
      <Feedback state={state} />
    </form>
  );
}

// ─── Lesson Row ───────────────────────────────────────────────
function LessonRow({ lesson, index }: { lesson: Lesson; index: number }) {
  const [editing, setEditing] = useState(false);
  const [, startTransition] = useTransition();

  const handleDelete = () => {
    if (window.confirm(`Eliminare la lezione "${lesson.title}"?`)) {
      startTransition(async () => { await deleteLesson(lesson.id); });
    }
  };

  return (
    <div className="flex flex-col gap-2">
      <div
        className="flex items-center gap-3 p-3 rounded-lg"
        style={{ background: "rgba(249,249,249,0.03)", border: "1px solid rgba(249,249,249,0.06)" }}
      >
        <div
          className="w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0"
          style={{ background: "rgba(249,249,249,0.08)", color: "rgba(249,249,249,0.8)" }}
        >
          {index + 1}
        </div>
        <div className="flex-1 min-w-0">
          <div className="text-sm font-semibold truncate" style={{ color: "#f9f9f9" }}>{lesson.title}</div>
          <div className="text-xs truncate" style={{ color: "rgba(249,249,249,0.55)" }}>{lesson.description}</div>
        </div>
        <div className="text-xs flex items-center gap-3" style={{ color: "rgba(249,249,249,0.5)" }}>
          <span>{formatDuration(lesson.duration)}</span>
        </div>
        <button onClick={() => setEditing(!editing)} className="text-xs font-semibold px-3 py-1.5 rounded-lg" style={{ color: "#ff8a4a", background: "transparent", border: "1px solid rgba(251,70,4,0.3)" }}>
          {editing ? "Chiudi" : "Modifica"}
        </button>
        <button onClick={handleDelete} className="text-xs font-semibold" style={{ color: "#ff8a8a" }}>
          Elimina
        </button>
      </div>
      {editing && <LessonEditForm lesson={lesson} onClose={() => setEditing(false)} />}
    </div>
  );
}

// ─── Add Lesson Form ──────────────────────────────────────────
function AddLessonForm({ moduleId, onSuccess }: { moduleId: string; onSuccess: () => void }) {
  const [state, formAction, isPending] = useActionState(
    async (prev: any, fd: FormData) => {
      const result = await createLesson(prev, fd);
      if (result?.success) onSuccess();
      return result;
    },
    null
  );

  return (
    <form action={formAction} className="flex flex-col gap-3 p-4 rounded-xl mt-2" style={{ background: "rgba(251,70,4,0.06)", border: "1px dashed rgba(251,70,4,0.3)" }}>
      <input type="hidden" name="moduleId" value={moduleId} />
      <p className="text-xs font-semibold uppercase tracking-widest" style={{ color: "#ff8a4a" }}>Nuova lezione</p>
      <Field label="Titolo *" name="title" />
      <Field label="Descrizione" name="description" />
      <Field label="URL Video" name="videoUrl" />
      <div>
        <Label>Durata (min)</Label>
        <input name="duration" type="number" className="input-field" placeholder="20" />
      </div>
      <div className="flex gap-3">
        <button type="submit" disabled={isPending} className="btn-orange text-sm py-2 px-4">
          {isPending ? "Creazione..." : "Crea lezione"}
        </button>
      </div>
      <Feedback state={state} />
    </form>
  );
}

// ─── Module Accordion ─────────────────────────────────────────
function ModuleAccordion({
  mod,
  isExpanded,
  onToggle,
}: {
  mod: Module;
  isExpanded: boolean;
  onToggle: () => void;
}) {
  const [updateState, updateAction, isUpdating] = useActionState(updateModule, null);
  const [showAddLesson, setShowAddLesson] = useState(false);
  const [, startTransition] = useTransition();

  const handleDelete = () => {
    if (window.confirm(`Eliminare il modulo "${mod.title}" e tutte le sue lezioni?`)) {
      startTransition(async () => { await deleteModule(mod.id); });
    }
  };

  return (
    <div className="card-dark !p-0 overflow-hidden">
      <div
        className="flex items-center gap-4 p-5 cursor-pointer transition-colors"
        onClick={onToggle}
      >
        <div
          className="w-12 h-12 rounded-xl flex items-center justify-center text-lg font-extrabold flex-shrink-0"
          style={{ background: "rgba(251,70,4,0.14)", color: "#ff8a4a", border: "1px solid rgba(251,70,4,0.35)" }}
        >
          {mod.index.toString().padStart(2, "0")}
        </div>
        <div className="flex-1 min-w-0">
          <div className="text-xs font-semibold uppercase tracking-widest mb-0.5" style={{ color: "#ff8a4a" }}>
            Modulo {mod.index}
          </div>
          <h3 className="text-base font-bold truncate" style={{ color: "#f9f9f9" }}>{mod.title}</h3>
          <div className="text-xs mt-1" style={{ color: "rgba(249,249,249,0.55)" }}>
            {mod.lessons.length} lezioni · {formatDuration(mod.lessons.reduce((a, l) => a + l.duration, 0))}
          </div>
        </div>
        <svg
          width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"
          style={{ color: "rgba(249,249,249,0.5)", transform: isExpanded ? "rotate(180deg)" : "none", transition: "transform 0.2s" }}
        >
          <polyline points="6 9 12 15 18 9" />
        </svg>
      </div>

      {isExpanded && (
        <div className="border-t" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
          {/* Module edit form */}
          <form action={updateAction} className="p-5 grid md:grid-cols-2 gap-4 border-b" style={{ borderColor: "rgba(249,249,249,0.08)" }}>
            <input type="hidden" name="moduleId" value={mod.id} />
            <Field label="Titolo" name="title" defaultValue={mod.title} />
            <Field label="Sottotitolo" name="subtitle" defaultValue={mod.subtitle ?? ""} />
            <div className="md:col-span-2">
              <Field label="Descrizione" name="description" defaultValue={mod.description ?? ""} textarea />
            </div>
            <div className="md:col-span-2 flex items-center gap-3">
              <button type="submit" disabled={isUpdating} className="btn-orange py-2 px-4 text-sm">
                {isUpdating ? "Salvataggio..." : "Salva modulo"}
              </button>
              <button type="button" onClick={handleDelete} className="btn-ghost py-2 px-4 text-sm" style={{ color: "#ff8a8a", borderColor: "rgba(255,138,138,0.3)" }}>
                Elimina modulo
              </button>
            </div>
            <div className="md:col-span-2"><Feedback state={updateState} /></div>
          </form>

          {/* Lessons */}
          <div className="px-5 py-4">
            <div className="flex items-center justify-between mb-3">
              <h4 className="text-sm font-semibold" style={{ color: "#f9f9f9" }}>Lezioni</h4>
              <button
                onClick={() => setShowAddLesson(!showAddLesson)}
                className="text-xs font-semibold px-3 py-1.5 rounded-lg"
                style={{ background: "rgba(251,70,4,0.14)", color: "#ff8a4a", border: "1px solid rgba(251,70,4,0.35)" }}
              >
                {showAddLesson ? "Annulla" : "+ Aggiungi lezione"}
              </button>
            </div>
            <div className="flex flex-col gap-2">
              {mod.lessons.map((l, i) => (
                <LessonRow key={l.id} lesson={l} index={i} />
              ))}
            </div>
            {showAddLesson && (
              <AddLessonForm moduleId={mod.id} onSuccess={() => setShowAddLesson(false)} />
            )}
          </div>
        </div>
      )}
    </div>
  );
}

// ─── Add Module Form ──────────────────────────────────────────
function AddModuleForm({ courseId, onSuccess }: { courseId: string; onSuccess: () => void }) {
  const [state, formAction, isPending] = useActionState(
    async (prev: any, fd: FormData) => {
      const result = await createModule(prev, fd);
      if (result?.success) onSuccess();
      return result;
    },
    null
  );

  return (
    <form action={formAction} className="card-dark flex flex-col gap-4">
      <input type="hidden" name="courseId" value={courseId} />
      <p className="text-sm font-bold" style={{ color: "#ff8a4a" }}>Nuovo modulo</p>
      <Field label="Titolo *" name="title" />
      <Field label="Sottotitolo" name="subtitle" />
      <Field label="Descrizione" name="description" textarea />
      <div className="flex gap-3">
        <button type="submit" disabled={isPending} className="btn-orange py-2 px-4 text-sm">
          {isPending ? "Creazione..." : "Crea modulo"}
        </button>
        <button type="button" onClick={onSuccess} className="btn-ghost py-2 px-4 text-sm">Annulla</button>
      </div>
      <Feedback state={state} />
    </form>
  );
}

// ─── Main CourseEditor ────────────────────────────────────────
export default function CourseEditor({ course }: { course: Course }) {
  const [tab, setTab] = useState<"info" | "moduli" | "risorse">("moduli");
  const [expandedModule, setExpandedModule] = useState<string | null>(
    course.modules[0]?.id ?? null
  );
  const [showAddModule, setShowAddModule] = useState(false);
  const [infoState, infoFormAction, isInfoPending] = useActionState(updateCourse, null);

  return (
    <div className="flex flex-col gap-6">
      {/* Tabs */}
      <div
        className="flex items-center gap-2 p-1 rounded-xl self-start"
        style={{ background: "rgba(249,249,249,0.05)", border: "1px solid rgba(249,249,249,0.1)" }}
      >
        {(
          [
            ["info", "Informazioni"],
            ["moduli", `Moduli (${course.modules.length})`],
            ["risorse", `Risorse (${course.globalResources.length})`],
          ] as const
        ).map(([key, label]) => (
          <button
            key={key}
            onClick={() => setTab(key)}
            className="px-4 py-2 rounded-lg text-sm font-semibold transition-colors"
            style={
              tab === key
                ? { background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)", color: "#ffffff", boxShadow: "0 4px 14px -4px rgba(251,70,4,0.45)" }
                : { background: "transparent", color: "rgba(249,249,249,0.6)" }
            }
          >
            {label}
          </button>
        ))}
      </div>

      {/* ── Tab Info ── */}
      {tab === "info" && (
        <form action={infoFormAction} className="card-dark flex flex-col gap-5">
          <input type="hidden" name="courseId" value={course.id} />
          <input type="hidden" name="courseSlug" value={course.slug} />
          <Field label="Titolo" name="title" defaultValue={course.title} />
          <Field label="Sottotitolo" name="subtitle" defaultValue={course.subtitle} />
          <Field label="Tagline" name="tagline" defaultValue={course.tagline} />
          <Field label="Descrizione" name="description" defaultValue={course.description} textarea />
          <div className="flex gap-4">
            <div className="flex-1">
              <Label>Status</Label>
              <select name="status" defaultValue={course.status} className="input-field">
                <option value="available">Pubblicato</option>
                <option value="coming-soon">In arrivo (draft)</option>
              </select>
            </div>
          </div>
          <Field label="URL immagine di copertina" name="coverUrl" defaultValue={course.cover ?? ""} />
          <Field label="URL Sales Page" name="salesPageUrl" defaultValue={course.salesPageUrl ?? ""} />
          <div className="flex items-center gap-3 pt-2">
            <button type="submit" disabled={isInfoPending} className="btn-orange py-2.5 px-6">
              {isInfoPending ? "Salvataggio..." : "Salva informazioni"}
            </button>
          </div>
          <Feedback state={infoState} />
        </form>
      )}

      {/* ── Tab Moduli ── */}
      {tab === "moduli" && (
        <div className="flex flex-col gap-4">
          {course.modules.map((mod) => (
            <ModuleAccordion
              key={mod.id}
              mod={mod}
              isExpanded={expandedModule === mod.id}
              onToggle={() => setExpandedModule(expandedModule === mod.id ? null : mod.id)}
            />
          ))}

          {showAddModule ? (
            <AddModuleForm
              courseId={course.id}
              onSuccess={() => setShowAddModule(false)}
            />
          ) : (
            <button
              onClick={() => setShowAddModule(true)}
              className="card-dark !p-5 text-center transition-all"
              style={{ borderStyle: "dashed", borderColor: "rgba(251,70,4,0.4)", color: "#ff8a4a" }}
            >
              <div className="flex items-center justify-center gap-2 font-semibold">
                <span className="text-xl">+</span>
                Aggiungi nuovo modulo
              </div>
            </button>
          )}
        </div>
      )}

      {/* ── Tab Risorse ── */}
      {tab === "risorse" && (
        <div className="card-dark">
          <div className="flex items-center justify-between mb-5">
            <div>
              <h3 className="text-base font-bold" style={{ color: "#f9f9f9" }}>
                Risorse globali del corso
              </h3>
              <p className="text-xs mt-1" style={{ color: "rgba(249,249,249,0.55)" }}>
                File scaricabili dalla pagina corso (non legati a una lezione specifica).
              </p>
            </div>
          </div>
          <div className="flex flex-col gap-2">
            {course.globalResources.map((r) => (
              <div
                key={r.id}
                className="flex items-center gap-4 p-3 rounded-lg"
                style={{ background: "rgba(249,249,249,0.03)", border: "1px solid rgba(249,249,249,0.06)" }}
              >
                <div
                  className="w-10 h-10 rounded-lg flex items-center justify-center text-xs font-bold"
                  style={{ background: "rgba(251,70,4,0.14)", color: "#ff8a4a", border: "1px solid rgba(251,70,4,0.35)" }}
                >
                  {r.type.toUpperCase()}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="text-sm font-semibold truncate" style={{ color: "#f9f9f9" }}>{r.title}</div>
                  <div className="text-xs" style={{ color: "rgba(249,249,249,0.55)" }}>{r.size}</div>
                </div>
                <a href={r.href} target="_blank" rel="noreferrer" className="text-xs font-semibold" style={{ color: "#ff8a4a" }}>
                  Scarica
                </a>
              </div>
            ))}
            {course.globalResources.length === 0 && (
              <p style={{ color: "rgba(249,249,249,0.4)", fontSize: "0.875rem" }}>Nessuna risorsa globale. Caricale dalla pagina Risorse.</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
