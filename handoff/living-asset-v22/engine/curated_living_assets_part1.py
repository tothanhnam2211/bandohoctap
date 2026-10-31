# -*- coding: utf-8 -*-
"""
BỘ DỮ LIỆU CHUYÊN SÂU — LIVING ASSETS 01..08 (MẠCH 1: SỐ HỌC & TẬP HỢP + MẠCH 2: ĐẠI SỐ & PHƯƠNG TRÌNH)
Mỗi Living Asset mang đầy đủ ngữ nghĩa Toán học, kịch bản tương tác, 3 hồ sơ học sinh (Learner A/B/C),
chẩn đoán sai lầm thực tế của học sinh Việt Nam, 4 giấy nhớ nhận thức và bài tập đồng bộ Phiếu A4.
"""

from __future__ import annotations
from typing import Any, Dict, List

LIVING_ASSETS_PART_1: List[Dict[str, Any]] = [
    # 01. TOÁN 6 — MẠCH 1 (SỐ HỌC & TẬP HỢP): ƯCLN & BÀI TOÁN LÁT GẠCH SÂN ĐÌNH
    {
        "asset_id": "YD-LA-NUM-G6-01",
        "asset_no": "01",
        "skill_id": "S_G06_B09",
        "grade": 6,
        "strand_code": "SO_HOC_VA_TAP_HOP",
        "strand_name": "Số học & Tập hợp",
        "header_subtitle": "TOÁN 6 • SỐ HỌC & TẬP HỢP • ƯỚC CHUNG LỚN NHẤT (ƯCLN)",
        "title": "Kiến Trúc Sư Sân Đình Cổ: Lát Gạch Vuông Không Cắt & Bí Mật ƯCLN",
        "story_hook": "Bác thợ cả cần lát kín nền sân đình hình chữ nhật dài 24 dm, rộng 18 dm bằng những viên gạch hình vuông nguyên vẹn (không viên nào bị cắt lẻ). Làm sao chọn được cỡ gạch lớn nhất?",
        "objective": "Hiểu bản chất hình học của Ước chung lớn nhất: cạnh viên gạch vuông lớn nhất lát khít hình chữ nhật a × b chính là ƯCLN(a, b).",
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "primitives_used": ["PRIM_GRID_TILING"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "GRID_TILING_GCD",
            "control_label": "Chọn kích thước cạnh viên gạch vuông d (dm):",
            "min_val": 1,
            "max_val": 12,
            "step_val": 1,
            "default_trial": 5,
            "target_solution": 6,
            "unit": "dm",
            "parameters": {"width": 24, "height": 18, "target_solution": 6},
        },
        "math_semantics": {
            "unknown_symbol": "d",
            "domain_constraint": "d ∈ ℕ*, 1 ≤ d ≤ 18",
            "invariant_relation": "24 ⋮ d và 18 ⋮ d, d lớn nhất ⇔ d = ƯCLN(24, 18) = 6",
            "target_equation": "ƯCLN(24, 18) = 2 · 3 = 6 (dm); Số viên gạch = (24 : 6) × (18 : 6) = 12 (viên)",
            "verification_type": "EXACT_ARITHMETIC_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Mình đừng vội tính nhẩm! Hãy kéo thanh trượt thử viên gạch cạnh 5 dm: bạn sẽ thấy cuối sân bị thừa ra một khe hẹp 4 dm (vết đỏ) phải chặt gạch. Hãy kéo đến khi toàn bộ sân hiện màu vàng khít nhau nhé!",
            "B": "Để lát kín không cắt gạch, cạnh d phải đồng thời chia hết 24 và 18. Hãy tìm tập hợp ƯC(24, 18) và chọn số lớn nhất.",
            "C": "Tổng quát hóa: Với sân a × b, vì sao tích diện tích một viên gạch lớn nhất (d²) nhân với số viên gạch luôn bằng a·b?",
        },
        "misconceptions": [
            "Nhầm lẫn giữa ƯCLN (chia nhỏ hình lớn thành các ô vuông bằng nhau) và BCNN (ghép nhiều hình nhỏ thành hình lớn).",
            "Chọn ước chung d = 2 hoặc d = 3 (lát vừa nhưng quên điều kiện 'cạnh viên gạch lớn nhất').",
        ],
        "knowledge_activation": "Muốn xếp khít các viên gạch vuông cạnh d vào cạnh dài a (không dư), thì a phải chia hết cho d (hay d là ước của a).",
        "worked_example": {
            "problem": "Một mảnh sân hình chữ nhật dài 24 dm, rộng 18 dm. Người ta muốn lát kín sân bằng các viên gạch hình vuông cạnh d (dm, d ∈ ℕ*) sao cho không có viên gạch nào bị cắt. Tìm d lớn nhất và số viên gạch cần dùng.",
            "steps": [
                "Bước 1 (Thiết lập điều kiện): Để không phải cắt gạch theo cả chiều dài và chiều rộng, ta phải có 24 ⋮ d và 18 ⋮ d, đồng thời d lớn nhất nên d = ƯCLN(24, 18).",
                "Bước 2 (Phân tích thừa số nguyên tố): 24 = 2³ · 3; 18 = 2 · 3² ⇒ ƯCLN(24, 18) = 2 · 3 = 6 (dm).",
                "Bước 3 (Tính số viên gạch): Chiều dài xếp được 24 : 6 = 4 viên; chiều rộng xếp được 18 : 6 = 3 viên ⇒ Tổng số gạch = 4 × 3 = 12 viên.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Tìm ƯCLN(36, 24) và cho biết có thể chia một tấm bìa hình chữ nhật 36 cm × 24 cm thành các hình vuông bằng nhau có cạnh lớn nhất là bao nhiêu xăng-ti-mét?",
                "final_answer": "12 cm",
                "teacher_solution": "36 = 2² · 3²; 24 = 2³ · 3 ⇒ ƯCLN(36, 24) = 2² · 3 = 12 (cm).",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Đội tình nguyện có 48 quyển vở và 32 chiếc bút muốn chia đều vào các túi quà sao cho số túi là nhiều nhất. Hỏi chia được nhiều nhất bao nhiêu túi quà?",
                "final_answer": "16 túi",
                "teacher_solution": "Số túi nhiều nhất là ƯCLN(48, 32) = 16 túi (mỗi túi có 3 quyển vở và 2 bút).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Một căn phòng hình chữ nhật kích thước 42 dm × 30 dm. Nếu lát bằng gạch vuông cạnh 6 dm thì hết bao nhiêu viên gạch?",
            "final_answer": "35 viên",
            "teacher_solution": "ƯCLN(42, 30) = 6 dm. Số viên gạch = (42 : 6) × (30 : 6) = 7 × 5 = 35 (viên).",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Bác An có hai thanh gỗ dài 120 cm và 90 cm. Bác muốn cưa cả hai thanh thành những đoạn bằng nhau dài nhất có thể mà không thừa mẩu gỗ nào. Tìm độ dài mỗi đoạn và tổng số đoạn gỗ thu được.",
            "final_answer": "30 cm; 7 đoạn",
            "teacher_solution": "Độ dài mỗi đoạn là ƯCLN(120, 90) = 30 cm. Tổng số đoạn = (120 : 30) + (90 : 30) = 4 + 3 = 7 đoạn.",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Gặp từ khóa 'chia đều lớn nhất', 'cắt hình vuông lớn nhất không dư' → Nghĩ ngay đến ƯCLN(a, b)!",
                    "Phân tích mỗi số ra thừa số nguyên tố rồi chọn các thừa số nguyên tố CHUNG với số mũ NHỎ NHẤT.",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Đừng lấy tổng diện tích chia cho cạnh d! Số viên gạch phải bằng (Dài : d) × (Rộng : d).",
                    "Tránh nhầm quy tắc: ƯCLN chọn thừa số CHUNG mũ NHỎ; BCNN chọn CHUNG & RIÊNG mũ LỚN.",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Lấy chiều dài và chiều rộng chia thử cho d xem phép chia có dư bằng 0 hay không.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 02. TOÁN 6 — MẠCH 1 (SỐ HỌC): CỘNG TRỪ SỐ NGUYÊN & TÀU NGẦM THÁM HIỂM
    {
        "asset_id": "YD-LA-NUM-G6-02",
        "asset_no": "02",
        "skill_id": "S_G06_B14",
        "grade": 6,
        "strand_code": "SO_HOC_VA_TAP_HOP",
        "strand_name": "Số học & Tập hợp",
        "header_subtitle": "TOÁN 6 • SỐ NGUYÊN • PHÉP CỘNG TRỪ SỐ NGUYÊN & QUY TẮC DẤU",
        "title": "Tàu Ngầm Thám Hiểm Rãnh Mariana: Vì Sao Trừ Đi Số Âm Lại Là Cộng?",
        "story_hook": "Tàu ngầm đang ở độ sâu -120 m so với mực nước biển. Khi thuyền trưởng ra lệnh 'Thả bỏ 3 quả tạ chì' (mỗi quả tạ từng kéo tàu chìm -15 m), tàu sẽ nổi lên hay chìm xuống?",
        "objective": "Trực quan hóa quy tắc trừ số nguyên a - (-b) = a + b thông qua cơ chế tháo bỏ vật nặng trên trục số thẳng đứng.",
        "artistic_world": "EUCLIDEAN_ATELIER_PRO",
        "primitives_used": ["PRIM_NUMBER_LINE_VECTOR"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "SUBMARINE_VECTOR_LINE",
            "control_label": "Số quả tạ chì (-15m/quả) được tháo bỏ khỏi tàu:",
            "min_val": -2,
            "max_val": 6,
            "step_val": 1,
            "default_trial": 1,
            "target_solution": 3,
            "unit": "quả tạ",
            "parameters": {"initial_depth": -120, "ballast_weight": -15, "target_solution": 3, "target_depth": -75},
        },
        "math_semantics": {
            "unknown_symbol": "k",
            "domain_constraint": "k ∈ ℤ",
            "invariant_relation": "h_moi = h_cu - k * (-15) = -120 + 15k",
            "target_equation": "(-120) - (-45) = -120 + 45 = -75 (m)",
            "verification_type": "EXACT_ARITHMETIC_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Mỗi quả tạ chì giống như một số âm (-15) kéo tàu xuống đáy biển. Khi mình BỚT ĐI (phép trừ) 3 quả tạ chì, tàu nhẹ đi và NỔI LÊN (+45 m)!",
            "B": "Biểu diễn trên trục số thẳng đứng: Bắt đầu tại -120, thực hiện phép trừ (-45) tương đương dịch chuyển 45 đơn vị theo chiều dương (hướng lên mặt biển).",
            "C": "Chứng minh tính chất đối xứng: a - b = a + (-b) với mọi a, b ∈ ℤ trên không gian vector một chiều.",
        },
        "misconceptions": [
            "Nhìn thấy hai số âm trong (-120) - (-45) liền cộng hai giá trị tuyệt đối thành -165.",
            "Quên dấu âm biểu thị độ sâu dưới mực nước biển khi kết luận.",
        ],
        "knowledge_activation": "Muốn trừ số nguyên a cho số nguyên b, ta cộng a với số đối của b: a - b = a + (-b). Đặc biệt: a - (-b) = a + b.",
        "worked_example": {
            "problem": "Tàu ngầm đang ở độ cao -120 m so với mực nước biển. Tàu tháo bỏ một khối lượng dằn tương đương độ chìm -45 m (tức là thực hiện phép tính (-120) - (-45)). Hỏi tàu ngầm ở độ cao mới là bao nhiêu mét?",
            "steps": [
                "Bước 1 (Chuyển phép trừ thành cộng số đối): Số đối của (-45) là +45, nên (-120) - (-45) = (-120) + 45.",
                "Bước 2 (Cộng hai số nguyên trái dấu): Ta lấy số lớn trừ số nhỏ: 120 - 45 = 75, rồi đặt dấu của số có phần tự nhiên lớn hơn (dấu '-' của -120).",
                "Bước 3 (Kết luận): Độ cao mới của tàu ngầm là -75 m (tức là tàu đã nổi lên cao hơn 45 m).",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Thực hiện phép tính: A = (-85) - (-35) + (-20).",
                "final_answer": "-70",
                "teacher_solution": "A = (-85) + 35 + (-20) = (-50) + (-20) = -70.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Nhiệt độ buổi tối tại Sa Pa là -2°C, đến nửa đêm giảm thêm 4°C nữa. Hỏi nhiệt độ lúc nửa đêm là bao nhiêu độ C?",
                "final_answer": "-6°C",
                "teacher_solution": "Nhiệt độ lúc nửa đêm là: (-2) - 4 = (-2) + (-4) = -6 (°C).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Tìm số nguyên x biết: x - (-28) = -12.",
            "final_answer": "x = -40",
            "teacher_solution": "x + 28 = -12 ⇒ x = -12 - 28 = -40.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một thiết bị khảo sát biển lặn từ độ cao -30 m xuống thêm 50 m, sau đó nổi lên 25 m. Tính độ cao cuối cùng của thiết bị so với mực nước biển.",
            "final_answer": "-55 m",
            "teacher_solution": "Độ cao cuối cùng: (-30) - 50 + 25 = -80 + 25 = -55 (m).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Gặp hai dấu trừ đứng liền nhau '- (-b)' → Đổi ngay thành dấu cộng '+ b'!",
                    "Hãy tưởng tượng trục số thẳng đứng: Cộng số dương là đi LÊN, cộng số âm là đi XUỐNG.",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Cộng hai số trái dấu: Lấy phần số lớn TRỪ phần số bé, mang dấu của bên lớn hơn.",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Ở độ sâu -120 m mà nổi lên 45 m thì phải gần mặt biển hơn (-75 m lớn hơn -120 m).",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 03. TOÁN 6 — MẠCH 1 (SỐ HỌC): PHÂN SỐ, TỈ SỐ PHẦN TRĂM & ĐẠI LƯỢNG BẤT BIẾN
    {
        "asset_id": "YD-LA-NUM-G6-03",
        "asset_no": "03",
        "skill_id": "S_G06_B25",
        "grade": 6,
        "strand_code": "SO_HOC_VA_TAP_HOP",
        "strand_name": "Số học & Tập hợp",
        "header_subtitle": "TOÁN 6 • PHÂN SỐ & TỈ SỐ PHẦN TRĂM • BÀI TOÁN PHA CHẾ BẤT BIẾN",
        "title": "Phòng Pha Chế Cam Tươi: Phân Số, Tỉ Số Phần Trăm & Đại Lượng Bất Biến",
        "story_hook": "Một bình nước cam 400 ml có chứa 25% cốt cam nguyên chất. Khi bạn rót thêm 100 ml nước lọc vào bình, nồng độ cốt cam thay đổi thế nào và đại lượng nào tuyệt đối không đổi?",
        "objective": "Nắm vững mối liên hệ giữa phân số, tỉ số phần trăm và phát hiện 'đại lượng bất biến' (lượng chất tan không đổi khi chỉ thêm nước).",
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "primitives_used": ["PRIM_RATIO_MIXTURE_LAB"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "RATIO_MIXTURE_BEAKER",
            "control_label": "Lượng nước lọc rót thêm vào bình ΔV (ml):",
            "min_val": 0,
            "max_val": 400,
            "step_val": 25,
            "default_trial": 50,
            "target_solution": 100,
            "unit": "ml",
            "parameters": {"initial_total": 400, "solute_ml": 100, "target_solution": 100, "target_pct": 20.0},
        },
        "math_semantics": {
            "unknown_symbol": "V_them",
            "domain_constraint": "V_them ≥ 0",
            "invariant_relation": "V_cam = 25% × 400 = 100 ml (Bất biến khi thêm nước)",
            "target_equation": "C%_mới = 100 / (400 + 100) × 100% = 20%",
            "verification_type": "EXACT_ARITHMETIC_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Hãy nhìn vạch màu cam đậm dưới đáy bình: dù bạn đổ thêm bao nhiêu nước lọc trong suốt, lượng cốt cam nguyên chất vẫn giữ nguyên 100 ml!",
            "B": "Tính lượng cốt cam ban đầu: 400 × 25% = 100 ml. Sau khi thêm 100 ml nước, tổng thể tích mới là 500 ml ⇒ Tỉ số phần trăm mới là 100/500 = 20%.",
            "C": "Ngược lại: Muốn bình nước cam 400 ml (25%) tăng độ đậm đặc lên 40% bằng cách pha thêm cốt cam nguyên chất x (ml), phương trình bất biến lượng nước lọc là gì?",
        },
        "misconceptions": [
            "Lấy tỉ số phần trăm trừ trực tiếp hoặc quên cộng thêm lượng nước mới vào mẫu số (tổng thể tích dung dịch).",
            "Nhầm lẫn giữa bài toán 'thêm nước lọc' (cốt cam bất biến) và 'thêm cốt cam' (nước lọc bất biến).",
        ],
        "knowledge_activation": "Tỉ số phần trăm của đại lượng a so với tổng thể tích V là (a / V) × 100%. Khi chỉ thêm nước lọc, lượng chất cốt ban đầu không đổi.",
        "worked_example": {
            "problem": "Một bình nước cam dung tích 400 ml có tỉ lệ cốt cam nguyên chất là 25%. Người ta pha thêm 100 ml nước lọc vào bình. Tính tỉ số phần trăm cốt cam trong bình sau khi pha.",
            "steps": [
                "Bước 1 (Tìm đại lượng bất biến): Lượng cốt cam nguyên chất trong bình ban đầu là: 400 × 25% = 400 × (1/4) = 100 (ml).",
                "Bước 2 (Tính tổng thể tích mới): Sau khi thêm 100 ml nước lọc, thể tích nước cam trong bình là: 400 + 100 = 500 (ml).",
                "Bước 3 (Tính tỉ số phần trăm mới): Tỉ lệ cốt cam lúc sau là: (100 / 500) × 100% = 20%.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Trong 200 g dung dịch nước muối có chứa 10 g muối tinh. Tính tỉ số phần trăm của muối trong dung dịch.",
                "final_answer": "5%",
                "teacher_solution": "Tỉ số phần trăm của muối là: (10 / 200) × 100% = 5%.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Một lớp học có 40 học sinh, trong đó 3/5 số học sinh tham gia câu lạc bộ STEM. Hỏi có bao nhiêu học sinh tham gia câu lạc bộ STEM?",
                "final_answer": "24 học sinh",
                "teacher_solution": "Số học sinh tham gia CLB STEM là: 40 × (3/5) = 24 (học sinh).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Có 300 g dung dịch đường nồng độ 20%. Cần pha thêm bao nhiêu gam nước lọc để được dung dịch đường mới có nồng độ 15%?",
            "final_answer": "100 g nước",
            "teacher_solution": "Khối lượng đường bất biến: 300 × 20% = 60 g. Khối lượng dung dịch lúc sau: 60 : 15% = 400 g ⇒ Nước thêm vào: 400 - 300 = 100 g.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một chiếc balo có giá niêm yết 350 000 đồng. Nhân dịp khai giảng, cửa hàng giảm giá 20%. Hỏi bạn Minh cần trả bao nhiêu tiền để mua chiếc balo đó?",
            "final_answer": "280 000 đồng",
            "teacher_solution": "Số tiền sau giảm giá chiếm 100% - 20% = 80% giá niêm yết. Số tiền phải trả: 350 000 × 80% = 280 000 (đồng).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Tìm của một số: Lấy số đó NHÂN với phân số (hoặc tỉ số %).",
                    "Bài toán pha chế: Hỏi xem cái gì KHÔNG ĐỔI (cốt cam hay nước lọc) để tính nó trước tiên!",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Khi thêm nước hoặc thêm chất tan, mẫu số (tổng khối lượng dung dịch) BẮT BUỘC phải cộng thêm lượng vừa đổ vào.",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Pha thêm nước lọc thì dung dịch loãng ra → Tỉ số % mới (20%) phải nhỏ hơn ban đầu (25%).",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 04. TOÁN 7 — MẠCH 1 (SỐ THỰC & SỐ VÔ TỈ): ĐƯỜNG CHÉO HÌNH VUÔNG & CĂN BẬC HAI CỦA 2
    {
        "asset_id": "YD-LA-NUM-G7-04",
        "asset_no": "04",
        "skill_id": "S_G07_B05",
        "grade": 7,
        "strand_code": "SO_HOC_VA_TAP_HOP",
        "strand_name": "Số học & Tập hợp",
        "header_subtitle": "TOÁN 7 • SỐ VÔ TỈ & CĂN BẬC HAI • BÍ ẨN ĐƯỜNG CHÉO HÌNH VUÔNG ĐƠN VỊ",
        "title": "Bí Ẩn Đường Chéo Hình Vuông Đơn Vị & Sự Ra Đời Của Số Vô Tỉ √2",
        "story_hook": "Ghép hai hình vuông nhỏ cạnh 1 dm (diện tích 1 dm²) bằng cách cắt theo đường chéo thành 4 tam giác vuông rồi xếp lại thành một hình vuông lớn diện tích 2 dm². Cạnh của hình vuông lớn chính là đường chéo d của hình vuông nhỏ: d² = 2 ⇒ d = √2!",
        "objective": "Hiểu ý nghĩa hình học cụ thể của số vô tỉ √2 (cạnh hình vuông có diện tích bằng 2) và cách biểu diễn chính xác điểm √2 trên trục số bằng compa.",
        "artistic_world": "EUCLIDEAN_ATELIER_PRO",
        "primitives_used": ["PRIM_GEOMETRY_CUT_FOLD_RAY", "PRIM_NUMBER_LINE_VECTOR"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "SQRT2_COMPASS_ZOOM",
            "control_label": "Thử nghiệm cạnh hình vuông d để diện tích d² tiệm cận 2:",
            "min_val": 1.0,
            "max_val": 2.0,
            "step_val": 0.05,
            "default_trial": 1.40,
            "target_solution": 1.4142,
            "unit": "dm",
            "parameters": {"target_area": 2.0, "target_solution": 1.4142},
        },
        "math_semantics": {
            "unknown_symbol": "d",
            "domain_constraint": "d > 0",
            "invariant_relation": "d² = 1² + 1² = 2 ⇒ d = √2 ≈ 1,41421356...",
            "target_equation": "d² = 2 (d > 0) ⇔ d = √2 ∈ I (Số vô tỉ)",
            "verification_type": "SYMBOLIC_SYMPY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Đừng sợ ký hiệu √2! Nó chỉ đơn giản là độ dài đường chéo của một viên gạch vuông cạnh 1 dm. Khi lấy compa quay đường chéo đó xuống trục số, kim compa chạm đúng điểm √2 ≈ 1,414...",
            "B": "Hai hình vuông diện tích 1 dm² cắt ghép thành hình vuông lớn có diện tích S = 2 dm². Vì S = d² = 2 nên cạnh hình vuông lớn là d = √2.",
            "C": "Chứng minh phản chứng cổ điển: Vì sao không tồn tại phân số tối giản m/n nào thỏa mãn (m/n)² = 2?",
        },
        "misconceptions": [
            "Tưởng nhầm √2 bằng đúng 1,4 hoặc 1,41 (thực chất 1,4² = 1,96 < 2 và 1,41² = 1,9881 < 2).",
            "Gộp nhầm căn bậc hai số học: viết √9 = ±3 (chuẩn SGK Toán 7: căn bậc hai số học của a ≥ 0 là số KHÔNG ÂM).",
        ],
        "knowledge_activation": "Căn bậc hai số học của một số a không âm (ký hiệu √a) là số x không âm sao cho x² = a.",
        "worked_example": {
            "problem": "Cắt hai hình vuông cạnh 1 dm dọc theo đường chéo thành 4 tam giác vuông bằng nhau rồi ghép thành một hình vuông lớn. Tính diện tích và độ dài cạnh của hình vuông lớn (làm tròn đến chữ số thập phân thứ hai).",
            "steps": [
                "Bước 1 (Bảo toàn diện tích): Diện tích mỗi hình vuông nhỏ là 1² = 1 (dm²). Hình vuông lớn ghép từ hai hình vuông nhỏ nên có diện tích S = 1 + 1 = 2 (dm²).",
                "Bước 2 (Thiết lập quan hệ cạnh): Gọi độ dài cạnh hình vuông lớn là d (d > 0). Ta có d² = 2 ⇒ d = √2 (dm).",
                "Bước 3 (Xấp xỉ thập phân): Vì √2 = 1,4142... nên làm tròn đến chữ số thập phân thứ hai ta được d ≈ 1,41 (dm).",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Tính giá trị biểu thức: M = √49 + √25 - 2·√9.",
                "final_answer": "6",
                "teacher_solution": "M = 7 + 5 - 2·3 = 12 - 6 = 6.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Một tấm thảm hình vuông có diện tích 81 m². Tính độ dài cạnh và chu vi của tấm thảm đó.",
                "final_answer": "Cạnh 9 m; Chu vi 36 m",
                "teacher_solution": "Độ dài cạnh tấm thảm: a = √81 = 9 (m). Chu vi tấm thảm: 4 × 9 = 36 (m).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "So sánh hai số thực không dùng máy tính: A = 5 và B = √23.",
            "final_answer": "5 > √23",
            "teacher_solution": "Ta có 5 = √25. Vì 25 > 23 > 0 nên √25 > √23, tức là 5 > √23.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Sân trường có một bồn hoa hình vuông diện tích 18 m². Bác bảo vệ muốn căng dây đèn trang trí dọc theo cạnh bồn hoa. Hỏi mỗi cạnh bồn hoa dài khoảng bao nhiêu mét (làm tròn đến hàng phần mười)?",
            "final_answer": "4,2 m",
            "teacher_solution": "Độ dài cạnh bồn hoa là √18 ≈ 4,2426... Làm tròn đến hàng phần mười được 4,2 (m).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Biết diện tích hình vuông S → Cạnh hình vuông luôn bằng √S (với S ≥ 0).",
                    "Muốn so sánh số nguyên k với √a, hãy đưa k vào trong căn: k = √(k²).",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Căn bậc hai số học √a LUÔN KHÔNG ÂM: √16 = 4 (tuyệt đối không viết √16 = -4).",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Bình phương lại kết quả vừa tìm được xem có bằng đúng số dưới dấu căn hay không.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 05. TOÁN 7 — MẠCH 2 (ĐẠI SỐ): TỈ LỆ THỨC & DÃY TỈ SỐ BẰNG NHAU
    {
        "asset_id": "YD-LA-ALG-G7-05",
        "asset_no": "05",
        "skill_id": "S_G07_B12",
        "grade": 7,
        "strand_code": "DAI_SO_VA_HAM_SO",
        "strand_name": "Đại số, Phương trình & Hàm số",
        "header_subtitle": "TOÁN 7 • ĐẠI SỐ • TỈ LỆ THỨC & TÍNH CHẤT DÃY TỈ SỐ BẰNG NHAU",
        "title": "Trạm Phối Trộn Hợp Kim Đồng – Kẽm & Bản Chất Dãy Tỉ Số Bằng Nhau",
        "story_hook": "Để đúc một chiếc chuông đồng thanh vang nặng 150 gam, nghệ nhân phối trộn Đồng (x) và Kẽm (y) theo tỉ lệ 3 phần Đồng đi với 2 phần Kẽm. Mỗi 'phần bằng nhau' nặng bao nhiêu gam?",
        "objective": "Hiểu giá trị chung k của dãy tỉ số bằng nhau x/a = y/b = (x+y)/(a+b) = k chính là khối lượng của MỘT PHẦN ĐƠN VỊ.",
        "artistic_world": "WARM_STORYBOOK_TACTILE",
        "primitives_used": ["PRIM_RATIO_MIXTURE_LAB", "PRIM_RATE_BALANCE_3D"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "PROPORTION_UNIT_BLOCKS",
            "control_label": "Thử nghiệm khối lượng 1 phần đơn vị k (gam/phần):",
            "min_val": 10,
            "max_val": 50,
            "step_val": 5,
            "default_trial": 20,
            "target_solution": 30,
            "unit": "g/phần",
            "parameters": {"ratio_a": 3, "ratio_b": 2, "total_sum": 150, "target_solution": 30},
        },
        "math_semantics": {
            "unknown_symbol": "k",
            "domain_constraint": "x, y > 0",
            "invariant_relation": "x/3 = y/2 = (x + y)/(3 + 2) = k",
            "target_equation": "x/3 = y/2 = 150/5 = 30 ⇒ x = 90; y = 60",
            "verification_type": "SYMBOLIC_SYMPY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Nhìn 3 thanh Đồng màu cam và 2 thanh Kẽm màu xanh: tất cả có 3 + 2 = 5 thanh bằng nhau nặng tổng cộng 150 gam. Vậy mỗi thanh nặng đúng 150 : 5 = 30 gam!",
            "B": "Viết dãy tỉ số x/3 = y/2 và áp dụng tính chất dãy tỉ số bằng nhau với tổng x + y = 150.",
            "C": "Mở rộng khi đề bài cho hiệu (x - y = 30) hoặc cho điều kiện có hệ số (2x + 3y = 360): biến đổi tử và mẫu tương ứng 2x/6 = 3y/6.",
        },
        "misconceptions": [
            "Viết ngược tỉ số: 'x và y tỉ lệ với 3 và 2' nhưng lại viết 3x = 2y (đúng phải là x/3 = y/2).",
            "Cộng tử số x + y nhưng dưới mẫu lại lấy tích 3 × 2 hoặc hiệu 3 - 2.",
        ],
        "knowledge_activation": "Tính chất dãy tỉ số bằng nhau: Từ x/a = y/b suy ra x/a = y/b = (x + y)/(a + b) = (x - y)/(a - b) (với các mẫu khác 0).",
        "worked_example": {
            "problem": "Để làm một khối hợp kim đồng thau nặng 150 gam, người ta trộn khối lượng Đồng (x) và khối lượng Kẽm (y) tỉ lệ với 3 và 2. Tính khối lượng Đồng và Kẽm cần dùng.",
            "steps": [
                "Bước 1 (Lập tỉ lệ thức và tổng): Theo đề bài ta có x/3 = y/2 và x + y = 150 (x, y > 0).",
                "Bước 2 (Áp dụng tính chất dãy tỉ số bằng nhau): x/3 = y/2 = (x + y)/(3 + 2) = 150/5 = 30.",
                "Bước 3 (Tìm từng đại lượng): x = 30 × 3 = 90 (gam Đồng); y = 30 × 2 = 60 (gam Kẽm).",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Tìm hai số x và y biết: x/4 = y/5 và x + y = 36.",
                "final_answer": "x = 16; y = 20",
                "teacher_solution": "x/4 = y/5 = (x+y)/(4+5) = 36/9 = 4 ⇒ x = 16, y = 20.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Số cây trồng được của hai lớp 7A và 7B tỉ lệ với 5 và 7. Biết lớp 7B trồng nhiều hơn lớp 7A là 18 cây. Tính số cây mỗi lớp đã trồng.",
                "final_answer": "7A: 45 cây; 7B: 63 cây",
                "teacher_solution": "Gọi số cây của 7A, 7B là a, b. Ta có b/7 = a/5 = (b-a)/(7-5) = 18/2 = 9 ⇒ a = 45, b = 63.",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Ba chi đội 7A, 7B, 7C quyên góp được tổng cộng 240 quyển sách tỉ lệ với 3; 4; 5. Tính số sách mỗi chi đội quyên góp.",
            "final_answer": "60; 80; 100 quyển",
            "teacher_solution": "x/3 = y/4 = z/5 = (x+y+z)/(3+4+5) = 240/12 = 20 ⇒ x = 60, y = 80, z = 100.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một mảnh vườn hình chữ nhật có chu vi 80 m, tỉ số giữa chiều rộng và chiều dài là 3/5. Tính diện tích mảnh vườn đó.",
            "final_answer": "375 m²",
            "teacher_solution": "Nửa chu vi: 80 : 2 = 40 m. r/3 = d/5 = (r+d)/8 = 40/8 = 5 ⇒ r = 15 m, d = 25 m ⇒ Diện tích S = 15 × 25 = 375 m².",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "'x, y tỉ lệ thuận với a, b' → Viết ngay x/a = y/b.",
                    "Giá trị chung k = (x+y)/(a+b) chính là độ lớn của 1 phần đơn vị!",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Với bài toán hình chữ nhật cho CHU VI, nhớ chia đôi chu vi để lấy NỬA CHU VI (Dài + Rộng = P/2) trước khi áp dụng dãy tỉ số!",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Cộng lại x + y xem có đúng bằng tổng đề bài cho (90 + 60 = 150) và tỉ số 90:60 có rút gọn về 3:2 không.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 06. TOÁN 8 — MẠCH 2 (ĐẠI SỐ & HÀM SỐ): HÀM SỐ BẬC NHẤT & GIAO ĐIỂM CƯỚC TAXI
    {
        "asset_id": "YD-LA-ALG-G8-06",
        "asset_no": "06",
        "skill_id": "S_G08_B25",
        "grade": 8,
        "strand_code": "DAI_SO_VA_HAM_SO",
        "strand_name": "Đại số, Phương trình & Hàm số",
        "header_subtitle": "TOÁN 8 • HÀM SỐ BẬC NHẤT y = ax + b • GIAO ĐIỂM ĐỒ THỊ & BÀI TOÁN KINH TẾ",
        "title": "Bản Đồ Giao Điểm Chi Phí: Hàm Số Bậc Nhất y = ax + b & Chọn Hãng Taxi",
        "story_hook": "Hãng Taxi Xanh mở cửa 10 nghìn đồng, mỗi km tiếp theo giá 12 nghìn. Hãng Taxi Cam mở cửa 20 nghìn đồng, nhưng mỗi km chỉ lấy 10 nghìn. Đi bao nhiêu km thì hai hãng bằng tiền nhau?",
        "objective": "Đọc hiểu ý nghĩa thực tế của hệ số góc a (đơn giá mỗi km), tung độ gốc b (phí mở cửa) và hoành độ giao điểm x₀ (quãng đường hòa vốn).",
        "artistic_world": "STEM_COMMAND_3D",
        "primitives_used": ["PRIM_FUNCTION_GRAPH_PORTAL"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "TAXI_LINEAR_INTERSECTION",
            "control_label": "Kéo chọn quãng đường di chuyển x (km):",
            "min_val": 0,
            "max_val": 12,
            "step_val": 0.5,
            "default_trial": 3.0,
            "target_solution": 5.0,
            "unit": "km",
            "parameters": {"a1": 12, "b1": 10, "a2": 10, "b2": 20, "target_solution": 5.0, "target_y": 70.0},
        },
        "math_semantics": {
            "unknown_symbol": "x",
            "domain_constraint": "x ≥ 0",
            "invariant_relation": "y₁(x) = 12x + 10; y₂(x) = 10x + 20",
            "target_equation": "12x + 10 = 10x + 20 ⇔ 2x = 10 ⇔ x = 5 (km); y = 70 (nghìn đồng)",
            "verification_type": "SYMBOLIC_SYMPY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Khi xe chưa lăn bánh (x = 0 km), vạch xuất phát trên trục đứng chính là phí mở cửa b! Kéo xe chạy đến đúng mốc x = 5 km, hai đường thẳng cắt nhau tại 70 nghìn đồng.",
            "B": "Lập hai hàm số bậc nhất y₁ = 12x + 10 và y₂ = 10x + 20. Giải phương trình hoành độ giao điểm y₁ = y₂ để tìm điểm cắt nhau.",
            "C": "Phân tích miền tối ưu: Vì sao với quãng đường ngắn (0 < x < 5) nên chọn hãng có b nhỏ, còn đi đường dài (x > 5) lại phải chọn hãng có hệ số góc a nhỏ?",
        },
        "misconceptions": [
            "Gán nhầm hệ số a và b: lấy phí mở cửa nhân với x (viết nhầm thành y = 10x + 12).",
            "Tìm được x = 5 nhưng quên thay lại vào một trong hai hàm số để tính tung độ giao điểm y = 70.",
        ],
        "knowledge_activation": "Trong hàm số bậc nhất y = ax + b (a ≠ 0): b là giá trị ban đầu khi x = 0 (tung độ gốc), còn a là tốc độ thay đổi trên mỗi đơn vị x (hệ số góc).",
        "worked_example": {
            "problem": "Hãng xe A tính phí mở cửa 10 nghìn đồng và 12 nghìn đồng cho mỗi km di chuyển (y₁ = 12x + 10). Hãng xe B tính phí mở cửa 20 nghìn đồng và 10 nghìn đồng cho mỗi km (y₂ = 10x + 20). Hỏi đi quãng đường bao nhiêu km thì chi phí hai hãng bằng nhau?",
            "steps": [
                "Bước 1 (Thiết lập phương trình giao điểm): Để chi phí hai hãng bằng nhau, ta cho y₁ = y₂ ⇔ 12x + 10 = 10x + 20.",
                "Bước 2 (Giải phương trình bậc nhất): Chuyển vế ta được 12x - 10x = 20 - 10 ⇔ 2x = 10 ⇔ x = 5 (km).",
                "Bước 3 (Tính chi phí tại điểm cắt): Thay x = 5 vào y₁ = 12·5 + 10 = 70 (nghìn đồng). Vậy đi 5 km thì cả hai hãng đều hết 70 nghìn đồng.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Cho hàm số bậc nhất y = 3x - 2. Tính giá trị của y khi x = 4 và tìm giao điểm của đồ thị với trục tung Oy.",
                "final_answer": "y = 10; A(0; -2)",
                "teacher_solution": "Khi x = 4 thì y = 3·4 - 2 = 10. Giao với Oy tại x = 0 ⇒ y = -2, điểm A(0; -2).",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Tìm tọa độ giao điểm của hai đường thẳng (d₁): y = 2x + 1 và (d₂): y = x + 4.",
                "final_answer": "M(3; 7)",
                "teacher_solution": "Hoành độ giao điểm: 2x + 1 = x + 4 ⇔ x = 3 ⇒ y = 3 + 4 = 7. Giao điểm M(3; 7).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Xác định hàm số bậc nhất y = ax + b biết đồ thị của nó song song với đường thẳng y = 2x - 5 và đi qua điểm K(1; 6).",
            "final_answer": "y = 2x + 4",
            "teacher_solution": "Song song với y = 2x - 5 nên a = 2 và b ≠ -5. Qua K(1; 6) ⇒ 2·1 + b = 6 ⇒ b = 4 (thỏa mãn). Vậy y = 2x + 4.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một bể nước đang có sẵn 150 lít nước. Mỗi phút vòi bơm thêm vào bể 25 lít nước. Viết công thức biểu thị lượng nước y (lít) trong bể sau x (phút) và tính thời gian để bể đạt 400 lít.",
            "final_answer": "y = 25x + 150; x = 10 phút",
            "teacher_solution": "Công thức: y = 25x + 150. Khi y = 400 ⇒ 25x + 150 = 400 ⇒ 25x = 250 ⇒ x = 10 (phút).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Cái gì cố định ban đầu → là số cộng thêm b. Cái gì lặp lại theo mỗi km, mỗi phút → là hệ số nhân a·x!",
                    "Tìm giao điểm của hai đường thẳng y = a₁x + b₁ và y = a₂x + b₂: Giải phương trình a₁x + b₁ = a₂x + b₂.",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Hai đường thẳng song song khi a₁ = a₂ VÀ b₁ ≠ b₂.",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Thay x₀ vừa tìm được vào CẢ HAI công thức y₁ và y₂ xem kết quả có bằng nhau khít không.",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 07. TOÁN 8/9 — MẠCH 2 (ĐẠI SỐ): PHƯƠNG TRÌNH HỮU TỈ NĂNG SUẤT & CÂN LẬP LUẬN 3D
    {
        "asset_id": "YD-LA-ALG-G8-07",
        "asset_no": "07",
        "skill_id": "S_G08_B23",
        "grade": 8,
        "strand_code": "DAI_SO_VA_HAM_SO",
        "strand_name": "Đại số, Phương trình & Hàm số",
        "header_subtitle": "TOÁN 8–9 • PHƯƠNG TRÌNH PHÂN THỨC QUY VỀ BẬC HAI • BÀI TOÁN NĂNG SUẤT STEM",
        "title": "Tổng Công Trình Sư Vận Tải & Trồng Cây: Cân Lập Luận Phương Trình Hữu Tỉ",
        "story_hook": "Đội xe dự định chở 60 tấn hàng chia đều cho x chiếc xe. Khi khởi hành, đội được bổ sung thêm 3 xe nên mỗi xe chở nhẹ hơn dự định đúng 1 tấn. Làm sao cân bằng đại lượng để tìm x?",
        "objective": "Thiết lập phương trình chứa ẩn ở mẫu Q/x - Q/(x+k) = Δ từ bài toán năng suất/phân phối, quy đồng khử mẫu về phương trình bậc hai và loại nghiệm âm ngoại lai.",
        "artistic_world": "STEM_COMMAND_3D",
        "primitives_used": ["PRIM_RATE_BALANCE_3D"],
        "interaction_level": 4,
        "interactive_engine": {
            "engine_type": "RATE_BALANCE_RATIONAL",
            "control_label": "Thử nghiệm số xe dự định ban đầu x (chiếc):",
            "min_val": 4,
            "max_val": 20,
            "step_val": 1,
            "default_trial": 10,
            "target_solution": 12,
            "unit": "xe",
            "parameters": {"Q": 60, "k": 3, "target_delta": 1.0, "mode": "add_divisor", "target_solution": 12},
        },
        "math_semantics": {
            "unknown_symbol": "x",
            "domain_constraint": "x ∈ ℕ*",
            "invariant_relation": "60/x - 60/(x + 3) = 1 (Giả thiết Δ = 1 khóa cố định)",
            "target_equation": "60/x - 60/(x+3) = 1 ⇒ x² + 3x - 180 = 0 ⇒ x₁ = 12 (Nhận); x₂ = -15 (Loại)",
            "verification_type": "SYMBOLIC_SYMPY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Hãy thử kéo thanh trượt tới x = 10 xe: Dự định mỗi xe chở 60:10 = 6 tấn, thực tế 13 xe chở 60:13 ≈ 4,62 tấn, lệch tới 1,38 tấn ≠ 1 tấn (Cán cân bị nghiêng!). Kéo tới đúng x = 12 xe, cán cân thăng bằng hoàn hảo: 5 - 4 = 1 tấn!",
            "B": "Lập bảng 3 cột (Tổng hàng Q | Số xe | Tải trọng mỗi xe = Q/Số xe). Lấy tải trọng lúc ít xe (60/x) trừ tải trọng lúc nhiều xe (60/(x+3)) bằng đúng độ giảm Δ = 1.",
            "C": "Khử mẫu đưa về phương trình bậc hai x² + 3x - 180 = 0, phân tích thành nhân tử (x - 12)(x + 15) = 0 và giải thích ý nghĩa vật lý vì sao nghiệm đại số x₂ = -15 bị loại bỏ.",
        },
        "misconceptions": [
            "Lấy phân thức nhỏ trừ phân thức lớn: viết 60/(x+3) - 60/x = 1 dẫn đến nghiệm dương bị đảo dấu.",
            "Giải phương trình bậc hai ra hai nghiệm nhưng quên đối chiếu điều kiện x > 0 để loại nghiệm âm x₂ = -15.",
        ],
        "knowledge_activation": "Với tổng khối lượng công việc Q không đổi: Đại lượng trên mỗi đơn vị = Q / Số đơn vị. Mẫu số càng lớn thì giá trị phân thức càng nhỏ.",
        "worked_example": {
            "problem": "Một đội xe dự định dùng một số xe cùng loại để chở hết 60 tấn hàng cứu trợ. Lúc sắp khởi hành, đội được bổ sung thêm 3 xe cùng loại nên mỗi xe chở ít hơn dự định 1 tấn hàng. Hỏi lúc đầu đội có bao nhiêu xe?",
            "steps": [
                "Bước 1 (Chọn ẩn và đặt ĐKXĐ): Gọi số xe lúc đầu của đội là x (chiếc, x ∈ ℕ*). Số xe thực tế là x + 3 (chiếc).",
                "Bước 2 (Biểu diễn theo ẩn và lập phương trình): Dự định mỗi xe chở 60/x (tấn), thực tế mỗi xe chở 60/(x+3) (tấn). Vì mỗi xe chở ít hơn dự định 1 tấn nên: 60/x - 60/(x+3) = 1.",
                "Bước 3 (Khử mẫu & Lọc nghiệm): Quy đồng khử mẫu: 60(x + 3) - 60x = x(x + 3) ⇔ x² + 3x - 180 = 0 ⇔ (x - 12)(x + 15) = 0 ⇒ x = 12 (nhận) hoặc x = -15 (loại). Vậy lúc đầu đội có 12 xe.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Giải phương trình chứa ẩn ở mẫu: 30/x - 30/(x + 5) = 1 (với x > 0).",
                "final_answer": "x = 10",
                "teacher_solution": "30(x+5) - 30x = x(x+5) ⇔ x² + 5x - 150 = 0 ⇔ (x - 10)(x + 15) = 0. Vì x > 0 nên nhận x = 10.",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Một chi đoàn dự định trồng 300 cây xanh. Đến ngày lao động có 5 bạn báo vắng nên mỗi bạn đi học phải trồng thêm 2 cây. Tính số đoàn viên ban đầu.",
                "final_answer": "30 đoàn viên",
                "teacher_solution": "Phương trình: 300/(x - 5) - 300/x = 2 ⇔ x² - 5x - 750 = 0 ⇒ x = 30 (nhận) hoặc x = -25 (loại).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Một phân xưởng may 360 chiếc áo. Nhờ cải tiến kỹ thuật, mỗi ngày phân xưởng may thêm được 4 áo nên hoàn thành sớm hơn dự định 1 ngày. Tính số áo may mỗi ngày theo dự định.",
            "final_answer": "36 áo/ngày",
            "teacher_solution": "360/x - 360/(x+4) = 1 ⇔ x² + 4x - 1440 = 0 ⇔ (x - 36)(x + 40) = 0 ⇒ x = 36 (áo/ngày).",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một ca nô xuôi dòng 40 km rồi ngược dòng 40 km trên dòng sông có vận tốc dòng nước 2 km/h hết tổng cộng 4 giờ 30 phút (9/2 giờ). Tính vận tốc riêng của ca nô.",
            "final_answer": "18 km/h",
            "teacher_solution": "40/(x+2) + 40/(x-2) = 9/2 ⇔ 80x · 2 = 9(x² - 4) ⇔ 9x² - 160x - 36 = 0 ⇒ x = 18 (km/h, nhận).",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Quy tắc Vàng trên Cán cân: Luôn lấy PHÂN THỨC LỚN (mẫu nhỏ) trừ PHÂN THỨC BÉ (mẫu lớn) = Độ chênh lệch dương Δ.",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Sau khi giải phương trình bậc hai, BẮT BUỘC phải đối chiếu ĐKXĐ (x > 0, x ∈ ℕ*) để gạch bỏ nghiệm âm ngoại lai!",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Thay x = 12 vào đề bài: Lúc đầu 60:12 = 5 tấn/xe; lúc sau 60:15 = 4 tấn/xe → Giảm đúng 5 - 4 = 1 tấn!",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },

    # 08. TOÁN 9 — MẠCH 2 (ĐẠI SỐ): BÀI TOÁN HAI VÒI NƯỚC CÙNG CHẢY (CẤU TRÚC MỚI)
    {
        "asset_id": "YD-LA-ALG-G9-08",
        "asset_no": "08",
        "skill_id": "S_G09_B03",
        "grade": 9,
        "strand_code": "DAI_SO_VA_HAM_SO",
        "strand_name": "Đại số, Phương trình & Hàm số",
        "header_subtitle": "TOÁN 9 • HỆ PHƯƠNG TRÌNH & PHƯƠNG TRÌNH QUY VỀ BẬC NHẤT/BẬC HAI • BÀI TOÁN CHUNG – RIÊNG",
        "title": "Hệ Thống Hồ Chứa Thủy Điện: Bài Toán Hai Vòi Nước Cùng Chảy (1/x + 1/y = 1/T)",
        "story_hook": "Vòi I chảy riêng đầy bể trong 4 giờ, vòi II chảy riêng đầy bể trong 6 giờ. Nếu mở cả hai vòi cùng lúc thì sau bao lâu đầy bể? Vì sao không bao giờ được lấy 4 + 6 = 10 giờ?",
        "objective": "Hiểu sâu sắc bản chất bài toán công việc chung–riêng: ta không cộng thời gian hoàn thành (x + y), mà phải quy về cộng NĂNG SUẤT trong 1 đơn vị thời gian (1/x + 1/y = 1/T).",
        "artistic_world": "STEM_COMMAND_3D",
        "primitives_used": ["PRIM_DUAL_FLOW_ACCUMULATOR", "PRIM_RATE_BALANCE_3D"],
        "interaction_level": 3,
        "interactive_engine": {
            "engine_type": "DUAL_PIPE_HARMONIC",
            "control_label": "Điều chỉnh thời gian vòi II chảy một mình đầy bể y (giờ):",
            "min_val": 2,
            "max_val": 12,
            "step_val": 1,
            "default_trial": 8,
            "target_solution": 6,
            "unit": "giờ",
            "parameters": {"pipe1_hours": 4, "target_solution": 6, "target_joint_T": 2.4},
        },
        "math_semantics": {
            "unknown_symbol": "y",
            "domain_constraint": "x, y > T > 0",
            "invariant_relation": "1/x + 1/y = 1/T (Tổng phần bể chảy được trong 1 giờ)",
            "target_equation": "1/4 + 1/6 = 5/12 (bể/giờ) ⇒ T = 12/5 = 2,4 (giờ) = 2 giờ 24 phút",
            "verification_type": "SYMBOLIC_SYMPY_VERIFIED",
        },
        "learner_scaffolding": {
            "A": "Nếu một mình vòi I chảy mất 4 giờ đã đầy bể, thì khi có thêm vòi II phụ giúp, bể PHẢI ĐẦY NHANH HƠN 4 GIỜ (chứ không thể lâu tới 4 + 6 = 10 giờ!). Hãy nhìn vạch nước trong 1 giờ: vòi I chảy 1/4 bể, vòi II chảy 1/6 bể.",
            "B": "Coi toàn bộ bể nước là 1 đơn vị. Trong 1 giờ: vòi I chảy được 1/x (bể), vòi II chảy được 1/y (bể), cả hai vòi chảy được 1/T (bể) ⇒ Phương trình: 1/x + 1/y = 1/T.",
            "C": "Liên hệ Trung bình điều hòa (Harmonic Mean) và giải hệ phương trình đặt ẩn phụ u = 1/x, v = 1/y khi hai vòi mở lệch thời gian t₁·u + t₂·v = k.",
        },
        "misconceptions": [
            "Cộng trực tiếp thời gian hoàn thành của hai vòi: x + y = T.",
            "Tìm được năng suất chung trong 1 giờ là 5/12 (bể) nhưng quên nghịch đảo lại để ra thời gian T = 12/5 giờ.",
        ],
        "knowledge_activation": "Nếu một vòi chảy riêng trong x giờ thì đầy bể (x > 0), thì trong 1 giờ vòi đó chảy được 1/x (bể).",
        "worked_example": {
            "problem": "Hai vòi nước cùng chảy vào một bể cạn thì sau 2 giờ 24 phút (tức 12/5 giờ) đầy bể. Nếu chảy riêng thì vòi thứ nhất làm đầy bể nhanh hơn vòi thứ hai là 2 giờ. Hỏi nếu chảy riêng thì mỗi vòi chảy bao lâu đầy bể?",
            "steps": [
                "Bước 1 (Chọn ẩn & ĐKXĐ): Gọi thời gian vòi I chảy riêng đầy bể là x (giờ, x > 12/5). Thời gian vòi II chảy riêng đầy bể là x + 2 (giờ).",
                "Bước 2 (Quy về năng suất 1 giờ): Trong 1 giờ, vòi I chảy được 1/x (bể), vòi II chảy được 1/(x+2) (bể), cả hai vòi chảy được 1 : (12/5) = 5/12 (bể). Ta có phương trình: 1/x + 1/(x + 2) = 5/12.",
                "Bước 3 (Giải & Kết luận): Quy đồng khử mẫu: 12(2x + 2) = 5x(x + 2) ⇔ 5x² - 14x - 24 = 0 ⇒ x = 4 (nhận) hoặc x = -6/5 (loại). Vậy vòi I chảy 4 giờ, vòi II chảy 6 giờ.",
            ],
        },
        "basic_exercises": [
            {
                "id": "B1",
                "label": "Câu 2a (Cơ bản)",
                "prompt": "Vòi A chảy riêng 3 giờ đầy bể, vòi B chảy riêng 6 giờ đầy bể. Hỏi cả hai vòi cùng chảy thì sau mấy giờ đầy bể?",
                "final_answer": "2 giờ",
                "teacher_solution": "Trong 1 giờ cả hai vòi chảy được: 1/3 + 1/6 = 1/2 (bể) ⇒ Thời gian đầy bể là 1 : (1/2) = 2 (giờ).",
            },
            {
                "id": "B2",
                "label": "Câu 2b (Thực hành)",
                "prompt": "Hai tổ công nhân cùng làm một công việc trong 4 giờ thì xong. Nếu tổ I làm một mình mất 12 giờ mới xong thì tổ II làm một mình mất bao lâu?",
                "final_answer": "6 giờ",
                "teacher_solution": "1/12 + 1/y = 1/4 ⇒ 1/y = 1/4 - 1/12 = 1/6 ⇒ y = 6 (giờ).",
            },
        ],
        "advanced_exercise": {
            "id": "ADV",
            "prompt": "Hai vòi nước cùng chảy vào bể sau 6 giờ thì đầy. Nếu mở vòi I chảy trong 2 giờ rồi mở tiếp vòi II chảy trong 3 giờ thì được 2/5 bể. Tìm thời gian mỗi vòi chảy riêng đầy bể.",
            "final_answer": "Vòi I: 10 giờ; Vòi II: 15 giờ",
            "teacher_solution": "Hệ: 1/x + 1/y = 1/6 và 2/x + 3/y = 2/5. Đặt u = 1/x, v = 1/y ⇒ u = 1/10, v = 1/15 ⇒ x = 10h, y = 15h.",
        },
        "real_world_problem": {
            "id": "RW",
            "prompt": "Một hồ chứa có vòi bơm vào làm đầy hồ trong 4 giờ và một van xả đáy làm cạn hồ đầy trong 12 giờ. Nếu hồ đang cạn mà mở đồng thời cả vòi bơm và van xả thì sau mấy giờ hồ đầy?",
            "final_answer": "6 giờ",
            "teacher_solution": "Trong 1 giờ lượng nước thực tế giữ lại được là: 1/4 - 1/12 = 2/12 = 1/6 (hồ) ⇒ Hồ đầy sau 6 giờ.",
        },
        "text_notes": {
            "note1_start": {
                "title": "1. BẮT ĐẦU Ở ĐÂY NHÉ!",
                "bullets": [
                    "Coi toàn bộ công việc (hoặc bể nước) là số 1. Làm xong trong x giờ → 1 giờ làm được 1/x công việc!",
                ],
            },
            "note2_watchout": {
                "title": "2. CẨN THẬN LỖI NÀY!",
                "bullets": [
                    "Đổi thời gian hỗn số sang phân số trước khi nghịch đảo: 2 giờ 24 phút = 12/5 giờ ⇒ 1 giờ chảy được 5/12 bể.",
                ],
            },
            "note3_check": {
                "title": "3. KIỂM TRA LẠI NHÉ!",
                "bullets": [
                    "Thời gian hai vòi chảy chung T (2,4 giờ) LUÔN PHẢI NHỎ HƠN thời gian của từng vòi chảy riêng (4h và 6h).",
                ],
            },
            "note4_reflection": {"title": "HÔM NAY MÌNH ĐÃ HIỂU..."},
        },
    },
]
