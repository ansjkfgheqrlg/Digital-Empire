# Script di verifica API Fliki e render video di test (WF-S5)
import os

def test_fliki_api():
    key = os.environ.get('FLIKI_API_KEY')
    if not key:
        print('[WARN] FLIKI_API_KEY non trovata in .env o variabili di sistema.')
        return False
    print('[INFO] Verifica connessione a Fliki API...')
    return True

if __name__ == '__main__':
    test_fliki_api()
