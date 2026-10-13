#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parse_notebook_md.py
Bộ bóc tách tự động tệp Markdown (.md) được tạo từ Gemini Notebook / NotebookLM
thành tệp cấu trúc JSON chuẩn cho WebApp BANDOHOCTAP.VN.
"""

import os
import sys
import re
import json
import argparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def parse_markdown_to_day_json(md_path, day_number=1, lesson_id=None, title=None):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Trích xuất Tiêu đề & ID nếu chưa truyền
    if not title:
        m_title = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = m_title.group(1).strip() if m_title else f"Ngày {day_number:02d}: Bài học Toán 9"

    if not lesson_id:
        m_id = re.search(r"ID[:\s]+([A-Za-z0-9_]+)", content)
        lesson_id = m_id.group(1).strip() if m_id else f"K9_Toan_C1_N{day_number:02d}"

    day_str = f"day-{day_number:02d}"

    # Cấu trúc JSON cơ sở
    day_data = {
        "day": day_number,
        "id": lesson_id,
        "title": title,
        "download_links": {
            "docx": f"assets/{day_str}/Phieu_Hoc_Tap_Ngay_{day_number}.pdf",
            "infographic": f"assets/{day_str}/infographic.png"
        },
        "shorts": {
            "heading": "BỘ BA MICRO-SHORTS TỰ HỌC (30s - 45s)",
            "subheading": "Xem ngắn để tháo gỡ từng điểm nghẽn kiến thức trong ngày:",
            "clips": []
        },
        "infographic_tab": {
            "heading": "SƠ ĐỒ TƯ DUY & TÀI LIỆU TẢI VỀ",
            "subheading": "Tóm tắt Khung công thức vàng & Bộ tài liệu in ấn ra giấy:",
            "image_url": f"assets/{day_str}/infographic.png",
            "theory_sections": []
        },
        "skeleton_tab": {
            "heading": "THỬ THÁCH ĐIỀN KHUYẾT SKELETON NOTES",
            "subheading": "Điền kết quả đúng vào các ô trống dưới đây để hoàn thiện ghi nhớ:",
            "questions": []
        },
        "quiz_tab": {
            "heading": "THỬ THÁCH TRẮC NGHIỆM ĐIỂM 9+",
            "subheading": "Kiểm tra kiến thức từ nhận biết đến vận dụng thực tế:",
            "questions": []
        },
        "stem3d_tab": {
            "title": f"Phòng Thí Nghiệm STEM 3D - Ngày {day_number:02d}",
            "src": "assets/stem_labs/songuyen.html"
        }
    }

    # 1. Trích xuất Clips Shorts
    # Tìm các mẫu như: Clip 1: Zombie Bẫy Lỗi...
    clip_matches = re.findall(r"(?:Clip|Short|Video)\s+(\d+)[:\s]+([^\n]+)", content, re.IGNORECASE)
    if clip_matches:
        for c_num, c_title in clip_matches[:3]:
            badge = "Bẫy Zombie" if "zombie" in c_title.lower() or "bẫy" in c_title.lower() else "Bí kíp 9+"
            day_data["shorts"]["clips"].append({
                "id": f"clip{c_num}",
                "tag": f"Clip {c_num}: {c_title.strip()}",
                "title": c_title.strip(),
                "video_url": f"assets/{day_str}/clip{c_num}.mp4",
                "thumbnail": f"assets/{day_str}/infographic.png",
                "badge": badge,
                "desc": f"Tập trung tháo gỡ điểm nghẽn then chốt của {c_title.strip()}."
            })
    else:
        # Fallback 3 clips mặc định
        day_data["shorts"]["clips"] = [
            {
                "id": "clip1",
                "tag": "Clip 1: Zombie Bẫy Lỗi",
                "title": "Cảnh báo bẫy sai lầm phổ biến",
                "video_url": f"assets/{day_str}/clip1.mp4",
                "thumbnail": f"assets/{day_str}/infographic.png",
                "badge": "Bẫy Zombie",
                "desc": "Tháo gỡ lỗi sai học sinh hay vấp phải."
            },
            {
                "id": "clip2",
                "tag": "Clip 2: Bí Kíp 9+",
                "title": "Kỹ thuật giải nhanh mẫu chốt",
                "video_url": f"assets/{day_str}/clip2.mp4",
                "thumbnail": f"assets/{day_str}/infographic.png",
                "badge": "Bí kíp 9+",
                "desc": "Kỹ thuật biến đổi không bị nhầm dấu."
            },
            {
                "id": "clip3",
                "tag": "Clip 3: Toán Thực Tế",
                "title": "Ứng dụng trực quan hóa",
                "video_url": f"assets/{day_str}/clip3.mp4",
                "thumbnail": f"assets/{day_str}/infographic.png",
                "badge": "Toán thực tế",
                "desc": "Liên hệ thực tế sinh động."
            }
        ]

    # 2. Trích xuất Lý Thuyết Cốt Lõi
    theory_match = re.search(r"(?:LÝ THUYẾT|TÓM TẮT|QUY TẮC)([\s\S]*?)(?=(?:SKELETON|ĐIỀN KHUYẾT|TRẮC NGHIỆM|BÀI TẬP|$))", content, re.IGNORECASE)
    if theory_match:
        raw_theory = theory_match.group(1).strip()
        lines = [line.strip() for line in raw_theory.split("\n") if line.strip()]
        rules = []
        for line in lines:
            if line.startswith("-") or line.startswith("*") or re.match(r"^\d+\.", line):
                rules.append(re.sub(r"^[-*\d.]+\s*", "", line))
        if rules:
            day_data["infographic_tab"]["theory_sections"].append({
                "title": "Kiến Thức Cốt Lõi Cần Nhớ",
                "rules": rules[:5]
            })

    # 3. Trích xuất Câu Hỏi Trắc Nghiệm
    # Mẫu: Câu 1 ... A. ... B. ... C. ... D. ... Đáp án / Giải thích
    q_blocks = re.split(r"(?:Câu|Bài)\s+\d+[:.]", content)[1:]
    q_index = 1
    for block in q_blocks[:4]:
        lines = [l.strip() for l in block.split("\n") if l.strip()]
        if not lines: continue
        q_text = lines[0]

        # Options A, B, C, D
        opts = re.findall(r"([A-D])[\.:\)]\s*([^\n]+)", block)
        if len(opts) >= 4:
            options = [o[1].strip() for o in opts[:4]]
            correct_idx = 0
            # Tìm đáp án
            m_ans = re.search(r"(?:Đáp án|Chọn)[:\s]*([A-D])", block, re.IGNORECASE)
            if m_ans:
                correct_letter = m_ans.group(1).upper()
                correct_idx = ord(correct_letter) - ord('A')

            # Giải thích
            m_exp = re.search(r"(?:Giải thích|Lời giải|Bẫy)[:\s]*([^\n]+)", block, re.IGNORECASE)
            explanation = m_exp.group(1).strip() if m_exp else "Xem lại quy tắc biến đổi tương đương."

            level = "Nhận biết"
            if q_index == 2 or "bẫy" in block.lower():
                level = "Thông hiểu - Cảnh báo bẫy"
            elif q_index == 3:
                level = "Vận dụng"
            elif q_index == 4:
                level = "Thực tế"

            day_data["quiz_tab"]["questions"].append({
                "id": f"q{q_index}",
                "level": level,
                "question": f"Câu {q_index}: {q_text}",
                "options": options,
                "correct_index": correct_idx,
                "explanation": explanation
            })
            q_index += 1

    return day_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chuyển đổi file .md học liệu thành JSON cho WebApp")
    parser.add_argument("--md", required=True, help="Đường dẫn file .md")
    parser.add_argument("--day", type=int, default=1, help="Số thứ tự ngày (1-30)")
    parser.add_argument("--out", help="Đường dẫn file JSON đầu ra")
    args = parser.parse_args()

    out_file = args.out or f"data/day-{args.day:02d}.json"
    result = parse_markdown_to_day_json(args.md, args.day)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã tạo thành công {out_file}")
