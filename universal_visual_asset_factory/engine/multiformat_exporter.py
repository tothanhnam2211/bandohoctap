# -*- coding: utf-8 -*-
"""
MULTIFORMAT EXPORTER
Kết xuất đồng thời 4 định dạng trực quan cho mỗi biến thể:
1. Master SVG (Bản Thầy / Vector gốc độ phân giải vô hạn)
2. Master PNG (Bản Thầy / Bitmap 150 DPI trong suốt, in ấn & web sắc nét)
3. Student SVG (Phiếu Học sinh / Vector có dấu '?' và khoảng trống thực hành)
4. Student PNG (Phiếu Học sinh / Bitmap 150 DPI trong suốt)
5. Metadata JSON chuẩn hóa đi kèm SHA-256
"""

import os
import json
import hashlib
from typing import Dict, Any, Tuple
import pymupdf

from engine.asset_renderer_dispatch import dispatch_render_svg

def export_variant(
    variant: Dict[str, Any],
    base_output_dir: str,
) -> Dict[str, Any]:
    """
    Kết xuất 4 file trực quan + 1 file JSON metadata cho một variant.
    Trả về dict thông tin tóm tắt để lưu vào SQLite registry.
    """
    grade = variant["grade"]
    g_str = f"G{grade:02d}"
    v_id = variant["variant_id"]
    gtype = variant["generator_type"]
    params = variant["params"]
    title = variant["title"]

    # Target directories
    svg_dir = os.path.join(base_output_dir, "output", "svg", g_str)
    png_dir = os.path.join(base_output_dir, "output", "png", g_str)
    json_dir = os.path.join(base_output_dir, "output", "json", g_str)

    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(png_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)

    # 1. Render Master SVG
    svg_master_content = dispatch_render_svg(
        generator_type=gtype,
        params=params,
        title=title,
        is_student_worksheet=False,
    )
    svg_master_filename = f"{v_id}_master.svg"
    svg_master_path = os.path.join(svg_dir, svg_master_filename)
    with open(svg_master_path, "w", encoding="utf-8") as f:
        f.write(svg_master_content)
    sha_master_svg = hashlib.sha256(svg_master_content.encode("utf-8")).hexdigest()

    # 2. Render Master PNG (150 DPI)
    doc_m = pymupdf.open(stream=svg_master_content.encode("utf-8"), filetype="svg")
    pix_m = doc_m[0].get_pixmap(dpi=150, alpha=True)
    png_master_bytes = pix_m.tobytes(output="png")
    doc_m.close()

    png_master_filename = f"{v_id}_master.png"
    png_master_path = os.path.join(png_dir, png_master_filename)
    with open(png_master_path, "wb") as f:
        f.write(png_master_bytes)
    sha_master_png = hashlib.sha256(png_master_bytes).hexdigest()

    # 3. Render Student SVG (Worksheet)
    svg_student_content = dispatch_render_svg(
        generator_type=gtype,
        params=params,
        title=title,
        is_student_worksheet=True,
    )
    svg_student_filename = f"{v_id}_student.svg"
    svg_student_path = os.path.join(svg_dir, svg_student_filename)
    with open(svg_student_path, "w", encoding="utf-8") as f:
        f.write(svg_student_content)
    sha_student_svg = hashlib.sha256(svg_student_content.encode("utf-8")).hexdigest()

    # 4. Render Student PNG (150 DPI)
    doc_s = pymupdf.open(stream=svg_student_content.encode("utf-8"), filetype="svg")
    pix_s = doc_s[0].get_pixmap(dpi=150, alpha=True)
    png_student_bytes = pix_s.tobytes(output="png")
    doc_s.close()

    png_student_filename = f"{v_id}_student.png"
    png_student_path = os.path.join(png_dir, png_student_filename)
    with open(png_student_path, "wb") as f:
        f.write(png_student_bytes)
    sha_student_png = hashlib.sha256(png_student_bytes).hexdigest()

    # 5. Metadata Record
    meta = {
        "variant_id": v_id,
        "family_id": variant["family_id"],
        "grade": grade,
        "strand": variant["strand"],
        "chapter": variant["chapter"],
        "topic_vi": variant["topic_vi"],
        "title": title,
        "generator_type": gtype,
        "math_invariant": variant["math_invariant"],
        "files": {
            "master_svg": f"output/svg/{g_str}/{svg_master_filename}",
            "master_png": f"output/png/{g_str}/{png_master_filename}",
            "student_svg": f"output/svg/{g_str}/{svg_student_filename}",
            "student_png": f"output/png/{g_str}/{png_student_filename}",
        },
        "hashes": {
            "master_svg": sha_master_svg,
            "master_png": sha_master_png,
            "student_svg": sha_student_svg,
            "student_png": sha_student_png,
        },
        "sizes": {
            "master_svg_bytes": len(svg_master_content),
            "master_png_bytes": len(png_master_bytes),
            "student_svg_bytes": len(svg_student_content),
            "student_png_bytes": len(png_student_bytes),
        }
    }

    json_filename = f"{v_id}_meta.json"
    json_path = os.path.join(json_dir, json_filename)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    return meta
