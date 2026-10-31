# -*- coding: utf-8 -*-
"""
CORE MATHEMATICAL VECTOR PRIMITIVES ENGINE
Dựng hình học, đồ thị, sơ đồ và mô hình STEM chuẩn xác từng pixel bằng vector SVG.
Tách biệt rõ ràng 2 lớp:
  - <g id="art-layer">: Nền, khung lưới thẩm mỹ, bóng đổ, gradient
  - <g id="math-layer">: Tọa độ chính xác, điểm, đường, góc, ký hiệu chuẩn
Hỗ trợ 2 chế độ:
  - is_student_worksheet=False (Bản Thầy / Master): Hiện đủ tọa độ, số đo, bằng chứng
  - is_student_worksheet=True (Phiếu Học sinh): Ẩn đáp số, đặt dấu '?', chừa dòng chấm
"""

import math
from typing import Dict, Any, List, Tuple, Optional

# ==========================================
# 1. HÌNH HỌC PHẲNG (POLYGONS, ANGLES, TRIANGLES, QUADRILATERALS)
# ==========================================

def render_polygon_geometry(
    vertices: List[Tuple[float, float]],
    labels: List[str],
    side_labels: Optional[List[Dict[str, Any]]] = None,
    right_angles: Optional[List[int]] = None,
    angle_arcs: Optional[List[Dict[str, Any]]] = None,
    auxiliary_segments: Optional[List[Tuple[int, int]]] = None,
    shaded_subpolygon: Optional[List[int]] = None,
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
    accent = style.get("accent", "#F59E0B")
    border = style.get("border_color", "#CBD5E1")

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
    ]

    # Grid background dots
    for x in range(20, width, 30):
        for y in range(20, height, 30):
            svg.append(f'<circle cx="{x}" cy="{y}" r="0.8" fill="#94A3B8" opacity="0.3"/>')

    # Shaded subpolygon if any
    if shaded_subpolygon:
        pts = " ".join(f"{vertices[i][0]},{vertices[i][1]}" for i in shaded_subpolygon)
        svg.append(f'<polygon points="{pts}" fill="{brand}" fill-opacity="0.18" stroke="none"/>')

    svg.append('</g>')
    svg.append('<g id="math-layer">')

    # Main polygon edges
    pts_str = " ".join(f"{x},{y}" for x, y in vertices)
    svg.append(f'<polygon points="{pts_str}" fill="none" stroke="{ink}" stroke-width="2.2" stroke-linejoin="round"/>')

    # Auxiliary segments (dashed)
    if auxiliary_segments:
        for idx1, idx2 in auxiliary_segments:
            p1, p2 = vertices[idx1], vertices[idx2]
            stroke_style = "4,4" if is_student_worksheet else "none"
            color = "#64748B" if is_student_worksheet else brand
            svg.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="{color}" stroke-width="1.8" stroke-dasharray="5,4"/>')

    # Right angle marks
    if right_angles:
        d = 12
        for idx in right_angles:
            prev_idx = (idx - 1) % len(vertices)
            next_idx = (idx + 1) % len(vertices)
            p = vertices[idx]
            p_prev = vertices[prev_idx]
            p_next = vertices[next_idx]
            # Unit vectors
            v1 = (p_prev[0] - p[0], p_prev[1] - p[1])
            v2 = (p_next[0] - p[0], p_next[1] - p[1])
            len1 = math.hypot(*v1) or 1
            len2 = math.hypot(*v2) or 1
            u1 = (v1[0] / len1 * d, v1[1] / len1 * d)
            u2 = (v2[0] / len2 * d, v2[1] / len2 * d)
            corner_x = p[0] + u1[0] + u2[0]
            corner_y = p[1] + u1[1] + u2[1]
            svg.append(f'<polyline points="{p[0]+u1[0]},{p[1]+u1[1]} {corner_x},{corner_y} {p[0]+u2[0]},{p[1]+u2[1]}" fill="none" stroke="{brand}" stroke-width="1.6"/>')

    # Angle arcs
    if angle_arcs:
        for arc in angle_arcs:
            idx = arc.get("vertex_idx", 0)
            p = vertices[idx]
            deg = arc.get("deg", 60)
            r = arc.get("r", 20)
            lbl = "?" if is_student_worksheet and arc.get("hide_in_worksheet") else arc.get("label", f"{deg}°")
            svg.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="{r}" fill="none" stroke="{accent}" stroke-width="1.5" stroke-dasharray="3,3"/>')
            svg.append(f'<text x="{p[0]+r+4}" y="{p[1]+4}" font-family="Segoe UI, Arial" font-size="11" font-weight="700" fill="{accent}">{lbl}</text>')

    # Side length labels
    if side_labels:
        for sl in side_labels:
            i1, i2 = sl["segment"]
            val = "?" if is_student_worksheet and sl.get("hide_in_worksheet") else sl["text"]
            mx = (vertices[i1][0] + vertices[i2][0]) / 2 + sl.get("offset_x", 0)
            my = (vertices[i1][1] + vertices[i2][1]) / 2 + sl.get("offset_y", 0)
            svg.append(f'<text x="{mx}" y="{my}" font-family="Segoe UI, Arial" font-size="11.5" font-weight="700" fill="{ink}" text-anchor="middle">{val}</text>')

    # Vertex dots and labels
    for i, (x, y) in enumerate(vertices):
        lbl = labels[i] if i < len(labels) else f"V{i}"
        svg.append(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{brand}"/>')
        # Offset label away from center
        ox = 10 if x >= width / 2 else -16
        oy = 14 if y >= height / 2 else -8
        svg.append(f'<text x="{x + ox}" y="{y + oy}" font-family="Segoe UI, Arial" font-size="13" font-weight="800" fill="{ink}">{lbl}</text>')

    # Title kicker
    if title:
        svg.append(f'<text x="18" y="26" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 2. HÌNH HỌC ĐƯỜNG TRÒN (CIRCLES, TANGENTS, INSCRIBED ANGLES)
# ==========================================

def render_circle_geometry(
    radius: float,
    center: Tuple[float, float] = (250, 190),
    chords: Optional[List[Tuple[float, float]]] = None, # angles in deg
    tangents: Optional[List[float]] = None, # angles of tangency
    inscribed_triangles: Optional[List[Tuple[float, float, float]]] = None,
    labels: Optional[Dict[str, Tuple[float, float]]] = None,
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
    accent = style.get("accent", "#10B981")
    border = style.get("border_color", "#CBD5E1")

    cx, cy = center
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{brand}" fill-opacity="0.04"/>',
        '</g>',
        '<g id="math-layer">',
        f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{ink}" stroke-width="2.2"/>',
        f'<circle cx="{cx}" cy="{cy}" r="3.5" fill="{brand}"/>',
        f'<text x="{cx+6}" y="{cy-6}" font-family="Segoe UI, Arial" font-size="13" font-weight="800" fill="{ink}">O</text>',
    ]

    # Inscribed triangle if any
    if inscribed_triangles:
        for a1, a2, a3 in inscribed_triangles:
            p1 = (cx + radius * math.cos(math.radians(a1)), cy - radius * math.sin(math.radians(a1)))
            p2 = (cx + radius * math.cos(math.radians(a2)), cy - radius * math.sin(math.radians(a2)))
            p3 = (cx + radius * math.cos(math.radians(a3)), cy - radius * math.sin(math.radians(a3)))
            svg.append(f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" fill="none" stroke="{brand}" stroke-width="2"/>')
            for i, p in enumerate([p1, p2, p3]):
                name = ["A", "B", "C"][i]
                svg.append(f'<circle cx="{p[0]}" cy="{p[1]}" r="3" fill="{brand}"/>')
                dx = 12 * math.cos(math.radians([a1, a2, a3][i]))
                dy = -12 * math.sin(math.radians([a1, a2, a3][i]))
                svg.append(f'<text x="{p[0]+dx}" y="{p[1]+dy}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">{name}</text>')

    # Tangent lines
    if tangents:
        for deg in tangents:
            rad = math.radians(deg)
            tx = cx + radius * math.cos(rad)
            ty = cy - radius * math.sin(rad)
            # Normal vector is (cos, -sin). Tangent direction is (sin, cos)
            L = 100
            tan_dx = math.sin(rad) * L
            tan_dy = math.cos(rad) * L
            svg.append(f'<line x1="{tx - tan_dx}" y1="{ty - tan_dy}" x2="{tx + tan_dx}" y2="{ty + tan_dy}" stroke="{accent}" stroke-width="2"/>')
            svg.append(f'<circle cx="{tx}" cy="{ty}" r="3.5" fill="{accent}"/>')
            # Radius line to point of tangency (dashed)
            svg.append(f'<line x1="{cx}" y1="{cy}" x2="{tx}" y2="{ty}" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4"/>')

    if title:
        svg.append(f'<text x="18" y="26" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 3. HỆ TRỤC TỌA ĐỘ 2D & ĐỒ THỊ HÀM SỐ (OXY, LINES, PARABOLAS, CUBICS)
# ==========================================

def render_coordinate_plot_2d(
    curves: List[Dict[str, Any]], # list of curve defs: {"type": "line|parabola|cubic|rational|ellipse", "params": {...}, "color": "..."}
    xlim: Tuple[float, float] = (-5, 5),
    ylim: Tuple[float, float] = (-4, 6),
    key_points: Optional[List[Dict[str, Any]]] = None,
    shaded_region: Optional[Dict[str, Any]] = None,
    asymptotes: Optional[List[Dict[str, Any]]] = None,
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
    accent = style.get("accent", "#DC2626")
    border = style.get("border_color", "#CBD5E1")

    # Margins and mapping
    mx, my = 45, 35
    plot_w = width - 2 * mx
    plot_h = height - 2 * my

    def to_screen(x: float, y: float) -> Tuple[float, float]:
        sx = mx + (x - xlim[0]) / (xlim[1] - xlim[0]) * plot_w
        sy = my + (ylim[1] - y) / (ylim[1] - ylim[0]) * plot_h
        return sx, sy

    ox, oy = to_screen(0, 0)
    # Clamp origin inside canvas if out
    ox_clamped = max(mx, min(width - mx, ox))
    oy_clamped = max(my, min(height - my, oy))

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
    ]

    # Grid lines
    for gx in range(int(xlim[0]), int(xlim[1]) + 1):
        if gx == 0:
            continue
        sx, _ = to_screen(gx, 0)
        svg.append(f'<line x1="{sx}" y1="{my}" x2="{sx}" y2="{height-my}" stroke="#E2E8F0" stroke-width="1"/>')
    for gy in range(int(ylim[0]), int(ylim[1]) + 1):
        if gy == 0:
            continue
        _, sy = to_screen(0, gy)
        svg.append(f'<line x1="{mx}" y1="{sy}" x2="{width-mx}" y2="{sy}" stroke="#E2E8F0" stroke-width="1"/>')

    # Shaded integral region if any
    if shaded_region:
        x_start = shaded_region.get("x_from", -2)
        x_end = shaded_region.get("x_to", 2)
        func = shaded_region.get("func", lambda x: -x**2 + 4)
        poly_pts = []
        poly_pts.append(f"{to_screen(x_start, 0)[0]},{to_screen(x_start, 0)[1]}")
        steps = 30
        for i in range(steps + 1):
            cur_x = x_start + (x_end - x_start) * (i / steps)
            cur_y = func(cur_x)
            sx, sy = to_screen(cur_x, cur_y)
            poly_pts.append(f"{sx},{sy}")
        poly_pts.append(f"{to_screen(x_end, 0)[0]},{to_screen(x_end, 0)[1]}")
        svg.append(f'<polygon points="{" ".join(poly_pts)}" fill="{brand}" fill-opacity="0.25"/>')

    svg.append('</g>')
    svg.append('<g id="math-layer">')

    # Axes
    svg.append(f'<line x1="{mx-15}" y1="{oy_clamped}" x2="{width-mx+15}" y2="{oy_clamped}" stroke="{ink}" stroke-width="1.8"/>')
    svg.append(f'<polygon points="{width-mx+18},{oy_clamped} {width-mx+10},{oy_clamped-4} {width-mx+10},{oy_clamped+4}" fill="{ink}"/>')
    svg.append(f'<text x="{width-mx+22}" y="{oy_clamped+4}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">x</text>')

    svg.append(f'<line x1="{ox_clamped}" y1="{height-my+15}" x2="{ox_clamped}" y2="{my-15}" stroke="{ink}" stroke-width="1.8"/>')
    svg.append(f'<polygon points="{ox_clamped},{my-18} {ox_clamped-4},{my-10} {ox_clamped+4},{my-10}" fill="{ink}"/>')
    svg.append(f'<text x="{ox_clamped+8}" y="{my-12}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">y</text>')
    svg.append(f'<text x="{ox_clamped-12}" y="{oy_clamped+14}" font-family="Segoe UI, Arial" font-size="11" font-weight="700" fill="{ink}">O</text>')

    # Axis tick labels
    for gx in range(int(xlim[0]), int(xlim[1]) + 1):
        if gx == 0:
            continue
        sx, sy = to_screen(gx, 0)
        svg.append(f'<line x1="{sx}" y1="{oy_clamped-3}" x2="{sx}" y2="{oy_clamped+3}" stroke="{ink}" stroke-width="1.2"/>')
        svg.append(f'<text x="{sx}" y="{oy_clamped+15}" font-family="Segoe UI, Arial" font-size="9.5" fill="#475569" text-anchor="middle">{gx}</text>')
    for gy in range(int(ylim[0]), int(ylim[1]) + 1):
        if gy == 0:
            continue
        sx, sy = to_screen(0, gy)
        svg.append(f'<line x1="{ox_clamped-3}" y1="{sy}" x2="{ox_clamped+3}" y2="{sy}" stroke="{ink}" stroke-width="1.2"/>')
        svg.append(f'<text x="{ox_clamped-8}" y="{sy+3}" font-family="Segoe UI, Arial" font-size="9.5" fill="#475569" text-anchor="end">{gy}</text>')

    # Asymptotes (dashed)
    if asymptotes:
        for asy in asymptotes:
            if asy.get("vertical"):
                vx = asy["val"]
                sx, _ = to_screen(vx, 0)
                svg.append(f'<line x1="{sx}" y1="{my}" x2="{sx}" y2="{height-my}" stroke="{accent}" stroke-width="1.5" stroke-dasharray="4,4"/>')
                svg.append(f'<text x="{sx+4}" y="{my+16}" font-family="Segoe UI, Arial" font-size="10" font-weight="700" fill="{accent}">x={vx}</text>')
            elif asy.get("horizontal"):
                hy = asy["val"]
                _, sy = to_screen(0, hy)
                svg.append(f'<line x1="{mx}" y1="{sy}" x2="{width-mx}" y2="{sy}" stroke="{accent}" stroke-width="1.5" stroke-dasharray="4,4"/>')
                svg.append(f'<text x="{width-mx-40}" y="{sy-5}" font-family="Segoe UI, Arial" font-size="10" font-weight="700" fill="{accent}">y={hy}</text>')

    # Render mathematical curves
    for curve in curves:
        ctype = curve.get("type", "line")
        ccolor = curve.get("color", brand)
        cwidth = curve.get("width", 2.4)
        cname = "?" if is_student_worksheet and curve.get("hide_label_in_worksheet") else curve.get("name", "")

        if ctype == "line":
            m, b_val = curve["slope"], curve["intercept"]
            x1, x2 = xlim[0], xlim[1]
            p1 = to_screen(x1, m * x1 + b_val)
            p2 = to_screen(x2, m * x2 + b_val)
            svg.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="{ccolor}" stroke-width="{cwidth}"/>')
            if cname:
                svg.append(f'<text x="{p2[0]-25}" y="{p2[1]-8}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="{ccolor}">{cname}</text>')

        elif ctype in ("parabola", "cubic", "rational", "custom"):
            func = curve["func"]
            pts = []
            steps = 120
            dx = (xlim[1] - xlim[0]) / steps
            for i in range(steps + 1):
                cur_x = xlim[0] + i * dx
                try:
                    cur_y = func(cur_x)
                    if ylim[0] - 5 <= cur_y <= ylim[1] + 5:
                        sx, sy = to_screen(cur_x, cur_y)
                        pts.append((sx, sy))
                except Exception:
                    pass
            # Polyline segments
            if len(pts) > 1:
                pts_str = " ".join(f"{round(x,1)},{round(y,1)}" for x, y in pts)
                svg.append(f'<polyline points="{pts_str}" fill="none" stroke="{ccolor}" stroke-width="{cwidth}" stroke-linecap="round"/>')
            if cname and pts:
                svg.append(f'<text x="{pts[-1][0]-30}" y="{pts[-1][1]-10}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="{ccolor}">{cname}</text>')

        elif ctype == "ellipse":
            a, b_val = curve["a"], curve["b"]
            cx_pt, cy_pt = to_screen(0, 0)
            rx = a / (xlim[1] - xlim[0]) * plot_w
            ry = b_val / (ylim[1] - ylim[0]) * plot_h
            svg.append(f'<ellipse cx="{cx_pt}" cy="{cy_pt}" rx="{rx}" ry="{ry}" fill="none" stroke="{ccolor}" stroke-width="{cwidth}"/>')

    # Key points (Extrema, Roots, Intercepts, Foci)
    if key_points:
        for kp in key_points:
            kx, ky = kp["x"], kp["y"]
            sx, sy = to_screen(kx, ky)
            kname = "?" if is_student_worksheet and kp.get("hide_in_worksheet") else kp.get("label", "")
            kcolor = kp.get("color", accent)
            svg.append(f'<circle cx="{sx}" cy="{sy}" r="4" fill="{kcolor}"/>')
            if kname:
                svg.append(f'<text x="{sx+6}" y="{sy-6}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="{kcolor}">{kname}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 4. HÌNH KHÔNG GIAN 3D (PRISMS, PYRAMIDS, CONES, SPHERES, OXYZ)
# ==========================================

def render_solid_geometry(
    solid_type: str, # "prism_tri", "pyramid_quad", "cylinder", "cone", "sphere", "cube", "oxyz_frame"
    params: Optional[Dict[str, Any]] = None,
    title: str = "",
    style: Optional[Dict[str, Any]] = None,
    is_student_worksheet: bool = False,
    width: int = 500,
    height: int = 380,
) -> str:
    params = params or {}
    style = style or {}
    bg = style.get("bg_panel", "#FFFFFF")
    ink = style.get("ink_primary", "#0F172A")
    brand = style.get("brand", "#0284C7")
    accent = style.get("accent", "#10B981")
    border = style.get("border_color", "#CBD5E1")

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
    ]

    cx, cy = width / 2, height / 2 + 10

    if solid_type == "pyramid_quad":
        # S.ABCD with S on top, ABCD base in perspective
        S = (cx, cy - 130)
        A = (cx - 130, cy + 50)
        B = (cx - 40, cy + 100)
        C = (cx + 140, cy + 70)
        D = (cx + 50, cy + 20)
        # Hidden edges: AD, CD, SD
        svg.append(f'<polygon points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]} {S[0]},{S[1]}" fill="{brand}" fill-opacity="0.08"/>')
        svg.append('</g><g id="math-layer">')
        # Visible lines
        svg.append(f'<line x1="{S[0]}" y1="{S[1]}" x2="{A[0]}" y2="{A[1]}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<line x1="{S[0]}" y1="{S[1]}" x2="{B[0]}" y2="{B[1]}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<line x1="{S[0]}" y1="{S[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<line x1="{B[0]}" y1="{B[1]}" x2="{C[0]}" y2="{C[1]}" stroke="{ink}" stroke-width="2"/>')
        # Dashed hidden lines
        svg.append(f'<line x1="{A[0]}" y1="{A[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#64748B" stroke-width="1.6" stroke-dasharray="5,4"/>')
        svg.append(f'<line x1="{D[0]}" y1="{D[1]}" x2="{C[0]}" y2="{C[1]}" stroke="#64748B" stroke-width="1.6" stroke-dasharray="5,4"/>')
        svg.append(f'<line x1="{S[0]}" y1="{S[1]}" x2="{D[0]}" y2="{D[1]}" stroke="#64748B" stroke-width="1.6" stroke-dasharray="5,4"/>')
        # Labels
        for pt, name in [(S, "S"), (A, "A"), (B, "B"), (C, "C"), (D, "D")]:
            svg.append(f'<circle cx="{pt[0]}" cy="{pt[1]}" r="3.5" fill="{brand}"/>')
            svg.append(f'<text x="{pt[0]+(6 if pt[0]>=cx else -16)}" y="{pt[1]+(14 if pt[1]>=cy else -8)}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">{name}</text>')

    elif solid_type == "cylinder":
        rx, ry = 110, 32
        h = 160
        top_cy = cy - h / 2
        bot_cy = cy + h / 2
        svg.append(f'<rect x="{cx-rx}" y="{top_cy}" width="{2*rx}" height="{h}" fill="{brand}" fill-opacity="0.08"/>')
        svg.append('</g><g id="math-layer">')
        # Top ellipse (fully visible)
        svg.append(f'<ellipse cx="{cx}" cy="{top_cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{ink}" stroke-width="2"/>')
        # Side lines
        svg.append(f'<line x1="{cx-rx}" y1="{top_cy}" x2="{cx-rx}" y2="{bot_cy}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<line x1="{cx+rx}" y1="{top_cy}" x2="{cx+rx}" y2="{bot_cy}" stroke="{ink}" stroke-width="2"/>')
        # Bottom half visible, half dashed
        svg.append(f'<path d="M {cx-rx} {bot_cy} A {rx} {ry} 0 0 0 {cx+rx} {bot_cy}" fill="none" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<path d="M {cx-rx} {bot_cy} A {rx} {ry} 0 0 1 {cx+rx} {bot_cy}" fill="none" stroke="#64748B" stroke-width="1.6" stroke-dasharray="5,4"/>')
        # Height and radius indicators
        svg.append(f'<line x1="{cx}" y1="{top_cy}" x2="{cx+rx}" y2="{top_cy}" stroke="{accent}" stroke-width="1.8"/>')
        r_lbl = "?" if is_student_worksheet else "R"
        svg.append(f'<text x="{cx+rx/2}" y="{top_cy-6}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="{accent}">{r_lbl}</text>')

    elif solid_type == "cone":
        rx, ry = 110, 30
        h = 170
        tip = (cx, cy - h / 2)
        bot_cy = cy + h / 2
        svg.append(f'<polygon points="{tip[0]},{tip[1]} {cx-rx},{bot_cy} {cx+rx},{bot_cy}" fill="{brand}" fill-opacity="0.08"/>')
        svg.append('</g><g id="math-layer">')
        svg.append(f'<line x1="{tip[0]}" y1="{tip[1]}" x2="{cx-rx}" y2="{bot_cy}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<line x1="{tip[0]}" y1="{tip[1]}" x2="{cx+rx}" y2="{bot_cy}" stroke="{ink}" stroke-width="2"/>')
        # Bottom ellipse
        svg.append(f'<path d="M {cx-rx} {bot_cy} A {rx} {ry} 0 0 0 {cx+rx} {bot_cy}" fill="none" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<path d="M {cx-rx} {bot_cy} A {rx} {ry} 0 0 1 {cx+rx} {bot_cy}" fill="none" stroke="#64748B" stroke-width="1.6" stroke-dasharray="5,4"/>')
        # Axis height (dashed)
        svg.append(f'<line x1="{tip[0]}" y1="{tip[1]}" x2="{cx}" y2="{bot_cy}" stroke="#64748B" stroke-width="1.6" stroke-dasharray="5,4"/>')
        svg.append(f'<line x1="{cx}" y1="{bot_cy}" x2="{cx+rx}" y2="{bot_cy}" stroke="{accent}" stroke-width="1.8" stroke-dasharray="4,4"/>')

    elif solid_type == "oxyz_frame":
        # 3D Coordinate Axes Oxyz
        svg.append('</g><g id="math-layer">')
        O = (cx - 20, cy + 40)
        # Oz upwards
        Oz = (O[0], O[1] - 160)
        # Oy rightwards
        Oy = (O[0] + 170, O[1] - 10)
        # Ox downwards-leftwards (perspective)
        Ox = (O[0] - 120, O[1] + 90)
        svg.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{Oz[0]}" y2="{Oz[1]}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<polygon points="{Oz[0]},{Oz[1]-5} {Oz[0]-4},{Oz[1]+3} {Oz[0]+4},{Oz[1]+3}" fill="{ink}"/>')
        svg.append(f'<text x="{Oz[0]-16}" y="{Oz[1]-4}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">z</text>')

        svg.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{Oy[0]}" y2="{Oy[1]}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<polygon points="{Oy[0]+5},{Oy[1]} {Oy[0]-3},{Oy[1]-4} {Oy[0]-3},{Oy[1]+4}" fill="{ink}"/>')
        svg.append(f'<text x="{Oy[0]+10}" y="{Oy[1]+4}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">y</text>')

        svg.append(f'<line x1="{O[0]}" y1="{O[1]}" x2="{Ox[0]}" y2="{Ox[1]}" stroke="{ink}" stroke-width="2"/>')
        svg.append(f'<polygon points="{Ox[0]-4},{Ox[1]+4} {Ox[0]+4},{Ox[1]} {Ox[0]},{Ox[1]-5}" fill="{ink}"/>')
        svg.append(f'<text x="{Ox[0]-14}" y="{Ox[1]+16}" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{ink}">x</text>')
        svg.append(f'<text x="{O[0]-14}" y="{O[1]-4}" font-family="Segoe UI, Arial" font-size="11" font-weight="700" fill="{ink}">O</text>')

        # Example Point M(x, y, z) box projection
        mx_val = params.get("mx", 80)
        my_val = params.get("my", 110)
        mz_val = params.get("mz", 90)
        # Vector combination
        M_x = O[0] - mx_val * 0.8 + my_val * 0.95
        M_y = O[1] + mx_val * 0.6 - mz_val
        M_base_x = O[0] - mx_val * 0.8 + my_val * 0.95
        M_base_y = O[1] + mx_val * 0.6
        svg.append(f'<line x1="{M_base_x}" y1="{M_base_y}" x2="{M_x}" y2="{M_y}" stroke="{brand}" stroke-width="1.8" stroke-dasharray="4,4"/>')
        svg.append(f'<circle cx="{M_x}" cy="{M_y}" r="4" fill="{accent}"/>')
        lbl_M = "M(?, ?, ?)" if is_student_worksheet else f"M({params.get('coords', 'x0, y0, z0')})"
        svg.append(f'<text x="{M_x+8}" y="{M_y-6}" font-family="Segoe UI, Arial" font-size="11.5" font-weight="800" fill="{accent}">{lbl_M}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 5. THỐNG KÊ, BIỂU ĐỒ & XÁC SUẤT (BOXPLOTS, HISTOGRAMS, PROBABILITY TREES)
# ==========================================

def render_statistics_chart(
    chart_type: str, # "box_plot", "histogram", "tree_diagram", "scatter_trend"
    data: Dict[str, Any],
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
    accent = style.get("accent", "#7C3AED")
    border = style.get("border_color", "#CBD5E1")

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="math-layer">',
    ]

    if chart_type == "box_plot":
        # Box-and-Whisker: min, Q1, median, Q3, max
        q1 = data.get("q1", 25)
        med = data.get("med", 45)
        q3 = data.get("q3", 70)
        dmin = data.get("min", 10)
        dmax = data.get("max", 95)
        # Map [0, 100] to canvas X
        scale_x = lambda v: 60 + (v / 100) * 380
        cy = 200

        # Number line axis
        svg.append(f'<line x1="50" y1="{cy+70}" x2="450" y2="{cy+70}" stroke="{ink}" stroke-width="1.5"/>')
        for tick in range(0, 101, 20):
            tx = scale_x(tick)
            svg.append(f'<line x1="{tx}" y1="{cy+65}" x2="{tx}" y2="{cy+75}" stroke="{ink}"/>')
            svg.append(f'<text x="{tx}" y="{cy+90}" font-family="Segoe UI, Arial" font-size="10" fill="#475569" text-anchor="middle">{tick}</text>')

        # Whiskers
        svg.append(f'<line x1="{scale_x(dmin)}" y1="{cy}" x2="{scale_x(q1)}" y2="{cy}" stroke="{brand}" stroke-width="2"/>')
        svg.append(f'<line x1="{scale_x(q3)}" y1="{cy}" x2="{scale_x(dmax)}" y2="{cy}" stroke="{brand}" stroke-width="2"/>')
        svg.append(f'<line x1="{scale_x(dmin)}" y1="{cy-18}" x2="{scale_x(dmin)}" y2="{cy+18}" stroke="{brand}" stroke-width="2"/>')
        svg.append(f'<line x1="{scale_x(dmax)}" y1="{cy-18}" x2="{scale_x(dmax)}" y2="{cy+18}" stroke="{brand}" stroke-width="2"/>')

        # Interquartile Box
        bx = scale_x(q1)
        bw = scale_x(q3) - bx
        svg.append(f'<rect x="{bx}" y="{cy-35}" width="{bw}" height="70" fill="{brand}" fill-opacity="0.18" stroke="{brand}" stroke-width="2.2" rx="4"/>')
        # Median line
        svg.append(f'<line x1="{scale_x(med)}" y1="{cy-35}" x2="{scale_x(med)}" y2="{cy+35}" stroke="{accent}" stroke-width="3"/>')

        # Labels
        lbl_med = "?" if is_student_worksheet else f"Trung vị = {med}"
        svg.append(f'<text x="{scale_x(med)}" y="{cy-42}" font-family="Segoe UI, Arial" font-size="11.5" font-weight="800" fill="{accent}" text-anchor="middle">{lbl_med}</text>')
        svg.append(f'<text x="{scale_x(q1)}" y="{cy+50}" font-family="Segoe UI, Arial" font-size="10" font-weight="700" fill="{brand}" text-anchor="middle">Q1={q1}</text>')
        svg.append(f'<text x="{scale_x(q3)}" y="{cy+50}" font-family="Segoe UI, Arial" font-size="10" font-weight="700" fill="{brand}" text-anchor="middle">Q3={q3}</text>')

    elif chart_type == "tree_diagram":
        # 2-stage probability tree
        pA = data.get("pA", 0.6)
        pB_given_A = data.get("pB_A", 0.7)
        # Root
        root = (60, 190)
        nodeA1 = (200, 120)
        nodeA2 = (200, 260)
        nodeB11 = (360, 80)
        nodeB12 = (360, 160)
        nodeB21 = (360, 220)
        nodeB22 = (360, 300)

        # Branches
        for p1, p2, prob_txt in [
            (root, nodeA1, f"P(A) = {pA}"),
            (root, nodeA2, f"P(A') = {round(1-pA, 2)}"),
            (nodeA1, nodeB11, f"P(B|A) = {pB_given_A}"),
            (nodeA1, nodeB12, f"P(B'|A) = {round(1-pB_given_A, 2)}"),
            (nodeA2, nodeB21, "P(B|A')"),
            (nodeA2, nodeB22, "P(B'|A')"),
        ]:
            svg.append(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="{ink}" stroke-width="1.8"/>')
            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 - 6
            svg.append(f'<text x="{mx}" y="{my}" font-family="Segoe UI, Arial" font-size="10" font-weight="700" fill="{brand}" text-anchor="middle">{prob_txt}</text>')

        # Node circles and text
        for pt, lbl in [(root, "Bắt đầu"), (nodeA1, "A"), (nodeA2, "A'"), (nodeB11, "B"), (nodeB12, "B'"), (nodeB21, "B"), (nodeB22, "B'")]:
            svg.append(f'<circle cx="{pt[0]}" cy="{pt[1]}" r="14" fill="{bg}" stroke="{brand}" stroke-width="2"/>')
            svg.append(f'<text x="{pt[0]}" y="{pt[1]+4}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="{ink}" text-anchor="middle">{lbl}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)


# ==========================================
# 6. STEM, ĐÒN BẨY & CÁN CÂN THĂNG BẰNG
# ==========================================

def render_stem_balance_scale(
    tilt_angle_deg: float,
    left_weight_val: float,
    right_weight_val: float,
    left_label: str = "Vế Trái",
    right_label: str = "Vế Phải",
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
    accent = style.get("accent", "#10B981" if abs(tilt_angle_deg) < 0.1 else "#F59E0B")
    border = style.get("border_color", "#CBD5E1")

    cx, cy = width / 2, height / 2 + 15
    beam_len = 170
    rad = math.radians(tilt_angle_deg)

    # Beam endpoints
    x_left = cx - beam_len * math.cos(rad)
    y_left = cy - beam_len * math.sin(rad)
    x_right = cx + beam_len * math.cos(rad)
    y_right = cy + beam_len * math.sin(rad)

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="{bg}" rx="8" stroke="{border}" stroke-width="1.5"/>',
        '<g id="art-layer">',
    ]

    # Fulcrum base & pillar
    svg.append(f'<polygon points="{cx},{cy} {cx-35},{cy+110} {cx+35},{cy+110}" fill="#334155"/>')
    svg.append(f'<rect x="{cx-70}" y="{cy+110}" width="140" height="12" fill="#1E293B" rx="3"/>')

    # Gauge arc at top
    svg.append(f'<path d="M {cx-40} {cy-25} A 50 50 0 0 1 {cx+40} {cy-25}" fill="none" stroke="#94A3B8" stroke-width="1.5"/>')
    # Needle
    needle_tip_x = cx - 45 * math.sin(rad)
    needle_tip_y = cy - 45 * math.cos(rad)
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{needle_tip_x}" y2="{needle_tip_y}" stroke="{accent}" stroke-width="2.5"/>')

    svg.append('</g><g id="math-layer">')

    # Rotating beam
    svg.append(f'<line x1="{x_left}" y1="{y_left}" x2="{x_right}" y2="{y_right}" stroke="#F59E0B" stroke-width="6" stroke-linecap="round"/>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="#0284C7"/>')

    # Hanging pans
    chain_h = 65
    pan_w = 70
    for px, py, val, lbl in [(x_left, y_left, left_weight_val, left_label), (x_right, y_right, right_weight_val, right_label)]:
        # Chains
        svg.append(f'<line x1="{px}" y1="{py}" x2="{px-pan_w/2}" y2="{py+chain_h}" stroke="#94A3B8" stroke-width="1.2"/>')
        svg.append(f'<line x1="{px}" y1="{py}" x2="{px+pan_w/2}" y2="{py+chain_h}" stroke="#94A3B8" stroke-width="1.2"/>')
        # Pan
        svg.append(f'<path d="M {px-pan_w/2} {py+chain_h} Q {px} {py+chain_h+18} {px+pan_w/2} {py+chain_h}" fill="#E2E8F0" stroke="#475569" stroke-width="2"/>')
        # Weight load box
        box_txt = "?" if is_student_worksheet and "Target" in lbl else f"{val}"
        svg.append(f'<rect x="{px-20}" y="{py+chain_h-22}" width="40" height="22" fill="{brand}" rx="4"/>')
        svg.append(f'<text x="{px}" y="{py+chain_h-7}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle">{box_txt}</text>')
        svg.append(f'<text x="{px}" y="{py+chain_h+32}" font-family="Segoe UI, Arial" font-size="11" font-weight="700" fill="{ink}" text-anchor="middle">{lbl}</text>')

    # Balance state badge
    state_txt = "★ THĂNG BẰNG HOÀN TOÀN (0° LỆCH)" if abs(tilt_angle_deg) < 0.1 else f"▲ CÁN CÂN MẤT CÂN BẰNG ({round(abs(tilt_angle_deg), 1)}° LỆCH)"
    state_color = "#10B981" if abs(tilt_angle_deg) < 0.1 else "#F59E0B"
    svg.append(f'<rect x="{cx-120}" y="{height-38}" width="240" height="26" fill="{state_color}" fill-opacity="0.15" stroke="{state_color}" rx="5"/>')
    svg.append(f'<text x="{cx}" y="{height-21}" font-family="Segoe UI, Arial" font-size="11" font-weight="800" fill="{state_color}" text-anchor="middle">{state_txt}</text>')

    if title:
        svg.append(f'<text x="18" y="24" font-family="Segoe UI, Arial" font-size="12" font-weight="800" fill="{brand}">{title}</text>')

    svg.append('</g>')
    svg.append('</svg>')
    return "\n".join(svg)
