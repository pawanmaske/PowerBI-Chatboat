import streamlit as st
import requests

st.title("Power BI Assistant 🤖")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

API_KEY = st.secrets["OPENROUTER_API_KEY"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_ai(prompt):
    try:
        payload = {
            "model": "openchat/openchat-3.5-0106:free",  # ✅ only this changed
            "messages": [
                {"role": "system", "content": "You are a Power BI expert."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        elif "error" in data:
            return f"Error: {data['error']}"
        else:
            return "Unexpected response"

    except Exception as e:
        return f"Error: {str(e)}"

query = st.text_input("Ask your question:")

if query:
    answer = ask_ai(query)
    st.write("Answer:", answer)
