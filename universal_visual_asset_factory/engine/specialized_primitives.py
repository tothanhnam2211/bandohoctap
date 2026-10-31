# -*- coding: utf-8 -*-
"""
SPECIALIZED MATHEMATICAL VECTOR PRIMITIVES
Bổ sung các renderer chuyên biệt cho K12:
- Trục số & Đoạn/Khoảng tập hợp R (Number Lines & Real Intervals)
- Biểu đồ Venn & Xác suất hợp/giao (Venn Diagrams)
- Mô hình Phân số & Tỷ số phần trăm (Fraction Pies, Tapes, Grids)
- Cây phân tích thừa số nguyên tố & Dãy số (Factor Trees & Sequences)
- Đường tròn lượng giác & Góc radian/độ (Unit Circle & Trigonometry)
- Biểu đồ cột & Hình quạt tròn thống kê (Bar Charts & Pie Slices)
"""

import math
from typing import Dict, Any, List, Tuple, Optional

# ==========================================
# 1. TRỤC SỐ (TỰ NHIÊN, NGUYÊN, HỮU TỈ, TẬP NGHIỆM BẤT PHƯƠNG TRÌNH, KHOẢNG ĐOẠN R)
# ==========================================

def render_number_line(
    x_range: Tuple[float, float] = (-5, 5),
    step: float = 1.0,
    highlight_points: Optional[List[Dict[str, Any]]] = None, # [{"val": 2, "label": "A(2)", "color": "#0284C7"}]
    intervals: Optional[List[Dict[str, Any]]] = None, # [{"from": -2, "to": 3, "left_open": True, "right_open": False, "color": "#10B981"}]
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 240,
) -> str:
    style = style or {}
    bg = style.get("bg_panel", "#FFFFFF")
    ink = style.get("ink_primary", "#0F172A")
    brand = style.get("brand", "#0284C7")
    accent = style.get("accent", "#EF4444")
    border = style.get("border_color", "#CBD5E1")

    pad_x = 45
    axis_y = height / 2 + 15
    scale_x = lambda v: pad_x + (v - x_range[0]) / (x_range[1] - x_range[0]) * (width - 2 * pad_x)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
    ]

    # Interval highlights / shadings
    if intervals:
        for itv in intervals:
            x1 = scale_x(itv.get("from", x_range[0]))
            x2 = scale_x(itv.get("to", x_range[1]))
            color = itv.get("color", brand)
            svg.append(f'<rect x="{min(x1, x2)}" y="{axis_y-14}" width="{abs(x2-x1)}" height="28" fill="{color}" fill-opacity="0.25" rx="4"/>')

    svg.append('</g><g id="math-layer">')

    # Main horizontal axis with arrow
    svg.append(f'<line x1="{pad_x-15}" y1="{axis_y}" x2="{width-pad_x+15}" y2="{axis_y}" stroke="{ink}" stroke-width="2"/>')
    svg.append(f'<polygon points="{width-pad_x+20},{axis_y} {width-pad_x+10},{axis_y-4} {width-pad_x+10},{axis_y+4}" fill="{ink}"/>')
    svg.append(f'<text x="{width-pad_x+24}" y="{axis_y+4}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">x</text>')

    # Axis ticks and numbers
    cur = x_range[0]
    while cur <= x_range[1] + 1e-6:
        tx = scale_x(cur)
        svg.append(f'<line x1="{tx}" y1="{axis_y-5}" x2="{tx}" y2="{axis_y+5}" stroke="{ink}" stroke-width="1.4"/>')
        val_str = str(int(cur)) if abs(cur - round(cur)) < 1e-4 else f"{cur:.1f}"
        svg.append(f'<text x="{tx}" y="{axis_y+20}" font-family="Segoe UI, Arial" font-size="10.5" font-weight="600" fill="#334155" text-anchor="middle">{val_str}</text>')
        cur += step

    # Intervals brackets [ , )
    if intervals:
        for itv in intervals:
            f_val = itv.get("from", None)
            t_val = itv.get("to", None)
            c = itv.get("color", brand)
            if f_val is not None and f_val >= x_range[0]:
                fx = scale_x(f_val)
                bracket = "(" if itv.get("left_open", False) else "["
                svg.append(f'<text x="{fx}" y="{axis_y+5}" font-family="Segoe UI, Arial" font-size="19" font-weight="800" fill="{c}" text-anchor="middle">{bracket}</text>')
            if t_val is not None and t_val <= x_range[1]:
                tx = scale_x(t_val)
                bracket = ")" if itv.get("right_open", False) else "]"
                svg.append(f'<text x="{tx}" y="{axis_y+5}" font-family="Segoe UI, Arial" font-size="19" font-weight="800" fill="{c}" text-anchor="middle">{bracket}</text>')

    # Highlight points
    if highlight_points:
        for pt in highlight_points:
            px = scale_x(pt["val"])
            c = pt.get("color", accent)
            svg.append(f'<circle cx="{px}" cy="{axis_y}" r="4.5" fill="{c}"/>')
            lbl = "?" if is_student_worksheet and pt.get("hide_in_worksheet") else pt.get("label", "")
            if lbl:
                svg.append(f'<text x="{px}" y="{axis_y-12}" font-family="Segoe UI, Arial" font-size="11.5" font-weight="800" fill="{c}" text-anchor="middle">{lbl}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 2. BIỂU ĐỒ VENN (TẬP HỢP, HỢP, GIAO, HIỆU, XÁC SUẤT ĐIỀU KIỆN)
# ==========================================

def render_venn_diagram(
    set_a_elements: List[str],
    set_b_elements: List[str],
    intersection_elements: List[str],
    label_a: str = "Tập A",
    label_b: str = "Tập B",
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 320,
) -> str:
    style = style or {}
    bg = style.get("bg_panel", "#FFFFFF")
    ink = style.get("ink_primary", "#0F172A")
    brand = style.get("brand", "#0284C7")
    accent = style.get("accent", "#8B5CF6")
    border = style.get("border_color", "#CBD5E1")

    r = 95
    c1 = (width / 2 - 60, height / 2 + 10)
    c2 = (width / 2 + 60, height / 2 + 10)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
        # Set A circle filled
        f'<circle cx="{c1[0]}" cy="{c1[1]}" r="{r}" fill="{brand}" fill-opacity="0.14"/>',
        # Set B circle filled
        f'<circle cx="{c2[0]}" cy="{c2[1]}" r="{r}" fill="{accent}" fill-opacity="0.14"/>',
        '</g><g id="math-layer">',
        f'<circle cx="{c1[0]}" cy="{c1[1]}" r="{r}" fill="none" stroke="{brand}" stroke-width="2.2"/>',
        f'<circle cx="{c2[0]}" cy="{c2[1]}" r="{r}" fill="none" stroke="{accent}" stroke-width="2.2"/>',
        # Labels A and B
        f'<text x="{c1[0]-50}" y="{c1[1]-r-8}" font-family="Segoe UI, Arial" font-size="13" font-weight="800" fill="{brand}">{label_a}</text>',
        f'<text x="{c2[0]+50}" y="{c2[1]-r-8}" font-family="Segoe UI, Arial" font-size="13" font-weight="800" fill="{accent}" text-anchor="end">{label_b}</text>',
    ]

    # Elements inside A only
    for i, el in enumerate(set_a_elements[:5]):
        ey = c1[1] - 30 + i * 20
        txt = "?" if is_student_worksheet and i == 0 else el
        svg.append(f'<text x="{c1[0]-40}" y="{ey}" font-family="Segoe UI, Arial" font-size="11.5" font-weight="600" fill="{ink}">{txt}</text>')

    # Elements inside intersection
    for i, el in enumerate(intersection_elements[:4]):
        ey = c1[1] - 25 + i * 22
        txt = "?" if is_student_worksheet and i == 0 else el
        svg.append(f'<text x="{width/2}" y="{ey}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="#0369A1" text-anchor="middle">{txt}</text>')

    # Elements inside B only
    for i, el in enumerate(set_b_elements[:5]):
        ey = c2[1] - 30 + i * 20
        txt = "?" if is_student_worksheet and i == 0 else el
        svg.append(f'<text x="{c2[0]+35}" y="{ey}" font-family="Segoe UI, Arial" font-size="11.5" font-weight="600" fill="{ink}">{txt}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 3. MÔ HÌNH PHÂN SỐ & PHẦN TRĂM (PIE, TAPE, 100-GRID)
# ==========================================

def render_fraction_model(
    model_type: str, # "pie", "tape", "grid_100"
    numerator: int,
    denominator: int,
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 320,
) -> str:
    style = style or {}
    bg = style.get("bg_panel", "#FFFFFF")
    ink = style.get("ink_primary", "#0F172A")
    brand = style.get("brand", "#0284C7")
    accent = style.get("accent", "#10B981")
    border = style.get("border_color", "#CBD5E1")

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="math-layer">',
    ]

    if model_type == "pie":
        cx, cy, r = width / 2, height / 2 + 10, 100
        # Draw denominator sectors
        for i in range(denominator):
            a1 = (i / denominator) * 2 * math.pi - math.pi / 2
            a2 = ((i + 1) / denominator) * 2 * math.pi - math.pi / 2
            x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
            x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
            is_shaded = i < numerator
            fill_c = brand if is_shaded else "#F8FAFC"
            fill_op = "0.75" if is_shaded else "1.0"
            large_arc = 1 if (a2 - a1) > math.pi else 0
            path_d = f"M {cx} {cy} L {x1} {y1} A {r} {r} 0 {large_arc} 1 {x2} {y2} Z"
            svg.append(f'<path d="{path_d}" fill="{fill_c}" fill-opacity="{fill_op}" stroke="{ink}" stroke-width="1.8"/>')

        # Fraction Badge
        lbl = f"? / {denominator}" if is_student_worksheet else f"{numerator} / {denominator}"
        svg.append(f'<rect x="{width-130}" y="{cy-22}" width="110" height="44" fill="#F1F5F9" rx="6" stroke="{brand}" stroke-width="1.5"/>')
        svg.append(f'<text x="{width-75}" y="{cy+6}" font-family="Segoe UI, Arial" font-size="16" font-weight="800" fill="{brand}" text-anchor="middle">{lbl}</text>')

    elif model_type == "tape":
        # Fraction Bar / Tape diagram
        tx, ty = 50, height / 2 - 30
        tw, th = 400, 60
        seg_w = tw / denominator
        for i in range(denominator):
            sx = tx + i * seg_w
            is_shaded = i < numerator
            fill_c = brand if is_shaded else "#F8FAFC"
            fill_op = "0.6" if is_shaded else "1.0"
            svg.append(f'<rect x="{sx}" y="{ty}" width="{seg_w}" height="{th}" fill="{fill_c}" fill-opacity="{fill_op}" stroke="{ink}" stroke-width="1.8"/>')
            svg.append(f'<text x="{sx + seg_w/2}" y="{ty + th/2 + 5}" font-family="Segoe UI, Arial" font-size="11" font-weight="700" fill="{ink}" text-anchor="middle">1/{denominator}</text>')

        lbl = f"? / {denominator}" if is_student_worksheet else f"Tô màu: {numerator}/{denominator} phần"
        svg.append(f'<text x="{width/2}" y="{ty + th + 35}" font-family="Segoe UI, Arial" font-size="13" font-weight="800" fill="{brand}" text-anchor="middle">{lbl}</text>')

    elif model_type == "grid_100":
        # 10x10 Percentage Square Grid
        gx, gy = width / 2 - 100, height / 2 - 95
        cell_size = 20
        shaded_count = min(100, int((numerator / max(1, denominator)) * 100))
        for r_idx in range(10):
            for c_idx in range(10):
                cell_num = r_idx * 10 + c_idx
                is_shaded = cell_num < shaded_count
                fill_c = accent if is_shaded else "#FFFFFF"
                fill_op = "0.8" if is_shaded else "1.0"
                svg.append(f'<rect x="{gx + c_idx*cell_size}" y="{gy + r_idx*cell_size}" width="{cell_size}" height="{cell_size}" fill="{fill_c}" fill-opacity="{fill_op}" stroke="#CBD5E1" stroke-width="1"/>')
        svg.append(f'<rect x="{gx}" y="{gy}" width="200" height="200" fill="none" stroke="{ink}" stroke-width="2"/>')
        pct_lbl = "? %" if is_student_worksheet else f"{shaded_count}% ({shaded_count}/100)"
        svg.append(f'<text x="{gx + 250}" y="{height/2+5}" font-family="Segoe UI, Arial" font-size="14" font-weight="800" fill="{accent}">{pct_lbl}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 4. CÂY THỪA SỐ NGUYÊN TỐ & DÃY SỐ (PRIME TREE & SEQUENCES)
# ==========================================

def render_factor_tree(
    root_value: int,
    branches: List[Dict[str, Any]], # [{"val": 12, "left": 2, "right": 6, ...}]
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 340,
) -> str:
    style = style or {}
    bg = style.get("bg_panel", "#FFFFFF")
    ink = style.get("ink_primary", "#0F172A")
    brand = style.get("brand", "#0284C7")
    accent = style.get("accent", "#10B981")
    border = style.get("border_color", "#CBD5E1")

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="math-layer">',
    ]

    # Level 1 Root
    r_pt = (width / 2, 60)
    svg.append(f'<circle cx="{r_pt[0]}" cy="{r_pt[1]}" r="22" fill="#F8FAFC" stroke="{brand}" stroke-width="2.5"/>')
    svg.append(f'<text x="{r_pt[0]}" y="{r_pt[1]+6}" font-family="Segoe UI, Arial" font-size="15" font-weight="800" fill="{brand}" text-anchor="middle">{root_value}</text>')

    # Level 2 Branching
    l2_left = (width / 2 - 80, 150)
    l2_right = (width / 2 + 80, 150)
    svg.append(f'<line x1="{r_pt[0]}" y1="{r_pt[1]+22}" x2="{l2_left[0]}" y2="{l2_left[1]-20}" stroke="{ink}" stroke-width="2"/>')
    svg.append(f'<line x1="{r_pt[0]}" y1="{r_pt[1]+22}" x2="{l2_right[0]}" y2="{l2_right[1]-20}" stroke="{ink}" stroke-width="2"/>')

    val_l2_left = branches[0].get("left", 2) if branches else 2
    val_l2_right = branches[0].get("right", root_value // val_l2_left) if branches else root_value // 2

    txt_l2 = "?" if is_student_worksheet else str(val_l2_left)
    svg.append(f'<circle cx="{l2_left[0]}" cy="{l2_left[1]}" r="20" fill="#ECFDF5" stroke="{accent}" stroke-width="2.2"/>')
    svg.append(f'<text x="{l2_left[0]}" y="{l2_left[1]+5}" font-family="Segoe UI, Arial" font-size="14" font-weight="800" fill="{accent}" text-anchor="middle">{txt_l2}</text>')

    svg.append(f'<circle cx="{l2_right[0]}" cy="{l2_right[1]}" r="20" fill="#F8FAFC" stroke="{brand}" stroke-width="2.2"/>')
    svg.append(f'<text x="{l2_right[0]}" y="{l2_right[1]+5}" font-family="Segoe UI, Arial" font-size="14" font-weight="800" fill="{brand}" text-anchor="middle">{val_l2_right}</text>')

    # Level 3 Branching from right node
    l3_left = (l2_right[0] - 50, 240)
    l3_right = (l2_right[0] + 50, 240)
    svg.append(f'<line x1="{l2_right[0]}" y1="{l2_right[1]+20}" x2="{l3_left[0]}" y2="{l3_left[1]-20}" stroke="{ink}" stroke-width="2"/>')
    svg.append(f'<line x1="{l2_right[0]}" y1="{l2_right[1]+20}" x2="{l3_right[0]}" y2="{l3_right[1]-20}" stroke="{ink}" stroke-width="2"/>')

    val_l3_left = 2 if val_l2_right % 2 == 0 else 3
    val_l3_right = val_l2_right // val_l3_left

    txt_l3 = "?" if is_student_worksheet else str(val_l3_left)
    svg.append(f'<circle cx="{l3_left[0]}" cy="{l3_left[1]}" r="18" fill="#ECFDF5" stroke="{accent}" stroke-width="2"/>')
    svg.append(f'<text x="{l3_left[0]}" y="{l3_left[1]+5}" font-family="Segoe UI, Arial" font-size="13" font-weight="800" fill="{accent}" text-anchor="middle">{txt_l3}</text>')

    svg.append(f'<circle cx="{l3_right[0]}" cy="{l3_right[1]}" r="18" fill="#ECFDF5" stroke="{accent}" stroke-width="2"/>')
    svg.append(f'<text x="{l3_right[0]}" y="{l3_right[1]+5}" font-family="Segoe UI, Arial" font-size="13" font-weight="800" fill="{accent}" text-anchor="middle">{val_l3_right}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 5. ĐƯỜNG TRÒN LƯỢNG GIÁC (UNIT CIRCLE & TRIG VALUES)
# ==========================================

def render_unit_circle(
    angle_deg: float,
    show_sin_cos: bool = True,
    show_tan: bool = False,
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 380,
) -> str:
    style = style or {}
    bg = style.get("bg_panel", "#FFFFFF")
    ink = style.get("ink_primary", "#0F172A")
    brand = style.get("brand", "#0284C7")
    accent = style.get("accent", "#EF4444")
    green = style.get("success", "#10B981")
    border = style.get("border_color", "#CBD5E1")

    cx, cy, r = width / 2, height / 2 + 10, 130
    rad = math.radians(angle_deg)
    px = cx + r * math.cos(rad)
    py = cy - r * math.sin(rad)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{brand}" fill-opacity="0.03"/>',
        '</g><g id="math-layer">',
    ]

    # Coordinate Axes
    svg.append(f'<line x1="{cx-r-30}" y1="{cy}" x2="{cx+r+30}" y2="{cy}" stroke="{ink}" stroke-width="1.8"/>')
    svg.append(f'<polygon points="{cx+r+33},{cy} {cx+r+25},{cy-4} {cx+r+25},{cy+4}" fill="{ink}"/>')
    svg.append(f'<text x="{cx+r+36}" y="{cy+4}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">cos x</text>')

    svg.append(f'<line x1="{cx}" y1="{cy+r+30}" x2="{cx}" y2="{cy-r-30}" stroke="{ink}" stroke-width="1.8"/>')
    svg.append(f'<polygon points="{cx},{cy-r-33} {cx-4},{cy-r-25} {cx+4},{cy-r-25}" fill="{ink}"/>')
    svg.append(f'<text x="{cx+6}" y="{cy-r-25}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">sin x</text>')
    svg.append(f'<text x="{cx-12}" y="{cy+14}" font-family="Segoe UI, Arial" font-size="11" font-weight="700" fill="{ink}">O</text>')

    # Unit circle
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{ink}" stroke-width="2.2"/>')

    # Radius vector OP
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{px}" y2="{py}" stroke="{brand}" stroke-width="2.4"/>')
    svg.append(f'<circle cx="{px}" cy="{py}" r="4.5" fill="{accent}"/>')
    svg.append(f'<text x="{px+8}" y="{py-6}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{accent}">M({angle_deg}°)</text>')

    # Angle arc
    arc_r = 32
    large_arc = 1 if angle_deg > 180 else 0
    arc_end_x = cx + arc_r * math.cos(rad)
    arc_end_y = cy - arc_r * math.sin(rad)
    svg.append(f'<path d="M {cx+arc_r} {cy} A {arc_r} {arc_r} 0 {large_arc} 0 {arc_end_x} {arc_end_y}" fill="none" stroke="{accent}" stroke-width="1.8"/>')
    lbl_ang = "?" if is_student_worksheet else f"{angle_deg}°"
    svg.append(f'<text x="{cx+arc_r+12}" y="{cy-10}" font-family="Segoe UI, Arial" font-size="11.5" font-weight="800" fill="{accent}">{lbl_ang}</text>')

    # Projections on cos and sin axes
    if show_sin_cos:
        # Cos projection (vertical dashed to x-axis)
        svg.append(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{cy}" stroke="{green}" stroke-width="1.5" stroke-dasharray="4,4"/>')
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{px}" y2="{cy}" stroke="{green}" stroke-width="3"/>')
        cos_val = round(math.cos(rad), 2)
        lbl_cos = "?" if is_student_worksheet else f"cos={cos_val}"
        svg.append(f'<text x="{px}" y="{cy+18}" font-family="Segoe UI, Arial" font-size="10.5" font-weight="800" fill="{green}" text-anchor="middle">{lbl_cos}</text>')

        # Sin projection (horizontal dashed to y-axis)
        svg.append(f'<line x1="{px}" y1="{py}" x2="{cx}" y2="{py}" stroke="{brand}" stroke-width="1.5" stroke-dasharray="4,4"/>')
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{py}" stroke="{brand}" stroke-width="3"/>')
        sin_val = round(math.sin(rad), 2)
        lbl_sin = "?" if is_student_worksheet else f"sin={sin_val}"
        svg.append(f'<text x="{cx-38}" y="{py+4}" font-family="Segoe UI, Arial" font-size="10.5" font-weight="800" fill="{brand}">{lbl_sin}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 6. BIỂU ĐỒ CỘT & THỐNG KÊ RỜI RẠC (BAR CHARTS & FREQUENCY)
# ==========================================

def render_bar_chart(
    categories: List[str],
    values: List[float],
    y_label: str = "Tần số",
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 320,
) -> str:
    style = style or {}
    bg = style.get("bg_panel", "#FFFFFF")
    ink = style.get("ink_primary", "#0F172A")
    brand = style.get("brand", "#0284C7")
    accent = style.get("accent", "#38BDF8")
    border = style.get("border_color", "#CBD5E1")

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="math-layer">',
    ]

    pad_l, pad_r, pad_b, pad_t = 60, 30, 50, 40
    plot_w = width - pad_l - pad_r
    plot_h = height - pad_t - pad_b
    max_val = max(values) if values else 10
    max_y = math.ceil(max_val * 1.2) or 10

    # Axes
    svg.append(f'<line x1="{pad_l}" y1="{height-pad_b}" x2="{width-pad_r}" y2="{height-pad_b}" stroke="{ink}" stroke-width="1.8"/>')
    svg.append(f'<line x1="{pad_l}" y1="{height-pad_b}" x2="{pad_l}" y2="{pad_t-10}" stroke="{ink}" stroke-width="1.8"/>')
    svg.append(f'<polygon points="{pad_l},{pad_t-15} {pad_l-4},{pad_t-6} {pad_l+4},{pad_t-6}" fill="{ink}"/>')
    svg.append(f'<text x="{pad_l-10}" y="{pad_t-18}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="{ink}">{y_label}</text>')

    # Horizontal grid lines & Y labels
    y_steps = 5
    for s in range(y_steps + 1):
        y_val = (s / y_steps) * max_y
        sy = height - pad_b - (s / y_steps) * plot_h
        svg.append(f'<line x1="{pad_l}" y1="{sy}" x2="{width-pad_r}" y2="{sy}" stroke="#E2E8F0" stroke-width="1"/>')
        svg.append(f'<text x="{pad_l-8}" y="{sy+4}" font-family="Segoe UI, Arial" font-size="10" fill="#475569" text-anchor="end">{int(y_val)}</text>')

    # Bars
    n = len(categories)
    col_w = plot_w / (n * 1.5 + 0.5)
    gap = col_w * 0.5

    for i, (cat, val) in enumerate(zip(categories, values)):
        bx = pad_l + gap + i * (col_w + gap)
        bh = (val / max_y) * plot_h
        by = height - pad_b - bh
        svg.append(f'<rect x="{bx}" y="{by}" width="{col_w}" height="{bh}" fill="{brand}" rx="3"/>')
        val_txt = "?" if is_student_worksheet and i == len(categories)-1 else str(int(val))
        svg.append(f'<text x="{bx + col_w/2}" y="{by - 6}" font-family="Segoe UI, Arial" font-size="11" font-weight="700" fill="{brand}" text-anchor="middle">{val_txt}</text>')
        svg.append(f'<text x="{bx + col_w/2}" y="{height - pad_b + 18}" font-family="Segoe UI, Arial" font-size="10.5" font-weight="600" fill="{ink}" text-anchor="middle">{cat}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)
