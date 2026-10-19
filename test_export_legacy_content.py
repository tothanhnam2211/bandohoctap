import os
import shutil
import json
import unittest
import export_legacy_content

class TestExportLegacyContent(unittest.TestCase):
    def setUp(self):
        # Create a temporary workspace for testing
        self.test_dir = 'test_workspace'
        self.export_dir = 'legacy_export' # default hardcoded in the script

        # We need to temporarily change the script to work with our test paths,
        # but to keep it simple we can just mock the files in the current working directory
        # since we will run it from a subshell or we can chdir into test workspace
        os.makedirs(self.test_dir, exist_ok=True)
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

        os.makedirs('data', exist_ok=True)
        os.makedirs('assets/day-test', exist_ok=True)

        # Valid asset
        with open('assets/day-test/valid.png', 'w') as f:
            f.write('valid image')

    def tearDown(self):
        os.chdir(self.original_cwd)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_export_with_vietnamese_and_missing_assets(self):
        curriculum = [
            {
                "day": 1,
                "id": "K9_Toan_1",
                "title": "Ngày 01: Tiếng Việt có dấu",
                "status": "unlocked",
                "file": "data/day-01.json"
            },
            {
                "day": 2,
                "id": "K9_Toan_2",
                "title": "Ngày 02: Missing File",
                "status": "locked",
                "file": "data/day-02.json"
            }
        ]
        with open('data/curriculum.json', 'w', encoding='utf-8') as f:
            json.dump(curriculum, f, ensure_ascii=False)

        day_1_data = {
            "title": "Nội dung tiếng Việt",
            "image": "assets/day-test/valid.png",
            "missing_video": "assets/day-test/missing.mp4"
        }
        with open('data/day-01.json', 'w', encoding='utf-8') as f:
            json.dump(day_1_data, f, ensure_ascii=False)

        # Call the script's main
        export_legacy_content.main()

        # Verify export directory
        self.assertTrue(os.path.exists(self.export_dir))

        # Verify curriculum
        with open(f'{self.export_dir}/data/curriculum.json', 'r', encoding='utf-8') as f:
            exported_curr = json.load(f)
            self.assertEqual(len(exported_curr), 2)
            self.assertEqual(exported_curr[0]['title'], "Ngày 01: Tiếng Việt có dấu")

        # Verify day-01 data and unicode
        with open(f'{self.export_dir}/data/day-01.json', 'r', encoding='utf-8') as f:
            exported_day1 = json.load(f)
            self.assertEqual(exported_day1['title'], "Nội dung tiếng Việt")

        # Verify valid asset copied
        self.assertTrue(os.path.exists(f'{self.export_dir}/assets/day-test/valid.png'))

        # Verify missing asset not copied
        self.assertFalse(os.path.exists(f'{self.export_dir}/assets/day-test/missing.mp4'))

        # Verify inventory
        with open(f'{self.export_dir}/inventory.json', 'r', encoding='utf-8') as f:
            inventory = json.load(f)

            # available days
            self.assertEqual(len(inventory['available_days']), 1)
            self.assertEqual(inventory['available_days'][0]['day'], 1)

            # missing days (day-02 file doesn't exist)
            self.assertEqual(len(inventory['missing_days']), 1)
            self.assertEqual(inventory['missing_days'][0]['day'], 2)

            # unresolved references (missing.mp4)
            self.assertEqual(len(inventory['unresolved_references']), 1)
            self.assertEqual(inventory['unresolved_references'][0]['reference'], 'assets/day-test/missing.mp4')

        # Verify manifest
        with open(f'{self.export_dir}/manifest.json', 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            self.assertIn('data/curriculum.json', manifest)
            self.assertIn('data/day-01.json', manifest)
            self.assertIn('assets/day-test/valid.png', manifest)
            self.assertIn('inventory.json', manifest)

    def test_malformed_json_curriculum(self):
        # Write invalid JSON
        with open('data/curriculum.json', 'w', encoding='utf-8') as f:
            f.write('[ {"day": 1, "title": "Missing quotes} ]')

        with self.assertRaises(json.JSONDecodeError):
            export_legacy_content.main()

    def test_malformed_json_day(self):
        curriculum = [
            {
                "day": 1,
                "file": "data/day-01.json"
            }
        ]
        with open('data/curriculum.json', 'w', encoding='utf-8') as f:
            json.dump(curriculum, f)

        # Write invalid JSON
        with open('data/day-01.json', 'w', encoding='utf-8') as f:
            f.write('{ "title": "Missing quotes }')

        with self.assertRaises(json.JSONDecodeError):
            export_legacy_content.main()

    def test_duplicate_ids(self):
        curriculum = [
            {
                "day": 1,
                "id": "K9_Toan_1",
                "title": "Ngày 01",
                "status": "unlocked",
                "file": "data/day-01.json"
            },
            {
                "day": 2,
                "id": "K9_Toan_1", # Duplicate ID
                "title": "Ngày 02",
                "status": "locked",
                "file": "data/day-02.json"
            }
        ]
        with open('data/curriculum.json', 'w', encoding='utf-8') as f:
            json.dump(curriculum, f, ensure_ascii=False)

        with open('data/day-01.json', 'w', encoding='utf-8') as f:
            json.dump({"title": "Day 1"}, f)

        with open('data/day-02.json', 'w', encoding='utf-8') as f:
            json.dump({"title": "Day 2"}, f)

        export_legacy_content.main()

        with open(f'{self.export_dir}/inventory.json', 'r', encoding='utf-8') as f:
            inventory = json.load(f)
            self.assertEqual(len(inventory['available_days']), 2)
            self.assertEqual(inventory['available_days'][0]['id'], "K9_Toan_1")
            self.assertEqual(inventory['available_days'][1]['id'], "K9_Toan_1")

    def test_deterministic_output(self):
        curriculum = [
            {
                "day": 1,
                "file": "data/day-01.json"
            }
        ]
        with open('data/curriculum.json', 'w', encoding='utf-8') as f:
            json.dump(curriculum, f)

        with open('data/day-01.json', 'w', encoding='utf-8') as f:
            json.dump({"b": 2, "a": 1}, f) # Unsorted keys

        export_legacy_content.main()

        # Read the manifest and check sort_keys=True effect
        with open(f'{self.export_dir}/manifest.json', 'r', encoding='utf-8') as f:
            manifest_str = f.read()
            manifest = json.loads(manifest_str)
            # Check deterministic keys sorting
            keys = list(manifest.keys())
            self.assertEqual(keys, sorted(keys))

if __name__ == '__main__':
    unittest.main()
