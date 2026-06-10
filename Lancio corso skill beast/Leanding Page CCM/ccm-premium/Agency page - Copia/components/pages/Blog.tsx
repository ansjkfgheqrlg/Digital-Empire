
import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ArrowRight, User, Clock, Fingerprint, ArrowLeft, Zap } from 'lucide-react';
import { GoldButton } from '../ui/GoldButton';
import { CosmicBackground } from '../ui/CosmicBackground';
import { blogPosts } from '../../data/blogPosts';
import { MetallicFrame, SilverBody } from '../blog/BlogParts';

const MotionDiv = motion.div as any;

export const Blog: React.FC = () => {
    const [activePost, setActivePost] = useState<any>(null);

    useEffect(() => {
        if (activePost) {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }, [activePost]);

    const getThemeStyles = (color: string) => {
        const overlays: Record<string, string> = {
            red: 'radial-gradient(circle at 50% -20%, rgba(153, 27, 27, 0.4) 0%, transparent 60%)',
            blue: 'radial-gradient(circle at 50% -20%, rgba(14, 116, 144, 0.4) 0%, transparent 60%)',
            gold: 'radial-gradient(circle at 50% -20%, rgba(133, 77, 14, 0.4) 0%, transparent 60%)',
            purple: 'radial-gradient(circle at 50% -20%, rgba(107, 33, 168, 0.4) 0%, transparent 60%)',
            emerald: 'radial-gradient(circle at 50% -20%, rgba(6, 95, 70, 0.4) 0%, transparent 60%)',
        };
        return { bgOverlay: overlays[color] || 'radial-gradient(circle at 50% -20%, rgba(51, 65, 85, 0.4) 0%, transparent 60%)' };
    };

    const currentTheme = activePost ? getThemeStyles(activePost.themeColor || 'silver') : null;

    return (
        <AnimatePresence mode="wait">
            {!activePost ? (
                <MotionDiv
                    key="list"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    className="pt-32 pb-40 relative min-h-screen bg-[#030303] overflow-hidden"
                >
                    <CosmicBackground />

                    <div className="container mx-auto px-4 relative z-10 max-w-7xl">
                        <div className="flex flex-col items-center justify-center mb-40 mt-10">
                            <div className="w-[1px] h-20 bg-gradient-to-b from-transparent via-slate-400 to-transparent mb-8"></div>
                            <MotionDiv className="relative border border-slate-700/50 bg-black/40 backdrop-blur-xl px-8 py-3 rounded-full mb-10">
                                <div className="flex items-center gap-4">
                                    <div className="w-2 h-2 bg-slate-200 rounded-full animate-pulse shadow-[0_0_10px_white]"></div>
                                    <span className="text-[10px] font-mono text-slate-300 uppercase tracking-[0.4em] font-bold lowercase">intelligence archive</span>
                                    <div className="w-2 h-2 bg-slate-200 rounded-full animate-pulse shadow-[0_0_10px_white]"></div>
                                </div>
                            </MotionDiv>
                            <h1 className="text-center">
                                <span className="block font-serif text-6xl md:text-9xl font-black tracking-tighter leading-[0.85] mb-2 mix-blend-luminosity opacity-30 text-slate-600 lowercase">empire</span>
                                <span className="block font-serif text-6xl md:text-9xl font-black tracking-tighter leading-[0.85] text-transparent bg-clip-text bg-gradient-to-b from-white via-slate-300 to-slate-600 drop-shadow-[0_10px_20px_rgba(0,0,0,1)] relative z-10 -mt-8 md:-mt-16 lowercase">insights</span>
                            </h1>
                        </div>

                        <div className="mb-40 relative cursor-pointer max-w-5xl mx-auto" onClick={() => setActivePost(blogPosts[0])}>
                            <MetallicFrame intensity="gold" className="w-full min-h-[550px] md:min-h-[60vh] relative group shadow-[0_0_50px_rgba(0,0,0,0.5)]">
                                <div className="absolute inset-0 group-hover:scale-105 transition-transform duration-[1.5s] ease-out">
                                    <img src={blogPosts[0].image} alt="Featured" className="w-full h-full object-cover opacity-90 transition-all duration-1000" />
                                    <div className="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent"></div>
                                    <div className="absolute inset-0 bg-gradient-to-r from-[#050505] via-[#050505]/20 to-transparent"></div>
                                </div>
                                <div className="absolute bottom-0 left-0 p-8 md:p-16 w-full md:w-4/5 lg:w-2/3 z-20 flex flex-col justify-end h-full">
                                    <div className="flex items-center gap-6 mb-8">
                                        <div className="px-4 py-1 border border-gold-500/50 bg-black/50 text-gold-500 font-mono text-[9px] uppercase tracking-[0.3em] backdrop-blur-md lowercase">strategy core</div>
                                        <div className="h-[1px] w-20 bg-gold-500"></div>
                                    </div>
                                    <h2 className="font-serif text-4xl md:text-6xl lg:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-200 to-slate-500 leading-[0.9] mb-6 drop-shadow-lg tracking-tighter lowercase">copywriting:<br />macchina da soldi</h2>
                                    <SilverBody className="max-w-xl text-base md:text-xl mb-10 lowercase border-l-2 border-gold-500/50 pl-6 backdrop-blur-sm bg-black/20 p-4 rounded-r-lg">
                                        se i copywriter non esistessero, le aziende farebbero prima a bruciare i soldi.
                                    </SilverBody>
                                    <div className="flex items-center gap-4 group/btn">
                                        <div className="w-14 h-14 border border-gold-400 rounded-full flex items-center justify-center bg-white/5 backdrop-blur group-hover/btn:bg-white group-hover/btn:text-black transition-all duration-500"><ArrowRight size={24} /></div>
                                        <span className="font-mono text-sm uppercase tracking-[0.3em] text-gold-400 group-hover/btn:text-white transition-colors font-bold lowercase">accedi al manuale</span>
                                    </div>
                                </div>
                            </MetallicFrame>
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 mb-40 max-w-5xl mx-auto">
                            {blogPosts.slice(1).map((post) => (
                                <MotionDiv
                                    key={post.id}
                                    initial={{ opacity: 0, y: 50 }}
                                    whileInView={{ opacity: 1, y: 0 }}
                                    viewport={{ once: true }}
                                    className="group flex flex-col gap-6 cursor-pointer"
                                    onClick={() => setActivePost(post)}
                                >
                                    <MetallicFrame intensity={post.themeColor as any} className="aspect-[16/10] shadow-2xl">
                                        <div className="absolute inset-0 overflow-hidden">
                                            <img src={post.image} alt={post.title} className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 opacity-90 group-hover:opacity-100" />
                                            <div className="absolute inset-0 bg-gradient-to-tr from-black/80 via-transparent to-transparent z-10" />
                                            <div className="absolute top-0 left-0 w-full h-[1px] bg-white/30 z-20 group-hover:top-full transition-all duration-[1.5s] ease-in-out opacity-0 group-hover:opacity-100"></div>
                                        </div>
                                    </MetallicFrame>
                                    <div className="px-2">
                                        <div className="flex justify-between items-end mb-4 border-b border-slate-800 pb-4">
                                            <span className="font-mono text-[9px] uppercase tracking-[0.2em] text-slate-500 font-bold group-hover:text-white transition-colors lowercase">{post.category}</span>
                                            <span className="font-mono text-[9px] text-slate-600">{post.readTime}</span>
                                        </div>
                                        <h3 className="font-serif text-2xl md:text-3xl font-bold leading-tight mb-3 group-hover:text-slate-200 transition-colors lowercase">{post.title}</h3>
                                        <SilverBody className="text-sm mb-5 lowercase opacity-70 group-hover:opacity-100 transition-opacity leading-relaxed">{post.excerpt}</SilverBody>
                                        <div className="flex items-center gap-2 text-[9px] font-mono uppercase tracking-widest text-slate-500 group-hover:text-white transition-colors lowercase">
                                            <Zap size={10} className={post.themeColor === "red" ? "text-red-500" : post.themeColor === "blue" ? "text-cyan-500" : post.themeColor === "purple" ? "text-purple-500" : post.themeColor === "emerald" ? "text-emerald-500" : "text-yellow-500"} />
                                            read data
                                        </div>
                                    </div>
                                </MotionDiv>
                            ))}
                        </div>
                    </div>
                </MotionDiv>
            ) : (
                <MotionDiv
                    key="detail"
                    initial={{ opacity: 0, scale: 0.98 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, y: 50 }}
                    transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                    className={`pt-0 relative min-h-screen overflow-hidden selection:bg-gold-500/30 selection:text-white`}
                >
                    <CosmicBackground />

                    <div className="relative w-full min-h-[70vh] flex flex-col items-center justify-center mb-0 mt-0">
                        <div className="absolute inset-0 w-full h-full z-0 overflow-hidden">
                            <motion.div
                                initial={{ scale: 1.1 }}
                                animate={{ scale: 1 }}
                                transition={{ duration: 2, ease: "easeOut" }}
                                className="w-full h-full"
                            >
                                <img src={activePost.image} alt={activePost.title} className="w-full h-full object-cover opacity-50" />
                            </motion.div>
                            <div className="absolute inset-0 bg-[#020202]/40 mix-blend-multiply"></div>
                            <div className="absolute inset-0 bg-gradient-to-t from-[#020202] via-[#020202]/50 to-transparent"></div>
                            <div className="absolute inset-0 bg-gradient-to-b from-[#020202]/80 via-transparent to-[#020202]/20"></div>
                        </div>

                        <div className="absolute top-32 left-4 md:left-8 z-50">
                            <button onClick={() => setActivePost(null)} className="group flex items-center gap-4 text-white hover:text-slate-300 transition-colors">
                                <div className={`w-12 h-12 rounded-full border bg-black/50 backdrop-blur-md flex items-center justify-center transition-colors group-hover:bg-white/10 border-white/20`}>
                                    <ArrowLeft size={20} className="text-white" />
                                </div>
                                <span className="font-mono text-xs uppercase tracking-[0.2em] font-bold hidden md:inline-block text-shadow-sm lowercase">torna all'archivio</span>
                            </button>
                        </div>

                        <div className="relative z-10 container mx-auto px-4 max-w-5xl text-center pt-32">
                            <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.3 }} className="flex items-center justify-center gap-4 mb-8">
                                <span className={`font-mono text-[10px] uppercase tracking-widest px-4 py-1.5 rounded-full border bg-black/40 backdrop-blur-md border-white/20 text-white shadow-lg lowercase`}>
                                    {activePost.category}
                                </span>
                            </motion.div>
                            <motion.h1 initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: 0.4 }} className="font-serif text-5xl md:text-7xl lg:text-8xl font-black text-white leading-[0.9] tracking-tighter mb-8 drop-shadow-2xl lowercase">
                                {activePost.title}
                            </motion.h1>
                            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.5 }} className="flex items-center justify-center gap-6 text-[10px] font-mono uppercase tracking-widest text-gray-200 lowercase">
                                <span className="flex items-center gap-2"><User size={12} /> empire intelligence</span>
                                <span className="flex items-center gap-2"><Clock size={12} /> {activePost.readTime} read</span>
                            </motion.div>
                        </div>
                    </div>

                    <div className="fixed inset-0 pointer-events-none z-0 mix-blend-screen opacity-40 transition-all duration-1000" style={{ background: currentTheme?.bgOverlay }} />

                    <style dangerouslySetInnerHTML={{
                        __html: `
                    .silver-prose p, .silver-prose li, .silver-prose span { background: linear-gradient(180deg, #FFFFFF 0%, #CBD5E1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0px 0px 20px rgba(255,255,255,0.1); font-weight: 300; line-height: 1.8; }
                    .silver-prose strong, .silver-prose b, .silver-prose em { background: linear-gradient(180deg, #FDE68A 0%, #D4AF37 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900; letter-spacing: 0.05em; font-style: normal; text-shadow: 0px 0px 15px rgba(212,175,55,0.3); text-transform: uppercase; font-size: 0.95em; }
                    .silver-prose h1, .silver-prose h2, .silver-prose h3, .silver-prose h4 { background: linear-gradient(180deg, #FFFFFF 0%, #94A3B8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
                `}} />

                    <div className="absolute inset-0 opacity-[0.07] mix-blend-soft-light pointer-events-none z-0" style={{ backgroundImage: 'url("https://grainy-gradients.vercel.app/noise.svg")' }}></div>

                    <div className="container mx-auto px-4 relative z-20 max-w-4xl pt-20">
                        <div className="max-w-3xl mx-auto pb-40">
                            <div className="silver-prose prose prose-invert prose-lg max-w-none">
                                <p className="lead text-xl md:text-2xl font-serif italic text-white/80 border-l-4 border-white/20 pl-6 mb-16 lowercase">
                                    {activePost.excerpt}
                                </p>
                                {activePost.content || <p>Contenuto completo del dossier in fase di decrittazione...</p>}
                                <div className="mt-24 pt-10 border-t border-white/10 flex items-center justify-between">
                                    <div>
                                        <div className="h-12 w-32 bg-white/10 mask-signature opacity-50"></div>
                                        <p className="text-[10px] font-mono uppercase tracking-widest text-slate-500 mt-2 lowercase">chief strategy officer</p>
                                    </div>
                                    <Fingerprint size={40} className="opacity-20 text-white" />
                                </div>
                            </div>

                            <div className="mt-24 p-12 rounded-2xl border bg-black/40 backdrop-blur-md text-center border-white/10 shadow-[0_0_50px_rgba(0,0,0,0.5)]">
                                <h3 className="font-serif text-3xl text-white mb-4 lowercase">non rimanere teorico</h3>
                                <p className="text-slate-400 text-sm mb-10 max-w-md mx-auto lowercase">la conoscenza senza esecuzione è intrattenimento. hai appena letto come dominare il tuo mercato. ora fallo.</p>
                                <GoldButton href="#contact" variant={activePost.themeColor === 'blue' ? 'cyan' : activePost.themeColor === 'purple' ? 'purple' : activePost.themeColor === 'emerald' ? 'emerald' : 'gold'}>
                                    applica protocollo ora
                                </GoldButton>
                            </div>
                        </div>
                    </div>
                </MotionDiv>
            )}
        </AnimatePresence>
    );
};
