import unittest
from response_formatter import clean_response

class TestResponseFormatter(unittest.TestCase):
    def test_basic_formatting(self):
        raw = "\n\n## Answer\nThis is a test.\n\n"
        formatted = clean_response(raw)
        self.assertEqual(formatted.strip(), "Answer\nThis is a test.")

    def test_markdown_cleanup(self):
        raw = "### Title\n- Item 1\n- Item 2\n"
        formatted = clean_response(raw)
        self.assertNotIn("###", formatted)
        self.assertIn("Item 1", formatted)
