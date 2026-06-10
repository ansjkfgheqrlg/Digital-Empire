# package.json

> Source: File system (`SKILL & Agenti\SKILL\Skill empire-premium-style\references\package.json.md`)
> Collected: 2026-05-06
> Published: Unknown

# package.json FROZEN

Usa esattamente queste dipendenze. Sostituisci solo il campo `name`.

```json
{
  "name": "<PROJECT-NAME>-empire",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint"
  },
  "dependencies": {
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "framer-motion": "^12.38.0",
    "gsap": "^3.14.2",
    "lenis": "^1.3.21",
    "lucide-react": "^1.8.0",
    "next": "16.2.3",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "tailwind-merge": "^3.5.0",
    "tw-animate-css": "^1.4.0"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "16.2.3",
    "tailwindcss": "^4",
    "typescript": "^5"
  }
}
```

## Configs di contorno

**postcss.config.mjs**
```js
const config = { plugins: ["@tailwindcss/postcss"] };
export default config;
```

**next.config.ts**
```ts
import type { NextConfig } from "next";
const nextConfig: NextConfig = {};
export default nextConfig;
```

**tsconfig.json**
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

**Nota importante**: Se `design-tokens.css` contiene `@import "shadcn/tailwind.css"` o `@import "tw-animate-css"`, rimuovi la riga shadcn (non abbiamo shadcn in deps qui). Tieni `tw-animate-css` se usato. In caso di errore build, commenta entrambi `@import` non-tailwind e riprova.
