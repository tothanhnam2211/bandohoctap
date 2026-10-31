# -*- coding: utf-8 -*-
"""
MODULE 4 — PEDAGOGICAL EXPERIENCE ENGINE (mod4_pedagogy_engine.py)
Kết nối 16 Flagship Living Assets (phân bố trên 4 mạch Toán 6–9) với:
- Mục tiêu học tập, kích hoạt kiến thức nền, bẫy sai lầm thực tế của học sinh Việt Nam.
- Giàn giáo thích ứng 3 hồ sơ người học (Learner A: Mất gốc/Sợ Toán; Learner B: Chuẩn; Learner C: Mở rộng).
- Bộ 311 gói TextNote nhận thức từ Four Maps để sẵn sàng mở rộng sản xuất hàng loạt.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List

from .curated_living_assets_part1 import LIVING_ASSETS_PART_1
from .curated_living_assets_part2 import LIVING_ASSETS_PART_2


class PedagogicalExperienceEngine:
    """Module 4: Động cơ sư phạm đa tầng cho Living Mathematical Asset Factory."""

    def __init__(self, factory_dir: Path):
        self.factory_dir = factory_dir
        self.data_dir = factory_dir / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        local_packs = self.data_dir / "thcs_326_skills_textnote_packs.json"
        fallback_packs = Path(r"D:\YOURDREAM.VN\TEXTNOTE_FACTORY\data\thcs_326_skills_textnote_packs.json")
        self.textnote_packs_src = local_packs if local_packs.exists() else fallback_packs

    def get_all_16_living_assets(self) -> List[Dict[str, Any]]:
        assets = list(LIVING_ASSETS_PART_1) + list(LIVING_ASSETS_PART_2)
        return assets

    def build_pedagogical_catalog(self, semantic_registry: Dict[str, Any]) -> Dict[str, Any]:
        assets_16 = self.get_all_16_living_assets()
        strand_summary: Dict[str, int] = {}
        grade_summary: Dict[str, int] = {}
        for a in assets_16:
            sc = a["strand_code"]
            gr = f"Lớp {a['grade']}"
            strand_summary[sc] = strand_summary.get(sc, 0) + 1
            grade_summary[gr] = grade_summary.get(gr, 0) + 1

        textnote_count = 311
        if self.textnote_packs_src.exists():
            tn_data = json.loads(self.textnote_packs_src.read_text(encoding="utf-8"))
            textnote_count = tn_data.get("textnote_generated_count", 311)

        catalog = {
            "catalog_version": "2.2.0",
            "total_flagship_living_assets": len(assets_16),
            "strands_covered": strand_summary,
            "grades_covered": grade_summary,
            "linked_source_verified_skills": semantic_registry.get("total_source_verified_skills", 311),
            "linked_textnote_scaffolding_packs": textnote_count,
            "learner_profiles_supported": {
                "A": "Học sinh mất gốc / sợ Toán — Trực quan hóa vật thể ấm áp, bắt đầu từ thao tác tay, không áp lực công thức",
                "B": "Học sinh chuẩn chương trình — Kết nối mô hình trực quan với lập bảng, lập phương trình và giải toán",
                "C": "Học sinh khá giỏi — Khảo sát bất biến, phản ví dụ, nghiệm ngoại lai và tổng quát hóa cấu trúc",
            },
            "assets": assets_16,
        }

        out_path = self.data_dir / "living_asset_pedagogical_catalog.json"
        out_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
        return catalog
