"use client";

import { motion } from "framer-motion";

interface UploadProgressProps {
  progress: number; // 0-100
  filename?: string;
}

export default function UploadProgress({ progress, filename }: UploadProgressProps) {
  return (
    <div style={{ padding: "1rem", borderRadius: "0.75rem", background: "rgba(255,138,74,0.06)", border: "1px solid rgba(255,138,74,0.2)" }}>
      {filename && (
        <p style={{ color: "rgba(249,249,249,0.7)", fontSize: "0.8rem", marginBottom: "0.5rem", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
          {filename}
        </p>
      )}
      <div style={{ height: 4, borderRadius: 2, background: "rgba(249,249,249,0.1)", overflow: "hidden" }}>
        <motion.div
          initial={{ width: 0 }}
          animate={{ width: `${progress}%` }}
          transition={{ ease: "easeOut" }}
          style={{ height: "100%", background: "#ff8a4a", borderRadius: 2 }}
        />
      </div>
      <p style={{ color: "#ff8a4a", fontSize: "0.75rem", marginTop: "0.375rem", textAlign: "right" }}>
        {Math.round(progress)}%
      </p>
    </div>
  );
}
