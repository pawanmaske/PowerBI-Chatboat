import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxx"}  # your token

def query_hf(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return {"error": f"API Error: {response.status_code} - {response.text}"}

        return response.json()

    except Exception as e:
        return {"error": str(e)}

st.title("Power BI Assistant 🤖")

query = st.text_input("Ask your question:")

if query:
    prompt = f"You are a Power BI expert. Answer clearly:\n{query}"

    result = query_hf(prompt)

    if isinstance(result, list) and "generated_text" in result[0]:
        answer = result[0]["generated_text"]
    elif isinstance(result, dict) and "error" in result:
        answer = result["error"]
    else:
        answer = "Model loading... try again"

    st.write("Answer:", answer)
