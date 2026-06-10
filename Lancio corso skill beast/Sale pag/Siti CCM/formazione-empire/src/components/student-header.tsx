import { createClient } from "@/lib/supabase/server";
import StudentHeaderClient from "./student-header-client";

export default async function StudentHeader({
  inCourseTheme = false,
}: {
  inCourseTheme?: boolean;
}) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  // Il middleware protegge le rotte — qui user dovrebbe sempre esserci.
  // Fallback minimo per non far crashare in caso di race.
  if (!user) {
    return (
      <StudentHeaderClient
        user={{ name: "Studente", email: "" }}
        inCourseTheme={inCourseTheme}
      />
    );
  }

  const { data: profile } = await supabase
    .from("profiles")
    .select("name, email")
    .eq("id", user.id)
    .single();

  return (
    <StudentHeaderClient
      user={{
        name: profile?.name ?? user.email?.split("@")[0] ?? "Studente",
        email: profile?.email ?? user.email ?? "",
      }}
      inCourseTheme={inCourseTheme}
    />
  );
}
