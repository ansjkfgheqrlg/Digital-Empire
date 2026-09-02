/** @type {import('next').NextConfig} */
// GH_PAGES_BASE: valorizzato SOLO per la build di anteprima su GitHub Pages,
// che serve il sito da un sottopercorso. Su Vercel resta vuoto e non cambia nulla.
const raw = process.env.GH_PAGES_BASE || "";
const base = raw && !raw.startsWith("/") ? "/" + raw : raw;

const nextConfig = {
  output: "export",
  images: { unoptimized: true },
  trailingSlash: true,
  ...(base ? { basePath: base, assetPrefix: base } : {}),
};
export default nextConfig;
