import json
from pathlib import Path
import sympy as sp

RUNTIME_DIR = Path(r"D:\YOURDREAM.VN\LIVING_ASSET_FACTORY\01_STAGE1_BASELINE_RUNTIME")

def run_sympy_audit():
    x, y = sp.symbols('x y', real=True)
    Q, k, dm, dx, dt, dc = sp.symbols('Q k dm dx dt dc', positive=True)

    problems = [
        {"id": "VD5_Tr117", "tab": 1, "Q": 60, "x_expected": 12, "k": 3, "diff": 1, "C": 4.5},
        {"id": "Cau8_Tr119", "tab": 1, "Q": 120, "x_expected": 15, "k": 5, "diff": 2, "C": 6.5},
        {"id": "Cau9_Tr119", "tab": 1, "Q": 160, "x_expected": 16, "k": 4, "diff": 2, "C": 8.5},
        {"id": "Cau10_Tr119", "tab": 1, "Q": 24, "x_expected": 8, "k": 4, "diff": 1, "C": 2.5},
        {"id": "Cau5_Tr118", "tab": 2, "Q": 360, "x_expected": 36, "k": 4, "diff": 1},
        {"id": "Cau1_Tr118", "tab": 2, "Q": 240, "x_expected": 24, "k": 6, "diff": 2},
        {"id": "VD7_Tr117", "tab": 3, "Q": 300, "x_expected": 30, "k": 5, "diff": 2},
        {"id": "Cau18_Tr120", "tab": 3, "Q": 480, "x_expected": 40, "k": 8, "diff": 3},
        {"id": "Cau21_Tr121", "tab": 4, "Q": 120, "x_expected": 12, "k": 3, "diff": 1},
    ]

    results = []
    for p in problems:
        tab = p["tab"]
        Qv = sp.Rational(p["Q"])
        kv = sp.Rational(p["k"])
        dv = sp.Rational(p["diff"])

        if tab in (1, 2):
            # Q/x - Q/(x+k) = diff
            eq_1var = sp.Eq(Qv / x - Qv / (x + kv), dv)
            eq_2var = [sp.Eq(x * y, Qv), sp.Eq((x + kv) * (y - dv), Qv)]
            domain_cond = lambda r: r > 0 and (r.is_integer if tab == 1 else True)
        elif tab == 3:
            # Q/(x-k) - Q/x = diff
            eq_1var = sp.Eq(Qv / (x - kv) - Qv / x, dv)
            eq_2var = [sp.Eq(x * y, Qv), sp.Eq((x - kv) * (y + dv), Qv)]
            domain_cond = lambda r: r > kv and r.is_integer
        else:
            # Q/x - ((Q/2)/x + (Q/2)/(x+k)) = diff
            halfQ = Qv / 2
            eq_1var = sp.Eq(Qv / x - (halfQ / x + halfQ / (x + kv)), dv)
            eq_2var = [sp.Eq(x * y, Qv), sp.Eq((x + kv) * (y / 2 - dv), halfQ)]
            domain_cond = lambda r: r > 0

        roots_1var = sp.solve(eq_1var, x)
        valid_roots_1var = [r for r in roots_1var if domain_cond(r)]
        extraneous_roots_1var = [r for r in roots_1var if not domain_cond(r)]

        sols_2var = sp.solve(eq_2var, (x, y), dict=True)
        valid_sols_2var = [s for s in sols_2var if domain_cond(s[x]) and s[y] > 0]

        results.append({
            "id": p["id"],
            "tab": tab,
            "all_algebraic_roots_1var": [str(r) for r in roots_1var],
            "extraneous_roots_omitted_by_prototype": [str(r) for r in extraneous_roots_1var],
            "valid_root_1var": str(valid_roots_1var[0]) if valid_roots_1var else None,
            "matches_expected_x": (valid_roots_1var[0] == p["x_expected"]) if valid_roots_1var else False,
            "valid_2var_solution": { "x": str(valid_sols_2var[0][x]), "y": str(valid_sols_2var[0][y]) } if valid_sols_2var else None
        })

    # Audit specific mathematical defects in nang_suat.html
    math_defects_found = [
        {
            "defect_id": "MATH-DEF-01",
            "severity": "HIGH (Pedagogical & Mathematical Inversion)",
            "title": "Biến ẩn cần tìm (x) thành thanh trượt đầu vào làm tự động biến đổi giả thiết đề bài (Δm, Δt, Δc)",
            "evidence": "Trong updateAlgebraPanel() (dòng 1853-2107) và updateProblemStatementBox() (dòng 3629-3668), các tham số giả thiết gốc dataState[1].delta_m, dataState[2].early_d, dataState[3].extra_c, dataState[4].early_h bị bỏ qua hoàn toàn. Khi học sinh kéo thanh trượt x sang giá trị sai (ví dụ VD5_Tr117 kéo x từ 12 sang 10), hệ thống không báo phương trình 60/10 - 60/13 = 1.38 != 1 (sai với đề bài), mà tự động sửa đề bài gốc thành Δm = 1.38 tấn/xe và kết luận 'Nghiệm mô hình: x = 10 xe'. Hệ quả: Học sinh không thể thử sai nghiệm x trên một đề bài cố định."
        },
        {
            "defect_id": "MATH-DEF-02",
            "severity": "MEDIUM (Missing Quadratic Resolution & Extraneous Root Rejection)",
            "title": "Bỏ qua bước quy đồng khử mẫu thành phương trình bậc hai và không hiển thị nghiệm ngoại lai bị loại",
            "evidence": "Tất cả 9 bài toán thực chất là phương trình chứa ẩn ở mẫu quy về phương trình bậc hai ax^2 + bx + c = 0 có 2 nghiệm (1 nghiệm dương nhận, 1 nghiệm âm loại do điều kiện xác định x > 0 hoặc x > k). Ví dụ VD5_Tr117: 60/x - 60/(x+3) = 1 <=> x^2 + 3x - 180 = 0 <=> x = 12 (nhận) hoặc x = -15 (loại). Prototype nhảy thẳng từ phương trình chứa ẩn ở mẫu sang 'Nghiệm mô hình: x = 12', thiếu bước biến đổi tương đương / suy ra và bước đối chiếu điều kiện xác định."
        },
        {
            "defect_id": "MATH-DEF-03",
            "severity": "MEDIUM (Rounding Discrepancy in Substitute Equations)",
            "title": "Làm tròn 2 chữ số thập phân trực tiếp vào vế phải phương trình đại số gây sai lệch nghiệm khi Q không chia hết",
            "evidence": "Khi kéo thanh trượt sang bộ số không chia hết (ví dụ Tab 2: Q=360, x=35, dx=4 -> early = 360/35 - 360/39 = 1.054945...), dòng 1972 hiển thị dấu '=' tuyệt đối: '360/x - 360/(x+4) = 1.05' và khẳng định 'Nghiệm: x = 35'. Tuy nhiên nghiệm thực sự của 360/x - 360/(x+4) = 1.05 là x ≈ 35.091, không phải 35 (chỉ có Tab 1 dùng dấu xấp xỉ ≈, còn Tab 2, 3, 4 dùng dấu '=' cứng với số đã làm tròn 2 chữ số)."
        },
        {
            "defect_id": "MATH-DEF-04",
            "severity": "MEDIUM (Quiz Option A Hardcoding)",
            "title": "100% câu hỏi trắc nghiệm 4 mức độ (NB, TH, VD, VDNC) ở cả 4 Dạng đều có đáp án đúng cố định ở Phương án A (correct: 0)",
            "evidence": "Trong cả de_toan_nang_suat_gdpt2018.json và hàm buildQuizBankForCurrentState() (dòng 3914-3941), toàn bộ 16/16 câu hỏi đều gán correct: 0 (Phương án A). Thậm chí dòng 3995 hardcode chuỗi tĩnh: 'Đáp án đúng là Phương án A'."
        },
        {
            "defect_id": "MATH-DEF-05",
            "severity": "LOW-MEDIUM (Animation vs Quantity Desynchronization in Tab 2, 3, 4)",
            "title": "Số lượng vật thể 3D trong Dạng 2 (8 áo/làn), Dạng 3 (1 cây/học sinh), Dạng 4 (10 áo) không tỷ lệ với đại lượng Q",
            "evidence": "Ở Dạng 1, số xe 3D bằng đúng x + k. Nhưng ở Dạng 2, dù Q = 120 hay Q = 600 bộ áo thì băng chuyền vẫn chỉ có đúng 8 chiếc áo lặp vòng vô tận. Ở Dạng 3, có x học sinh nhưng học sinh vắng mặt (mờ đi, isAbsent = true, dòng 2350-2356) VẪN có 1 cái cây mọc lên bên cạnh mình khi chạy mô phỏng (treeMeshes vẫn thêm cây của cả học sinh vắng mặt!), mâu thuẫn trực tiếp với bản chất toán học là học sinh vắng mặt không trồng cây mà học sinh có mặt phải trồng gánh phần cây đó."
        }
    ]

    out = {
        "sympy_verified_problems": results,
        "mathematical_and_representation_defects": math_defects_found
    }
    out_path = RUNTIME_DIR / "STAGE1_SYMPY_MATH_AUDIT.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Saved SymPy audit to:", out_path)

if __name__ == "__main__":
    run_sympy_audit()
