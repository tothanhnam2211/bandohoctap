# -*- coding: utf-8 -*-
"""
MODULE 6 — MULTIFORMAT RENDERING (mod6_multiformat_renderer.py)
Từ cùng một đặc tả Living Mathematical Asset thống nhất, kết xuất đồng thời 5 định dạng:
1. Interactive Living Experience HTML (output/interactive_html/<asset_id>.html) — Có Canvas/SVG động
   vẽ lại trực tiếp theo thao tác kéo/thử nghiệm của học sinh, chuyển đổi Learner A/B/C và 5 Artistic Worlds.
2. Layered Precision SVG (output/svg/<asset_id>.svg) — Tách lớp Art Layer và Math Layer.
3. A4 Printable Worksheet HTML & PDF (output/html_a4/, output/pdf_student/, output/pdf_teacher/) —
   Bản Học sinh (0% lộ đáp án) và Bản Giáo viên (đầy đủ lời giải & barem), in qua Headless Edge.
4. High-Resolution PNG Previews 150 DPI (output/previews_png/) — Kết xuất qua PyMuPDF (fitz).
5. Structured 6-DNA SDK JSON (output/json/<asset_id>.json).
"""

from __future__ import annotations
import os
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, List
import pymupdf as fitz

from .mod2_creative_asset_generator import CreativeAssetGenerator, ARTISTIC_WORLDS
from .math_typography import typeset_math_html, get_math_css
from .causal_interaction_engine import CausalInteractionEngine

candidate_sticky_dirs = [
    Path(__file__).resolve().parent.parent / "assets" / "sticky_notes_v01",
    Path(os.environ.get("LIVING_ASSET_FACTORY_DIR", ".")) / "assets" / "sticky_notes_v01",
    Path(r"D:\YOURDREAM.VN\03_ASSETS\sticky_notes_v01"),
]
STICKY_ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets" / "sticky_notes_v01"
for d in candidate_sticky_dirs:
    if d.exists() and (d / "YD_NOTE_yellow_BLANK_ALPHA_v01.png").exists():
        STICKY_ASSETS_DIR = d
        break
EDGE_PATHS = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
]

FORBIDDEN_STUDENT_TOKENS = [
    "SOURCE_VERIFIED",
    "TOC_ONLY_DEFERRED",
    "PEDAGOGICAL_REVIEW_PENDING",
    "PRODUCT_OWNER_APPROVED",
    "JULES_HANDOFF",
    "ĐÁP ÁN:",
    "HƯỚNG DẪN CHẤM",
]


def _find_edge_binary() -> str:
    for p in EDGE_PATHS:
        if p.exists():
            return str(p)
    raise FileNotFoundError("Microsoft Edge executable not found for headless PDF rendering.")


def _load_sticky_note_uris() -> Dict[str, str]:
    colors = ["yellow", "pink", "sage", "blue"]
    uris = {}
    for c in colors:
        p = STICKY_ASSETS_DIR / f"YD_NOTE_{c}_BLANK_ALPHA_v01.png"
        uris[c] = p.as_uri() if p.exists() else ""
    return uris


class MultiformatRenderer:
    """Module 6: Kết xuất đa định dạng (Interactive HTML + SVG + A4 PDF Student/Teacher + PNG + JSON)."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.dir_interactive = output_dir / "interactive_html"
        self.dir_svg = output_dir / "svg"
        self.dir_html_a4 = output_dir / "html_a4"
        self.dir_pdf_stu = output_dir / "pdf_student"
        self.dir_pdf_tea = output_dir / "pdf_teacher"
        self.dir_png = output_dir / "previews_png"
        self.dir_json = output_dir / "json"

        for d in (
            self.dir_interactive,
            self.dir_svg,
            self.dir_html_a4,
            self.dir_pdf_stu,
            self.dir_pdf_tea,
            self.dir_png,
            self.dir_json,
        ):
            d.mkdir(parents=True, exist_ok=True)

        self.svg_gen = CreativeAssetGenerator(self.dir_svg)
        self.causal_engine = CausalInteractionEngine()

    def _build_interactive_living_html(
        self, asset: Dict[str, Any], svg_static: str, stu_pdf_uri: str
    ) -> str:
        """Tạo trang HTML tương tác độc lập (Zero-CORS) với Canvas mô phỏng toán học trực tiếp."""
        aid = asset["asset_id"]
        asset_json_str = json.dumps(asset, ensure_ascii=False)
        worlds_json_str = json.dumps(ARTISTIC_WORLDS, ensure_ascii=False)

        return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{aid} — {asset['title']} | YOURDREAM Living Asset</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="if(window.renderMathInElement)renderMathInElement(document.body);"></script>
<style>
{get_math_css()}
  :root {{
    --bg-main: #0F172A;
    --bg-panel: #1E293B;
    --ink: #F8FAFC;
    --muted: #94A3B8;
    --accent: #38BDF8;
    --accent2: #10B981;
    --border: #334155;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
    background: var(--bg-main);
    color: var(--ink);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    transition: background 0.25s, color 0.25s;
  }}
  .top-bar {{
    padding: 12px 20px;
    background: #0F172A;
    color: #F8FAFC;
    border-bottom: 2px solid var(--accent);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }}
  .brand-row {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
  .badge {{
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 800;
    background: var(--accent);
    color: #0F172A;
  }}
  .badge-strand {{
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    background: rgba(56, 189, 248, 0.18);
    color: var(--accent);
    border: 1px solid var(--accent);
  }}
  .controls-top {{ display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }}
  .btn-pill {{
    padding: 6px 12px;
    border-radius: 7px;
    border: 1px solid var(--border);
    background: var(--bg-panel);
    color: var(--ink);
    font-size: 12.5px;
    font-weight: 700;
    cursor: pointer;
    text-decoration: none;
  }}
  .btn-pill.active {{
    background: var(--accent);
    color: #0F172A;
    border-color: var(--accent);
  }}
  .workspace {{
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 450px;
    gap: 18px;
    padding: 18px;
    max-width: 1560px;
    width: 100%;
    margin: 0 auto;
  }}
  @media (max-width: 1080px) {{
    .workspace {{
      grid-template-columns: 1fr;
    }}
  }}
  .stage-column {{
    display: flex;
    flex-direction: column;
    gap: 14px;
    min-width: 0;
  }}
  .story-banner {{
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-left: 5px solid var(--accent);
    border-radius: 12px;
    padding: 14px 18px;
  }}
  .story-banner h1 {{ font-size: 19px; font-weight: 800; margin-bottom: 6px; }}
  .story-banner p {{ font-size: 13.8px; line-height: 1.5; opacity: 0.92; }}
  .canvas-card {{
    background: var(--bg-panel);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .canvas-viewport {{
    width: 100%;
    height: 350px;
    background: #FFFFFF;
    border-radius: 10px;
    border: 1.5px solid #CBD5E1;
    overflow: hidden;
    position: relative;
  }}
  canvas#simCanvas {{
    width: 100%;
    height: 100%;
    display: block;
  }}
  .slider-deck {{
    background: rgba(15, 23, 42, 0.06);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
  }}
  .slider-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 8px;
  }}
  input[type=range] {{
    width: 100%;
    accent-color: var(--accent);
    cursor: pointer;
    height: 8px;
  }}
  .status-banner {{
    padding: 11px 14px;
    border-radius: 9px;
    font-weight: 700;
    font-size: 13.5px;
    border: 1.5px solid transparent;
  }}
  .status-ok {{
    background: rgba(16, 185, 129, 0.16);
    border-color: #10B981;
    color: #10B981;
  }}
  .status-warn {{
    background: rgba(245, 158, 11, 0.16);
    border-color: #F59E0B;
    color: #F59E0B;
  }}
  .pedagogy-column {{
    display: flex;
    flex-direction: column;
    gap: 14px;
    min-width: 0;
  }}
  .panel-card {{
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 15px 18px;
  }}
  .panel-card h3 {{
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    color: var(--accent);
    margin-bottom: 10px;
  }}
  .math-box {{
    font-family: "Cambria Math", "Segoe UI", serif;
    font-size: 14.5px;
    background: rgba(15, 23, 42, 0.22);
    padding: 10px 12px;
    border-radius: 8px;
    border: 1px solid var(--border);
    margin-top: 6px;
    line-height: 1.55;
  }}
  .scaffold-box {{
    font-size: 13.5px;
    line-height: 1.55;
    padding: 12px;
    border-radius: 8px;
    background: rgba(56, 189, 248, 0.1);
    border-left: 4px solid var(--accent);
  }}
  .trap-list {{
    padding-left: 18px;
    font-size: 13px;
    line-height: 1.5;
  }}
  .trap-list li {{ margin-bottom: 6px; }}
  .quiz-box {{
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .quiz-input-row {{
    display: flex;
    gap: 8px;
  }}
  .quiz-input-row input {{
    flex: 1;
    padding: 8px 12px;
    border-radius: 7px;
    border: 1px solid var(--border);
    font-size: 13.5px;
  }}
</style>
</head>
<body>
  <header class="top-bar">
    <div class="brand-row">
      <span class="badge">LỚP {asset['grade']} • {aid}</span>
      <span class="badge-strand">{asset['strand_name']}</span>
      <span style="font-size:12.5px; font-weight:700; opacity:0.85;">Kỹ năng: {asset['skill_id']} ({asset['math_semantics']['verification_type']})</span>
    </div>
    <div class="controls-top">
      <span style="font-size:12px; font-weight:700;">Hồ sơ người học:</span>
      <button class="btn-pill active" id="btnProfA" onclick="setProfile('A')">Learner A (Mất gốc/Trực quan)</button>
      <button class="btn-pill" id="btnProfB" onclick="setProfile('B')">Learner B (Chuẩn)</button>
      <button class="btn-pill" id="btnProfC" onclick="setProfile('C')">Learner C (Mở rộng)</button>
      <select class="btn-pill" id="worldSelect" onchange="setWorld(this.value)">
        <option value="WARM_STORYBOOK_TACTILE">Theme: Storybook Ấm Áp</option>
        <option value="STEM_COMMAND_3D">Theme: Đài Chỉ Huy STEM</option>
        <option value="EUCLIDEAN_ATELIER_PRO">Theme: Xưởng Hình Học</option>
        <option value="DATA_OBSERVATORY_LAB">Theme: Đài Dữ Liệu</option>
        <option value="REAL_PAPER_HYBRID_V04">Theme: Giấy Thật A4</option>
      </select>
      <a class="btn-pill" href="{stu_pdf_uri}" target="_blank" style="background:#10B981; color:#0F172A; border-color:#10B981;">📄 Mở Phiếu A4 (PDF)</a>
    </div>
  </header>

  <main class="workspace">
    <section class="stage-column">
      <div class="story-banner">
        <h1>{asset['title']}</h1>
        <p><strong>Câu chuyện dẫn nhập:</strong> {asset['story_hook']}</p>
      </div>

      <div class="canvas-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
          <span style="font-weight:800; font-size:14px;">MÔ HÌNH NHÂN - QUẢ &amp; CÁN CÂN THĂNG BẰNG ({", ".join(asset['primitives_used'])})</span>
          <div style="display:flex; gap:6px;">
            <button class="btn-pill" onclick="setTrialToDefault()">↺ Thử Nghiệm Ban Đầu</button>
            <button class="btn-pill" onclick="resetTrial()">Đặt Lại</button>
            <button class="btn-pill" onclick="checkCausalBalance()" style="background:#0284C7; color:#FFFFFF; border-color:#0284C7;">⚖ Kiểm Tra Cân Bằng Cán Cân</button>
          </div>
        </div>
        <div class="canvas-viewport">
          <canvas id="simCanvas" width="820" height="350"></canvas>
        </div>

        <div class="slider-deck">
          <div class="slider-head">
            <label for="trialSlider">{asset['interactive_engine']['control_label']}</label>
            <span id="trialValueDisplay" style="font-size:16px; font-weight:800; color:var(--accent);"></span>
          </div>
          <input type="range" id="trialSlider"
                 min="{asset['interactive_engine']['min_val']}"
                 max="{asset['interactive_engine']['max_val']}"
                 step="{asset['interactive_engine']['step_val']}"
                 value="{asset['interactive_engine']['default_trial']}"
                 oninput="onSliderChange(this.value)">
        </div>

        <div id="statusBanner" class="status-banner status-warn"></div>
      </div>

      <div class="panel-card">
        <h3>Sơ Đồ Cấu Trúc Chuẩn (Layered Vector SVG)</h3>
        <div style="background:#FFFFFF; border-radius:10px; padding:8px; border:1px solid #CBD5E1;">
          {svg_static}
        </div>
      </div>
    </section>

    <aside class="pedagogy-column">
      <div class="panel-card">
        <h3>1. Trợ Lý Sư Phạm Thích Ứng (Learner Profile A / B / C)</h3>
        <div id="scaffoldText" class="scaffold-box"></div>
      </div>

      <div class="panel-card">
        <h3>2. Bất Biến Toán Học &amp; Mô Hình Bài Toán</h3>
        <div style="font-size:13px; margin-bottom:6px;"><strong>Mục tiêu:</strong> {typeset_math_html(asset['objective'])}</div>
        <div class="math-box">
          <div>• <strong>Miền xác định:</strong> <span class="m-math">{typeset_math_html(asset['math_semantics']['domain_constraint'])}</span></div>
          <div>• <strong>Quan hệ bất biến:</strong> <span class="m-math">{typeset_math_html(asset['math_semantics']['invariant_relation'])}</span></div>
          <div style="color:#F59E0B; margin-top:5px; font-size:12.8px;">• <strong>Nhiệm vụ:</strong> Điều chỉnh thanh trượt để đưa Cán Cân Nhân - Quả về trạng thái thăng bằng tuyệt đối!</div>
          <div id="unlockedSolutionCard" style="display:none; margin-top:8px; padding:6px 9px; background:rgba(16,185,129,0.2); border-left:3px solid #10B981; border-radius:4px;">
            <div style="font-weight:800; color:#10B981; font-size:12.5px;">★ ĐÃ GIẢI MÃ THÀNH CÔNG:</div>
            <div style="font-size:13px; color:#F8FAFC; margin-top:3px;" class="m-math">{typeset_math_html(asset['math_semantics']['target_equation'])}</div>
          </div>
        </div>
      </div>

      <div class="panel-card">
        <h3>3. Chốt Chặn Sai Lầm Điển Hình</h3>
        <ul class="trap-list">
          {"".join(f"<li>{typeset_math_html(m)}</li>" for m in asset['misconceptions'])}
        </ul>
      </div>

      <div class="panel-card">
        <h3>4. Thử Thách Tự Kiểm Tra Nhanh</h3>
        <div class="quiz-box">
          <div style="font-size:13.2px; font-weight:600;">{typeset_math_html(asset['basic_exercises'][0]['prompt'])}</div>
          <div class="quiz-input-row">
            <input type="text" id="selfCheckInput" placeholder="Nhập câu trả lời của bạn...">
            <button class="btn-pill active" onclick="checkQuickAnswer()">Kiểm tra</button>
          </div>
          <div id="selfCheckFeedback" style="font-size:13px; font-weight:700; min-height:20px;"></div>
        </div>
      </div>
    </aside>
  </main>

<script>
const ASSET = {asset_json_str};
const WORLDS = {worlds_json_str};
let currentProfile = 'A';
let currentTrial = parseFloat(ASSET.interactive_engine.default_trial);

function setWorld(worldId) {{
  const w = WORLDS[worldId] || WORLDS['STEM_COMMAND_3D'];
  document.documentElement.style.setProperty('--bg-main', w.bg_primary);
  document.documentElement.style.setProperty('--bg-panel', w.bg_panel);
  document.documentElement.style.setProperty('--ink', w.ink_primary);
  document.documentElement.style.setProperty('--accent', w.accent_main);
  document.documentElement.style.setProperty('--accent2', w.accent_secondary);
  document.documentElement.style.setProperty('--border', w.border_color);
  document.getElementById('worldSelect').value = worldId;
  drawSimulation();
}}

function setProfile(p) {{
  currentProfile = p;
  ['A', 'B', 'C'].forEach(k => {{
    document.getElementById('btnProf' + k).classList.toggle('active', k === p);
  }});
  document.getElementById('scaffoldText').innerHTML =
    '<strong>Gợi ý Hồ sơ ' + p + ':</strong> ' + ASSET.learner_scaffolding[p];
}}

function setTrialToDefault() {{
  const v = ASSET.interactive_engine.default_trial;
  document.getElementById('trialSlider').value = v;
  onSliderChange(v);
}}

function resetTrial() {{
  const v = ASSET.interactive_engine.default_trial;
  document.getElementById('trialSlider').value = v;
  onSliderChange(v);
}}

function checkCausalBalance() {{
  const target = parseFloat(ASSET.interactive_engine.target_solution);
  const isSol = Math.abs(currentTrial - target) < 0.05;
  const banner = document.getElementById('statusBanner');
  if (isSol) {{
    banner.className = 'status-banner status-ok';
    banner.textContent = '★ XÁC NHẬN CÂN BẰNG! Chúc mừng bạn đã giải mã chính xác mô hình nhân - quả.';
    const solCard = document.getElementById('unlockedSolutionCard');
    if (solCard) solCard.style.display = 'block';
  }} else {{
    banner.className = 'status-banner status-warn';
    banner.textContent = '⚠ CÁN CÂN CHƯA THĂNG BẰNG: Quan sát độ lệch kim chỉ thị và tiếp tục điều chỉnh thanh trượt!';
  }}
}}

function onSliderChange(val) {{
  currentTrial = parseFloat(val);
  document.getElementById('trialValueDisplay').textContent =
    currentTrial + ' ' + ASSET.interactive_engine.unit;
  drawSimulation();
}}

function checkQuickAnswer() {{
  const raw = document.getElementById('selfCheckInput').value.trim().toLowerCase();
  const ans = ASSET.basic_exercises[0].final_answer.toLowerCase();
  const fb = document.getElementById('selfCheckFeedback');
  const numMatch = ans.match(/-?\\d+([.,]\\d+)?/);
  const keyNum = numMatch ? numMatch[0].replace(',', '.') : ans;
  if (raw && (raw.includes(keyNum) || raw === ans)) {{
    fb.style.color = '#10B981';
    fb.textContent = '✓ Chính xác! Bạn đã tìm ra kết quả đúng.';
  }} else {{
    fb.style.color = '#F59E0B';
    fb.textContent = '💡 Gợi ý Socratic: ' + ASSET.text_notes.note1_start.bullets[0] + ' Hãy quan sát cán cân và thử lại!';
  }}
}}

function drawPhysicalScene(ctx, x0, y0, w, h, asset, val, isSol) {{
  ctx.save();
  ctx.fillStyle = '#FFFFFF';
  ctx.strokeStyle = '#CBD5E1';
  ctx.lineWidth = 1;
  ctx.beginPath();
  if (ctx.roundRect) ctx.roundRect(x0, y0, w, h, 8);
  else ctx.rect(x0, y0, w, h);
  ctx.fill(); ctx.stroke();

  ctx.fillStyle = '#0F172A';
  ctx.font = 'bold 12px Segoe UI';
  ctx.fillText('HIỆN TRƯỜNG THỰC TẾ: ' + asset.title.split('(')[0].trim(), x0 + 12, y0 + 20);

  const eng = asset.interactive_engine.engine_type;
  const p = asset.interactive_engine.parameters;

  if (eng === 'GRID_TILING_GCD') {{
    const d = Math.max(1, Math.round(val));
    const scale = 11;
    const cw = p.width * scale, ch = p.height * scale;
    const ox = x0 + 20, oy = y0 + 35;
    ctx.strokeStyle = '#78350F'; ctx.lineWidth = 2.5;
    ctx.strokeRect(ox, oy, cw, ch);
    const cols = Math.floor(p.width / d), rows = Math.floor(p.height / d);
    for (let r = 0; r < rows; r++) {{
      for (let c = 0; c < cols; c++) {{
        ctx.fillStyle = (r + c) % 2 === 0 ? '#FDE68A' : '#FCD34D';
        ctx.fillRect(ox + c * d * scale + 1, oy + r * d * scale + 1, d * scale - 2, d * scale - 2);
      }}
    }}
    const remW = p.width % d, remH = p.height % d;
    if (remW > 0) {{
      ctx.fillStyle = 'rgba(239, 68, 68, 0.5)';
      ctx.fillRect(ox + cols * d * scale, oy, remW * scale, ch);
    }}
    if (remH > 0) {{
      ctx.fillStyle = 'rgba(239, 68, 68, 0.5)';
      ctx.fillRect(ox, oy + rows * d * scale, cw, remH * scale);
    }}
    ctx.fillStyle = isSol ? '#15803D' : '#991B1B';
    ctx.font = 'bold 11px Segoe UI';
    ctx.fillText(isSol ? '✓ Lát khít: 4 x 3 = 12 viên (Không cắt)' : '✗ Thừa đỏ: dư ' + remW + 'dm & ' + remH + 'dm (Phải cắt gạch)', ox, oy + ch + 20);
  }} else if (eng === 'RATE_BALANCE_RATIONAL' || asset.asset_id === 'YD-LA-ALG-G8-07') {{
    const numTrucks = Math.max(1, Math.round(60 / val));
    const ox = x0 + 15, oy = y0 + 35;
    ctx.fillStyle = '#334155';
    ctx.fillRect(ox, oy + 70, w - 30, 40);
    ctx.strokeStyle = '#FDE047'; ctx.setLineDash([10, 8]); ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(ox, oy + 90); ctx.lineTo(ox + w - 30, oy + 90); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#0284C7';
    ctx.fillRect(ox + w - 65, oy + 30, 38, 40);
    ctx.fillStyle = '#0F172A'; ctx.font = 'bold 9px Segoe UI';
    ctx.fillText('KHO GẠO 60T', ox + w - 75, oy + 25);
    const displayTrucks = Math.min(5, numTrucks);
    for (let t = 0; t < displayTrucks; t++) {{
      const tx = ox + 10 + t * 44;
      const ty = oy + 76;
      ctx.fillStyle = isSol ? '#10B981' : '#38BDF8';
      ctx.fillRect(tx, ty, 30, 16);
      ctx.fillStyle = '#1E293B';
      ctx.beginPath(); ctx.arc(tx + 6, ty + 18, 4, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(tx + 22, ty + 18, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#F59E0B';
      ctx.fillRect(tx + 2, ty - 5, 16, 5);
    }}
    ctx.fillStyle = '#0F172A'; ctx.font = '11.5px Segoe UI';
    ctx.fillText('Đội xe dự định: (60/' + val + ') = ' + (60/val).toFixed(1) + ' xe', ox, oy + 145);
    ctx.fillText('Thực tế thêm 3 xe: (60/' + (val+3) + ') = ' + (60/(val+3)).toFixed(1) + ' xe', ox, oy + 165);
    ctx.fillStyle = isSol ? '#15803D' : '#B45309'; ctx.font = 'bold 11.5px Segoe UI';
    ctx.fillText('Độ lệch thời gian thực tế: Δt = ' + (60/val - 60/(val+3)).toFixed(2) + ' ngày', ox, oy + 188);
  }} else if (asset.asset_id === 'YD-LA-GEO-G8-13') {{
    const ox = x0 + 60, oy = y0 + 185;
    ctx.strokeStyle = '#0F172A'; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(ox - 25, oy); ctx.lineTo(ox + 160, oy); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(ox, oy + 10); ctx.lineTo(ox, oy - 135); ctx.stroke();
    const groundD = 70, wallH = 95;
    ctx.strokeStyle = isSol ? '#10B981' : '#E11D48'; ctx.lineWidth = 4.5;
    ctx.beginPath(); ctx.moveTo(ox, oy - wallH); ctx.lineTo(ox + groundD, oy); ctx.stroke();
    ctx.fillStyle = '#0F172A'; ctx.font = '11px Segoe UI';
    ctx.fillText('Tường: 4m', ox + 6, oy - 50);
    ctx.fillText('Đất: 3m', ox + 20, oy + 16);
    ctx.fillStyle = isSol ? '#15803D' : '#BE123C'; ctx.font = 'bold 11.5px Segoe UI';
    ctx.fillText('Thang: L = ' + val + 'm ' + (isSol ? '(Chuẩn khít 5m)' : '(Lệch đỉnh tường)'), ox + 40, oy - 60);
  }} else if (asset.asset_id === 'YD-LA-ALG-G9-09') {{
    const ox = x0 + 175, oy = y0 + 170;
    ctx.strokeStyle = '#0F172A'; ctx.lineWidth = 2;
    ctx.fillStyle = '#E0F2FE'; ctx.fillRect(x0 + 10, oy, w - 20, 45);
    ctx.beginPath(); ctx.strokeStyle = '#0284C7'; ctx.lineWidth = 3.5;
    for (let px = -110; px <= 110; px += 4) {{
      const py = - (px * px) / 150;
      if (px === -110) ctx.moveTo(ox + px, oy + py);
      else ctx.lineTo(ox + px, oy + py);
    }}
    ctx.stroke();
    const bx = val * 7.5;
    ctx.fillStyle = isSol ? '#10B981' : '#F59E0B';
    ctx.fillRect(ox - bx, oy - 48, bx * 2, 48);
    ctx.fillStyle = '#0F172A'; ctx.font = 'bold 11px Segoe UI';
    ctx.fillText('Sà lan mép x = ' + val + 'm', ox - 45, oy - 55);
  }} else {{
    const ox = x0 + 20, oy = y0 + 40;
    ctx.fillStyle = '#F8FAFC'; ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 1;
    ctx.fillRect(ox, oy, w - 40, 150);
    ctx.strokeRect(ox, oy, w - 40, 150);
    ctx.fillStyle = '#0F172A'; ctx.font = 'bold 12.5px Segoe UI';
    ctx.fillText(asset.title.split('(')[0].trim(), ox + 15, oy + 28);
    ctx.font = '11.5px Segoe UI'; ctx.fillStyle = '#475569';
    ctx.fillText('Biến số: ' + asset.interactive_engine.control_label, ox + 15, oy + 60);
    ctx.fillText('Thử nghiệm: ' + val + ' ' + asset.interactive_engine.unit, ox + 15, oy + 88);
    ctx.fillStyle = isSol ? '#15803D' : '#D97706'; ctx.font = 'bold 12px Segoe UI';
    ctx.fillText(isSol ? '✓ Đạt trạng thái cân bằng lý tưởng!' : '→ Đang khảo sát sai số nhân - quả...', ox + 15, oy + 125);
  }}
  ctx.restore();
}}

function drawCausalBalanceScale(ctx, cx, cy, armL, asset, val, target, isSol) {{
  ctx.save();
  ctx.fillStyle = '#0F172A';
  ctx.font = 'bold 12.5px Segoe UI';
  ctx.fillText('CÁN CÂN THĂNG BẰNG ĐẠI SỐ (EQUILIBRIUM)', cx - 135, cy - 80);

  const diff = val - target;
  const tiltDeg = isSol ? 0.0 : Math.max(-24.0, Math.min(24.0, diff * 7.0));
  const tiltRad = tiltDeg * Math.PI / 180;

  // Stand
  ctx.fillStyle = '#475569';
  ctx.beginPath();
  ctx.moveTo(cx - 22, cy + 90);
  ctx.lineTo(cx + 22, cy + 90);
  ctx.lineTo(cx + 5, cy);
  ctx.lineTo(cx - 5, cy);
  ctx.closePath();
  ctx.fill();

  // Pivot circle
  ctx.fillStyle = '#0284C7';
  ctx.beginPath(); ctx.arc(cx, cy, 8, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = '#FFFFFF';
  ctx.beginPath(); ctx.arc(cx, cy, 3.5, 0, Math.PI * 2); ctx.fill();

  // Dial Arc
  ctx.strokeStyle = '#94A3B8'; ctx.lineWidth = 1.8;
  ctx.beginPath();
  ctx.arc(cx, cy - 6, 36, -Math.PI * 0.8, -Math.PI * 0.2);
  ctx.stroke();

  // Green center mark
  ctx.strokeStyle = '#10B981'; ctx.lineWidth = 3.5;
  ctx.beginPath();
  ctx.arc(cx, cy - 6, 36, -Math.PI * 0.53, -Math.PI * 0.47);
  ctx.stroke();

  // Indicator Needle
  const needleAngle = -Math.PI / 2 + tiltRad;
  ctx.strokeStyle = isSol ? '#10B981' : '#EF4444';
  ctx.lineWidth = 2.2;
  ctx.beginPath();
  ctx.moveTo(cx, cy);
  ctx.lineTo(cx + Math.cos(needleAngle) * 40, cy + Math.sin(needleAngle) * 40);
  ctx.stroke();

  // Rotating Beam
  const cosT = Math.cos(tiltRad), sinT = Math.sin(tiltRad);
  const lx = cx - cosT * armL, ly = cy - sinT * armL;
  const rx = cx + cosT * armL, ry = cy + sinT * armL;

  ctx.strokeStyle = isSol ? '#10B981' : '#F59E0B';
  ctx.lineWidth = 5.5;
  ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(lx, ly); ctx.lineTo(rx, ry); ctx.stroke();

  // Pans
  const panH = 46;
  ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(lx, ly); ctx.lineTo(lx - 18, ly + panH); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(lx, ly); ctx.lineTo(lx + 18, ly + panH); ctx.stroke();

  ctx.fillStyle = isSol ? '#D1FAE5' : '#E0F2FE';
  ctx.strokeStyle = isSol ? '#10B981' : '#0284C7';
  ctx.lineWidth = 1.8;
  ctx.beginPath();
  if (ctx.roundRect) ctx.roundRect(lx - 42, ly + panH, 84, 32, 5);
  else ctx.rect(lx - 42, ly + panH, 84, 32);
  ctx.fill(); ctx.stroke();
  ctx.fillStyle = '#0F172A'; ctx.font = 'bold 10.5px Segoe UI';
  ctx.fillText('Vế Thử: ' + val, lx - 34, ly + panH + 15);
  ctx.font = '9.5px Segoe UI'; ctx.fillStyle = '#0369A1';
  ctx.fillText(isSol ? '✓ Cân Bằng' : (diff > 0 ? 'Thừa tải' : 'Thiếu tải'), lx - 34, ly + panH + 26);

  ctx.strokeStyle = '#64748B'; ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(rx, ry); ctx.lineTo(rx - 18, ry + panH); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(rx, ry); ctx.lineTo(rx + 18, ry + panH); ctx.stroke();

  ctx.fillStyle = isSol ? '#D1FAE5' : '#FEF3C7';
  ctx.strokeStyle = isSol ? '#10B981' : '#F59E0B';
  ctx.lineWidth = 1.8;
  ctx.beginPath();
  if (ctx.roundRect) ctx.roundRect(rx - 42, ry + panH, 84, 32, 5);
  else ctx.rect(rx - 42, ry + panH, 84, 32);
  ctx.fill(); ctx.stroke();
  ctx.fillStyle = '#0F172A'; ctx.font = 'bold 10.5px Segoe UI';
  ctx.fillText('Đích Đề Bài', rx - 34, ry + panH + 15);
  ctx.font = '9.5px Segoe UI'; ctx.fillStyle = isSol ? '#15803D' : '#B45309';
  ctx.fillText(isSol ? '0.0° Khớp 100%' : 'Chờ cân bằng', rx - 34, ry + panH + 26);

  // Status banner under scale
  ctx.fillStyle = isSol ? '#ECFDF5' : '#FFFBEB';
  ctx.strokeStyle = isSol ? '#10B981' : '#F59E0B';
  ctx.lineWidth = 1.2;
  ctx.beginPath();
  if (ctx.roundRect) ctx.roundRect(cx - 125, cy + 82, 250, 22, 4);
  else ctx.rect(cx - 125, cy + 82, 250, 22);
  ctx.fill(); ctx.stroke();
  ctx.fillStyle = isSol ? '#065F46' : '#92400E';
  ctx.font = 'bold 10.5px Segoe UI';
  ctx.fillText(isSol ? '★ CÁN CÂN CÂN BẰNG HOÀN TOÀN (0° LỆCH)' : ('⚠ CÁN CÂN LỆCH ' + (diff > 0 ? 'TRÁI' : 'PHẢI') + ' (' + Math.abs(tiltDeg).toFixed(1) + '°)'), cx - 115, cy + 97);

  ctx.restore();
}}

function drawCausalReasoningRibbon(ctx, x, y, w, h, asset, val, target, isSol) {{
  ctx.save();
  ctx.fillStyle = '#0F172A';
  ctx.strokeStyle = isSol ? '#10B981' : '#38BDF8';
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  if (ctx.roundRect) ctx.roundRect(x, y, w, h, 7);
  else ctx.rect(x, y, w, h);
  ctx.fill(); ctx.stroke();

  ctx.fillStyle = isSol ? '#10B981' : '#38BDF8';
  ctx.font = 'bold 11px Segoe UI';
  ctx.fillText('SỔ TAY LẬP LUẬN NHÂN - QUẢ (CAUSAL REASONING LOG):', x + 14, y + 18);

  ctx.fillStyle = '#F8FAFC';
  ctx.font = '11px Segoe UI';
  const diff = val - target;
  let causeText = '▶ Hành động: Thử giá trị = ' + val + ' ' + asset.interactive_engine.unit + '.';
  let effectText = isSol
    ? '▶ Hệ quả: Hai vế phương trình đạt thế cân bằng tuyệt đối! Mọi bất biến toán học được thỏa mãn.'
    : (diff > 0
        ? '▶ Hệ quả: Giá trị thử nghiệm cao hơn điểm cân bằng, vế trái thừa tải làm cán cân lệch.'
        : '▶ Hệ quả: Giá trị thử nghiệm thấp hơn điểm cân bằng, vế trái thiếu tải so với yêu cầu.');
  let invariantText = '▶ Bảo toàn bất biến: Giữ nguyên 100% các điều kiện và hằng số của bài toán.';

  ctx.fillText(causeText + '  ' + effectText, x + 14, y + 36);
  ctx.fillStyle = '#94A3B8';
  ctx.font = '10.5px Segoe UI';
  ctx.fillText(invariantText + ' (Không tự ý biến dạng giả thiết khi thử sai số).', x + 14, y + 52);

  ctx.restore();
}}

function drawSimulation() {{
  const canvas = document.getElementById('simCanvas');
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height;
  ctx.clearRect(0, 0, W, H);

  const target = parseFloat(ASSET.interactive_engine.target_solution);
  const isSol = Math.abs(currentTrial - target) < 0.05;
  const banner = document.getElementById('statusBanner');
  const solCard = document.getElementById('unlockedSolutionCard');

  // Background
  const bgGrad = ctx.createLinearGradient(0, 0, 0, H);
  bgGrad.addColorStop(0, '#F8FAFC');
  bgGrad.addColorStop(1, '#F1F5F9');
  ctx.fillStyle = bgGrad;
  ctx.fillRect(0, 0, W, H);

  ctx.strokeStyle = '#E2E8F0';
  ctx.lineWidth = 1;
  for (let x = 0; x < W; x += 35) {{ ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }}
  for (let y = 0; y < H; y += 35) {{ ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }}

  // Divider
  ctx.strokeStyle = '#CBD5E1'; ctx.lineWidth = 1.5; ctx.setLineDash([4, 4]);
  ctx.beginPath(); ctx.moveTo(410, 10); ctx.lineTo(410, 265); ctx.stroke();
  ctx.setLineDash([]);

  // 1. Physical Scene Simulation (Left)
  drawPhysicalScene(ctx, 35, 15, 360, 250, ASSET, currentTrial, isSol);

  // 2. Dynamic Causal Balance Scale (Right)
  drawCausalBalanceScale(ctx, 615, 135, 140, ASSET, currentTrial, target, isSol);

  // 3. Bottom Socratic Causal Reasoning Ribbon
  drawCausalReasoningRibbon(ctx, 20, 275, 780, 65, ASSET, currentTrial, target, isSol);

  // Status Banner & Unlocked Solution Card
  if (isSol) {{
    banner.className = 'status-banner status-ok';
    banner.textContent = '★ TRẠNG THÁI CÂN BẰNG ĐẠT ĐƯỢC! Mô hình toán học đã được thỏa mãn tuyệt đối.';
    if (solCard) solCard.style.display = 'block';
  }} else {{
    banner.className = 'status-banner status-warn';
    banner.textContent = '⚠ CÁN CÂN ĐANG MẤT CÂN BẰNG: Hãy quan sát độ lệch đĩa cân và tiếp tục điều chỉnh để tìm điểm thăng bằng!';
    if (solCard) solCard.style.display = 'none';
  }}
}}

setProfile('A');
setWorld(ASSET.artistic_world);
onSliderChange(ASSET.interactive_engine.default_trial);
</script>
</body>
</html>"""

    def _build_a4_worksheet_html(
        self,
        asset: Dict[str, Any],
        svg_diagram: str,
        sticky_uris: Dict[str, str],
        is_teacher: bool = False,
    ) -> str:
        """Tạo trang A4 chuẩn Real Paper v0.4 (1 trang A4 khít, tách biệt Học sinh & Giáo viên)."""
        no = asset["asset_no"]
        grade = asset["grade"]
        title = asset["title"]
        subtitle = asset["header_subtitle"]
        objective = asset["objective"]
        activation = asset["knowledge_activation"]
        we = asset["worked_example"]
        ex2a, ex2b = asset["basic_exercises"][0], asset["basic_exercises"][1]
        ex3 = asset["advanced_exercise"]
        ex4 = asset["real_world_problem"]
        tn = asset["text_notes"]

        steps_html = "".join(f'<div class="we-step">• {typeset_math_html(st)}</div>' for st in we["steps"])
        n1_bullets = "".join(f"<li>{typeset_math_html(b)}</li>" for b in tn["note1_start"]["bullets"])
        n2_bullets = "".join(f"<li>{typeset_math_html(b)}</li>" for b in tn["note2_watchout"]["bullets"])
        n3_bullets = "".join(f"<li>{typeset_math_html(b)}</li>" for b in tn["note3_check"]["bullets"])

        if not is_teacher:
            right_header = """
            <div class="student-info-box">
              <div>Họ và tên: ....................................................</div>
              <div style="margin-top:3px;">Lớp: .......... &nbsp;&nbsp;Ngày: ....../....../20......</div>
            </div>"""
            ex2a_work = '<div class="work-label">Bài làm:</div><div class="dot-line"></div><div class="dot-line"></div>'
            ex2b_work = '<div class="work-label">Bài làm:</div><div class="dot-line"></div><div class="dot-line"></div>'
            ex3_work = '<div class="work-label">Bài làm:</div><div class="dot-line"></div><div class="dot-line"></div>'
            ex4_work = '<div class="work-label">Bài làm:</div><div class="dot-line"></div><div class="dot-line"></div>'
            n4_body = '<div class="note-dot"></div><div class="note-dot"></div><div class="note-dot"></div>'
        else:
            right_header = f"""
            <div class="teacher-badge-box">
              <div style="font-weight:800; color:#991B1B; font-size:10px;">BẢN GIÁO VIÊN &amp; HƯỚNG DẪN CHẤM</div>
              <div style="font-size:8.8px; color:#7F1D1D; margin-top:2px;">Asset: {asset['asset_id']} • Kỹ năng: {asset['skill_id']}</div>
            </div>"""
            ex2a_work = f'<div class="ans-box"><strong>Kết quả: {typeset_math_html(ex2a["final_answer"])}</strong><br>{typeset_math_html(ex2a["teacher_solution"])}</div>'
            ex2b_work = f'<div class="ans-box"><strong>Kết quả: {typeset_math_html(ex2b["final_answer"])}</strong><br>{typeset_math_html(ex2b["teacher_solution"])}</div>'
            ex3_work = f'<div class="ans-box"><strong>Kết quả: {typeset_math_html(ex3["final_answer"])}</strong><br>{typeset_math_html(ex3["teacher_solution"])}</div>'
            ex4_work = f'<div class="ans-box"><strong>Kết quả: {typeset_math_html(ex4["final_answer"])}</strong><br>{typeset_math_html(ex4["teacher_solution"])}</div>'
            n4_body = f'<div style="font-size:8.6px; color:#0F172A;"><strong>Bất biến:</strong> {typeset_math_html(asset["math_semantics"]["invariant_relation"])}</div>'

        return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>YOURDREAM — Phiếu Living Asset Số {no} (Toán {grade})</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="if(window.renderMathInElement)renderMathInElement(document.body);"></script>
<style>
{get_math_css()}
  @page {{ size: A4 portrait; margin: 0; }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
  html, body {{
    width: 210mm; height: 297mm;
    font-family: "Segoe UI", Arial, sans-serif;
    color: #1E293B; background: #FFFFFF; overflow: hidden;
  }}
  .a4-sheet {{ width: 210mm; height: 297mm; display: flex; flex-direction: column; padding: 6.5mm 7.5mm 6mm 7.5mm; }}
  .top-header {{
    display: flex; justify-content: space-between; align-items: stretch;
    border-bottom: 2px solid #0284C7; padding-bottom: 4px; margin-bottom: 5px; gap: 8px;
  }}
  .header-left {{ flex: 1; }}
  .brand-kicker {{ font-size: 8.5px; font-weight: 800; color: #0284C7; text-transform: uppercase; }}
  .main-title {{ font-size: 13.5px; font-weight: 800; color: #0F172A; line-height: 1.2; margin-top: 1px; }}
  .obj-line {{ font-size: 8.7px; color: #334155; margin-top: 2px; }}
  .student-info-box, .teacher-badge-box {{
    width: 68mm; border: 1px dashed #64748B; border-radius: 5px;
    padding: 4px 7px; font-size: 9px; background: #F8FAFC;
  }}
  .teacher-badge-box {{ border: 1.5px solid #DC2626; background: #FEF2F2; }}
  .body-columns {{ flex: 1; display: flex; gap: 5mm; overflow: hidden; }}
  .col-left {{ width: 64.5%; display: flex; flex-direction: column; gap: 4.5px; }}
  .col-right {{
    width: 35.5%; background: #EFECE6; border-radius: 7px;
    padding: 6px 6.5px; display: flex; flex-direction: column; justify-content: space-between;
    border: 1px solid #DCD6CC;
  }}
  .sec-card {{ border: 1px solid #CBD5E1; border-radius: 6px; padding: 4.5px 7px; background: #FFFFFF; }}
  .sec-title {{ font-size: 9.5px; font-weight: 800; color: #0369A1; text-transform: uppercase; margin-bottom: 2px; }}
  .act-box {{ background: #F0F9FF; border-color: #BAE6FD; font-size: 8.8px; line-height: 1.3; }}
  .svg-wrap {{ width: 100%; height: 34mm; margin: 2px 0; overflow: hidden; border-radius: 4px; }}
  .we-prob {{ font-size: 8.9px; font-weight: 700; color: #0F172A; margin-bottom: 2px; line-height: 1.28; }}
  .we-step {{ font-size: 8.4px; color: #1E293B; line-height: 1.26; margin-bottom: 1.5px; }}
  .ex-prompt {{ font-size: 8.8px; color: #0F172A; line-height: 1.28; margin-bottom: 2px; }}
  .work-label {{ font-size: 8px; font-weight: 700; color: #64748B; }}
  .dot-line {{ border-bottom: 1px dotted #94A3B8; height: 4.3mm; width: 100%; }}
  .ans-box {{ background: #F0FDF4; border-left: 2.5px solid #16A34A; padding: 3px 6px; font-size: 8.3px; color: #14532D; line-height: 1.25; }}
  .sticky-card {{
    position: relative; border-radius: 6px; padding: 7px 8px 6px 8px;
    box-shadow: 0 2px 5px rgba(15,23,42,0.08); font-size: 8.4px; line-height: 1.28;
  }}
  .note-yellow {{ background: #FEF9C3; border: 1px solid #FDE047; transform: rotate(-0.5deg); }}
  .note-pink {{ background: #FCE7F3; border: 1px solid #F9A8D4; transform: rotate(0.4deg); }}
  .note-sage {{ background: #DCFCE7; border: 1px solid #86EFAC; transform: rotate(-0.4deg); }}
  .note-blue {{ background: #E0F2FE; border: 1px solid #7DD3FC; transform: rotate(0.3deg); }}
  .sticky-title {{ font-size: 9px; font-weight: 800; margin-bottom: 3px; color: #0F172A; }}
  .sticky-card ul {{ padding-left: 12px; }}
  .sticky-card li {{ margin-bottom: 2px; }}
  .note-dot {{ border-bottom: 1px dotted #64748B; height: 4.5mm; width: 100%; }}
  .footer-bar {{
    margin-top: 3px; padding-top: 3px; border-top: 1px solid #CBD5E1;
    display: flex; justify-content: space-between; font-size: 7.8px; color: #64748B;
  }}
</style>
</head>
<body>
  <div class="a4-sheet">
    <header class="top-header">
      <div class="header-left">
        <div class="brand-kicker">{subtitle} • PHIẾU HỌC TẬP SỐ {no}</div>
        <div class="main-title">{title}</div>
        <div class="obj-line"><strong>Mục tiêu cần đạt:</strong> {typeset_math_html(objective)}</div>
      </div>
      {right_header}
    </header>

    <div class="body-columns">
      <div class="col-left">
        <div class="sec-card act-box">
          <div class="sec-title">I. KÍCH HOẠT TƯ DUY &amp; MÔ HÌNH TRỰC QUAN</div>
          <div>{typeset_math_html(activation)}</div>
          <div class="svg-wrap">{svg_diagram}</div>
        </div>

        <div class="sec-card">
          <div class="sec-title">II. VÍ DỤ MINH HỌA TỪNG BƯỚC</div>
          <div class="we-prob">Đề bài: {typeset_math_html(we['problem'])}</div>
          {steps_html}
        </div>

        <div class="sec-card">
          <div class="sec-title">III. LUYỆN TẬP CƠ BẢN &amp; THỰC HÀNH</div>
          <div class="ex-prompt"><strong>{ex2a['label']}:</strong> {typeset_math_html(ex2a['prompt'])}</div>
          {ex2a_work}
          <div class="ex-prompt" style="margin-top:3px;"><strong>{ex2b['label']}:</strong> {typeset_math_html(ex2b['prompt'])}</div>
          {ex2b_work}
        </div>

        <div class="sec-card">
          <div class="sec-title">IV. VẬN DỤNG NÂNG CAO &amp; THỰC TIỄN</div>
          <div class="ex-prompt"><strong>Câu 3 (Vận dụng):</strong> {typeset_math_html(ex3['prompt'])}</div>
          {ex3_work}
          <div class="ex-prompt" style="margin-top:3px;"><strong>Câu 4 (Thực tiễn):</strong> {typeset_math_html(ex4['prompt'])}</div>
          {ex4_work}
        </div>
      </div>

      <aside class="col-right">
        <div class="sticky-card note-yellow">
          <div class="sticky-title">📌 {tn['note1_start']['title']}</div>
          <ul>{n1_bullets}</ul>
        </div>
        <div class="sticky-card note-pink">
          <div class="sticky-title">⚠️ {tn['note2_watchout']['title']}</div>
          <ul>{n2_bullets}</ul>
        </div>
        <div class="sticky-card note-sage">
          <div class="sticky-title">✅ {tn['note3_check']['title']}</div>
          <ul>{n3_bullets}</ul>
        </div>
        <div class="sticky-card note-blue">
          <div class="sticky-title">💡 {tn['note4_reflection']['title']}</div>
          {n4_body}
        </div>
      </aside>
    </div>

    <footer class="footer-bar">
      <span>YOURDREAM Living Mathematical Asset Factory • Đồng bộ Mô hình Tương tác &amp; Phiếu Giấy A4</span>
      <span>Trang 1/1</span>
    </footer>
  </div>
</body>
</html>"""

    def _render_html_to_pdf_with_edge(self, edge_bin: str, html_path: Path, pdf_path: Path) -> None:
        cmd = [
            edge_bin,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={str(pdf_path)}",
            html_path.as_uri(),
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def render_all_16_assets(self, assets: List[Dict[str, Any]]) -> Dict[str, Any]:
        edge_bin = _find_edge_binary()
        sticky_uris = _load_sticky_note_uris()
        svg_paths = self.svg_gen.export_all_svgs(assets)

        render_jobs = []
        manifest_items = []

        for a in assets:
            aid = a["asset_id"]
            no = a["asset_no"]
            grade = a["grade"]
            svg_code = self.svg_gen.get_svg_for_asset(aid)

            stu_pdf_path = self.dir_pdf_stu / f"YOURDREAM_LivingAsset_G{grade}_{no}_{aid}_HocSinh.pdf"
            tea_pdf_path = self.dir_pdf_tea / f"YOURDREAM_LivingAsset_G{grade}_{no}_{aid}_GiaoVien.pdf"
            stu_html_a4 = self.dir_html_a4 / f"YOURDREAM_LivingAsset_G{grade}_{no}_{aid}_HocSinh.html"
            tea_html_a4 = self.dir_html_a4 / f"YOURDREAM_LivingAsset_G{grade}_{no}_{aid}_GiaoVien.html"
            interactive_path = self.dir_interactive / f"{aid}.html"
            json_path = self.dir_json / f"{aid}.json"

            # 1. Write A4 Student & Teacher HTML
            stu_a4_str = self._build_a4_worksheet_html(a, svg_code, sticky_uris, is_teacher=False)
            tea_a4_str = self._build_a4_worksheet_html(a, svg_code, sticky_uris, is_teacher=True)
            stu_html_a4.write_text(stu_a4_str, encoding="utf-8")
            tea_html_a4.write_text(tea_a4_str, encoding="utf-8")

            # 2. Write Interactive Living Experience HTML (Relative PDF link for universal portability)
            rel_pdf_uri = f"../pdf_student/{stu_pdf_path.name}"
            inter_str = self._build_interactive_living_html(a, svg_code, rel_pdf_uri)
            interactive_path.write_text(inter_str, encoding="utf-8")

            # 3. Write 6-DNA JSON spec
            json_path.write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding="utf-8")

            render_jobs.append((edge_bin, stu_html_a4, stu_pdf_path))
            render_jobs.append((edge_bin, tea_html_a4, tea_pdf_path))

            manifest_items.append({
                "asset_id": aid,
                "asset_no": no,
                "skill_id": a["skill_id"],
                "grade": grade,
                "strand_code": a["strand_code"],
                "title": a["title"],
                "interactive_html_path": str(interactive_path),
                "svg_path": svg_paths[aid],
                "student_html_a4_path": str(stu_html_a4),
                "teacher_html_a4_path": str(tea_html_a4),
                "student_pdf_path": str(stu_pdf_path),
                "teacher_pdf_path": str(tea_pdf_path),
                "json_path": str(json_path),
            })

        # Parallel Headless Edge PDF rendering
        with ThreadPoolExecutor(max_workers=6) as pool:
            futures = [pool.submit(self._render_html_to_pdf_with_edge, eb, hp, pp) for eb, hp, pp in render_jobs]
            for f in futures:
                f.result()

        # Render 150 DPI PNG Previews & Verify 1-Page + Zero Answer Leak on Student PDFs
        all_passed_gate = True
        for item in manifest_items:
            stu_pdf = Path(item["student_pdf_path"])
            tea_pdf = Path(item["teacher_pdf_path"])
            stu_png = self.dir_png / f"{item['asset_id']}_HocSinh_150dpi.png"
            tea_png = self.dir_png / f"{item['asset_id']}_GiaoVien_150dpi.png"

            with fitz.open(stu_pdf) as doc_s:
                stu_pages = len(doc_s)
                stu_text = doc_s[0].get_text("text")
                pix = doc_s[0].get_pixmap(dpi=150)
                pix.save(str(stu_png))

            with fitz.open(tea_pdf) as doc_t:
                tea_pages = len(doc_t)
                pix_t = doc_t[0].get_pixmap(dpi=150)
                pix_t.save(str(tea_png))

            leaked = [tok for tok in FORBIDDEN_STUDENT_TOKENS if tok in stu_text]
            passed_item = (stu_pages == 1) and (tea_pages == 1) and (len(leaked) == 0)
            if not passed_item:
                all_passed_gate = False

            item["student_png_preview"] = str(stu_png)
            item["teacher_png_preview"] = str(tea_png)
            item["student_pdf_pages"] = stu_pages
            item["teacher_pdf_pages"] = tea_pages
            item["zero_answer_leak_verified"] = len(leaked) == 0

        report = {
            "renderer_version": "2.2.0",
            "total_interactive_htmls": len(manifest_items),
            "total_svgs": len(manifest_items),
            "total_student_pdfs": len(manifest_items),
            "total_teacher_pdfs": len(manifest_items),
            "total_png_previews": len(manifest_items) * 2,
            "all_passed_single_page_and_zero_leak_gate": all_passed_gate,
            "assets": manifest_items,
        }
        (self.output_dir / "multiformat_render_report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return report
