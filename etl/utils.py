import json


def load_json(path):
    """Load JSON file from given path."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, path, indent=2):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
