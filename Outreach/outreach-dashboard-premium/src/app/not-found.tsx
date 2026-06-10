import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-ink text-center px-8">
      <div className="pre-headline mb-6">Errore 404</div>
      <h1 className="text-8xl font-black mb-4" style={{ color: "rgba(255,255,255,0.07)" }}>404</h1>
      <p className="text-white/60 text-base mb-8 max-w-sm leading-relaxed">
        Questa pagina non esiste o è stata rimossa.
      </p>
      <Link href="/" className="btn-orange text-sm">
        Torna alla Dashboard
      </Link>
    </div>
  );
}
