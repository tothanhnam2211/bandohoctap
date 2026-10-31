#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO JULES & INDEPENDENT SDK CONSUMER TEST (PORTABLE RUNNER)
"""
from __future__ import annotations
import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

from engine.living_asset_sdk import LivingAssetRegistry


def run_qa_suite() -> dict:
    reg = LivingAssetRegistry(ROOT_DIR)
    all_assets = reg.list_assets()
    flagships = reg.list_assets(flagship_only=True)

    assert len(flagships) == 16, f"Expected 16 flagship assets, got {len(flagships)}"
    assert len(all_assets) == 20, f"Expected 20 total SDK assets, got {len(all_assets)}"

    # Test Baseline nang_suat.html existence
    baseline_html = ROOT_DIR / "baseline" / "nang_suat.html"
    assert baseline_html.exists(), "nang_suat.html missing from baseline handoff!"
    assert baseline_html.stat().st_size > 200000, "nang_suat.html corrupted or truncated!"

    strands = {a.strand_code for a in flagships}
    assert len(strands) == 4, f"Expected 4 strands, got {strands}"

    # Test Zero Hypothesis Mutation on Rate Asset
    state_wrong = reg.apply_action("YD-LA-ALG-G8-07", {"value": 10})
    state_right = reg.apply_action("YD-LA-ALG-G8-07", {"value": 12})
    assert state_wrong["is_solution"] is False
    assert state_wrong["locked_hypothesis_delta"] == 1.0
    assert state_right["is_solution"] is True
    assert state_right["locked_hypothesis_delta"] == 1.0

    # Test Causal Interaction Engine (Balance Scale & Zero Hypothesis Mutation)
    causal_wrong = reg.evaluate_causal_balance("YD-LA-ALG-G8-07", 10.0)
    causal_right = reg.evaluate_causal_balance("YD-LA-ALG-G8-07", 12.0)
    assert causal_wrong.is_equilibrium is False
    assert causal_wrong.torque_direction == "LEAN_LEFT"
    assert "BẤT BIẾN BẢO TOÀN" in causal_wrong.hypothesis_locked_proof
    assert causal_right.is_equilibrium is True
    assert causal_right.torque_direction == "BALANCED"
    assert causal_right.tilt_angle_deg == 0.0

    # Test Grid Tiling GCD counterexample vs solution
    tile_wrong = reg.apply_action("YD-LA-NUM-G6-01", {"value": 5})
    tile_right = reg.apply_action("YD-LA-NUM-G6-01", {"value": 6})
    assert tile_wrong["fits_perfectly"] is False
    assert tile_right["is_maximal_gcd"] is True

    # Test Generative Experience Synthesis
    syn_ok = reg.synthesize_experience({
        "spec_id": "QA_TRANSFER_JOINT_WORK",
        "title": "Hai máy cày cùng làm việc",
        "grade": 9,
        "mathematical_structure": "JOINT_FLOW_HARMONIC_RATE",
        "quantities": {"t1": 3, "t2": 6},
        "invariant_relation": "1/3 + 1/6 = 1/T",
        "target_equation": "1/3 + 1/6 = 1/2 => T = 2",
        "expected_solution": "2",
    })
    assert syn_ok["synthesis_status"] == "EXPERIENCE_SYNTHESIZED_FROM_PRIMITIVES"

    syn_unsupported = reg.synthesize_experience({
        "spec_id": "QA_UNSUPPORTED_DIFF_EQ",
        "title": "Phương trình vi phân cấp hai",
        "grade": 12,
        "mathematical_structure": "SECOND_ORDER_DIFFERENTIAL_EQUATION",
    })
    assert syn_unsupported["synthesis_status"] == "UNSUPPORTED_STRUCTURE_HONESTLY_DECLINED"

    # Test Zero Answer Leak in student_payloads
    stu_dir = ROOT_DIR / "student_payloads"
    stu_files = list(stu_dir.glob("*_student.json"))
    assert len(stu_files) == 16, f"Expected 16 student payloads, got {len(stu_files)}"
    for sf in stu_files:
        txt = sf.read_text(encoding="utf-8")
        assert '"final_answer"' not in txt, f"Answer leak in {sf.name}"
        assert '"teacher_solution"' not in txt, f"Solution leak in {sf.name}"
        assert '"target_solution"' not in txt, f"Target solution leak in {sf.name}"

    result = {
        "suite": "YOURDREAM_LIVING_ASSET_QA_AND_SDK_CONSUMER_SUITE",
        "total_sdk_assets": len(all_assets),
        "flagship_assets": len(flagships),
        "strands_verified": sorted(list(strands)),
        "zero_hypothesis_mutation_verified": True,
        "zero_student_answer_leak_verified": True,
        "generative_synthesis_verified": True,
        "unsupported_honest_decline_verified": True,
        "status": "ALL_TESTS_PASSED",
    }
    out_file = ROOT_DIR / "qa_verification_report.json"
    out_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


if __name__ == "__main__":
    run_qa_suite()
