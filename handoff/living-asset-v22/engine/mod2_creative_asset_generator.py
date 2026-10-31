# -*- coding: utf-8 -*-
"""
MODULE 2 — CREATIVE ASSET GENERATION (mod2_creative_asset_generator.py)
Sinh tài sản đồ họa chất lượng cao cho từng Living Asset:
1. Tách biệt Lớp Nghệ Thuật (<g id="art-layer">) và Lớp Cấu Trúc Toán Học (<g id="math-layer">)
   để vừa đạt thẩm mỹ cao vừa đảm bảo độ chính xác hình học/đại số tuyệt đối.
2. Quản lý 5 Ngôn ngữ Nghệ thuật (Artistic Worlds):
   - WARM_STORYBOOK_TACTILE (Ấm áp, chất liệu gỗ & sân gạch cổ, thân thiện với học sinh sợ Toán)
   - STEM_COMMAND_3D (Đài điều khiển kỹ thuật 3D/2.5D hiện đại)
   - EUCLIDEAN_ATELIER_PRO (Xưởng thiết kế hình học & kiến trúc chuẩn xác)
   - DATA_OBSERVATORY_LAB (Phòng thí nghiệm dữ liệu, cân trọng tâm & mô phỏng Monte Carlo)
   - REAL_PAPER_HYBRID_V04 (Ngôn ngữ giấy thật A4 v0.4 kết hợp giấy nhớ nhận thức)
"""

from __future__ import annotations
from pathlib import Path
from typing import Dict, Any


ARTISTIC_WORLDS: Dict[str, Dict[str, Any]] = {
    "WARM_STORYBOOK_TACTILE": {
        "world_id": "WARM_STORYBOOK_TACTILE",
        "name_vi": "Xưởng Truyện Tranh & Vật Thể Ấm Áp (Storybook Tactile)",
        "bg_primary": "#FDF8F0",
        "bg_panel": "#FFFFFF",
        "ink_primary": "#292524",
        "accent_main": "#D97706",
        "accent_secondary": "#059669",
        "border_color": "#E7E5E4",
        "mood": "Ấm áp, gần gũi, giảm lo âu Toán học, phù hợp mở đầu trực quan",
    },
    "STEM_COMMAND_3D": {
        "world_id": "STEM_COMMAND_3D",
        "name_vi": "Đài Chỉ Huy Kỹ Thuật STEM 3D/2.5D (STEM Command Deck)",
        "bg_primary": "#0F172A",
        "bg_panel": "#1E293B",
        "ink_primary": "#F8FAFC",
        "accent_main": "#38BDF8",
        "accent_secondary": "#10B981",
        "border_color": "#334155",
        "mood": "Hiện đại, mô phỏng hệ thống kỹ thuật, vận tải, thủy điện & đồ thị",
    },
    "EUCLIDEAN_ATELIER_PRO": {
        "world_id": "EUCLIDEAN_ATELIER_PRO",
        "name_vi": "Xưởng Kiến Trúc & Hình Học Chuẩn Xác (Euclidean Atelier)",
        "bg_primary": "#F8FAFC",
        "bg_panel": "#FFFFFF",
        "ink_primary": "#0F172A",
        "accent_main": "#2563EB",
        "accent_secondary": "#DC2626",
        "border_color": "#CBD5E1",
        "mood": "Chuẩn mực, lưới tọa độ rõ nét, cắt ghép hình học & tia sáng đồng dạng",
    },
    "DATA_OBSERVATORY_LAB": {
        "world_id": "DATA_OBSERVATORY_LAB",
        "name_vi": "Đài Quan Sát Dữ Liệu & Mô Phỏng Ngẫu Nhiên (Data Observatory)",
        "bg_primary": "#F5F3FF",
        "bg_panel": "#FFFFFF",
        "ink_primary": "#1E1B4B",
        "accent_main": "#7C3AED",
        "accent_secondary": "#0D9488",
        "border_color": "#DDD6FE",
        "mood": "Khám phá quy luật số lớn, cân bằng trọng tâm thống kê & tăng trưởng tài chính",
    },
    "REAL_PAPER_HYBRID_V04": {
        "world_id": "REAL_PAPER_HYBRID_V04",
        "name_vi": "Phiếu Học Tập Giấy Thật & Giấy Nhớ (Real Paper v0.4)",
        "bg_primary": "#EFECE6",
        "bg_panel": "#FFFFFF",
        "ink_primary": "#111827",
        "accent_main": "#1D4ED8",
        "accent_secondary": "#B91C1C",
        "border_color": "#D1D5DB",
        "mood": "Đồng bộ 1:1 với vở học sinh và trang in A4 chất lượng cao",
    },
}


class CreativeAssetGenerator:
    """Module 2: Tạo SVG phân lớp (Art Layer + Math Layer) cho toàn bộ 16 Living Assets."""

    def __init__(self, output_svg_dir: Path):
        self.output_svg_dir = output_svg_dir
        self.output_svg_dir.mkdir(parents=True, exist_ok=True)

    def get_svg_for_asset(self, asset_id: str) -> str:
        """Trả về mã SVG chuẩn (viewBox 0 0 560 220) tách lớp nghệ thuật và lớp toán học."""
        generators = {
            "YD-LA-NUM-G6-01": self._svg_num_g6_01_courtyard_tiling,
            "YD-LA-NUM-G6-02": self._svg_num_g6_02_submarine_integers,
            "YD-LA-NUM-G6-03": self._svg_num_g6_03_orange_mixture,
            "YD-LA-NUM-G7-04": self._svg_num_g7_04_sqrt2_spiral,
            "YD-LA-ALG-G7-05": self._svg_alg_g7_05_alloy_proportion,
            "YD-LA-ALG-G8-06": self._svg_alg_g8_06_taxi_intersection,
            "YD-LA-ALG-G8-07": self._svg_alg_g8_07_rate_balance_3d,
            "YD-LA-ALG-G9-08": self._svg_alg_g9_08_dual_pipe_hydro,
            "YD-LA-ALG-G9-09": self._svg_alg_g9_09_parabola_bridge,
            "YD-LA-GEO-G6-10": self._svg_geo_g6_10_lshape_garden_h07,
            "YD-LA-GEO-G8-11": self._svg_geo_g8_11_pythagoras_cutpaste,
            "YD-LA-GEO-G8-12": self._svg_geo_g8_12_thales_shadow_tower,
            "YD-LA-GEO-G9-13": self._svg_geo_g9_13_cylinder_net_3d,
            "YD-LA-STAT-G7-14": self._svg_stat_g7_14_mean_median_seesaw,
            "YD-LA-STAT-G8-15": self._svg_stat_g8_15_monte_carlo_convergence,
            "YD-LA-APPL-G9-16": self._svg_appl_g9_16_garden_path_finance,
        }
        fn = generators.get(asset_id, self._svg_num_g6_01_courtyard_tiling)
        return fn()

    def export_all_svgs(self, assets: list[Dict[str, Any]]) -> Dict[str, str]:
        paths = {}
        for a in assets:
            aid = a["asset_id"]
            svg_code = self.get_svg_for_asset(aid)
            p = self.output_svg_dir / f"{aid}.svg"
            p.write_text(svg_code, encoding="utf-8")
            paths[aid] = str(p)
        return paths

    def _svg_num_g6_01_courtyard_tiling(self) -> str:
        # 24m x 18m courtyard tiled with 6m x 6m squares (4 x 3 = 12 tiles) vs 5m crack counterexample
        tiles = []
        for r in range(3):
            for c in range(4):
                x = 34 + c * 42
                y = 38 + r * 42
                fill = "#FDE68A" if (r + c) % 2 == 0 else "#FCD34D"
                tiles.append(
                    f'<rect x="{x}" y="{y}" width="40" height="40" rx="3" fill="{fill}" stroke="#B45309" stroke-width="1.5"/>'
                )
        tiles_str = "".join(tiles)
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.5"/>
    <rect x="28" y="32" width="180" height="138" rx="6" fill="#78350F" opacity="0.12"/>
    {tiles_str}
    <rect x="310" y="38" width="220" height="132" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-dasharray="5,4" stroke-width="1.5"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="125" y="24" font-size="11.5" font-weight="700" fill="#92400E" text-anchor="middle">Sân 24×18 dm (Gạch d = ƯCLN = 6 dm)</text>
    <text x="125" y="188" font-size="11" font-weight="700" fill="#15803D" text-anchor="middle">✓ Khít: (24:6) × (18:6) = 4 × 3 = 12 viên</text>
    <text x="420" y="60" font-size="12" font-weight="700" fill="#B91C1C" text-anchor="middle">Phản ví dụ khi chọn gạch cạnh d = 5 dm:</text>
    <rect x="330" y="72" width="140" height="70" fill="#FCA5A5" stroke="#B91C1C" stroke-width="1.5"/>
    <rect x="470" y="72" width="38" height="70" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="400" y="112" font-size="11.5" font-weight="700" fill="#7F1D1D" text-anchor="middle">4 viên × 5 = 20 dm</text>
    <text x="489" y="112" font-size="10.5" font-weight="700" fill="#DC2626" text-anchor="middle">Dư 4!</text>
    <text x="420" y="160" font-size="11" font-weight="600" fill="#991B1B" text-anchor="middle">24 chia 5 dư 4 dm → Phải chặt gạch!</text>
  </g>
</svg>"""

    def _svg_num_g6_02_submarine_integers(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <linearGradient id="seaGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#E0F2FE"/>
      <stop offset="28%" stop-color="#BAE6FD"/>
      <stop offset="29%" stop-color="#0284C7"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </linearGradient>
    <rect x="0" y="0" width="560" height="220" rx="12" fill="url(#seaGrad)"/>
    <path d="M 0 62 Q 70 56 140 62 T 280 62 T 420 62 T 560 62" fill="none" stroke="#FFFFFF" stroke-width="2.5"/>
    <!-- Submarine -->
    <ellipse cx="250" cy="145" rx="46" ry="18" fill="#FBBF24" stroke="#B45309" stroke-width="2"/>
    <rect x="238" y="116" width="22" height="14" rx="4" fill="#F59E0B" stroke="#B45309" stroke-width="1.5"/>
    <circle cx="235" cy="145" r="5" fill="#E0F2FE" stroke="#78350F" stroke-width="1.5"/>
    <circle cx="252" cy="145" r="5" fill="#E0F2FE" stroke="#78350F" stroke-width="1.5"/>
    <circle cx="269" cy="145" r="5" fill="#E0F2FE" stroke="#78350F" stroke-width="1.5"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <line x1="85" y1="18" x2="85" y2="205" stroke="#FFFFFF" stroke-width="2.5"/>
    <text x="72" y="66" font-size="11.5" font-weight="700" fill="#FFFFFF" text-anchor="end">0 m (Mặt biển)</text>
    <text x="72" y="148" font-size="11.5" font-weight="700" fill="#FDE047" text-anchor="end">-120 m</text>
    <text x="72" y="195" font-size="11.5" font-weight="700" fill="#FCA5A5" text-anchor="end">-200 m</text>
    <!-- Vector arrows -->
    <line x1="150" y1="62" x2="150" y2="145" stroke="#FDE047" stroke-width="3"/>
    <polygon points="145,142 155,142 150,152" fill="#FDE047"/>
    <text x="160" y="108" font-size="11" font-weight="700" fill="#FEF08A">Lặn: -120 m</text>
    <line x1="340" y1="145" x2="340" y2="98" stroke="#4ADE80" stroke-width="3"/>
    <polygon points="335,102 345,102 340,92" fill="#4ADE80"/>
    <text x="352" y="125" font-size="11.5" font-weight="700" fill="#86EFAC">Thả 3 quả nặng (-3 × -15 = +45 m)</text>
    <rect x="330" y="152" width="210" height="48" rx="8" fill="#0F172A" opacity="0.88" stroke="#38BDF8"/>
    <text x="435" y="172" font-size="12" font-weight="700" fill="#38BDF8" text-anchor="middle">Phép toán: (-120) - (-45)</text>
    <text x="435" y="190" font-size="12.5" font-weight="800" fill="#4ADE80" text-anchor="middle">= -120 + 45 = -75 m</text>
  </g>
</svg>"""

    def _svg_num_g6_03_orange_mixture(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#FFF7ED" stroke="#FB923C" stroke-width="1.5"/>
    <!-- Beaker 1 -->
    <rect x="60" y="50" width="90" height="120" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2.5"/>
    <rect x="63" y="86" width="84" height="81" rx="4" fill="#FDBA74"/>
    <rect x="63" y="135" width="84" height="32" rx="4" fill="#F97316"/>
    <!-- Beaker 2 -->
    <rect x="230" y="40" width="100" height="130" rx="8" fill="#FFFFFF" stroke="#475569" stroke-width="2.5"/>
    <rect x="233" y="62" width="94" height="105" rx="4" fill="#FED7AA"/>
    <rect x="233" y="135" width="94" height="32" rx="4" fill="#F97316"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="105" y="36" font-size="12" font-weight="700" fill="#9A3412" text-anchor="middle">Bình ban đầu: 400 ml</text>
    <text x="105" y="155" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle">Cam nguyên chất: 100 ml</text>
    <text x="105" y="192" font-size="12" font-weight="700" fill="#C2410C" text-anchor="middle">Tỉ lệ: 100/400 = 25%</text>
    <text x="190" y="110" font-size="18" font-weight="800" fill="#EA580C" text-anchor="middle">+ 100 ml nước</text>
    <text x="280" y="28" font-size="12" font-weight="700" fill="#9A3412" text-anchor="middle">Bình sau pha: 500 ml</text>
    <text x="280" y="155" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle">Bất biến: 100 ml cam</text>
    <text x="280" y="192" font-size="12" font-weight="700" fill="#15803D" text-anchor="middle">Tỉ lệ mới: 100/500 = 20%</text>
    <rect x="360" y="55" width="180" height="115" rx="10" fill="#FFFFFF" stroke="#F97316" stroke-width="1.5"/>
    <text x="450" y="80" font-size="12" font-weight="800" fill="#9A3412" text-anchor="middle">ĐẠI LƯỢNG BẤT BIẾN</text>
    <text x="450" y="104" font-size="11.5" fill="#334155" text-anchor="middle">Thêm nước lọc làm tăng</text>
    <text x="450" y="122" font-size="11.5" fill="#334155" text-anchor="middle">tổng thể tích dung dịch,</text>
    <text x="450" y="140" font-size="11.5" font-weight="700" fill="#EA580C" text-anchor="middle">nhưng lượng cốt cam</text>
    <text x="450" y="156" font-size="11.5" font-weight="700" fill="#EA580C" text-anchor="middle">giữ nguyên = 100 ml!</text>
  </g>
</svg>"""

    def _svg_num_g7_04_sqrt2_spiral(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <!-- Unit square and rotated square of area 2 -->
    <rect x="65" y="95" width="70" height="70" fill="#DBEAFE" stroke="#1D4ED8" stroke-width="2"/>
    <polygon points="65,95 135,95 135,165" fill="#93C5FD" opacity="0.6"/>
    <polygon points="65,95 135,165 205,95 135,25" fill="#FEF3C7" fill-opacity="0.75" stroke="#D97706" stroke-width="2.2"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="100" y="182" font-size="11.5" font-weight="700" fill="#1E40AF" text-anchor="middle">Cạnh = 1 dm (S = 1)</text>
    <text x="135" y="88" font-size="12" font-weight="800" fill="#B45309" text-anchor="middle">S_lớn = 2 dm² ⇒ Cạnh d = √2</text>
    <!-- Number line with compass arc -->
    <line x1="255" y1="150" x2="530" y2="150" stroke="#0F172A" stroke-width="2.2"/>
    <circle cx="280" cy="150" r="4" fill="#0F172A"/>
    <text x="280" y="172" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">0</text>
    <circle cx="380" cy="150" r="4" fill="#1D4ED8"/>
    <text x="380" y="172" font-size="12" font-weight="700" fill="#1D4ED8" text-anchor="middle">1</text>
    <circle cx="480" cy="150" r="4" fill="#0F172A"/>
    <text x="480" y="172" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">2</text>
    <!-- Square on number line -->
    <rect x="280" y="50" width="100" height="100" fill="none" stroke="#94A3B8" stroke-dasharray="4,4" stroke-width="1.5"/>
    <line x1="280" y1="150" x2="380" y2="50" stroke="#DC2626" stroke-width="2.5"/>
    <path d="M 380 50 A 141.4 141.4 0 0 1 421.4 150" fill="none" stroke="#DC2626" stroke-width="2" stroke-dasharray="5,3"/>
    <circle cx="421.4" cy="150" r="5" fill="#DC2626"/>
    <text x="421.4" y="192" font-size="12.5" font-weight="800" fill="#DC2626" text-anchor="middle">√2 ≈ 1,4142...</text>
  </g>
</svg>"""

    def _svg_alg_g7_05_alloy_proportion(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5"/>
    <!-- 3 parts Copper, 2 parts Zinc -->
    <rect x="40" y="58" width="65" height="36" rx="4" fill="#EA580C" stroke="#9A3412" stroke-width="1.5"/>
    <rect x="110" y="58" width="65" height="36" rx="4" fill="#EA580C" stroke="#9A3412" stroke-width="1.5"/>
    <rect x="180" y="58" width="65" height="36" rx="4" fill="#EA580C" stroke="#9A3412" stroke-width="1.5"/>
    <rect x="40" y="118" width="65" height="36" rx="4" fill="#38BDF8" stroke="#0369A1" stroke-width="1.5"/>
    <rect x="110" y="118" width="65" height="36" rx="4" fill="#38BDF8" stroke="#0369A1" stroke-width="1.5"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="40" y="45" font-size="12" font-weight="700" fill="#9A3412">Đồng (x): 3 phần bằng nhau</text>
    <text x="40" y="110" font-size="12" font-weight="700" fill="#0369A1">Kẽm (y): 2 phần bằng nhau</text>
    <text x="142" y="185" font-size="12.5" font-weight="800" fill="#166534" text-anchor="middle">Tổng số phần: 3 + 2 = 5 phần ⇔ 150 gam</text>
    <rect x="285" y="42" width="245" height="140" rx="10" fill="#FFFFFF" stroke="#15803D" stroke-width="1.8"/>
    <text x="407" y="70" font-size="13" font-weight="800" fill="#166534" text-anchor="middle">DÃY TỈ SỐ BẰNG NHAU</text>
    <text x="407" y="102" font-size="13.5" font-weight="700" fill="#0F172A" text-anchor="middle">x / 3 = y / 2 = (x + y) / (3 + 2)</text>
    <text x="407" y="130" font-size="13.5" font-weight="800" fill="#EA580C" text-anchor="middle">= 150 / 5 = 30 (gam/phần)</text>
    <text x="407" y="160" font-size="12.5" font-weight="700" fill="#0369A1" text-anchor="middle">⇒ x = 90 g Đồng; y = 60 g Kẽm</text>
  </g>
</svg>"""

    def _svg_alg_g8_06_taxi_intersection(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#0F172A"/>
    <g stroke="#1E293B" stroke-width="1">
      <line x1="60" y1="40" x2="340" y2="40"/><line x1="60" y1="80" x2="340" y2="80"/>
      <line x1="60" y1="120" x2="340" y2="120"/><line x1="60" y1="160" x2="340" y2="160"/>
      <line x1="120" y1="20" x2="120" y2="190"/><line x1="180" y1="20" x2="180" y2="190"/>
      <line x1="240" y1="20" x2="240" y2="190"/><line x1="300" y1="20" x2="300" y2="190"/>
    </g>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <!-- Axes -->
    <line x1="60" y1="185" x2="345" y2="185" stroke="#94A3B8" stroke-width="2"/>
    <line x1="60" y1="185" x2="60" y2="22" stroke="#94A3B8" stroke-width="2"/>
    <!-- Line A: y = 12x + 10 -->
    <line x1="60" y1="165" x2="320" y2="45" stroke="#38BDF8" stroke-width="3"/>
    <!-- Line B: y = 10x + 20 -->
    <line x1="60" y1="145" x2="320" y2="55" stroke="#F59E0B" stroke-width="3"/>
    <!-- Intersection at x = 5 km, y = 70k -->
    <circle cx="190" cy="105" r="6" fill="#4ADE80" stroke="#FFFFFF" stroke-width="2"/>
    <line x1="190" y1="105" x2="190" y2="185" stroke="#4ADE80" stroke-dasharray="4,3"/>
    <text x="190" y="203" font-size="11.5" font-weight="700" fill="#4ADE80" text-anchor="middle">x₀ = 5 km (Hòa vốn)</text>
    <rect x="355" y="34" width="185" height="152" rx="10" fill="#1E293B" stroke="#334155"/>
    <text x="447" y="58" font-size="12.5" font-weight="800" fill="#F8FAFC" text-anchor="middle">SO SÁNH CƯỚC TAXI</text>
    <text x="368" y="84" font-size="11.5" font-weight="700" fill="#38BDF8">• Hãng A: y₁ = 12x + 10</text>
    <text x="368" y="106" font-size="11.5" font-weight="700" fill="#F59E0B">• Hãng B: y₂ = 10x + 20</text>
    <text x="368" y="134" font-size="11.5" fill="#E2E8F0">Giao điểm: 12x + 10 = 10x + 20</text>
    <text x="368" y="156" font-size="12" font-weight="800" fill="#4ADE80">⇒ x = 5 km; y = 70 nghìn</text>
  </g>
</svg>"""

    def _svg_alg_g8_07_rate_balance_3d(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
    <!-- Balance Pillar & Beam -->
    <polygon points="155,190 185,190 170,105" fill="#475569"/>
    <line x1="65" y1="105" x2="275" y2="105" stroke="#FBBF24" stroke-width="5"/>
    <rect x="42" y="115" width="75" height="36" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="2"/>
    <rect x="222" y="115" width="75" height="36" rx="6" fill="#1E293B" stroke="#10B981" stroke-width="2"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="170" y="34" font-size="12.5" font-weight="800" fill="#38BDF8" text-anchor="middle">CÂN LẬP LUẬN ĐẠI SỐ (KHÓA GIẢ THIẾT Δ = 1)</text>
    <text x="79" y="138" font-size="12" font-weight="700" fill="#38BDF8" text-anchor="middle">60/x - 60/(x+3)</text>
    <text x="259" y="138" font-size="12.5" font-weight="800" fill="#10B981" text-anchor="middle">Δ = 1 tấn/xe</text>
    <rect x="320" y="32" width="220" height="160" rx="10" fill="#1E293B" stroke="#334155"/>
    <text x="430" y="56" font-size="12" font-weight="800" fill="#FDE047" text-anchor="middle">KHỬ MẪU &amp; LỌC NGHIỆM BẬC HAI</text>
    <text x="430" y="82" font-size="12" fill="#F8FAFC" text-anchor="middle">60(x + 3) - 60x = x(x + 3)</text>
    <text x="430" y="106" font-size="13" font-weight="800" fill="#38BDF8" text-anchor="middle">⇔ x² + 3x - 180 = 0</text>
    <text x="430" y="134" font-size="12" font-weight="700" fill="#4ADE80" text-anchor="middle">✓ x₁ = 12 (Nhận vì x &gt; 0)</text>
    <text x="430" y="158" font-size="12" font-weight="700" fill="#F87171" text-anchor="middle">✗ x₂ = -15 (Loại nghiệm âm)</text>
  </g>
</svg>"""

    def _svg_alg_g9_08_dual_pipe_hydro(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.5"/>
    <!-- Hydro Tank -->
    <rect x="65" y="55" width="130" height="130" rx="8" fill="#FFFFFF" stroke="#0369A1" stroke-width="2.5"/>
    <rect x="68" y="95" width="124" height="87" rx="5" fill="#38BDF8" opacity="0.75"/>
    <!-- Pipe 1 & Pipe 2 -->
    <rect x="25" y="65" width="45" height="12" fill="#0284C7"/>
    <rect x="190" y="65" width="45" height="12" fill="#0D9488"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="130" y="36" font-size="12" font-weight="800" fill="#0369A1" text-anchor="middle">Bể chứa 1 đơn vị thể tích</text>
    <text x="130" y="142" font-size="12" font-weight="800" fill="#0F172A" text-anchor="middle">Năng suất cộng hưởng</text>
    <rect x="255" y="34" width="280" height="154" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
    <text x="395" y="58" font-size="12.5" font-weight="800" fill="#0369A1" text-anchor="middle">BẢN CHẤT BÀI TOÁN HAI VÒI NƯỚC</text>
    <text x="395" y="84" font-size="11.5" fill="#B91C1C" font-anchor="middle" text-anchor="middle">✗ Sai lầm: Cộng thời gian x + y = T</text>
    <text x="395" y="110" font-size="12.5" font-weight="800" fill="#15803D" text-anchor="middle">✓ Đúng: Cộng phần bể chảy trong 1 giờ!</text>
    <text x="395" y="138" font-size="13.5" font-weight="800" fill="#0F172A" text-anchor="middle">1/x + 1/y = 1/T</text>
    <text x="395" y="166" font-size="11.5" font-weight="700" fill="#0369A1" text-anchor="middle">Với x = 4h, y = 6h ⇒ 1/4 + 1/6 = 5/12 ⇒ T = 2,4h</text>
  </g>
</svg>"""

    def _svg_alg_g9_09_parabola_bridge(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#0F172A"/>
    <!-- Water river -->
    <rect x="30" y="165" width="300" height="35" rx="4" fill="#0369A1" opacity="0.6"/>
    <!-- Cargo Boat clearance box -->
    <rect x="130" y="105" width="100" height="60" fill="#10B981" fill-opacity="0.28" stroke="#10B981" stroke-width="2" stroke-dasharray="4,3"/>
    <!-- Parabolic Arch y = -0.05 x^2 -->
    <path d="M 60 165 Q 180 -15 300 165" fill="none" stroke="#F59E0B" stroke-width="4"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <line x1="180" y1="25" x2="180" y2="195" stroke="#94A3B8" stroke-dasharray="3,3"/>
    <circle cx="180" cy="75" r="5" fill="#FDE047"/>
    <text x="180" y="65" font-size="11.5" font-weight="700" fill="#FDE047" text-anchor="middle">Đỉnh O(0; 0) cao 9 m</text>
    <text x="180" y="140" font-size="11" font-weight="700" fill="#86EFAC" text-anchor="middle">Tàu rộng 8m, cao 6m</text>
    <rect x="345" y="34" width="195" height="154" rx="10" fill="#1E293B" stroke="#334155"/>
    <text x="442" y="58" font-size="12" font-weight="800" fill="#FBBF24" text-anchor="middle">VÒM CẦU PARABOL y = ax²</text>
    <text x="442" y="84" font-size="11.5" fill="#E2E8F0" text-anchor="middle">Chân cầu rộng 24m ⇒ x = ±12</text>
    <text x="442" y="106" font-size="11.5" fill="#38BDF8" text-anchor="middle">-9 = a·12² ⇒ a = -1/16</text>
    <text x="442" y="132" font-size="11.5" fill="#E2E8F0" text-anchor="middle">Tại mép tàu x = 4m: y = -1 m</text>
    <text x="442" y="156" font-size="12" font-weight="800" fill="#4ADE80" text-anchor="middle">Độ thoáng = 9 - 1 = 8m &gt; 6m ✓</text>
  </g>
</svg>"""

    def _svg_geo_g6_10_lshape_garden_h07(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F0FDF4" stroke="#16A34A" stroke-width="1.5"/>
    <!-- L-shaped garden -->
    <polygon points="45,40 225,40 225,105 155,105 155,175 45,175" fill="#86EFAC" stroke="#15803D" stroke-width="2.5"/>
    <!-- Cut corner ghost -->
    <rect x="155" y="105" width="70" height="70" fill="#FEE2E2" stroke="#DC2626" stroke-width="2" stroke-dasharray="5,4"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="135" y="30" font-size="12" font-weight="700" fill="#166534" text-anchor="middle">Chiều dài 12 m</text>
    <text x="25" y="110" font-size="12" font-weight="700" fill="#166534" text-anchor="middle" transform="rotate(-90 25 110)">Rộng 10 m</text>
    <text x="190" y="142" font-size="11" font-weight="700" fill="#B91C1C" text-anchor="middle">Khoét 4m×4m</text>
    <rect x="275" y="35" width="260" height="150" rx="10" fill="#FFFFFF" stroke="#16A34A" stroke-width="1.5"/>
    <text x="405" y="60" font-size="12.5" font-weight="800" fill="#166534" text-anchor="middle">BẤT BIẾN CHU VI HÌNH CHỮ L (H07)</text>
    <text x="405" y="88" font-size="12" fill="#0F172A" text-anchor="middle">• Diện tích GIẢM phần khoét:</text>
    <text x="405" y="108" font-size="12.5" font-weight="700" fill="#0369A1" text-anchor="middle">S = 12×10 - 4×4 = 104 m²</text>
    <text x="405" y="136" font-size="12" fill="#0F172A" text-anchor="middle">• Chu vi KHÔNG ĐỔI (dời cạnh ra góc):</text>
    <text x="405" y="158" font-size="12.5" font-weight="800" fill="#15803D" text-anchor="middle">P = 2 × (12 + 10) = 44 m!</text>
  </g>
</svg>"""

    def _svg_geo_g8_11_pythagoras_cutpaste(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F8FAFC" stroke="#2563EB" stroke-width="1.5"/>
    <!-- Left frame (a+b)^2 with tilted c^2 -->
    <rect x="45" y="42" width="140" height="140" fill="#DBEAFE" stroke="#1E40AF" stroke-width="2"/>
    <polygon points="45,102 105,42 185,122 125,182" fill="#FEF08A" stroke="#CA8A04" stroke-width="2.2"/>
    <!-- Right frame (a+b)^2 with a^2 and b^2 -->
    <rect x="315" y="42" width="140" height="140" fill="#DBEAFE" stroke="#1E40AF" stroke-width="2"/>
    <rect x="315" y="42" width="60" height="60" fill="#FCA5A5" stroke="#DC2626" stroke-width="2"/>
    <rect x="375" y="102" width="80" height="80" fill="#86EFAC" stroke="#16A34A" stroke-width="2"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="115" y="118" font-size="15" font-weight="800" fill="#854D0E" text-anchor="middle">c²</text>
    <text x="250" y="110" font-size="13" font-weight="800" fill="#1D4ED8" text-anchor="middle">Trượt 4 Δ vuông ⇒</text>
    <text x="345" y="77" font-size="14" font-weight="800" fill="#991B1B" text-anchor="middle">a²</text>
    <text x="415" y="147" font-size="14" font-weight="800" fill="#166534" text-anchor="middle">b²</text>
    <text x="280" y="204" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle">Cùng khung (a+b)² trừ 4 tam giác vuông ⇒ a² + b² = c²</text>
  </g>
</svg>"""

    def _svg_geo_g8_12_thales_shadow_tower(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#FFFBEB" stroke="#D97706" stroke-width="1.5"/>
    <circle cx="42" cy="36" r="16" fill="#F59E0B"/>
    <!-- Tower -->
    <polygon points="105,175 135,175 125,45 115,45" fill="#B45309"/>
    <!-- Stick -->
    <line x1="340" y1="175" x2="340" y2="135" stroke="#15803D" stroke-width="4"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <line x1="60" y1="175" x2="480" y2="175" stroke="#78350F" stroke-width="2.5"/>
    <!-- Sun rays -->
    <line x1="120" y1="45" x2="290" y2="175" stroke="#EA580C" stroke-width="2" stroke-dasharray="5,3"/>
    <line x1="340" y1="135" x2="392" y2="175" stroke="#EA580C" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="95" y="112" font-size="12" font-weight="800" fill="#92400E" text-anchor="end">Tháp h = ?</text>
    <text x="205" y="194" font-size="11.5" font-weight="700" fill="#B45309" text-anchor="middle">Bóng tháp = 18 m</text>
    <text x="332" y="155" font-size="11.5" font-weight="700" fill="#15803D" text-anchor="end">Cọc 2 m</text>
    <text x="366" y="194" font-size="11.5" font-weight="700" fill="#15803D" text-anchor="middle">Bóng 1,5 m</text>
    <rect x="398" y="38" width="146" height="100" rx="8" fill="#FFFFFF" stroke="#D97706"/>
    <text x="471" y="62" font-size="12" font-weight="800" fill="#92400E" text-anchor="middle">TỈ SỐ ĐỒNG DẠNG</text>
    <text x="471" y="88" font-size="12.5" font-weight="700" fill="#0F172A" text-anchor="middle">h / 2 = 18 / 1,5</text>
    <text x="471" y="115" font-size="13" font-weight="800" fill="#15803D" text-anchor="middle">⇒ h = 24 m</text>
  </g>
</svg>"""

    def _svg_geo_g9_13_cylinder_net_3d(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F8FAFC" stroke="#0284C7" stroke-width="1.5"/>
    <!-- 3D Cylinder -->
    <rect x="55" y="65" width="80" height="100" fill="#BAE6FD" stroke="#0369A1" stroke-width="2"/>
    <ellipse cx="95" cy="65" rx="40" ry="14" fill="#7DD3FC" stroke="#0369A1" stroke-width="2"/>
    <ellipse cx="95" cy="165" rx="40" ry="14" fill="#38BDF8" stroke="#0369A1" stroke-width="2"/>
    <!-- Unrolled Net -->
    <rect x="240" y="65" width="190" height="100" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
    <circle cx="335" cy="36" r="24" fill="#7DD3FC" stroke="#0369A1" stroke-width="2"/>
    <circle cx="335" cy="192" r="24" fill="#7DD3FC" stroke="#0369A1" stroke-width="2"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="95" y="120" font-size="12" font-weight="700" fill="#0C4A6E" text-anchor="middle">h = 10 cm</text>
    <text x="95" y="68" font-size="11" font-weight="700" fill="#0C4A6E" text-anchor="middle">R = 4 cm</text>
    <text x="188" y="115" font-size="13" font-weight="800" fill="#0284C7" text-anchor="middle">Trải phẳng ⇒</text>
    <text x="335" y="112" font-size="12.5" font-weight="800" fill="#92400E" text-anchor="middle">Chiều dài = Chu vi đáy = 2πR</text>
    <text x="335" y="134" font-size="12.5" font-weight="800" fill="#15803D" text-anchor="middle">S_xq = (2πR) · h = 80π cm²</text>
  </g>
</svg>"""

    def _svg_stat_g7_14_mean_median_seesaw(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F5F3FF" stroke="#7C3AED" stroke-width="1.5"/>
    <!-- Seesaw beam -->
    <line x1="45" y1="135" x2="515" y2="135" stroke="#4C1D95" stroke-width="5"/>
    <!-- Blocks for data: 4, 5, 6, 7 and outlier 28 -->
    <rect x="75" y="105" width="26" height="30" rx="4" fill="#60A5FA"/>
    <rect x="110" y="105" width="26" height="30" rx="4" fill="#60A5FA"/>
    <rect x="145" y="105" width="26" height="30" rx="4" fill="#10B981"/>
    <rect x="180" y="105" width="26" height="30" rx="4" fill="#60A5FA"/>
    <rect x="465" y="95" width="36" height="40" rx="4" fill="#EF4444"/>
    <!-- Fulcrum at Mean = 10 -->
    <polygon points="245,175 285,175 265,135" fill="#F59E0B" stroke="#B45309" stroke-width="2"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="158" y="92" font-size="11.5" font-weight="800" fill="#047857" text-anchor="middle">Trung vị M_e = 6 (Ổn định)</text>
    <text x="265" y="196" font-size="12" font-weight="800" fill="#B45309" text-anchor="middle">▲ Trọng tâm Trung bình x̄ = 10 (Bị kéo lệch!)</text>
    <text x="483" y="84" font-size="11.5" font-weight="800" fill="#DC2626" text-anchor="middle">Ngoại lai = 28</text>
    <text x="280" y="38" font-size="13" font-weight="800" fill="#4C1D95" text-anchor="middle">ĐÒN BẨY DỮ LIỆU: TRUNG BÌNH CỘNG LÀ TÂM KHỐI LƯỢNG VẬT LÝ</text>
  </g>
</svg>"""

    def _svg_stat_g8_15_monte_carlo_convergence(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#F8FAFC" stroke="#0D9488" stroke-width="1.5"/>
    <line x1="65" y1="175" x2="515" y2="175" stroke="#334155" stroke-width="2"/>
    <line x1="65" y1="35" x2="65" y2="175" stroke="#334155" stroke-width="2"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <!-- Theoretical probability line P = 0.5 -->
    <line x1="65" y1="105" x2="515" y2="105" stroke="#DC2626" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="510" y="96" font-size="11.5" font-weight="800" fill="#DC2626" text-anchor="end">Xác suất lý thuyết P(A) = 0,50</text>
    <!-- Empirical curve -->
    <path d="M 65 45 L 110 145 L 155 82 L 210 122 L 270 95 L 340 112 L 420 102 L 510 105" fill="none" stroke="#0D9488" stroke-width="3"/>
    <text x="290" y="32" font-size="12.5" font-weight="800" fill="#0F766E" text-anchor="middle">LUẬT SỐ LỚN: KHI SỐ PHÉP THỬ N → 1000, k/N HỘI TỤ VỀ P(A)</text>
    <text x="290" y="198" font-size="11.5" font-weight="700" fill="#334155" text-anchor="middle">Số phép thử N (10 → 50 → 200 → 1000 lần tung)</text>
  </g>
</svg>"""

    def _svg_appl_g9_16_garden_path_finance(self) -> str:
        return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 220" width="100%" height="100%">
  <g id="art-layer">
    <rect x="0" y="0" width="560" height="220" rx="12" fill="#ECFDF5" stroke="#059669" stroke-width="1.5"/>
    <!-- Outer garden 20m x 14m -->
    <rect x="40" y="40" width="200" height="140" rx="6" fill="#FDE68A" stroke="#B45309" stroke-width="2"/>
    <!-- Inner flower bed (20-2x)(14-2x) -->
    <rect x="65" y="65" width="150" height="90" rx="4" fill="#4ADE80" stroke="#15803D" stroke-width="2"/>
  </g>
  <g id="math-layer" font-family="Segoe UI, sans-serif">
    <text x="140" y="114" font-size="12" font-weight="800" fill="#064E3B" text-anchor="middle">Vườn hoa: (20 - 2x)(14 - 2x)</text>
    <text x="140" y="56" font-size="11" font-weight="700" fill="#92400E" text-anchor="middle">Lối đi rộng x (m) bao quanh</text>
    <rect x="265" y="38" width="270" height="144" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
    <text x="400" y="62" font-size="12" font-weight="800" fill="#065F46" text-anchor="middle">TỔ HỢP HÌNH HỌC H07 + ĐẠI SỐ BẬC HAI</text>
    <text x="400" y="88" font-size="11.5" fill="#0F172A" text-anchor="middle">Diện tích hoa = 160 m² (0 &lt; x &lt; 7)</text>
    <text x="400" y="112" font-size="12" font-weight="700" fill="#0369A1" text-anchor="middle">(20 - 2x)(14 - 2x) = 160</text>
    <text x="400" y="136" font-size="12.5" font-weight="800" fill="#B45309" text-anchor="middle">⇔ x² - 17x + 30 = 0</text>
    <text x="400" y="162" font-size="12" font-weight="800" fill="#15803D" text-anchor="middle">✓ Nhận x₁ = 2 m | ✗ Loại x₂ = 15 m (&gt; 7)</text>
  </g>
</svg>"""
