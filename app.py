import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxx"}  # your token

def query_hf(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("Power BI Assistant 🤖")

query = st.text_input("Ask your question:")

if query:
    prompt = f"You are a Power BI expert. Answer clearly:\n{query}"

    result = query_hf(prompt)

    try:
        answer = result[0]["generated_text"]
    except:
        answer = "Model loading... try again"

    st.write("Answer:", answer)
