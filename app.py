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

    # 🔍 Debug: show response (temporary)
    # st.write(result)

    if isinstance(result, list) and "generated_text" in result[0]:
        answer = result[0]["generated_text"]
    elif isinstance(result, dict) and "error" in result:
        answer = "Model is loading... please try again in few seconds"
    else:
        answer = "Unexpected response. Try again."

    st.write("Answer:", answer)
