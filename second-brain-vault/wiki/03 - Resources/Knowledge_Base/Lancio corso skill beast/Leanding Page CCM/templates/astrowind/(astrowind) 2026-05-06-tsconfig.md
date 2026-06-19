# tsconfig
            
> Path: [[Map - Lancio_Corso_Skill_Beast|Lancio corso skill beast > Leanding Page CCM > templates > astrowind]]

## Content

{
  "extends": "astro/tsconfigs/base",
  "compilerOptions": {
    "strictNullChecks": true,
    "allowJs": true,
    "baseUrl": ".",
    "paths": {
      "~/*": ["src/*"]
    }
  },
  "include": [".astro/types.d.ts", "**/*"],
  "exclude": ["dist/"]
}

## Collegamenti Correlati
- [[Map - Lancio_Corso_Skill_Beast|Lancio Corso Skill Beast Area]]
