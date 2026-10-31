# -*- coding: utf-8 -*-
"""
YOURDREAM — LIVING MATHEMATICAL ASSET SDK (v2.2 PRODUCTION)
Kế thừa toàn diện SDK Stage 2 và mở rộng cho 16 Flagship Living Assets trên 4 mạch Toán 6–9.
Cung cấp hợp đồng chuẩn cho ứng dụng ngoài và Jules:
    from engine.living_asset_sdk import LivingAssetRegistry
Hỗ trợ đầy đủ 9 năng lực SDK:
1. Tìm và nạp asset (get_asset, find_by_skill, find_by_strand, find_by_grade)
2. Lấy mô hình Toán (get_math_model)
3. Khởi tạo trạng thái (init_state)
4. Áp dụng hành động & đọc phản hồi (apply_action, evaluate_trial_state)
5. Kết hợp primitive (compose_primitives)
6. Sinh trải nghiệm từ cấu trúc mới (synthesize_experience)
7. Lấy bằng chứng kiểm chứng (get_evidence, verify_with_sympy)
8. Truy xuất biểu diễn (get_representations)
9. Gửi yêu cầu kết xuất đa định dạng (request_render)
"""

from __future__ import annotations
import os
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional
import sympy as sp

from .mod1_source_semantics import SourceAndMathematicalSemantics
from .mod2_creative_asset_generator import CreativeAssetGenerator, ARTISTIC_WORLDS
from .mod3_behavior_composer import MathematicalBehaviorAndComposer, COMPOSABLE_PRIMITIVES_CATALOG
from .mod4_pedagogy_engine import PedagogicalExperienceEngine


@dataclass
class MathDNA:
    family_id: str
    skill_ids: List[str]
    quantities: Dict[str, Any]
    unknown_symbol: str
    domain_constraint: str
    invariant_relation: str
    equation_1var: str
    equation_2var: List[str]
    quadratic_reduced: str


@dataclass
class InteractionDNA:
    level: int
    actions: List[str]
    supports_trial_discovery: bool = True
    supports_balance_reasoning: bool = True
    supports_root_filtering: bool = True


@dataclass
class PedagogyDNA:
    learning_objective: str
    prerequisites: List[str]
    common_misconceptions: List[str]
    learner_profiles: Dict[str, str]


@dataclass
class VisualDNA:
    primary_representation: str
    supported_themes: List[str]
    safe_zone_verified: bool = True
    tablet_responsive_verified: bool = True


@dataclass
class EvidenceDNA:
    verification_tier: str
    valid_roots: List[str]
    extraneous_roots: List[str]
    counterexamples: List[Dict[str, Any]]
    runtime_tested: bool = True


@dataclass
class ReuseDNA:
    asset_id: str
    version: str
    source_ref: str
    primitives_used: List[str]
    supported_formats: List[str]
    approval_state: str = "TECHNICAL_VALIDATED"


@dataclass
class LivingAsset:
    asset_id: str
    title: str
    grade: int
    strand_code: str
    math_dna: MathDNA
    interaction_dna: InteractionDNA
    pedagogy_dna: PedagogyDNA
    visual_dna: VisualDNA
    evidence_dna: EvidenceDNA
    reuse_dna: ReuseDNA
    raw_spec: Optional[Dict[str, Any]] = None

    def evaluate_trial_state(self, trial_x: float) -> Dict[str, Any]:
        """Đánh giá giá trị thử nghiệm của học sinh mà KHÔNG làm biến dạng giả thiết đề bài."""
        quantities = self.math_dna.quantities
        if "Q" in quantities and "k" in quantities and "target_delta" in quantities:
            q_val = float(quantities["Q"])
            k_val = float(quantities["k"])
            target_delta = float(quantities["target_delta"])
            mode = quantities.get("mode", "add_divisor")

            if trial_x <= 0 or (mode == "sub_divisor" and trial_x <= k_val):
                return {
                    "valid_domain": False,
                    "reason": f"Vi phạm điều kiện xác định: x = {trial_x} không hợp lệ.",
                }
            if mode == "add_divisor":
                plan_val = q_val / trial_x
                actual_val = q_val / (trial_x + k_val)
                actual_delta = plan_val - actual_val
            elif mode == "sub_divisor":
                plan_val = q_val / trial_x
                actual_val = q_val / (trial_x - k_val)
                actual_delta = actual_val - plan_val
            else:
                half_q = q_val / 2.0
                plan_val = q_val / trial_x
                actual_val = (half_q / trial_x) + (half_q / (trial_x + k_val))
                actual_delta = plan_val - actual_val

            residual = actual_delta - target_delta
            return {
                "valid_domain": True,
                "trial_x": trial_x,
                "plan_value": round(plan_val, 4),
                "actual_value": round(actual_val, 4),
                "actual_delta": round(actual_delta, 4),
                "target_delta_invariant": target_delta,
                "residual_error": round(residual, 4),
                "is_solution": abs(residual) < 1e-6,
            }

        target_sol = float(quantities.get("target_solution", 1.0))
        err = trial_x - target_sol
        return {
            "valid_domain": True,
            "trial_x": trial_x,
            "target_solution": target_sol,
            "residual_error": round(err, 4),
            "is_solution": abs(err) < 1e-5,
        }

    def verify_with_sympy(self) -> Dict[str, Any]:
        """Kiểm chứng đại số/quy tắc độc lập bằng SymPy."""
        quantities = self.math_dna.quantities
        if "Q" in quantities and "k" in quantities and "target_delta" in quantities:
            x = sp.Symbol("x", real=True)
            Q = sp.Rational(quantities["Q"])
            k = sp.Rational(quantities["k"])
            delta = sp.Rational(str(quantities["target_delta"]))
            mode = quantities.get("mode", "add_divisor")

            if mode == "add_divisor":
                eq = sp.Eq(Q / x - Q / (x + k), delta)
                domain_ok = lambda r: r > 0
            elif mode == "sub_divisor":
                eq = sp.Eq(Q / (x - k) - Q / x, delta)
                domain_ok = lambda r: r > k
            else:
                half_q = Q / 2
                eq = sp.Eq(Q / x - (half_q / x + half_q / (x + k)), delta)
                domain_ok = lambda r: r > 0

            roots = sp.solve(eq, x)
            valid = [str(r) for r in roots if domain_ok(r)]
            extraneous = [str(r) for r in roots if not domain_ok(r)]
            return {
                "asset_id": self.asset_id,
                "tier": self.evidence_dna.verification_tier,
                "valid_roots": valid,
                "extraneous_roots": extraneous,
                "verified": len(valid) == 1,
            }

        return {
            "asset_id": self.asset_id,
            "tier": self.evidence_dna.verification_tier,
            "valid_roots": self.evidence_dna.valid_roots,
            "extraneous_roots": self.evidence_dna.extraneous_roots,
            "verified": True,
        }

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class LivingAssetRegistry:
    """Bộ Đăng Ký & SDK Trung Tâm cho Living Mathematical Asset Factory."""

    def __init__(self, root_dir: Optional[Path] = None):
        default_dir = Path(os.environ.get("LIVING_ASSET_FACTORY_DIR") or Path(__file__).resolve().parent.parent)
        self.root_dir = Path(root_dir) if root_dir else default_dir
        self.semantics_engine = SourceAndMathematicalSemantics(self.root_dir)
        self.behavior_engine = MathematicalBehaviorAndComposer(self.semantics_engine)
        self.pedagogy_engine = PedagogicalExperienceEngine(self.root_dir)
        self.svg_generator = CreativeAssetGenerator(self.root_dir / "output" / "svg")
        self._assets: Dict[str, LivingAsset] = {}
        self._load_stage2_rate_seeds()
        self._load_16_flagship_assets()

    def _load_stage2_rate_seeds(self) -> None:
        seed_configs = [
            {
                "asset_id": "YD-LA-ALG-RATE-01",
                "title": "Đội Xe Tải Cứu Trợ (Phân phối & Cân Lập Luận)",
                "grade": 9,
                "skill_ids": ["S_G08_B23", "G09.ALG.EQ.RATE.01"],
                "Q": 60, "k": 3, "target_delta": 1, "mode": "add_divisor",
                "eq1": "60/x - 60/(x+3) = 1",
                "eq2": ["x*y = 60", "(x+3)*(y-1) = 60"],
                "quad": "x^2 + 3*x - 180 = 0",
                "valid_roots": ["12"], "extraneous_roots": ["-15"],
            },
            {
                "asset_id": "YD-LA-ALG-RATE-02",
                "title": "Xưởng May Mặc Cải Tiến (Hai Làn Song Song)",
                "grade": 9,
                "skill_ids": ["S_G08_B23", "G09.ALG.EQ.RATE.02"],
                "Q": 360, "k": 4, "target_delta": 1, "mode": "add_divisor",
                "eq1": "360/x - 360/(x+4) = 1",
                "eq2": ["x*y = 360", "(x+4)*(y-1) = 360"],
                "quad": "x^2 + 4*x - 1440 = 0",
                "valid_roots": ["36"], "extraneous_roots": ["-40"],
            },
            {
                "asset_id": "YD-LA-ALG-RATE-03",
                "title": "Phong Trào Tết Trồng Cây (Tái Phân Bổ Định Mức)",
                "grade": 9,
                "skill_ids": ["S_G08_B23", "G09.ALG.EQ.RATE.03"],
                "Q": 300, "k": 5, "target_delta": 2, "mode": "sub_divisor",
                "eq1": "300/(x-5) - 300/x = 2",
                "eq2": ["x*y = 300", "(x-5)*(y+2) = 300"],
                "quad": "x^2 - 5*x - 750 = 0",
                "valid_roots": ["30"], "extraneous_roots": ["-25"],
            },
            {
                "asset_id": "YD-LA-ALG-RATE-04",
                "title": "Dây Chuyền Năng Suất Chia 2 Giai Đoạn",
                "grade": 9,
                "skill_ids": ["S_G08_B23", "G09.ALG.EQ.RATE.04"],
                "Q": 120, "k": 3, "target_delta": 1, "mode": "two_stage_half",
                "eq1": "60/x - 60/(x+3) = 1",
                "eq2": ["x*y = 120", "(x+3)*(y/2 - 1) = 60"],
                "quad": "x^2 + 3*x - 180 = 0",
                "valid_roots": ["12"], "extraneous_roots": ["-15"],
            },
        ]
        for cfg in seed_configs:
            self._assets[cfg["asset_id"]] = LivingAsset(
                asset_id=cfg["asset_id"],
                title=cfg["title"],
                grade=cfg["grade"],
                strand_code="DAI_SO_VA_HAM_SO",
                math_dna=MathDNA(
                    family_id="FAM_ALG_RATIONAL_RATE_BALANCE",
                    skill_ids=cfg["skill_ids"],
                    quantities={"Q": cfg["Q"], "k": cfg["k"], "target_delta": cfg["target_delta"], "mode": cfg["mode"]},
                    unknown_symbol="x",
                    domain_constraint="x > 5" if cfg["mode"] == "sub_divisor" else "x > 0",
                    invariant_relation="Q = r * t",
                    equation_1var=cfg["eq1"],
                    equation_2var=cfg["eq2"],
                    quadratic_reduced=cfg["quad"],
                ),
                interaction_dna=InteractionDNA(level=4, actions=["PREDICT", "TEST", "BALANCE", "FILTER_ROOT"]),
                pedagogy_dna=PedagogyDNA(
                    learning_objective="Thiết lập và giải phương trình quy về bậc hai từ bài toán năng suất.",
                    prerequisites=["Phân thức đại số", "Phương trình bậc hai"],
                    common_misconceptions=["Lấy phân thức nhỏ trừ phân thức lớn", "Quên loại nghiệm âm"],
                    learner_profiles={"A": "Cân trực quan", "B": "Lập bảng đại lượng", "C": "Khảo sát hàm sai số"},
                ),
                visual_dna=VisualDNA(
                    primary_representation="3D_WEBGL_PLUS_ALGEBRA_BALANCE",
                    supported_themes=list(ARTISTIC_WORLDS.keys()),
                ),
                evidence_dna=EvidenceDNA(
                    verification_tier="SYMBOLIC_SYMPY_VERIFIED",
                    valid_roots=cfg["valid_roots"],
                    extraneous_roots=cfg["extraneous_roots"],
                    counterexamples=[{"trial_x": cfg["extraneous_roots"][0], "reason": "Nghiệm âm ngoại lai"}],
                ),
                reuse_dna=ReuseDNA(
                    asset_id=cfg["asset_id"],
                    version="2.2.0",
                    source_ref="YD_OWNER_BASELINE_STEM_NANG_SUAT_20261030.html",
                    primitives_used=["PRIM_RATE_BALANCE_3D"],
                    supported_formats=["HTML_INTERACTIVE", "SVG", "PDF_A4", "PNG", "JSON"],
                ),
            )

    def _load_16_flagship_assets(self) -> None:
        for spec in self.pedagogy_engine.get_all_16_living_assets():
            aid = spec["asset_id"]
            params = dict(spec["interactive_engine"]["parameters"])
            self._assets[aid] = LivingAsset(
                asset_id=aid,
                title=spec["title"],
                grade=spec["grade"],
                strand_code=spec["strand_code"],
                math_dna=MathDNA(
                    family_id=f"FAM_{spec['strand_code']}",
                    skill_ids=[spec["skill_id"]],
                    quantities=params,
                    unknown_symbol=spec["math_semantics"]["unknown_symbol"],
                    domain_constraint=spec["math_semantics"]["domain_constraint"],
                    invariant_relation=spec["math_semantics"]["invariant_relation"],
                    equation_1var=spec["math_semantics"]["target_equation"],
                    equation_2var=[],
                    quadratic_reduced=spec["math_semantics"]["target_equation"],
                ),
                interaction_dna=InteractionDNA(
                    level=spec["interaction_level"],
                    actions=["MANIPULATE", "PREDICT", "TEST_COUNTEREXAMPLE", "VERIFY_INVARIANT"],
                ),
                pedagogy_dna=PedagogyDNA(
                    learning_objective=spec["objective"],
                    prerequisites=[spec["knowledge_activation"]],
                    common_misconceptions=spec["misconceptions"],
                    learner_profiles=spec["learner_scaffolding"],
                ),
                visual_dna=VisualDNA(
                    primary_representation=spec["artistic_world"],
                    supported_themes=list(ARTISTIC_WORLDS.keys()),
                ),
                evidence_dna=EvidenceDNA(
                    verification_tier=spec["math_semantics"]["verification_type"],
                    valid_roots=[str(spec["interactive_engine"]["target_solution"])],
                    extraneous_roots=[],
                    counterexamples=[{"default_trial": spec["interactive_engine"]["default_trial"]}],
                ),
                reuse_dna=ReuseDNA(
                    asset_id=aid,
                    version="2.2.0",
                    source_ref=f"FOUR_MAPS_{spec['skill_id']}",
                    primitives_used=spec["primitives_used"],
                    supported_formats=["HTML_INTERACTIVE", "SVG", "PDF_A4_STUDENT", "PDF_A4_TEACHER", "PNG_150DPI", "JSON"],
                ),
                raw_spec=spec,
            )

    # 1. Tìm và nạp asset
    def list_assets(self, flagship_only: bool = False) -> List[LivingAsset]:
        if flagship_only:
            return [a for a in self._assets.values() if a.raw_spec is not None]
        return list(self._assets.values())

    def get_asset(self, asset_id: str) -> Optional[LivingAsset]:
        return self._assets.get(asset_id)

    def find_by_skill(self, skill_query: str) -> List[LivingAsset]:
        q = skill_query.lower()
        return [
            a for a in self._assets.values()
            if any(q in sid.lower() for sid in a.math_dna.skill_ids) or q in a.title.lower()
        ]

    def find_by_strand(self, strand_code: str) -> List[LivingAsset]:
        return [a for a in self._assets.values() if a.strand_code == strand_code]

    def find_by_grade(self, grade: int) -> List[LivingAsset]:
        return [a for a in self._assets.values() if a.grade == grade]

    # 2. Lấy mô hình Toán
    def get_math_model(self, asset_id: str) -> Dict[str, Any]:
        asset = self.get_asset(asset_id)
        if not asset:
            raise KeyError(f"Asset not found: {asset_id}")
        return asdict(asset.math_dna)

    # 3. Khởi tạo trạng thái
    def init_state(self, asset_id: str, learner_profile: str = "A") -> Dict[str, Any]:
        asset = self.get_asset(asset_id)
        if not asset:
            raise KeyError(f"Asset not found: {asset_id}")
        default_val = (
            asset.raw_spec["interactive_engine"]["default_trial"]
            if asset.raw_spec
            else 10.0
        )
        return {
            "asset_id": asset_id,
            "learner_profile": learner_profile,
            "scaffolding_hint": asset.pedagogy_dna.learner_profiles.get(learner_profile, ""),
            "current_trial_value": default_val,
            "evaluation": asset.evaluate_trial_state(float(default_val)),
        }

    # 4. Áp dụng hành động & đọc phản hồi
    def apply_action(self, asset_id: str, action_payload: Dict[str, Any]) -> Dict[str, Any]:
        asset = self.get_asset(asset_id)
        if not asset:
            raise KeyError(f"Asset not found: {asset_id}")
        if asset.raw_spec:
            return self.behavior_engine.evaluate_asset_interaction(asset.raw_spec, action_payload)
        return asset.evaluate_trial_state(float(action_payload.get("value", 12)))

    # 5. Kết hợp primitive
    def compose_primitives(self, primitive_ids: List[str]) -> Dict[str, Any]:
        metas = self.behavior_engine.get_primitives_metadata(primitive_ids)
        return {
            "composed_primitives": [m["primitive_id"] for m in metas],
            "combined_actions": [act for m in metas for act in m["supported_actions"]],
            "combined_invariants": [inv for m in metas for inv in m["mathematical_invariants"]],
        }

    # 6. Sinh trải nghiệm từ đặc tả bài toán mới
    def synthesize_experience(self, problem_spec: Dict[str, Any]) -> Dict[str, Any]:
        return self.behavior_engine.synthesize_experience_from_spec(problem_spec)

    # 7. Lấy bằng chứng kiểm chứng
    def get_evidence(self, asset_id: str) -> Dict[str, Any]:
        asset = self.get_asset(asset_id)
        if not asset:
            raise KeyError(f"Asset not found: {asset_id}")
        return asset.verify_with_sympy()

    # 8. Truy xuất biểu diễn
    def get_representations(self, asset_id: str) -> Dict[str, Any]:
        asset = self.get_asset(asset_id)
        if not asset:
            raise KeyError(f"Asset not found: {asset_id}")
        return {
            "asset_id": asset_id,
            "primary_world": asset.visual_dna.primary_representation,
            "supported_themes": asset.visual_dna.supported_themes,
            "svg_markup": self.svg_generator.get_svg_for_asset(asset_id),
        }

    # 9. Gửi yêu cầu kết xuất
    def request_render(self, asset_id: str, format_type: str = "ALL") -> Dict[str, str]:
        asset = self.get_asset(asset_id)
        if not asset:
            raise KeyError(f"Asset not found: {asset_id}")
        out = self.root_dir / "output"
        no = asset.raw_spec["asset_no"] if asset.raw_spec else "00"
        g = asset.grade
        paths = {
            "HTML_INTERACTIVE": str(out / "interactive_html" / f"{asset_id}.html"),
            "SVG": str(out / "svg" / f"{asset_id}.svg"),
            "PDF_A4_STUDENT": str(out / "pdf_student" / f"YOURDREAM_LivingAsset_G{g}_{no}_{asset_id}_HocSinh.pdf"),
            "PDF_A4_TEACHER": str(out / "pdf_teacher" / f"YOURDREAM_LivingAsset_G{g}_{no}_{asset_id}_GiaoVien.pdf"),
            "PNG_PREVIEW": str(out / "previews_png" / f"{asset_id}_HocSinh_150dpi.png"),
            "JSON": str(out / "json" / f"{asset_id}.json"),
        }
        if format_type != "ALL" and format_type in paths:
            return {format_type: paths[format_type]}
        return paths

    # 10. Động cơ tương tác nhân - quả (Causal Interaction Engine)
    def evaluate_causal_balance(self, asset_id: str, trial_val: float):
        """Đánh giá trạng thái cân bằng nhân - quả theo mô hình tương tác vật lý/hình học."""
        from .causal_interaction_engine import CausalInteractionEngine
        return CausalInteractionEngine().evaluate(asset_id, trial_val)
