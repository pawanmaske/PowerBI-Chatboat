import requests
import streamlit as st

# HF OpenAI-compatible endpoint
API_URL = "https://api-inference.huggingface.co/v1/chat/completions"

# your token
HEADERS = {
    "Authorization": "Bearer hf_xxxxxxxxxxxxxxxxx",
    "Content-Type": "application/json"
}

def ask_ai(user_query):
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "system", "content": "You are a Power BI expert. Answer clearly with examples."},
            {"role": "user", "content": user_query}
        ],
        "max_tokens": 200
    }

    try:
        res = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)

        if res.status_code != 200:
            return f"API Error {res.status_code}: {res.text}"

        data = res.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"

st.title("Power BI Assistant 🤖")

query = st.text_input("Ask your question:")

if query:
    answer = ask_ai(query)
    st.write("Answer:", answer)
