"use client";

import { useRef } from "react";

function extractYouTubeId(url: string): string | null {
  const patterns = [
    /youtube\.com\/watch\?v=([^&\s]+)/,
    /youtu\.be\/([^?\s]+)/,
    /youtube\.com\/embed\/([^?\s]+)/,
  ];
  for (const p of patterns) {
    const m = url.match(p);
    if (m) return m[1];
  }
  return null;
}

function isMP4(url: string): boolean {
  return url.toLowerCase().includes('.mp4');
}

interface VideoPlayerProps {
  videoUrl?: string | null;
  title?: string;
}

export default function VideoPlayer({ videoUrl, title }: VideoPlayerProps) {
  if (videoUrl) {
    const ytId = extractYouTubeId(videoUrl);

    if (ytId) {
      return (
        <div className="relative w-full" style={{ paddingBottom: '56.25%', background: '#0a0a0a' }}>
          <iframe
            className="absolute inset-0 w-full h-full rounded-2xl"
            src={`https://www.youtube.com/embed/${ytId}?rel=0&modestbranding=1`}
            title={title ?? "Video lezione"}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      );
    }

    if (isMP4(videoUrl)) {
      return (
        <video
          controls
          className="w-full rounded-2xl"
          style={{ background: '#0a0a0a' }}
        >
          <source src={videoUrl} type="video/mp4" />
          Il tuo browser non supporta la riproduzione video.
        </video>
      );
    }
  }

  // Placeholder dark — nessun video disponibile
  return (
    <div
      className="w-full rounded-2xl flex items-center justify-center"
      style={{ paddingBottom: '56.25%', position: 'relative', background: '#0a0a0a', border: '1px solid rgba(249,249,249,0.08)' }}
    >
      <div style={{ position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: '1rem' }}>
        <div style={{ width: 64, height: 64, borderRadius: '50%', background: 'rgba(255,138,74,0.15)', border: '1px solid rgba(255,138,74,0.3)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="#ff8a4a">
            <polygon points="5,3 19,12 5,21" />
          </svg>
        </div>
        <p style={{ color: 'rgba(249,249,249,0.4)', fontSize: '0.875rem' }}>Video non ancora disponibile</p>
      </div>
    </div>
  );
}
