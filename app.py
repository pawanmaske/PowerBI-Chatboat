import streamlit as st
import requests

st.set_page_config(page_title="Power BI Assistant", layout="centered")

st.title("Power BI Assistant 🤖")

# Input
user_input = st.text_input("Ask your question:")

# When user asks something
if user_input:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": f"You are a Power BI expert. Answer clearly:\n{user_input}",
                "stream": False
            }
        )

        result = response.json()
        st.write("### Answer:")
        st.write(result["response"])

    except Exception as e:
        st.error("Error connecting to Ollama. Make sure it is running.")
