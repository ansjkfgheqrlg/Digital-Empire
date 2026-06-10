"use server";

import { revalidatePath } from "next/cache";
import { createClient } from "@/lib/supabase/server";

export async function updateProfile(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return { error: "Non autenticato" };

  const name = (formData.get("name") as string)?.trim();
  if (!name) return { error: "Il nome non può essere vuoto" };

  const { error } = await supabase
    .from("profiles")
    .update({ name })
    .eq("id", user.id);

  if (error) return { error: error.message };
  revalidatePath("/account");
  return { success: "Profilo aggiornato" };
}

export async function changePassword(
  prevState: any,
  formData: FormData
): Promise<{ success?: string; error?: string }> {
  const password = formData.get("password") as string;
  const confirmPassword = formData.get("confirmPassword") as string;

  if (password !== confirmPassword) return { error: "Le password non coincidono" };
  if (password.length < 8) return { error: "La password deve essere di almeno 8 caratteri" };

  const supabase = await createClient();
  const { error } = await supabase.auth.updateUser({ password });

  if (error) return { error: error.message };
  return { success: "Password aggiornata con successo" };
}
