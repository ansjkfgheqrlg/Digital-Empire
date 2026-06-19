# Skill_neon-dark-premium
            
> Path: [[Map - Saas|SaaS > Agents_and_Skills]]

## Content

---
name: neon-dark-premium-style
description: Stile ultra-premium per landing page SaaS. Mix di deep dark mode, neon glows viola/rosa e typography contrastante.
---

# SKILL: Neon Dark Premium Style

Questa skill trasforma l'output di sviluppo web in una landing page esteticamente impeccabile basata sullo stile "Zentira/Neon SaaS".

## Core Principles
1. **Backgrounds**: Neri profondi (`#050505` o `#000000`). Nessun grigio chiaro.
2. **Illuminazione (Glows)**: Utilizzo di `radial-gradient` posizionati in modo assoluto (dietro i contenuti) con colori neon come viola acceso (`#9b51e0`), fucsia, e blu cobalto. I glow devono essere molto sfumati (alta `blur`).
3. **Glassmorphism**: Elementi UI in primo piano (es. form input, card) devono essere semitrasparenti (`bg-white/5` o `bg-black/40`), con un forte `backdrop-blur-xl` e un leggero bordo semitrasparente (`border border-white/10`).
4. **Typography Mix**: 
   - Elementi "duri/razionali" (Headline principale, bottoni): Sans-serif geometrico e bold (es. Inter, Roboto o Onest).
   - Elementi "eleganti/emozionali" (seconda parte della headline): Serif in corsivo (es. Playfair Display, Instrument Serif).
5. **Micro-interazioni**: Effetti di hover leggeri, glow che aumentano d'intensità al passaggio del mouse.

## Palette di Riferimento
- Background: `#000000` o `#0A0A0F`
- Glow Neon Primario: `#8A2BE2` (Blue Violet) / `#9333EA` (Purple-600)
- Glow Neon Secondario: `#EC4899` (Pink-500)
- Text Primary: `#FFFFFF`
- Text Secondary: `#A1A1AA` (Zinc-400) o `#9CA3AF` (Gray-400)
- Glass Background: `rgba(255, 255, 255, 0.03)`
- Glass Border: `rgba(255, 255, 255, 0.08)`

## Stack Richiesto
- Next.js App Router
- Tailwind CSS v3 o v4
- Framer Motion per entry animations e hover states.

## Componenti Chiave
- **Waitlist Badge**: Pillola superiore con mini facce sovrapposte (avatar) e testo.
- **Glowing Input**: Input email senza bordi duri, incastonato in un contenitore glass, con bottone integrato e forte ombra neon (`box-shadow: 0 0 40px rgba(138, 43, 226, 0.4)`).
- **Dashboard Mockup Window**: Immagine/UI racchiusa in un div con bordo sfumato e un enorme bagliore sottostante.

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Saas|Saas Area]]
