
import React from 'react';

export type ButtonVariant = 'gold' | 'cyan' | 'purple' | 'emerald' | 'silver' | 'silverGreen';

interface GoldButtonProps {
  children: React.ReactNode;
  onClick?: (e?: React.MouseEvent) => void;
  fullWidth?: boolean;
  href?: string;
  className?: string;
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
  variant?: ButtonVariant;
}

export const GoldButton: React.FC<GoldButtonProps> = ({ 
  children, 
  onClick, 
  fullWidth = false, 
  href, 
  className = "", 
  type = "button", 
  disabled = false,
  variant = 'gold'
}) => {

  const variantStyles: Record<ButtonVariant, string> = {
    // ARGENTO DORATO (Realistico, Metallico, High-End)
    gold: `
      bg-gradient-to-b from-[#FFFFFF] via-[#F3EFDE] to-[#DBCBA8]
      text-[#2A2312]
      border border-[#BFA97C]
      shadow-[inset_0_1px_0_0_rgba(255,255,255,1),0_2px_4px_rgba(0,0,0,0.3)]
      hover:shadow-[inset_0_1px_0_0_rgba(255,255,255,1),0_12px_24px_rgba(0,0,0,0.4)]
      hover:bg-gradient-to-b hover:from-[#FFFFFF] hover:via-[#F9F6EB] hover:to-[#E3D4B5]
    `,
    // VERDE ARGENTATO (Premium Silver-Green)
    silverGreen: `
      bg-gradient-to-b from-[#FFFFFF] via-[#E8F3EE] to-[#B0CDC5]
      text-[#022c22]
      border border-[#8EAEA5]
      shadow-[inset_0_1px_0_0_rgba(255,255,255,1),0_2px_4px_rgba(0,0,0,0.3)]
      hover:shadow-[inset_0_1px_0_0_rgba(255,255,255,1),0_12px_24px_rgba(5,150,105,0.4)]
      hover:bg-gradient-to-b hover:from-[#FFFFFF] hover:via-[#F0F9F6] hover:to-[#C1E0D7]
    `,
    cyan: `
      bg-gradient-to-b from-[#E0F7FA] via-[#B2EBF2] to-[#4DD0E1]
      text-[#004D40]
      border border-[#26C6DA]
      shadow-[inset_0_1px_0_0_rgba(255,255,255,0.8),0_2px_4px_rgba(0,0,0,0.3)]
      hover:shadow-[inset_0_1px_0_0_rgba(255,255,255,0.8),0_12px_24px_rgba(0,0,0,0.4)]
    `,
    purple: `
      bg-gradient-to-b from-[#F3E5F5] via-[#E1BEE7] to-[#BA68C8]
      text-[#4A148C]
      border border-[#AB47BC]
      shadow-[inset_0_1px_0_0_rgba(255,255,255,0.8),0_2px_4px_rgba(0,0,0,0.3)]
      hover:shadow-[inset_0_1px_0_0_rgba(255,255,255,0.8),0_12px_24px_rgba(0,0,0,0.4)]
    `,
    emerald: `
      bg-gradient-to-b from-[#E8F5E9] via-[#C8E6C9] to-[#66BB6A]
      text-[#1B5E20]
      border border-[#4CAF50]
      shadow-[inset_0_1px_0_0_rgba(255,255,255,0.8),0_2px_4px_rgba(0,0,0,0.3)]
      hover:shadow-[inset_0_1px_0_0_rgba(255,255,255,0.8),0_12px_24px_rgba(0,0,0,0.4)]
    `,
    silver: `
      bg-gradient-to-b from-[#F8FAFC] via-[#E2E8F0] to-[#94A3B8]
      text-[#0F172A]
      border border-[#CBD5E1]
      shadow-[inset_0_1px_0_0_rgba(255,255,255,0.9),0_2px_4px_rgba(0,0,0,0.3)]
      hover:shadow-[inset_0_1px_0_0_rgba(255,255,255,0.9),0_12px_24px_rgba(0,0,0,0.4)]
    `
  };

  const baseClasses = `
    relative 
    px-10 py-5 
    font-sans font-extrabold tracking-[0.2em] lowercase text-xs
    rounded-[2px] 
    cursor-pointer
    transition-all duration-300 ease-out
    flex items-center justify-center gap-3
    transform
    hover:-translate-y-[2px]
    active:translate-y-[1px] active:shadow-[inset_0_2px_4px_rgba(0,0,0,0.1)]
    ${fullWidth ? 'w-full' : 'w-auto'}
    ${disabled ? 'opacity-70 cursor-not-allowed grayscale' : ''}
    ${variantStyles[variant]}
    ${className}
  `;

  const handleLinkClick = (e: React.MouseEvent<HTMLAnchorElement>) => {
    if (href?.startsWith('#')) {
      e.preventDefault();
      const targetId = href.substring(1);
      const element = document.getElementById(targetId);
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
      }
    }
    if (onClick) onClick(e);
  };

  // Contenuto interno con leggera ombra per dare profondità al testo inciso
  const InnerContent = () => (
    <span className="relative z-10 flex items-center gap-3 drop-shadow-[0_1px_0_rgba(255,255,255,0.4)]">
      {children}
    </span>
  );

  if (href) {
    return (
      <a href={href} onClick={handleLinkClick} className={baseClasses}>
        <InnerContent />
      </a>
    );
  }

  return (
    <button type={type} onClick={onClick} disabled={disabled} className={baseClasses}>
      <InnerContent />
    </button>
  );
};
