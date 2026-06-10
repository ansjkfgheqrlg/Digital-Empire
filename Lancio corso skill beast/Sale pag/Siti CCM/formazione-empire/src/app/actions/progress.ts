"use server";

import { revalidatePath } from "next/cache";
import { createClient } from "@/lib/supabase/server";

export async function markLessonComplete(
  lessonId: string,
  courseSlug: string,
  moduleSlug: string,
  lessonSlug: string
): Promise<{ error?: string }> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return { error: "Non autenticato" };

  const { error } = await supabase.from("lesson_progress").upsert(
    {
      user_id: user.id,
      lesson_id: lessonId,
      completed: true,
      completed_at: new Date().toISOString(),
    },
    { onConflict: "user_id,lesson_id" }
  );

  if (error) return { error: error.message };

  revalidatePath(`/corsi/${courseSlug}/moduli/${moduleSlug}/${lessonSlug}`);
  revalidatePath(`/corsi/${courseSlug}`);
  revalidatePath("/dashboard");
  return {};
}

export async function unmarkLessonComplete(
  lessonId: string,
  courseSlug: string,
  moduleSlug: string,
  lessonSlug: string
): Promise<{ error?: string }> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return { error: "Non autenticato" };

  // La riga rimane ma torniamo completed = false (preserva watched_seconds)
  const { error } = await supabase
    .from("lesson_progress")
    .update({ completed: false, completed_at: null })
    .eq("user_id", user.id)
    .eq("lesson_id", lessonId);

  if (error) return { error: error.message };

  revalidatePath(`/corsi/${courseSlug}/moduli/${moduleSlug}/${lessonSlug}`);
  revalidatePath(`/corsi/${courseSlug}`);
  revalidatePath("/dashboard");
  return {};
}
