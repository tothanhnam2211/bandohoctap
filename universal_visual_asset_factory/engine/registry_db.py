# -*- coding: utf-8 -*-
"""
REGISTRY DATABASE (SQLITE & FTS5)
Lưu trữ và chỉ mục hóa toàn bộ 30,000+ assets của thư viện K12.
Cung cấp khả năng tìm kiếm toàn văn FTS5 tốc độ mili-giây theo lớp, mạch kiến thức, chủ đề và bất biến toán học.
"""

import sqlite3
import os
from typing import Dict, Any, List, Optional

DB_FILENAME = "visual_asset_registry.db"

def get_db_path(base_dir: str) -> str:
    return os.path.join(base_dir, DB_FILENAME)

def init_db(db_path: str, drop_existing: bool = False):
    """Khởi tạo cấu trúc bảng SQLite và FTS5 index"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    if drop_existing:
        cur.execute("DROP TABLE IF EXISTS asset_search_fts")
        cur.execute("DROP TABLE IF EXISTS asset_variants")
        cur.execute("DROP TABLE IF EXISTS asset_families")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS asset_families (
        family_id TEXT PRIMARY KEY,
        grade INTEGER,
        strand TEXT,
        chapter TEXT,
        topic_vi TEXT,
        generator_type TEXT,
        math_invariant TEXT,
        variants_count INTEGER DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS asset_variants (
        variant_id TEXT PRIMARY KEY,
        family_id TEXT,
        grade INTEGER,
        strand TEXT,
        chapter TEXT,
        topic_vi TEXT,
        title TEXT,
        generator_type TEXT,
        math_invariant TEXT,
        master_svg_path TEXT,
        master_png_path TEXT,
        student_svg_path TEXT,
        student_png_path TEXT,
        master_svg_bytes INTEGER,
        master_png_bytes INTEGER,
        student_svg_bytes INTEGER,
        student_png_bytes INTEGER,
        sha256_master_png TEXT,
        FOREIGN KEY (family_id) REFERENCES asset_families(family_id)
    )
    """)

    cur.execute("CREATE INDEX IF NOT EXISTS idx_var_family ON asset_variants(family_id)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_var_grade ON asset_variants(grade)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_var_strand ON asset_variants(strand)")

    # FTS5 Virtual Table for full-text search
    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS asset_search_fts USING fts5(
        variant_id,
        family_id,
        grade UNINDEXED,
        strand,
        chapter,
        topic_vi,
        title,
        math_invariant,
        tokenize = 'unicode61'
    )
    """)

    conn.commit()
    conn.close()


def insert_families_batch(db_path: str, families: List[Any]):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executemany("""
    INSERT OR REPLACE INTO asset_families (
        family_id, grade, strand, chapter, topic_vi, generator_type, math_invariant, variants_count
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        (f.family_id, f.grade, f.strand, f.chapter, f.topic_vi, f.generator_type, f.math_invariant, f.variants_target)
        for f in families
    ])
    conn.commit()
    conn.close()


def insert_variants_batch(db_path: str, variant_metas: List[Dict[str, Any]]):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    records = []
    fts_records = []
    for m in variant_metas:
        records.append((
            m["variant_id"],
            m["family_id"],
            m["grade"],
            m["strand"],
            m["chapter"],
            m["topic_vi"],
            m["title"],
            m["generator_type"],
            m["math_invariant"],
            m["files"]["master_svg"],
            m["files"]["master_png"],
            m["files"]["student_svg"],
            m["files"]["student_png"],
            m["sizes"]["master_svg_bytes"],
            m["sizes"]["master_png_bytes"],
            m["sizes"]["student_svg_bytes"],
            m["sizes"]["student_png_bytes"],
            m["hashes"]["master_png"],
        ))
        fts_records.append((
            m["variant_id"],
            m["family_id"],
            m["grade"],
            m["strand"],
            m["chapter"],
            m["topic_vi"],
            m["title"],
            m["math_invariant"],
        ))

    cur.executemany("""
    INSERT OR REPLACE INTO asset_variants (
        variant_id, family_id, grade, strand, chapter, topic_vi, title, generator_type, math_invariant,
        master_svg_path, master_png_path, student_svg_path, student_png_path,
        master_svg_bytes, master_png_bytes, student_svg_bytes, student_png_bytes, sha256_master_png
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, records)

    cur.executemany("""
    INSERT INTO asset_search_fts (
        variant_id, family_id, grade, strand, chapter, topic_vi, title, math_invariant
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, fts_records)

    conn.commit()
    conn.close()


def get_db_stats(db_path: str) -> Dict[str, Any]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM asset_families")
    fam_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM asset_variants")
    var_count = cur.fetchone()[0]

    cur.execute("SELECT grade, COUNT(*) FROM asset_variants GROUP BY grade ORDER BY grade")
    by_grade = dict(cur.fetchall())

    cur.execute("SELECT strand, COUNT(*) FROM asset_variants GROUP BY strand ORDER BY strand")
    by_strand = dict(cur.fetchall())

    cur.execute("""
    SELECT 
        SUM(master_svg_bytes), 
        SUM(master_png_bytes), 
        SUM(student_svg_bytes), 
        SUM(student_png_bytes) 
    FROM asset_variants
    """)
    byte_stats = cur.fetchone()

    conn.close()
    return {
        "family_count": fam_count,
        "variant_count": var_count,
        "total_rendered_files": var_count * 4,
        "by_grade": by_grade,
        "by_strand": by_strand,
        "bytes_summary": {
            "master_svg": byte_stats[0] or 0,
            "master_png": byte_stats[1] or 0,
            "student_svg": byte_stats[2] or 0,
            "student_png": byte_stats[3] or 0,
            "total_bytes": sum(filter(None, byte_stats)),
        }
    }
