"use client";

import { useEffect } from "react";
import { motion } from "framer-motion";

export type ToastType = "success" | "error" | "info";

interface ToastProps {
  id: string;
  message: string;
  type?: ToastType;
  onDismiss: (id: string) => void;
}

const COLORS = {
  success: "#6fdca0",
  error: "#ff8a8a",
  info: "#ff8a4a",
};

const ICONS = {
  success: "✓",
  error: "✕",
  info: "ℹ",
};

export default function Toast({ id, message, type = "info", onDismiss }: ToastProps) {
  useEffect(() => {
    const t = setTimeout(() => onDismiss(id), 4000);
    return () => clearTimeout(t);
  }, [id, onDismiss]);

  const color = COLORS[type];

  return (
    <motion.div
      layout
      initial={{ opacity: 0, x: 60, scale: 0.95 }}
      animate={{ opacity: 1, x: 0, scale: 1 }}
      exit={{ opacity: 0, x: 60, scale: 0.95 }}
      transition={{ duration: 0.25, ease: "easeOut" }}
      style={{
        display: "flex",
        alignItems: "center",
        gap: "0.75rem",
        padding: "0.875rem 1.25rem",
        borderRadius: "0.75rem",
        background: "linear-gradient(135deg, #1a1a1a, #121212)",
        border: `1px solid ${color}40`,
        minWidth: 280,
        maxWidth: 400,
        boxShadow: "0 8px 32px rgba(0,0,0,0.4)",
      }}
    >
      <span style={{ color, fontSize: "1rem", fontWeight: 700, flexShrink: 0 }}>
        {ICONS[type]}
      </span>
      <span style={{ color: "#f9f9f9", fontSize: "0.875rem", flex: 1, lineHeight: 1.4 }}>
        {message}
      </span>
      <button
        onClick={() => onDismiss(id)}
        style={{ color: "rgba(249,249,249,0.4)", background: "none", border: "none", cursor: "pointer", fontSize: "1rem", flexShrink: 0, padding: "0.25rem" }}
        aria-label="Chiudi"
      >
        ✕
      </button>
    </motion.div>
  );
}
