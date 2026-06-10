import { cn } from "@/lib/utils";

export function HairlineGold({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "divider-hairline mx-auto max-w-3xl",
        className
      )}
      aria-hidden
    />
  );
}

export function HairlineSilver({ className }: { className?: string }) {
  return (
    <div
      className={cn(
        "divider-hairline-silver mx-auto max-w-3xl",
        className
      )}
      aria-hidden
    />
  );
}
