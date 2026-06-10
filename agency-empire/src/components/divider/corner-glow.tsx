type Props = {
  variant?: "mini" | "full";
};

export function CornerGlow({ variant = "mini" }: Props) {
  if (variant === "full") {
    return (
      <>
        <span className="corner-bracket corner-tl" aria-hidden />
        <span className="corner-bracket corner-tr" aria-hidden />
        <span className="corner-bracket corner-bl" aria-hidden />
        <span className="corner-bracket corner-br" aria-hidden />
      </>
    );
  }
  return (
    <>
      <span className="corner-mini tl top-6 left-6" aria-hidden />
      <span className="corner-mini tr top-6 right-6" aria-hidden />
      <span className="corner-mini bl bottom-6 left-6" aria-hidden />
      <span className="corner-mini br bottom-6 right-6" aria-hidden />
    </>
  );
}
