-- ============================================================
-- Formazione Empire — Schema iniziale
-- Esegui questo SQL interamente nel SQL Editor di Supabase.
-- ============================================================

-- Estensioni
create extension if not exists "pgcrypto";

-- ============================================================
-- PROFILES (estensione di auth.users)
-- ============================================================
create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text not null unique,
  name text,
  avatar_url text,
  role text not null default 'student' check (role in ('student', 'admin')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Auto-create profile on signup
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into public.profiles (id, email, name)
  values (new.id, new.email, coalesce(new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)));
  return new;
end;
$$;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ============================================================
-- COURSES
-- ============================================================
create table public.courses (
  id uuid primary key default gen_random_uuid(),
  slug text not null unique,
  title text not null,
  subtitle text,
  tagline text,
  description text,
  cover_url text,
  sales_page_url text,
  status text not null default 'available' check (status in ('available', 'coming-soon', 'archived')),
  sort_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index courses_slug_idx on public.courses(slug);

-- ============================================================
-- MODULES
-- ============================================================
create table public.modules (
  id uuid primary key default gen_random_uuid(),
  course_id uuid not null references public.courses(id) on delete cascade,
  slug text not null,
  title text not null,
  subtitle text,
  description text,
  sort_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (course_id, slug)
);

create index modules_course_id_idx on public.modules(course_id);

-- ============================================================
-- LESSONS
-- ============================================================
create table public.lessons (
  id uuid primary key default gen_random_uuid(),
  module_id uuid not null references public.modules(id) on delete cascade,
  slug text not null,
  title text not null,
  description text,
  long_description text,
  duration_minutes int not null default 0,
  video_url text,
  sort_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (module_id, slug)
);

create index lessons_module_id_idx on public.lessons(module_id);

-- ============================================================
-- RESOURCES (allegati scaricabili: lesson / module / course)
-- Solo UNO dei tre fk può essere valorizzato per riga.
-- ============================================================
create table public.resources (
  id uuid primary key default gen_random_uuid(),
  course_id uuid references public.courses(id) on delete cascade,
  module_id uuid references public.modules(id) on delete cascade,
  lesson_id uuid references public.lessons(id) on delete cascade,
  title text not null,
  type text not null check (type in ('pdf', 'md', 'skill', 'zip', 'link')),
  size_label text,
  href text not null,
  sort_order int not null default 0,
  created_at timestamptz not null default now(),
  constraint resources_owner_xor check (
    (course_id is not null)::int + (module_id is not null)::int + (lesson_id is not null)::int = 1
  )
);

create index resources_course_id_idx on public.resources(course_id);
create index resources_module_id_idx on public.resources(module_id);
create index resources_lesson_id_idx on public.resources(lesson_id);

-- ============================================================
-- ENROLLMENTS (chi possiede quale corso)
-- ============================================================
create table public.enrollments (
  user_id uuid not null references public.profiles(id) on delete cascade,
  course_id uuid not null references public.courses(id) on delete cascade,
  enrolled_at timestamptz not null default now(),
  expires_at timestamptz,
  primary key (user_id, course_id)
);

create index enrollments_user_id_idx on public.enrollments(user_id);

-- ============================================================
-- LESSON PROGRESS (progresso per utente/lezione)
-- ============================================================
create table public.lesson_progress (
  user_id uuid not null references public.profiles(id) on delete cascade,
  lesson_id uuid not null references public.lessons(id) on delete cascade,
  completed boolean not null default false,
  completed_at timestamptz,
  watched_seconds int not null default 0,
  last_watched_at timestamptz,
  primary key (user_id, lesson_id)
);

create index lesson_progress_user_id_idx on public.lesson_progress(user_id);

-- ============================================================
-- TIMESTAMPS AUTO-UPDATE
-- ============================================================
create or replace function public.touch_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create trigger profiles_touch before update on public.profiles
  for each row execute function public.touch_updated_at();
create trigger courses_touch before update on public.courses
  for each row execute function public.touch_updated_at();
create trigger modules_touch before update on public.modules
  for each row execute function public.touch_updated_at();
create trigger lessons_touch before update on public.lessons
  for each row execute function public.touch_updated_at();

-- ============================================================
-- ROW LEVEL SECURITY
-- ============================================================
alter table public.profiles enable row level security;
alter table public.courses enable row level security;
alter table public.modules enable row level security;
alter table public.lessons enable row level security;
alter table public.resources enable row level security;
alter table public.enrollments enable row level security;
alter table public.lesson_progress enable row level security;

-- Helper: is admin?
create or replace function public.is_admin()
returns boolean
language sql stable security definer
set search_path = public
as $$
  select exists (
    select 1 from public.profiles
    where id = auth.uid() and role = 'admin'
  );
$$;

-- PROFILES: ognuno legge il proprio profilo; admin legge tutti; ognuno aggiorna il proprio
create policy profiles_self_read on public.profiles
  for select using (auth.uid() = id or public.is_admin());
create policy profiles_self_update on public.profiles
  for update using (auth.uid() = id);
create policy profiles_admin_all on public.profiles
  for all using (public.is_admin()) with check (public.is_admin());

-- COURSES: lettura pubblica (catalogo visibile a tutti); scrittura solo admin
create policy courses_public_read on public.courses
  for select using (true);
create policy courses_admin_write on public.courses
  for all using (public.is_admin()) with check (public.is_admin());

-- MODULES / LESSONS / RESOURCES: lettura pubblica
create policy modules_public_read on public.modules for select using (true);
create policy modules_admin_write on public.modules for all using (public.is_admin()) with check (public.is_admin());

create policy lessons_public_read on public.lessons for select using (true);
create policy lessons_admin_write on public.lessons for all using (public.is_admin()) with check (public.is_admin());

create policy resources_public_read on public.resources for select using (true);
create policy resources_admin_write on public.resources for all using (public.is_admin()) with check (public.is_admin());

-- ENROLLMENTS: utente vede i propri; admin vede/gestisce tutti
create policy enrollments_self_read on public.enrollments
  for select using (auth.uid() = user_id or public.is_admin());
create policy enrollments_admin_write on public.enrollments
  for all using (public.is_admin()) with check (public.is_admin());

-- LESSON_PROGRESS: utente legge/scrive solo il proprio
create policy lesson_progress_self on public.lesson_progress
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy lesson_progress_admin_read on public.lesson_progress
  for select using (public.is_admin());

-- ============================================================
-- VISTA COMODA: corsi con conteggi
-- ============================================================
create or replace view public.course_stats as
select
  c.id as course_id,
  c.slug,
  count(distinct m.id) as modules_count,
  count(distinct l.id) as lessons_count,
  coalesce(sum(l.duration_minutes), 0) as total_duration_minutes
from public.courses c
left join public.modules m on m.course_id = c.id
left join public.lessons l on l.module_id = m.id
group by c.id, c.slug;
