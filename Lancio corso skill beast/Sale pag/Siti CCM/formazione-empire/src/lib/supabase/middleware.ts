import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

const PROTECTED_PREFIXES = ["/dashboard", "/corsi", "/admin", "/account"];
const AUTH_PAGES = ["/login", "/signup"];

// Regex per estrarre courseSlug da /corsi/[courseSlug] e sottopagine
const COURSE_ROUTE_RE = /^\/corsi\/([^/]+)/;

export async function updateSession(request: NextRequest) {
  let supabaseResponse = NextResponse.next({ request });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll();
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value }) =>
            request.cookies.set(name, value),
          );
          supabaseResponse = NextResponse.next({ request });
          cookiesToSet.forEach(({ name, value, options }) =>
            supabaseResponse.cookies.set(name, value, options),
          );
        },
      },
    },
  );

  // Refresh session (obbligatorio: non mettere codice tra createServerClient e getUser)
  const {
    data: { user },
  } = await supabase.auth.getUser();

  const pathname = request.nextUrl.pathname;
  const isProtected = PROTECTED_PREFIXES.some((p) => pathname.startsWith(p));
  const isAuthPage = AUTH_PAGES.some((p) => pathname.startsWith(p));

  // Non loggato + rotta protetta → login
  if (!user && isProtected) {
    const url = request.nextUrl.clone();
    url.pathname = "/login";
    url.searchParams.set("redirect", pathname);
    return NextResponse.redirect(url);
  }

  // Loggato + pagina auth → dashboard
  if (user && isAuthPage) {
    const url = request.nextUrl.clone();
    url.pathname = "/dashboard";
    return NextResponse.redirect(url);
  }

  // ============================================================
  //  ENROLLMENT GATE — /corsi/[courseSlug] e sottopagine
  //  Solo utenti iscritti al corso possono accedere.
  // ============================================================
  if (user) {
    const courseMatch = pathname.match(COURSE_ROUTE_RE);
    if (courseMatch) {
      const courseSlug = courseMatch[1];

      // Recupera il corso e verifica l'iscrizione in un'unica query
      const { data: course } = await supabase
        .from("courses")
        .select("id, sales_page_url")
        .eq("slug", courseSlug)
        .single();

      if (course) {
        const { data: enrollment } = await supabase
          .from("enrollments")
          .select("user_id")
          .eq("user_id", user.id)
          .eq("course_id", course.id)
          .maybeSingle();

        if (!enrollment) {
          // Non iscritto → redirect alla sales page (o homepage come fallback)
          const destination = course.sales_page_url ?? "/";
          return NextResponse.redirect(new URL(destination, request.url));
        }
      }
      // Se il corso non esiste, lascia passare (la page component restituirà 404)
    }
  }

  return supabaseResponse;
}
