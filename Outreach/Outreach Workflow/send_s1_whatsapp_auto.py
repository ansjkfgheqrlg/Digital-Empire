# Script Python per verifica APSOC e invio guidato messaggi WhatsApp (WF-S1)
import os, sys

def verify_apsoc(text):
    checks = {
        'A (Attention)': '?' in text or '!' in text or 'NOVACAR' in text or 'preventivo' in text.lower(),
        'P (Problem)': '40 minuti' in text or 'A4' in text or 'attesa' in text.lower() or 'concorren' in text.lower(),
        'S (Solution)': '120 secondi' in text or 'PDF' in text or 'tablet' in text.lower() or 'Preventa' in text,
        'O (Offer)': '343' in text or '149' in text or 'Partenza Anticipata' in text or 'scontato' in text.lower(),
        'C (Close)': 'giugno' in text.lower() or 'luglio' in text.lower() or 'settembre' in text.lower() or 'preferisci' in text.lower() or 'slot' in text.lower()
    }
    passed = [k for k, v in checks.items() if v]
    print('=== DIAGNOSTICA CHECKLIST APSOC (Andrei Pascu) ===')
    for k, v in checks.items():
        print(f'[{chr(10003) if v else "X"}] {k}')
    print(f'Punteggio indicativo: {len(passed)}/5 ({len(passed)*20}%)')
    if len(passed) >= 4:
        print('ESITO: GO (Messaggio conforme al protocollo)')
    else:
        print('ESITO: NO-GO (Arricchire con leva dolore/valore)')

if __name__ == '__main__':
    msg = """Ciao! Ti scrivo perché l'app preventivi è live: NOVACAR la usa e ha tagliato i tempi da 40 minuti a 120 secondi con PDF brandizzato su tablet. Ti riservo la Partenza Anticipata Luglio: setup €343 invece di €490 e canone €149/mese, così a settembre sei già operativo e non perdi clienti con fogli A4. Ti blocco uno dei due slot rimasti o preferisci partire a settembre a listino pieno?"""
    verify_apsoc(msg)
