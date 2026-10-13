#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publish_lesson.py
Quy trình tự động hóa xuất bản 1 bài học mới vào WebApp BANDOHOCTAP.VN.
"""

import os
import sys
import shutil
import json
import argparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from parse_notebook_md import parse_markdown_to_day_json

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
PUBLIC_ASSETS_DIR = os.path.join(PROJECT_ROOT, "public", "assets")

def publish(day, md_path=None, json_path=None, docx_path=None, infographic_path=None, video_path=None, auto_unlock=True):
    day_str = f"day-{day:02d}"
    target_asset_dir = os.path.join(ASSETS_DIR, day_str)
    target_public_dir = os.path.join(PUBLIC_ASSETS_DIR, day_str)
    os.makedirs(target_asset_dir, exist_ok=True)
    os.makedirs(target_public_dir, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

    print(f"🚀 BẮT ĐẦU XUẤT BẢN HỌC LIỆU NGÀY {day:02d}...")

    # 1. Sao chép các tệp tài nguyên nếu có
    if docx_path and os.path.exists(docx_path):
        ext = os.path.splitext(docx_path)[1]
        dest = os.path.join(target_asset_dir, f"Phieu_Hoc_Tap_Ngay_{day}{ext}")
        shutil.copy2(docx_path, dest)
        shutil.copy2(docx_path, os.path.join(target_public_dir, f"Phieu_Hoc_Tap_Ngay_{day}{ext}"))
        print(f"  📄 Đã sao chép Phiếu học tập -> {dest}")

    if infographic_path and os.path.exists(infographic_path):
        dest = os.path.join(target_asset_dir, "infographic.png")
        shutil.copy2(infographic_path, dest)
        shutil.copy2(infographic_path, os.path.join(target_public_dir, "infographic.png"))
        print(f"  🖼️ Đã sao chép Infographic -> {dest}")

    if video_path and os.path.exists(video_path):
        dest = os.path.join(target_asset_dir, "clip1.mp4")
        shutil.copy2(video_path, dest)
        shutil.copy2(video_path, os.path.join(target_public_dir, "clip1.mp4"))
        print(f"  🎬 Đã sao chép Video bài giảng -> {dest}")

    # 2. Xử lý dữ liệu bài học JSON
    target_json = os.path.join(DATA_DIR, f"day-{day:02d}.json")
    if json_path and os.path.exists(json_path):
        shutil.copy2(json_path, target_json)
        with open(target_json, "r", encoding="utf-8") as f:
            lesson_data = json.load(f)
    elif md_path and os.path.exists(md_path):
        lesson_data = parse_markdown_to_day_json(md_path, day)
        with open(target_json, "w", encoding="utf-8") as f:
            json.dump(lesson_data, f, ensure_ascii=False, indent=2)
        print(f"  🧠 Đã bóc tách tệp Markdown thành công -> {target_json}")
    else:
        if os.path.exists(target_json):
            with open(target_json, "r", encoding="utf-8") as f:
                lesson_data = json.load(f)
        else:
            print(f"⚠️ Chưa có file .md hoặc JSON cho ngày {day}.")
            return

    # 3. Cập nhật danh mục curriculum.json
    curr_path = os.path.join(DATA_DIR, "curriculum.json")
    if os.path.exists(curr_path):
        with open(curr_path, "r", encoding="utf-8") as f:
            curr = json.load(f)

        updated = False
        for item in curr:
            if item.get("day") == day:
                if "title" in lesson_data:
                    item["title"] = lesson_data["title"]
                if auto_unlock:
                    item["status"] = "unlocked"
                updated = True
                break

        if not updated:
            curr.append({
                "day": day,
                "id": lesson_data.get("id", f"K9_Toan_C1_N{day:02d}"),
                "title": lesson_data.get("title", f"Ngày {day:02d}: Bài học mới"),
                "status": "unlocked" if auto_unlock else "locked",
                "file": f"data/day-{day:02d}.json"
            })

        with open(curr_path, "w", encoding="utf-8") as f:
            json.dump(curr, f, ensure_ascii=False, indent=2)
        print(f"  📋 Đã cập nhật danh mục 30 ngày trong curriculum.json (Đã mở khóa Ngày {day:02d})")

    print(f"🎉 HOÀN TẤT XUẤT BẢN NGÀY {day:02d} VÀO WEBAPP!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tự động hóa xuất bản bài học vào WebApp")
    parser.add_argument("--day", type=int, required=True, help="Số ngày (1-30)")
    parser.add_argument("--md", help="Đường dẫn file .md bóc tách từ Gemini Notebook")
    parser.add_argument("--json", help="Đường dẫn file JSON có sẵn")
    parser.add_argument("--docx", help="Đường dẫn file Phiếu học tập Word (.docx) hoặc .pdf")
    parser.add_argument("--infographic", help="Đường dẫn file ảnh Infographic (.png)")
    parser.add_argument("--video", help="Đường dẫn file video bài giảng (.mp4)")
    args = parser.parse_args()

    publish(args.day, args.md, args.json, args.docx, args.infographic, args.video)
