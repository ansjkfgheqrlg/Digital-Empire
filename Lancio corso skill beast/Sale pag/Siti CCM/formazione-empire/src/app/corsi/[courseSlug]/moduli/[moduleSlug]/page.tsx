import { notFound, redirect } from "next/navigation";
import { getModule } from "@/lib/data";

export default async function ModuleIndexPage({
  params,
}: {
  params: Promise<{ courseSlug: string; moduleSlug: string }>;
}) {
  const { courseSlug, moduleSlug } = await params;
  const res = getModule(courseSlug, moduleSlug);
  if (!res) notFound();
  const { course, module } = res;
  const target = module.lessons.find((l) => !l.completed) ?? module.lessons[0];
  if (!target) redirect(`/corsi/${course.slug}`);
  redirect(`/corsi/${course.slug}/moduli/${module.slug}/${target.slug}`);
}
