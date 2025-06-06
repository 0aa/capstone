from config import load_config
from notion_reader import fetch_notion_knowledge
from prompt_builder import build_prompt
from ollama_interface import query_ollama


def main():
    config = load_config()

    knowledge = fetch_notion_knowledge()
    print("Loaded knowledge base.")

    while True:
        query = input("Ask a question (or 'exit'): ")
        if query.strip().lower() == "exit":
            break
        prompt = build_prompt(knowledge, query, config["max_tokens"])
        response = query_ollama(prompt, config["model"])
        print("\n[AI Assistant]:\n", response)


if __name__ == "__main__":
    main()
