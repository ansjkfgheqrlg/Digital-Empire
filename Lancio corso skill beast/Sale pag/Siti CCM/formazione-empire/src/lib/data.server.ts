import { cache } from "react";
import { createClient } from "@/lib/supabase/server";
import type { Course, Module, Lesson, Resource } from "@/lib/data";

function mapResourceFromDB(row: any): Resource {
  return {
    id: row.id,
    title: row.title,
    type: row.type as Resource["type"],
    size: row.size_label ?? undefined,
    href: row.href,
  };
}

function mapLessonFromDB(row: any, completed = false): Lesson {
  return {
    id: row.id,
    slug: row.slug,
    title: row.title,
    description: row.description ?? "",
    longDescription: row.long_description ?? "",
    duration: row.duration_minutes ?? 0,
    videoUrl: row.video_url ?? undefined,
    resources: Array.isArray(row.resources)
      ? row.resources
          .sort((a: any, b: any) => a.sort_order - b.sort_order)
          .map(mapResourceFromDB)
      : [],
    completed,
  };
}

function mapModuleFromDB(row: any, index: number): Module {
  return {
    id: row.id,
    slug: row.slug,
    index,
    title: row.title,
    subtitle: row.subtitle ?? "",
    description: row.description ?? "",
    lessons: Array.isArray(row.lessons)
      ? row.lessons
          .sort((a: any, b: any) => a.sort_order - b.sort_order)
          .map((l: any) => mapLessonFromDB(l))
      : [],
  };
}

function mapCourseFromDB(row: any): Course {
  const modules: Module[] = Array.isArray(row.modules)
    ? row.modules
        .sort((a: any, b: any) => a.sort_order - b.sort_order)
        .map((m: any, i: number) => mapModuleFromDB(m, i))
    : [];

  const globalResources: Resource[] = Array.isArray(row.resources)
    ? row.resources
        .sort((a: any, b: any) => a.sort_order - b.sort_order)
        .map(mapResourceFromDB)
    : [];

  const totalLessons = modules.reduce((acc, m) => acc + m.lessons.length, 0);
  const totalDuration = modules.reduce(
    (acc, m) => acc + m.lessons.reduce((a, l) => a + l.duration, 0),
    0
  );

  return {
    id: row.id,
    slug: row.slug,
    title: row.title,
    subtitle: row.subtitle ?? "",
    tagline: row.tagline ?? "",
    description: row.description ?? "",
    cover: row.cover_url ?? undefined,
    owned: false,
    salesPageUrl: row.sales_page_url ?? undefined,
    modules,
    globalResources,
    totalLessons,
    totalDuration,
    status: (row.status as Course["status"]) ?? "available",
  };
}

export const fetchCourse = cache(async (slug: string): Promise<Course | null> => {
  const supabase = await createClient();
  const { data } = await supabase
    .from("courses")
    .select(`
      *,
      modules (
        *,
        lessons (
          *,
          resources (*)
        )
      ),
      resources (*)
    `)
    .eq("slug", slug)
    .single();

  if (!data) return null;
  return mapCourseFromDB(data);
});

export const fetchModule = cache(async (courseSlug: string, moduleSlug: string) => {
  const course = await fetchCourse(courseSlug);
  if (!course) return null;
  const mod = course.modules.find((m) => m.slug === moduleSlug) ?? null;
  if (!mod) return null;
  return { course, module: mod };
});

export const fetchLesson = cache(async (courseSlug: string, moduleSlug: string, lessonSlug: string) => {
  const result = await fetchModule(courseSlug, moduleSlug);
  if (!result) return null;
  const lesson = result.module.lessons.find((l) => l.slug === lessonSlug) ?? null;
  if (!lesson) return null;
  return { course: result.course, module: result.module, lesson };
});

export const fetchCourseProgress = cache(async (courseId: string, userId: string) => {
  const supabase = await createClient();

  const { data: course } = await supabase
    .from("courses")
    .select("modules(lessons(id))")
    .eq("id", courseId)
    .single();

  const allLessonIds: string[] =
    course?.modules?.flatMap((m: any) => m.lessons.map((l: any) => l.id)) ?? [];
  const total = allLessonIds.length;

  if (total === 0) return { completed: 0, total: 0, percentage: 0 };

  const { data: progress } = await supabase
    .from("lesson_progress")
    .select("lesson_id")
    .eq("user_id", userId)
    .eq("completed", true)
    .in("lesson_id", allLessonIds);

  const completed = progress?.length ?? 0;
  return {
    completed,
    total,
    percentage: Math.round((completed / total) * 100),
  };
});

export const getEnrolledCourses = cache(async (userId: string): Promise<Course[]> => {
  const supabase = await createClient();
  const { data } = await supabase
    .from("enrollments")
    .select("courses(*)")
    .eq("user_id", userId)
    .order("enrolled_at", { ascending: false });

  if (!data) return [];
  return (data as any[])
    .map((e) => (e.courses ? mapCourseFromDB({ ...e.courses, owned: true }) : null))
    .filter(Boolean) as Course[];
});
