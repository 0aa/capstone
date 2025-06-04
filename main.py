from config import load_config
from notion_reader import read_knowledge_file
from prompt_builder import build_prompt
from ollama_interface import query_model


def main():
    config = load_config()

    knowledge = read_knowledge_file(config["knowledge_file"])
    print("Loaded knowledge base.")

    while True:
        query = input("Ask a question (or 'exit'): ")
        if query.strip().lower() == "exit":
            break
        prompt = build_prompt(knowledge, query, config["max_tokens"])
        response = query_model(prompt, config["model"])
        print("\n[AI Assistant]:\n", response)


if __name__ == "__main__":
    main()
