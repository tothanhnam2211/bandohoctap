# -*- coding: utf-8 -*-
"""
MODULE 3 — MATHEMATICAL BEHAVIOR & COMPOSITION (mod3_behavior_composer.py)
1. Quản lý Thư viện 8 Primitive Tương tác Toán học Độc lập (Composable Interactive Primitives).
2. Gắn hành vi Toán học thực (Kéo/Thử nghiệm, Cắt ghép, Đo đạc, Phát hiện sai số, Sinh phản ví dụ,
   Quan sát bất biến, Lọc nghiệm ngoại lai).
3. Bộ Sinh Trải Nghiệm Mới (Generative Experience Synthesizer): Từ một đặc tả bài toán mới (JSON/Dict),
   tự động chọn và kết hợp các Primitive phù hợp để tạo trải nghiệm tương tác, hoặc trung thực
   báo UNSUPPORTED_STRUCTURE khi gặp cấu trúc vượt phạm vi hỗ trợ.
"""

from __future__ import annotations
import math
from typing import Any, Dict, List


COMPOSABLE_PRIMITIVES_CATALOG: Dict[str, Dict[str, Any]] = {
    "PRIM_GRID_TILING": {
        "primitive_id": "PRIM_GRID_TILING",
        "name_vi": "Lưới Lát Gạch & Phân Nhóm Ước Bội (Grid Tiling & Divisor Partition)",
        "supported_actions": ["SLIDE_TILE_SIZE", "CHECK_REMAINDER_CRACK", "HIGHLIGHT_GCD_CELLS", "OBSERVE_INVARIANT"],
        "mathematical_invariants": ["a = d * q1 + r1", "b = d * q2 + r2", "r1 == 0 and r2 == 0 <=> d | gcd(a,b)"],
        "counterexample_generator": "Khi chọn cạnh gạch d không phải ước chung, xuất hiện dải gạch lẻ (vết cắt đỏ) rộng a mod d hoặc b mod d.",
    },
    "PRIM_NUMBER_LINE_VECTOR": {
        "primitive_id": "PRIM_NUMBER_LINE_VECTOR",
        "name_vi": "Trục Số Động & Mũi Tên Vector (Directed Number Line & Compass Arc)",
        "supported_actions": ["ADD_VECTOR_STEP", "RELEASE_BALLAST_NEGATIVE", "UNROLL_HYPOTENUSE_ARC", "ZOOM_DECIMAL"],
        "mathematical_invariants": ["x_end = x_start + delta", "a - (-b) = a + b", "d = sqrt(1^2 + 1^2) = sqrt(2)"],
        "counterexample_generator": "Khi cộng nhầm dấu trừ thành lặn sâu hơn khi thả tạ, tàu ngầm chạm vùng cảnh báo áp suất.",
    },
    "PRIM_RATIO_MIXTURE_LAB": {
        "primitive_id": "PRIM_RATIO_MIXTURE_LAB",
        "name_vi": "Phòng Thí Nghiệm Tỉ Lệ & Nồng Độ Bất Biến (Ratio & Mixture Invariant Lab)",
        "supported_actions": ["POUR_SOLVENT", "ADD_SOLUTE", "SCALE_PROPORTION_BARS", "VERIFY_INVARIANT_MASS"],
        "mathematical_invariants": ["m_solute = C% * m_total", "x/a = y/b = (x+y)/(a+b)"],
        "counterexample_generator": "Phản ví dụ trực quan cho sai lầm cộng ngang tử với tử, mẫu với mẫu khi tính nồng độ.",
    },
    "PRIM_RATE_BALANCE_3D": {
        "primitive_id": "PRIM_RATE_BALANCE_3D",
        "name_vi": "Mô Phỏng Năng Suất 3D & Cân Lập Luận Đại Số (3D Rate & Relational Balance)",
        "supported_actions": ["TRIAL_UNKNOWN_X", "TILT_BALANCE_SCALE", "REDUCE_TO_QUADRATIC", "FILTER_EXTRANEOUS_ROOT"],
        "mathematical_invariants": ["Q = r * t", "Q/x - Q/(x+k) = delta_fixed"],
        "counterexample_generator": "Giữ nguyên giả thiết delta_fixed; thử x sai làm nghiêng đĩa cân; thử nghiệm âm x2 < 0 bị chặn bởi miền xác định thực tế.",
    },
    "PRIM_DUAL_FLOW_ACCUMULATOR": {
        "primitive_id": "PRIM_DUAL_FLOW_ACCUMULATOR",
        "name_vi": "Bể Tích Lũy Hai Dòng Chảy Cộng Hưởng (Dual Flow Harmonic Rate Accumulator)",
        "supported_actions": ["SET_PIPE_TIMES", "RUN_1HOUR_SLICE", "COMPARE_SUM_TIMES_VS_RATES", "SOLVE_HARMONIC"],
        "mathematical_invariants": ["r_total = 1/x + 1/y = 1/T", "T = (x*y)/(x+y) < min(x,y)"],
        "counterexample_generator": "Bác bỏ sai lầm T = x + y: hai vòi cùng chảy phải đầy nhanh hơn từng vòi chảy riêng (T < x và T < y).",
    },
    "PRIM_FUNCTION_GRAPH_PORTAL": {
        "primitive_id": "PRIM_FUNCTION_GRAPH_PORTAL",
        "name_vi": "Đồ Thị Hàm Số Động & Cổng Kiểm Thử Thực Tế (Dynamic Function & Clearance Portal)",
        "supported_actions": ["DRAG_DISTANCE_X", "FIND_INTERSECTION_POINT", "ADJUST_PARABOLA_A", "TEST_BOAT_CLEARANCE"],
        "mathematical_invariants": ["y1(x0) = y2(x0)", "y = a * x^2", "clearance(x) = H_arch - |a|*x^2"],
        "counterexample_generator": "Khi thuyền có nửa chiều rộng w/2 tạo độ cao chạm vòm Parabol, cảnh báo va chạm đỏ tại tọa độ (w/2, h_boat).",
    },
    "PRIM_GEOMETRY_CUT_FOLD_RAY": {
        "primitive_id": "PRIM_GEOMETRY_CUT_FOLD_RAY",
        "name_vi": "Xưởng Cắt Ghép Hình Học, Tia Nắng Đồng Dạng & Mở Phẳng 3D (Cut-Paste, Ray & 3D Net)",
        "supported_actions": ["SLIDE_TRIANGLES", "TRANSLATE_CORNER_EDGES", "ADJUST_SUN_ANGLE", "UNROLL_3D_SURFACE"],
        "mathematical_invariants": ["P_L_shape = 2*(W+H)", "a^2 + b^2 = c^2", "h_tower / h_stick = s_tower / s_stick", "S_xq = 2*pi*R*h"],
        "counterexample_generator": "Khi cắt góc hình chữ nhật, diện tích giảm nhưng 2 cạnh mới bù đúng 2 cạnh mất đi nên chu vi không giảm.",
    },
    "PRIM_STAT_PROB_SIMULATOR": {
        "primitive_id": "PRIM_STAT_PROB_SIMULATOR",
        "name_vi": "Đòn Bẩy Trọng Tâm Thống Kê & Mô Phỏng Hội Tụ Monte Carlo (Fulcrum & Monte Carlo Lab)",
        "supported_actions": ["DRAG_OUTLIER_VALUE", "OBSERVE_MEAN_SHIFT", "RUN_N_TRIALS", "COMPARE_EMPIRICAL_THEORETICAL"],
        "mathematical_invariants": ["sum(x_i - mean) = 0", "median = middle_rank_value", "lim_{N->inf} k/N = P(A)"],
        "counterexample_generator": "Khi kéo 1 điểm dữ liệu lên gấp 5 lần, Trung bình cộng bị kéo lệch mạnh nhưng Trung vị đứng yên.",
    },
}


# 4 Bài toán Kiểm thử Chuyển giao Sinh Trải Nghiệm Mới (Held-out Generative Transfer Benchmarks)
GENERATIVE_TRANSFER_BENCHMARKS: List[Dict[str, Any]] = [
    {
        "benchmark_id": "TRANSFER_TEST_A_SAME_FAMILY_NEW_STRUCTURE",
        "test_category": "Test A — Cùng mạch Đại số nhưng khác cấu trúc phương trình (Hai vòi chảy + Rò rỉ đáy)",
        "mathematical_structure": "JOINT_FLOW_HARMONIC_RATE",
        "spec_id": "YD-TRANSFER-A-HYDRO-LEAK",
        "title": "Hồ Chứa Nước Có Van Xả: Hai Vòi Bơm Vào & Một Van Rò Rỉ",
        "grade": 9,
        "quantities": {"t_in_1": 4, "t_in_2": 6, "t_leak": 12, "target_fill": 1},
        "invariant_relation": "1/t1 + 1/t2 - 1/t_leak = 1/T",
        "domain_constraint": "t1, t2, t_leak > 0; 1/t1 + 1/t2 > 1/t_leak",
        "target_equation": "1/4 + 1/6 - 1/12 = 1/T  <=>  4/12 = 1/T  <=>  T = 3 (giờ)",
        "expected_solution": "3",
    },
    {
        "benchmark_id": "TRANSFER_TEST_B_CROSS_FAMILY_COMPOSITION",
        "test_category": "Test B — Kết hợp Đa Họ (Hình học Lối đi Vườn H07 + Đại số Phương trình Bậc hai + Cân Chi phí)",
        "mathematical_structure": "COMPOSITE_GEOMETRY_ALGEBRA",
        "spec_id": "YD-TRANSFER-B-POOL-WALKWAY",
        "title": "Thiết Kế Hồ Bơi Sinh Thái Có Đường Dạo Bộ Lát Đá Bốn Phía",
        "grade": 9,
        "quantities": {"outer_L": 30, "outer_W": 20, "inner_area": 336},
        "invariant_relation": "(L - 2x)*(W - 2x) = S_inner",
        "domain_constraint": "0 < x < 10",
        "target_equation": "(30 - 2x)(20 - 2x) = 336 <=> x^2 - 25x + 66 = 0",
        "expected_solution": "3 (Loại x2 = 22 vì 2x < 20 => x < 10)",
    },
    {
        "benchmark_id": "TRANSFER_TEST_C_NEW_REPRESENTATION_MODALITY",
        "test_category": "Test C — Chuyển đổi Biểu diễn (Từ Đại số Tỉ lệ sang Đồ thị Giao điểm Tuyến tính + Bảng Quyết định)",
        "mathematical_structure": "DYNAMIC_FUNCTION_INTERSECTION",
        "spec_id": "YD-TRANSFER-C-SOLAR_VS_GRID",
        "title": "Bài Toán Quyết Định Năng Lượng: Lắp Điện Mặt Trời Hay Dùng Điện Lưới?",
        "grade": 8,
        "quantities": {"fixed_A": 18, "rate_A": 0.5, "fixed_B": 0, "rate_B": 2.0},
        "invariant_relation": "C_A(t) = 18 + 0.5*t; C_B(t) = 2.0*t",
        "domain_constraint": "t >= 0 (tháng)",
        "target_equation": "18 + 0.5*t = 2.0*t <=> 1.5*t = 18 <=> t = 12 (tháng)",
        "expected_solution": "12",
    },
    {
        "benchmark_id": "TRANSFER_TEST_D_UNSUPPORTED_HONEST_RECOGNITION",
        "test_category": "Test D — Nhận diện Trung thực Cấu trúc Chưa Hỗ trợ (Giải tích Tích phân / Hình học Vi phân)",
        "mathematical_structure": "SYMBOLIC_RIEMANN_INTEGRAL_3D_SURFACE_OF_REVOLUTION",
        "spec_id": "YD-TRANSFER-D-UNSUPPORTED-CALCULUS",
        "title": "Tính Thể Tích Khối Tròn Xoay Bằng Tích Phân Xác Định ∫ π f(x)² dx",
        "grade": 12,
        "quantities": {"lower": 0, "upper": 4},
        "invariant_relation": "V = pi * integral(f(x)^2, x, a, b)",
        "domain_constraint": "x in [0, 4]",
        "target_equation": "V = int_0^4 pi * x dx = 8*pi",
        "required_new_primitives": [
            "PRIM_RIEMANN_SLICE_INTEGRATOR_G12",
            "PRIM_SYMBOLIC_ANTIDERIVATIVE_STEPPER",
        ],
    },
]


class MathematicalBehaviorAndComposer:
    """Module 3: Gắn hành vi Toán học vào Living Asset và tổ hợp trải nghiệm mới từ cấu trúc."""

    def __init__(self, semantics_engine):
        self.semantics_engine = semantics_engine

    def get_primitives_metadata(self, primitive_ids: List[str]) -> List[Dict[str, Any]]:
        return [
            COMPOSABLE_PRIMITIVES_CATALOG[pid]
            for pid in primitive_ids
            if pid in COMPOSABLE_PRIMITIVES_CATALOG
        ]

    def evaluate_asset_interaction(
        self, asset_spec: Dict[str, Any], action_payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Thực thi một hành động tương tác của học sinh trên Living Asset và trả về trạng thái Toán học mới
        cùng chẩn đoán sai lầm mà KHÔNG BAO GIỜ tự ý sửa đổi giả thiết đề bài.
        """
        aid = asset_spec["asset_id"]
        engine_type = asset_spec["interactive_engine"]["engine_type"]
        params = asset_spec["interactive_engine"]["parameters"]
        trial_val = float(action_payload.get("value", params.get("default_trial", 1)))

        if engine_type == "GRID_TILING_GCD":
            W, H = int(params["width"]), int(params["height"])
            d = max(1, int(round(trial_val)))
            rem_w, rem_h = W % d, H % d
            fits = (rem_w == 0) and (rem_h == 0)
            gcd_val = math.gcd(W, H)
            return {
                "asset_id": aid,
                "trial_tile_size": d,
                "remainder_width": rem_w,
                "remainder_height": rem_h,
                "fits_perfectly": fits,
                "is_maximal_gcd": fits and (d == gcd_val),
                "tiles_count": (W // d) * (H // d) if fits else None,
                "feedback": (
                    f"Chính xác! Cạnh gạch d = {d} dm là ƯCLN({W}, {H}), lát khít {(W//d)*(H//d)} viên lớn nhất!"
                    if (fits and d == gcd_val)
                    else (
                        f"Gạch cạnh d = {d} dm lát vừa sân (ước chung), nhưng chưa phải viên gạch lớn nhất (ƯCLN = {gcd_val})."
                        if fits
                        else f"Phản ví dụ xuất hiện: Cạnh d = {d} dm làm dư {rem_w} dm chiều dài và {rem_h} dm chiều rộng (phải cắt gạch!)."
                    )
                ),
            }

        if engine_type == "RATE_BALANCE_RATIONAL":
            Q = float(params["Q"])
            k = float(params["k"])
            target_delta = float(params["target_delta"])
            mode = params.get("mode", "add_divisor")
            if trial_val <= 0 or (mode == "sub_divisor" and trial_val <= k):
                return {
                    "asset_id": aid,
                    "valid_domain": False,
                    "feedback": f"Vi phạm điều kiện xác định: x = {trial_val} không thỏa mãn miền xác định của bài toán.",
                }
            plan_v = Q / trial_val
            act_v = Q / (trial_val + k) if mode == "add_divisor" else Q / (trial_val - k)
            cur_delta = (plan_v - act_v) if mode == "add_divisor" else (act_v - plan_v)
            err = cur_delta - target_delta
            is_sol = abs(err) < 1e-6
            return {
                "asset_id": aid,
                "valid_domain": True,
                "trial_x": trial_val,
                "plan_rate": round(plan_v, 4),
                "actual_rate": round(act_v, 4),
                "current_delta": round(cur_delta, 4),
                "locked_hypothesis_delta": target_delta,
                "balance_tilt_error": round(err, 4),
                "is_solution": is_sol,
                "feedback": (
                    f"CÂN BẰNG CHÍNH XÁC! Tại x = {trial_val:g}, độ chênh lệch đúng bằng giả thiết Δ = {target_delta:g}."
                    if is_sol
                    else f"Đĩa cân đang nghiêng! Tại x = {trial_val:g}, chênh lệch thực tế là {cur_delta:.2f} ≠ giả thiết Δ = {target_delta:g} (lệch {err:+.2f})."
                ),
            }

        if engine_type == "DUAL_PIPE_HARMONIC":
            x_h = float(params["pipe1_hours"])
            y_h = float(trial_val)
            rate_sum = (1.0 / x_h) + (1.0 / y_h)
            joint_T = 1.0 / rate_sum
            wrong_sum = x_h + y_h
            return {
                "asset_id": aid,
                "pipe1_hours": x_h,
                "pipe2_hours": y_h,
                "hourly_fraction_filled": round(rate_sum, 4),
                "joint_fill_hours": round(joint_T, 4),
                "misconception_sum_hours": wrong_sum,
                "feedback": (
                    f"Hai vòi cùng chảy lấp đầy {rate_sum:.3f} bể mỗi giờ ⇒ Đầy bể sau T = {joint_T:.2f} giờ (nhanh hơn cả {x_h}h và {y_h}h, bác bỏ hoàn toàn sai lầm cộng thời gian {wrong_sum}h!)."
                ),
            }

        # Default generic invariant evaluation
        target = float(params.get("target_solution", 1))
        err = trial_val - target
        return {
            "asset_id": aid,
            "trial_value": trial_val,
            "target_solution": target,
            "residual_error": round(err, 4),
            "is_solution": abs(err) < 1e-5,
            "feedback": (
                f"Trạng thái đạt chuẩn bất biến tại giá trị = {trial_val:g}!"
                if abs(err) < 1e-5
                else f"Đang thử nghiệm giá trị = {trial_val:g} (độ lệch so với điểm cân bằng: {err:+.2f})."
            ),
        }

    def synthesize_experience_from_spec(self, raw_spec: Dict[str, Any]) -> Dict[str, Any]:
        """
        BỘ SINH TRẢI NGHIỆM TỪ CẤU TRÚC TOÁN MỚI (GENERATIVE EXPERIENCE CAPABILITY).
        Phân tích cấu trúc Toán học, chọn các Primitive có sẵn, kết hợp thành kịch bản tương tác,
        hoặc trung thực báo cáo UNSUPPORTED_STRUCTURE.
        """
        parsed = self.semantics_engine.parse_external_problem_spec(raw_spec)
        if not parsed.get("supported"):
            return {
                "synthesis_status": "UNSUPPORTED_STRUCTURE_HONESTLY_DECLINED",
                "spec_id": raw_spec.get("spec_id", "UNKNOWN"),
                "title": raw_spec.get("title", ""),
                "diagnostics": parsed,
            }

        prims = self.get_primitives_metadata(parsed["primitives_selected"])
        return {
            "synthesis_status": "EXPERIENCE_SYNTHESIZED_FROM_PRIMITIVES",
            "spec_id": parsed["spec_id"],
            "title": parsed["title"],
            "grade": parsed["grade"],
            "family_id": parsed["family_id"],
            "artistic_world": parsed["artistic_world"],
            "composed_primitives": [p["primitive_id"] for p in prims],
            "composed_actions": [act for p in prims for act in p["supported_actions"]],
            "invariant_bound": parsed["invariant_relation"],
            "domain_guard": parsed["domain_constraint"],
            "target_equation": parsed["target_equation"],
            "expected_solution": raw_spec.get("expected_solution", ""),
            "counterexample_rules": [p["counterexample_generator"] for p in prims],
        }

    def run_all_transfer_benchmarks(self) -> Dict[str, Any]:
        """Chạy 4 bài kiểm thử chuyển giao cấu trúc mới (Test A, B, C, D)."""
        results = []
        for bm in GENERATIVE_TRANSFER_BENCHMARKS:
            res = self.synthesize_experience_from_spec(bm)
            res["benchmark_id"] = bm["benchmark_id"]
            res["test_category"] = bm["test_category"]
            results.append(res)
        return {
            "total_benchmarks": len(results),
            "synthesized_count": sum(
                1 for r in results if r["synthesis_status"] == "EXPERIENCE_SYNTHESIZED_FROM_PRIMITIVES"
            ),
            "unsupported_honestly_declined_count": sum(
                1 for r in results if r["synthesis_status"] == "UNSUPPORTED_STRUCTURE_HONESTLY_DECLINED"
            ),
            "benchmarks": results,
        }
