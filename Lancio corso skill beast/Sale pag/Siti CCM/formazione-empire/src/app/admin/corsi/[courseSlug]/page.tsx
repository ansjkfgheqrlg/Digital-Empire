import Link from "next/link";
import { notFound } from "next/navigation";
import AdminShell from "@/components/admin-shell";
import { fetchCourse } from "@/lib/data.server";
import CourseEditor from "./course-editor";

export default async function AdminCoursePage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const course = await fetchCourse(courseSlug);
  if (!course) notFound();

  return (
    <AdminShell
      title={course.title}
      subtitle="Modifica il corso, i moduli e le lezioni"
      actions={
        <>
          <Link href={`/corsi/${course.slug}`} target="_blank" className="btn-ghost">
            Vedi sul sito
          </Link>
        </>
      }
    >
      <CourseEditor course={course} />
    </AdminShell>
  );
}
