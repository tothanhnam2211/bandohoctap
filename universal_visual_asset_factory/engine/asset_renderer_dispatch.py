# -*- coding: utf-8 -*-
"""
ASSET RENDERER DISPATCHER
Điều phối từ generator_type và bộ tham số variant sang đúng hàm vẽ vector SVG.
Bảo đảm tính chuẩn xác toán học, thẩm mỹ phân tầng (Art + Math), và chế độ Dual (Thầy vs Trò).
Tự động làm sạch và escape ký tự đặc biệt XML (&, <, >, ") để bảo đảm SVG luôn chuẩn 100%.
"""

import math
from typing import Dict, Any, Optional

from engine.core_math_primitives import (
    render_polygon_geometry,
    render_circle_geometry,
    render_coordinate_plot_2d,
    render_solid_geometry,
    render_statistics_chart,
    render_stem_balance_scale,
)
from engine.specialized_primitives import (
    render_number_line,
    render_venn_diagram,
    render_fraction_model,
    render_factor_tree,
    render_unit_circle,
    render_bar_chart,
)

def _sanitize_xml(obj: Any) -> Any:
    """Đệ quy làm sạch chuỗi để bảo đảm hợp lệ XML/SVG"""
    if isinstance(obj, str):
        return (
            obj.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )
    elif isinstance(obj, dict):
        return {k: _sanitize_xml(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_sanitize_xml(x) for x in obj]
    elif isinstance(obj, tuple):
        return tuple(_sanitize_xml(x) for x in obj)
    return obj

def dispatch_render_svg(
    generator_type: str,
    params: Dict[str, Any],
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 380,
) -> str:
    """
    Nhận generator_type và params, trả về chuỗi vector SVG hoàn chỉnh.
    """
    # Tự động sanitize title và params để chống lỗi parser XML
    title = _sanitize_xml(title)
    params = _sanitize_xml(params)

    gtype = generator_type.lower()

    # 1. TRỤC SỐ & KHOẢNG ĐOẠN TẬP HỢP
    if gtype in ("number_line_nat", "number_line_int", "number_line_rational", 
                 "algebra_ineq_numberline", "alg_intervals_real", "vertical_integer_scale"):
        x_range = params.get("x_range", (-5, 5))
        step = params.get("step", 1.0)
        highlight_points = params.get("highlight_points", None)
        intervals = params.get("intervals", None)
        return render_number_line(
            x_range=x_range,
            step=step,
            highlight_points=highlight_points,
            intervals=intervals,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=260 if height > 260 else height,
        )

    # 2. TẬP HỢP VENN & XÁC SUẤT ĐIỀU KIỆN
    elif gtype in ("set_venn", "stat_bayes_theorem_venn", "stat_indep_venn_tree"):
        set_a = params.get("set_a_elements", ["2", "4", "6", "8"])
        set_b = params.get("set_b_elements", ["3", "6", "9", "12"])
        inter = params.get("intersection_elements", ["6"])
        label_a = params.get("label_a", "Tập A")
        label_b = params.get("label_b", "Tập B")
        return render_venn_diagram(
            set_a_elements=set_a,
            set_b_elements=set_b,
            intersection_elements=inter,
            label_a=label_a,
            label_b=label_b,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 3. MÔ HÌNH PHÂN SỐ, TỶ LỆ & PHẦN TRĂM
    elif gtype in ("fraction_pie", "fraction_tape", "fraction_grid_equiv", "percentage_100_grid", "decimal_blocks"):
        mtype = "pie" if "pie" in gtype else ("grid_100" if "percentage" in gtype or "grid" in gtype else "tape")
        num = params.get("numerator", 3)
        den = params.get("denominator", 4)
        return render_fraction_model(
            model_type=mtype,
            numerator=num,
            denominator=den,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 4. CÂY THỪA SỐ & DÃY SỐ
    elif gtype in ("prime_factor_tree", "gcd_lcm_grid", "math_power_tree", "alg_pascal_triangle"):
        root_val = params.get("root_value", 36)
        branches = params.get("branches", [{"left": 2, "right": 18}])
        return render_factor_tree(
            root_value=root_val,
            branches=branches,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 5. ĐƯỜNG TRÒN LƯỢNG GIÁC
    elif gtype in ("trig_unit_circle",):
        deg = params.get("angle_deg", 45)
        show_sc = params.get("show_sin_cos", True)
        return render_unit_circle(
            angle_deg=deg,
            show_sin_cos=show_sc,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 6. BIỂU ĐỒ CỘT & THỐNG KÊ RỜI RẠC
    elif gtype in ("stat_bar_chart", "stat_double_bar", "stat_pictograph", "stat_tally_chart"):
        cats = params.get("categories", ["Lớp A", "Lớp B", "Lớp C", "Lớp D"])
        vals = params.get("values", [35, 42, 28, 50])
        y_lbl = params.get("y_label", "Số học sinh")
        return render_bar_chart(
            categories=cats,
            values=vals,
            y_label=y_lbl,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 7. THỐNG KÊ HỘP & SƠ ĐỒ CÂY XÁC SUẤT
    elif gtype in ("stat_box_plot", "stat_grouped_median_ogive", "stat_variance_std_bell"):
        return render_statistics_chart(
            chart_type="box_plot",
            data=params,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )
    elif gtype in ("stat_tree_diagram", "stat_bayes_tree", "prob_dice_coin", "prob_spinner", "stat_probability_gauge"):
        return render_statistics_chart(
            chart_type="tree_diagram",
            data=params,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 8. STEM & CÁN CÂN THĂNG BẰNG
    elif gtype in ("algebra_linear_balance", "stem_lever_torque", "stem_mixing_ratio", "stem_motion_meeting", "stem_piggy_budget", "stem_gears_ratio"):
        tilt = params.get("tilt_angle_deg", 0.0)
        lw = params.get("left_weight_val", 50.0)
        rw = params.get("right_weight_val", 50.0)
        llbl = params.get("left_label", "2x + 10")
        rlbl = params.get("right_label", "50")
        return render_stem_balance_scale(
            tilt_angle_deg=tilt,
            left_weight_val=lw,
            right_weight_val=rw,
            left_label=llbl,
            right_label=rlbl,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 9. HÌNH HỌC ĐƯỜNG TRÒN
    elif gtype in ("geom_circle_analytic", "geom_inscribed_central", "geom_circle_tangent", 
                   "geom_two_tangents_meet", "geom_cyclic_quad"):
        rad = params.get("radius", 110)
        center = params.get("center", (width / 2, height / 2 + 10))
        chords = params.get("chords", None)
        tangents = params.get("tangents", None)
        triangles = params.get("inscribed_triangles", [(60, 180, 310)])
        return render_circle_geometry(
            radius=rad,
            center=center,
            chords=chords,
            tangents=tangents,
            inscribed_triangles=triangles,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 10. HÌNH KHÔNG GIAN 3D & OXYZ
    elif gtype in ("geom_solid_prism_quad", "geom_solid_prism_tri", "geom_solid_cylinder", 
                   "geom_solid_cone", "geom_solid_sphere", "geom_solid_net_unfold",
                   "geom_pyramid_quad", "geom_pyramid_tri", "geom3d_pyramid_cross_section",
                   "geom3d_line_parallel_plane", "geom3d_line_perp_plane", "geom3d_two_perp_planes",
                   "geom3d_parallel_planes", "geom3d_dist_point_plane", "geom3d_dihedral_angle",
                   "geom3d_skew_lines_dist", "geom_oxyz_axes_point", "geom_oxyz_cross_product",
                   "geom_oxyz_plane", "geom_oxyz_line_space", "geom_oxyz_rel_lines",
                   "geom_oxyz_sphere_plane", "stem_radar_airspace_3d", "calc_revolution_solid_3d"):
        stype = "oxyz_frame" if "oxyz" in gtype or "radar" in gtype else (
            "cylinder" if "cylinder" in gtype else (
                "cone" if "cone" in gtype else "pyramid_quad"
            )
        )
        return render_solid_geometry(
            solid_type=stype,
            params=params,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 11. HỆ TỌA ĐỘ 2D & ĐỒ THỊ GIẢI TÍCH
    elif gtype in ("algebra_direct_inverse_plot", "algebra_linear_slope_intercept", "algebra_lines_rel_pos",
                   "algebra_parabola_basic", "algebra_parabola_line", "algebra_quad_delta", "algebra_sys2_geo",
                   "algebra_viete_geom", "alg_quad_full_study", "alg_half_plane_ineq", "alg_linprog_polygon",
                   "geom_conic_ellipse", "geom_conic_hyperbola", "geom_conic_parabola", "trig_sine_graph",
                   "trig_cos_tan_graph", "alg_exp_log_graphs", "calc_secant_to_tangent", "calc_cubic_6shapes",
                   "calc_quartic_shapes", "calc_homographic_asymptotes", "calc_oblique_asymptote",
                   "calc_integral_shaded_area", "calc_continuity_ivt", "calc_limit_seq",
                   "stem_parabolic_arch", "stem_parabolic_dish", "stem_projectile_parabola",
                   "stem_half_life_decay", "stem_tank_flow_harmonic", "stem_logistic_growth"):
        curves = params.get("curves", [
            {"type": "parabola", "func": lambda x: 0.5 * (x - 1)**2 - 2, "name": "y = 0.5(x-1)² - 2"}
        ])
        xlim = params.get("xlim", (-5, 5))
        ylim = params.get("ylim", (-4, 6))
        key_points = params.get("key_points", None)
        shaded = params.get("shaded_region", None)
        asymptotes = params.get("asymptotes", None)
        return render_coordinate_plot_2d(
            curves=curves,
            xlim=xlim,
            ylim=ylim,
            key_points=key_points,
            shaded_region=shaded,
            asymptotes=asymptotes,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )

    # 12. HÌNH HỌC PHẲNG CÒN LẠI (TAM GIÁC, TỨ GIÁC, ĐỊNH LÝ HÌNH HỌC)
    else:
        # Default fallback to polygon geometry
        verts = params.get("vertices", [
            (width / 2 - 120, height / 2 + 70),
            (width / 2 + 130, height / 2 + 70),
            (width / 2, height / 2 - 80),
        ])
        lbls = params.get("labels", ["A", "B", "C"])
        side_lbls = params.get("side_labels", None)
        right_ang = params.get("right_angles", None)
        angle_arcs = params.get("angle_arcs", None)
        aux_seg = params.get("auxiliary_segments", None)
        shaded = params.get("shaded_subpolygon", None)
        return render_polygon_geometry(
            vertices=verts,
            labels=lbls,
            side_labels=side_lbls,
            right_angles=right_ang,
            angle_arcs=angle_arcs,
            auxiliary_segments=aux_seg,
            shaded_subpolygon=shaded,
            title=title,
            style=style,
            is_student_worksheet=is_student_worksheet,
            width=width,
            height=height,
        )
