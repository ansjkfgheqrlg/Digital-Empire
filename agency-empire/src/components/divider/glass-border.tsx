import { cn } from "@/lib/utils";

export function GlassBorder({ className }: { className?: string }) {
  return (
    <div
      className={cn("section-glass-top w-full", className)}
      style={{ height: 1 }}
      aria-hidden
    />
  );
}
