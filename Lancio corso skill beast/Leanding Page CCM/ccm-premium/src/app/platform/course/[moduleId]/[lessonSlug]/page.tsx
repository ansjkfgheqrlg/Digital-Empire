import { courseData } from "@/lib/course-data";
import { LessonClient } from "./lesson-client";

export function generateStaticParams() {
  return courseData.flatMap((mod) =>
    mod.lessons.map((lesson) => ({ moduleId: mod.id, lessonSlug: lesson.slug }))
  );
}

export default function LessonPage() {
  return <LessonClient />;
}
