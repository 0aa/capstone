import unittest
import os
from config import load_config

class TestConfig(unittest.TestCase):
    def test_load_valid_config(self):
        config = load_config("config.json")
        self.assertIn("model", config)
        self.assertIn("max_tokens", config)

    def test_missing_config_file(self):
        with self.assertRaises(FileNotFoundError):
            load_config("nonexistent.json")

