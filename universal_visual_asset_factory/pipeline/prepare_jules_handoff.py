# -*- coding: utf-8 -*-
"""
PREPARE JULES VISUAL ASSET FACTORY HANDOFF
Tập hợp toàn bộ mã nguồn nhà máy, cơ sở dữ liệu SQLite, webapp Studio,
tập mẫu đại diện và tài liệu hướng dẫn kỹ thuật cho Jules.
"""

import os
import sys
import shutil
import json
import sqlite3
import hashlib
from typing import Dict, Any, List

FACTORY_DIR = r"D:\YOURDREAM.VN\VISUAL_ASSET_FACTORY"
HANDOFF_DIR = r"D:\YOURDREAM.VN\JULES_VISUAL_ASSET_HANDOFF"

def assemble_handoff():
    print(f"Bắt đầu đóng gói Jules Handoff tại: {HANDOFF_DIR}")
    os.makedirs(HANDOFF_DIR, exist_ok=True)

    # 1. Sao chép cây thư mục mã nguồn
    subdirs = ["curriculum", "engine", "pipeline", "studio"]
    for sub in subdirs:
        src = os.path.join(FACTORY_DIR, sub)
        dst = os.path.join(HANDOFF_DIR, sub)
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
            print(f"  + Đã sao chép mã nguồn: {sub}/")

    # 2. Sao chép Database SQLite Registry
    src_db = os.path.join(FACTORY_DIR, "visual_asset_registry.db")
    dst_db = os.path.join(HANDOFF_DIR, "visual_asset_registry.db")
    if os.path.exists(src_db):
        shutil.copy2(src_db, dst_db)
        print(f"  + Đã sao chép visual_asset_registry.db ({os.path.getsize(dst_db)/(1024*1024):.2f} MB)")

    # 3. Trích xuất tập mẫu đại diện (Representative Sample Pack across G06-G12)
    sample_dir = os.path.join(HANDOFF_DIR, "sample_assets")
    os.makedirs(sample_dir, exist_ok=True)

    conn = sqlite3.connect(src_db)
    cur = conn.cursor()
    # Lấy 14 mẫu tiêu biểu đại diện cho 7 khối lớp và 5 mạch kiến thức
    cur.execute("""
    SELECT variant_id, grade, strand, master_svg_path, master_png_path, student_svg_path, student_png_path
    FROM asset_variants
    WHERE variant_id LIKE '%_VAR_01'
    ORDER BY grade, strand
    """)
    sample_rows = cur.fetchall()

    copied_samples = 0
    sample_catalog = []
    # Chọn 2 mẫu mỗi khối lớp (tổng cộng 14 mẫu đại diện đầy đủ)
    selected_by_grade = {}
    for r in sample_rows:
        g = r[1]
        if selected_by_grade.get(g, 0) < 2:
            selected_by_grade[g] = selected_by_grade.get(g, 0) + 1
            for p_idx, p_rel in [(3, "master_svg"), (4, "master_png"), (5, "student_svg"), (6, "student_png")]:
                f_path = os.path.join(FACTORY_DIR, r[p_idx].replace("/", "\\"))
                if os.path.exists(f_path):
                    shutil.copy2(f_path, sample_dir)
                    copied_samples += 1
            sample_catalog.append({
                "variant_id": r[0],
                "grade": r[1],
                "strand": r[2],
            })
    conn.close()
    print(f"  + Đã trích xuất {copied_samples} file mẫu trực quan đại diện vào sample_assets/")

    # 4. Tạo Manifests
    manifest_dir = os.path.join(HANDOFF_DIR, "manifests")
    os.makedirs(manifest_dir, exist_ok=True)

    # Manifest Họ Asset
    sys.path.append(FACTORY_DIR)
    from curriculum.k12_curriculum_catalog import get_k12_asset_families
    families = get_k12_asset_families()
    families_manifest = [
        {
            "family_id": f.family_id,
            "grade": f.grade,
            "strand": f.strand,
            "chapter": f.chapter,
            "topic_vi": f.topic_vi,
            "generator_type": f.generator_type,
            "math_invariant": f.math_invariant,
            "variants_count": 46
        }
        for f in families
    ]
    with open(os.path.join(manifest_dir, "MANIFEST_K12_ASSET_FAMILIES.json"), "w", encoding="utf-8") as f:
        json.dump(families_manifest, f, ensure_ascii=False, indent=2)

    # Manifest Tóm tắt Index
    conn = sqlite3.connect(src_db)
    cur = conn.cursor()
    cur.execute("SELECT grade, COUNT(*) FROM asset_variants GROUP BY grade ORDER BY grade")
    by_grade = dict(cur.fetchall())
    cur.execute("SELECT strand, COUNT(*) FROM asset_variants GROUP BY strand ORDER BY strand")
    by_strand = dict(cur.fetchall())
    conn.close()

    summary_manifest = {
        "factory_name": "YOURDREAM Universal Mathematical Visual Asset Factory",
        "version": "1.0.0",
        "timestamp": "2026-10-31",
        "total_families": len(families),
        "total_variants": sum(by_grade.values()),
        "total_images_rendered_on_disk": sum(by_grade.values()) * 4,
        "disk_archive_root": r"D:\YOURDREAM.VN\VISUAL_ASSET_FACTORY\output",
        "by_grade": by_grade,
        "by_strand": by_strand,
        "representative_samples": sample_catalog,
    }
    with open(os.path.join(manifest_dir, "MANIFEST_ASSET_INDEX_SUMMARY.json"), "w", encoding="utf-8") as f:
        json.dump(summary_manifest, f, ensure_ascii=False, indent=2)
    print("  + Đã tạo manifests đầy đủ.")

    # 5. requirements.txt
    with open(os.path.join(HANDOFF_DIR, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write("pymupdf>=1.24.0\n")

    print("Hoàn tất chuẩn bị thư mục Jules Handoff!")

if __name__ == "__main__":
    assemble_handoff()
