# HƯỚNG DẪN TÁI LẬP HỆ THỐNG — LIVING MATHEMATICAL ASSET FACTORY v2.2
## YOURDREAM · REPRODUCIBILITY & PRODUCTION GUIDE

Tài liệu này cung cấp toàn bộ chỉ dẫn để cài đặt, thiết lập môi trường mới độc lập, chạy lại nhà máy và kiểm thử toàn bộ 16 Living Assets Toán THCS (Lớp 6–9) mà không cần truy cập ổ cứng `D:\` của MASTER.

---

## 1. Yêu cầu Hệ thống & Môi trường

- **Hệ điều hành:** Windows 10/11, Ubuntu 22.04+ LTS, macOS Monterey+.
- **Python:** Phiên bản 3.10 trở lên (khuyến nghị 3.11 hoặc 3.12).
- **Trình duyệt xuất PDF:** Microsoft Edge (`msedge.exe`) hoặc Google Chrome / Chromium có cờ `--headless`.
- **Bộ nhớ RAM:** Tối thiểu 4 GB (khuyến nghị 8 GB khi render song song 16 PDF).
- **Dung lượng đĩa trống:** Tối thiểu 500 MB.

---

## 2. Cài đặt Môi trường Mới (Clean Environment Setup)

```bash
# 1. Di chuyển vào thư mục dự án
cd LIVING_ASSET_FACTORY

# 2. Khởi tạo môi trường ảo Python
python -m venv venv

# 3. Kích hoạt môi trường ảo
# Trên Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Trên Windows (Command Prompt):
.\venv\Scripts\activate.bat
# Trên Linux / macOS:
source venv/bin/activate

# 4. Cài đặt dependencies bắt buộc
pip install -r requirements.txt

# 5. Cài đặt trình duyệt cho Playwright (nếu chạy test E2E UI)
playwright install chromium
```

---

## 3. Các Lệnh Vận Hành & Sản Xuất

### 3.1 Chạy toàn bộ dây chuyền sản xuất (End-to-End Batch Production)
Lệnh này kích hoạt cả 7 modules tuần tự: đọc 326 kỹ năng, dựng SVG 5 thế giới nghệ thuật, kiểm chứng SymPy, render 16 HTML + 16 SVG + 32 PDF A4 + 32 PNG 150 DPI, tạo Living Asset Studio và đóng gói JULES Handoff:

```bash
python nha_may_living_asset_toan6_9.py --mode all
```

*Thời gian thực thi dự kiến:* ~40 - 55 giây trên máy tính hiện đại (sử dụng `ThreadPoolExecutor` đa luồng cho Headless Edge PDF rendering).

### 3.2 Sản xuất riêng lẻ 1 Living Asset cụ thể
```bash
# Cú pháp: python nha_may_living_asset_toan6_9.py --asset <ASSET_ID>
python nha_may_living_asset_toan6_9.py --asset YD-LA-NUM-G6-01
```

### 3.3 Thử nghiệm Bộ Sinh Trải Nghiệm Mới (Generative Experience Composer)
```bash
# Tổng hợp tương tác từ tệp đặc tả JSON cấu trúc toán học
python nha_may_living_asset_toan6_9.py --synthesize path/to/custom_spec.json
```

---

## 4. Kiểm Thử Tự Động (Automated QA & Contract Verification)

### 4.1 Chạy bộ QA hợp đồng 9 năng lực SDK & Zero Answer Leak
```bash
python tests/test_factory_and_jules_handoff.py
```
*Kết quả chuẩn:* `ALL_TESTS_PASSED` (100% 16 student payloads không chứa đáp án thô, bất biến giả thiết toán học không bị biến dạng khi thử sai số).

### 4.2 Chạy bộ kiểm thử giao diện trình duyệt không đầu (Playwright Browser Verification)
```bash
python tests/verify_studio_browser.py
```
*Kết quả chuẩn:* `page_errors: []`, render đầy đủ 16 thẻ asset trong Studio, chuyển tab và thử nghiệm Generative Transfer không có lỗi script.

---

## 5. Cấu trúc Thư mục Đầu ra (Deliverables Map)

```
LIVING_ASSET_FACTORY/
├── engine/                      # Mã nguồn Python 7 modules cốt lõi + SDK
├── data/                        # Dữ liệu 326 kỹ năng THCS & Textnote packs
├── assets/                      # Hình ảnh sticky notes và texture hỗ trợ
├── output/                      # Kết quả sản xuất đa định dạng
│   ├── interactive_html/        # 16 HTML tương tác độc lập (Zero-CORS)
│   ├── svg/                     # 16 Layered Precision SVG (Art + Math layers)
│   ├── html_a4/                 # 32 HTML A4 (16 Học sinh + 16 Giáo viên)
│   ├── pdf_student/             # 16 PDF A4 Học sinh (1 trang, 0% lộ đáp án)
│   ├── pdf_teacher/             # 16 PDF A4 Giáo viên (1 trang, lời giải & barem)
│   ├── previews_png/            # 32 PNG 150 DPI chất lượng cao
│   └── json/                    # 16 tệp đặc tả 6-DNA Living Asset
├── studio/                      # Living Asset Studio HTML
├── tests/                       # Bộ kịch bản kiểm thử tự động
├── YOURDREAM_Living_Asset_Studio.html  # Studio giao diện trực quan cho MASTER
├── nha_may_living_asset_toan6_9.py     # Lệnh điều phối toàn nhà máy
└── requirements.txt             # Khai báo thư viện phụ thuộc
```

---

## 6. Biến Môi Trường (Environment Variables)

Nhà máy hỗ trợ định cấu hình động qua biến môi trường để chạy trong container, Docker, hoặc CI/CD runner:

- `LIVING_ASSET_FACTORY_DIR`: Đường dẫn gốc của thư mục nhà máy (mặc định: thư mục chứa mã nguồn).
- `JULES_HANDOFF_DIR`: Đường dẫn thư mục đóng gói bàn giao (mặc định: `../JULES_LIVING_ASSET_HANDOFF`).
- `CHECKPOINTS_DIR`: Đường dẫn lưu trữ checkpoint JSON/MD (mặc định: `../CHECKPOINTS`).
