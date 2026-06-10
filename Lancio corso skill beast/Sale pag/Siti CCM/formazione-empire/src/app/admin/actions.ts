"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { createAdminClient } from "@/lib/supabase/admin";
import { createClient } from "@/lib/supabase/server";

// ============================================================
//  GUARD — verifica che l'utente sia autenticato e sia admin
// ============================================================

async function requireAdmin() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  const admin = createAdminClient();
  const { data: profile } = await admin
    .from("profiles")
    .select("role")
    .eq("id", user.id)
    .single();

  if (profile?.role !== "admin") redirect("/dashboard");
  return { admin, userId: user.id };
}

// ============================================================
//  COURSE ACTIONS
// ============================================================

export async function updateCourse(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const { admin } = await requireAdmin();
  const courseId = formData.get("courseId") as string;

  const { error } = await admin
    .from("courses")
    .update({
      title: formData.get("title"),
      subtitle: formData.get("subtitle"),
      tagline: formData.get("tagline"),
      description: formData.get("description"),
      status: formData.get("status"),
      sales_page_url: formData.get("salesPageUrl"),
      cover_url: formData.get("coverUrl"),
    })
    .eq("id", courseId);

  if (error) return { error: error.message };
  revalidatePath("/admin/corsi");
  revalidatePath(`/corsi/${formData.get("courseSlug")}`);
  return { success: "Corso aggiornato" };
}

// ============================================================
//  MODULE ACTIONS
// ============================================================

export async function createModule(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const { admin } = await requireAdmin();
  const courseId = formData.get("courseId") as string;
  const title = formData.get("title") as string;

  const slug = title
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

  const { error } = await admin.from("modules").insert({
    course_id: courseId,
    title,
    slug,
    subtitle: formData.get("subtitle") ?? null,
    description: formData.get("description") ?? null,
    sort_order: parseInt(formData.get("sortOrder") as string) || 999,
  });

  if (error) return { error: error.message };
  revalidatePath("/admin/corsi");
  return { success: "Modulo creato" };
}

export async function updateModule(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const { admin } = await requireAdmin();
  const moduleId = formData.get("moduleId") as string;

  const { error } = await admin
    .from("modules")
    .update({
      title: formData.get("title"),
      subtitle: formData.get("subtitle") ?? null,
      description: formData.get("description") ?? null,
    })
    .eq("id", moduleId);

  if (error) return { error: error.message };
  revalidatePath("/admin/corsi");
  return { success: "Modulo aggiornato" };
}

export async function deleteModule(
  moduleId: string
): Promise<{ error?: string }> {
  const { admin } = await requireAdmin();
  const { error } = await admin.from("modules").delete().eq("id", moduleId);
  if (error) return { error: error.message };
  revalidatePath("/admin/corsi");
  return {};
}

// ============================================================
//  LESSON ACTIONS
// ============================================================

export async function createLesson(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const { admin } = await requireAdmin();
  const moduleId = formData.get("moduleId") as string;
  const title = formData.get("title") as string;
  const slug = title
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

  const durationRaw = formData.get("duration") as string;
  const sortOrderRaw = formData.get("sortOrder") as string;

  const { error } = await admin.from("lessons").insert({
    module_id: moduleId,
    title,
    slug,
    description: formData.get("description") ?? null,
    long_description: formData.get("longDescription") ?? null,
    duration_minutes: durationRaw ? parseInt(durationRaw) : null,
    video_url: formData.get("videoUrl") ?? null,
    sort_order: sortOrderRaw ? parseInt(sortOrderRaw) : 999,
  });

  if (error) return { error: error.message };
  revalidatePath("/admin/corsi");
  return { success: "Lezione creata" };
}

export async function updateLesson(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const { admin } = await requireAdmin();
  const lessonId = formData.get("lessonId") as string;

  const durationRaw = formData.get("duration") as string;

  const { error } = await admin
    .from("lessons")
    .update({
      title: formData.get("title"),
      description: formData.get("description") ?? null,
      long_description: formData.get("longDescription") ?? null,
      duration_minutes: durationRaw ? parseInt(durationRaw) : null,
      video_url: formData.get("videoUrl") ?? null,
    })
    .eq("id", lessonId);

  if (error) return { error: error.message };
  revalidatePath("/admin/corsi");
  return { success: "Lezione aggiornata" };
}

export async function deleteLesson(
  lessonId: string
): Promise<{ error?: string }> {
  const { admin } = await requireAdmin();
  const { error } = await admin.from("lessons").delete().eq("id", lessonId);
  if (error) return { error: error.message };
  revalidatePath("/admin/corsi");
  return {};
}

// ============================================================
//  RESOURCE ACTIONS
// ============================================================

export async function createResource(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const { admin } = await requireAdmin();

  // Rispetta la constraint resources_owner_xor: solo uno dei tre FK valorizzato
  const courseId = (formData.get("courseId") as string) || null;
  const lessonId = (formData.get("lessonId") as string) || null;
  const moduleId = (formData.get("moduleId") as string) || null;

  const { error } = await admin.from("resources").insert({
    course_id: courseId,
    lesson_id: lessonId,
    module_id: moduleId,
    title: formData.get("title"),
    type: formData.get("type"),
    href: formData.get("href"),
    size_label: (formData.get("sizeLabel") as string) || null,
    sort_order: 999,
  });

  if (error) return { error: error.message };
  revalidatePath("/admin/risorse");
  return { success: "Risorsa creata" };
}

export async function deleteResource(
  resourceId: string
): Promise<{ error?: string }> {
  const { admin } = await requireAdmin();
  const { error } = await admin
    .from("resources")
    .delete()
    .eq("id", resourceId);
  if (error) return { error: error.message };
  revalidatePath("/admin/risorse");
  return {};
}

// ============================================================
//  STUDENTS / ADMIN VIEW
// ============================================================

export async function getAdminStudents() {
  const { admin } = await requireAdmin();

  const { data } = await admin
    .from("enrollments")
    .select(
      `
      user_id,
      enrolled_at,
      profiles (id, name, email, avatar_url),
      courses (id, title, slug)
    `
    )
    .order("enrolled_at", { ascending: false });

  return data ?? [];
}

// ============================================================
//  SETTINGS ACTIONS
//  Nota: la tabella app_settings non è nel migration 0001.
//  Creala con:
//    create table public.app_settings (
//      id uuid primary key default gen_random_uuid(),
//      platform_name text,
//      support_email text,
//      welcome_email_template text,
//      updated_at timestamptz not null default now()
//    );
// ============================================================

export async function saveSettings(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const { admin } = await requireAdmin();

  const { data: existing } = await admin
    .from("app_settings")
    .select("id")
    .limit(1)
    .maybeSingle();

  const settingsData = {
    platform_name: formData.get("platformName"),
    support_email: formData.get("supportEmail"),
    welcome_email_template: formData.get("welcomeEmailTemplate"),
  };

  let error;
  if (existing?.id) {
    ({ error } = await admin
      .from("app_settings")
      .update(settingsData)
      .eq("id", existing.id));
  } else {
    ({ error } = await admin.from("app_settings").insert(settingsData));
  }

  if (error) return { error: error.message };
  revalidatePath("/admin/impostazioni");
  return { success: "Impostazioni salvate" };
}

export async function getSettings() {
  const { admin } = await requireAdmin();
  const { data } = await admin
    .from("app_settings")
    .select("*")
    .limit(1)
    .maybeSingle();
  return data ?? {};
}
