
from config import load_config

config = load_config()
print("Model:", config['model'])
print("Knowledge file:", config['knowledge_base_path'])