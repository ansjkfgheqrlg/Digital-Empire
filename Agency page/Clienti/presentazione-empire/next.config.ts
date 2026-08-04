import type { NextConfig } from "next";
const nextConfig: NextConfig = {
  ...(process.env.NODE_ENV === "development" && {
    allowedDevOrigins: ["10.5.0.2"],
  }),
};
export default nextConfig;
