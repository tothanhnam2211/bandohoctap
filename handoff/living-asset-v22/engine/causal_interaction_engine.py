# -*- coding: utf-8 -*-
"""
YOURDREAM CAUSAL INTERACTION ENGINE (engine/causal_interaction_engine.py)
========================================================================
Động cơ Tương tác Nhân - Quả Liên kết Đa Biểu diễn (Causal Multi-Representation Engine):
Kế thừa & Nâng tầm Bản quyền Tác giả của `nang_suat.html`:
1. Mô hình Đồ thị Nhân - Quả (Causal Directed Graph: Action Cause -> Physical Mediators -> Equilibrium State).
2. Cán cân Thăng bằng Đại số & Hình học (Dynamic Algebraic Balance Scale & Torque Equilibrium).
3. Sổ tay Lập luận Nhân - Quả Tức thì (Instant Socratic Causal Reasoning Log / Thought Ribbon).
4. Bảo toàn Tuyệt đối Bất biến Giả thiết (Strict Hypothesis Invariance Protection).
5. Phục vụ 16 Flagship Living Assets trên cả 4 mạch kiến thức THCS GDPT 2018.
"""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class CausalNode:
    """Biến số hoặc đối tượng trong mạng lưới nhân - quả."""
    id: str
    symbol: str
    label_vi: str
    unit: str
    role: str  # "ACTION_CAUSE" | "PHYSICAL_MEDIATOR" | "INVARIANT_CONSTANT" | "OBSERVATION_STATE"
    value: float
    min_val: float = 0.0
    max_val: float = 100.0


@dataclass
class CausalBalanceResult:
    """Trạng thái phản hồi của Cán Cân Thăng Bằng Nhân - Quả."""
    tilt_angle_deg: float         # Góc nghiêng cán cân (-30° đến +30°)
    left_weight: float            # Giá trị vế trái (Ví dụ: Thời gian dự định T1)
    right_weight: float           # Giá trị vế phải (Ví dụ: Thời gian thực tế T2 + delta)
    imbalance_delta: float        # Độ lệch |Vế trái - Vế phải|
    is_equilibrium: bool          # Đạt trạng thái cân bằng chuẩn
    torque_direction: str         # "BALANCED" | "LEAN_LEFT" | "LEAN_RIGHT"
    cause_action_text: str        # Mô tả hành động của học sinh
    physical_consequence_text: str # Hệ quả vật lý / hình học trực tiếp
    socratic_reasoning_text: str  # Lời diễn giải sư phạm Socratic
    hypothesis_locked_proof: str  # Bằng chứng bảo vệ bất biến đề bài


class CausalInteractionEngine:
    """Động cơ Tương tác Nhân - Quả Trung Tâm cho Living Assets."""

    def __init__(self):
        self._registry: Dict[str, Dict[str, Any]] = {}
        self._init_16_causal_systems()

    def _init_16_causal_systems(self) -> None:
        """Đăng ký mô hình nhân - quả chuẩn hóa cho 16 Living Assets."""

        # 1. YD-LA-NUM-G6-01: Lát gạch sân đình (ƯCLN & Bội số)
        self._registry["YD-LA-NUM-G6-01"] = {
            "title": "Lát Gạch Sân Đình Cổ (24 × 18 dm)",
            "cause_var": "d",
            "cause_label": "Kích thước cạnh viên gạch vuông d (dm)",
            "min_val": 1, "max_val": 12, "target": 6,
            "invariants": {"width": 24, "height": 18, "unit": "dm"},
            "eval_fn": lambda d: self._eval_grid_tiling(d, 24, 18, 6),
        }

        # 2. YD-LA-NUM-G6-02: Tàu ngầm đo độ sâu (Số nguyên)
        self._registry["YD-LA-NUM-G6-02"] = {
            "title": "Tàu Ngầm Đo Độ Sâu Đại Dương (-120 m)",
            "cause_var": "k",
            "cause_label": "Số khoang nước dằn xả bỏ (mỗi khoang tương đương 15 m)",
            "min_val": 0, "max_val": 6, "target": 3,
            "invariants": {"initial_depth": -120, "chamber_val": 15, "target_depth": -75},
            "eval_fn": lambda k: self._eval_submarine(k, -120, 15, 3),
        }

        # 3. YD-LA-NUM-G6-03: Chiếc bánh sinh nhật tỉ lệ (Phân số & Nồng độ)
        self._registry["YD-LA-NUM-G6-03"] = {
            "title": "Pha Nước Cam Tỉ Lệ (Bình 400 ml, 25% cốt cam)",
            "cause_var": "w",
            "cause_label": "Thể tích nước lọc thêm vào (ml)",
            "min_val": 0, "max_val": 300, "target": 100,
            "invariants": {"v_initial": 400, "p_initial": 0.25, "v_cam_pure": 100},
            "eval_fn": lambda w: self._eval_orange_juice(w, 400, 100, 100),
        }

        # 4. YD-LA-NUM-G7-04: Cắt ghép hình vuông (Số vô tỉ & Căn bậc hai)
        self._registry["YD-LA-NUM-G7-04"] = {
            "title": "Đo Cạnh Hình Vuông Ghép (Diện tích S = 2 dm²)",
            "cause_var": "d",
            "cause_label": "Cạnh thử nghiệm d (dm)",
            "min_val": 1.0, "max_val": 2.0, "target": math.sqrt(2),
            "invariants": {"area_target": 2.0},
            "eval_fn": lambda d: self._eval_irrational_square(d, 2.0),
        }

        # 5. YD-LA-ALG-G7-05: Cầu cân bằng tỉ lệ thức (Dãy tỉ số bằng nhau)
        self._registry["YD-LA-ALG-G7-05"] = {
            "title": "Cầu Cân Bằng Đòn Bẩy Đồng Thau (Tỉ lệ 3 : 2, Tổng 150g)",
            "cause_var": "k",
            "cause_label": "Hệ số tỉ lệ k = x/3 = y/2",
            "min_val": 10, "max_val": 50, "target": 30,
            "invariants": {"ratio_x": 3, "ratio_y": 2, "total_weight": 150},
            "eval_fn": lambda k: self._eval_lever_ratio(k, 3, 2, 150),
        }

        # 6. YD-LA-ALG-G7-06: Chi phí hai hãng xe taxi (Đa thức & Hàm số)
        self._registry["YD-LA-ALG-G7-06"] = {
            "title": "So Sánh Chi Phí Hai Hãng Xe Taxi",
            "cause_var": "x",
            "cause_label": "Quãng đường di chuyển x (km)",
            "min_val": 1, "max_val": 10, "target": 5,
            "invariants": {"rate_a": 12, "open_a": 10, "rate_b": 10, "open_b": 20},
            "eval_fn": lambda x: self._eval_taxi_fare(x, 12, 10, 10, 20),
        }

        # 7. YD-LA-ALG-G8-07: Đoàn xe vận tải lương thực (Năng suất chuẩn `nang_suat.html`)
        self._registry["YD-LA-ALG-G8-07"] = {
            "title": "Đoàn Xe Vận Tải Lương Thực Cứu Trợ (60 tấn, thêm 3 xe)",
            "cause_var": "x",
            "cause_label": "Năng suất dự kiến mỗi xe chở x (tấn/xe)",
            "min_val": 5, "max_val": 20, "target": 12,
            "invariants": {"Q": 60, "extra_vehicles": 3, "delta_target": 1.0},
            "eval_fn": lambda x: self._eval_transport_convoy(x, 60, 3, 1.0),
        }

        # 8. YD-LA-ALG-G8-08: Hai vòi nước cùng chảy vào bể (Lưu lượng điều hòa)
        self._registry["YD-LA-ALG-G8-08"] = {
            "title": "Hai Vòi Nước Cùng Chảy Vào Bể Cạn",
            "cause_var": "x",
            "cause_label": "Thời gian vòi thứ nhất chảy một mình x (giờ)",
            "min_val": 2, "max_val": 8, "target": 4,
            "invariants": {"time_diff": 2, "t_joint": 2.4},  # 12/5 = 2.4 giờ
            "eval_fn": lambda x: self._eval_two_pipes(x, 2, 2.4),
        }

        # 9. YD-LA-ALG-G9-09: Vòm cầu giao thông parabol (y = ax²)
        self._registry["YD-LA-ALG-G9-09"] = {
            "title": "Vòm Cầu Parabol & Tĩnh Không Sà Lan An Toàn",
            "cause_var": "x",
            "cause_label": "Hoành độ mép sà lan từ tâm vòm x (m)",
            "min_val": 0, "max_val": 10, "target": 4,
            "invariants": {"arch_span": 24, "arch_height": 9, "barge_width": 8, "barge_height": 6},
            "eval_fn": lambda x: self._eval_parabolic_arch(x, 24, 9, 8, 6),
        }

        # 10. YD-LA-ALG-G9-10: Giao lộ hai luồng xe (Hệ hai phương trình bậc nhất 2 ẩn)
        self._registry["YD-LA-ALG-G9-10"] = {
            "title": "Điều Tiết Hai Luồng Xe Qua Cầu Cân Bằng",
            "cause_var": "x",
            "cause_label": "Lưu lượng luồng xe thứ nhất x (xe/phút)",
            "min_val": 10, "max_val": 50, "target": 30,
            "invariants": {"total_capacity": 50, "target_flow": 30},
            "eval_fn": lambda x: self._eval_traffic_flow(x, 50, 30),
        }

        # 11. YD-LA-GEO-G7-11: Kính tiệm cận góc so le trong (Đường thẳng song song)
        self._registry["YD-LA-GEO-G7-11"] = {
            "title": "Kính Tiệm Cận Góc So Le & Hai Tia Song Song",
            "cause_var": "alpha",
            "cause_label": "Góc quay của tia ngắm α (độ)",
            "min_val": 30, "max_val": 120, "target": 60,
            "invariants": {"parallel_target_angle": 60},
            "eval_fn": lambda a: self._eval_parallel_angles(a, 60),
        }

        # 12. YD-LA-GEO-G7-12: Giàn thép tam giác bằng nhau
        self._registry["YD-LA-GEO-G7-12"] = {
            "title": "Khung Giàn Thép Cầu Treo (Tam Giác Bằng Nhau c-c-c)",
            "cause_var": "c",
            "cause_label": "Độ dài thanh giằng chịu lực c (m)",
            "min_val": 3, "max_val": 8, "target": 5,
            "invariants": {"side_a": 3, "side_b": 4, "target_c": 5},
            "eval_fn": lambda c: self._eval_triangle_congruence(c, 3, 4, 5),
        }

        # 13. YD-LA-GEO-G8-13: Chiếc thang dựa tường Pythagore
        self._registry["YD-LA-GEO-G8-13"] = {
            "title": "Chiếc Thang Dựa Tường Định Lý Pythagore",
            "cause_var": "L",
            "cause_label": "Chiều dài chiếc thang L (m)",
            "min_val": 3.5, "max_val": 7.0, "target": 5.0,
            "invariants": {"base_dist": 3.0, "wall_height": 4.0},
            "eval_fn": lambda l: self._eval_pythagoras(l, 3.0, 4.0),
        }

        # 14. YD-LA-GEO-G9-14: Ngọn hải đăng & Góc nội tiếp
        self._registry["YD-LA-GEO-G9-14"] = {
            "title": "Ngọn Hải Đăng & Góc Nội Tiếp Chắn Cung",
            "cause_var": "angle_p",
            "cause_label": "Góc ngắm từ tàu thuyền ∠APB (độ)",
            "min_val": 20, "max_val": 80, "target": 45,
            "invariants": {"central_angle": 90},  # Góc ở tâm = 90° => Góc nội tiếp = 45°
            "eval_fn": lambda a: self._eval_inscribed_angle(a, 90),
        }

        # 15. YD-LA-STA-G6-15: Biểu đồ cột khảo sát đọc sách (Thống kê)
        self._registry["YD-LA-STA-G6-15"] = {
            "title": "Cân Bằng Tổng Tỉ Lệ Khảo Sát Thói Quen Đọc Sách",
            "cause_var": "n_book",
            "cause_label": "Số học sinh nhóm thích Sách Khoa học n (học sinh)",
            "min_val": 5, "max_val": 35, "target": 20,
            "invariants": {"total_students": 50, "other_groups": 30},
            "eval_fn": lambda n: self._eval_statistics_sum(n, 50, 30),
        }

        # 16. YD-LA-STA-G8-16: Vòng quay may mắn hội làng (Xác suất thực nghiệm)
        self._registry["YD-LA-STA-G8-16"] = {
            "title": "Vòng Quay May Mắn & Hội Tụ Xác Suất Thực Nghiệm",
            "cause_var": "trials",
            "cause_label": "Số lượt quay thử nghiệm N (lượt)",
            "min_val": 10, "max_val": 200, "target": 120,
            "invariants": {"p_theoretical": 0.25, "lucky_sectors": 2, "total_sectors": 8},
            "eval_fn": lambda t: self._eval_probability_convergence(t, 0.25),
        }

    # --- Evaluator Functions ---

    def _eval_transport_convoy(self, x: float, Q: float, k: float, delta_target: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả đoàn xe vận tải lương thực (kế thừa nang_suat.html)."""
        x_val = max(1.0, float(x))
        T1 = Q / x_val
        T2 = Q / (x_val + k)
        actual_delta = T1 - T2
        diff = actual_delta - delta_target
        is_eq = abs(diff) < 0.02

        # Cán cân nghiêng: T1 bên trái, (T2 + delta_target) bên phải
        tilt = max(-30.0, min(30.0, diff * 22.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh thử nghiệm năng suất mỗi xe: x = {x_val:.1f} tấn/xe."
        phys_text = (
            f"Kế hoạch cần {T1:.2f} xe/chuyến. Thực tế bổ sung {int(k)} xe, "
            f"mỗi xe chở {x_val + k:.1f} tấn nên cần {T2:.2f} xe/chuyến. "
            f"Độ lệch thời gian thực tế: Δt = {actual_delta:.2f} ngày."
        )

        if is_eq:
            soc_text = (
                f"★ HOÀN TOÀN CÂN BẰNG! Khi x = {x_val:.0f} tấn, dự định cần {T1:.0f} xe, "
                f"thực tế có {int(T1 + k)} xe chở {x_val + k:.0f} tấn/xe. "
                f"Thời gian rút ngắn đúng {delta_target:.1f} ngày ({T1:.0f} - {T2:.0f} = {delta_target:.0f}). "
                f"Phương trình nghiệm đúng: 60/{x_val:.0f} - 60/{x_val+k:.0f} = 1."
            )
        elif diff > 0:
            soc_text = (
                f"Cán cân nghiêng sang TRÁI (Δt = {actual_delta:.2f} > 1 ngày): "
                f"Năng suất x = {x_val:.1f} tấn là QUÁ NHỎ! Dự định cần tới {T1:.2f} xe, "
                f"thời gian dự định kéo dài vượt mức kế hoạch. Hãy TĂNG năng suất x!"
            )
        else:
            soc_text = (
                f"Cán cân nghiêng sang PHẢI (Δt = {actual_delta:.2f} < 1 ngày): "
                f"Năng suất x = {x_val:.1f} tấn là QUÁ LỚN! Dự định chỉ cần {T1:.2f} xe, "
                f"việc thêm {int(k)} xe không tạo ra đủ 1 ngày chênh lệch như đề bài yêu cầu. Hãy GIẢM năng suất x!"
            )

        proof = f"BẤT BIẾN BẢO TOÀN: Tổng lượng hàng Q = {int(Q)} tấn; Số xe bổ sung k = {int(k)} xe; Độ lệch kế hoạch = {delta_target:.1f} ngày."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(T1, 2),
            right_weight=round(T2 + delta_target, 2),
            imbalance_delta=round(abs(diff), 3),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_grid_tiling(self, d: float, w: int, h: int, target_gcd: int) -> CausalBalanceResult:
        """Đánh giá nhân - quả lát gạch sân đình."""
        d_val = max(1, round(d))
        rem_w = w % d_val
        rem_h = h % d_val
        total_rem = rem_w + rem_h
        is_eq = (d_val == target_gcd)
        fits = (rem_w == 0 and rem_h == 0)

        tilt = 0.0 if is_eq else (-25.0 if not fits else (15.0 if d_val < target_gcd else -20.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if not fits else "LEAN_RIGHT")

        cause_text = f"Học sinh thử chọn cạnh gạch vuông: d = {d_val} dm."
        phys_text = (
            f"Chiều dài 24 dm xếp được {w // d_val} viên (dư {rem_w} dm). "
            f"Chiều rộng 18 dm xếp được {h // d_val} viên (dư {rem_h} dm). "
            f"Tổng phần thừa phải chặt gạch: {total_rem} dm."
        )

        if is_eq:
            soc_text = (
                f"★ CÂN BẰNG TỐI ĐA! d = {d_val} dm chính là ƯCLN(24, 18). "
                f"Sân được lát khít hoàn hảo bởi (24:6) × (18:6) = 4 × 3 = 12 viên gạch. Không viên gạch nào bị cắt!"
            )
        elif not fits:
            soc_text = (
                f"MẤT CÂN BẰNG (Dư {total_rem} dm): Cạnh d = {d_val} không phải là ước chung! "
                f"Thợ xây phải cắt vỡ gạch để chèn vào mép sân. Hãy chọn d là ước của cả 24 và 18."
            )
        else:
            soc_text = (
                f"GẠCH LÁT KHÍT NHƯNG CHƯA TỐI ĐA: d = {d_val} dm là ước chung, nhưng chưa phải ƯCLN! "
                f"Số lượng gạch cần mua quá nhiều ({ (w//d_val)*(h//d_val) } viên). Hãy tăng kích thước viên gạch lên!"
            )

        proof = f"BẤT BIẾN BẢO TOÀN: Chiều dài sân a = {w} dm; Chiều rộng sân b = {h} dm."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=float(d_val),
            right_weight=float(target_gcd),
            imbalance_delta=float(abs(d_val - target_gcd)),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_submarine(self, k: float, h0: float, step_h: float, target_k: int) -> CausalBalanceResult:
        """Đánh giá nhân - quả tàu ngầm số nguyên."""
        k_val = max(0, round(k))
        current_depth = h0 + k_val * step_h
        target_depth = h0 + target_k * step_h
        diff = current_depth - target_depth
        is_eq = (k_val == target_k)

        tilt = max(-30.0, min(30.0, diff * 1.5))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff < 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh xả bỏ {k_val} khoang nước dằn."
        phys_text = f"Độ sâu hiện tại: {current_depth} m (Độ sâu chỉ định: {target_depth} m)."
        soc_text = (
            f"★ CÂN BẰNG ĐỘ SÂU! Tàu đạt đúng độ sâu {target_depth} m theo phép tính: (-120) - (-{k_val*int(step_h)}) = {target_depth} m."
            if is_eq else
            f"CHƯA ĐẠT ĐỘ SÂU CHỈ ĐỊNH: Tàu đang ở {current_depth} m ({'SÂU HƠN' if current_depth < target_depth else 'NÔNG HƠN'} mục tiêu {abs(diff)} m)."
        )
        proof = f"BẤT BIẾN: Độ sâu xuất phát h = {int(h0)} m; Khối lượng mỗi khoang = {int(step_h)} m tương đương."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=float(current_depth),
            right_weight=float(target_depth),
            imbalance_delta=float(abs(diff)),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_orange_juice(self, w: float, v0: float, v_cam: float, target_w: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả pha nước cam phân số."""
        w_val = max(0.0, float(w))
        v_total = v0 + w_val
        p_current = (v_cam / v_total) * 100.0
        p_target = (v_cam / (v0 + target_w)) * 100.0
        diff = p_current - p_target
        is_eq = abs(w_val - target_w) < 1.0

        tilt = max(-30.0, min(30.0, diff * 5.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh thêm {w_val:.0f} ml nước lọc vào bình 400 ml."
        phys_text = f"Tổng thể tích mới: {v_total:.0f} ml. Nồng độ cốt cam mới: {p_current:.1f}% (Mục tiêu: 20.0%)."
        soc_text = (
            f"★ NỒNG ĐỘ CHUẨN XÁC 20%! Bất biến lượng cốt cam 100 ml được bảo toàn: 100 / (400 + 100) × 100% = 20%."
            if is_eq else
            f"NỒNG ĐỘ CHƯA ĐẠT: Nước cam đang {'QUÁ ĐẬM ĐẶC' if p_current > p_target else 'QUÁ LOÃNG'} ({p_current:.1f}% so với 20%)."
        )
        proof = f"BẤT BIẾN: Thể tích cốt cam nguyên chất V_cam = {int(v_cam)} ml không đổi khi thêm nước lọc."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(p_current, 1),
            right_weight=round(p_target, 1),
            imbalance_delta=round(abs(diff), 2),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_irrational_square(self, d: float, target_area: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả số vô tỉ & diện tích hình vuông."""
        d_val = max(0.1, float(d))
        calc_area = d_val * d_val
        diff = calc_area - target_area
        is_eq = abs(diff) < 0.02

        tilt = max(-30.0, min(30.0, diff * 35.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh chọn cạnh hình vuông: d = {d_val:.4f} dm."
        phys_text = f"Diện tích hình vuông sinh ra: d² = {calc_area:.4f} dm² (Mục tiêu: {target_area:.1f} dm²)."
        soc_text = (
            f"★ DIỆN TÍCH TRÙNG KHÍT! d² ≈ 2 dm² => d = √2 ≈ 1.4142... thuộc tập số vô tỉ 𝕀."
            if is_eq else
            f"CHƯA TRÙNG KHÍT: d² = {calc_area:.4f} {'LỚN HƠN' if diff > 0 else 'NHỎ HƠN'} diện tích 2 hình vuông ban đầu ghép lại!"
        )
        proof = "BẤT BIẾN: Tổng diện tích 2 hình vuông cạnh 1 dm là S = 1² + 1² = 2 dm²."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(calc_area, 3),
            right_weight=float(target_area),
            imbalance_delta=round(abs(diff), 3),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_lever_ratio(self, k: float, rx: int, ry: int, total_w: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả tỉ lệ thức & đòn bẩy Archimedes."""
        k_val = max(1.0, float(k))
        x_calc = rx * k_val
        y_calc = ry * k_val
        sum_calc = x_calc + y_calc
        diff = sum_calc - total_w
        is_eq = abs(diff) < 0.1

        tilt = max(-30.0, min(30.0, diff * 1.5))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh thử hệ số tỉ lệ k = {k_val:.1f}."
        phys_text = f"Khối lượng Đồng x = {x_calc:.1f}g, Kẽm y = {y_calc:.1f}g. Tổng: {sum_calc:.1f}g (Yêu cầu: {int(total_w)}g)."
        soc_text = (
            f"★ ĐÒN BẨY ĐỒNG THAU CÂN BẰNG! Với k = 30, Đồng x = 90g và Kẽm y = 60g, tỉ số x/3 = y/2 = 30 và tổng 90 + 60 = 150g."
            if is_eq else
            f"ĐÒN BẨY LỆCH TẢI: Tổng khối lượng {sum_calc:.1f}g {'NẶNG HƠN' if diff > 0 else 'NHẸ HƠN'} khối lượng thỏi đồng thau {int(total_w)}g!"
        )
        proof = f"BẤT BIẾN: Tỉ số nguyên tố hợp kim x : y = {rx} : {ry}; Khối lượng thau = {int(total_w)}g."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(sum_calc, 1),
            right_weight=float(total_w),
            imbalance_delta=round(abs(diff), 2),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_taxi_fare(self, x: float, rA: float, oA: float, rB: float, oB: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả chi phí taxi."""
        x_val = max(0.5, float(x))
        yA = rA * x_val + oA
        yB = rB * x_val + oB
        diff = yA - yB
        is_eq = abs(diff) < 0.5

        tilt = max(-30.0, min(30.0, diff * 3.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh chọn quãng đường x = {x_val:.1f} km."
        phys_text = f"Hãng A: y1 = {yA:.1f}k, Hãng B: y2 = {yB:.1f}k. Chênh lệch: {abs(diff):.1f} nghìn đồng."
        soc_text = (
            f"★ ĐIỂM GIAO NHAU CÂN BẰNG CHI PHÍ! Tại x = 5 km, cả hai hãng đều có chi phí bằng nhau: y = 70 nghìn đồng."
            if is_eq else
            f"CHI PHÍ CHÊNH LỆCH: Tại x = {x_val:.1f} km, Hãng {'A ĐẮT HƠN' if diff > 0 else 'B ĐẮT HƠN'} {abs(diff):.1f}k!"
        )
        proof = f"BẤT BIẾN: Giá cước Hãng A: y1 = {int(rA)}x + {int(oA)}; Hãng B: y2 = {int(rB)}x + {int(oB)}."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(yA, 1),
            right_weight=round(yB, 1),
            imbalance_delta=round(abs(diff), 2),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_two_pipes(self, x: float, diff_h: float, t_joint: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả hai vòi nước cùng chảy."""
        x_val = max(0.5, float(x))
        y_val = x_val + diff_h
        flow_joint = (1.0 / x_val) + (1.0 / y_val)
        target_flow = 1.0 / t_joint
        diff = flow_joint - target_flow
        is_eq = abs(diff) < 0.01

        tilt = max(-30.0, min(30.0, diff * 120.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh chọn thời gian vòi 1 chảy một mình: x = {x_val:.1f} giờ."
        phys_text = f"Vòi 1 chảy 1/x = {1/x_val:.3f} bể/h, Vòi 2 chảy 1/(x+{int(diff_h)}) = {1/y_val:.3f} bể/h. Tổng: {flow_joint:.3f} bể/h (Mục tiêu: {target_flow:.3f})."
        soc_text = (
            f"★ CÂN BẰNG LƯU LƯỢNG NẠP BỂ! Khi x = 4h, vòi 1 chảy 1/4 bể/h, vòi 2 chảy 1/6 bể/h. Tổng 1/4 + 1/6 = 5/12 bể/h => T = 12/5 = 2.4 giờ (2h24p) đầy bể."
            if is_eq else
            f"LƯU LƯỢNG CHƯA ĐỒNG BỘ: Hai vòi đang nạp {'NHANH HƠN' if diff > 0 else 'CHẬM HƠN'} quy chuẩn 2 giờ 24 phút của đề bài!"
        )
        proof = f"BẤT BIẾN: Chênh lệch thời gian hai vòi = {int(diff_h)} giờ; Thời gian cùng chảy T = {t_joint:.1f} giờ."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(flow_joint, 3),
            right_weight=round(target_flow, 3),
            imbalance_delta=round(abs(diff), 3),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_parabolic_arch(self, x: float, span: float, h_arch: float, b_w: float, b_h: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả vòm cầu parabol."""
        x_val = max(0.0, float(x))
        # a = -9 / (12^2) = -1/16
        y_val = -(1.0 / 16.0) * (x_val ** 2)
        clearance = h_arch + y_val  # Độ cao từ mặt nước lên vòm tại x
        target_clearance = 8.0     # Tại x = 4 (mép sà lan)
        diff = clearance - target_clearance
        is_eq = abs(x_val - 4.0) < 0.1

        tilt = max(-30.0, min(30.0, (x_val - 4.0) * 8.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if x_val < 4.0 else "LEAN_RIGHT")

        cause_text = f"Học sinh kiểm tra tọa độ mép tải: x = {x_val:.1f} m."
        phys_text = f"Độ cao vòm cầu tại x = {x_val:.1f}m là H = {clearance:.2f} m. Độ cao tĩnh không sà lan: {b_h} m."
        soc_text = (
            f"★ TĨNH KHÔNG AN TOÀN TUYỆT ĐỐI! Tại mép sà lan x = 4m, vòm cầu đạt độ cao 8m > 6m. Sà lan chui qua an toàn với khoảng đệm an toàn 2m!"
            if is_eq else
            f"KHẢO SÁT VỊ TRÍ: Tại x = {x_val:.1f}m, tĩnh không đạt {clearance:.2f}m ({'ĐỦ' if clearance >= b_h else 'NGUY HIỂM VA CHẠM'} so với chiều cao sà lan {b_h}m)."
        )
        proof = f"BẤT BIẾN: Nhịp cầu {int(span)}m, chiều cao đỉnh vòm {int(h_arch)}m; Chiều rộng sà lan {int(b_w)}m, chiều cao {int(b_h)}m."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(clearance, 2),
            right_weight=float(b_h),
            imbalance_delta=round(abs(diff), 2),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_traffic_flow(self, x: float, total_cap: float, target_x: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả luồng xe hệ phương trình."""
        x_val = max(0.0, float(x))
        y_val = total_cap - x_val
        diff = x_val - target_x
        is_eq = abs(diff) < 0.5

        tilt = max(-30.0, min(30.0, diff * 1.5))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh điều tiết luồng xe 1: x = {x_val:.0f} xe/phút."
        phys_text = f"Luồng xe 1: {x_val:.0f} xe/phút; Luồng xe 2: {y_val:.0f} xe/phút. Tổng luồng: {total_cap:.0f} xe/phút."
        soc_text = (
            f"★ CÂN BẰNG NÚT GIAO THÔNG! Tại x = {int(target_x)} xe/phút, cả hai nhánh đều thông suốt không ùn tắc."
            if is_eq else
            f"LỆCH TẢI GIAO THÔNG: Nhánh {'1 QUÁ TẢI' if diff > 0 else '2 QUÁ TẢI'}, gây ùn ứ cục bộ!"
        )
        proof = f"BẤT BIẾN: Tổng công suất nút giao = {int(total_cap)} xe/phút."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=float(x_val),
            right_weight=float(target_x),
            imbalance_delta=float(abs(diff)),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_parallel_angles(self, alpha: float, target_a: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả góc so le trong & song song."""
        a_val = max(10.0, min(170.0, float(alpha)))
        diff = a_val - target_a
        is_eq = abs(diff) < 0.5

        tilt = max(-30.0, min(30.0, diff * 1.2))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh chỉnh góc ngắm tia: α = {a_val:.1f}°."
        phys_text = f"Góc so le trong: A1 = {a_val:.1f}°, B1 = {target_a:.1f}°. Độ lệch góc: {abs(diff):.1f}°."
        soc_text = (
            f"★ HAI ĐƯỜNG THẲNG SONG SONG TUYỆT ĐỐI! Khi góc so le trong A1 = B1 = {int(target_a)}°, tiên đề Ơ-clit được thỏa mãn: a // b."
            if is_eq else
            f"TIA ĐƯỜNG BỊ CẮT NHAU: Hai góc so le trong không bằng nhau ({a_val:.1f}° ≠ {target_a:.1f}°). Hai đường thẳng sẽ cắt nhau!"
        )
        proof = f"BẤT BIẾN: Góc chuẩn của đường thẳng cố định B1 = {int(target_a)}°."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(a_val, 1),
            right_weight=float(target_a),
            imbalance_delta=round(abs(diff), 1),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_triangle_congruence(self, c: float, a: float, b: float, target_c: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả tam giác bằng nhau."""
        c_val = max(1.0, float(c))
        diff = c_val - target_c
        is_eq = abs(diff) < 0.1

        tilt = max(-30.0, min(30.0, diff * 15.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh gia công thanh giằng c = {c_val:.1f} m."
        phys_text = f"Cạnh thanh giằng: {c_val:.1f}m (Yêu cầu khung giàn: {target_c:.1f}m)."
        soc_text = (
            f"★ KHUNG GIÀN KHỚP HOÀN TOÀN (c-c-c)! Tam giác ΔABC = ΔA'B'C' vững chắc, không biến dạng."
            if is_eq else
            f"LỖI KHUNG GIÀN: Thanh giằng c {'QUÁ DÀI' if diff > 0 else 'QUÁ NGẮN'}, không lắp vừa vào hai đỉnh tam giác!"
        )
        proof = f"BẤT BIẾN: Hai cạnh chuẩn của khung tam giác a = {int(a)}m, b = {int(b)}m."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(c_val, 1),
            right_weight=float(target_c),
            imbalance_delta=round(abs(diff), 2),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_pythagoras(self, L: float, a: float, b: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả định lý Pythagore."""
        l_val = max(1.0, float(L))
        hypotenuse = math.sqrt(a**2 + b**2)
        diff = l_val - hypotenuse
        is_eq = abs(diff) < 0.1

        tilt = max(-30.0, min(30.0, diff * 18.0))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh chọn chiều dài thang: L = {l_val:.2f} m."
        phys_text = f"Khoảng cách chân thang a = {a}m, độ cao tường b = {b}m. Chiều dài thang lý tưởng: c = √(3² + 4²) = {hypotenuse:.2f} m."
        soc_text = (
            f"★ ĐỊNH LÝ PYTHAGORE CÂN BẰNG! Chiếc thang 5m dựa chuẩn khít vào đỉnh tường 4m khi cách chân tường 3m (3² + 4² = 5²)."
            if is_eq else
            f"THANG KHÔNG CHẠM ĐÍNH: Thang {'DÀI THỪA' if diff > 0 else 'NGẮN KHÔNG VỚI TỚI'} đỉnh tường {abs(diff):.2f}m!"
        )
        proof = f"BẤT BIẾN: Chân tường vuông góc 90°; Chân thang cách tường a = {int(a)}m, độ cao tường b = {int(b)}m."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(l_val, 2),
            right_weight=round(hypotenuse, 2),
            imbalance_delta=round(abs(diff), 2),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_inscribed_angle(self, angle_p: float, central_angle: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả góc nội tiếp đường tròn."""
        a_val = max(5.0, min(170.0, float(angle_p)))
        target_a = central_angle / 2.0
        diff = a_val - target_a
        is_eq = abs(diff) < 0.5

        tilt = max(-30.0, min(30.0, diff * 1.5))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh dịch chuyển tàu ngắm: ∠APB = {a_val:.1f}°."
        phys_text = f"Góc ở tâm ngọn hải đăng ∠AOB = {int(central_angle)}°. Góc nội tiếp quan sát: ∠APB = {a_val:.1f}°."
        soc_text = (
            f"★ ĐỊNH LÝ GÓC NỘI TIẾP CHUẨN XÁC! ∠APB = 1/2 ∠AOB = {int(target_a)}° không đổi khi tàu di chuyển trên cùng cung tròn!"
            if is_eq else
            f"TÀU NẰM NGOÀI ĐƯỜNG TRÒN AN TOÀN: Góc ngắm {a_val:.1f}° ≠ {int(target_a)}°. Hãy điều chỉnh tàu vào đúng cung tròn hải đăng!"
        )
        proof = f"BẤT BIẾN: Hai tiêu điểm hải đăng cố định A và B; Góc ở tâm AOB = {int(central_angle)}°."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(a_val, 1),
            right_weight=float(target_a),
            imbalance_delta=round(abs(diff), 1),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_statistics_sum(self, n: float, total_s: int, other_g: int) -> CausalBalanceResult:
        """Đánh giá nhân - quả thống kê khảo sát đọc sách."""
        n_val = max(1, round(n))
        calc_total = other_g + n_val
        diff = calc_total - total_s
        is_eq = (calc_total == total_s)

        tilt = max(-30.0, min(30.0, diff * 2.5))
        direction = "BALANCED" if is_eq else ("LEAN_LEFT" if diff > 0 else "LEAN_RIGHT")

        cause_text = f"Học sinh điều chỉnh nhóm sách Khoa học: n = {n_val} bạn."
        phys_text = f"Tổng số học sinh khảo sát: {calc_total} bạn (Sĩ số toàn khối: {total_s} bạn)."
        soc_text = (
            f"★ DỮ LIỆU THỐNG KÊ CÂN BẰNG 100%! Nhóm khoa học chiếm n = 20 bạn (40%), bảo đảm tổng sĩ số khối đúng 50 bạn."
            if is_eq else
            f"LỆCH TỔNG SĨ SỐ THỐNG KÊ: Tổng mẫu {calc_total} bạn {'DƯ THỪA' if diff > 0 else 'THIẾU HỤT'} {abs(diff)} bạn so với danh sách lớp!"
        )
        proof = f"BẤT BIẾN: Sĩ số toàn khối = {total_s} học sinh; Các nhóm sở thích khác = {other_g} học sinh."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=float(calc_total),
            right_weight=float(total_s),
            imbalance_delta=float(abs(diff)),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def _eval_probability_convergence(self, trials: float, p_true: float) -> CausalBalanceResult:
        """Đánh giá nhân - quả xác suất thực nghiệm hội tụ xác suất lý thuyết."""
        n_trials = max(10, round(trials))
        # Định luật số lớn: độ lệch giảm theo 1/sqrt(N)
        simulated_err = 0.25 / math.sqrt(n_trials / 10.0)
        p_emp = p_true + (simulated_err if n_trials < 100 else 0.005)
        diff = p_emp - p_true
        is_eq = (n_trials >= 100)

        tilt = max(-30.0, min(30.0, (120 - n_trials) * 0.25))
        direction = "BALANCED" if is_eq else "LEAN_LEFT"

        cause_text = f"Học sinh thực hiện N = {n_trials} lượt quay thử nghiệm."
        phys_text = f"Xác suất thực nghiệm: P* = {p_emp:.3f}. Xác suất lý thuyết: P = {p_true:.3f} (2/8 ô trúng thưởng)."
        soc_text = (
            f"★ ĐỊNH LUẬT SỐ LỚN HỘI TỤ HOÀN HẢO! Khi N = {n_trials} lượt (đủ lớn), xác suất thực nghiệm tiến sát xác suất lý thuyết 25%."
            if is_eq else
            f"CỠ MẪU QUÁ NHỎ: N = {n_trials} lượt chưa đủ để triệt tiêu sai số ngẫu nhiên! Hãy tăng số lượt quay N lên trên 100!"
        )
        proof = f"BẤT BIẾN: Vòng quay chia đều 8 ô bằng nhau, có đúng 2 ô trúng thưởng (P_lý_thuyết = 2/8 = 25%)."

        return CausalBalanceResult(
            tilt_angle_deg=tilt,
            left_weight=round(p_emp * 100, 1),
            right_weight=round(p_true * 100, 1),
            imbalance_delta=round(abs(diff) * 100, 1),
            is_equilibrium=is_eq,
            torque_direction=direction,
            cause_action_text=cause_text,
            physical_consequence_text=phys_text,
            socratic_reasoning_text=soc_text,
            hypothesis_locked_proof=proof,
        )

    def evaluate(self, asset_id: str, action_value: float) -> CausalBalanceResult:
        """Thực thi đánh giá nhân - quả cho một Living Asset với giá trị hành động cụ thể."""
        sys_config = self._registry.get(asset_id)
        if not sys_config:
            # Fallback mặc định
            return self._eval_transport_convoy(action_value, 60, 3, 1.0)
        return sys_config["eval_fn"](action_value)

    def get_system_config(self, asset_id: str) -> Optional[Dict[str, Any]]:
        return self._registry.get(asset_id)
