import os
import shutil
import json
import hashlib

def get_asset_paths_from_dict(d):
    paths = []
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, str) and v.startswith('assets/'):
                paths.append(v)
            elif isinstance(v, (dict, list)):
                paths.extend(get_asset_paths_from_dict(v))
    elif isinstance(d, list):
        for item in d:
            paths.extend(get_asset_paths_from_dict(item))
    return paths

def main():
    export_dir = 'legacy_export'
    if os.path.exists(export_dir):
        shutil.rmtree(export_dir)
    os.makedirs(export_dir)

    with open('data/curriculum.json', 'r', encoding='utf-8') as f:
        curriculum = json.load(f)

    export_data_dir = os.path.join(export_dir, 'data')
    os.makedirs(export_data_dir, exist_ok=True)

    # Save curriculum
    with open(os.path.join(export_data_dir, 'curriculum.json'), 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=2)

    inventory = {
        'available_days': [],
        'missing_days': [],
        'unresolved_references': []
    }

    for item in curriculum:
        file_path = item.get('file')
        day_num = item.get('day')
        title = item.get('title')

        if file_path and os.path.exists(file_path):
            inventory['available_days'].append({
                'day': day_num,
                'title': title,
                'id': item.get('id')
            })
            with open(file_path, 'r', encoding='utf-8') as f:
                day_data = json.load(f)

            dest_file_path = os.path.join(export_dir, file_path)
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
            with open(dest_file_path, 'w', encoding='utf-8') as f:
                json.dump(day_data, f, ensure_ascii=False, indent=2)

            # Extract and copy assets
            asset_paths = get_asset_paths_from_dict(day_data)
            for asset_path in asset_paths:
                if os.path.exists(asset_path):
                    dest_asset_path = os.path.join(export_dir, asset_path)
                    os.makedirs(os.path.dirname(dest_asset_path), exist_ok=True)
                    shutil.copy2(asset_path, dest_asset_path)
                else:
                    inventory['unresolved_references'].append({
                        'day': day_num,
                        'reference': asset_path
                    })
        else:
            inventory['missing_days'].append({
                'day': day_num,
                'title': title,
                'id': item.get('id'),
                'expected_file': file_path
            })

    with open(os.path.join(export_dir, 'inventory.json'), 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    # Generate SHA-256 manifest
    manifest = {}
    for root, dirs, files in os.walk(export_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Make the path relative to export_dir for the manifest keys
            rel_path = os.path.relpath(file_path, export_dir)

            with open(file_path, 'rb') as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            manifest[rel_path] = file_hash

    with open(os.path.join(export_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, sort_keys=True)

if __name__ == '__main__':
    main()
