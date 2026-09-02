"""
Scrape a CS2Online lesson: login, extract page content, download video, extract frames.
Usage: python scrape_lesson.py <lesson_slug> <lesson_number> [--email EMAIL] [--password PASSWORD]

Storage state saved to %LOCALAPPDATA%/empire-studio/storage_state.json for reuse.
NO credentials saved to disk.
"""
import sys, os, json, re, subprocess, time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.andrei-copy.com/cs2online"
STORAGE_DIR = Path(os.environ.get("LOCALAPPDATA", "")) / "empire-studio"
STORAGE_FILE = STORAGE_DIR / "storage_state.json"

def get_args():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("slug", help="Lesson slug (e.g. lezione-18-come-scrivo-piccoli-codici-google-sites-h48d2)")
    p.add_argument("lesson_number", type=int, help="Lesson number (e.g. 18)")
    p.add_argument("--email", default="max.infoproducer@gmail.com")
    p.add_argument("--password", required=True)
    p.add_argument("--output-dir", default=None, help="Output directory (default: lessons/lezione-NN/)")
    p.add_argument("--frame-interval", type=int, default=2, help="Frame extraction interval in seconds")
    p.add_argument("--skip-video", action="store_true", help="Skip video download + frame extraction")
    return p.parse_args()

def login(page, email, password):
    """Login to CS2Online platform."""
    print("[LOGIN] Navigating to login page...")
    page.goto(f"{BASE_URL}", wait_until="networkidle", timeout=30000)
    time.sleep(2)

    # Handle cookie banner if present
    try:
        cookie_btn = page.locator("text=Accetta").first
        if cookie_btn.is_visible(timeout=3000):
            cookie_btn.click()
            time.sleep(1)
    except:
        pass

    # Check if already logged in (lesson content visible)
    if page.locator(".course-section").count() > 0:
        print("[LOGIN] Already logged in via saved session!")
        return True

    # Find and fill login form
    print("[LOGIN] Filling login form...")
    # Try iframe login first
    try:
        frame = page.frame_locator("iframe").first
        frame.locator("#login-email").fill(email, timeout=5000)
        frame.locator("#login-password").fill(password)
        frame.locator("button[type='submit']").click()
    except:
        # Try direct login fields
        try:
            page.locator("#login-email, input[type='email']").first.fill(email, timeout=5000)
            page.locator("#login-password, input[type='password']").first.fill(password)
            page.locator("button[type='submit'], input[type='submit']").first.click()
        except:
            # Navigate to explicit login page
            page.goto("https://www.andrei-copy.com/account/frame/login", wait_until="networkidle")
            time.sleep(2)
            page.locator("#login-email, input[type='email']").first.fill(email, timeout=5000)
            page.locator("#login-password, input[type='password']").first.fill(password)
            page.locator("button[type='submit'], input[type='submit']").first.click()

    print("[LOGIN] Waiting for login to complete...")
    time.sleep(5)
    page.wait_for_load_state("networkidle", timeout=15000)
    print("[LOGIN] Login complete!")
    return True

def scrape_lesson(page, slug):
    """Navigate to lesson page and extract all text content."""
    url = f"{BASE_URL}/{slug}"
    print(f"[SCRAPE] Navigating to {url}")
    page.goto(url, wait_until="networkidle", timeout=30000)
    time.sleep(3)

    # Handle cookie banner again
    try:
        cookie_btn = page.locator("text=Accetta").first
        if cookie_btn.is_visible(timeout=2000):
            cookie_btn.click()
            time.sleep(1)
    except:
        pass

    # Extract all text content
    content = page.inner_text("body")

    # Try to find Vimeo video URL
    vimeo_url = None
    iframes = page.locator("iframe").all()
    for iframe in iframes:
        src = iframe.get_attribute("src") or ""
        if "vimeo" in src or "player.vimeo" in src:
            vimeo_url = src
            break

    # Also check for video elements
    if not vimeo_url:
        videos = page.locator("video source").all()
        for v in videos:
            src = v.get_attribute("src") or ""
            if src:
                vimeo_url = src
                break

    # Extract all links on page
    links = []
    for a in page.locator("a[href]").all():
        href = a.get_attribute("href") or ""
        text = a.inner_text().strip()
        if href and text and not href.startswith("#"):
            links.append({"text": text, "href": href})

    return {
        "content": content,
        "vimeo_url": vimeo_url,
        "links": links,
        "page_url": url
    }

def download_video_yt_dlp(vimeo_url, output_path, referer=None):
    """Download video using yt-dlp with session cookies."""
    print(f"[VIDEO] Downloading from {vimeo_url}")
    cmd = [
        "yt-dlp",
        "--no-check-certificates",
        "-o", str(output_path),
        "--referer", referer or BASE_URL,
    ]
    # Add cookies from storage if available
    if STORAGE_FILE.exists():
        # yt-dlp can use browser cookies
        cmd.extend(["--cookies-from-browser", "chromium"])
    cmd.append(vimeo_url)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if result.returncode == 0:
            print(f"[VIDEO] Downloaded to {output_path}")
            return True
        else:
            print(f"[VIDEO] yt-dlp failed: {result.stderr[:500]}")
            return False
    except subprocess.TimeoutExpired:
        print("[VIDEO] Download timed out")
        return False

def extract_frames(video_path, frames_dir, interval=2):
    """Extract frames from video using ffmpeg."""
    frames_dir.mkdir(parents=True, exist_ok=True)
    output_pattern = str(frames_dir / "frame-%03d.png")
    cmd = [
        "ffmpeg", "-i", str(video_path),
        "-vf", f"fps=1/{interval}",
        output_pattern,
        "-y"
    ]
    print(f"[FRAMES] Extracting frames every {interval}s from {video_path}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if result.returncode == 0:
        frame_count = len(list(frames_dir.glob("frame-*.png")))
        print(f"[FRAMES] Extracted {frame_count} frames")
        return frame_count
    else:
        print(f"[FRAMES] ffmpeg error: {result.stderr[:500]}")
        return 0

def main():
    args = get_args()

    # Setup output directory
    script_dir = Path(__file__).parent
    if args.output_dir:
        out_dir = Path(args.output_dir)
    else:
        out_dir = script_dir / "lessons" / f"lezione-{args.lesson_number}"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Setup storage directory
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)

        # Load saved session if available
        context_opts = {"viewport": {"width": 1920, "height": 1080}}
        if STORAGE_FILE.exists():
            print(f"[SESSION] Loading saved session from {STORAGE_FILE}")
            context_opts["storage_state"] = str(STORAGE_FILE)

        context = browser.new_context(**context_opts)
        page = context.new_page()

        # Login
        login(page, args.email, args.password)

        # Save session state
        context.storage_state(path=str(STORAGE_FILE))
        print(f"[SESSION] Saved session to {STORAGE_FILE}")

        # Scrape lesson
        data = scrape_lesson(page, args.slug)

        # Save raw page content
        raw_file = out_dir / "_page_raw.txt"
        with open(raw_file, "w", encoding="utf-8") as f:
            f.write(data["content"])
        print(f"[SCRAPE] Page content saved to {raw_file}")

        # Save metadata
        meta = {
            "slug": args.slug,
            "lesson_number": args.lesson_number,
            "page_url": data["page_url"],
            "vimeo_url": data["vimeo_url"],
            "links": data["links"],
            "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(out_dir / "_scrape_meta.json", "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)

        # Download video if Vimeo URL found
        if data["vimeo_url"] and not args.skip_video:
            video_dir = out_dir / "video"
            video_dir.mkdir(exist_ok=True)
            video_path = video_dir / f"lezione-{args.lesson_number}.mp4"

            # For Vimeo private videos, we might need to use page context
            # Try direct download with yt-dlp first
            if not download_video_yt_dlp(data["vimeo_url"], video_path, data["page_url"]):
                print("[VIDEO] yt-dlp failed, trying alternative methods...")
                # Try downloading from page directly
                # Save page cookies for yt-dlp
                cookies = context.cookies()
                cookie_file = out_dir / "_cookies.json"
                with open(cookie_file, "w") as f:
                    json.dump(cookies, f)
                print(f"[VIDEO] Cookies saved to {cookie_file} for manual retry")
        elif not args.skip_video:
            print("[VIDEO] No Vimeo URL found on page")

        # Extract frames if video exists
        if not args.skip_video:
            video_files = list((out_dir / "video").glob("*.mp4")) if (out_dir / "video").exists() else []
            if not video_files:
                video_files = list(out_dir.glob("video.mp4"))
            if video_files:
                frames_dir = out_dir / "frames"
                extract_frames(video_files[0], frames_dir, args.frame_interval)
            else:
                print("[FRAMES] No video file found, skipping frame extraction")

        browser.close()

    print(f"\n[DONE] Lesson {args.lesson_number} scraped to {out_dir}")
    print(f"  - Page content: {out_dir / '_page_raw.txt'}")
    if (out_dir / "frames").exists():
        frame_count = len(list((out_dir / "frames").glob("frame-*.png")))
        print(f"  - Frames: {frame_count} in {out_dir / 'frames'}")

if __name__ == "__main__":
    main()
