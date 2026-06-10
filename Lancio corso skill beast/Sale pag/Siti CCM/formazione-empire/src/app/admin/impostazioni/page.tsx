import AdminShell from "@/components/admin-shell";
import { getSettings } from "@/app/admin/actions";
import SettingsForm from "./settings-form";

export default async function AdminSettingsPage() {
  const settings = await getSettings();

  return (
    <AdminShell title="Impostazioni" subtitle="Configurazione generale della piattaforma">
      <SettingsForm settings={settings} />
    </AdminShell>
  );
}
