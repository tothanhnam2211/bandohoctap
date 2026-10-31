# HÀNG ĐỢI NHIỆM VỤ JULES — LIVING MATHEMATICAL ASSET FACTORY (V2.2)

- **Kho mã nguồn mục tiêu:** `https://github.com/tothanhnam2211/bandohoctap`
- **Trạng thái bàn giao:** `JULES_HANDOFF_READY`
- **Quy tắc bảo vệ nhánh:** Không ghi đè PR #2 của H07; không tự động merge vào main/production khi chưa qua QA và phê duyệt của MASTER.

## Danh sách 5 Nhiệm vụ QA, Sửa lỗi & Tích hợp Không Xung đột Nhánh

| Mã nhiệm vụ | Nhánh Git độc lập | Phạm vi & Đường dẫn (`owned_paths`) | Tiêu chí nghiệm thu |
| :--- | :--- | :--- | :--- |
| `JULES_LA_TASK_01_SDK_AND_CONTRACT_QA` | `test/living-asset-sdk-contract-qa` | **Kiểm thử hợp đồng SDK 9 năng lực, Zero Answer Leak trên 16 student_payloads & bất biến giả thiết**<br>`tests/living_asset/test_sdk_contract.py`, `src/lib/living-asset/sdkAdapter.ts` | Pass 100% kiểm thử không lộ đáp án thô và không tự sửa giả thiết đề bài khi thử nghiệm sai số. |
| `JULES_LA_TASK_02_PRIMITIVE_COMPOSER_INTEGRATION` | `feat/living-asset-8-primitives-engine` | **Tích hợp 8 Composable Interactive Primitives vào WebApp React/TypeScript**<br>`src/components/living-asset/primitives/` | Render mượt 8 primitive trên Desktop & Tablet (768x1024), không tràn khung HUD. |
| `JULES_LA_TASK_03_GENERATIVE_TRANSFER_STRESS_TEST` | `test/living-asset-generative-transfer` | **Kiểm thử khả năng tổng quát hóa trên các bài toán chưa hardcode (Tests A, B, C, D + tập bài mới)**<br>`tests/living_asset/transfer_generalization.spec.ts` | Tổ hợp đúng primitive cho bài toán mới cùng họ/đa họ và từ chối trung thực cấu trúc ngoài phạm vi. |
| `JULES_LA_TASK_04_CROSS_DEVICE_PLAYWRIGHT_E2E` | `test/living-asset-playwright-multi-device` | **Kiểm thử hồi quy trình duyệt (Desktop 1440x900, iPad 768x1024, Mobile 390x844) cho 16 Living Assets**<br>`tests/e2e/living_asset_16_experiences.spec.ts` | 0 lỗi console/WebGL, 100% thanh trượt và nút Learner A/B/C phản hồi tức thời. |
| `JULES_LA_TASK_05_STUDIO_AND_A4_PRINT_SYNC` | `feat/living-asset-studio-a4-sync` | **Tích hợp Living Asset Studio & trình xuất Phiếu A4 1 trang vào cổng giáo viên**<br>`src/pages/studio/LivingAssetStudioPage.tsx` | Đồng bộ số liệu 1:1 giữa mô hình tương tác trên màn hình và bản in PDF A4. |