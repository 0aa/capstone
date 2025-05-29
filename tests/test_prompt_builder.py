import unittest
from prompt_builder import build_prompt

class TestPromptBuilder(unittest.TestCase):
    def test_prompt_with_short_knowledge(self):
        knowledge = "Always write unit tests for core modules."
        query = "Why are unit tests important?"
        prompt = build_prompt(knowledge, query)
        self.assertIn(knowledge, prompt)
        self.assertIn(query, prompt)

    def test_prompt_truncation(self):
        long_text = "test " * 2000  # Simulate long knowledge base
        query = "Summarize the content."
        prompt = build_prompt(long_text, query, max_tokens=4000)
        self.assertTrue(len(prompt.split()) <= 4000)

    def test_prompt_token_limit(self):
        knowledge = "token " * 5000  # Overload with token repetition
        query = "Explain the token limit issue."
        prompt = build_prompt(knowledge, query, max_tokens=1000)
        self.assertLessEqual(len(prompt.split()), 1000)

