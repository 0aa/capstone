import unittest
import os
from notion_reader import read_knowledge_file

class TestNotionReader(unittest.TestCase):
    def test_read_existing_file(self):
        content = read_knowledge_file("sample_data/sample.md")
        self.assertTrue(len(content) > 0)
        self.assertIn("Project Overview", content)

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_knowledge_file("missing.md")

