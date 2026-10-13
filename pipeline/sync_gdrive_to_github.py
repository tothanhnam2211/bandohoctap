#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_gdrive_to_github.py
Cầu nối tự động hóa toàn diện:
Google Drive (G:\Drive của tôi\BANDOHOCTAP_NGUON) -> WebApp Compiler -> GitHub (Auto Push)
"""

import os
import sys
import glob
import re
import subprocess
import argparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIPELINE_DIR = os.path.join(PROJECT_ROOT, "pipeline")
sys.path.insert(0, PIPELINE_DIR)
from publish_lesson import publish

def find_gdrive_source():
    """Tự động tìm kiếm thư mục nguồn BANDOHOCTAP_NGUON trên ổ G:"""
    potential_roots = [
        "G:\\Drive của tôi\\BANDOHOCTAP_NGUON",
        "G:\\My Drive\\BANDOHOCTAP_NGUON",
    ]
    for p in potential_roots:
        if os.path.exists(p):
            return p

    # Quét đệ quy cấp 1 trên G:\ nếu tên thư mục biến thiên
    if os.path.exists("G:\\"):
        for entry in os.listdir("G:\\"):
            full = os.path.join("G:\\", entry)
            if os.path.isdir(full):
                target = os.path.join(full, "BANDOHOCTAP_NGUON")
                if os.path.exists(target):
                    return target
    return None

def sync_all_from_gdrive(source_dir=None, auto_push=True):
    if not source_dir:
        source_dir = find_gdrive_source()

    if not source_dir or not os.path.exists(source_dir):
        print(f"❌ Không tìm thấy thư mục nguồn Google Drive tại: {source_dir}")
        print("💡 Hãy đảm bảo Google Drive for Desktop (ổ G:) đang chạy.")
        return False

    print("=" * 60)
    print(f"🔄 ĐANG ĐỒNG BỘ TỪ GOOGLE DRIVE:\n   {source_dir}")
    print("=" * 60)

    # Quét tất cả thư mục ngày: Ngay_01, Ngay_02, ...
    subdirs = sorted(os.listdir(source_dir))
    synced_days = []

    for folder_name in subdirs:
        folder_path = os.path.join(source_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue

        # Trích xuất số ngày từ tên thư mục (vd: Ngay_01 -> 1)
        m_day = re.search(r"(\d+)", folder_name)
        if not m_day:
            continue
        day_num = int(m_day.group(1))

        # Tìm các tệp trong thư mục ngày
        md_files = glob.glob(os.path.join(folder_path, "*.md"))
        docx_files = glob.glob(os.path.join(folder_path, "*.docx")) + glob.glob(os.path.join(folder_path, "*.pdf"))
        png_files = glob.glob(os.path.join(folder_path, "*.png")) + glob.glob(os.path.join(folder_path, "*.jpg"))
        mp4_files = glob.glob(os.path.join(folder_path, "*.mp4"))

        md_path = md_files[0] if md_files else None
        docx_path = docx_files[0] if docx_files else None
        infographic_path = png_files[0] if png_files else None
        video_path = mp4_files[0] if mp4_files else None

        print(f"\n📂 Đang xử lý: {folder_name} (Ngày {day_num:02d})")
        if md_path:
            print(f"   - Markdown: {os.path.basename(md_path)}")
        if docx_path:
            print(f"   - Phiếu học tập: {os.path.basename(docx_path)}")
        if infographic_path:
            print(f"   - Infographic: {os.path.basename(infographic_path)}")
        if video_path:
            print(f"   - Video: {os.path.basename(video_path)}")

        publish(
            day=day_num,
            md_path=md_path,
            docx_path=docx_path,
            infographic_path=infographic_path,
            video_path=video_path,
            auto_unlock=True
        )
        synced_days.append(day_num)

    print("\n" + "=" * 60)
    print(f"✅ ĐÃ ĐỒNG BỘ XONG {len(synced_days)} BÀI HỌC VÀO WEBAPP!")
    print("=" * 60)

    # 4. Kiểm tra Git & Đẩy lên GitHub
    if auto_push:
        push_to_github(f"Tự động cập nhật học liệu từ Google Drive: Ngày {', '.join(map(str, synced_days))}")

    return True

def push_to_github(commit_msg):
    print("\n📦 KIỂM TRA THAY ĐỔI VÀ ĐẨY LÊN GITHUB...")
    try:
        # Kiểm tra xem có file nào thay đổi không
        res = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True, cwd=PROJECT_ROOT)
        if not res.stdout.strip():
            print("✨ Không có thay đổi mới nào cần commit lên GitHub.")
            return

        subprocess.run("git add .", shell=True, check=True, cwd=PROJECT_ROOT)
        subprocess.run(f'git commit -m "{commit_msg}"', shell=True, check=True, cwd=PROJECT_ROOT)
        print("✅ Đã tạo Git commit thành công.")

        # Kiểm tra remote origin
        remotes = subprocess.run("git remote", shell=True, capture_output=True, text=True, cwd=PROJECT_ROOT).stdout.strip()
        if "origin" in remotes:
            print("🚀 Đang đẩy dữ liệu lên GitHub (git push origin main)...")
            subprocess.run("git push -u origin main", shell=True, check=True, cwd=PROJECT_ROOT)
            print("🎉 HOÀN TẤT ĐẨY LÊN GITHUB! Website sẽ tự động cập nhật trong giây lát.")
        else:
            print("💡 Git remote 'origin' chưa được gắn.")
            print("👉 Bạn hãy chạy lệnh sau một lần để liên kết với GitHub repo:")
            print("   git remote add origin https://github.com/<tai-khoan>/<ten-repo>.git")
            print("   git push -u origin main")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ Quá trình Git gặp thông báo: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Đồng bộ tự động từ Google Drive vào WebApp và đẩy lên GitHub")
    parser.add_argument("--source", help="Đường dẫn thư mục nguồn (mặc định tự quét ổ G:)")
    parser.add_argument("--no-push", action="store_true", help="Không tự động đẩy lên GitHub")
    args = parser.parse_args()

    sync_all_from_gdrive(source_dir=args.source, auto_push=not args.no_push)
