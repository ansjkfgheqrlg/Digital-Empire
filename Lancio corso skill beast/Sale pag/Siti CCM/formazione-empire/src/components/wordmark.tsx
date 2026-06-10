import Link from "next/link";
import { cn } from "@/lib/utils";

type Props = { href?: string; size?: "sm" | "md" | "lg"; className?: string };

const sizes = {
  sm: "text-lg",
  md: "text-2xl",
  lg: "text-4xl md:text-5xl",
};

export default function Wordmark({ href = "/", size = "md", className }: Props) {
  return (
    <Link href={href} className={cn("wordmark", sizes[size], className)}>
      <span className="wm-formazione">Formazione</span>
      <span className="wm-empire">Empire</span>
    </Link>
  );
}
