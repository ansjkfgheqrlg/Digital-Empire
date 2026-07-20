
import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost' | 'diamond' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  icon?: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({ 
  children, 
  variant = 'primary', 
  size = 'md', 
  className = '', 
  icon,
  ...props 
}) => {
  const baseStyles = "inline-flex items-center justify-center font-bold tracking-wide transition-all duration-200 focus:outline-none disabled:opacity-50 disabled:cursor-not-allowed border shadow-sm relative overflow-hidden";
  
  // Sharp borders for enterprise feel
  const radius = "rounded-sm";

  const variants = {
    // True Silver Gradient - Removed white glow, replaced with standard shadow
    primary: `bg-silver-gradient text-surface-900 border-transparent hover:brightness-110 hover:shadow-md active:scale-[0.98]`,
    
    secondary: `bg-surface-800 text-platinum-200 border-surface-border hover:bg-surface-700 hover:border-platinum-500 hover:text-white`,
    
    outline: `bg-transparent border-platinum-500 text-platinum-200 hover:bg-platinum-500/10 hover:text-white`,
    
    ghost: `bg-transparent border-transparent text-platinum-400 hover:text-white hover:bg-surface-800 shadow-none`,
    
    danger: `bg-red-900/20 border-red-900/50 text-red-400 hover:bg-red-900/40 hover:text-red-200`,
    
    // NEW INVERTED DIAMOND THEME: Azure Silver Metallic Block with Black Text
    // Removed the colored rgba glow (shadow-[0_0_20px...]) which caused the "cut light" effect.
    // Replaced with standard shadow-md/lg for clean depth.
    diamond: `
      bg-gradient-to-b from-diamond-300 via-diamond-400 to-diamond-500
      border border-diamond-300/50
      text-black
      shadow-md
      hover:shadow-lg
      hover:brightness-110
      active:scale-[0.98]
      relative overflow-hidden
      
      /* Subtle Sheen Effect on Hover - Kept internal sheen, removed external glow */
      after:absolute after:inset-0 after:bg-white/20 after:translate-y-full hover:after:translate-y-0 after:transition-transform after:duration-300 after:pointer-events-none
    `,
  };

  const sizes = {
    sm: "px-3 py-1.5 text-xs",
    md: "px-6 py-2.5 text-sm",
    lg: "px-8 py-3 text-base",
  };

  return (
    <button 
      className={`${baseStyles} ${radius} ${variants[variant]} ${sizes[size]} ${className}`}
      {...props}
    >
      <span className="relative z-10 flex items-center">
        {icon && <span className="mr-2">{icon}</span>}
        {children}
      </span>
    </button>
  );
};
