export function RibbonSvg() {
  return (
    <div className="w-full py-6" aria-hidden>
      <svg
        viewBox="0 0 1440 60"
        className="w-full h-[60px] block"
        preserveAspectRatio="none"
      >
        <defs>
          {/* Gradiente crema → navy: la firma del brand */}
          <linearGradient id="ribbonBrand" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%"   stopColor="#edeebe" stopOpacity="0" />
            <stop offset="20%"  stopColor="#edeebe" stopOpacity="0.7" />
            <stop offset="50%"  stopColor="#3a6bc0" stopOpacity="1" />
            <stop offset="80%"  stopColor="#062155" stopOpacity="0.7" />
            <stop offset="100%" stopColor="#062155" stopOpacity="0" />
          </linearGradient>
          {/* Gradiente navy → crema: ribbon speculare */}
          <linearGradient id="ribbonBrandSoft" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%"   stopColor="#062155" stopOpacity="0" />
            <stop offset="35%"  stopColor="#062155" stopOpacity="0.4" />
            <stop offset="65%"  stopColor="#edeebe" stopOpacity="0.4" />
            <stop offset="100%" stopColor="#edeebe" stopOpacity="0" />
          </linearGradient>
          {/* Glow radiale centro */}
          <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%"   stopColor="#edeebe" stopOpacity="0.9" />
            <stop offset="100%" stopColor="#3a6bc0" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Ribbon superiore: crema→navy */}
        <path
          d="M 0,30 Q 360,0 720,30 T 1440,30"
          stroke="url(#ribbonBrand)"
          strokeWidth="1.5"
          fill="none"
          opacity="0.65"
        />
        {/* Ribbon inferiore: navy→crema speculare */}
        <path
          d="M 0,30 Q 360,60 720,30 T 1440,30"
          stroke="url(#ribbonBrandSoft)"
          strokeWidth="1"
          fill="none"
          opacity="0.45"
        />
        {/* Ornamento centrale — dot crema con ring navy */}
        <circle cx="720" cy="30" r="4"  fill="#edeebe" opacity="0.90" />
        <circle cx="720" cy="30" r="9"  fill="none" stroke="#3a6bc0" strokeWidth="0.8" opacity="0.60" />
        <circle cx="720" cy="30" r="14" fill="none" stroke="#062155" strokeWidth="0.4" opacity="0.35" />
        {/* Micro-dots laterali */}
        <circle cx="480" cy="20" r="1.5" fill="#edeebe" opacity="0.40" />
        <circle cx="960" cy="40" r="1.5" fill="#062155" opacity="0.40" />
      </svg>
    </div>
  );
}
