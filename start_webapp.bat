@echo off
title BANDOHOCTAP.VN - Trạm Điều Hành WebApp Học Liệu
chcp 65001 > nul
echo ========================================================
echo   BANDOHOCTAP.VN - BẢN ĐỒ 30 NGÀY BẮT GỐC TOÁN 9
echo   Hệ thống học liệu & WebApp tự động hóa
echo ========================================================
echo.
echo [1] Đang khởi chạy máy chủ xem trước nội bộ tại http://localhost:8080 ...
start http://localhost:8080
python -m http.server 8080
pause
