"use client";

import Link from "next/link";
import { useState, useEffect, useRef } from "react";
import Wordmark from "./wordmark";
import { signOut } from "@/app/(auth)/actions";

export type StudentHeaderUser = {
  name: string;
  email: string;
};

export default function StudentHeaderClient({
  user,
  inCourseTheme = false,
}: {
  user: StudentHeaderUser;
  inCourseTheme?: boolean;
}) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, []);

  void inCourseTheme;

  return (
    <header
      className="sticky top-0 z-50"
      style={{
        backdropFilter: "saturate(140%) blur(14px)",
        background: "rgba(26,26,26,0.85)",
        borderBottom: "1px solid rgba(249,249,249,0.08)",
      }}
    >
      <div className="container-wide flex items-center justify-between py-4">
        <div className="flex items-center gap-8">
          <Wordmark size="sm" href="/dashboard" />
          <nav className="hidden md:flex items-center gap-6 text-sm">
            <Link href="/dashboard" style={{ color: "rgba(249,249,249,0.7)" }}>
              Dashboard
            </Link>
            <Link
              href="/corsi/claude-code-mastery"
              style={{ color: "rgba(249,249,249,0.7)" }}
            >
              Il mio corso
            </Link>
          </nav>
        </div>

        <div className="relative flex items-center gap-3" ref={ref}>
          <button
            onClick={() => setOpen(!open)}
            className="flex items-center gap-2.5 px-3 py-2 rounded-xl transition-colors"
            style={{
              background: "rgba(249,249,249,0.05)",
              border: "1px solid rgba(249,249,249,0.08)",
            }}
          >
            <div
              className="w-8 h-8 rounded-full flex items-center justify-center font-bold text-sm"
              style={{
                background: "linear-gradient(135deg, #fb4604 0%, #ff6a2e 100%)",
                color: "#ffffff",
              }}
            >
              {user.name.charAt(0).toUpperCase()}
            </div>
            <span
              className="hidden sm:inline text-sm font-medium"
              style={{ color: "#f9f9f9" }}
            >
              {user.name}
            </span>
            <svg
              width="14"
              height="14"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              style={{
                color: "rgba(249,249,249,0.6)",
                transform: open ? "rotate(180deg)" : "none",
                transition: "transform 0.2s",
              }}
            >
              <polyline points="6 9 12 15 18 9" />
            </svg>
          </button>

          {open && (
            <div
              className="absolute right-0 top-full mt-2 w-64 rounded-xl overflow-hidden z-50"
              style={{
                background: "#141414",
                border: "1px solid rgba(249,249,249,0.08)",
                boxShadow: "0 20px 50px -12px rgba(0,0,0,0.6)",
              }}
            >
              <div
                className="p-4 border-b"
                style={{ borderColor: "rgba(249,249,249,0.08)" }}
              >
                <div
                  className="text-sm font-semibold"
                  style={{ color: "#f9f9f9" }}
                >
                  {user.name}
                </div>
                <div
                  className="text-xs truncate"
                  style={{ color: "rgba(249,249,249,0.6)" }}
                >
                  {user.email}
                </div>
              </div>
              <div className="py-2">
                <Link
                  href="/dashboard"
                  className="block px-4 py-2.5 text-sm hover:bg-white/5 transition-colors"
                  style={{ color: "rgba(249,249,249,0.75)" }}
                >
                  Dashboard
                </Link>
                <Link
                  href="/account"
                  className="block px-4 py-2.5 text-sm hover:bg-white/5 transition-colors"
                  style={{ color: "rgba(249,249,249,0.75)" }}
                >
                  Impostazioni
                </Link>
                <form action={signOut}>
                  <button
                    type="submit"
                    className="w-full text-left px-4 py-2.5 text-sm hover:bg-white/5 transition-colors"
                    style={{ color: "#ff8a4a" }}
                  >
                    Esci
                  </button>
                </form>
              </div>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}
