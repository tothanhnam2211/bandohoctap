#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KỊCH BẢN KIỂM THỬ TRÌNH DUYỆT PLAYWRIGHT CHO LIVING ASSET STUDIO & CÁC SẢN PHẨM ĐẦU RA
Chụp ảnh màn hình thực tế của:
1. Giao diện YOURDREAM_Living_Asset_Studio.html (Thư viện 16 Living Assets 4 mạch).
2. Cửa sổ thao tác trực tiếp (Live Asset Modal) ngay trong Studio.
3. Tab 2: Bộ Sinh Trải Nghiệm Từ Cấu Trúc Mới (Generative Composer).
4. Một Living Asset độc lập (YD-LA-NUM-G6-01 — Lát gạch ƯCLN với phản ví dụ và nghiệm chuẩn).
"""

from __future__ import annotations
import json
import shutil
import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")

FACTORY_DIR = Path(os.environ.get("LIVING_ASSET_FACTORY_DIR") or Path(__file__).resolve().parent.parent)
SCREENSHOT_DIR = FACTORY_DIR / "output" / "studio_screenshots"
ARTIFACT_DIR = Path(os.environ.get("ARTIFACT_DIR") or r"C:\Users\Admin\.gemini\antigravity\brain\5d2278ec-09f5-47e5-9e57-a9d76d06c1fa")


def run_browser_verification() -> dict:
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    studio_uri = (FACTORY_DIR / "YOURDREAM_Living_Asset_Studio.html").as_uri()
    asset01_uri = (FACTORY_DIR / "output" / "interactive_html" / "YD-LA-NUM-G6-01.html").as_uri()
    page_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 920})
        page.on("pageerror", lambda err: page_errors.append(str(err)))

        # 1. Open Studio Library Tab
        page.goto(studio_uri, wait_until="networkidle")
        cards_count = page.locator(".asset-card").count()
        s1 = SCREENSHOT_DIR / "studio_tab1_library_16_assets.png"
        page.screenshot(path=str(s1), full_page=False)

        # 2. Switch to Tab 2 (Generative Experience Composer) & test Test A and Test D
        page.click("#tabBtn2")
        page.wait_for_timeout(300)
        s2 = SCREENSHOT_DIR / "studio_tab2_generative_composer.png"
        page.screenshot(path=str(s2), full_page=False)

        # Click Test D (Unsupported Calculus structure)
        page.click("button:has-text('Test D')")
        page.wait_for_timeout(250)
        s3 = SCREENSHOT_DIR / "studio_tab2_testD_unsupported_honest.png"
        page.screenshot(path=str(s3), full_page=False)

        # 3. Open standalone interactive asset YD-LA-NUM-G6-01 (Tile GCD)
        page.goto(asset01_uri, wait_until="networkidle")
        page.wait_for_timeout(300)
        s4 = SCREENSHOT_DIR / "asset01_courtyard_counterexample_d5.png"
        page.screenshot(path=str(s4), full_page=False)

        # Move slider to d = 6 and check causal balance
        page.evaluate("() => { const s = document.getElementById('trialSlider'); s.value = 6; s.dispatchEvent(new Event('input')); }")
        page.wait_for_timeout(200)
        page.click("button:has-text('Kiểm Tra Cân Bằng Cán Cân')")
        page.wait_for_timeout(300)
        s5 = SCREENSHOT_DIR / "asset01_courtyard_solution_d6.png"
        page.screenshot(path=str(s5), full_page=False)

        # 4. Open Rate Asset YD-LA-ALG-G8-07 (Truck Convoy & Dynamic Causal Balance Scale)
        asset07_uri = (FACTORY_DIR / "output" / "interactive_html" / "YD-LA-ALG-G8-07.html").as_uri()
        page.goto(asset07_uri, wait_until="networkidle")
        page.wait_for_timeout(300)
        s6 = SCREENSHOT_DIR / "asset07_causal_balance_off_x10.png"
        page.screenshot(path=str(s6), full_page=False)

        # Move slider to x = 12 and check balance
        page.evaluate("() => { const s = document.getElementById('trialSlider'); s.value = 12; s.dispatchEvent(new Event('input')); }")
        page.wait_for_timeout(200)
        page.click("button:has-text('Kiểm Tra Cân Bằng Cán Cân')")
        page.wait_for_timeout(300)
        s7 = SCREENSHOT_DIR / "asset07_causal_balance_equil_x12.png"
        page.screenshot(path=str(s7), full_page=False)

        browser.close()

    for img in (s1, s2, s3, s4, s5, s6, s7):
        shutil.copy2(img, ARTIFACT_DIR / img.name)

    report = {
        "studio_cards_rendered": cards_count,
        "page_errors": page_errors,
        "screenshots": [str(s1), str(s2), str(s3), str(s4), str(s5), str(s6), str(s7)],
    }
    (FACTORY_DIR / "output" / "studio_browser_verification.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


if __name__ == "__main__":
    run_browser_verification()
