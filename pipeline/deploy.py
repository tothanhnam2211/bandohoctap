#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deploy.py
Tự động đẩy toàn bộ WebApp lên Cloudflare Pages hoặc máy chủ Web.
"""

import os
import sys
import subprocess
import argparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def deploy_cloudflare(project_name="bandohoctap"):
    print("🌐 Đang đẩy WebApp lên Cloudflare Pages...")
    cmd = f"npx wrangler pages deploy \"{PROJECT_ROOT}\" --project-name {project_name}"
    try:
        res = subprocess.run(cmd, shell=True, check=True, cwd=PROJECT_ROOT)
        print("✅ Triển khai thành công lên Cloudflare Pages!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi triển khai Cloudflare: {e}")
        return False

def deploy_git(commit_message="Tự động cập nhật học liệu bài học mới"):
    print("📦 Đang đẩy thay đổi lên Git...")
    try:
        subprocess.run("git add .", shell=True, check=True, cwd=PROJECT_ROOT)
        subprocess.run(f'git commit -m "{commit_message}"', shell=True, check=True, cwd=PROJECT_ROOT)
        subprocess.run("git push", shell=True, check=True, cwd=PROJECT_ROOT)
        print("✅ Đã push mã nguồn và dữ liệu lên Git thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git push chưa được thiết lập hoặc có lỗi: {e}")
        return False

def start_local_preview(port=8080):
    print(f"🚀 Đang khởi động máy chủ xem trước tại: http://localhost:{port}")
    cmd = f"{sys.executable} -m http.server {port}"
    subprocess.run(cmd, shell=True, cwd=PROJECT_ROOT)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Triển khai WebApp lên Internet")
    parser.add_argument("--mode", choices=["cloudflare", "git", "local"], default="local", 
                        help="Phương thức triển khai: cloudflare, git hoặc local preview")
    parser.add_argument("--project", default="bandohoctap", help="Tên project Cloudflare Pages")
    parser.add_argument("--port", type=int, default=8080, help="Cổng chạy preview nội bộ")
    args = parser.parse_args()

    if args.mode == "cloudflare":
        deploy_cloudflare(args.project)
    elif args.mode == "git":
        deploy_git()
    else:
        start_local_preview(args.port)
