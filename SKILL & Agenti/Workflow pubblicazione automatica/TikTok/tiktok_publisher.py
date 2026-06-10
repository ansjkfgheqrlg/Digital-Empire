import time
import sys
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.browser_manager import BrowserManager
import config

def publish(file_path, caption, headless=True):
    print(f"[TikTok] Inizio pubblicazione...")
    manager = BrowserManager('TikTok', headless=headless)
    
    try:
        context = manager.get_context()
        page = context.new_page()
        
        page.goto("https://www.tiktok.com/creator-center/upload?from=upload")
        page.wait_for_load_state('networkidle')
        time.sleep(5)
        
        iframe_element = page.locator('iframe[data-tt="Upload_index_iframe"]')
        if iframe_element.is_visible():
            frame = iframe_element.content_frame
        else:
            frame = page

        with frame.expect_file_chooser() as fc_info:
            frame.get_by_text("Select video").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        
        print("[TikTok] Attendere completamento upload...")
        time.sleep(10)
        
        caption_area = frame.locator('.DraftEditor-editorContainer div[contenteditable="true"]')
        caption_area.clear()
        caption_area.fill(caption)
        time.sleep(2)
        
        post_btn = frame.get_by_role("button", name="Post")
        post_btn.click()
        
        print("[TikTok] Cliccato Pubblica. Attendo conferma...")
        time.sleep(5)
        print("[TikTok] Video pubblicato con successo!")
        
    except Exception as e:
        print(f"[TikTok] Errore: {e}")
    finally:
        manager.close()
