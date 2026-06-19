# SKILL
            
> Path: [[Map - Crea_Siti|Crea siti > skills > site-3d]]

## Content

---
description: Integra esperienze 3D nel sito usando Three.js (Percorso A HTML puro) o React Three Fiber + Drei (Percorso B React). Solo per portfolio creativi, SaaS premium, o product showcase dove l'esperienza 3D ha valore reale. Genera scene 3D per hero sections, product viewer o background interattivi.
---

Sei la skill di integrazione 3D del sistema /site. Aggiungi esperienze tridimensionali al sito già costruito, scegliendo la libreria corretta in base allo stack e al tipo di scena richiesta.

## Trigger

Attivata da `/site 3d`. Wave 3 — solo per progetti premium che lo richiedono esplicitamente.

## IMPORTANTE — Quando NON usare questa skill

Usa `site-3d` SOLO se il brief menziona esplicitamente uno di questi contesti:
- Portfolio creativo / design / artista 3D
- Product showcase con oggetti fisici (gioielli, electronics, auto, architettura)
- SaaS premium che vuole un'esperienza wow per differenziarsi
- Agency creativa / studio di design

**NON usare per:** siti business standard, landing page semplici, blog, e-commerce di prodotti comuni, siti istituzionali. Se il brief non giustifica il 3D, segnalalo all'utente e suggerisci `/site animate` come alternativa più appropriata.

## Tipologie di Scene 3D

Identifica la scena più adatta al progetto tra queste:

| Tipo | Descrizione | Caso d'uso |
|---|---|---|
| `hero-3d` | Oggetto 3D rotante/interattivo nella hero | Logo 3D, prodotto, forma geometrica brand |
| `particle-bg` | Campo di particelle 3D come sfondo | SaaS tech, portfolio astratto |
| `product-viewer` | Visualizzatore 3D con drag-to-rotate | Prodotto fisico da mostrare a 360° |
| `abstract-art` | Geometria generativa decorativa | Agency creativa, portfolio designer |
| `globe` | Globo interattivo | Aziende con presenza globale |

## Processo

### Step 1 — Leggi il contesto
1. Leggi `SITE-STACK.md` — determina Percorso A (HTML + Three.js) o B (React Three Fiber)
2. Leggi `SITE-BRIEF.md` — identifica il tipo di scena più appropriata
3. Leggi `SITE-DESIGN.md` — estrai palette colori da applicare alla scena 3D
4. Leggi `index.html` o il file della pagina target — individua dove inserire il canvas

### Step 2 — Scegli la libreria

```
Stack è React/Next.js (Percorso B)?
  └── Sì → React Three Fiber + Drei
      └── Scena complessa con physics/shader? → aggiungi @react-three/rapier o drei shaders
  └── No (Percorso A — HTML puro) →
      └── Scena con geometrie e luci → Three.js
      └── Solo particelle → Three.js (Points + BufferGeometry)
      └── File .glb/.gltf da caricare → Three.js + GLTFLoader
      └── Animazioni JSON → lottie-web (non è 3D ma simile WOW effect)
```

### Step 3A — Implementazione Percorso A (Three.js)

**Installa via CDN nell'head HTML:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

**Aggiungi canvas alla pagina:**
```html
<section class="hero-3d" aria-hidden="true">
  <canvas id="hero-canvas"></canvas>
  <div class="hero-3d-content">
    <!-- Contenuto testuale sopra il canvas -->
  </div>
</section>
```

**Crea `js/scene-3d.js`** con questa struttura:

```javascript
// ============================================================
// SCENE 3D — [tipo di scena]
// ============================================================
(function initScene3D() {
  const canvas = document.getElementById('hero-canvas');
  if (!canvas) return;

  // Fallback: se WebGL non supportato, nascondi canvas
  if (!window.WebGLRenderingContext) {
    canvas.style.display = 'none';
    return;
  }

  // Setup base
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // Luci
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
  scene.add(ambientLight);
  const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
  directionalLight.position.set(5, 10, 5);
  scene.add(directionalLight);

  // [OGGETTO 3D — specifico per tipo di scena]
  // Hero 3D — sfera con materiale premium:
  const geometry = new THREE.IcosahedronGeometry(1.5, 4);
  const material = new THREE.MeshStandardMaterial({
    color: 0x[colore primario dal design system],
    wireframe: false,
    metalness: 0.3,
    roughness: 0.4,
  });
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  camera.position.z = 4;

  // Interazione mouse
  let mouseX = 0, mouseY = 0;
  document.addEventListener('mousemove', e => {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
  });

  // Rispetta prefers-reduced-motion
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Animation loop
  function animate() {
    requestAnimationFrame(animate);
    if (!prefersReduced) {
      mesh.rotation.x += 0.003;
      mesh.rotation.y += 0.005;
      mesh.rotation.x += (mouseY * 0.1 - mesh.rotation.x) * 0.05;
      mesh.rotation.y += (mouseX * 0.1 - mesh.rotation.y) * 0.05;
    }
    renderer.render(scene, camera);
  }
  animate();

  // Responsive resize
  window.addEventListener('resize', () => {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });

  // Disabilita su mobile se hardware limitato
  if (navigator.hardwareConcurrency < 4) {
    canvas.style.display = 'none';
  }
})();
```

**Varianti per tipo di scena:**

*Particle Background:*
```javascript
const particleCount = 2000;
const positions = new Float32Array(particleCount * 3);
for (let i = 0; i < particleCount * 3; i++) {
  positions[i] = (Math.random() - 0.5) * 20;
}
const geometry = new THREE.BufferGeometry();
geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
const material = new THREE.PointsMaterial({ color: 0x[accent], size: 0.02 });
const particles = new THREE.Points(geometry, material);
scene.add(particles);
// Nel loop: particles.rotation.y += 0.0005;
```

*Product Viewer (carica .glb):*
```javascript
// Aggiungi GLTFLoader CDN
const loader = new THREE.GLTFLoader();
loader.load('assets/models/product.glb', (gltf) => {
  scene.add(gltf.scene);
  // OrbitControls per drag-to-rotate
});
```

### Step 3B — Implementazione Percorso B (React Three Fiber)

**Installa dipendenze:**
```bash
bun add @react-three/fiber @react-three/drei three
bun add -D @types/three
```

**Crea `components/Scene3D.tsx`:**
```tsx
'use client';
import { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Environment, Float } from '@react-three/drei';
import { Mesh } from 'three';

function HeroObject() {
  const meshRef = useRef<Mesh>(null);

  useFrame((state) => {
    if (!meshRef.current) return;
    meshRef.current.rotation.x = Math.sin(state.clock.elapsedTime * 0.3) * 0.2;
    meshRef.current.rotation.y += 0.005;
  });

  return (
    <Float speed={2} rotationIntensity={0.5} floatIntensity={0.5}>
      <mesh ref={meshRef}>
        <icosahedronGeometry args={[1.5, 4]} />
        <meshStandardMaterial
          color="#[colore primario]"
          metalness={0.3}
          roughness={0.4}
        />
      </mesh>
    </Float>
  );
}

export default function Scene3D() {
  return (
    <Canvas
      camera={{ position: [0, 0, 4], fov: 75 }}
      style={{ position: 'absolute', inset: 0 }}
      aria-hidden="true"
    >
      <ambientLight intensity={0.6} />
      <directionalLight position={[5, 10, 5]} intensity={0.8} />
      <HeroObject />
      <Environment preset="city" />
      <OrbitControls enableZoom={false} enablePan={false} />
    </Canvas>
  );
}
```

**Usa nel layout/pagina:**
```tsx
import { Suspense } from 'react';
import dynamic from 'next/dynamic';

const Scene3D = dynamic(() => import('@/components/Scene3D'), { ssr: false });

export default function HeroSection() {
  return (
    <section className="hero relative">
      <Suspense fallback={<div className="hero-fallback-bg" />}>
        <Scene3D />
      </Suspense>
      <div className="hero-content relative z-10">
        {/* Testo sopra la scena 3D */}
      </div>
    </section>
  );
}
```

### Step 4 — Regole di Performance

- La scena 3D **non blocca** il caricamento del contenuto testuale — usa `Suspense` e posizionamento assoluto
- Fornisci sempre un **fallback statico** se WebGL non è supportato (gradiente o immagine)
- Target: **60fps su desktop**, 30fps accettabile su mobile
- **Disabilita su mobile** con hardware limitato: `navigator.hardwareConcurrency < 4` o CSS `@media (max-width: 768px) { canvas { display: none; } }`
- `prefers-reduced-motion`: se attivo, ferma tutte le animazioni del loop
- Pixel ratio: `Math.min(window.devicePixelRatio, 2)` — mai più di 2x per risparmiare GPU

### Step 5 — Output

**Percorso A:**
- `js/scene-3d.js` — file della scena Three.js
- `index.html` aggiornato con canvas + script CDN
- Aggiungi `<script src="js/scene-3d.js" defer></script>` dopo main.js

**Percorso B:**
- `components/Scene3D.tsx` — componente React
- File pagina aggiornato con import e Suspense wrapper

**Entrambi:**
- CSS per il canvas: `position: absolute; inset: 0; z-index: 0;` — il testo viene sopra con `z-index: 1`
- Nota nel codice: come configurare il colore della scena con le variabili del design system

## Comunicazione Finale

Mostra all'utente:
1. Tipo di scena implementata e libreria usata
2. File creati/modificati
3. Come aprire in preview
4. Consigli di ottimizzazione specifici per la scena generata
5. Come sostituire i colori placeholder con quelli esatti del brand

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - Crea_Siti|Crea Siti Area]]
- [[Map - Saas|Saas Area]]
