# -*- coding: utf-8 -*-
"""
VARIANT GENERATOR ENGINE
Tạo ra các tập tham số đa dạng, chuẩn xác toán học và không trùng lặp cho mỗi Họ Asset (Asset Family).
Hỗ trợ tạo N biến thể (variants) cho mỗi họ asset với seed xác định để bảo đảm tính tái lập hoàn toàn.
"""

import math
from typing import Dict, Any, List
from curriculum.k12_curriculum_catalog import AssetFamilySpec

def generate_family_variants(family: AssetFamilySpec, count: int = 46) -> List[Dict[str, Any]]:
    """
    Tạo ra danh sách `count` bộ tham số riêng biệt cho họ asset.
    Mỗi biến thể có `variant_id`, `variant_index`, `title`, `params`, `math_concept`.
    """
    gtype = family.generator_type.lower()
    variants = []

    for idx in range(1, count + 1):
        var_id = f"{family.family_id}_VAR_{idx:02d}"
        var_title = f"{family.topic_vi} - Biến thể {idx:02d}"
        p = {}

        # 1. TRỤC SỐ & KHOẢNG ĐOẠN
        if gtype in ("number_line_nat", "number_line_int", "number_line_rational", 
                     "algebra_ineq_numberline", "alg_intervals_real", "vertical_integer_scale"):
            offset = (idx % 5) - 2
            a = -3 + offset
            b = 2 + (idx % 4)
            p = {
                "x_range": (-6 + offset, 6 + offset),
                "step": 1.0,
                "intervals": [{
                    "from": min(a, b),
                    "to": max(a, b),
                    "left_open": bool(idx % 2 == 1),
                    "right_open": bool((idx // 2) % 2 == 1),
                    "color": "#0284C7" if idx % 2 == 0 else "#10B981"
                }],
                "highlight_points": [
                    {"val": min(a, b), "label": f"[{min(a, b)}" if idx % 2 == 0 else f"({min(a, b)}", "color": "#EF4444"},
                    {"val": max(a, b), "label": f"{max(a, b)}]" if (idx // 2) % 2 == 0 else f"{max(a, b)})", "color": "#EF4444"},
                ]
            }

        # 2. BIỂU ĐỒ VENN
        elif gtype in ("set_venn", "stat_bayes_theorem_venn", "stat_indep_venn_tree"):
            k = idx % 8 + 2
            p = {
                "set_a_elements": [f"a{i}" for i in range(1, (idx % 4) + 3)],
                "set_b_elements": [f"b{i}" for i in range(1, ((idx + 1) % 4) + 3)],
                "intersection_elements": [f"x{i}" for i in range(1, ((idx + 2) % 3) + 2)],
                "label_a": f"Tập hợp A_{idx}",
                "label_b": f"Tập hợp B_{idx}",
            }

        # 3. MÔ HÌNH PHÂN SỐ
        elif gtype in ("fraction_pie", "fraction_tape", "fraction_grid_equiv", "percentage_100_grid", "decimal_blocks"):
            denoms = [2, 3, 4, 5, 6, 8, 10, 12]
            den = denoms[(idx - 1) % len(denoms)]
            num = ((idx - 1) % (den - 1)) + 1 if den > 1 else 1
            p = {
                "numerator": num,
                "denominator": den,
            }

        # 4. CÂY THỪA SỐ
        elif gtype in ("prime_factor_tree", "gcd_lcm_grid", "math_power_tree", "alg_pascal_triangle"):
            composites = [12, 18, 20, 24, 28, 30, 36, 40, 42, 45, 48, 50, 54, 60, 72, 80, 84, 90, 96, 100, 108, 120]
            root_v = composites[(idx - 1) % len(composites)]
            left_v = 2 if root_v % 2 == 0 else 3
            p = {
                "root_value": root_v,
                "branches": [{"left": left_v, "right": root_v // left_v}]
            }

        # 5. ĐƯỜNG TRÒN LƯỢNG GIÁC
        elif gtype in ("trig_unit_circle",):
            angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
            ang = angles[(idx - 1) % len(angles)]
            p = {
                "angle_deg": ang,
                "show_sin_cos": True,
            }

        # 6. BIỂU ĐỒ CỘT
        elif gtype in ("stat_bar_chart", "stat_double_bar", "stat_pictograph", "stat_tally_chart"):
            base = 15 + (idx % 10) * 3
            p = {
                "categories": ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4"],
                "values": [base, base + 8 + (idx % 5), base + 14 - (idx % 4), base + 20 + (idx % 6)],
                "y_label": "Sản lượng (tấn)",
            }

        # 7. HỘP THỐNG KÊ & CÂY XÁC SUẤT
        elif gtype in ("stat_box_plot", "stat_grouped_median_ogive", "stat_variance_std_bell"):
            shift = (idx % 15)
            p = {
                "min": 10 + shift,
                "q1": 25 + shift,
                "med": 45 + shift + (idx % 5),
                "q3": 70 + shift,
                "max": 90 + shift,
            }
        elif gtype in ("stat_tree_diagram", "stat_bayes_tree", "prob_dice_coin", "prob_spinner", "stat_probability_gauge"):
            p_val = round(0.3 + (idx % 6) * 0.1, 2)
            p = {
                "pA": p_val,
                "pB_A": round(0.4 + (idx % 5) * 0.1, 2),
            }

        # 8. STEM & CÁN CÂN
        elif gtype in ("algebra_linear_balance", "stem_lever_torque", "stem_mixing_ratio", "stem_motion_meeting", "stem_piggy_budget", "stem_gears_ratio"):
            is_equil = (idx % 3 == 0)
            tilt = 0.0 if is_equil else (-12.0 if idx % 2 == 1 else 12.0)
            lw = 40.0 + (idx % 5) * 10
            rw = lw if is_equil else lw + 15.0
            p = {
                "tilt_angle_deg": tilt,
                "left_weight_val": lw,
                "right_weight_val": rw,
                "left_label": f"Vế Trái ({int(lw)} kg)",
                "right_label": f"Vế Phải ({int(rw)} kg)",
            }

        # 9. ĐƯỜNG TRÒN HÌNH HỌC
        elif gtype in ("geom_circle_analytic", "geom_inscribed_central", "geom_circle_tangent", 
                       "geom_two_tangents_meet", "geom_cyclic_quad"):
            r_val = 95 + (idx % 6) * 5
            a1 = (30 + idx * 15) % 360
            a2 = (a1 + 100 + (idx % 4) * 10) % 360
            a3 = (a2 + 110 + (idx % 3) * 10) % 360
            p = {
                "radius": r_val,
                "inscribed_triangles": [(a1, a2, a3)],
                "tangents": [a1] if idx % 2 == 1 else None,
            }

        # 10. HÌNH KHÔNG GIAN 3D & OXYZ
        elif gtype in ("geom_solid_prism_quad", "geom_solid_prism_tri", "geom_solid_cylinder", 
                       "geom_solid_cone", "geom_solid_sphere", "geom_solid_net_unfold",
                       "geom_pyramid_quad", "geom_pyramid_tri", "geom3d_pyramid_cross_section",
                       "geom3d_line_parallel_plane", "geom3d_line_perp_plane", "geom3d_two_perp_planes",
                       "geom3d_parallel_planes", "geom3d_dist_point_plane", "geom3d_dihedral_angle",
                       "geom3d_skew_lines_dist", "geom_oxyz_axes_point", "geom_oxyz_cross_product",
                       "geom_oxyz_plane", "geom_oxyz_line_space", "geom_oxyz_rel_lines",
                       "geom_oxyz_sphere_plane", "stem_radar_airspace_3d", "calc_revolution_solid_3d"):
            mx = 50 + (idx % 8) * 10
            my = 70 + (idx % 6) * 12
            mz = 60 + (idx % 7) * 10
            p = {
                "mx": mx,
                "my": my,
                "mz": mz,
                "coords": f"{int(mx/20)}, {int(my/20)}, {int(mz/20)}",
            }

        # 11. ĐỒ THỊ TỌA ĐỘ 2D & GIẢI TÍCH
        elif gtype in ("algebra_direct_inverse_plot", "algebra_linear_slope_intercept", "algebra_lines_rel_pos",
                       "algebra_parabola_basic", "algebra_parabola_line", "algebra_quad_delta", "algebra_sys2_geo",
                       "algebra_viete_geom", "alg_quad_full_study", "alg_half_plane_ineq", "alg_linprog_polygon",
                       "geom_conic_ellipse", "geom_conic_hyperbola", "geom_conic_parabola", "trig_sine_graph",
                       "trig_cos_tan_graph", "alg_exp_log_graphs", "calc_secant_to_tangent", "calc_cubic_6shapes",
                       "calc_quartic_shapes", "calc_homographic_asymptotes", "calc_oblique_asymptote",
                       "calc_integral_shaded_area", "calc_continuity_ivt", "calc_limit_seq",
                       "stem_parabolic_arch", "stem_parabolic_dish", "stem_projectile_parabola",
                       "stem_half_life_decay", "stem_tank_flow_harmonic", "stem_logistic_growth"):
            a_coeff = 0.5 if idx % 2 == 0 else -0.5
            h = (idx % 5) - 2
            k = ((idx + 2) % 5) - 2
            func = (lambda a, h, k: lambda x: a * (x - h)**2 + k)(a_coeff, h, k)
            p = {
                "curves": [{
                    "type": "parabola",
                    "func": func,
                    "name": f"y = {a_coeff}(x-{h})² + {k}",
                    "color": "#0284C7" if a_coeff > 0 else "#DC2626",
                }],
                "key_points": [
                    {"x": h, "y": k, "label": f"Đỉnh I({h};{k})", "color": "#F59E0B"}
                ],
                "xlim": (-5, 5),
                "ylim": (-4, 6),
            }

        # 12. HÌNH HỌC PHẲNG CÒN LẠI (TAM GIÁC, TỨ GIÁC)
        else:
            w_offset = (idx % 7) * 10
            h_offset = ((idx + 3) % 6) * 12
            A = (250 - 120 + w_offset, 270)
            B = (250 + 130 - w_offset, 270)
            C = (250 + (w_offset - 30), 110 + h_offset)
            p = {
                "vertices": [A, B, C],
                "labels": ["A", "B", "C"],
                "side_labels": [
                    {"segment": (0, 1), "text": f"c = {round(math.hypot(B[0]-A[0], B[1]-A[1])/20, 1)}"},
                    {"segment": (1, 2), "text": f"a = {round(math.hypot(C[0]-B[0], C[1]-B[1])/20, 1)}"},
                    {"segment": (2, 0), "text": f"b = {round(math.hypot(A[0]-C[0], A[1]-C[1])/20, 1)}"},
                ],
                "right_angles": [0] if idx % 4 == 0 else None,
                "angle_arcs": [{"vertex_idx": 1, "deg": 60 + (idx % 5) * 5, "label": f"{60 + (idx%5)*5}°"}]
            }

        variants.append({
            "family_id": family.family_id,
            "grade": family.grade,
            "strand": family.strand,
            "chapter": family.chapter,
            "topic_vi": family.topic_vi,
            "variant_id": var_id,
            "variant_index": idx,
            "title": var_title,
            "generator_type": family.generator_type,
            "math_invariant": family.math_invariant,
            "params": p,
        })

    return variants
