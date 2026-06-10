import AdminShell from "@/components/admin-shell";
import { createClient } from "@/lib/supabase/server";
import { deleteResource } from "@/app/admin/actions";
import DeleteResourceButton from "./delete-resource-button";

export default async function AdminResourcesPage() {
  const supabase = await createClient();
  const { data: resources } = await supabase
    .from("resources")
    .select("*, courses(title), lessons(title)")
    .order("sort_order");

  return (
    <AdminShell
      title="Risorse"
      subtitle="Tutti i file scaricabili della piattaforma"
    >
      <div className="card-dark !p-0 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-sm">
            <thead style={{ background: "rgba(249,249,249,0.03)" }}>
              <tr>
                <Th>File</Th>
                <Th>Tipo</Th>
                <Th>Dimensione</Th>
                <Th>Corso</Th>
                <Th>{""}</Th>
              </tr>
            </thead>
            <tbody>
              {resources && resources.length > 0 ? (
                resources.map((r) => (
                  <tr key={r.id} className="border-t" style={{ borderColor: "rgba(249,249,249,0.06)" }}>
                    <Td>
                      <div className="flex items-center gap-3">
                        <div
                          className="w-10 h-10 rounded-lg flex items-center justify-center text-xs font-bold"
                          style={{ background: "rgba(251,70,4,0.14)", color: "#ff8a4a", border: "1px solid rgba(251,70,4,0.35)" }}
                        >
                          {(r.type ?? "—").toUpperCase().slice(0, 3)}
                        </div>
                        <span className="font-semibold" style={{ color: "#f9f9f9" }}>{r.title}</span>
                      </div>
                    </Td>
                    <Td>
                      <span className="uppercase text-xs font-semibold" style={{ color: "rgba(249,249,249,0.6)" }}>{r.type}</span>
                    </Td>
                    <Td>
                      <span style={{ color: "rgba(249,249,249,0.65)" }}>{r.size_label ?? "—"}</span>
                    </Td>
                    <Td>
                      <span style={{ color: "rgba(249,249,249,0.65)" }}>{(r as any).courses?.title ?? "—"}</span>
                    </Td>
                    <Td>
                      <div className="flex items-center gap-3">
                        <a href={r.href} target="_blank" rel="noreferrer" className="text-xs font-semibold" style={{ color: "#ff8a4a" }}>
                          Scarica
                        </a>
                        <DeleteResourceButton resourceId={r.id} />
                      </div>
                    </Td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={5} className="px-5 py-10 text-center" style={{ color: "rgba(249,249,249,0.4)" }}>
                    Nessuna risorsa ancora. Carica file dai corsi.
                  </td>
                </tr>
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
