import json
import os

files = ['emails_b5_ready.json', 'emails_b6_ready.json']
for f_name in files:
    path = os.path.join(r'c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow', f_name)
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        ready_emails = [e for e in data if e.get('status') == 'ready']
        niches = {}
        for e in ready_emails:
            n = e.get('nicchia', 'altro')
            niches[n] = niches.get(n, 0) + 1
        print(f"{f_name} ready niches: {niches}")
