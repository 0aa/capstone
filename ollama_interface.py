

import ollama

def query_model(prompt, model='mistral'):
    return ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])['message']['content']
