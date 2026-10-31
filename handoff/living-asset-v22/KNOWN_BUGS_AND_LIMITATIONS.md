# CÁC LỖI ĐÃ BIẾT & PHẠM VI CHƯA XÁC MINH
## YOURDREAM LIVING MATHEMATICAL ASSET FACTORY v2.2

Tài liệu này ghi nhận trung thực các giới hạn kỹ thuật, các trường hợp biên, các lỗi đã biết và phạm vi chưa được xác minh nhằm bảo đảm tính minh bạch khi bàn giao cho Jules và nhóm tích hợp.

---

## 1. Giới hạn Phạm vi (Scope Boundaries)

1. **Phạm vi Cấp học Hiện tại:**
   - Nhà máy đã hoàn thiện và kiểm chứng 16 Flagship Living Assets đại diện cho 4 mạch kiến thức THCS (Số học, Đại số, Hình học & Đo lường, Thống kê & Xác suất) cho các lớp 6, 7, 8, 9 theo Chương trình GDPT 2018.
   - Các nội dung Toán THPT (Lớp 10–12 như Đạo hàm, Tích phân, Hình học Không gian Oxyz, Số phức) chưa được xây dựng bộ asset mẫu (nằm ngoài phạm vi của hợp đồng hiện tại).
   - Bộ 326 kỹ năng THCS đã có bảng chỉ mục và đề xuất cấu trúc, nhưng mới chỉ có 16 kỹ năng cốt lõi được tác quyền hóa thành Living Asset hoàn chỉnh.

2. **Chế độ Thể nghiệm 3D (Stage 2 Exploratory Prototype):**
   - Lab 3D Three.js (`02_STAGE2_CREATIVE_DISCOVERY/stage2_creative_frontier_lab.html`) là bản mẫu thăm dò cho mô hình 3D tương tác.
   - Hiện tại, bản 3D này hoạt động độc lập và chưa được nhúng trực tiếp vào bản in PDF A4 tĩnh (bản in PDF A4 sử dụng ảnh chiếu và sơ đồ hình học 2D để tối ưu in ấn và không phụ thuộc WebGL).

---

## 2. Các Trường hợp Biên & Lỗi Đã Biết (Known Edge Cases & Behaviors)

1. **Phông chữ khi in PDF A4 qua Headless Edge:**
   - Bản in A4 được thiết kế với phông `Inter` và `JetBrains Mono`. Nếu máy tính chạy bản in không có sẵn phông chữ này trên hệ điều hành và không có kết nối internet để tải qua Google Fonts CDN, trình duyệt Edge sẽ tự động thay thế bằng phông hệ thống (`Arial` hoặc `Segoe UI`). Bố cục trang A4 vẫn bảo toàn nguyên vẹn 1 trang duy nhất, nhưng độ mảnh nét chữ có thể hơi khác biệt.

2. **Độ phân giải màn hình Retina / High-DPI (Canvas Scaling):**
   - Bộ mô phỏng Canvas trong Interactive HTML sử dụng tỉ lệ `devicePixelRatio` mặc định của màn hình. Trên một số màn hình cảm ứng độ phân giải cực cao (> 300 DPI), nét vẽ canvas có thể hơi đậm hơn bình thường nếu người dùng phóng to (zoom) trên 150%. Đã được xử lý tự co giãn bằng CSS vector.

3. **Từ chối Cấu trúc Toán học Không Hỗ trợ (Honest Decline):**
   - Khi đưa một bài toán có cấu trúc toán học ngoài phạm vi 9 Họ toán học THCS (ví dụ: Phương trình vi phân cấp hai, Ma trận biến đổi không gian đa chiều), Bộ Sinh Trải Nghiệm Mới (`Generative Experience Composer`) sẽ chủ động trả về trạng thái `UNSUPPORTED_STRUCTURE_HONESTLY_DECLINED`. Đây là hành vi thiết kế có chủ đích (Honest Rejection), không phải lỗi kỹ thuật (Crash).

---

## 3. Trạng thái Quản trị & Phê duyệt (Governance Gates)

- **Trạng thái Kỹ thuật:** `SOURCE_VERIFIED` & `TECH_AUDIT_PASSED` (Đã kiểm chứng độc lập 100% bằng SymPy và Playwright).
- **Trạng thái Bàn giao:** `JULES_HANDOFF_READY` (Đầy đủ hợp đồng dữ liệu, schema, mã nguồn và hàng đợi 5 nhiệm vụ).
- **Trạng thái Sư phạm & Phát hành:** `PEDAGOGICAL_REVIEW_PENDING` (Chờ MASTER phê duyệt nghiệm thu sư phạm và nghệ thuật cuối cùng; `FINAL_APPROVED = False`). Tuyệt đối không tự ý deploy lên môi trường Production hoặc merge vào nhánh `main` khi chưa có chữ ký của MASTER.
