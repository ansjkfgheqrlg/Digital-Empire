
import React, { useState, useEffect } from 'react';
import { Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { GoldButton } from '../ui/GoldButton';
import { useNavigate, useLocation, Link } from 'react-router-dom';

const MotionDiv = motion.div as any;

const navItems = [
  { id: 'hero', label: 'home', path: '/' },
  { id: 'services', label: 'servizi', path: '/#services' },
  { id: 'process', label: 'metodo', path: '/#process' },
  { id: 'blog', label: 'blog', path: '/blog' },
];

export const Navbar: React.FC = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('hero');
  const [hoveredSection, setHoveredSection] = useState<string | null>(null);

  const navigate = useNavigate();
  const location = useLocation();

  // Handle Scroll effect and Active Section detection
  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);

      // Solo se siamo in home controlliamo le sezioni
      if (location.pathname === '/') {
        const sections = navItems
          .filter(item => item.path.includes('#')) // Filtra solo le ancore
          .map(item => ({ id: item.id, el: document.getElementById(item.id) }))
          .sort((a, b) => (a.el?.offsetTop || 0) - (b.el?.offsetTop || 0)); // Sort by physical position

        const scrollPosition = window.scrollY + 200;
        let current = 'hero';

        sections.forEach(({ id, el }) => {
          if (el && el.offsetTop <= scrollPosition) {
            current = id;
          }
        });

        // Se siamo in cima
        if (window.scrollY < 100) current = 'hero';

        setActiveSection(current);
      }
    };

    // Imposta la sezione attiva in base alla pagina corrente
    if (location.pathname.includes('blog')) {
      setActiveSection('blog');
    } else if (location.pathname === '/') {
      handleScroll(); // Rileva la sezione corrente sulla home
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Check on mount
    return () => window.removeEventListener('scroll', handleScroll);
  }, [location.pathname]);

  // Gestione click navigazione
  const handleNavClick = async (e: React.MouseEvent | undefined, item: typeof navItems[0]) => {
    if (e) e.preventDefault();
    setIsMobileMenuOpen(false);

    // Aggiorna immediatamente lo stato attivo
    setActiveSection(item.id);

    // Se è la pagina blog
    if (item.id === 'blog') {
      navigate('/blog');
      // Scrolla in alto quando si naviga al blog
      setTimeout(() => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }, 100);
      return;
    }

    // Se è un link alla home/ancora
    if (location.pathname !== '/') {
      // Se non siamo in home, andiamo in home e poi scrolliamo
      navigate('/');
      setTimeout(() => {
        if (item.id === 'hero') {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        } else {
          const element = document.getElementById(item.id);
          if (element) {
            const offset = 80; // Offset per la navbar
            const elementPosition = element.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - offset;
            window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
          }
        }
      }, 300); // Aumentato timeout per navigazione più affidabile
    } else {
      // Se siamo già in home
      if (item.id === 'hero') {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } else {
        const element = document.getElementById(item.id);
        if (element) {
          const offset = 80; // Offset per la navbar
          const elementPosition = element.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - offset;
          window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
        }
      }
    }
  };

  // High-End Gradients matched from Hero
  const logoGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 45%, #FDE68A 50%, #D4AF37 75%, #FFF7ED 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    filter: 'drop-shadow(0px 2px 4px rgba(0,0,0,0.5))',
  };

  const silverTextGradient = {
    backgroundImage: 'linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 50%, #94A3B8 100%)',
    WebkitBackgroundClip: 'text',
    backgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  };

  return (
    <nav
      className={`fixed top-0 w-full z-50 transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] ${isScrolled
        ? 'py-4 bg-[#020202]/80 backdrop-blur-xl border-b border-white/5 shadow-2xl'
        : 'py-8 bg-transparent'
        }`}
    >
      <div className="container mx-auto px-6 md:px-12 flex justify-between items-center relative">

        {/* LEFT: Logo - LUXURY UPGRADE */}
        <div
          onClick={(e) => handleNavClick(e, navItems[0])}
          className="flex items-center gap-4 group cursor-pointer z-50 select-none"
        >
          {/* Logo Icon Box */}
          <div className="relative w-12 h-12 flex items-center justify-center overflow-hidden rounded-xl bg-gradient-to-br from-black-900 to-black-950 border border-white/10 group-hover:border-gold-500/50 transition-all duration-500 shadow-[0_0_30px_rgba(0,0,0,0.5)] group-hover:shadow-[0_0_30px_rgba(212,175,55,0.2)]">
            {/* Inner Shine */}
            <div className="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

            {/* The "DE" Text */}
            <span style={logoGradient as any} className="font-serif font-black text-xl tracking-tighter relative z-10 transform group-hover:scale-110 transition-transform duration-500 lowercase">
              de
            </span>
          </div>

          {/* Logo Text */}
          <div className="flex flex-col justify-center gap-0.5">
            <span style={silverTextGradient as any} className="font-serif text-sm font-bold tracking-[0.25em] leading-none lowercase">
              empire
            </span>
            <span className="font-mono text-[9px] text-gold-500/80 tracking-[0.4em] leading-none opacity-60 group-hover:opacity-100 transition-opacity duration-500 lowercase">
              systems
            </span>
          </div>
        </div>

        {/* CENTER: DYNAMIC CAPSULE NAVIGATION */}
        <div className={`hidden md:flex items-center absolute left-1/2 -translate-x-1/2 transition-all duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] ${isScrolled ? 'translate-y-0 opacity-100' : 'translate-y-0 opacity-100'}`}>
          <div
            className="flex items-center p-1.5 rounded-full border border-white/10 shadow-[0_10px_40px_rgba(0,0,0,0.5)] bg-[#050505]/60 backdrop-blur-2xl relative overflow-hidden group/nav hover:border-white/20 transition-colors duration-500"
            onMouseLeave={() => setHoveredSection(null)}
          >
            {/* Glossy Overlay */}
            <div className="absolute top-0 left-0 w-full h-[50%] bg-gradient-to-b from-white/5 to-transparent pointer-events-none rounded-full"></div>

            {navItems.map((item) => {
              const isActive = activeSection === item.id;
              const isHovered = hoveredSection === item.id;

              return (
                <a
                  key={item.id}
                  href={item.path}
                  onClick={(e) => handleNavClick(e, item)}
                  onMouseEnter={() => setHoveredSection(item.id)}
                  className="relative px-7 py-2.5 rounded-full text-[10px] font-bold tracking-[0.15em] lowercase transition-all duration-500 z-10 cursor-pointer flex justify-center items-center"
                >
                  {/* TEXT LAYER */}
                  <span className={`relative z-20 transition-all duration-300 ${isActive ? 'text-[#2A2312] font-black' : 'text-gray-400 group-hover/nav:text-gray-300 hover:text-white'}`}>
                    {item.label}
                  </span>

                  {/* ACTIVE BACKGROUND (Solid Gold Pill) */}
                  {isActive && (
                    <MotionDiv
                      layoutId="navbar-active"
                      className="absolute inset-0 rounded-full shadow-[0_0_25px_rgba(212,175,55,0.4)]"
                      initial={false}
                      transition={{ type: "spring", stiffness: 300, damping: 30 }}
                      style={{
                        borderRadius: 9999,
                        background: 'linear-gradient(180deg, #FCD34D 0%, #FDE68A 20%, #D4AF37 80%, #996515 100%)',
                        boxShadow: 'inset 0 1px 0 rgba(255,255,255,0.6), 0 4px 10px rgba(0,0,0,0.3)'
                      }}
                    />
                  )}

                  {/* HOVER BACKGROUND (Glass) */}
                  {!isActive && isHovered && (
                    <MotionDiv
                      layoutId="navbar-hover"
                      className="absolute inset-0 bg-white/10 rounded-full"
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 0.2 }}
                      style={{ borderRadius: 9999 }}
                    />
                  )}
                </a>
              );
            })}
          </div>
        </div>

        {/* RIGHT: CTA Button - REPLACED */}
        <div className="hidden md:block z-50">
          <GoldButton
            href="#contact"
            className="!py-3 !px-8 !text-[10px] !tracking-[0.25em] shadow-[0_0_30px_rgba(253,185,19,0.1)] hover:shadow-[0_0_40px_rgba(253,185,19,0.3)]"
            onClick={(e) => {
              if (location.pathname !== '/') {
                e?.preventDefault();
                navigate('/');
                setTimeout(() => {
                  document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });
                }, 100);
              }
              // Normal behavior handles anchor link if on home
            }}
          >
            prenota demo
          </GoldButton>
        </div>

        {/* Mobile Toggle */}
        <button
          className="md:hidden text-white hover:text-gold-400 transition-colors z-50 p-3 bg-black-900/80 rounded-xl backdrop-blur-md border border-white/10 shadow-lg active:scale-95 duration-200"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        >
          {isMobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
        </button>
      </div>

      {/* Mobile Menu Overlay */}
      <AnimatePresence>
        {isMobileMenuOpen && (
          <MotionDiv
            initial={{ opacity: 0, y: -20, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -20, scale: 0.98 }}
            transition={{ duration: 0.2 }}
            className="absolute top-24 left-4 right-4 bg-[#080808]/95 backdrop-blur-3xl border border-white/10 rounded-3xl p-6 flex flex-col items-center gap-2 md:hidden shadow-[0_50px_100px_rgba(0,0,0,1)] z-40 overflow-hidden"
          >
            {/* Top Shine */}
            <div className="absolute top-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-white/20 to-transparent" />

            {navItems.map((item) => (
              <a
                key={item.id}
                href={item.path}
                onClick={(e) => handleNavClick(e, item)}
                className={`font-serif text-lg transition-all w-full text-center py-4 rounded-xl lowercase ${activeSection === item.id
                  ? 'text-gold-500 font-bold bg-white/5'
                  : 'text-gray-400 hover:text-white hover:bg-white/5'
                  }`}
              >
                {item.label}
              </a>
            ))}

            <div className="w-full mt-4 pt-4 border-t border-white/5">
              <GoldButton
                href="#contact"
                fullWidth
                onClick={(e) => {
                  e?.preventDefault();
                  setIsMobileMenuOpen(false);
                  if (location.pathname !== '/') {
                    navigate('/');
                    setTimeout(() => {
                      document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });
                    }, 100);
                  } else {
                    document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });
                  }
                }}
              >
                prenota demo
              </GoldButton>
            </div>
          </MotionDiv>
        )}
      </AnimatePresence>
    </nav>
  );
};
