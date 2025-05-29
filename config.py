import json
import os

def load_config(path='config.json'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file '{path}' not found.")

    with open(path, 'r') as f:
        config = json.load(f)

    required_keys = ['model', 'max_tokens', 'knowledge_base_path']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")

    return config