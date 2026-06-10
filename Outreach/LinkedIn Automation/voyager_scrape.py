"""
LinkedIn Voyager API scraper — estrae profili senza browser.
Usa i cookie della sessione Playwright per chiamare l'API interna LinkedIn.
Molto più veloce e affidabile del browser scraping.
"""
import json
import os
import sys
import time
import random
import requests
from datetime import date

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from config import SESSION_FILE, LEADS_FILE, TARGET_SEARCHES


def load_session_cookies():
    """Estrae i cookie dalla sessione Playwright salvata."""
    session_path = os.path.join(BASE, SESSION_FILE)
    with open(session_path, encoding="utf-8") as f:
        session = json.load(f)
    cookies = {}
    for c in session.get("cookies", []):
        if "linkedin.com" in c.get("domain", ""):
            cookies[c["name"]] = c["value"]
    return cookies


def load_leads():
    path = os.path.join(BASE, LEADS_FILE)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_leads(leads):
    with open(os.path.join(BASE, LEADS_FILE), "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)


def voyager_search(cookies, keywords, start=0, count=10):
    """Chiama l'API Voyager per cercare persone."""
    url = "https://www.linkedin.com/voyager/api/search/blended"
    params = {
        "q": "blended",
        "keywords": keywords,
        "count": count,
        "start": start,
        "filters": "List(resultType->PEOPLE)",
        "queryContext": "List(spellCorrectionEnabled->true)",
        "origin": "GLOBAL_SEARCH_HEADER",
        "blendedSrpEnabled": "true",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/vnd.linkedin.normalized+json+2.1",
        "Accept-Language": "it-IT,it;q=0.9",
        "x-restli-protocol-version": "2.0.0",
        "x-li-lang": "it_IT",
        "x-li-track": '{"clientVersion":"1.13.14661","mpVersion":"1.13.14661"}',
        "csrf-token": cookies.get("JSESSIONID", "").strip('"'),
        "Referer": "https://www.linkedin.com/search/results/people/",
    }
    try:
        resp = requests.get(url, params=params, headers=headers, cookies=cookies, timeout=15)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"  API {resp.status_code}: {resp.text[:200]}")
            return None
    except Exception as e:
        print(f"  Errore API: {e}")
        return None


def parse_profiles(data):
    """Estrae profili dalla risposta Voyager."""
    profiles = []
    if not data:
        return profiles

    included = data.get("included", [])
    for item in included:
        # Profile type
        if item.get("$type") in (
            "com.linkedin.voyager.identity.shared.MiniProfile",
            "com.linkedin.voyager.dash.identity.profile.Profile",
        ):
            slug = item.get("publicIdentifier", "")
            name = f"{item.get('firstName', '')} {item.get('lastName', '')}".strip()
            headline = item.get("headline", "")
            location = ""
            if "locationUnion" in item:
                loc = item["locationUnion"]
                if isinstance(loc, dict):
                    location = loc.get("geo", {}).get("defaultLocalizedName", "")

            if slug and name:
                profiles.append({
                    "name": name,
                    "title": headline,
                    "location": location,
                    "profile_url": f"https://www.linkedin.com/in/{slug}",
                    "slug": slug,
                })

    return profiles


def main():
    print("LinkedIn Voyager API Scraper")
    print("="*50)

    try:
        cookies = load_session_cookies()
        print(f"Cookies caricati: {len(cookies)} cookie LinkedIn")
    except Exception as e:
        print(f"ERRORE caricamento sessione: {e}")
        return []

    existing_leads = load_leads()
    existing_urls = {l["profile_url"] for l in existing_leads}
    new_leads = []

    for query in TARGET_SEARCHES:
        print(f"\nRicerca: '{query}'")
        data = voyager_search(cookies, query, count=25)

        if data is None:
            print(f"  Nessun risultato")
            continue

        profiles = parse_profiles(data)
        print(f"  Profili estratti: {len(profiles)}")

        for p in profiles:
            if p["profile_url"] not in existing_urls:
                lead = {
                    "name": p["name"],
                    "title": p["title"],
                    "location": p["location"],
                    "profile_url": p["profile_url"],
                    "search_query": query,
                    "status": "new",
                    "scraped_date": str(date.today()),
                    "connect_sent": None,
                    "connect_accepted": False,
                    "message_sent": None,
                    "message_text": None,
                    "followup1_sent": None,
                    "followup2_sent": None,
                }
                new_leads.append(lead)
                existing_urls.add(p["profile_url"])
                print(f"    + {p['name']}: {p['title'][:40]}")

        time.sleep(random.uniform(1.5, 3))

    all_leads = existing_leads + new_leads
    save_leads(all_leads)

    print(f"\n{'='*50}")
    print(f"Nuovi lead aggiunti: {len(new_leads)}")
    print(f"Totale lead database: {len(all_leads)}")
    print(f"{'='*50}")
    return new_leads


if __name__ == "__main__":
    main()
