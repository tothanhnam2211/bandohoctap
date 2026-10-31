# -*- coding: utf-8 -*-
"""
STUDIO APP BUILDER
Biên dịch WebApp tương tác hoàn chỉnh: YOURDREAM_Universal_Visual_Asset_Studio.html
Tích hợp sẵn danh mục asset, bộ lọc đa cấp, chế độ xem trước Master/Student,
và khả năng sao chép vector SVG / đường dẫn PNG ngay lập tức.
"""

import os
import sys
import json
import sqlite3
from typing import Dict, Any, List

BASE_DIR = r"D:\YOURDREAM.VN\VISUAL_ASSET_FACTORY"

def build_studio_html(output_html_path: str):
    db_path = os.path.join(BASE_DIR, "visual_asset_registry.db")

    # Lấy mẫu asset đa dạng đại diện cho mỗi Họ Asset (mỗi họ lấy 1 variant mẫu để nhúng vào Studio)
    samples = []
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
        SELECT 
            v.variant_id, v.family_id, v.grade, v.strand, v.chapter, v.topic_vi, v.title, 
            v.generator_type, v.math_invariant,
            v.master_svg_path, v.master_png_path, v.student_svg_path, v.student_png_path
        FROM asset_variants v
        WHERE v.variant_id LIKE '%_VAR_01'
        ORDER BY v.grade, v.strand, v.family_id
        """)
        rows = cur.fetchall()
        for r in rows:
            # Đọc nội dung SVG master & student để nhúng inline (tải ngay lập tức không cần server)
            svg_m_full = os.path.join(BASE_DIR, r[9].replace("/", "\\"))
            svg_s_full = os.path.join(BASE_DIR, r[11].replace("/", "\\"))
            svg_m_content = ""
            svg_s_content = ""
            if os.path.exists(svg_m_full):
                with open(svg_m_full, "r", encoding="utf-8", errors="ignore") as f:
                    svg_m_content = f.read()
            if os.path.exists(svg_s_full):
                with open(svg_s_full, "r", encoding="utf-8", errors="ignore") as f:
                    svg_s_content = f.read()

            samples.append({
                "variant_id": r[0],
                "family_id": r[1],
                "grade": r[2],
                "strand": r[3],
                "chapter": r[4],
                "topic_vi": r[5],
                "title": r[6],
                "generator_type": r[7],
                "math_invariant": r[8],
                "master_svg_path": r[9],
                "master_png_path": r[10],
                "student_svg_path": r[11],
                "student_png_path": r[12],
                "master_svg_content": svg_m_content,
                "student_svg_content": svg_s_content,
            })
        conn.close()

    samples_json_str = json.dumps(samples, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YOURDREAM — Universal Mathematical Visual Asset Studio</title>
<style>
:root {{
  --bg-main: #0B0F19;
  --bg-card: #151D2F;
  --bg-card-hover: #1C263D;
  --border-color: #2D3748;
  --text-main: #F1F5F9;
  --text-muted: #94A3B8;
  --brand-blue: #0284C7;
  --brand-cyan: #38BDF8;
  --accent-green: #10B981;
  --accent-amber: #F59E0B;
  --accent-purple: #8B5CF6;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background-color: var(--bg-main);
  color: var(--text-main);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  padding: 24px;
}}
header {{
  background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px 32px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}}
.header-title h1 {{
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.5px;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  gap: 12px;
}}
.header-title h1 span.badge {{
  background: var(--brand-blue);
  color: #FFF;
  font-size: 12px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  text-transform: uppercase;
}}
.header-title p {{
  color: var(--text-muted);
  font-size: 14px;
  margin-top: 4px;
}}
.stats-banner {{
  display: flex;
  gap: 20px;
}}
.stat-pill {{
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 10px 18px;
  text-align: center;
}}
.stat-pill .num {{
  font-size: 20px;
  font-weight: 800;
  color: var(--brand-cyan);
}}
.stat-pill .lbl {{
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
}}

/* Filter Bar */
.control-bar {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 18px 24px;
  margin-bottom: 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}}
.search-row {{
  display: flex;
  gap: 16px;
  align-items: center;
}}
.search-input {{
  flex: 1;
  background: #0B0F19;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 10px 16px;
  color: #FFF;
  font-size: 14px;
  outline: none;
}}
.search-input:focus {{
  border-color: var(--brand-cyan);
}}
.mode-toggle {{
  display: flex;
  background: #0B0F19;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
}}
.mode-btn {{
  background: transparent;
  border: none;
  color: var(--text-muted);
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}}
.mode-btn.active {{
  background: var(--brand-blue);
  color: #FFF;
}}

.pills-row {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  align-items: center;
}}
.pills-label {{
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-right: 6px;
}}
.filter-pill {{
  background: #0B0F19;
  border: 1px solid var(--border-color);
  border-radius: 20px;
  padding: 4px 12px;
  font-size: 12px;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.2s;
}}
.filter-pill:hover, .filter-pill.active {{
  background: var(--brand-blue);
  color: #FFF;
  border-color: var(--brand-blue);
}}

/* Asset Grid */
.grid-container {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 20px;
}}
.asset-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s, border-color 0.2s;
}}
.asset-card:hover {{
  transform: translateY(-2px);
  border-color: var(--brand-cyan);
}}
.preview-box {{
  background: #FFFFFF;
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 240px;
  cursor: pointer;
}}
.preview-box svg {{
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}}
.card-content {{
  padding: 16px;
  display: flex;
  flex-direction: column;
  flex: 1;
}}
.card-badges {{
  display: flex;
  gap: 6px;
  margin-bottom: 8px;
}}
.badge-grade {{
  background: #0369A1;
  color: #FFF;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
}}
.badge-strand {{
  background: rgba(255, 255, 255, 0.08);
  color: var(--text-muted);
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 4px;
}}
.card-title {{
  font-size: 14.5px;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 6px;
}}
.card-meta {{
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 12px;
}}
.card-actions {{
  margin-top: auto;
  display: flex;
  gap: 8px;
}}
.btn {{
  flex: 1;
  background: #0B0F19;
  border: 1px solid var(--border-color);
  color: var(--text-main);
  padding: 7px 10px;
  font-size: 12px;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s;
}}
.btn:hover {{
  background: var(--brand-blue);
  color: #FFF;
  border-color: var(--brand-blue);
}}

/* Modal Drawer */
.modal-overlay {{
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(4px);
  z-index: 1000;
  justify-content: center;
  align-items: center;
  padding: 24px;
}}
.modal-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  max-width: 960px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  padding: 24px;
  position: relative;
}}
.modal-close {{
  position: absolute;
  top: 20px;
  right: 20px;
  background: transparent;
  border: none;
  color: var(--text-muted);
  font-size: 24px;
  cursor: pointer;
}}
.modal-split {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 16px;
}}
.modal-viewbox {{
  background: #FFFFFF;
  border-radius: 8px;
  padding: 12px;
  text-align: center;
}}
.modal-viewbox h4 {{
  color: #0F172A;
  font-size: 13px;
  font-weight: 800;
  margin-bottom: 8px;
  text-transform: uppercase;
}}
</style>
</head>
<body>

<header>
  <div class="header-title">
    <h1>YOURDREAM <span class="badge">Universal Visual Asset Studio</span></h1>
    <p>Nhà máy đồ họa Toán học phổ thông K12 · GDPT 2018 · 30,000+ Vector SVGs & 150 DPI PNGs</p>
  </div>
  <div class="stats-banner">
    <div class="stat-pill">
      <div class="num" id="stat-total-rendered">30,544+</div>
      <div class="lbl">File trực quan</div>
    </div>
    <div class="stat-pill">
      <div class="num" id="stat-variants">7,636</div>
      <div class="lbl">Biến thể Toán</div>
    </div>
    <div class="stat-pill">
      <div class="num" id="stat-families">166</div>
      <div class="lbl">Họ Asset K12</div>
    </div>
  </div>
</header>

<div class="control-bar">
  <div class="search-row">
    <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm theo chủ đề, định lý, từ khóa (ví dụ: tam giác, parabol, cán cân, xác suất, tích phân, lăng trụ, vectơ)...">
    <div class="mode-toggle">
      <button class="mode-btn active" id="btnMasterMode" onclick="setRenderMode('master')">Bản Thầy (Master)</button>
      <button class="mode-btn" id="btnStudentMode" onclick="setRenderMode('student')">Phiếu Học Sinh (?)</button>
    </div>
  </div>

  <div class="pills-row">
    <span class="pills-label">Khối Lớp:</span>
    <span class="filter-pill active" onclick="setGradeFilter(0)">Tất cả (K12)</span>
    <span class="filter-pill" onclick="setGradeFilter(6)">Lớp 6</span>
    <span class="filter-pill" onclick="setGradeFilter(7)">Lớp 7</span>
    <span class="filter-pill" onclick="setGradeFilter(8)">Lớp 8</span>
    <span class="filter-pill" onclick="setGradeFilter(9)">Lớp 9</span>
    <span class="filter-pill" onclick="setGradeFilter(10)">Lớp 10</span>
    <span class="filter-pill" onclick="setGradeFilter(11)">Lớp 11</span>
    <span class="filter-pill" onclick="setGradeFilter(12)">Lớp 12</span>
  </div>

  <div class="pills-row">
    <span class="pills-label">Mạch kiến thức:</span>
    <span class="filter-pill active" onclick="setStrandFilter('ALL')">Tất cả mạch</span>
    <span class="filter-pill" onclick="setStrandFilter('SO_HOC_DAI_SO')">Số học & Đại số</span>
    <span class="filter-pill" onclick="setStrandFilter('HINH_HOC_DO_LUONG')">Hình học & Đo lường</span>
    <span class="filter-pill" onclick="setStrandFilter('THONG_KE_XAC_SUAT')">Thống kê & Xác suất</span>
    <span class="filter-pill" onclick="setStrandFilter('STEM_THUC_TIEN')">STEM & Thực tiễn</span>
    <span class="filter-pill" onclick="setStrandFilter('GIAI_TICH_HINH_HOC')">Giải tích & Tọa độ</span>
  </div>
</div>

<div class="grid-container" id="assetGrid"></div>

<!-- Modal Drawer -->
<div class="modal-overlay" id="detailModal">
  <div class="modal-card">
    <button class="modal-close" onclick="closeModal()">&times;</button>
    <h2 id="modalTitle" style="color: #FFF; font-size: 18px; margin-bottom: 4px;"></h2>
    <p id="modalSubtitle" style="color: var(--text-muted); font-size: 13px;"></p>

    <div class="modal-split">
      <div class="modal-viewbox">
        <h4>Bản Thầy (Đầy đủ dữ kiện & đáp số)</h4>
        <div id="modalMasterSvg"></div>
      </div>
      <div class="modal-viewbox">
        <h4>Phiếu Học Sinh (Ẩn đáp án, Dấu '?')</h4>
        <div id="modalStudentSvg"></div>
      </div>
    </div>

    <div style="margin-top: 18px; display: flex; gap: 12px;">
      <button class="btn" style="background: var(--brand-blue); color: #FFF;" onclick="copyCurrentSvg()">Sao chép mã SVG Bản Thầy</button>
      <button class="btn" style="background: var(--accent-green); color: #FFF;" onclick="copyCurrentStudentSvg()">Sao chép mã SVG Phiếu Trò</button>
      <button class="btn" onclick="copyCurrentPaths()">Sao chép đường dẫn File đĩa</button>
    </div>
  </div>
</div>

<script>
const ASSETS_DATA = {samples_json_str};

let currentGrade = 0;
let currentStrand = 'ALL';
let currentMode = 'master'; // 'master' or 'student'
let currentSearch = '';
let activeAsset = null;

function renderGrid() {{
  const grid = document.getElementById('assetGrid');
  grid.innerHTML = '';

  const q = currentSearch.toLowerCase().trim();
  const filtered = ASSETS_DATA.filter(item => {{
    if (currentGrade !== 0 && item.grade !== currentGrade) return false;
    if (currentStrand !== 'ALL' && item.strand !== currentStrand) return false;
    if (q) {{
      const matchText = (item.title + ' ' + item.topic_vi + ' ' + item.chapter + ' ' + item.math_invariant + ' ' + item.generator_type).toLowerCase();
      if (!matchText.includes(q)) return false;
    }}
    return true;
  }});

  filtered.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'asset-card';

    const svgContent = currentMode === 'master' ? item.master_svg_content : item.student_svg_content;

    card.innerHTML = `
      <div class="preview-box" onclick='openModal(${{JSON.stringify(item.variant_id)}})'>
        ${{svgContent}}
      </div>
      <div class="card-content">
        <div class="card-badges">
          <span class="badge-grade">Lớp ${{item.grade}}</span>
          <span class="badge-strand">${{item.strand}}</span>
        </div>
        <div class="card-title">${{item.title}}</div>
        <div class="card-meta"><b>Chương:</b> ${{item.chapter}}</div>
        <div class="card-meta"><b>Bất biến Toán:</b> ${{item.math_invariant}}</div>
        <div class="card-actions">
          <button class="btn" onclick='openModal(${{JSON.stringify(item.variant_id)}})'>Chi tiết & Tải về</button>
        </div>
      </div>
    `;
    grid.appendChild(card);
  }});
}}

function setGradeFilter(g) {{
  currentGrade = g;
  document.querySelectorAll('.pills-row:nth-child(2) .filter-pill').forEach((pill, idx) => {{
    pill.classList.toggle('active', (g === 0 && idx === 0) || (g !== 0 && idx === g - 5));
  }});
  renderGrid();
}}

function setStrandFilter(s) {{
  currentStrand = s;
  document.querySelectorAll('.pills-row:nth-child(3) .filter-pill').forEach(pill => {{
    pill.classList.toggle('active', pill.innerText.includes(s) || (s === 'ALL' && pill.innerText.includes('Tất cả')));
  }});
  renderGrid();
}}

function setRenderMode(mode) {{
  currentMode = mode;
  document.getElementById('btnMasterMode').classList.toggle('active', mode === 'master');
  document.getElementById('btnStudentMode').classList.toggle('active', mode === 'student');
  renderGrid();
}}

document.getElementById('searchInput').addEventListener('input', (e) => {{
  currentSearch = e.target.value;
  renderGrid();
}});

function openModal(variantId) {{
  const item = ASSETS_DATA.find(x => x.variant_id === variantId);
  if (!item) return;
  activeAsset = item;
  document.getElementById('modalTitle').innerText = item.title;
  document.getElementById('modalSubtitle').innerText = `Lớp ${{item.grade}} · ${{item.chapter}} · Bất biến: ${{item.math_invariant}}`;
  document.getElementById('modalMasterSvg').innerHTML = item.master_svg_content;
  document.getElementById('modalStudentSvg').innerHTML = item.student_svg_content;
  document.getElementById('detailModal').style.display = 'flex';
}}

function closeModal() {{
  document.getElementById('detailModal').style.display = 'none';
  activeAsset = null;
}}

function copyCurrentSvg() {{
  if (!activeAsset) return;
  navigator.clipboard.writeText(activeAsset.master_svg_content).then(() => {{
    alert('Đã sao chép mã Master SVG vào Clipboard!');
  }});
}}

function copyCurrentStudentSvg() {{
  if (!activeAsset) return;
  navigator.clipboard.writeText(activeAsset.student_svg_content).then(() => {{
    alert('Đã sao chép mã Student SVG vào Clipboard!');
  }});
}}

function copyCurrentPaths() {{
  if (!activeAsset) return;
  const paths = `Master SVG: D:/YOURDREAM.VN/VISUAL_ASSET_FACTORY/${{activeAsset.master_svg_path}}\\nMaster PNG: D:/YOURDREAM.VN/VISUAL_ASSET_FACTORY/${{activeAsset.master_png_path}}\\nStudent SVG: D:/YOURDREAM.VN/VISUAL_ASSET_FACTORY/${{activeAsset.student_svg_path}}\\nStudent PNG: D:/YOURDREAM.VN/VISUAL_ASSET_FACTORY/${{activeAsset.student_png_path}}`;
  navigator.clipboard.writeText(paths).then(() => {{
    alert('Đã sao chép đường dẫn 4 file trực quan vào Clipboard!');
  }});
}}

// Initial load
renderGrid();
</script>
</body>
</html>
"""

    os.makedirs(os.path.dirname(output_html_path), exist_ok=True)
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Đã biên dịch thành công Studio App tại: {output_html_path}")
    print(f"Tổng số mẫu asset nhúng sẵn: {len(samples)}")

if __name__ == "__main__":
    out_file = os.path.join(BASE_DIR, "studio", "YOURDREAM_Universal_Visual_Asset_Studio.html")
    build_studio_html(out_file)
