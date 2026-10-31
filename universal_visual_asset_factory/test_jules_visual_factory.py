# -*- coding: utf-8 -*-
"""
JULES VISUAL ASSET FACTORY TEST SUITE
Bài kiểm thử độc lập cho Jules:
1. Kiểm tra môi trường & import toàn bộ các modules nhà máy.
2. Kiểm tra SQLite registry & FTS5 full-text search.
3. Kiểm tra tính năng kết xuất động vector SVG & PNG 150 DPI trên một biến thể bất kỳ.
4. Kiểm tra tính toàn vẹn của tập mẫu đại diện sample_assets/.
"""

import os
import sys
import sqlite3
import hashlib
import unittest

HANDOFF_DIR = os.path.dirname(os.path.abspath(__file__))
if HANDOFF_DIR not in sys.path:
    sys.path.insert(0, HANDOFF_DIR)

class TestJulesVisualFactory(unittest.TestCase):

    def test_01_modules_import(self):
        """Kiểm tra import thành công toàn bộ engine"""
        try:
            from curriculum.k12_curriculum_catalog import get_k12_asset_families
            from engine.core_math_primitives import render_polygon_geometry, render_coordinate_plot_2d
            from engine.specialized_primitives import render_number_line, render_venn_diagram
            from engine.asset_renderer_dispatch import dispatch_render_svg
            from engine.variant_generator import generate_family_variants
            from engine.multiformat_exporter import export_variant
            from engine.registry_db import get_db_stats
            import pymupdf
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Import failed: {e}")

    def test_02_database_integrity(self):
        """Kiểm tra SQLite database và FTS5 index"""
        db_path = os.path.join(HANDOFF_DIR, "visual_asset_registry.db")
        self.assertTrue(os.path.exists(db_path), "Database file missing")

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM asset_families")
        fam_count = cur.fetchone()[0]
        self.assertEqual(fam_count, 166, "Expected 166 families in DB")

        cur.execute("SELECT COUNT(*) FROM asset_variants")
        var_count = cur.fetchone()[0]
        self.assertEqual(var_count, 7636, "Expected 7,636 variants in DB")

        # FTS5 search check
        cur.execute("SELECT COUNT(*) FROM asset_search_fts WHERE asset_search_fts MATCH 'parabol'")
        hits = cur.fetchone()[0]
        self.assertGreater(hits, 0, "FTS5 search should find parabol")
        conn.close()

    def test_03_dynamic_rendering_pipeline(self):
        """Kiểm tra render SVG và PNG 150 DPI cho 1 biến thể động"""
        from curriculum.k12_curriculum_catalog import get_k12_asset_families
        from engine.variant_generator import generate_family_variants
        from engine.asset_renderer_dispatch import dispatch_render_svg
        import pymupdf

        fam = get_k12_asset_families()[0]
        var = generate_family_variants(fam, count=1)[0]

        # Render Master SVG
        svg_m = dispatch_render_svg(var["generator_type"], var["params"], title="Test Master", is_student_worksheet=False)
        self.assertTrue(svg_m.startswith("<svg") and svg_m.endswith("</svg>"))

        # Render Master PNG 150 DPI
        doc = pymupdf.open(stream=svg_m.encode("utf-8"), filetype="svg")
        pix = doc[0].get_pixmap(dpi=150, alpha=True)
        png_bytes = pix.tobytes(output="png")
        doc.close()

        self.assertGreater(len(png_bytes), 1000)
        self.assertEqual(png_bytes[:8], b"\x89PNG\r\n\x1a\n", "PNG header invalid")

    def test_04_sample_assets_presence(self):
        """Kiểm tra tập mẫu đại diện sample_assets/"""
        sample_dir = os.path.join(HANDOFF_DIR, "sample_assets")
        self.assertTrue(os.path.exists(sample_dir))
        files = os.listdir(sample_dir)
        self.assertGreaterEqual(len(files), 20, "Expected at least 20 sample files")

if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING JULES VISUAL FACTORY ACCEPTANCE TESTS...")
    print("=" * 60)
    unittest.main(verbosity=2)
