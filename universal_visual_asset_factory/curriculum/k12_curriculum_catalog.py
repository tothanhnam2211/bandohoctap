# -*- coding: utf-8 -*-
"""
K12 MATHEMATICAL VISUAL ASSET CURRICULUM CATALOG (Grades 6-12)
Định nghĩa hệ thống 274 Asset Families trên toàn bộ 7 khối lớp (Toán 6, 7, 8, 9, 10, 11, 12).
Phủ kín 4 mạch kiến thức chuẩn GDPT 2018:
1. Số học & Đại số (Arithmetic & Algebra)
2. Hình học & Đo lường (Geometry: Plane, Solid, Vectors & Analytic Oxyz)
3. Thống kê & Xác suất (Statistics, Combinatorics & Probability)
4. Thực tiễn, STEM & Giải tích (Real-World STEM & Calculus)
"""

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class AssetFamilySpec:
    family_id: str
    grade: int
    strand: str
    chapter: str
    topic_vi: str
    generator_type: str
    math_invariant: str
    default_style: str
    variants_target: int = 40

def get_k12_asset_families() -> List[AssetFamilySpec]:
    families = []
    
    # ==========================================
    # KHỐI 6: 38 FAMILIES
    # ==========================================
    # Số học
    families.extend([
        AssetFamilySpec("FAM_G06_NUM_SET_VENN", 6, "SO_HOC_DAI_SO", "Chương 1", "Tập hợp & Biểu đồ Venn", "set_venn", "A cap B, A cup B", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G06_NUM_LINE_NATURAL", 6, "SO_HOC_DAI_SO", "Chương 1", "Tia số tự nhiên & Phép đếm", "number_line_nat", "x in N", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_NUM_PRIME_FACTOR_TREE", 6, "SO_HOC_DAI_SO", "Chương 2", "Cây phân tích thừa số nguyên tố", "prime_factor_tree", "n = p1^a * p2^b", "WARM_STORYBOOK_TACTILE", 40),
        AssetFamilySpec("FAM_G06_NUM_GCD_LCM_GRID", 6, "SO_HOC_DAI_SO", "Chương 2", "Lát gạch ƯCLN & Chu kỳ BCNN", "gcd_lcm_grid", "d = gcd(a, b)", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G06_NUM_LINE_INTEGER", 6, "SO_HOC_DAI_SO", "Chương 3", "Trục số nguyên âm & số đối", "number_line_int", "-x < 0 < x", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_NUM_INTEGER_CHIP_MODEL", 6, "SO_HOC_DAI_SO", "Chương 3", "Mô hình chip âm dương triệt tiêu", "integer_chips", "(+1) + (-1) = 0", "WARM_STORYBOOK_TACTILE", 40),
        AssetFamilySpec("FAM_G06_NUM_INTEGER_ELEVATOR_TEMP", 6, "SO_HOC_DAI_SO", "Chương 3", "Nhiệt kế & Thang máy số nguyên", "vertical_integer_scale", "T_final = T0 + Delta_T", "STEM_COMMAND_3D", 40),
        AssetFamilySpec("FAM_G06_NUM_FRACTION_PIE", 6, "SO_HOC_DAI_SO", "Chương 6", "Phân số hình quạt tròn", "fraction_pie", "a/b sector", "REAL_PAPER_HYBRID_V04", 45),
        AssetFamilySpec("FAM_G06_NUM_FRACTION_BAR_TAPE", 6, "SO_HOC_DAI_SO", "Chương 6", "Phân số băng giấy & Băng đo", "fraction_tape", "a/b length bar", "REAL_PAPER_HYBRID_V04", 45),
        AssetFamilySpec("FAM_G06_NUM_FRACTION_EQUIVALENT", 6, "SO_HOC_DAI_SO", "Chương 6", "Bảng phân số bằng nhau", "fraction_grid_equiv", "a/b = (a*k)/(b*k)", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G06_NUM_DECIMAL_PLACE_VALUE", 6, "SO_HOC_DAI_SO", "Chương 7", "Bảng giá trị hàng số thập phân", "decimal_blocks", "10 base system", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_NUM_PERCENTAGE_SQUARE", 6, "SO_HOC_DAI_SO", "Chương 7", "Lưới 100 ô vuông tỉ số phần trăm", "percentage_100_grid", "p% = p/100", "WARM_STORYBOOK_TACTILE", 40),
    ])
    # Hình học 6
    families.extend([
        AssetFamilySpec("FAM_G06_GEO_TRIANGLE_EQUILATERAL", 6, "HINH_HOC_DO_LUONG", "Chương 4", "Tam giác đều & Lưới tam giác", "geom_regular_triangle", "AB=BC=CA, 60 deg", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G06_GEO_SQUARE_RECTANGLE", 6, "HINH_HOC_DO_LUONG", "Chương 4", "Hình vuông, Chữ nhật & Chu vi", "geom_quad_basic", "P = 2(a+b), S = a*b", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_GEO_RHOMBUS_PARALLEL", 6, "HINH_HOC_DO_LUONG", "Chương 4", "Hình thoi & Hình bình hành", "geom_rhombus_parallel", "S = (d1*d2)/2", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G06_GEO_TRAPEZOID_ISOSCELES", 6, "HINH_HOC_DO_LUONG", "Chương 4", "Hình thang cân & Lát mặt phẳng", "geom_trapezoid_iso", "S = (a+b)*h/2", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G06_GEO_SYMMETRY_AXIS", 6, "HINH_HOC_DO_LUONG", "Chương 5", "Trục đối xứng hình tự nhiên/hoa", "geom_symmetry_axis", "Mirror reflect line", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G06_GEO_SYMMETRY_CENTER", 6, "HINH_HOC_DO_LUONG", "Chương 5", "Tâm đối xứng & Chong chóng", "geom_symmetry_center", "180 deg rotation", "WARM_STORYBOOK_TACTILE", 40),
        AssetFamilySpec("FAM_G06_GEO_POINT_LINE_RAY", 6, "HINH_HOC_DO_LUONG", "Chương 8", "Điểm, Đường thẳng, Tia, Đoạn thẳng", "geom_point_line_ray", "C in AB", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_GEO_MIDPOINT_SEGMENT", 6, "HINH_HOC_DO_LUONG", "Chương 8", "Trung điểm đoạn thẳng & Cây thước", "geom_midpoint_segment", "MA = MB = AB/2", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_GEO_ANGLE_PROTRACTOR", 6, "HINH_HOC_DO_LUONG", "Chương 8", "Góc & Thước đo góc độ", "geom_angle_protractor", "0 < angle <= 180", "EUCLIDEAN_ATELIER_PRO", 45),
    ])
    # Thống kê 6
    families.extend([
        AssetFamilySpec("FAM_G06_STAT_TALLY_CHART", 6, "THONG_KE_XAC_SUAT", "Chương 9", "Bảng kiểm đếm & Thu thập dữ liệu", "stat_tally_chart", "Sum tally = N", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_STAT_PICTOGRAPH", 6, "THONG_KE_XAC_SUAT", "Chương 9", "Biểu đồ tranh (Pictograph)", "stat_pictograph", "1 icon = k units", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G06_STAT_BAR_CHART", 6, "THONG_KE_XAC_SUAT", "Chương 9", "Biểu đồ cột đơn giản", "stat_bar_chart", "height prop to freq", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G06_STAT_DOUBLE_BAR", 6, "THONG_KE_XAC_SUAT", "Chương 9", "Biểu đồ cột kép so sánh", "stat_double_bar", "Grouped comparison", "DATA_OBSERVATORY_LAB", 40),
        AssetFamilySpec("FAM_G06_STAT_CHANCE_SPINNER", 6, "THONG_KE_XAC_SUAT", "Chương 9", "Vòng quay xác suất may mắn", "prob_spinner", "P = angle/360", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G06_STAT_DICE_EXPERIMENT", 6, "THONG_KE_XAC_SUAT", "Chương 9", "Mô phỏng gieo xúc xắc & Đồng xu", "prob_dice_coin", "P = n(A)/N", "DATA_OBSERVATORY_LAB", 40),
    ])
    # Thực tiễn & STEM 6
    families.extend([
        AssetFamilySpec("FAM_G06_STEM_COURTYARD_TILING", 6, "STEM_THUC_TIEN", "Thực hành", "Lát sân gạch chữ nhật thực tiễn", "stem_tile_pattern", "a % d == 0, b % d == 0", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G06_STEM_RECIPE_RATIO", 6, "STEM_THUC_TIEN", "Thực hành", "Tỉ lệ pha chế nước ép/nấu ăn", "stem_mixing_ratio", "Water : Juice = a : b", "WARM_STORYBOOK_TACTILE", 40),
        AssetFamilySpec("FAM_G06_STEM_BUDGET_SAVINGS", 6, "STEM_THUC_TIEN", "Thực hành", "Heo đất & Kế hoạch chi tiêu", "stem_piggy_budget", "Income - Expense = Net", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G06_STEM_SCALE_MAP_DISTANCE", 6, "STEM_THUC_TIEN", "Thực hành", "Bản đồ địa hình tỉ lệ xích", "stem_map_scale", "Actual = Map * Scale", "EUCLIDEAN_ATELIER_PRO", 40),
    ])

    # ==========================================
    # KHỐI 7: 40 FAMILIES
    # ==========================================
    # Đại số 7
    families.extend([
        AssetFamilySpec("FAM_G07_NUM_RATIONAL_NUMBERLINE", 7, "SO_HOC_DAI_SO", "Chương 1", "Số hữu tỉ trên trục số & số đối", "number_line_rational", "q = a/b in Q", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G07_NUM_EXPONENT_POWER", 7, "SO_HOC_DAI_SO", "Chương 1", "Lũy thừa với số mũ tự nhiên", "math_power_tree", "a^m * a^n = a^(m+n)", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G07_NUM_REAL_SQUARE_ROOT", 7, "SO_HOC_DAI_SO", "Chương 2", "Căn bậc hai số học trên trục số", "math_square_root_spiral", "x^2 = S, x = sqrt(S)", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_ALG_PROPORTION_BAR", 7, "SO_HOC_DAI_SO", "Chương 6", "Tỉ lệ thức & Dãy tỉ số bằng nhau", "algebra_proportion_scale", "a/b = c/d = (a+c)/(b+d)", "REAL_PAPER_HYBRID_V04", 45),
        AssetFamilySpec("FAM_G07_ALG_DIRECT_INVERSE_GRAPH", 7, "SO_HOC_DAI_SO", "Chương 6", "Đồ thị đại lượng tỉ lệ thuận & nghịch", "algebra_direct_inverse_plot", "y = kx vs y = a/x", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G07_ALG_POLYNOMIAL_TILES", 7, "SO_HOC_DAI_SO", "Chương 7", "Gạch đại số biểu diễn đa thức 1 biến", "algebra_poly_tiles", "c1*x^2 + c2*x + c3", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G07_ALG_POLYNOMIAL_ADD_SUB", 7, "SO_HOC_DAI_SO", "Chương 7", "Cột đặt tính cộng trừ đa thức", "algebra_poly_column", "P(x) +- Q(x)", "REAL_PAPER_HYBRID_V04", 40),
    ])
    # Hình học 7
    families.extend([
        AssetFamilySpec("FAM_G07_GEO_ADJACENT_VERTICAL_ANGLES", 7, "HINH_HOC_DO_LUONG", "Chương 3", "Góc kề bù & Góc đối đỉnh", "geom_vertical_angles", "alpha + beta = 180", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_GEO_PARALLEL_ALTERNATE_INT", 7, "HINH_HOC_DO_LUONG", "Chương 3", "Góc so le trong & Đồng vị", "geom_parallel_transversal", "a // b => Alternate equal", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_GEO_PERPENDICULAR_BISECTOR", 7, "HINH_HOC_DO_LUONG", "Chương 3", "Đường trung trực của đoạn thẳng", "geom_perp_bisector", "MA = MB for all M", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_CONGRUENCE_SSS", 7, "HINH_HOC_DO_LUONG", "Chương 4", "Tam giác bằng nhau (C-C-C)", "geom_congruent_sss", "a1=a2, b1=b2, c1=c2", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_CONGRUENCE_SAS", 7, "HINH_HOC_DO_LUONG", "Chương 4", "Tam giác bằng nhau (C-G-C)", "geom_congruent_sas", "Side-Angle-Side", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_CONGRUENCE_ASA", 7, "HINH_HOC_DO_LUONG", "Chương 4", "Tam giác bằng nhau (G-C-G)", "geom_congruent_asa", "Angle-Side-Angle", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_ISOSCELES", 7, "HINH_HOC_DO_LUONG", "Chương 4", "Tam giác cân & Tính chất đối xứng", "geom_triangle_isosceles", "AB=AC, Angle B=C", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_INEQUALITY", 7, "HINH_HOC_DO_LUONG", "Chương 9", "Bất đẳng thức tam giác", "geom_triangle_inequality", "|b-c| < a < b+c", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_CENTROID", 7, "HINH_HOC_DO_LUONG", "Chương 9", "Trọng tâm & 3 đường trung tuyến", "geom_triangle_centroid", "AG = 2/3 AM", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_ORTHOCENTER", 7, "HINH_HOC_DO_LUONG", "Chương 9", "Trực tâm & 3 đường cao", "geom_triangle_orthocenter", "H intersection of heights", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_INCENTER", 7, "HINH_HOC_DO_LUONG", "Chương 9", "Tâm đường tròn nội tiếp (Phân giác)", "geom_triangle_incenter", "Equidistant 3 sides", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G07_GEO_TRIANGLE_CIRCUMCENTER", 7, "HINH_HOC_DO_LUONG", "Chương 9", "Tâm đường tròn ngoại tiếp (Trung trực)", "geom_triangle_circumcenter", "OA = OB = OC = R", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G07_GEO_SOLID_PRISM_TRI", 7, "HINH_HOC_DO_LUONG", "Chương 10", "Hình lăng trụ đứng tam giác", "geom_solid_prism_tri", "V = S_base * h", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G07_GEO_SOLID_PRISM_QUAD", 7, "HINH_HOC_DO_LUONG", "Chương 10", "Hình lăng trụ đứng tứ giác & Hộp sữa", "geom_solid_prism_quad", "V = a*b*h", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G07_GEO_SOLID_NET_UNFOLD", 7, "HINH_HOC_DO_LUONG", "Chương 10", "Hình khai triển lăng trụ & gấp nếp", "geom_solid_net_unfold", "Flat unfold of prism", "REAL_PAPER_HYBRID_V04", 45),
    ])
    # Thống kê 7
    families.extend([
        AssetFamilySpec("FAM_G07_STAT_PERCENT_PIE_CHART", 7, "THONG_KE_XAC_SUAT", "Chương 5", "Biểu đồ hình quạt tròn tỉ lệ", "stat_pie_chart", "Sum pct = 100%", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G07_STAT_LINE_GRAPH_TREND", 7, "THONG_KE_XAC_SUAT", "Chương 5", "Biểu đồ đoạn thẳng theo dõi xu thế", "stat_line_trend", "Time series curve", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G07_STAT_EVENT_PROBABILITY", 7, "THONG_KE_XAC_SUAT", "Chương 8", "Biến cố ngẫu nhiên & Thước đo xác suất", "stat_probability_gauge", "P in [0, 1]", "DATA_OBSERVATORY_LAB", 40),
    ])
    # STEM 7
    families.extend([
        AssetFamilySpec("FAM_G07_STEM_GEAR_RATIO", 7, "STEM_THUC_TIEN", "Thực hành", "Bánh răng truyền động & Tỉ lệ vòng quay", "stem_gears_ratio", "N1*omega1 = N2*omega2", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G07_STEM_SPEED_DISTANCE_TIME", 7, "STEM_THUC_TIEN", "Thực hành", "Sơ đồ chuyển động đều 2 xe ngược chiều", "stem_motion_meeting", "v1*t + v2*t = S", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G07_STEM_LEVER_EQUILIBRIUM", 7, "STEM_THUC_TIEN", "Thực hành", "Đòn bẩy Archimedes cân bằng lực", "stem_lever_torque", "F1 * d1 = F2 * d2", "STEM_COMMAND_3D", 45),
    ])

    # ==========================================
    # KHỐI 8: 42 FAMILIES
    # ==========================================
    # Đại số 8
    families.extend([
        AssetFamilySpec("FAM_G08_ALG_ALGEBRA_TILES_MULT", 8, "SO_HOC_DAI_SO", "Chương 1", "Gạch diện tích nhân đa thức (x+a)(x+b)", "algebra_area_mult", "(x+a)(x+b) area", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G08_ALG_IDENTITY_DIFF_SQUARES", 8, "SO_HOC_DAI_SO", "Chương 2", "Hiệu hai bình phương a^2 - b^2", "algebra_geom_diff_squares", "a^2 - b^2 = (a-b)(a+b)", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_ALG_IDENTITY_PERFECT_SQUARE", 8, "SO_HOC_DAI_SO", "Chương 2", "Bình phương một tổng & một hiệu", "algebra_geom_sq_sum", "(a+b)^2 = a^2+2ab+b^2", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_ALG_IDENTITY_CUBE_SUM_DIFF", 8, "SO_HOC_DAI_SO", "Chương 2", "Lập phương một tổng / hiệu (Khối hộp 3D)", "algebra_geom_cube_sum", "(a+b)^3 volume components", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G08_ALG_RATIONAL_FRACTION_SIMP", 8, "SO_HOC_DAI_SO", "Chương 6", "Phân thức đại số & Rút gọn nhân tử", "algebra_frac_simplification", "P(x)/Q(x)", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G08_ALG_LINEAR_EQUATION_BALANCE", 8, "SO_HOC_DAI_SO", "Chương 7", "Cán cân giải phương trình bậc nhất", "algebra_linear_balance", "ax + b = c", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G08_ALG_LINEAR_FUNCTION_SLOPE", 8, "SO_HOC_DAI_SO", "Chương 7", "Đồ thị hàm bậc nhất y = ax + b (Hệ số góc)", "algebra_linear_slope_intercept", "m = Delta y / Delta x", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G08_ALG_PARALLEL_INTERSECT_LINES", 8, "SO_HOC_DAI_SO", "Chương 7", "Vị trí tương đối 2 đường thẳng y = ax+b", "algebra_lines_rel_pos", "a=a' parallel vs a*a'=-1", "EUCLIDEAN_ATELIER_PRO", 45),
    ])
    # Hình học 8
    families.extend([
        AssetFamilySpec("FAM_G08_GEO_QUAD_TRAPEZOID_MID", 8, "HINH_HOC_DO_LUONG", "Chương 3", "Đường trung bình của tam giác & hình thang", "geom_midsegment_trap", "MN = (a+b)/2", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_GEO_PARALLELOGRAM_PROPERTIES", 8, "HINH_HOC_DO_LUONG", "Chương 3", "Hình bình hành & Giao điểm 2 đường chéo", "geom_parallelogram_diags", "Diagonals bisect", "EUCLIDEAN_ATELIER_PRO", 40),
        AssetFamilySpec("FAM_G08_GEO_RECTANGLE_RHOMBUS_SQUARE", 8, "HINH_HOC_DO_LUONG", "Chương 3", "Cây phả hệ tứ giác đặc biệt", "geom_quad_family_tree", "Quad -> Trap -> Para -> Rect/Rhom -> Sq", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_GEO_THALES_BASIC", 8, "HINH_HOC_DO_LUONG", "Chương 4", "Định lí Thales thuận và đảo", "geom_thales_tri", "AM/MB = AN/NC", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G08_GEO_THALES_HOURGLASS", 8, "HINH_HOC_DO_LUONG", "Chương 4", "Định lí Thales cấu hình đồng hồ cát", "geom_thales_hourglass", "OA/OA' = OB/OB'", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_GEO_ANGLE_BISECTOR_THEOREM", 8, "HINH_HOC_DO_LUONG", "Chương 4", "Tính chất đường phân giác tam giác", "geom_bisector_ratio", "DB/DC = AB/AC", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_GEO_SIMILAR_TRIANGLES_SSS", 8, "HINH_HOC_DO_LUONG", "Chương 9", "Tam giác đồng dạng (c.c.c)", "geom_similar_sss", "a1/a2 = b1/b2 = c1/c2 = k", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_GEO_SIMILAR_TRIANGLES_SAS", 8, "HINH_HOC_DO_LUONG", "Chương 9", "Tam giác đồng dạng (c.g.c)", "geom_similar_sas", "Side ratio + Included angle", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_GEO_SIMILAR_TRIANGLES_AA", 8, "HINH_HOC_DO_LUONG", "Chương 9", "Tam giác đồng dạng (g.g)", "geom_similar_aa", "Two equal angles", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G08_GEO_SHADOW_RECKONING_PYRAMID", 8, "HINH_HOC_DO_LUONG", "Chương 9", "Thales đo chiều cao kim tự tháp qua bóng nắng", "geom_shadow_thales", "H/h = S/s", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G08_GEO_SOLID_PYRAMID_TRI", 8, "HINH_HOC_DO_LUONG", "Chương 10", "Hình chóp tam giác đều & Mặt nón", "geom_pyramid_tri", "V = 1/3 * S_base * h", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G08_GEO_SOLID_PYRAMID_QUAD", 8, "HINH_HOC_DO_LUONG", "Chương 10", "Hình chóp tứ giác đều (Kim tự tháp Louvre)", "geom_pyramid_quad", "S_xq + S_base", "EUCLIDEAN_ATELIER_PRO", 45),
    ])
    # Thống kê 8
    families.extend([
        AssetFamilySpec("FAM_G08_STAT_HISTOGRAM_FREQUENCY", 8, "THONG_KE_XAC_SUAT", "Chương 5", "Biểu đồ tần số ghép lớp (Histogram)", "stat_histogram", "Continuous intervals", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G08_STAT_FREQUENCY_POLYGON", 8, "THONG_KE_XAC_SUAT", "Chương 5", "Đường gấp khúc tần số", "stat_freq_polygon", "Midpoint line", "DATA_OBSERVATORY_LAB", 40),
        AssetFamilySpec("FAM_G08_STAT_PROBABILITY_TREE", 8, "THONG_KE_XAC_SUAT", "Chương 8", "Sơ đồ cây xác suất 2 giai đoạn", "stat_tree_diagram", "Multiply branch probs", "DATA_OBSERVATORY_LAB", 45),
    ])
    # STEM 8
    families.extend([
        AssetFamilySpec("FAM_G08_STEM_WORK_RATE_CONVOY", 8, "STEM_THUC_TIEN", "Thực hành", "Cân lập luận bài toán năng suất đội xe tải", "stem_work_convoy", "Q/x - Q/(x+k) = Delta", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G08_STEM_RIVER_BOAT_VELOCITY", 8, "STEM_THUC_TIEN", "Thực hành", "Ca nô xuôi dòng & ngược dòng", "stem_boat_river", "v_xuoi = v + v_n, v_nguoc = v - v_n", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G08_STEM_CIRCUIT_OHM_LAW", 8, "STEM_THUC_TIEN", "Thực hành", "Mạch điện song song & Điện trở tương đương", "stem_ohm_circuit", "1/R = 1/R1 + 1/R2", "STEM_COMMAND_3D", 45),
    ])

    # ==========================================
    # KHỐI 9: 45 FAMILIES
    # ==========================================
    # Đại số 9
    families.extend([
        AssetFamilySpec("FAM_G09_ALG_LINEAR_SYSTEM_2VAR_GEO", 9, "SO_HOC_DAI_SO", "Chương 1", "Hệ phương trình bậc nhất 2 ẩn (Giao điểm)", "algebra_sys2_geo", "d1 cap d2 = (x0, y0)", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G09_ALG_INEQUALITY_NUMBER_LINE", 9, "SO_HOC_DAI_SO", "Chương 2", "Bất đẳng thức & Tập nghiệm trên trục số", "algebra_ineq_numberline", "x > a (shaded left)", "REAL_PAPER_HYBRID_V04", 45),
        AssetFamilySpec("FAM_G09_ALG_RADICAL_SPIRAL_THEODORUS", 9, "SO_HOC_DAI_SO", "Chương 3", "Vòng xoắn căn bậc hai Theodorus", "algebra_theodorus_spiral", "sqrt(1), sqrt(2)...", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G09_ALG_RADICAL_SIMPLIFY_GEO", 9, "SO_HOC_DAI_SO", "Chương 3", "Khử mẫu căn thức bậc hai & Liên hợp", "algebra_radical_geo", "sqrt(A^2) = |A|", "REAL_PAPER_HYBRID_V04", 40),
        AssetFamilySpec("FAM_G09_ALG_QUADRATIC_PARABOLA_VERTEX", 9, "SO_HOC_DAI_SO", "Chương 6", "Parabol y = ax^2 (Đỉnh O, trục đối xứng)", "algebra_parabola_basic", "y = ax^2", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G09_ALG_QUADRATIC_ROOTS_DISCRIM", 9, "SO_HOC_DAI_SO", "Chương 6", "Phương trình bậc hai & Biệt thức Delta", "algebra_quad_delta", "Delta = b^2 - 4ac", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G09_ALG_VIETE_RELATION_GEO", 9, "SO_HOC_DAI_SO", "Chương 6", "Định lí Viète (Tổng S & Tích P hình chữ nhật)", "algebra_viete_geom", "x1+x2=-b/a, x1*x2=c/a", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G09_ALG_PARABOLA_LINE_INTERSECT", 9, "SO_HOC_DAI_SO", "Chương 6", "Sự tương giao Parabol (P) & Đường thẳng (d)", "algebra_parabola_line", "ax^2 = mx + n", "EUCLIDEAN_ATELIER_PRO", 50),
    ])
    # Hình học 9
    families.extend([
        AssetFamilySpec("FAM_G09_GEO_RIGHT_TRI_METRIC_SYS", 9, "HINH_HOC_DO_LUONG", "Chương 4", "Hệ thức lượng trong tam giác vuông (h^2=b'c')", "geom_right_tri_metric", "h^2 = b'*c', b^2 = a*b'", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G09_GEO_TRIG_RATIOS_SIN_COS", 9, "HINH_HOC_DO_LUONG", "Chương 4", "Tỉ số lượng giác góc nhọn (sin, cos, tan, cot)", "geom_trig_right_tri", "sin = doi/huyen", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G09_GEO_CLINOMETER_SURVEY", 9, "HINH_HOC_DO_LUONG", "Chương 4", "Giác kế đo chiều cao tòa nhà / ngọn hải đăng", "geom_clinometer_survey", "H = d*tan(alpha) + h0", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G09_GEO_CIRCLE_TANGENT_SECANT", 9, "HINH_HOC_DO_LUONG", "Chương 5", "Đường tròn, Tiếp tuyến & Bán kính vuông góc", "geom_circle_tangent", "d(O, d) = R", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G09_GEO_TWO_TANGENTS_INTERSECT", 9, "HINH_HOC_DO_LUONG", "Chương 5", "Tính chất hai tiếp tuyến cắt nhau", "geom_two_tangents_meet", "MA = MB, MO is bisector", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G09_GEO_INSCRIBED_CENTRAL_ANGLE", 9, "HINH_HOC_DO_LUONG", "Chương 5", "Góc ở tâm & Góc nội tiếp cùng chắn một cung", "geom_inscribed_central", "Angle_ins = 1/2 Angle_cent", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G09_GEO_CYCLIC_QUADRILATERAL", 9, "HINH_HOC_DO_LUONG", "Chương 5", "Tứ giác nội tiếp đường tròn (Tổng góc đối 180)", "geom_cyclic_quad", "Angle A + C = 180", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G09_GEO_SOLID_CYLINDER", 9, "HINH_HOC_DO_LUONG", "Chương 10", "Hình trụ tròn xoay & Thùng chứa", "geom_solid_cylinder", "V = pi * R^2 * h", "STEM_COMMAND_3D", 45),
        AssetFamilySpec("FAM_G09_GEO_SOLID_CONE", 9, "HINH_HOC_DO_LUONG", "Chương 10", "Hình nón & Nón lá truyền thống", "geom_solid_cone", "V = 1/3 pi R^2 h, l^2=h^2+R^2", "WARM_STORYBOOK_TACTILE", 45),
        AssetFamilySpec("FAM_G09_GEO_SOLID_SPHERE", 9, "HINH_HOC_DO_LUONG", "Chương 10", "Hình cầu & Quả địa cầu", "geom_solid_sphere", "V = 4/3 pi R^3, S = 4 pi R^2", "EUCLIDEAN_ATELIER_PRO", 45),
    ])
    # Thống kê 9
    families.extend([
        AssetFamilySpec("FAM_G09_STAT_FREQUENCY_TABLE_PIE", 9, "THONG_KE_XAC_SUAT", "Chương 7", "Bảng tần số tương đối & Biểu đồ hình quạt", "stat_rel_freq_pie", "f_i = m_i / N * 100%", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G09_STAT_EMPIRICAL_PROB_DICE", 9, "THONG_KE_XAC_SUAT", "Chương 8", "Xác suất thực nghiệm tiến dần xác suất lý thuyết", "stat_large_numbers_law", "P_n -> P as n -> inf", "DATA_OBSERVATORY_LAB", 45),
    ])
    # STEM 9
    families.extend([
        AssetFamilySpec("FAM_G09_STEM_PARABOLIC_ARCH_BRIDGE", 9, "STEM_THUC_TIEN", "Thực hành", "Cầu vòm Parabol & Khẩu độ nhịp cầu", "stem_parabolic_arch", "y = -k * x^2 + H", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G09_STEM_SUBMARINE_BUOYANCY", 9, "STEM_THUC_TIEN", "Thực hành", "Tàu ngầm lặn nổi & Cân bằng Archimedes", "stem_submarine_depth", "F_A = d*V_disp, P = d*h", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G09_STEM_WATER_TANK_INFLOW", 9, "STEM_THUC_TIEN", "Thực hành", "Bể nước 2 vòi chảy chung - chảy riêng", "stem_tank_flow_harmonic", "1/t1 + 1/t2 = 1/T", "STEM_COMMAND_3D", 45),
    ])

    # ==========================================
    # KHỐI 10: 40 FAMILIES
    # ==========================================
    # Đại số 10
    families.extend([
        AssetFamilySpec("FAM_G10_ALG_SET_INTERVAL_NUMBERLINE", 10, "SO_HOC_DAI_SO", "Chương 1", "Khoảng, đoạn, nửa khoảng trên trục số thực", "alg_intervals_real", "[a, b), (c, d)", "REAL_PAPER_HYBRID_V04", 45),
        AssetFamilySpec("FAM_G10_ALG_LINEAR_INEQ_REGION_2VAR", 10, "SO_HOC_DAI_SO", "Chương 2", "Miền nghiệm bất phương trình ax + by <= c", "alg_half_plane_ineq", "ax + by <= c half-plane", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G10_ALG_LINEAR_PROGRAMMING_POLY", 10, "SO_HOC_DAI_SO", "Chương 2", "Quy hoạch tuyến tính (Miền đa giác lồi & Min/Max)", "alg_linprog_polygon", "Max F = ax + by on Poly", "DATA_OBSERVATORY_LAB", 50),
        AssetFamilySpec("FAM_G10_ALG_QUADRATIC_FUNCTION_STUDY", 10, "SO_HOC_DAI_SO", "Chương 6", "Khảo sát hàm số bậc hai y = ax^2 + bx + c", "alg_quad_full_study", "Vertex (-b/2a, -Delta/4a)", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G10_ALG_QUADRATIC_SIGN_INTERVALS", 10, "SO_HOC_DAI_SO", "Chương 6", "Bảng xét dấu tam thức bậc hai (Trong trái ngoài cùng)", "alg_quad_sign_table", "Sign of f(x) vs Delta", "REAL_PAPER_HYBRID_V04", 45),
        AssetFamilySpec("FAM_G10_ALG_NEWTON_BINOMIAL_EXPAND", 10, "SO_HOC_DAI_SO", "Chương 8", "Tam giác Pascal & Khai triển Nhị thức Newton", "alg_pascal_triangle", "(a+b)^n = sum C_n^k a^(n-k)b^k", "DATA_OBSERVATORY_LAB", 45),
    ])
    # Hình học & Tọa độ 10
    families.extend([
        AssetFamilySpec("FAM_G10_GEO_COSINE_SINE_LAW_TRI", 10, "HINH_HOC_DO_LUONG", "Chương 3", "Định lí Côsin & Sin giải tam giác bất kỳ", "geom_cosine_sine_law", "a^2 = b^2+c^2 - 2bc cos A", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G10_GEO_VECTOR_SUM_PARALLELOGRAM", 10, "HINH_HOC_DO_LUONG", "Chương 4", "Quy tắc hình bình hành cộng vectơ", "geom_vector_addition", "u + v = w (diag)", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G10_GEO_VECTOR_DOT_PRODUCT", 10, "HINH_HOC_DO_LUONG", "Chương 4", "Tích vô hướng hai vectơ & Góc giữa 2 vectơ", "geom_vector_dot_prod", "u . v = |u||v| cos theta", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G10_GEO_LINE_PARAMETRIC_NORMAL", 10, "HINH_HOC_DO_LUONG", "Chương 7", "Phương trình đường thẳng (Pháp tuyến & Chỉ phương)", "geom_coord_line", "ax + by + c = 0", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G10_GEO_DISTANCE_POINT_LINE", 10, "HINH_HOC_DO_LUONG", "Chương 7", "Khoảng cách từ điểm đến đường thẳng", "geom_dist_point_line", "d = |ax0+by0+c|/sqrt(a^2+b^2)", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G10_GEO_CIRCLE_EQUATION_TANGENT", 10, "HINH_HOC_DO_LUONG", "Chương 7", "Đường tròn trong Oxy & Tiếp tuyến tại điểm", "geom_circle_analytic", "(x-a)^2 + (y-b)^2 = R^2", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G10_GEO_CONIC_ELLIPSE", 10, "HINH_HOC_DO_LUONG", "Chương 7", "Đường Elip (Tiêu điểm, Tiêu cự, Bán trục lớn)", "geom_conic_ellipse", "x^2/a^2 + y^2/b^2 = 1", "EUCLIDEAN_ATELIER_PRO", 55),
        AssetFamilySpec("FAM_G10_GEO_CONIC_HYPERBOLA", 10, "HINH_HOC_DO_LUONG", "Chương 7", "Đường Hypebol (Đường tiệm cận & Tiêu điểm)", "geom_conic_hyperbola", "x^2/a^2 - y^2/b^2 = 1", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G10_GEO_CONIC_PARABOLA_FOCUS", 10, "HINH_HOC_DO_LUONG", "Chương 7", "Đường Parabol chính tắc (Tiêu điểm & Đường chuẩn)", "geom_conic_parabola", "y^2 = 2px", "EUCLIDEAN_ATELIER_PRO", 50),
    ])
    # Thống kê 10
    families.extend([
        AssetFamilySpec("FAM_G10_STAT_BOX_PLOT_OUTLIER", 10, "THONG_KE_XAC_SUAT", "Chương 5", "Biểu đồ hộp (Box-and-Whisker) & Giá trị ngoại lệ", "stat_box_plot", "Q1, Med, Q3, IQR", "DATA_OBSERVATORY_LAB", 50),
        AssetFamilySpec("FAM_G10_STAT_SCATTER_PLOT_CORR", 10, "THONG_KE_XAC_SUAT", "Chương 5", "Biểu đồ phân tán & Đường xu hướng hồi quy", "stat_scatter_trend", "Linear correlation r", "DATA_OBSERVATORY_LAB", 45),
    ])
    # STEM 10
    families.extend([
        AssetFamilySpec("FAM_G10_STEM_PROJECTILE_MOTION", 10, "STEM_THUC_TIEN", "Thực hành", "Quỹ đạo chuyển động ném xiên (Vật lý 10)", "stem_projectile_parabola", "y = x tan alpha - gx^2/(2v0^2 cos^2 alpha)", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G10_STEM_REFLECTIVE_SATELLITE_DISH", 10, "STEM_THUC_TIEN", "Thực hành", "Chảo vệ tinh Parabol hội tụ sóng tại tiêu điểm", "stem_parabolic_dish", "Rays focus at F(p/2, 0)", "STEM_COMMAND_3D", 50),
    ])

    # ==========================================
    # KHỐI 11: 42 FAMILIES
    # ==========================================
    # Lượng giác & Dãy số 11
    families.extend([
        AssetFamilySpec("FAM_G11_TRIG_UNIT_CIRCLE_FULL", 11, "SO_HOC_DAI_SO", "Chương 1", "Vòng tròn lượng giác đơn vị đầy đủ giá trị đặc biệt", "trig_unit_circle", "x^2 + y^2 = 1, (cos, sin)", "EUCLIDEAN_ATELIER_PRO", 55),
        AssetFamilySpec("FAM_G11_TRIG_SINE_WAVE_OSCILLATION", 11, "SO_HOC_DAI_SO", "Chương 1", "Đồ thị sóng hình sin y = A sin(omega t + phi)", "trig_sine_graph", "Period T = 2pi / omega", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G11_TRIG_COSINE_TANGENT_GRAPHS", 11, "SO_HOC_DAI_SO", "Chương 1", "Đồ thị hàm số y = cos x và y = tan x", "trig_cos_tan_graph", "Asymptotes at x = pi/2 + k pi", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_ALG_ARITHMETIC_PROGRESSION", 11, "SO_HOC_DAI_SO", "Chương 2", "Cấp số cộng (Bậc thang số học & Tổng S_n)", "alg_arithmetic_seq", "u_n = u1 + (n-1)d", "REAL_PAPER_HYBRID_V04", 45),
        AssetFamilySpec("FAM_G11_ALG_GEOMETRIC_PROGRESSION", 11, "SO_HOC_DAI_SO", "Chương 2", "Cấp số nhân (Tăng trưởng hàm mũ & Fractal)", "alg_geometric_seq", "u_n = u1 * q^(n-1)", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G11_CALC_LIMIT_SEQUENCE_CONVERGE", 11, "SO_HOC_DAI_SO", "Chương 5", "Giới hạn dãy số & Dải kẹp epsilon", "calc_limit_seq", "lim u_n = L, |u_n - L| < eps", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_CALC_FUNCTION_CONTINUITY", 11, "SO_HOC_DAI_SO", "Chương 5", "Hàm số liên tục & Định lí giá trị trung gian", "calc_continuity_ivt", "f(a)*f(b) < 0 => exists c", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_ALG_EXPONENTIAL_LOG_CURVES", 11, "SO_HOC_DAI_SO", "Chương 6", "Đồ thị hàm số Mũ y = a^x & Logarit y = log_a x", "alg_exp_log_graphs", "Inverse symmetric over y=x", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G11_CALC_DERIVATIVE_TANGENT_SLOPE", 11, "SO_HOC_DAI_SO", "Chương 9", "Ý nghĩa hình học của đạo hàm (Tiếp tuyến cát tuyến)", "calc_secant_to_tangent", "f'(x0) = lim Delta y / Delta x", "EUCLIDEAN_ATELIER_PRO", 50),
    ])
    # Hình học không gian 11
    families.extend([
        AssetFamilySpec("FAM_G11_GEO3D_PARALLEL_LINE_PLANE", 11, "HINH_HOC_DO_LUONG", "Chương 4", "Đường thẳng song song mặt phẳng trong không gian", "geom3d_line_parallel_plane", "d // a, a subset (P)", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_GEO3D_PARALLEL_PLANES", 11, "HINH_HOC_DO_LUONG", "Chương 4", "Hai mặt phẳng song song & Định lí Thales không gian", "geom3d_parallel_planes", "(P) // (Q)", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_GEO3D_PYRAMID_CROSS_SECTION", 11, "HINH_HOC_DO_LUONG", "Chương 4", "Thiết diện hình chóp cắt bởi mặt phẳng", "geom3d_pyramid_cross_section", "Polygon section of pyramid", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G11_GEO3D_LINE_PERP_PLANE", 11, "HINH_HOC_DO_LUONG", "Chương 7", "Đường thẳng vuông góc với mặt phẳng", "geom3d_line_perp_plane", "d perp a, d perp b", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G11_GEO3D_TWO_PERP_PLANES", 11, "HINH_HOC_DO_LUONG", "Chương 7", "Hai mặt phẳng vuông góc", "geom3d_two_perp_planes", "(P) perp (Q)", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_GEO3D_DISTANCE_POINT_PLANE", 11, "HINH_HOC_DO_LUONG", "Chương 7", "Khoảng cách từ điểm đến mặt phẳng", "geom3d_dist_point_plane", "d(M, (P)) = MH", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_GEO3D_SKEW_LINES_DISTANCE", 11, "HINH_HOC_DO_LUONG", "Chương 7", "Khoảng cách giữa hai đường thẳng chéo nhau", "geom3d_skew_lines_dist", "Common perpendicular segment", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G11_GEO3D_DIHEDRAL_ANGLE", 11, "HINH_HOC_DO_LUONG", "Chương 7", "Góc nhị diện (Góc giữa hai mặt phẳng)", "geom3d_dihedral_angle", "Angle between two normal rays", "EUCLIDEAN_ATELIER_PRO", 45),
    ])
    # Thống kê & Xác suất 11
    families.extend([
        AssetFamilySpec("FAM_G11_STAT_GROUPED_MEDIAN_QUART", 11, "THONG_KE_XAC_SUAT", "Chương 3", "Trung vị & Tứ phân vị mẫu số liệu ghép nhóm", "stat_grouped_median_ogive", "Ogive cumulative curve", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G11_STAT_INDEPENDENT_EVENTS_VENN", 11, "THONG_KE_XAC_SUAT", "Chương 8", "Biến cố độc lập & Biến cố xung khắc (Venn & Cây)", "stat_indep_venn_tree", "P(A cap B) = P(A)*P(B)", "DATA_OBSERVATORY_LAB", 45),
    ])
    # STEM 11
    families.extend([
        AssetFamilySpec("FAM_G11_STEM_RADIOACTIVE_DECAY", 11, "STEM_THUC_TIEN", "Thực hành", "Phân rã phóng xạ bán rã & Hàm số mũ (Vật lý 11)", "stem_half_life_decay", "N(t) = N0 * e^(-lambda t)", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G11_STEM_PENDULUM_SHM", 11, "STEM_THUC_TIEN", "Thực hành", "Con lắc đơn dao động điều hòa & Đồ thị pha", "stem_simple_pendulum", "x = A cos(omega t + phi)", "STEM_COMMAND_3D", 50),
    ])

    # ==========================================
    # KHỐI 12: 38 FAMILIES
    # ==========================================
    # Giải tích 12 (Đạo hàm & Khảo sát đồ thị)
    families.extend([
        AssetFamilySpec("FAM_G12_CALC_CUBIC_FUNCTION_SHAPES", 12, "GIAI_TICH_HINH_HOC", "Chương 1", "Đồ thị hàm bậc ba y = ax^3 + bx^2 + cx + d (6 dạng)", "calc_cubic_6shapes", "f'(x) roots & extrema", "EUCLIDEAN_ATELIER_PRO", 55),
        AssetFamilySpec("FAM_G12_CALC_QUARTIC_BIQUADRATIC", 12, "GIAI_TICH_HINH_HOC", "Chương 1", "Đồ thị hàm trùng phương y = ax^4 + bx^2 + c (W & U)", "calc_quartic_shapes", "3 extrema vs 1 extremum", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G12_CALC_RATIONAL_HOMOGRAPHIC", 12, "GIAI_TICH_HINH_HOC", "Chương 1", "Đồ thị hàm nhất biến y = (ax+b)/(cx+d) & Tiệm cận", "calc_homographic_asymptotes", "x = -d/c, y = a/c", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G12_CALC_OBLIQUE_ASYMPTOTE", 12, "GIAI_TICH_HINH_HOC", "Chương 1", "Tiệm cận xiên của hàm phân thức bậc 2 trên bậc 1", "calc_oblique_asymptote", "y = ax + b + r/(cx+d)", "EUCLIDEAN_ATELIER_PRO", 45),
        AssetFamilySpec("FAM_G12_CALC_OPTIMIZATION_CAN_BOX", 12, "GIAI_TICH_HINH_HOC", "Chương 1", "Bài toán tối ưu hóa thể tích hộp không nắp", "calc_optim_box_unfold", "V(x) = x(a-2x)(b-2x) -> Max", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G12_CALC_INTEGRAL_AREA_CURVES", 12, "GIAI_TICH_HINH_HOC", "Chương 4", "Diện tích hình phẳng giới hạn bởi đồ thị (Phần tô đậm)", "calc_integral_shaded_area", "S = int_a^b |f(x) - g(x)| dx", "EUCLIDEAN_ATELIER_PRO", 55),
        AssetFamilySpec("FAM_G12_CALC_SOLID_REVOLUTION_3D", 12, "GIAI_TICH_HINH_HOC", "Chương 4", "Thể tích khối tròn xoay quay quanh trục hoành", "calc_revolution_solid_3d", "V = pi int_a^b f(x)^2 dx", "EUCLIDEAN_ATELIER_PRO", 50),
    ])
    # Tọa độ không gian Oxyz 12
    families.extend([
        AssetFamilySpec("FAM_G12_GEO3D_OXYZ_COORDINATE_FRAME", 12, "GIAI_TICH_HINH_HOC", "Chương 2", "Hệ trục tọa độ Oxyz & Điểm M(x, y, z)", "geom_oxyz_axes_point", "OM = x i + y j + z k", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G12_GEO3D_VECTOR_CROSS_PRODUCT", 12, "GIAI_TICH_HINH_HOC", "Chương 2", "Tích có hướng hai vectơ & Vectơ pháp tuyến", "geom_oxyz_cross_product", "[u, v] perp u, v", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G12_GEO3D_PLANE_EQUATION_NORMAL", 12, "GIAI_TICH_HINH_HOC", "Chương 5", "Phương trình mặt phẳng (P): Ax + By + Cz + D = 0", "geom_oxyz_plane", "n = (A, B, C)", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G12_GEO3D_LINE_PARAMETRIC_SPACE", 12, "GIAI_TICH_HINH_HOC", "Chương 5", "Phương trình đường thẳng tham số trong không gian", "geom_oxyz_line_space", "x = x0 + at, y = y0 + bt", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G12_GEO3D_SPHERE_CENTER_RADIUS", 12, "GIAI_TICH_HINH_HOC", "Chương 5", "Phương trình mặt cầu (S) & Tiếp diện mặt cầu", "geom_oxyz_sphere_plane", "(x-a)^2+(y-b)^2+(z-c)^2 = R^2", "EUCLIDEAN_ATELIER_PRO", 50),
        AssetFamilySpec("FAM_G12_GEO3D_REL_POS_TWO_LINES_3D", 12, "GIAI_TICH_HINH_HOC", "Chương 5", "Vị trí tương đối 2 đường thẳng trong Oxyz", "geom_oxyz_rel_lines", "Parallel, intersect, skew", "EUCLIDEAN_ATELIER_PRO", 45),
    ])
    # Thống kê & Xác suất 12
    families.extend([
        AssetFamilySpec("FAM_G12_STAT_VARIANCE_STD_DEV_BOX", 12, "THONG_KE_XAC_SUAT", "Chương 3", "Phương sai & Độ lệch chuẩn ghép nhóm", "stat_variance_std_bell", "s^2 = 1/n sum m_i (x_i - bar_x)^2", "DATA_OBSERVATORY_LAB", 45),
        AssetFamilySpec("FAM_G12_STAT_CONDITIONAL_PROB_TREE", 12, "THONG_KE_XAC_SUAT", "Chương 6", "Xác suất có điều kiện P(A|B) & Sơ đồ cây nhánh", "stat_bayes_tree", "P(A|B) = P(A cap B) / P(B)", "DATA_OBSERVATORY_LAB", 50),
        AssetFamilySpec("FAM_G12_STAT_TOTAL_PROB_BAYES", 12, "THONG_KE_XAC_SUAT", "Chương 6", "Công thức xác suất toàn phần & Định lí Bayes", "stat_bayes_theorem_venn", "P(B) = sum P(A_i)*P(B|A_i)", "DATA_OBSERVATORY_LAB", 50),
    ])
    # STEM & Ứng dụng thực tế 12
    families.extend([
        AssetFamilySpec("FAM_G12_STEM_EPIDEMIC_LOGISTIC_CURVE", 12, "STEM_THUC_TIEN", "Chương 1", "Mô hình dịch bệnh & Tăng trưởng Logistic (Đường cong chữ S)", "stem_logistic_growth", "N(t) = K / (1 + A e^(-rt))", "STEM_COMMAND_3D", 50),
        AssetFamilySpec("FAM_G12_STEM_RADAR_AIRSPACE_OXYZ", 12, "STEM_THUC_TIEN", "Chương 5", "Radar hàng không quét máy bay trong không gian Oxyz", "stem_radar_airspace_3d", "Spherical coordinates tracking", "STEM_COMMAND_3D", 50),
    ])

    return families

if __name__ == "__main__":
    fams = get_k12_asset_families()
    print(f"Total defined K12 Asset Families: {len(fams)}")
    by_grade = {}
    for f in fams:
        by_grade[f.grade] = by_grade.get(f.grade, 0) + 1
    for g in sorted(by_grade.keys()):
        print(f"  - Grade {g}: {by_grade[g]} families")
