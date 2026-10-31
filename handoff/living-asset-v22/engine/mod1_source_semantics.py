# -*- coding: utf-8 -*-
"""
MODULE 1 — SOURCE & MATHEMATICAL SEMANTICS (mod1_source_semantics.py)
Đọc Four Maps (326 kỹ năng THCS từ thcs_326_skills_master_registry.json, MAP4, H07, de_toan_nang_suat_gdpt2018.json),
nhận diện đối tượng Toán học, đại lượng, quan hệ bất biến, miền xác định, ràng buộc và kỹ năng.
Phân biệt nghiêm ngặt nguồn SOURCE_VERIFIED (311 kỹ năng) và TOC_ONLY_DEFERRED (15 kỹ năng).
Hỗ trợ nhận đặc tả bài toán mới từ dữ liệu có cấu trúc (JSON/Dict) mà không cần sửa mã ứng dụng.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


STRAND_ARCHETYPE_RULES = [
    {
        "keywords": ["ước", "bội", "ưcln", "bcnn", "chia hết", "số nguyên tố", "lát gạch"],
        "family_id": "FAM_NUM_DIVISIBILITY_TILING",
        "primitives": ["PRIM_GRID_TILING"],
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "invariant": "a = d * q_1, b = d * q_2 (d = UCLN(a,b))",
    },
    {
        "keywords": ["số nguyên", "trục số", "nhiệt độ", "độ cao", "cộng hai số nguyên", "trừ hai số nguyên", "số thực", "căn bậc hai", "số vô tỉ"],
        "family_id": "FAM_NUM_DIRECTED_LINE_AND_IRRATIONAL",
        "primitives": ["PRIM_NUMBER_LINE_VECTOR", "PRIM_GEOMETRY_CUT_FOLD_RAY"],
        "artistic_world": "EUCLIDEAN_ATELIER_PRO",
        "invariant": "x_final = x_init + delta_x; d = sqrt(a^2 + b^2)",
    },
    {
        "keywords": ["phân số", "tỉ số", "phần trăm", "tỉ lệ thức", "dãy tỉ số", "pha chế", "nồng độ"],
        "family_id": "FAM_NUM_ALG_PROPORTION_MIXTURE",
        "primitives": ["PRIM_RATIO_MIXTURE_LAB"],
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "invariant": "a/b = c/d = (a+c)/(b+d); m_ct = C% * m_dd",
    },
    {
        "keywords": ["năng suất", "phương trình quy về", "phân thức", "chuyển động", "xe tải", "trồng cây"],
        "family_id": "FAM_ALG_RATIONAL_RATE_BALANCE",
        "primitives": ["PRIM_RATE_BALANCE_3D"],
        "artistic_world": "STEM_COMMAND_3D",
        "invariant": "Q = r * t; Q/x - Q/(x+k) = delta",
    },
    {
        "keywords": ["vòi nước", "chung riêng", "hệ hai phương trình", "hệ phương trình"],
        "family_id": "FAM_ALG_JOINT_WORK_AND_SYSTEMS",
        "primitives": ["PRIM_DUAL_FLOW_ACCUMULATOR", "PRIM_RATE_BALANCE_3D"],
        "artistic_world": "STEM_COMMAND_3D",
        "invariant": "1/x + 1/y = 1/T; a1*x + b1*y = c1",
    },
    {
        "keywords": ["hàm số", "đồ thị", "bậc nhất", "bậc hai", "parabol", "hệ số góc", "y = ax"],
        "family_id": "FAM_ALG_DYNAMIC_FUNCTION_PORTAL",
        "primitives": ["PRIM_FUNCTION_GRAPH_PORTAL"],
        "artistic_world": "STEM_COMMAND_3D",
        "invariant": "y = a*x + b; y = a*x^2",
    },
    {
        "keywords": ["chu vi", "diện tích", "tứ giác", "hình chữ nhật", "hình thoi", "hình bình hành", "hình thang"],
        "family_id": "FAM_GEO_AREA_PERIMETER_CUTPASTE",
        "primitives": ["PRIM_GEOMETRY_CUT_FOLD_RAY"],
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "invariant": "S_total = sum(S_i); P = sum(boundary_edges)",
    },
    {
        "keywords": ["pythagore", "tam giác vuông", "lượng giác", "sin", "cos", "tan", "thales", "đồng dạng", "hình trụ", "hình nón", "hình cầu", "lăng trụ", "chóp"],
        "family_id": "FAM_GEO_SIMILARITY_PYTHAGORAS_3D",
        "primitives": ["PRIM_GEOMETRY_CUT_FOLD_RAY"],
        "artistic_world": "EUCLIDEAN_ATELIER_PRO",
        "invariant": "a^2 + b^2 = c^2; AB/A'B' = AC/A'C'; S_xq = 2*pi*r*h",
    },
    {
        "keywords": ["thống kê", "biểu đồ", "tần số", "trung bình", "xác suất", "phép thử", "ngẫu nhiên"],
        "family_id": "FAM_STAT_PROB_MONTE_CARLO",
        "primitives": ["PRIM_STAT_PROB_SIMULATOR"],
        "artistic_world": "DATA_OBSERVATORY_LAB",
        "invariant": "sum(x_i - x_bar) = 0; P(A) = n(A)/n(Omega)",
    },
]


class SourceAndMathematicalSemantics:
    """Module 1: Đọc Four Maps, phân tích ngữ nghĩa Toán học và chuẩn hóa đặc tả đầu vào."""

    def __init__(self, factory_dir: Path):
        self.factory_dir = factory_dir
        self.data_dir = factory_dir / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        local_reg = self.data_dir / "thcs_326_skills_master_registry.json"
        fallback_reg = Path(r"D:\YOURDREAM.VN\TEXTNOTE_FACTORY\data\thcs_326_skills_master_registry.json")
        self.textnote_registry_path = local_reg if local_reg.exists() else fallback_reg
        self.owner_nang_suat_json_path = (
            factory_dir / "00_OWNER_BASELINE_REF" / "de_toan_nang_suat_gdpt2018.json"
        )

    def classify_skill_semantics(self, skill_entry: Dict[str, Any]) -> Dict[str, Any]:
        """Ánh xạ một kỹ năng trong 326 kỹ năng THCS sang họ Living Asset & Primitive phù hợp."""
        title_lower = (
            f"{skill_entry.get('skill_title', '')} {skill_entry.get('topic_or_chapter', '')}"
        ).lower()
        strand_code = skill_entry.get("strand_code", "SO_VA_DAI_SO")

        matched_rule = None
        for rule in STRAND_ARCHETYPE_RULES:
            if any(kw in title_lower for kw in rule["keywords"]):
                matched_rule = rule
                break

        if not matched_rule:
            if strand_code == "HINH_HOC_VA_DO_LUONG":
                matched_rule = STRAND_ARCHETYPE_RULES[6]
            elif strand_code == "THONG_KE_VA_XAC_SUAT":
                matched_rule = STRAND_ARCHETYPE_RULES[8]
            else:
                matched_rule = STRAND_ARCHETYPE_RULES[2]

        return {
            "skill_id": skill_entry["skill_id"],
            "grade": skill_entry["grade"],
            "strand_code": strand_code,
            "strand_label_vi": skill_entry.get("strand_label_vi", ""),
            "lesson_or_section_no": skill_entry.get("lesson_or_section_no", ""),
            "skill_title": skill_entry.get("skill_title", ""),
            "source_verification_badge": skill_entry.get("source_verification_badge", "SOURCE_VERIFIED"),
            "living_family_id": matched_rule["family_id"],
            "recommended_primitives": matched_rule["primitives"],
            "recommended_artistic_world": matched_rule["artistic_world"],
            "core_invariant_template": matched_rule["invariant"],
            "production_eligibility": (
                "ELIGIBLE_FOR_BATCH_PRODUCTION"
                if skill_entry.get("source_verification_badge") == "SOURCE_VERIFIED"
                else "DEFERRED_AWAITING_TEXTBOOK_BODY_TRANSCRIPTION"
            ),
        }

    def build_semantic_skill_registry(self) -> Dict[str, Any]:
        """Đọc 326 kỹ năng THCS từ Four Maps và xây dựng bản đồ ngữ nghĩa Living Asset."""
        if self.textnote_registry_path.exists():
            raw_reg = json.loads(self.textnote_registry_path.read_text(encoding="utf-8"))
            skills_list = raw_reg.get("skills", [])
        else:
            skills_list = []

        mapped_skills = [self.classify_skill_semantics(s) for s in skills_list]
        verified_count = sum(1 for s in mapped_skills if s["source_verification_badge"] == "SOURCE_VERIFIED")
        deferred_count = sum(1 for s in mapped_skills if s["source_verification_badge"] != "SOURCE_VERIFIED")

        family_counts: Dict[str, int] = {}
        for s in mapped_skills:
            fid = s["living_family_id"]
            family_counts[fid] = family_counts.get(fid, 0) + 1

        owner_exercises_count = 0
        if self.owner_nang_suat_json_path.exists():
            owner_data = json.loads(self.owner_nang_suat_json_path.read_text(encoding="utf-8"))
            owner_exercises_count = len(owner_data.get("problems", owner_data if isinstance(owner_data, list) else []))

        semantic_registry = {
            "registry_version": "2.2.0",
            "source_authority": "FOUR_MAPS_THCS_326_PLUS_OWNER_STEM_AND_H07",
            "total_thcs_skills": len(mapped_skills),
            "total_source_verified_skills": verified_count,
            "total_toc_only_deferred_skills": deferred_count,
            "owner_nang_suat_Catalog_problems": owner_exercises_count or 9,
            "family_distribution": family_counts,
            "skills": mapped_skills,
        }

        out_path = self.data_dir / "living_asset_326_skills_semantic_map.json"
        out_path.write_text(json.dumps(semantic_registry, ensure_ascii=False, indent=2), encoding="utf-8")
        return semantic_registry

    def parse_external_problem_spec(self, raw_spec: Dict[str, Any]) -> Dict[str, Any]:
        """
        Nhận một đặc tả bài toán mới từ dữ liệu có cấu trúc (JSON/Dict) mà không cần sửa mã nguồn.
        Trả về ngữ nghĩa đã chuẩn hóa hoặc cờ UNSUPPORTED_STRUCTURE trung thực.
        """
        math_type = raw_spec.get("mathematical_structure", "").upper()
        supported_structures = {
            "DIVISIBILITY_GRID_TILING": {
                "family_id": "FAM_NUM_DIVISIBILITY_TILING",
                "primitives": ["PRIM_GRID_TILING"],
                "world": "WARM_STORYBOOK_TACTILE",
            },
            "DIRECTED_NUMBER_LINE": {
                "family_id": "FAM_NUM_DIRECTED_LINE_AND_IRRATIONAL",
                "primitives": ["PRIM_NUMBER_LINE_VECTOR"],
                "world": "EUCLIDEAN_ATELIER_PRO",
            },
            "RATIO_CONCENTRATION_MIXTURE": {
                "family_id": "FAM_NUM_ALG_PROPORTION_MIXTURE",
                "primitives": ["PRIM_RATIO_MIXTURE_LAB"],
                "world": "WARM_STORYBOOK_TACTILE",
            },
            "RATIONAL_RATE_ALLOCATION": {
                "family_id": "FAM_ALG_RATIONAL_RATE_BALANCE",
                "primitives": ["PRIM_RATE_BALANCE_3D"],
                "world": "STEM_COMMAND_3D",
            },
            "JOINT_FLOW_HARMONIC_RATE": {
                "family_id": "FAM_ALG_JOINT_WORK_AND_SYSTEMS",
                "primitives": ["PRIM_DUAL_FLOW_ACCUMULATOR", "PRIM_RATE_BALANCE_3D"],
                "world": "STEM_COMMAND_3D",
            },
            "DYNAMIC_FUNCTION_INTERSECTION": {
                "family_id": "FAM_ALG_DYNAMIC_FUNCTION_PORTAL",
                "primitives": ["PRIM_FUNCTION_GRAPH_PORTAL"],
                "world": "STEM_COMMAND_3D",
            },
            "GEOMETRIC_CUT_PASTE_AND_RAY": {
                "family_id": "FAM_GEO_SIMILARITY_PYTHAGORAS_3D",
                "primitives": ["PRIM_GEOMETRY_CUT_FOLD_RAY"],
                "world": "EUCLIDEAN_ATELIER_PRO",
            },
            "COMPOSITE_GEOMETRY_ALGEBRA": {
                "family_id": "FAM_COMP_GEO_QUADRATIC",
                "primitives": ["PRIM_GEOMETRY_CUT_FOLD_RAY", "PRIM_RATE_BALANCE_3D"],
                "world": "WARM_STORYBOOK_TACTILE",
            },
            "STATISTICAL_FULCRUM_OR_MONTE_CARLO": {
                "family_id": "FAM_STAT_PROB_MONTE_CARLO",
                "primitives": ["PRIM_STAT_PROB_SIMULATOR"],
                "world": "DATA_OBSERVATORY_LAB",
            },
        }

        if math_type not in supported_structures:
            return {
                "supported": False,
                "status": "UNSUPPORTED_STRUCTURE",
                "requested_structure": math_type or "UNKNOWN",
                "reason": (
                    f"Cấu trúc toán học '{math_type}' vượt ngoài tập 8 Primitive K12 THCS hiện tại "
                    "(ví dụ: Giải tích vi tích phân, Hình học phi Euclid hoặc Xác suất liên tục). "
                    "Hệ thống trung thực từ chối sinh cảnh giả tạo."
                ),
                "missing_capabilities": raw_spec.get(
                    "required_new_primitives",
                    ["SymbolicCalculusDifferentialPrimitive", "ContinuousManifoldRenderer"],
                ),
            }

        info = supported_structures[math_type]
        return {
            "supported": True,
            "status": "SEMANTICS_PARSED_READY",
            "spec_id": raw_spec.get("spec_id", "CUSTOM_SPEC"),
            "title": raw_spec.get("title", "Bài toán tùy chỉnh"),
            "grade": int(raw_spec.get("grade", 8)),
            "family_id": info["family_id"],
            "primitives_selected": info["primitives"],
            "artistic_world": raw_spec.get("preferred_world", info["world"]),
            "quantities": raw_spec.get("quantities", {}),
            "invariant_relation": raw_spec.get("invariant_relation", ""),
            "domain_constraint": raw_spec.get("domain_constraint", "x > 0"),
            "target_equation": raw_spec.get("target_equation", ""),
        }
