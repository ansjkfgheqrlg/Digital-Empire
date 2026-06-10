"use client";

import { useTransition } from "react";
import { deleteResource } from "@/app/admin/actions";

export default function DeleteResourceButton({ resourceId }: { resourceId: string }) {
  const [, startTransition] = useTransition();

  const handleDelete = () => {
    if (window.confirm("Eliminare questa risorsa?")) {
      startTransition(async () => {
        await deleteResource(resourceId);
      });
    }
  };

  return (
    <button onClick={handleDelete} className="text-xs font-semibold" style={{ color: "#ff8a8a" }}>
      Elimina
    </button>
  );
}
