

def build_prompt(knowledge, query, max_tokens=4000):
    knowledge = knowledge.strip() if knowledge else "No project knowledge provided."
    query = query.strip() if query else "No user query provided."

    prompt = f"Project Info:\n{knowledge}\n\nUser Question:\n{query}"
    return " ".join(prompt.split()[:max_tokens])