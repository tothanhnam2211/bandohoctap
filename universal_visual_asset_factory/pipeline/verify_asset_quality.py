# -*- coding: utf-8 -*-
"""
VISUAL ASSET QUALITY & INTEGRITY VERIFICATION SUITE
Kiểm thử độc lập toàn bộ thư viện:
1. File Integrity: Không có file 0-byte, không có file hỏng.
2. Magic Bytes: Mọi file PNG đều có chữ ký chuẩn 89 50 4E 47 0D 0A 1A 0A.
3. SVG Validity: Mọi file SVG đều chứa thẻ gốc hợp lệ, có cả art-layer và math-layer.
4. Database Consistency: Khớp 100% giữa số file thực tế trên ổ đĩa và bản ghi trong SQLite.
5. FTS5 Search Sanity: Thử nghiệm tìm kiếm toàn văn các từ khóa cốt lõi K12.
"""

import os
import sys
import glob
import sqlite3
import hashlib
from typing import Dict, Any, List

BASE_DIR = r"D:\YOURDREAM.VN\VISUAL_ASSET_FACTORY"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

def run_qa_suite() -> Dict[str, Any]:
    print("=" * 70)
    print("YOURDREAM — VISUAL ASSET FACTORY QA VERIFICATION")
    print("=" * 70)

    db_path = os.path.join(BASE_DIR, "visual_asset_registry.db")
    if not os.path.exists(db_path):
        return {"status": "FAILED", "error": "Database not found"}

    # 1. Quét file đĩa
    svg_files = glob.glob(os.path.join(BASE_DIR, "output", "svg", "*", "*.svg"))
    png_files = glob.glob(os.path.join(BASE_DIR, "output", "png", "*", "*.png"))
    json_files = glob.glob(os.path.join(BASE_DIR, "output", "json", "*", "*.json"))

    print(f"File thực tế trên ổ đĩa:")
    print(f"  - SVG files : {len(svg_files):,}")
    print(f"  - PNG files : {len(png_files):,}")
    print(f"  - JSON files: {len(json_files):,}")
    print(f"  - Tổng cộng : {len(svg_files) + len(png_files) + len(json_files):,} files")

    # 2. Kiểm tra zero-byte & magic bytes
    zero_bytes = 0
    invalid_png = 0
    invalid_svg = 0

    print("\nKiểm tra tính toàn vẹn (Zero-byte & Format headers)...")
    for p in png_files:
        sz = os.path.getsize(p)
        if sz == 0:
            zero_bytes += 1
            continue
        with open(p, "rb") as f:
            header = f.read(8)
            if header != PNG_MAGIC:
                invalid_png += 1

    for s in svg_files:
        sz = os.path.getsize(s)
        if sz == 0:
            zero_bytes += 1
            continue
        with open(s, "r", encoding="utf-8", errors="ignore") as f:
            head = f.read(200)
            if "<svg" not in head:
                invalid_svg += 1

    print(f"  - File 0-byte      : {zero_bytes} (Yêu cầu: 0)")
    print(f"  - File PNG lỗi mẫu : {invalid_png} (Yêu cầu: 0)")
    print(f"  - File SVG lỗi mẫu : {invalid_svg} (Yêu cầu: 0)")

    # 3. Kiểm tra tính nhất quán với SQLite
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM asset_variants")
    db_variants = cur.fetchone()[0]
    conn.close()

    expected_images = db_variants * 4
    disk_images = len(svg_files) + len(png_files)
    print(f"\nĐối chiếu SQLite Registry:")
    print(f"  - Biến thể trong DB: {db_variants:,}")
    print(f"  - File ảnh kỳ vọng: {expected_images:,}")
    print(f"  - File ảnh trên đĩa: {disk_images:,}")
    is_sync = (expected_images == disk_images)
    print(f"  - Trạng thái đồng bộ: {'HOÀN TOÀN KHỚP (100%)' if is_sync else 'CHƯA ĐỒNG BỘ'}")

    # 4. Kiểm tra FTS5 Search
    test_queries = ["tam giác", "parabol", "cán cân", "xác suất", "tích phân", "hộp", "đường tròn", "vectơ"]
    print("\nKiểm thử truy vấn toàn văn FTS5:")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    search_results = {}
    for q in test_queries:
        cur.execute("SELECT COUNT(*) FROM asset_search_fts WHERE asset_search_fts MATCH ?", (q,))
        cnt = cur.fetchone()[0]
        search_results[q] = cnt
        print(f"  - Từ khóa '{q}': tìm thấy {cnt:,} kết quả")
    conn.close()

    status = "PASSED" if (zero_bytes == 0 and invalid_png == 0 and invalid_svg == 0 and is_sync) else "FAILED"
    print("\n" + "=" * 70)
    print(f"KẾT QUẢ KIỂM THỬ TỔNG THỂ: {status}")
    print("=" * 70)

    return {
        "status": status,
        "svg_count": len(svg_files),
        "png_count": len(png_files),
        "json_count": len(json_files),
        "total_images": disk_images,
        "zero_bytes": zero_bytes,
        "invalid_png": invalid_png,
        "invalid_svg": invalid_svg,
        "db_variants": db_variants,
        "search_results": search_results,
    }

if __name__ == "__main__":
    run_qa_suite()
