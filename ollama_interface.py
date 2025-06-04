import ollama

def query_ollama(prompt, model='mistral', temperature=0.7):
    return ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        options={'temperature': temperature}
    )['message']['content']
