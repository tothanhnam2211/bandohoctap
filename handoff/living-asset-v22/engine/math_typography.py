# -*- coding: utf-8 -*-
"""
YOURDREAM MATHEMATICAL TYPOGRAPHY & TYPESETTING ENGINE
(engine/math_typography.py)
Chuẩn hóa và định dạng ký hiệu Toán học đẹp, chuẩn mực GDPT 2018 cho HTML & PDF:
1. Phân số xếp dọc chuẩn mực: <span class="m-frac"><span class="m-num">A</span><span class="m-den">B</span></span>
2. Dấu căn bậc hai: <span class="m-root"><span class="m-radic">&radic;</span><span class="m-radicand">A</span></span>
3. Số mũ & chỉ số dưới: x², x³, x₁, x₂, c², a² + b²
4. Toán tử toán học chuẩn mực: ×, ·, ÷, ±, ⇒, ⇔, ⋮, ∈, ℕ*, ℝ, 𝕀, °, π
5. Font toán học chuyên nghiệp (Cambria Math, STIX Two Math, KaTeX)
"""

from __future__ import annotations
import re


def typeset_math_html(text: str) -> str:
    """Chuyển đổi chuỗi văn bản hoặc công thức toán học thành HTML typesetting chuẩn mực."""
    if not text:
        return ""

    s = text

    # 1. Chuẩn hóa các mũi tên suy ra và tương đương
    s = s.replace(" <=> ", ' <span class="m-op">&hArr;</span> ')
    s = s.replace(" ⇔ ", ' <span class="m-op">&hArr;</span> ')
    s = s.replace(" => ", ' <span class="m-op">&rArr;</span> ')
    s = s.replace(" ⇒ ", ' <span class="m-op">&rArr;</span> ')

    # 2. Chuẩn hóa phép toán quan hệ và tập hợp
    s = s.replace(" in N*", ' &isin; <span class="m-set">&#8469;*</span>')
    s = s.replace(" ∈ N*", ' &isin; <span class="m-set">&#8469;*</span>')
    s = s.replace(" ∈ ℕ*", ' &isin; <span class="m-set">&#8469;*</span>')
    s = s.replace(" in I", ' &isin; <span class="m-set">&#120128;</span>')
    s = s.replace(" ∈ I", ' &isin; <span class="m-set">&#120128;</span>')
    s = s.replace(" chia het cho ", ' <span class="m-op">&vellip;</span> ')
    s = s.replace(" ⋮ ", ' <span class="m-op">&vellip;</span> ')

    # 3. Chuẩn hóa phép nhân & chia & xấp xỉ
    # Thay ' * ' bằng ' · ' (sdot) hoặc ' × ' (times)
    s = re.sub(r'(\d+)\s*\*\s*(\d+)', r'\1 &times; \2', s)
    s = s.replace(" x ", " &times; ")
    s = s.replace(" × ", " &times; ")
    s = s.replace(" · ", " &sdot; ")
    s = s.replace(" : ", " &divide; ")
    s = s.replace(" ≈ ", " &asymp; ")
    s = s.replace(" ~= ", " &asymp; ")
    s = s.replace(" != ", " &ne; ")
    s = s.replace(" ≠ ", " &ne; ")
    s = s.replace(" <= ", " &le; ")
    s = s.replace(" ≤ ", " &le; ")
    s = s.replace(" >= ", " &ge; ")
    s = s.replace(" ≥ ", " &ge; ")
    s = s.replace(" +/- ", " &plusmn; ")
    s = s.replace(" ± ", " &plusmn; ")

    # 4. Chuẩn hóa số mũ thường gặp
    s = s.replace("x^2", '<span class="m-var">x</span><sup>2</sup>')
    s = s.replace("x²", '<span class="m-var">x</span><sup>2</sup>')
    s = s.replace("x^3", '<span class="m-var">x</span><sup>3</sup>')
    s = s.replace("x³", '<span class="m-var">x</span><sup>3</sup>')
    s = s.replace("y^2", '<span class="m-var">y</span><sup>2</sup>')
    s = s.replace("y²", '<span class="m-var">y</span><sup>2</sup>')
    s = s.replace("a^2", '<span class="m-var">a</span><sup>2</sup>')
    s = s.replace("a²", '<span class="m-var">a</span><sup>2</sup>')
    s = s.replace("b^2", '<span class="m-var">b</span><sup>2</sup>')
    s = s.replace("b²", '<span class="m-var">b</span><sup>2</sup>')
    s = s.replace("c^2", '<span class="m-var">c</span><sup>2</sup>')
    s = s.replace("c²", '<span class="m-var">c</span><sup>2</sup>')
    s = s.replace("d^2", '<span class="m-var">d</span><sup>2</sup>')
    s = s.replace("d²", '<span class="m-var">d</span><sup>2</sup>')
    s = s.replace("12²", '12<sup>2</sup>')
    s = s.replace("4²", '4<sup>2</sup>')
    s = s.replace("3²", '3<sup>2</sup>')
    s = s.replace("5²", '5<sup>2</sup>')
    s = s.replace("1²", '1<sup>2</sup>')

    # 5. Chuẩn hóa chỉ số dưới
    s = s.replace("x1", '<span class="m-var">x</span><sub>1</sub>')
    s = s.replace("x2", '<span class="m-var">x</span><sub>2</sub>')
    s = s.replace("x_1", '<span class="m-var">x</span><sub>1</sub>')
    s = s.replace("x_2", '<span class="m-var">x</span><sub>2</sub>')
    s = s.replace("y1", '<span class="m-var">y</span><sub>1</sub>')
    s = s.replace("y2", '<span class="m-var">y</span><sub>2</sub>')
    s = s.replace("y_1", '<span class="m-var">y</span><sub>1</sub>')
    s = s.replace("y_2", '<span class="m-var">y</span><sub>2</sub>')
    s = s.replace("T1", '<span class="m-var">T</span><sub>1</sub>')
    s = s.replace("T2", '<span class="m-var">T</span><sub>2</sub>')
    s = s.replace("T_1", '<span class="m-var">T</span><sub>1</sub>')
    s = s.replace("T_2", '<span class="m-var">T</span><sub>2</sub>')
    s = s.replace("A1", '<span class="m-var">A</span><sub>1</sub>')
    s = s.replace("B1", '<span class="m-var">B</span><sub>1</sub>')
    s = s.replace("A2", '<span class="m-var">A</span><sub>2</sub>')
    s = s.replace("B2", '<span class="m-var">B</span><sub>2</sub>')

    # 6. Chuẩn hóa căn bậc hai
    s = s.replace("√2", '<span class="m-root"><span class="m-radic">&radic;</span><span class="m-radicand">2</span></span>')
    s = s.replace("√3", '<span class="m-root"><span class="m-radic">&radic;</span><span class="m-radicand">3</span></span>')
    s = s.replace("√5", '<span class="m-root"><span class="m-radic">&radic;</span><span class="m-radicand">5</span></span>')
    s = re.sub(r'\\sqrt\{([^}]+)\}', r'<span class="m-root"><span class="m-radic">&radic;</span><span class="m-radicand">\1</span></span>', s)

    # 7. Chuẩn hóa phân số dạng LaTeX: \frac{A}{B}
    s = re.sub(
        r'\\frac\{([^}]+)\}\{([^}]+)\}',
        r'<span class="m-frac"><span class="m-num">\1</span><span class="m-den">\2</span></span>',
        s
    )

    # 8. Chuẩn hóa phân số dạng đại số dạng: 60/x, 60/(x+3), 60/(x + 3), 1/4, 1/6, 5/12, 12/5, 100/500, 150/5, x/3, y/2
    frac_replacements = [
        (r'60/\(x\s*\+\s*3\)', '<span class="m-frac"><span class="m-num">60</span><span class="m-den"><span class="m-var">x</span> + 3</span></span>'),
        (r'60/x', '<span class="m-frac"><span class="m-num">60</span><span class="m-den"><span class="m-var">x</span></span></span>'),
        (r'1/\(16\)', '<span class="m-frac"><span class="m-num">1</span><span class="m-den">16</span></span>'),
        (r'-1/16', '-<span class="m-frac"><span class="m-num">1</span><span class="m-den">16</span></span>'),
        (r'1/16', '<span class="m-frac"><span class="m-num">1</span><span class="m-den">16</span></span>'),
        (r'1/4', '<span class="m-frac"><span class="m-num">1</span><span class="m-den">4</span></span>'),
        (r'1/6', '<span class="m-frac"><span class="m-num">1</span><span class="m-den">6</span></span>'),
        (r'5/12', '<span class="m-frac"><span class="m-num">5</span><span class="m-den">12</span></span>'),
        (r'12/5', '<span class="m-frac"><span class="m-num">12</span><span class="m-den">5</span></span>'),
        (r'1/2', '<span class="m-frac"><span class="m-num">1</span><span class="m-den">2</span></span>'),
        (r'1/3', '<span class="m-frac"><span class="m-num">1</span><span class="m-den">3</span></span>'),
        (r'2/3', '<span class="m-frac"><span class="m-num">2</span><span class="m-den">3</span></span>'),
        (r'3/4', '<span class="m-frac"><span class="m-num">3</span><span class="m-den">4</span></span>'),
        (r'100\s*/\s*500', '<span class="m-frac"><span class="m-num">100</span><span class="m-den">500</span></span>'),
        (r'150\s*/\s*5', '<span class="m-frac"><span class="m-num">150</span><span class="m-den">5</span></span>'),
        (r'x\s*/\s*3', '<span class="m-frac"><span class="m-num"><span class="m-var">x</span></span><span class="m-den">3</span></span>'),
        (r'y\s*/\s*2', '<span class="m-frac"><span class="m-num"><span class="m-var">y</span></span><span class="m-den">2</span></span>'),
        (r'\(x\s*\+\s*y\)\s*/\s*\(3\s*\+\s*2\)', '<span class="m-frac"><span class="m-num"><span class="m-var">x</span> + <span class="m-var">y</span></span><span class="m-den">3 + 2</span></span>'),
        (r'1/T', '<span class="m-frac"><span class="m-num">1</span><span class="m-den"><span class="m-var">T</span></span></span>'),
        (r'1/x', '<span class="m-frac"><span class="m-num">1</span><span class="m-den"><span class="m-var">x</span></span></span>'),
        (r'1/y', '<span class="m-frac"><span class="m-num">1</span><span class="m-den"><span class="m-var">y</span></span></span>'),
    ]
    for pattern, repl in frac_replacements:
        s = re.sub(pattern, repl, s)

    return s


def get_math_css() -> str:
    """Trả về CSS chuẩn hóa hiển thị toán học cho cả HTML tương tác và bản in PDF A4."""
    return """
/* --- YOURDREAM Mathematical Typography Styles --- */
.m-math {
  font-family: "Cambria Math", "Latin Modern Math", "STIX Two Math", "Georgia", serif;
  font-size: 1.02em;
  letter-spacing: 0.015em;
  display: inline-block;
}
.m-var {
  font-family: "Cambria Math", "Latin Modern Math", "Times New Roman", serif;
  font-style: italic;
  font-weight: 500;
  padding: 0 1px;
}
.m-op {
  font-style: normal;
  font-weight: 600;
  margin: 0 3px;
  color: #0F172A;
}
.m-set {
  font-weight: 700;
  font-family: "Cambria Math", "STIX Two Math", serif;
}
.m-frac {
  display: inline-flex;
  flex-direction: column;
  vertical-align: -0.48em;
  text-align: center;
  padding: 0 2.5px;
  font-size: 0.88em;
  line-height: 1.05;
}
.m-num {
  border-bottom: 1.25px solid currentColor;
  padding-bottom: 1.5px;
  display: block;
}
.m-den {
  padding-top: 1.5px;
  display: block;
}
.m-root {
  display: inline-flex;
  align-items: center;
  vertical-align: -0.1em;
  margin: 0 1px;
}
.m-radic {
  font-size: 1.18em;
  font-family: "Cambria Math", serif;
  line-height: 1;
  margin-right: 1px;
}
.m-radicand {
  border-top: 1.25px solid currentColor;
  padding-top: 1px;
  display: inline-block;
}
"""
