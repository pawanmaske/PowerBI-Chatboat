import streamlit as st
import requests

st.title("Power BI Assistant 🤖")

# OpenRouter API URL
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Get API key from Streamlit Secrets
API_KEY = st.secrets["OPENROUTER_API_KEY"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_ai(prompt):
    try:
        payload = {
            "model": "openchat/openchat-3.5-0106:free",  # working free model
            "messages": [
                {"role": "system", "content": "You are a Power BI expert. Answer clearly with examples."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        # If API fails
        if response.status_code != 200:
            return f"API Error {response.status_code}: {response.text}"

        data = response.json()

        # Debug (optional – remove later)
        # st.write(data)

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        elif "error" in data:
            return f"Error: {data['error']}"
        else:
            return "Unexpected response from API"

    except Exception as e:
        return f"Error: {str(e)}"

# UI
query = st.text_input("Ask your question:")

if query:
    answer = ask_ai(query)
    st.write("Answer:", answer)
