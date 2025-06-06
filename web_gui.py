from flask import Flask, request, render_template, session
import os
import re
from config import load_config
from notion_reader import fetch_notion_knowledge
from prompt_builder import build_prompt
from ollama_interface import query_ollama

app = Flask(__name__)
app.secret_key = os.urandom(24)

config = load_config()
knowledge = fetch_notion_knowledge()

def clean_response(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        query = request.form.get("query", "")
        if query.strip():
            prompt = build_prompt(knowledge, query, config["max_tokens"])
            answer = query_ollama(prompt, config["model"])
            clean = clean_response(answer)
            session["history"].append({"user": query, "assistant": clean})
            session.modified = True

    return render_template("chat.html", history=session["history"])

if __name__ == "__main__":
    app.run(debug=True)
