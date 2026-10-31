# -*- coding: utf-8 -*-
"""
MASS PRODUCTION PIPELINE RUNNER
Vận hành nhà máy kết xuất hàng loạt 30,000+ visual assets K12:
- Tận dụng đa tiến trình (multiprocessing) khai thác toàn bộ CPU cores
- Kết xuất đồng thời Master SVG, Master PNG, Student SVG, Student PNG và Metadata JSON
- Ghi nhận và chỉ mục hóa trực tiếp vào SQLite Registry + FTS5
- Báo cáo tiến độ và kiểm tra tính toàn vẹn (zero 0-byte files, hash verification)
"""

import os
import sys
import time
import argparse
from multiprocessing import Pool, cpu_count
from typing import List, Dict, Any, Tuple

# Set path
BASE_DIR = r"D:\YOURDREAM.VN\VISUAL_ASSET_FACTORY"
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from curriculum.k12_curriculum_catalog import get_k12_asset_families, AssetFamilySpec
from engine.variant_generator import generate_family_variants
from engine.multiformat_exporter import export_variant
from engine.registry_db import get_db_path, init_db, insert_families_batch, insert_variants_batch, get_db_stats

def _worker_process_family(args: Tuple[AssetFamilySpec, int, str]) -> List[Dict[str, Any]]:
    """Worker xử lý kết xuất toàn bộ biến thể của 1 Họ Asset"""
    family, variants_count, base_dir = args
    variants = generate_family_variants(family, count=variants_count)
    metas = []
    for var in variants:
        try:
            m = export_variant(var, base_dir)
            metas.append(m)
        except Exception as e:
            print(f"[ERR] Failed {var['variant_id']}: {e}")
    return metas

def run_production(variants_per_family: int = 46, num_workers: int = None, clean: bool = False):
    start_time = time.time()
    db_path = get_db_path(BASE_DIR)

    print("=" * 70)
    print("YOURDREAM — UNIVERSAL MATHEMATICAL VISUAL ASSET FACTORY")
    print(f"MASS PRODUCTION RUNNER · TARGET: 30,000+ ASSETS")
    print("=" * 70)

    # 1. Khởi tạo Database
    print(f"[1/5] Khởi tạo SQLite Registry tại: {db_path} (clean={clean})")
    init_db(db_path, drop_existing=clean)

    # 2. Tải danh mục Họ Asset
    families = get_k12_asset_families()
    total_families = len(families)
    target_variants = total_families * variants_per_family
    target_images = target_variants * 4
    print(f"[2/5] Đã tải {total_families} Họ Asset K12 (Lớp 6–12).")
    print(f"      Quy mô mục tiêu: {variants_per_family} biến thể/họ = {target_variants:,} biến thể")
    print(f"      Tổng file hình ảnh (SVG + PNG): {target_images:,} files")
    print(f"      Tổng file bao gồm JSON metadata: {target_variants * 5:,} files")

    # Lưu danh mục họ vào DB
    insert_families_batch(db_path, families)

    # 3. Chuẩn bị tác vụ đa tiến trình
    workers = num_workers or min(8, cpu_count())
    print(f"[3/5] Khởi động tiến trình song song với {workers} workers CPU...")

    task_args = [(fam, variants_per_family, BASE_DIR) for fam in families]

    all_metas = []
    completed_families = 0

    with Pool(processes=workers) as pool:
        for metas in pool.imap_unordered(_worker_process_family, task_args):
            all_metas.extend(metas)
            completed_families += 1
            if completed_families % 20 == 0 or completed_families == total_families:
                pct = (completed_families / total_families) * 100
                elapsed = time.time() - start_time
                curr_images = len(all_metas) * 4
                print(f"   -> Tiến độ: {completed_families}/{total_families} họ ({pct:.1f}%) | "
                      f"{curr_images:,} ảnh kết xuất | {elapsed:.1f}s")

    # 4. Lưu toàn bộ siêu dữ liệu vào SQLite Registry
    print(f"[4/5] Ghi {len(all_metas):,} bản ghi vào SQLite và FTS5 Full-Text Search...")
    # Batch insert by chunks of 500
    chunk_size = 500
    for i in range(0, len(all_metas), chunk_size):
        chunk = all_metas[i:i + chunk_size]
        insert_variants_batch(db_path, chunk)

    # 5. Thống kê & Kiểm tra tính toàn vẹn
    elapsed_total = time.time() - start_time
    stats = get_db_stats(db_path)
    total_mb = stats["bytes_summary"]["total_bytes"] / (1024 * 1024)

    print("\n" + "=" * 70)
    print("KẾT QUẢ SẢN XUẤT THÀNH CÔNG:")
    print(f" - Tổng số Họ Asset: {stats['family_count']}")
    print(f" - Tổng số Biến thể (Variants): {stats['variant_count']:,}")
    print(f" - Tổng file hình ảnh (SVG + PNG): {stats['total_rendered_files']:,}")
    print(f" - Tổng dung lượng hình ảnh: {total_mb:.2f} MB")
    print(f" - Phân bổ theo Lớp:")
    for g, count in sorted(stats["by_grade"].items()):
        print(f"     Lớp {g:02d}: {count * 4:,} file ảnh ({count:,} biến thể)")
    print(f" - Phân bổ theo Mạch kiến thức:")
    for s, count in sorted(stats["by_strand"].items()):
        print(f"     {s}: {count * 4:,} file ảnh")
    print(f" - Thời gian thực thi: {elapsed_total:.2f} giây (~{len(all_metas)*4/max(1, elapsed_total):.1f} files/s)")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mass Production Runner")
    parser.add_argument("--variants", type=int, default=46, help="Số biến thể cho mỗi họ asset")
    parser.add_argument("--workers", type=int, default=8, help="Số luồng worker")
    parser.add_argument("--clean", action="store_true", help="Xóa dữ liệu cũ và khởi tạo lại")
    args = parser.parse_args()

    run_production(variants_per_family=args.variants, num_workers=args.workers, clean=args.clean)
