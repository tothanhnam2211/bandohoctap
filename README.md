# BANDOHOCTAP.VN - Hệ Thống WebApp & Tự Động Hóa Học Liệu 30 Ngày

## 1. Cấu Trúc Dự Án
```
bandohoctap_webapp/
├── index.html                  # Giao diện WebApp (TailwindCSS, KaTeX toán học, Responsive)
├── app.js                      # Bộ điều khiển: chuyển Tab, làm bài Skeleton, chấm trắc nghiệm
├── start_webapp.bat            # Click đúp chuột để mở ngay WebApp trên trình duyệt
├── data/
│   ├── curriculum.json         # Danh mục tiến độ 30 ngày bắt gốc
│   ├── day-01.json             # Dữ liệu chi tiết Ngày 01 (Shorts, Sơ đồ, Skeleton, Quiz)
│   └── day-XX.json             # Dữ liệu các ngày tiếp theo
├── public/
│   └── assets/
│       ├── day-01/             # Chứa tệp Phiếu học tập, Infographic PNG, Clip MP4
│       └── stem_labs/          # Phòng thí nghiệm STEM 3D (trục số, chuyển động...)
└── pipeline/
    ├── parse_notebook_md.py    # Bóc tách tệp Markdown từ Notebook thành JSON bài học
    ├── publish_lesson.py       # Tự động đóng gói tài nguyên & mở khóa ngày mới vào WebApp
    └── deploy.py               # Tự động đẩy lên Cloudflare Pages hoặc máy chủ Web
```

## 2. Cách Vận Hành Tự Động

### Bước 1: Sau khi có học liệu từ Notebook (.md, .docx, .png, .mp4)
Chạy lệnh tự động đóng gói bài học (Ví dụ Ngày 02):
```bash
python pipeline/publish_lesson.py --day 2 --md "duong_dan/bai_02.md" --docx "duong_dan/Phieu_02.docx" --infographic "duong_dan/Infor_02.png" --video "duong_dan/Clip_02.mp4"
```
Hệ thống sẽ:
1. Bóc tách kiến thức, kịch bản shorts, skeleton notes, trắc nghiệm thành `data/day-02.json`.
2. Sao chép các tệp tài nguyên vào thư mục `public/assets/day-02/`.
3. Tự động mở khóa Ngày 02 trên sidebar của WebApp.

### Bước 2: Tự Động Đẩy Lên Website (Deploy)
* **Đẩy lên Cloudflare Pages:**
```bash
python pipeline/deploy.py --mode cloudflare --project bandohoctap
```
* **Hoặc đẩy qua Git (nếu kết nối GitHub/GitLab):**
```bash
python pipeline/deploy.py --mode git
```
* **Hoặc xem thử ngay trên máy:**
Chạy file `start_webapp.bat` hoặc lệnh:
```bash
python pipeline/deploy.py --mode local --port 8080
```
Mở trình duyệt tại: `http://localhost:8080`
