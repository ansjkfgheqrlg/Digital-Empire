import AdminShell from "@/components/admin-shell";
import { getAdminStudents } from "@/app/admin/actions";

const statusLabels: Record<string, { label: string; bg: string; color: string; border: string }> = {
  active: { label: "Attivo", bg: "rgba(80, 180, 120, 0.12)", color: "#6fdca0", border: "rgba(111, 220, 160, 0.25)" },
  completed: { label: "Completato", bg: "rgba(251,70,4,0.15)", color: "#ff8a4a", border: "rgba(251,70,4,0.3)" },
  inactive: { label: "Inattivo", bg: "rgba(249,249,249,0.06)", color: "rgba(249,249,249,0.6)", border: "rgba(249,249,249,0.1)" },
};

export default async function AdminStudentsPage() {
  const students = await getAdminStudents();

  return (
    <AdminShell
      title="Studenti"
      subtitle={`${students.length} studenti iscritti ai corsi`}
      actions={
        <>
          <button className="btn-ghost">Esporta CSV</button>
        </>
      }
    >
      {/* Filter bar */}
      <div className="flex flex-col md:flex-row gap-3 mb-6">
        <input placeholder="Cerca per nome o email..." className="input-field flex-1" />
        <select className="input-field md:w-52">
          <option>Tutti i corsi</option>
        </select>
      </div>

      {/* Table */}
      <div className="card-dark !p-0 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead style={{ background: "rgba(249,249,249,0.03)" }}>
              <tr>
                <Th>Studente</Th>
                <Th>Corso</Th>
                <Th>Data iscrizione</Th>
                <Th>{""}</Th>
              </tr>
            </thead>
            <tbody>
              {students.length === 0 ? (
                <tr>
                  <td colSpan={4} className="px-5 py-10 text-center" style={{ color: "rgba(249,249,249,0.4)" }}>
                    Nessuno studente ancora.
                  </td>
                </tr>
              ) : (
                students.map((e: any) => (
                  <tr
                    key={e.id}
                    className="border-t transition-colors"
                    style={{ borderColor: "rgba(249,249,249,0.06)" }}
                  >
                    <Td>
                      <div className="flex items-center gap-3">
                        <div
                          className="w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0"
                          style={{ background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)", color: "#ffffff" }}
                        >
                          {(e.profiles?.name ?? e.profiles?.email ?? "?").charAt(0).toUpperCase()}
                        </div>
                        <div className="min-w-0">
                          <div className="font-semibold truncate" style={{ color: "#f9f9f9" }}>
                            {e.profiles?.name ?? "—"}
                          </div>
                          <div className="text-xs truncate" style={{ color: "rgba(249,249,249,0.55)" }}>
                            {e.profiles?.email ?? "—"}
                          </div>
                        </div>
                      </div>
                    </Td>
                    <Td>
                      <span style={{ color: "rgba(249,249,249,0.65)" }}>{e.courses?.title ?? "—"}</span>
                    </Td>
                    <Td>
                      <span style={{ color: "rgba(249,249,249,0.65)" }}>
                        {e.enrolled_at ? new Date(e.enrolled_at).toLocaleDateString("it-IT") : "—"}
                      </span>
                    </Td>
                    <Td>
                      <button className="text-xs font-semibold" style={{ color: "#ff8a4a" }}>
                        Dettagli →
                      </button>
                    </Td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </AdminShell>
  );
}

function Th({ children }: { children: React.ReactNode }) {
  return (
    <th className="text-left px-5 py-3 text-xs font-semibold uppercase tracking-widest" style={{ color: "rgba(249,249,249,0.55)" }}>
      {children}
    </th>
  );
}
function Td({ children }: { children: React.ReactNode }) {
  return <td className="px-5 py-4">{children}</td>;
}
