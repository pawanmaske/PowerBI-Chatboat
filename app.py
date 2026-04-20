import streamlit as st
import requests

st.title("Power BI Assistant 🤖")

user_input = st.text_input("Ask your question:")

if user_input:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",   # make sure this model is installed
            "prompt": user_input,
            "stream": False
        }
    )

    result = response.json()
    st.write("Answer:", result["response"])
