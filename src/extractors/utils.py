thonimport json

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Error loading JSON from {file_path}: {e}")

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise ValueError(f"Error saving JSON to {file_path}: {e}")