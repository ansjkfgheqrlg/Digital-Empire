/**
 * LEGAL — dati societari (gesto di Max, ADR-026: non blocca).
 * Campo vuoto = la riga NON si renderizza (mai "[da inserire]" in pagina, mai href="#").
 */
export const LEGAL: { ragioneSociale: string; piva: string; sede: string; pec: string; email: string } = {
  ragioneSociale: "Digital Empire",
  piva: "",
  sede: "",
  pec: "",
  email: "",
};

export const LEGAL_RIGHE: string[] = [
  LEGAL.ragioneSociale,
  LEGAL.piva ? `P.IVA ${LEGAL.piva}` : "",
  LEGAL.sede,
  LEGAL.pec ? `PEC ${LEGAL.pec}` : "",
].filter((r) => r.length > 0);
