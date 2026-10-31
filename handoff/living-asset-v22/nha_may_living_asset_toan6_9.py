#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YOURDREAM — NHÀ MÁY TÀI SẢN TOÁN HỌC SỐNG (LIVING MATHEMATICAL ASSET FACTORY v2.2)
Tệp điều phối dây chuyền 7 Module (Chạy 1 lệnh duy nhất):
  python nha_may_living_asset_toan6_9.py --mode all
  python nha_may_living_asset_toan6_9.py --asset YD-LA-NUM-G6-01
  python nha_may_living_asset_toan6_9.py --synthesize path/to/problem_spec.json
"""

from __future__ import annotations
import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

FACTORY_DIR = Path(os.environ.get("LIVING_ASSET_FACTORY_DIR") or Path(__file__).resolve().parent)
OUTPUT_DIR = FACTORY_DIR / "output"
HANDOFF_DIR = Path(os.environ.get("JULES_HANDOFF_DIR") or (FACTORY_DIR.parent / "JULES_LIVING_ASSET_HANDOFF" if FACTORY_DIR.name == "LIVING_ASSET_FACTORY" else FACTORY_DIR / "handoff"))
CHECKPOINTS_DIR = Path(os.environ.get("CHECKPOINTS_DIR") or (FACTORY_DIR.parent / "CHECKPOINTS" if (FACTORY_DIR.parent / "CHECKPOINTS").exists() else FACTORY_DIR / "checkpoints"))

from engine.mod1_source_semantics import SourceAndMathematicalSemantics
from engine.mod3_behavior_composer import MathematicalBehaviorAndComposer
from engine.mod4_pedagogy_engine import PedagogicalExperienceEngine
from engine.mod5_truth_verifier import MathematicalTruthAndEvidenceEngine
from engine.mod6_multiformat_renderer import MultiformatRenderer
from engine.mod7_studio_and_jules_handoff import StudioAndJulesHandoffManager
from engine.living_asset_sdk import LivingAssetRegistry


def run_factory(mode: str = "all", target_asset: str | None = None, spec_file: str | None = None) -> dict:
    t0 = time.time()
    print("=" * 84)
    print("YOURDREAM — LIVING MATHEMATICAL ASSET FACTORY (7-MODULE PRODUCTION PIPELINE v2.2)")
    print("=" * 84)

    # MODULE 1: Source & Mathematical Semantics
    print("\n[MODULE 1/7] Đọc Four Maps & Phân tích Ngữ nghĩa Toán học 326 kỹ năng THCS...")
    m1 = SourceAndMathematicalSemantics(FACTORY_DIR)
    semantic_registry = m1.build_semantic_skill_registry()
    print(
        f"  -> Đã ánh xạ {semantic_registry['total_thcs_skills']} kỹ năng THCS sang Living Asset Families: "
        f"{semantic_registry['total_source_verified_skills']} SOURCE_VERIFIED | "
        f"{semantic_registry['total_toc_only_deferred_skills']} TOC_ONLY_DEFERRED."
    )

    # MODULE 3: Mathematical Behavior, Composable Primitives & Generative Experience Synthesis
    print("\n[MODULE 3/7] Kích hoạt 8 Composable Primitives & Chạy 4 Generative Transfer Benchmarks...")
    m3 = MathematicalBehaviorAndComposer(m1)
    if spec_file:
        custom_spec = json.loads(Path(spec_file).read_text(encoding="utf-8"))
        syn_res = m3.synthesize_experience_from_spec(custom_spec)
        print("  -> Kết quả sinh trải nghiệm từ đặc tả mới:")
        print(json.dumps(syn_res, ensure_ascii=False, indent=2))
        return syn_res

    transfer_report = m3.run_all_transfer_benchmarks()
    print(
        f"  -> Generative Transfer Benchmarks: {transfer_report['synthesized_count']}/3 bài toán mới "
        f"tổ hợp thành công từ Primitives | {transfer_report['unsupported_honestly_declined_count']}/1 bài "
        f"vượt phạm vi K12 từ chối trung thực (UNSUPPORTED_STRUCTURE)."
    )

    # MODULE 4: Pedagogical Experience Engine (16 Flagship Living Assets across 4 Strands & Grades 6-9)
    print("\n[MODULE 4/7] Xây dựng Danh mục 16 Flagship Living Assets (4 Mạch · Lớp 6–9 · Learner A/B/C)...")
    m4 = PedagogicalExperienceEngine(FACTORY_DIR)
    pedagogy_catalog = m4.build_pedagogical_catalog(semantic_registry)
    assets_16 = pedagogy_catalog["assets"]
    if target_asset:
        assets_16 = [a for a in assets_16 if a["asset_id"] == target_asset]
    print(
        f"  -> Sẵn sàng sản xuất {len(assets_16)} Living Assets trên 4 mạch: "
        f"{json.dumps(pedagogy_catalog['strands_covered'], ensure_ascii=False)}"
    )

    # MODULE 5: Mathematical Truth & Evidence Verification
    print("\n[MODULE 5/7] Kiểm chứng Chân lý Toán học Đa mạch (SymPy + Số học chính xác + Hình học + Thống kê)...")
    m5 = MathematicalTruthAndEvidenceEngine(FACTORY_DIR)
    math_ledger = m5.verify_all_assets_and_benchmarks(pedagogy_catalog["assets"], transfer_report)
    print(
        f"  -> Đã kiểm chứng {math_ledger['total_assets_verified']}/16 Living Assets & 4 Transfer Benchmarks: "
        f"{'100% MATH_VERIFIED' if math_ledger['all_passed'] else 'CẦN KIỂM TRA'}."
    )

    # MODULE 2 & MODULE 6: Creative Asset Generation & Multiformat Rendering
    print("\n[MODULE 2 & 6/7] Kết xuất Đa định dạng (16 HTML Tương tác + 16 SVG Phân lớp + 32 PDF A4 + 32 PNG + 16 JSON)...")
    m6 = MultiformatRenderer(OUTPUT_DIR)
    render_report = m6.render_all_16_assets(assets_16)
    print(
        f"  -> Đã xuất: {render_report['total_interactive_htmls']} HTML Tương tác | "
        f"{render_report['total_svgs']} SVG | {render_report['total_student_pdfs']} PDF Học sinh | "
        f"{render_report['total_teacher_pdfs']} PDF Giáo viên | {render_report['total_png_previews']} PNG 150 DPI."
    )
    print(
        f"  -> Cổng kiểm toán 1 Trang A4 & 0% Lộ Đáp Án Học sinh: "
        f"{'PASS 100%' if render_report['all_passed_single_page_and_zero_leak_gate'] else 'CẦN KIỂM TRA'}."
    )

    # MODULE 7: Living Asset Studio, SDK Verification & Jules Handoff Packaging
    print("\n[MODULE 7/7] Xây dựng Living Asset Studio, Kiểm tra SDK & Đóng gói JULES_LIVING_ASSET_HANDOFF...")
    m7 = StudioAndJulesHandoffManager(FACTORY_DIR, HANDOFF_DIR)
    studio_path = m7.build_living_asset_studio_html(
        pedagogy_catalog["assets"], render_report, semantic_registry, transfer_report, math_ledger
    )
    checkpoint = m7.package_jules_handoff(
        pedagogy_catalog["assets"], render_report, semantic_registry, transfer_report, math_ledger
    )

    # Verify SDK Registry contract
    reg = LivingAssetRegistry(FACTORY_DIR)
    sdk_total = len(reg.list_assets())
    sdk_flagship = len(reg.list_assets(flagship_only=True))
    print(f"  -> LivingAssetRegistry SDK sẵn sàng: {sdk_total} tổng tài sản ({sdk_flagship} Flagship đa mạch + 4 Seed Stage 2).")
    print(f"  -> Giao diện LIVING ASSET STUDIO: {studio_path}")
    print(f"  -> Gói bàn giao JULES_LIVING_ASSET_HANDOFF: {HANDOFF_DIR}")

    # Update MANIFEST_LIVING_ASSET.json and CHECKPOINTS
    manifest_summary = {
        "factory_name": "YOURDREAM_LIVING_MATHEMATICAL_ASSET_FACTORY",
        "version": "2.2.0-production",
        "stage": checkpoint["stage"],
        "pipeline_states": checkpoint["pipeline_progression"],
        "studio_html": str(studio_path),
        "stage2_3d_flagship_lab": str(
            FACTORY_DIR / "02_STAGE2_CREATIVE_DISCOVERY" / "stage2_creative_frontier_lab.html"
        ),
        "jules_handoff_dir": str(HANDOFF_DIR),
        "sdk_entry_point": "from engine.living_asset_sdk import LivingAssetRegistry",
        "counts": {
            "flagship_living_assets": sdk_flagship,
            "total_sdk_assets": sdk_total,
            "composable_primitives": 8,
            "artistic_worlds": 5,
            "interactive_htmls": render_report["total_interactive_htmls"],
            "layered_svgs": render_report["total_svgs"],
            "student_a4_pdfs": render_report["total_student_pdfs"],
            "teacher_a4_pdfs": render_report["total_teacher_pdfs"],
            "png_previews_150dpi": render_report["total_png_previews"],
            "thcs_skills_mapped": semantic_registry["total_thcs_skills"],
            "source_verified_skills": semantic_registry["total_source_verified_skills"],
        },
        "statuses": checkpoint["statuses"],
    }
    (FACTORY_DIR / "MANIFEST_LIVING_ASSET.json").write_text(
        json.dumps(manifest_summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    CHECKPOINTS_DIR.mkdir(parents=True, exist_ok=True)
    (CHECKPOINTS_DIR / "CHECKPOINT_LIVING_ASSET_FACTORY_20261031.json").write_text(
        json.dumps(checkpoint, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    elapsed = round(time.time() - t0, 2)
    print(f"\n[HOÀN TẤT DÂY CHUYỀN NHÀ MÁY TRONG {elapsed}s] Trạng thái: {checkpoint['stage']}")
    return checkpoint


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOURDREAM Living Mathematical Asset Factory v2.2")
    parser.add_argument("--mode", default="all", choices=["all", "verify", "render"])
    parser.add_argument("--asset", default=None, help="Chỉ kết xuất 1 mã Living Asset cụ thể (VD: YD-LA-NUM-G6-01)")
    parser.add_argument("--synthesize", default=None, help="Đường dẫn tệp JSON đặc tả bài toán mới để sinh trải nghiệm")
    args = parser.parse_args()
    run_factory(mode=args.mode, target_asset=args.asset, spec_file=args.synthesize)
