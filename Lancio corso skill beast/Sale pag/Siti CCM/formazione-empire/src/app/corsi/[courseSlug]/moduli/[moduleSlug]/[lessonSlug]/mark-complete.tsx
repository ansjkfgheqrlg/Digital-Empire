"use client";

import { useState, useTransition } from "react";
import { markLessonComplete, unmarkLessonComplete } from "@/app/actions/progress";

interface MarkCompleteProps {
  lessonId: string;
  courseSlug: string;
  moduleSlug: string;
  lessonSlug: string;
  initialCompleted: boolean;
}

export default function MarkCompleteButton({
  lessonId,
  courseSlug,
  moduleSlug,
  lessonSlug,
  initialCompleted,
}: MarkCompleteProps) {
  const [optimistic, setOptimistic] = useState(initialCompleted);
  const [isPending, startTransition] = useTransition();

  const toggle = () => {
    const next = !optimistic;
    setOptimistic(next);
    startTransition(async () => {
      const result = next
        ? await markLessonComplete(lessonId, courseSlug, moduleSlug, lessonSlug)
        : await unmarkLessonComplete(lessonId, courseSlug, moduleSlug, lessonSlug);
      if (result?.error) setOptimistic(!next);
    });
  };

  return (
    <button
      onClick={toggle}
      disabled={isPending}
      className={optimistic ? "btn-ghost" : "btn-orange"}
      style={
        optimistic
          ? { background: "rgba(251,70,4,0.12)", color: "#fb4604", borderColor: "rgba(251,70,4,0.35)" }
          : undefined
      }
    >
      {optimistic ? (
        <>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="20 6 9 17 4 12" />
          </svg>
          Completata
        </>
      ) : (
        <>
          {isPending ? "..." : "Segna come completata"}
          {!isPending && <span aria-hidden>→</span>}
        </>
      )}
    </button>
  );
}
