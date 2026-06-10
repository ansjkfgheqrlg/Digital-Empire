import { LucideIcon } from 'lucide-react';

export interface Service {
  title: string;
  description: string;
  fullDescription: string;
  icon: LucideIcon;
  details: string[];
  techSpecs?: string[];
}

export interface NavItem {
  label: string;
  href: string;
}

export interface StatItem {
  value: string;
  label: string;
}

export interface Lead {
  id: string;
  name: string;
  email: string;
  goal: string;
  message: string;
  date: string;
  status: 'new' | 'contacted';
}