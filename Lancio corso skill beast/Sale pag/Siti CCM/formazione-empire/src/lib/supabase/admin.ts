import { createClient } from "@supabase/supabase-js";

// ⚠️ SERVER ONLY — usa la service_role key, bypassa RLS.
// Non importare mai in un componente client.
export function createAdminClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    {
      auth: {
        persistSession: false,
        autoRefreshToken: false,
      },
    },
  );
}
