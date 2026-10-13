@echo off
setlocal
echo ===================================================================
echo   DONG BO HOC LIEU: GOOGLE DRIVE (G:) -^^> WEBAPP -^^> GITHUB
echo ===================================================================
echo.
cd /d "C:\Users\Admin\.gemini\antigravity\scratch\bandohoctap_webapp"
python "pipeline\sync_gdrive_to_github.py"
echo.
echo ===================================================================
echo   Hoan tat dong bo! Nhan phim bat ky de thoat.
echo ===================================================================
pause > nul
