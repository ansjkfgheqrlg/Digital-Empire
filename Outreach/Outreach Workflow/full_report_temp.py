import json
import os

files = ['emails_ready.json', 'emails_b4_ready.json', 'emails_b5_ready.json', 'emails_b6_ready.json']
report = {}

for f_name in files:
    path = os.path.join(r'c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow', f_name)
    if not os.path.exists(path):
        continue
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
        counts = {
            'ready': 0,
            'sent': 0,
            'failed': 0,
            'error': 0,
            'total': len(data)
        }
        for e in data:
            status = e.get('status', '').lower()
            if status == 'ready':
                counts['ready'] += 1
            elif status == 'sent':
                counts['sent'] += 1
            elif 'failed' in status:
                counts['failed'] += 1
            elif 'error' in status:
                counts['error'] += 1
        report[f_name] = counts

print(json.dumps(report, indent=2))
