# -*- coding: utf-8 -*-
"""
BỘ DỮ LIỆU CHUYÊN SÂU — LIVING ASSETS 09..16
(MẠCH 2: HÀM SỐ BẬC HAI + MẠCH 3: HÌNH HỌC, ĐO LƯỜNG & KHÔNG GIAN + MẠCH 4: THỐNG KÊ, XÁC SUẤT & TOÁN ỨNG DỤNG)
"""

from __future__ import annotations
from typing import Any, Dict, List

LIVING_ASSETS_PART_2: List[Dict[str, Any]] = [
    # 09. TOÁN 9 — MẠCH 2 (ĐẠI SỐ & HÀM SỐ): HÀM SỐ BẬC HAI y = ax² & VÒM CẦU PARABOL
    {
        "asset_id": "YD-LA-ALG-G9-09",
        "asset_no": "09",
        "skill_id": "S_G09_B18",
        "grade": 9,
        "strand_code": "DAI_SO_VA_HAM_SO",
        "strand_name": "Đại số, Phương trình & Hàm số",
        "header_subtitle": "TOÁN 9 • HÀM SỐ y = ax² (a ≠ 0) • ĐỒ THỊ PARABOL & KIỂM THỬ THỰC TẾ",
        "title": "Kỹ Sư Thiết Kế Vòm Cầu Parabol y = ax² & Kiểm Thử Độ Thoáng Tàu Hàng",
        "story_hook": "Vòm cầu có dạng Parabol y = ax² cao 9 m, nhịp cầu tại mặt nước rộng 24 m. Một tàu chở hàng rộng 8 m và cao 6 m tính từ mặt nước có đi lọt qua gầm cầu an toàn hay không?",
        "objective": "Gắn hệ tọa độ Oxy vào đỉnh Parabol y = ax², xác định hệ số a từ điểm biên thực tế và kiểm tra bất đẳng thức độ cao an toàn.",
        "artistic_world": "STEM_COMMAND_3D",
        "primitives_used": ["PRIM_FUNCTION_GRAPH_PORTAL"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "PARABOLA_ARCH_CLEARANCE",
            "control_label": "Điều chỉnh bề rộng tàu chở hàng W (m) đi chính giữa cầu:",
            "min_val": 2,
            "max_val": 20,
            "step_val": 2,
            "default_trial": 8,
            "target_solution": 8,
            "unit": "m",
            "parameters": {"arch_height": 9.0, "arch_span": 24.0, "boat_height": 6.0, "target_solution": 8.0},
        },
        "math_semantics": {
            "unknown_symbol": "a",
            "domain_constraint": "-12 ≤ x ≤ 12; a < 0",
            "invariant_relation": "y = (-1/16)·x²; h_thoáng(x) = 9 - x²/16",
            "target_equation": "Tại mép tàu x = 8/2 = 4: h_thoáng(4) = 9 - 16/16 = 8 (m) > 6 (m) ⇒ Tàu qua an toàn!",
            "verification_type": "SYMBOLIC_SYMPY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Đặt gốc tọa độ O(0; 0) ngay tại đỉnh cao nhất của vòm cầu! Vì cầu rộng 24 m và đối xứng hai bên nên chân cầu ở x = 12 m và x = -12 m. Kéo thử tàu rộng 8 m (mép tàu ở x = 4 m), bạn sẽ thấy trần cầu vẫn còn cách nóc tàu 2 m!",
            "B": "Thay tọa độ chân cầu B(12; -9) vào phương trình y = ax² để tìm a = -9/144 = -1/16. Sau đó tính tung độ y tại x = 4.",
            "C": "Bài toán ngược: Với tàu cao 6 m, chiều rộng tối đa W_max của tàu là bao nhiêu để vừa khít gầm cầu (9 - x²/16 = 6)?",
        },
        "misconceptions": [
            "Thay cả chiều rộng nhịp cầu x = 24 vào công thức y = ax² thay vì nửa chiều rộng x = 12.",
            "Quên trừ độ hạ của vòm Parabol khỏi chiều cao đỉnh cầu 9 m.",
        ],
        "knowledge_activation": "Đồ thị hàm số y = ax² (a ≠ 0) là một đường Parabol nhận trục tung Oy làm trục đối xứng và gốc O(0; 0) làm đỉnh.",
        "worked_example": {
            "problem": "Một vòm cầu có hình dạng Parabol y = ax² (gốc O tại đỉnh vòm, trục Oy hướng thẳng đứng lên trên). Chiều cao từ mặt nước lên đỉnh vòm là 9 m, khoảng cách giữa hai chân vòm tại mặt nước là 24 m. Một sà lan rộng 8 m, cao 6 m đi chính giữa gầm cầu có qua được không?",
            "steps": [
                "Bước 1 (Xác định tọa độ chân vòm & tìm a): Do tính đối xứng qua Oy, chân vòm phía phải có hoành độ x = 24 : 2 = 12 (m) và tung độ y = -9 (m). Thay vào y = ax²: -9 = a · 12² ⇒ a = -1/16.",
                "Bước 2 (Tính độ cao vòm tại mép sà lan): Sà lan rộng 8 m đi chính giữa nên mép sà lan có hoành độ x = 8 : 2 = 4 (m). Khi đó y = (-1/16) · 4² = -1 (m).",
                "Bước 3 (So sánh độ cao an toàn): Khoảng cách từ mặt nước lên vòm cầu tại x = 4 là 9 - 1 = 8 (m) > 6 (m). Vậy sà lan đi qua cầu an toàn.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Xác định hệ số a của hàm số y = ax² biết đồ thị của nó đi qua điểm M(2; 12).",
                "final_answer": "a = 3",
                "teacher_solution": "Thay x = 2, y = 12 vào y = ax²: 12 = a · 2² ⇒ 4a = 12 ⇒ a = 3.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Cho Parabol (P): y = 2x². Tìm tọa độ các điểm thuộc (P) có tung độ bằng 18.",
                "final_answer": "(3; 18) và (-3; 18)",
                "teacher_solution": "2x² = 18 ⇔ x² = 9 ⇔ x = 3 hoặc x = -3. Vậy có hai điểm (3; 18) và (-3; 18).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Tìm tọa độ giao điểm của Parabol (P): y = x² và đường thẳng (d): y = 2x + 3.",
            "final_answer": "A(-1; 1) và B(3; 9)",
            "teacher_solution": "Phương trình hoành độ giao điểm: x² - 2x - 3 = 0 ⇔ x = -1 (y = 1) hoặc x = 3 (y = 9).",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một cổng chào hình Parabol cao 8 m và khoảng cách giữa hai chân cổng là 8 m. Người ta muốn treo một tấm băng rôn ngang dài 4 m chính giữa cổng. Hỏi băng rôn phải treo ở độ cao bao nhiêu mét tính từ mặt đất để hai đầu băng rôn chạm đúng thành cổng?",
            "final_answer": "6 m",
            "teacher_solution": "Chọn O tại đỉnh cổng: chân cổng (4; -8) ⇒ -8 = a·4² ⇒ a = -1/2. Tại mép băng rôn x = 2 ⇒ y = (-1/2)·2² = -2 ⇒ Độ cao từ đất: 8 - 2 = 6 (m).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Gặp cổng vòm/cầu Parabol: Vì trục Oy chia đôi cổng nên hoành độ chân cổng luôn bằng NỬA CHIỀU RỘNG (x = Rộng : 2)!",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Nếu đặt gốc O tại ĐỈNH vòm thì phần cổng hướng xuống dưới mặt đất mang tung độ ÂM (y < 0).",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Tại x = 0 (chính giữa cầu), độ cao phải bằng đúng chiều cao đỉnh vòm (9 m).",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 10. TOÁN 6 — MẠCH 3 (HÌNH HỌC & ĐO LƯỜNG): HÌNH CHỮ L & BẪY CHU VI (KẾ THỪA H07)
    {
        "asset_id": "YD-LA-GEO-G6-10",
        "asset_no": "10",
        "skill_id": "S_G06_B20",
        "grade": 6,
        "strand_code": "HINH_HOC_VA_DO_LUONG",
        "strand_name": "Hình học, Đo lường & Không gian",
        "header_subtitle": "TOÁN 6 • CHU VI & DIỆN TÍCH HÌNH GHÉP (H07 CORE) • BẤT BIẾN CHU VI HÌNH CHỮ L",
        "title": "Kiến Trúc Sư Sân Vườn H07: Bẫy Chu Vi Khi Khoét Góc Hình Chữ Nhật",
        "story_hook": "Một mảnh vườn hình chữ nhật dài 12 m, rộng 10 m bị khoét đi một góc hình vuông 4 m × 4 m để làm hồ nước, tạo thành mảnh vườn hình chữ L. Diện tích giảm đi, nhưng vì sao chiều dài hàng rào bao quanh vườn (chu vi) lại KHÔNG HỀ GIẢM?",
        "objective": "Phá bỏ ngộ nhận kinh điển 'diện tích giảm thì chu vi cũng giảm' thông qua phép tịnh tiến hai cạnh góc khuyết ra viền ngoài (Bất biến Chu vi H07).",
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "primitives_used": ["PRIM_GEOMETRY_CUT_FOLD_RAY"],
        "interaction_level": 4,
        "interactive_engine": {
            "engine_type": "L_SHAPE_PERIMETER_INVARIANT",
            "control_label": "Kéo thay đổi cạnh góc vuông bị khoét c (m):",
            "min_val": 1,
            "max_val": 8,
            "step_val": 1,
            "default_trial": 4,
            "target_solution": 4,
            "unit": "m",
            "parameters": {"rect_L": 12, "rect_W": 10, "cut_c": 4, "target_solution": 4, "invariant_P": 44},
        },
        "math_semantics": {
            "unknown_symbol": "c",
            "domain_constraint": "0 < c < 10",
            "invariant_relation": "P_chữ_L = (12 - c) + c + c + (10 - c) + 12 + 10 = 44 m (Không phụ thuộc c!)",
            "target_equation": "S = 12×10 - 4×4 = 104 (m²); P = 2×(12 + 10) = 44 (m)",
            "verification_type": "RULE_BOUNDED_GEOMETRY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Hãy bấm nút 'Đẩy Cạnh Khuyết Ra Ngoài': đoạn ngang 4 m và đoạn dọc 4 m ở góc lõm khi đẩy ra ngoài sẽ ghép vừa khít lại thành hình chữ nhật ban đầu! Vậy hàng rào vẫn dài đúng 44 m!",
            "B": "Tính diện tích bằng phương pháp trừ (S_lớn - S_khoét = 120 - 16 = 104 m²) và tính chu vi bằng tổng 6 đoạn thẳng bao quanh.",
            "C": "Khi nào khoét hình chữ nhật mà chu vi lại TĂNG? (Gợi ý: Khoét một hốc ở giữa cạnh thay vì khoét ở góc!).",
        },
        "misconceptions": [
            "Lấy chu vi hình chữ nhật lớn trừ đi chu vi hình vuông nhỏ bị khoét (44 - 16 = 28 m — sai bản chất đường biên!).",
            "Cộng thiếu 2 đoạn thẳng nằm ở góc lõm bên trong hình chữ L khi tính chu vi.",
        ],
        "knowledge_activation": "Chu vi của một hình phẳng là tổng độ dài toàn bộ đường biên khép kín bao quanh hình đó. Diện tích là phần bề mặt bên trong.",
        "worked_example": {
            "problem": "Một mảnh vườn hình chữ nhật có chiều dài 12 m, chiều rộng 10 m. Người ta chừa lại một góc hình vuông cạnh 4 m ở một đỉnh để đặt bể nước, phần còn lại có dạng hình chữ L để trồng rau. Tính diện tích phần trồng rau và chu vi của phần vườn hình chữ L đó.",
            "steps": [
                "Bước 1 (Tính diện tích bằng cách trừ): Diện tích hình chữ nhật ban đầu là 12 × 10 = 120 (m²). Diện tích góc hình vuông là 4 × 4 = 16 (m²) ⇒ Diện tích trồng rau: S = 120 - 16 = 104 (m²).",
                "Bước 2 (Phân tích 6 cạnh đường biên hình chữ L): Các cạnh bao quanh gồm: 12 m, 10 m, (12 - 4) = 8 m, (10 - 4) = 6 m, và hai cạnh góc lõm 4 m, 4 m.",
                "Bước 3 (Tính chu vi bất biến): Chu vi hình chữ L là P = 12 + 10 + 8 + 6 + 4 + 4 = 44 (m) — đúng bằng chu vi hình chữ nhật ban đầu 2 × (12 + 10) = 44 (m).",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Một tấm bìa hình chữ nhật dài 15 cm, rộng 8 cm. Tính chu vi và diện tích của tấm bìa.",
                "final_answer": "Chu vi 46 cm; Diện tích 120 cm²",
                "teacher_solution": "Chu vi P = 2 × (15 + 8) = 46 (cm). Diện tích S = 15 × 8 = 120 (cm²).",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Từ tấm bìa 15 cm × 8 cm ở câu a, bạn An cắt bỏ một hình vuông cạnh 3 cm ở một góc. Hỏi diện tích và chu vi tấm bìa còn lại là bao nhiêu?",
                "final_answer": "Diện tích 111 cm²; Chu vi 46 cm",
                "teacher_solution": "Diện tích mới: 120 - 3² = 111 (cm²). Chu vi giữ nguyên không đổi: P = 46 (cm).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Một bậc thang gỗ nhìn ngang có dạng hình bậc thang gồm 4 bậc, tổng chiều rộng đáy là 120 cm và tổng chiều cao là 80 cm (các góc đều vuông). Tính chu vi của mặt cắt ngang bậc thang đó.",
            "final_answer": "400 cm",
            "teacher_solution": "Tổng các đoạn ngang của 4 bậc bằng đáy 120 cm; tổng các đoạn dọc của 4 bậc bằng chiều cao 80 cm ⇒ Chu vi P = 2 × (120 + 80) = 400 (cm).",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Sân nhà bác Minh hình chữ nhật dài 10 m, rộng 8 m. Bác làm một lối đi lát sỏi rộng 1 m chạy dọc theo một chiều dài và một chiều rộng của sân (hình chữ L). Tính diện tích phần lối đi lát sỏi.",
            "final_answer": "17 m²",
            "teacher_solution": "Phần sân còn lại là hình chữ nhật dài 10 - 1 = 9 m, rộng 8 - 1 = 7 m (diện tích 63 m²). Diện tích lối đi: 10×8 - 9×7 = 80 - 63 = 17 (m²).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Tính DIỆN TÍCH hình chữ L: Chia thành 2 hình chữ nhật nhỏ để cộng, hoặc lấy Hình chữ nhật lớn TRỪ góc bị khuyết.",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Bẫy kinh điển: Khoét một góc hình chữ nhật làm GIẢM diện tích nhưng CHU VI KHÔNG ĐỔI (tuyệt đối không lấy chu vi trừ chu vi)!",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Đếm đủ 6 cạnh của hình chữ L trước khi cộng chu vi.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 11. TOÁN 8 — MẠCH 3 (HÌNH HỌC): CHỨNG MINH ĐỊNH LÝ PYTHAGORE BẰNG CẮT GHÉP
    {
        "asset_id": "YD-LA-GEO-G8-11",
        "asset_no": "11",
        "skill_id": "S_G08_B15",
        "grade": 8,
        "strand_code": "HINH_HOC_VA_DO_LUONG",
        "strand_name": "Hình học, Đo lường & Không gian",
        "header_subtitle": "TOÁN 8 • ĐỊNH LÝ PYTHAGORE • CHỨNG MINH KHÔNG LỜI BẰNG BẤT BIẾN DIỆN TÍCH",
        "title": "Bằng Chứng Không Lời: Trượt 4 Tam Giác Vuông Chứng Minh a² + b² = c²",
        "story_hook": "Trong cùng một khung hình vuông cạnh (a + b), khi bạn đặt 4 tam giác vuông bằng nhau theo Cách 1 thì phần trống ở giữa là hình vuông cạnh huyền c². Khi trượt nhẹ 4 tam giác đó về góc theo Cách 2, phần trống tách thành đúng hai hình vuông a² và b²!",
        "objective": "Hiểu tại sao trong mọi tam giác vuông, bình phương cạnh huyền luôn bằng tổng bình phương hai cạnh góc vuông (a² + b² = c²) thông qua bảo toàn diện tích phần trống.",
        "artistic_world": "EUCLIDEAN_ATELIER_PRO",
        "primitives_used": ["PRIM_GEOMETRY_CUT_FOLD_RAY"],
        "interaction_level": 4,
        "interactive_engine": {
            "engine_type": "PYTHAGORAS_SLIDE_PROOF",
            "control_label": "Kéo thanh trượt tịnh tiến 4 tam giác vuông (0% → 100%):",
            "min_val": 0,
            "max_val": 100,
            "step_val": 10,
            "default_trial": 0,
            "target_solution": 100,
            "unit": "%",
            "parameters": {"leg_a": 6, "leg_b": 8, "hyp_c": 10, "target_solution": 100},
        },
        "math_semantics": {
            "unknown_symbol": "c",
            "domain_constraint": "a, b, c > 0",
            "invariant_relation": "S_trống = (a + b)² - 4·(1/2·a·b) = c² = a² + b²",
            "target_equation": "Với a = 6, b = 8 ⇒ c² = 6² + 8² = 36 + 64 = 100 ⇒ c = 10",
            "verification_type": "RULE_BOUNDED_GEOMETRY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Khung gỗ bên ngoài không đổi và 4 miếng gỗ hình tam giác vuông bên trong cũng không đổi! Vậy phần diện tích màu vàng ở trạng thái 1 (c²) BẮT BUỘC phải bằng tổng diện tích hai ô vuông ở trạng thái 2 (a² + b²)!",
            "B": "Khai triển đại số đồng thời với hình học: (a + b)² - 2ab = a² + b² = c².",
            "C": "Áp dụng Định lý Pythagore đảo để kiểm tra xem bộ ba đoạn thẳng (a, b, c) bất kỳ có tạo thành góc vuông của người thợ xây hay không.",
        },
        "misconceptions": [
            "Nhầm công thức tìm cạnh góc vuông với cạnh huyền: khi tìm cạnh góc vuông a lại lấy c² + b² thay vì c² - b².",
            "Quên khai căn bậc hai ở bước cuối (tính ra c² = 100 rồi kết luận luôn c = 100).",
        ],
        "knowledge_activation": "Trong một tam giác vuông, cạnh đối diện với góc vuông là cạnh lớn nhất và được gọi là cạnh huyền.",
        "worked_example": {
            "problem": "Một cánh buồm hình tam giác vuông có hai cạnh góc vuông dài a = 6 m và b = 8 m. Tính độ dài cạnh huyền c của cánh buồm và giải thích bằng bảo toàn diện tích trong hình vuông cạnh (a + b) = 14 m.",
            "steps": [
                "Bước 1 (Áp dụng định lý Pythagore): Trong tam giác vuông, ta có c² = a² + b² = 6² + 8² = 36 + 64 = 100.",
                "Bước 2 (Khai căn bậc hai): Vì c > 0 nên c = √100 = 10 (m).",
                "Bước 3 (Đối chiếu diện tích khung 14 m × 14 m): Diện tích khung lớn là 14² = 196 m². Tổng diện tích 4 tam giác vuông là 4 × (6×8/2) = 96 m². Phần trống còn lại: 196 - 96 = 100 m² = c² = 36 + 64.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Cho tam giác ABC vuông tại A có AB = 5 cm, AC = 12 cm. Tính độ dài cạnh huyền BC.",
                "final_answer": "BC = 13 cm",
                "teacher_solution": "BC² = AB² + AC² = 5² + 12² = 25 + 144 = 169 ⇒ BC = √169 = 13 (cm).",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Cho tam giác DEF vuông tại D có cạnh huyền EF = 15 cm và cạnh góc vuông DE = 9 cm. Tính độ dài cạnh DF.",
                "final_answer": "DF = 12 cm",
                "teacher_solution": "DF² = EF² - DE² = 15² - 9² = 225 - 81 = 144 ⇒ DF = √144 = 12 (cm).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Tam giác có độ dài ba cạnh là 9 cm, 12 cm và 15 cm có phải là tam giác vuông không? Vì sao?",
            "final_answer": "Là tam giác vuông",
            "teacher_solution": "Ta có 9² + 12² = 81 + 144 = 225 và 15² = 225. Vì 9² + 12² = 15² nên theo định lý Pythagore đảo, tam giác đó vuông.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một chiếc thang dài 5 m được đặt dựa vào bức tường thẳng đứng. Để an toàn, chân thang phải cách chân tường 3 m. Hỏi đầu trên của thang chạm tường ở độ cao bao nhiêu mét?",
            "final_answer": "4 m",
            "teacher_solution": "Áp dụng định lý Pythagore: h² = 5² - 3² = 25 - 9 = 16 ⇒ h = 4 (m).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Xác định góc vuông trước tiên → Cạnh đối diện góc vuông là CẠNH HUYỀN (dài nhất).",
                    "Tìm cạnh huyền: CỘNG bình phương (c² = a² + b²). Tìm cạnh góc vuông: TRỪ bình phương (a² = c² - b²).",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Tính xong c² nhớ lấy CĂN BẬC HAI √(c²) để ra độ dài cạnh c!",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Ghi nhớ 3 bộ số Pythagore vàng: (3; 4; 5), (6; 8; 10), (5; 12; 13).",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 12. TOÁN 8 — MẠCH 3 (HÌNH HỌC): ĐỊNH LÝ THALES & ĐO CHIỀU CAO THÁP BẰNG BÓNG NẮNG
    {
        "asset_id": "YD-LA-GEO-G8-12",
        "asset_no": "12",
        "skill_id": "S_G08_B31",
        "grade": 8,
        "strand_code": "HINH_HOC_VA_DO_LUONG",
        "strand_name": "Hình học, Đo lường & Không gian",
        "header_subtitle": "TOÁN 8 • ĐỊNH LÝ THALES & TAM GIÁC ĐỒNG DẠNG • ĐO ĐẠC GIÁN TIẾP NGOÀI THỰC ĐỊA",
        "title": "Nhà Đo Đạc Cổ Đại: Đo Chiều Cao Tháp Cổ Bằng Bóng Nắng & Định Lý Thales",
        "story_hook": "Làm sao nhà toán học Thales đo được chiều cao Kim Tự Tháp khổng lồ mà không cần trèo lên đỉnh? Ông chỉ cần cắm một chiếc cọc gỗ cao 2 m xuống cát và đo bóng nắng của cọc cùng lúc với bóng của tháp!",
        "objective": "Hiểu rằng các tia nắng mặt trời song song tạo ra hai tam giác vuông đồng dạng, giữ cho tỉ số (Chiều cao vật / Độ dài bóng nắng) là một đại lượng bất biến tại cùng một thời điểm.",
        "artistic_world": "EUCLIDEAN_ATELIER_PRO",
        "primitives_used": ["PRIM_GEOMETRY_CUT_FOLD_RAY"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "THALES_SHADOW_RAY",
            "control_label": "Thay đổi độ dài bóng nắng của tháp theo góc Mặt Trời (m):",
            "min_val": 9,
            "max_val": 36,
            "step_val": 3,
            "default_trial": 18,
            "target_solution": 18,
            "unit": "m",
            "parameters": {"tower_h": 24.0, "stick_h": 2.0, "stick_shadow": 1.5, "target_solution": 18.0},
        },
        "math_semantics": {
            "unknown_symbol": "h",
            "domain_constraint": "h > 0",
            "invariant_relation": "h_tháp / s_tháp = h_cọc / s_cọc = tan(α)",
            "target_equation": "h / 18 = 2 / 1,5 ⇔ h = (18 × 2) / 1,5 = 24 (m)",
            "verification_type": "RULE_BOUNDED_GEOMETRY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Cọc cao 2 m có bóng dài 1,5 m. Bóng của tháp dài 18 m — tức là dài gấp 18 : 1,5 = 12 lần bóng cọc! Vậy chiều cao của tháp cũng phải cao gấp 12 lần cây cọc: 2 × 12 = 24 m!",
            "B": "Vì các tia sáng mặt trời song song nên hai tam giác vuông tạo bởi (Tháp – Bóng tháp) và (Cọc – Bóng cọc) đồng dạng (g.g) ⇒ h / 2 = 18 / 1,5.",
            "C": "Mở rộng phương pháp ngắm qua gương phẳng đặt trên mặt đất (góc tới bằng góc phản xạ) khi trời râm không có bóng nắng.",
        },
        "misconceptions": [
            "Lập tỉ số lệch đơn vị đo (cọc tính bằng cm nhưng bóng tháp tính bằng m mà quên đổi về cùng đơn vị).",
            "Ghép nhầm cặp cạnh tương ứng: lấy (Chiều cao tháp / Chiều cao cọc) = (Bóng cọc / Bóng tháp).",
        ],
        "knowledge_activation": "Hai tam giác vuông có góc nhọn tạo bởi tia nắng mặt trời bằng nhau thì đồng dạng với nhau: tỉ số hai cạnh góc vuông tương ứng luôn bằng nhau.",
        "worked_example": {
            "problem": "Cùng một thời điểm trong ngày, một tòa tháp cổ có bóng trên mặt đất dài 18 m, còn một thanh cọc thẳng đứng cao 2 m cắm gần đó có bóng dài 1,5 m. Tính chiều cao h của tòa tháp.",
            "steps": [
                "Bước 1 (Mô hình hóa hình học): Vì tháp và cọc cùng vuông góc với mặt đất và các tia nắng mặt trời song song nên hai tam giác vuông tạo thành đồng dạng với nhau.",
                "Bước 2 (Lập tỉ lệ thức đồng dạng): Ta có tỉ số giữa chiều cao và độ dài bóng nắng là không đổi: h / 18 = 2 / 1,5.",
                "Bước 3 (Tính chiều cao h): Suy ra h = (18 × 2) / 1,5 = 36 / 1,5 = 24 (m).",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Cho tam giác ABC có DE // BC (D ∈ AB, E ∈ AC). Biết AD = 4 cm, DB = 6 cm, AE = 5 cm. Tính độ dài đoạn EC.",
                "final_answer": "EC = 7,5 cm",
                "teacher_solution": "Theo định lý Thales: AD/DB = AE/EC ⇒ 4/6 = 5/EC ⇒ EC = (6 × 5)/4 = 7,5 (cm).",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Một cột cờ có bóng trên sân trường dài 12 m. Cùng lúc đó, một học sinh cao 1,5 m đứng gần cột cờ có bóng dài 2 m. Tính chiều cao cột cờ.",
                "final_answer": "9 m",
                "teacher_solution": "h / 12 = 1,5 / 2 ⇒ h = (12 × 1,5) / 2 = 9 (m).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Cho tam giác ABC có DE // BC (D ∈ AB, E ∈ AC). Biết AD = 3 cm, AB = 9 cm và BC = 15 cm. Tính độ dài đoạn thẳng DE.",
            "final_answer": "DE = 5 cm",
            "teacher_solution": "Theo hệ quả định lý Thales: DE/BC = AD/AB ⇒ DE/15 = 3/9 = 1/3 ⇒ DE = 5 (cm).",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Để đo chiều rộng AB của một khúc sông mà không cần sang bờ bên kia, người ta ngắm tạo hai tam giác đồng dạng trên bờ với tỉ số đồng dạng k = 4 và cạnh tương ứng trên bờ đo được dài 16 m. Tính chiều rộng khúc sông AB.",
            "final_answer": "64 m",
            "teacher_solution": "AB / 16 = 4 ⇒ AB = 16 × 4 = 64 (m).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Bài toán bóng nắng: Luôn lập tỉ số (Cao lớn / Cao nhỏ) = (Bóng lớn / Bóng nhỏ)!",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Khi tính cạnh đáy song song DE/BC, mẫu số phải là CẢ CẠNH LỚN AB (DE/BC = AD/AB), tuyệt đối không dùng AD/DB!",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Kiểm tra xem đơn vị đo (cm, m) của cả 4 đoạn thẳng trong tỉ lệ thức đã đồng nhất chưa.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 13. TOÁN 9 — MẠCH 3 (HÌNH HỌC KHÔNG GIAN): MỞ PHẲNG HÌNH TRỤ & LĂNG TRỤ 3D → 2D
    {
        "asset_id": "YD-LA-GEO-G9-13",
        "asset_no": "13",
        "skill_id": "S_G09_B30",
        "grade": 9,
        "strand_code": "HINH_HOC_VA_DO_LUONG",
        "strand_name": "Hình học, Đo lường & Không gian",
        "header_subtitle": "TOÁN 9 • HÌNH TRỤ & HÌNH NÓN • TỪ MẠNG TRẢI PHẲNG 2D ĐẾN DIỆN TÍCH XUNG QUANH 3D",
        "title": "Xưởng Bao Bì Sáng Tạo: Mở Phẳng Hình Trụ 3D Thành Hình Chữ Nhật 2D",
        "story_hook": "Khi bóc nhãn giấy bao quanh một hộp sữa hình trụ có bán kính đáy R = 4 cm, chiều cao h = 10 cm rồi trải phẳng ra bàn, nhãn giấy có hình gì và chiều dài của nó bằng đúng đại lượng nào của đáy?",
        "objective": "Nhìn thấy trực tiếp mặt xung quanh của hình trụ khi trải phẳng là một hình chữ nhật có chiều rộng bằng đường cao h và chiều dài bằng đúng CHU VI ĐÁY 2πR ⇒ S_xq = 2πRh.",
        "artistic_world": "EUCLIDEAN_ATELIER_PRO",
        "primitives_used": ["PRIM_GEOMETRY_CUT_FOLD_RAY"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "CYLINDER_NET_UNROLL",
            "control_label": "Kéo thanh trượt mở phẳng mặt xung quanh hình trụ (0% → 100%):",
            "min_val": 0,
            "max_val": 100,
            "step_val": 10,
            "default_trial": 50,
            "target_solution": 100,
            "unit": "%",
            "parameters": {"radius_R": 4.0, "height_h": 10.0, "target_solution": 100, "s_xq_pi": 80},
        },
        "math_semantics": {
            "unknown_symbol": "S_xq",
            "domain_constraint": "R > 0, h > 0",
            "invariant_relation": "Chiều dài hình chữ nhật trải phẳng = Chu vi đường tròn đáy = 2πR",
            "target_equation": "S_xq = (2πR) · h = 2π · 4 · 10 = 80π (cm²); V = πR²h = 160π (cm³)",
            "verification_type": "RULE_BOUNDED_GEOMETRY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Đừng học thuộc lòng công thức khô khan! Hãy kéo thanh trượt mở chiếc lon ra: vỏ lon biến thành tờ giấy hình chữ nhật. Cạnh đứng là chiều cao h = 10 cm, còn cạnh ngang vừa ôm trọn một vòng đáy nên dài đúng bằng chu vi hình tròn 2πR!",
            "B": "Từ hình trải phẳng: S_xq = Dài × Rộng = (2πR) × h; Diện tích toàn phần S_tp = S_xq + 2·S_đáy = 2πRh + 2πR².",
            "C": "So sánh với khai triển mặt xung quanh hình nón (hình quạt tròn có độ dài cung bằng 2πR và bán kính quạt là đường sinh l ⇒ S_xq_nón = πRl).",
        },
        "misconceptions": [
            "Nhầm công thức chu vi đáy (2πR) với diện tích đáy (πR²) khi tính diện tích xung quanh.",
            "Đề bài cho ĐƯỜNG KÍNH d = 8 cm nhưng quên chia đôi để lấy bán kính R = 4 cm.",
        ],
        "knowledge_activation": "Đường tròn bán kính R có chu vi C = 2πR và diện tích S = πR². Hình trụ có chiều cao h và bán kính đáy R.",
        "worked_example": {
            "problem": "Một hộp sữa hình trụ có bán kính đáy R = 4 cm và chiều cao h = 10 cm. Tính diện tích nhãn giấy dán kín mặt xung quanh hộp sữa (bỏ qua mép dán) và thể tích của hộp sữa theo π.",
            "steps": [
                "Bước 1 (Trải phẳng mặt xung quanh): Nhãn giấy trải phẳng là hình chữ nhật có chiều dài bằng chu vi đáy C = 2πR = 8π (cm) và chiều rộng h = 10 (cm).",
                "Bước 2 (Tính diện tích xung quanh): S_xq = 2πRh = 8π × 10 = 80π ≈ 251,33 (cm²).",
                "Bước 3 (Tính thể tích hình trụ): V = S_đáy · h = πR²h = π · 4² · 10 = 160π ≈ 502,65 (cm³).",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Cho hình trụ có bán kính đáy R = 5 cm và chiều cao h = 8 cm. Tính diện tích xung quanh và diện tích toàn phần của hình trụ theo π.",
                "final_answer": "S_xq = 80π cm²; S_tp = 130π cm²",
                "teacher_solution": "S_xq = 2πRh = 2π·5·8 = 80π (cm²). S_tp = 80π + 2·π·5² = 130π (cm²).",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Một chiếc cốc hình trụ có đường kính đáy d = 6 cm, chiều cao h = 12 cm. Tính thể tích chiếc cốc theo π.",
                "final_answer": "108π cm³",
                "teacher_solution": "Bán kính R = 6 : 2 = 3 (cm). Thể tích V = πR²h = π · 3² · 12 = 108π (cm³).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Một tấm tôn hình chữ nhật dài 12π cm, rộng 10 cm được cuộn tròn lại vừa khít (ghép hai cạnh 10 cm) để làm mặt xung quanh của một chiếc thùng hình trụ cao 10 cm. Tính bán kính đáy của chiếc thùng đó.",
            "final_answer": "R = 6 cm",
            "teacher_solution": "Chu vi đáy thùng bằng chiều dài tấm tôn: 2πR = 12π ⇒ R = 6 (cm).",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một con lăn sơn tường hình trụ có đường kính 10 cm và chiều dài trục lăn 25 cm. Khi con lăn quay đúng 10 vòng trên tường phẳng thì diện tích mặt tường được phủ sơn là bao nhiêu cm² (tính theo π)?",
            "final_answer": "2500π cm²",
            "teacher_solution": "Bán kính R = 5 cm. Diện tích 1 vòng lăn là S_xq = 2π·5·25 = 250π (cm²). Sau 10 vòng: 10 × 250π = 2500π (cm²).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Mặt xung quanh hình trụ trải phẳng = Hình chữ nhật (Dài = 2πR, Rộng = h) → S_xq = 2πRh.",
                    "Thể tích hình trụ = Diện tích đáy × Chiều cao → V = πR²h.",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Đọc kỹ đề bài cho BÁN KÍNH R hay ĐƯỜNG KÍNH d! Nếu cho đường kính d thì phải tính R = d : 2 ngay dòng đầu tiên.",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Thứ nguyên đơn vị: Diện tích mang bậc hai (cm²), Thể tích mang bậc ba (cm³).",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 14. TOÁN 7–8 — MẠCH 4 (THỐNG KÊ): ĐÒN BẨY TRUNG BÌNH CỘNG VS TRUNG VỊ
    {
        "asset_id": "YD-LA-STAT-G7-14",
        "asset_no": "14",
        "skill_id": "S_G07_B18",
        "grade": 7,
        "strand_code": "THONG_KE_VA_XAC_SUAT",
        "strand_name": "Thống kê, Xác suất & Toán Ứng dụng",
        "header_subtitle": "TOÁN 7–8 • CÁC SỐ ĐẶC TRƯNG ĐO XU THẾ TRUNG TÂM • SỐ TRUNG BÌNH VS. TRUNG VỊ",
        "title": "Đòn Bẩy Dữ Liệu: Số Trung Bình Cộng vs. Trung Vị Khi Có Giá Trị Ngoại Lai",
        "story_hook": "Năm nhân viên trong quán có mức thưởng là 4, 5, 6, 7 và 8 triệu đồng (Trung bình = 6, Trung vị = 6). Nhưng khi người thứ 5 trúng thưởng đột biến 28 triệu đồng, số Trung bình vọt lên 10 triệu (không ai trong 4 người đầu đạt tới!), trong khi Trung vị vẫn đứng vững ở mức 6 triệu!",
        "objective": "Hiểu số Trung bình cộng (x̄) đóng vai trò là TÂM KHỐI LƯỢNG VẬT LÝ trên thanh đòn bẩy (rất nhạy cảm với giá trị ngoại lai), còn Trung vị (M_e) là mốc đứng giữa nên đại diện tốt hơn khi dữ liệu có độ lệch lớn.",
        "artistic_world": "DATA_OBSERVATORY_LAB",
        "primitives_used": ["PRIM_STAT_PROB_SIMULATOR"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "SEESAW_MEAN_MEDIAN_OUTLIER",
            "control_label": "Kéo thay đổi giá trị thứ 5 (Điểm ngoại lai x₅) trên thanh đòn bẩy:",
            "min_val": 8,
            "max_val": 38,
            "step_val": 5,
            "default_trial": 28,
            "target_solution": 28,
            "unit": "triệu",
            "parameters": {"base_values": [4, 5, 6, 7], "default_x5": 28, "target_solution": 28, "median_fixed": 6.0},
        },
        "math_semantics": {
            "unknown_symbol": "x_bar",
            "domain_constraint": "x_1 ≤ x_2 ≤ x_3 ≤ x_4 ≤ x_5",
            "invariant_relation": "∑(x_i - x̄) = 0 (Cân bằng mô-men lực quanh điểm tựa x̄); M_e = x_3 = 6",
            "target_equation": "Với dãy {4, 5, 6, 7, 28}: x̄ = (4+5+6+7+28)/5 = 10; Trung vị M_e = 6",
            "verification_type": "THEORETICAL_DISTRIBUTION_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Hãy kéo khối màu đỏ (x₅) chạy ra xa về bên phải: chiếc gối tựa màu vàng (Số trung bình cộng x̄) phải dịch chuyển theo sang phải để thanh gỗ không bị lật! Nhưng viên gạch màu xanh lá đứng ở vị trí số 3 chính giữa (Trung vị M_e = 6) thì không hề nhúc nhích!",
            "B": "Sắp xếp mẫu số liệu theo thứ tự không giảm. Tính số trung bình x̄ = Tổng / N và tìm số đứng chính giữa (Trung vị M_e).",
            "C": "Giải thích đẳng thức vật lý ∑(x_i - x̄) = 0: Tổng độ lệch bên trái số trung bình luôn triệt tiêu đúng bằng tổng độ lệch bên phải.",
        },
        "misconceptions": [
            "Tìm Trung vị M_e mà QUÊN SẮP XẾP dãy số liệu theo thứ tự từ bé đến lớn trước khi lấy số ở giữa.",
            "Dùng số Trung bình cộng để đại diện cho mẫu số liệu có chứa giá trị bất thường (ngoại lai) quá lớn hoặc quá nhỏ.",
        ],
        "knowledge_activation": "Số trung bình cộng x̄ bằng tổng các giá trị chia cho số các giá trị. Trung vị M_e là giá trị đứng chính giữa sau khi đã sắp xếp dãy số theo thứ tự không giảm.",
        "worked_example": {
            "problem": "Điểm kiểm tra của một nhóm 5 học sinh là: 6; 4; 28; 7; 5 (thang điểm 30). Hãy tìm số trung bình cộng, trung vị của mẫu số liệu và cho biết số nào đại diện tốt hơn cho mặt bằng chung của nhóm.",
            "steps": [
                "Bước 1 (Tính số trung bình cộng): x̄ = (6 + 4 + 28 + 7 + 5) / 5 = 50 / 5 = 10.",
                "Bước 2 (Sắp xếp & Tìm trung vị): Sắp xếp dãy theo thứ tự tăng dần: 4; 5; 6; 7; 28. Số đứng chính giữa (vị trí thứ 3) là Trung vị M_e = 6.",
                "Bước 3 (Nhận xét ý nghĩa): Vì có giá trị ngoại lai 28 chênh lệch rất lớn so với các giá trị còn lại (4; 5; 6; 7 đều nhỏ hơn 10) nên Trung vị M_e = 6 đại diện tốt hơn số trung bình cộng.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Tìm số trung bình cộng và trung vị của mẫu số liệu sau: 12; 8; 15; 10; 20.",
                "final_answer": "x̄ = 13; M_e = 12",
                "teacher_solution": "Sắp xếp: 8; 10; 12; 15; 20 ⇒ Trung vị M_e = 12. Số trung bình: x̄ = (8+10+12+15+20)/5 = 65/5 = 13.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Tìm trung vị của mẫu số liệu gồm 6 giá trị đã sắp xếp: 3; 5; 7; 9; 11; 19.",
                "final_answer": "M_e = 8",
                "teacher_solution": "Vì cỡ mẫu N = 6 (chẵn) nên trung vị là trung bình cộng của hai số đứng giữa (thứ 3 và thứ 4): M_e = (7 + 9)/2 = 8.",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Một mẫu số liệu gồm 4 số tự nhiên có số trung bình cộng bằng 9. Khi thêm số thứ năm là 29 vào mẫu thì số trung bình cộng mới bằng bao nhiêu?",
            "final_answer": "13",
            "teacher_solution": "Tổng của 4 số đầu là 4 × 9 = 36. Tổng của 5 số là 36 + 29 = 65 ⇒ Số trung bình mới là 65 : 5 = 13.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Thời gian chạy 100m (tính bằng giây) của 5 vận động viên là: 13; 14; 12; 15; 36 (vận động viên thứ 5 bị vấp ngã). Nên dùng số trung bình cộng hay trung vị để đánh giá tốc độ chung của đội?",
            "final_answer": "Dùng Trung vị M_e = 14 giây",
            "teacher_solution": "Sắp xếp: 12; 13; 14; 15; 36. Do 36 giây là giá trị bất thường nên dùng Trung vị M_e = 14 giây phản ánh đúng hơn số trung bình (18 giây).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Tìm Trung vị M_e: Bước số 1 BẮT BUỘC là SẮP XẾP dãy số từ bé đến lớn!",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Khi dãy có số phần tử CHẴN, Trung vị bằng trung bình cộng của HAI số đứng chính giữa.",
                    "Khi có giá trị ngoại lai (quá lớn/quá bé), phải chọn TRUNG VỊ thay vì Số trung bình.",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Số trung bình cộng luôn nằm giữa giá trị nhỏ nhất (Min) và giá trị lớn nhất (Max) của dãy.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 15. TOÁN 8–9 — MẠCH 4 (XÁC SUẤT): MÔ PHỎNG MONTE CARLO & HỘI TỤ XÁC SUẤT
    {
        "asset_id": "YD-LA-STAT-G8-15",
        "asset_no": "15",
        "skill_id": "S_G09_B22",
        "grade": 9,
        "strand_code": "THONG_KE_VA_XAC_SUAT",
        "strand_name": "Thống kê, Xác suất & Toán Ứng dụng",
        "header_subtitle": "TOÁN 8–9 • XÁC SUẤT THỰC NGHIỆM & XÁC SUẤT LÝ THUYẾT • PHÒNG THÍ NGHIỆM MONTE CARLO",
        "title": "Phòng Thí Nghiệm Monte Carlo: Hội Tụ Xác Suất Thực Nghiệm Về Xác Suất Lý Thuyết",
        "story_hook": "Khi gieo một con xúc xắc cân đối chỉ 10 lần, biến cố 'Xuất hiện mặt số chẵn' có thể chỉ xảy ra 3 lần (30%) hoặc tới 7 lần (70%). Nhưng điều kỳ diệu gì sẽ xảy ra khi máy tính gieo liên tiếp 1000 lần?",
        "objective": "Trực tiếp trải nghiệm Luật Số Lớn: khi số phép thử N tăng lớn (10 → 100 → 1000), xác suất thực nghiệm k/N sẽ dao động hẹp dần và hội tụ sát về xác suất lý thuyết P(A) = n(A)/n(Ω).",
        "artistic_world": "DATA_OBSERVATORY_LAB",
        "primitives_used": ["PRIM_STAT_PROB_SIMULATOR"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "MONTE_CARLO_PROBABILITY",
            "control_label": "Chọn số lần thực hiện phép thử ngẫu nhiên N (lần gieo):",
            "min_val": 10,
            "max_val": 1000,
            "step_val": 50,
            "default_trial": 100,
            "target_solution": 1000,
            "unit": "lần",
            "parameters": {"favorable_outcomes": 3, "total_outcomes": 6, "theoretical_p": 0.5, "target_solution": 1000},
        },
        "math_semantics": {
            "unknown_symbol": "P_A",
            "domain_constraint": "0 ≤ P(A) ≤ 1; n(Ω) = 6",
            "invariant_relation": "P(A) = n(A) / n(Ω) = 3 / 6 = 0,5; lim_{N→∞} (k/N) = P(A)",
            "target_equation": "Ω = {1; 2; 3; 4; 5; 6} ⇒ n(Ω) = 6; A = {2; 4; 6} ⇒ n(A) = 3 ⇒ P(A) = 3/6 = 1/2",
            "verification_type": "THEORETICAL_DISTRIBUTION_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Bấm thử 'Gieo 10 lần': đường biểu diễn còn nhảy lên xuống thất thường. Nhưng khi bạn kéo lên 'Gieo 1000 lần', đường màu xanh sẽ bám sát vào vạch đích màu đỏ P(A) = 0,50!",
            "B": "Liệt kê không gian mẫu Ω gồm các kết quả đồng khả năng, đếm số kết quả thuận lợi n(A) và tính tỉ số P(A) = n(A)/n(Ω).",
            "C": "Ứng dụng xác suất thực nghiệm để ước lượng số lượng cá thể trong hồ hoặc kiểm định xem một con xúc xắc có bị làm lệch trọng tâm hay không.",
        },
        "misconceptions": [
            "Ngộ nhận của con bạc (Gambler's Fallacy): tưởng rằng sau 3 lần ra mặt lẻ liên tiếp thì lần thứ 4 chắc chắn phải ra mặt chẵn.",
            "Đếm thiếu kết quả trong không gian mẫu khi gieo đồng thời 2 đồng xu hoặc 2 xúc xắc.",
        ],
        "knowledge_activation": "Trong phép thử ngẫu nhiên có n(Ω) kết quả đồng khả năng, nếu biến cố A có n(A) kết quả thuận lợi thì xác suất lý thuyết của A là P(A) = n(A) / n(Ω).",
        "worked_example": {
            "problem": "Gieo một con xúc xắc cân đối và đồng chất 1 lần. Tính xác suất lý thuyết của biến cố A: 'Số chấm xuất hiện là một số chẵn'. Nếu gieo xúc xắc 600 lần thì dự đoán biến cố A xuất hiện khoảng bao nhiêu lần?",
            "steps": [
                "Bước 1 (Xác định không gian mẫu): Tập hợp các kết quả có thể xảy ra là Ω = {1; 2; 3; 4; 5; 6} ⇒ n(Ω) = 6 kết quả đồng khả năng.",
                "Bước 2 (Đếm kết quả thuận lợi & Tính xác suất): Các kết quả thuận lợi cho biến cố A (số chẵn) là {2; 4; 6} ⇒ n(A) = 3. Vậy P(A) = 3/6 = 1/2 = 0,5.",
                "Bước 3 (Dự đoán bằng xác suất): Khi số phép thử N = 600 đủ lớn, k/600 ≈ P(A) = 0,5 ⇒ Số lần xuất hiện mặt chẵn khoảng k ≈ 600 × 0,5 = 300 (lần).",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Một hộp có 10 quả bóng cùng kích thước được đánh số từ 1 đến 10. Lấy ngẫu nhiên 1 quả bóng. Tính xác suất để lấy được quả bóng ghi số nguyên tố.",
                "final_answer": "2/5 (hay 0,4)",
                "teacher_solution": "Các số nguyên tố từ 1 đến 10 là {2; 3; 5; 7} (4 kết quả thuận lợi). Xác suất P = 4/10 = 2/5.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Tung một đồng xu cân đối 200 lần thấy có 96 lần xuất hiện mặt Ngửa (N). Tính xác suất thực nghiệm của biến cố xuất hiện mặt Ngửa.",
                "final_answer": "12/25 (hay 0,48)",
                "teacher_solution": "Xác suất thực nghiệm là: k/N = 96 / 200 = 12/25 = 0,48.",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Gieo đồng thời hai đồng xu cân đối và đồng chất. Tính xác suất của biến cố B: 'Có ít nhất một đồng xu xuất hiện mặt Ngửa'.",
            "final_answer": "3/4 (hay 0,75)",
            "teacher_solution": "Không gian mẫu Ω = {NN, NS, SN, SS} gồm 4 kết quả đồng khả năng. Biến cố B = {NN, NS, SN} có 3 kết quả ⇒ P(B) = 3/4.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Kiểm tra ngẫu nhiên 500 sản phẩm của một dây chuyền thấy có 10 sản phẩm bị lỗi. Trong một lô hàng 3000 sản phẩm của dây chuyền đó, hãy ước lượng có khoảng bao nhiêu sản phẩm đạt chuẩn (không lỗi)?",
            "final_answer": "2940 sản phẩm",
            "teacher_solution": "Xác suất thực nghiệm sản phẩm đạt chuẩn là (500 - 10)/500 = 490/500 = 0,98. Trong 3000 sản phẩm có khoảng 3000 × 0,98 = 2940 sản phẩm đạt chuẩn.",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "3 bước chuẩn tính xác suất cổ điển: (1) Đếm tổng số kết quả đồng khả năng n(Ω) → (2) Liệt kê và đếm kết quả thuận lợi n(A) → (3) Lập tỉ số P(A) = n(A)/n(Ω).",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Số 1 KHÔNG phải là số nguyên tố! Các số nguyên tố đầu tiên là: 2; 3; 5; 7; 11...",
                    "Xác suất P(A) luôn nằm trong đoạn từ 0 đến 1 (0 ≤ P(A) ≤ 1). Nếu tính ra P > 1 là chắc chắn sai!",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Tổng xác suất của biến cố A và biến cố đối Ā luôn bằng 1: P(A) + P(Ā) = 1.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 16. TOÁN 8–9 — TỔ HỢP ĐA MẠCH (HÌNH HỌC H07 + ĐẠI SỐ PHƯƠNG TRÌNH BẬC HAI & ỨNG DỤNG)
    {
        "asset_id": "YD-LA-APPL-G9-16",
        "asset_no": "16",
        "skill_id": "S_G09_B19",
        "grade": 9,
        "strand_code": "THONG_KE_VA_XAC_SUAT",
        "strand_name": "Thống kê, Xác suất & Toán Ứng dụng",
        "header_subtitle": "TOÁN 9 • TỔ HỢP HÌNH HỌC H07 + PHƯƠNG TRÌNH BẬC HAI • TỐI ƯU HÓA QUY HOẠCH",
        "title": "Quy Hoạch Lối Đi Khu Vườn Sinh Thái: Tổ Hợp Hình Học H07 & Đại Số Bậc Hai",
        "story_hook": "Một khu đất hình chữ nhật dài 20 m, rộng 14 m được làm một lối đi lát đá có bề rộng x (m) đều cả 4 phía bao quanh thảm hoa ở giữa. Muốn diện tích thảm hoa đúng bằng 160 m² thì lối đi rộng bao nhiêu mét? Vì sao chiều dài thảm hoa là (20 - 2x) chứ không phải (20 - x)?",
        "objective": "Kết hợp trực quan Hình học (lối đi bao quanh cả hai đầu làm mỗi chiều giảm đi 2x) với Đại số (giải phương trình bậc hai (20 - 2x)(14 - 2x) = 160 và loại nghiệm ngoại lai vượt quá một nửa chiều rộng).",
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "primitives_used": ["PRIM_GEOMETRY_CUT_FOLD_RAY", "PRIM_RATE_BALANCE_3D", "PRIM_STAT_PROB_SIMULATOR"],
        "interaction_level": 4,
        "interactive_engine": {
            "engine_type": "COMPOSITE_GARDEN_PATH_QUADRATIC",
            "control_label": "Kéo thử bề rộng lối đi bốn phía x (m) [0 < x < 7]:",
            "min_val": 0.5,
            "max_val": 6.0,
            "step_val": 0.5,
            "default_trial": 3.0,
            "target_solution": 2.0,
            "unit": "m",
            "parameters": {"outer_L": 20.0, "outer_W": 14.0, "target_inner_area": 160.0, "target_solution": 2.0},
        },
        "math_semantics": {
            "unknown_symbol": "x",
            "domain_constraint": "0 < x < 7 (vì 14 - 2x > 0)",
            "invariant_relation": "S_hoa(x) = (20 - 2x)(14 - 2x) = 160; S_lối_đi = 280 - 160 = 120 m²",
            "target_equation": "(20 - 2x)(14 - 2x) = 160 ⇔ x² - 17x + 30 = 0 ⇒ x₁ = 2 (Nhận); x₂ = 15 (Loại vì x < 7)",
            "verification_type": "SYMBOLIC_SYMPY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Nhìn kỹ sơ đồ khu vườn nhé: lối đi nằm ở CẢ BÊN TRÁI lẫn BÊN PHẢI thảm hoa! Vì thế chiều dài 20 m bị bớt đi x mét ở đầu trái và x mét ở đầu phải, còn lại (20 - 2x) mét! Kéo thử x = 2 m, thảm hoa sẽ có kích thước 16 m × 10 m = 160 m² vừa khít!",
            "B": "Biểu diễn kích thước hình chữ nhật bên trong là (20 - 2x) và (14 - 2x) với điều kiện 0 < x < 7. Lập phương trình diện tích (20 - 2x)(14 - 2x) = 160.",
            "C": "Giải thích ý nghĩa hình học của nghiệm ngoại lai x₂ = 15 m: tại x = 15 m, biểu thức đại số (-10) × (-16) vẫn bằng +160 nhưng độ dài hình học bị âm!",
        },
        "misconceptions": [
            "Trừ thiếu một bên lối đi: viết chiều dài còn lại là (20 - x) và chiều rộng là (14 - x).",
            "Chỉ đặt điều kiện x > 0 mà quên điều kiện chặn trên 14 - 2x > 0 ⇔ x < 7, dẫn đến nhận cả nghiệm x = 15 m.",
        ],
        "knowledge_activation": "Khi một lối đi rộng x bao quanh cả 4 phía của hình chữ nhật L × W, phần lõi bên trong có chiều dài (L - 2x) và chiều rộng (W - 2x) với điều kiện 0 < 2x < W.",
        "worked_example": {
            "problem": "Một mảnh đất hình chữ nhật dài 20 m, rộng 14 m. Người ta làm một lối đi có bề rộng x (m) đều khắp 4 phía xung quanh, phần đất hình chữ nhật ở chính giữa dùng để trồng hoa có diện tích 160 m². Tính bề rộng x của lối đi.",
            "steps": [
                "Bước 1 (Biểu diễn hình học & ĐKXĐ): Do lối đi bao quanh cả 4 phía nên thảm hoa ở giữa có chiều dài (20 - 2x) (m) và chiều rộng (14 - 2x) (m). Điều kiện: 14 - 2x > 0 ⇔ 0 < x < 7.",
                "Bước 2 (Lập phương trình bậc hai): Diện tích thảm hoa là 160 m² nên: (20 - 2x)(14 - 2x) = 160 ⇔ 4(10 - x)(7 - x) = 160 ⇔ x² - 17x + 30 = 0.",
                "Bước 3 (Giải & Lọc nghiệm hình học): Ta có (x - 2)(x - 15) = 0 ⇒ x = 2 (thỏa mãn 0 < x < 7) hoặc x = 15 (loại vì 15 > 7). Vậy bề rộng lối đi là 2 m.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Giải phương trình bậc hai: x² - 9x + 14 = 0.",
                "final_answer": "x = 2 hoặc x = 7",
                "teacher_solution": "(x - 2)(x - 7) = 0 ⇔ x = 2 hoặc x = 7.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Một mảnh vườn hình chữ nhật có chiều dài hơn chiều rộng 5 m và diện tích bằng 150 m². Tính chiều rộng và chiều dài của mảnh vườn.",
                "final_answer": "Rộng 10 m; Dài 15 m",
                "teacher_solution": "x(x + 5) = 150 (x > 0) ⇔ x² + 5x - 150 = 0 ⇒ x = 10 (nhận) hoặc x = -15 (loại). Vậy rộng 10 m, dài 15 m.",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Một bức tranh hình chữ nhật kích thước 30 cm × 20 cm được lồng vào một khung gỗ có bản rộng x (cm) đều cả 4 phía. Biết tổng diện tích cả khung và tranh là 816 cm². Tìm độ rộng x của khung gỗ.",
            "final_answer": "x = 2 cm",
            "teacher_solution": "(30 + 2x)(20 + 2x) = 816 (x > 0) ⇔ 4(15 + x)(10 + x) = 816 ⇔ x² + 25x - 54 = 0 ⇒ x = 2 (cm, nhận).",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Với lối đi khu vườn ở Ví dụ minh họa (diện tích lối đi là 20×14 - 160 = 120 m²), nếu chi phí lát đá lối đi là 250 000 đồng/m² thì tổng kinh phí lát lối đi là bao nhiêu triệu đồng?",
            "final_answer": "30 triệu đồng",
            "teacher_solution": "Tổng kinh phí lát đá lối đi là: 120 × 250 000 = 30 000 000 (đồng) = 30 triệu đồng.",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Lối đi nằm BÊN TRONG 4 phía → Trừ 2x: (Dài - 2x)(Rộng - 2x). Khung viền bọc BÊN NGOÀI 4 phía → Cộng 2x: (Dài + 2x)(Rộng + 2x)!",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Bắt buộc đặt điều kiện chiều rộng phần trong dương: Rộng - 2x > 0 ⇔ x < Rộng/2 để loại nghiệm dương quá lớn!",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Thử lại với x = 2 m: (20 - 4) × (14 - 4) = 16 × 10 = 160 m² (Khớp tuyệt đối!).",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },
]
