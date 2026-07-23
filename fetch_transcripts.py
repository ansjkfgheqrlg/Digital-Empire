import sys
from youtube_transcript_api import YouTubeTranscriptApi

ids = ['YFX5_JK_L-w', 'oJdGoAirTY4', 'PckOW38eBPA', 'xuEIOjuuOfQ']
out = ''

for vid in ids:
    try:
        t = YouTubeTranscriptApi.get_transcript(vid, languages=['it', 'en'])
        out += f'\n\n=== VIDEO {vid} ===\n' + ' '.join([x['text'] for x in t])
    except Exception as e:
        out += f'\n\n=== VIDEO {vid} ERROR: {e} ===\n'

with open('C:/Users/Utente/Desktop/qui tutto/Digital Empire/nft_transcripts.txt', 'w', encoding='utf-8') as f:
    f.write(out)
