# YOURDREAM — UNIVERSAL MATHEMATICAL VISUAL ASSET FACTORY
## JULES REPRODUCIBLE SOURCE HANDOFF KIT (v1.0)

**Dành cho:** Jules (Partner AI & Testing/Integration Engineer)  
**Tác giả:** Google Antigravity Ultra (Gemini Argon High)  
**Ngày bàn giao:** 31/10/2026  
**Chế độ:** SOURCE-FIRST · REUSABLE · 100% LOCAL ($0.00 API COST)

---

### I. TỔNG QUAN HỆ THỐNG ĐÃ SẢN XUẤT

Nhà máy đã hoàn thành sản xuất thư viện trực quan quy mô lớn bao phủ toàn bộ chương trình Toán phổ thông K12 (Lớp 6 đến Lớp 12 GDPT 2018):
- **166 Họ Asset cốt lõi** (`AssetFamilySpec`): Đại số, Hình học phẳng, Hình không gian, Thống kê, Xác suất, Giải tích & STEM.
- **7,636 Biến thể toán học độc lập** (`variant_id`): Tham số chuẩn xác, không trùng lặp.
- **30,544 File hình ảnh trực quan kết xuất sẵn trên đĩa**:
  - `Master SVG`: Vector gốc phân lớp thẩm mỹ (Art + Math), độ nét vô hạn.
  - `Master PNG`: Bitmap 150 DPI trong suốt, chuẩn in ấn A4 & hiển thị WebApp.
  - `Student SVG`: Phiếu học sinh với dữ kiện ẩn, dấu hỏi `?` và khoảng trống thực hành.
  - `Student PNG`: Bitmap 150 DPI trong suốt cho phiếu bài tập học sinh.
- **Cơ sở dữ liệu SQLite & FTS5 Full-Text Search Registry**: Tích hợp sẵn `visual_asset_registry.db`.

> [!NOTE]
> **Vị trí toàn bộ 30,544 file ảnh kết xuất:**
> Để giữ gói mã nguồn Git gọn nhẹ (< 15 MB), toàn bộ 30,544 file ảnh đầy đủ được lưu giữ nguyên vẹn tại:
> `D:\YOURDREAM.VN\VISUAL_ASSET_FACTORY\output\`
> Trong gói handoff này, Jules có sẵn thư mục `sample_assets/` chứa 56 file mẫu đại diện cho tất cả các khối lớp và mạch kiến thức, cùng toàn bộ mã nguồn để tự động sinh lại hoặc kết xuất động bất kỳ asset nào theo nhu cầu.

---

### II. CẤU TRÚC THƯ MỤC HANDOFF

```
JULES_VISUAL_ASSET_HANDOFF/
├── curriculum/
│   └── k12_curriculum_catalog.py       # Đặc tả 166 Họ Asset K12 (GDPT 2018)
├── engine/
│   ├── core_math_primitives.py         # Renderer vector hình học phẳng, 3D, tọa độ Oxy & STEM
│   ├── specialized_primitives.py       # Renderer trục số, Venn, phân số, cây thừa số, lượng giác
│   ├── asset_renderer_dispatch.py      # Bộ điều phối kết xuất & tự động làm sạch XML
│   ├── variant_generator.py            # Bộ sinh tham số biến thể chuẩn xác toán học
│   ├── multiformat_exporter.py         # Kết xuất đồng thời SVG & PNG 150 DPI
│   └── registry_db.py                  # Module giao tiếp SQLite & FTS5 Registry
├── pipeline/
│   ├── run_mass_production.py          # Bộ chạy sản xuất hàng loạt đa tiến trình CPU
│   ├── verify_asset_quality.py         # Bộ kiểm thử kiểm toán chất lượng độc lập
│   └── package_checkpoint.py           # Bộ đóng gói biên lai & checkpoint
├── studio/
│   ├── YOURDREAM_Universal_Visual_Asset_Studio.html  # Studio WebApp tương tác độc lập
│   └── build_studio_app.py             # Script biên dịch lại Studio HTML từ SQLite
├── sample_assets/                      # 56 file mẫu đại diện SVG/PNG Master & Student
├── manifests/
│   ├── MANIFEST_K12_ASSET_FAMILIES.json    # Danh mục đặc tả 166 họ asset
│   └── MANIFEST_ASSET_INDEX_SUMMARY.json   # Bảng tổng hợp thống kê & đường dẫn
├── visual_asset_registry.db            # Cơ sở dữ liệu SQLite chỉ mục hóa 7,636 biến thể
├── test_jules_visual_factory.py        # Bộ kiểm thử chấp nhận tự động (Unittest)
├── requirements.txt                    # Thư viện phụ thuộc (chỉ cần pymupdf)
└── README.md                           # Tài liệu hướng dẫn này
```

---

### III. HƯỚNG DẪN KIỂM THỬ NHANH CHO JULES

#### 1. Cài đặt môi trường
Chỉ cần cài đặt `pymupdf` (không cần GPU, không cần API trả phí):
```bash
pip install pymupdf
```

#### 2. Chạy bài kiểm thử chấp nhận (Acceptance Test)
```bash
python test_jules_visual_factory.py
```
*Kết quả kỳ vọng:* 4/4 test passed trong < 0.3 giây.

#### 3. Mở và kiểm thử Visual Studio WebApp
Mở trực tiếp trên trình duyệt (hoạt động offline 100%):
```bash
start studio/YOURDREAM_Universal_Visual_Asset_Studio.html
```
- Lọc theo khối lớp (Lớp 6 đến Lớp 12).
- Chuyển đổi giữa Bản Thầy (Master) và Phiếu Trò (Student).
- Nhấp "Chi tiết & Tải về" để xem kích thước lớn, sao chép mã SVG hoặc đường dẫn PNG.

---

### IV. HƯỚNG DẪN KẾT NỐI & TÁI SỬ DỤNG TRONG CÁC NHÀ MÁY HỌC LIỆU

#### 1. Truy vấn tài nguyên trực quan qua SQLite FTS5
```python
import sqlite3

conn = sqlite3.connect("visual_asset_registry.db")
cur = conn.cursor()

# Tìm kiếm toàn văn các asset liên quan đến 'parabol'
cur.execute("SELECT variant_id, title, master_svg_path, master_png_path FROM asset_search_fts WHERE asset_search_fts MATCH 'parabol' LIMIT 5")
for row in cur.fetchall():
    print(row)
conn.close()
```

#### 2. Kết xuất động một asset theo tham số tùy chỉnh trong runtime
```python
from engine.asset_renderer_dispatch import dispatch_render_svg
import pymupdf

# Tạo hình vẽ parabol với đỉnh và hệ số tùy chỉnh
custom_params = {
    "curves": [{"type": "parabola", "func": lambda x: 0.5 * (x - 2)**2 - 3, "name": "y = 0.5(x-2)² - 3", "color": "#0284C7"}],
    "key_points": [{"x": 2, "y": -3, "label": "I(2;-3)", "color": "#EF4444"}],
    "xlim": (-4, 8),
    "ylim": (-5, 5)
}

# 1. Sinh vector SVG
svg_code = dispatch_render_svg("algebra_parabola_basic", custom_params, title="Đồ thị hàm bậc hai tùy biến")

# 2. Kết xuất PNG 150 DPI trong suốt
doc = pymupdf.open(stream=svg_code.encode("utf-8"), filetype="svg")
png_bytes = doc[0].get_pixmap(dpi=150, alpha=True).tobytes(output="png")
doc.close()

with open("output_custom.png", "wb") as f:
    f.write(png_bytes)
```

---

### V. ĐƯỜNG DẪN LƯU TRỮ VÀ CHECKPOINT

- **Mã nguồn Git Remote:** `https://github.com/tothanhnam2211/bandohoctap.git`
  - Nhánh: `handoff/universal-visual-asset-factory-v10-jules-20261031`
- **Kho lưu trữ Google Drive:** `G:\Drive của tôi\YOURDREAM_AI_WORKSPACE\04_CODE_PIPELINES\VISUAL_ASSET_FACTORY`
- **Thư viện ảnh gốc toàn phần (30,544 files):** `D:\YOURDREAM.VN\VISUAL_ASSET_FACTORY\output\`
