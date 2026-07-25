"use client";

import React from "react";
import { Download, FileText, ExternalLink, ShieldCheck } from "lucide-react";
import { cn } from "@/lib/utils";

interface ResourceCardProps {
  title: string;
  type: string;
  size?: string;
  url?: string;
  variant?: "silver" | "orange";
}

export const ResourceCard = ({ title, type, size, url = "#", variant = "silver" }: ResourceCardProps) => {
  return (
    <div className={cn(
      "card-silver-orange group",
      variant === "orange" && "variant-orange"
    )}>
      <div className="flex items-start justify-between">
        <div className="eyebrow">{type}</div>
        <div className="w-10 h-10 rounded-xl bg-orange/10 flex items-center justify-center text-orange group-hover:bg-orange group-hover:text-white transition-all duration-300">
          <FileText className="h-5 w-5" />
        </div>
      </div>
      
      <h3 className="text-xl font-bold leading-tight mt-4 mb-2 pr-8">{title}</h3>
      <p className="text-[10px] uppercase tracking-widest font-bold text-black/40 mb-8">
        Digital Empire Asset • {size || "Premium Access"}
      </p>

      <div className="flex items-center justify-between mt-auto">
        <a 
          href={url}
          className="flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-black hover:text-orange transition-colors"
        >
          Download <Download className="h-3.5 w-3.5" />
        </a>
        <div className="flex items-center gap-1.5 text-[9px] font-bold text-black/20 uppercase tracking-tight">
          <ShieldCheck className="h-3 w-3" /> Verificato
        </div>
      </div>

      {/* Hover decoration */}
      <div className="absolute top-2 right-2 opacity-0 group-hover:opacity-10 transition-opacity">
        <ExternalLink className="h-4 w-4" />
      </div>
    </div>
  );
};
