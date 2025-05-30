def build_prompt(knowledge, query, max_tokens):
    if not knowledge.strip():
        knowledge = "No project knowledge provided."
    if not query.strip():
        query = "How can you help me?"

    prompt = (
        "You are an intelligent and approachable AI assistant helping a developer make sense of internal documentation.\n"
        "You have access to the full project knowledge below, and your job is to answer questions clearly and helpfully.\n"
        "If the answer is not directly stated, use logical reasoning based on related facts in the document. Be honest if it's unclear.\n"
        "Avoid sounding robotic. Keep your tone relaxed but respectful.\n\n"
        "Project Knowledge:\n"
        f"{knowledge.strip()}\n"
        "--- End of Document ---\n\n"
        f"User asked: {query.strip()}\n"
        "Your response:"
    )

    return prompt[:max_tokens]
