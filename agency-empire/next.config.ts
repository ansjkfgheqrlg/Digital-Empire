import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,   // /prenota -> prenota/index.html: ogni link risolve a un file (gate_siti CASSA, ADR-024 c.8)
  distDir: "dist",
  reactStrictMode: true,
  experimental: {
    optimizePackageImports: ["lucide-react", "framer-motion"],
  },
};

export default nextConfig;