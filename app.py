import requests
import streamlit as st

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": "Bearer sk-or-v1-xxxxxxxxxxxxxxxx",
    "Content-Type": "application/json"
}

def ask_ai(prompt):
    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a Power BI expert. Answer clearly."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    return data["choices"][0]["message"]["content"]

st.title("Power BI Assistant 🤖")

query = st.text_input("Ask your question:")

if query:
    answer = ask_ai(query)
    st.write("Answer:", answer)
