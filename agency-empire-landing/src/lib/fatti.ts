/**
 * FATTI — i numeri che il sito può dire, tutti con fonte in FATTI.md (C2.4).
 * Le sezioni li leggono da qui: cambiare un fatto = cambiarlo in un posto.
 */
export const FATTI = {
  giorniSetup: 7,
  messaggiGiorno: 300,
  canoneMese: 0,
  vpsMeseMin: 5,
  vpsMeseMax: 20,
  giorniSupporto: 90,
  giorniMonitoraggio: 30,
  giorniGaranzia: 30,
  minutiChiamata: 30,
  sistemi: 3,
  persone: 3,
  annoNascita: 2026,
  meseNascita: "gennaio",
  /** aritmetica dichiarata (V9): 30 DM × 5 minuti */
  dmAMano: 30,
  minutiPerDm: 5,
  orePerDm: 2.5,
  /** Novacar / PreventivoForge — CP-20260723-003 */
  novacar: { preventivi: 65, marche: 11, minutiPerPdf: 2, controlli: 6, periodo: "3-13 luglio 2026" },
  /** Preventa — avvia-outreach-preventa */
  preventaWhatsappGiorno: 50,
} as const;
