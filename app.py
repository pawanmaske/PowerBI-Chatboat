import streamlit as st
import requests

st.title("Power BI Assistant 🤖")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/blenderbot-400M-distill"

headers = {
    "Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_KEY']}",
    "Content-Type": "application/json"
}

user_input = st.text_input("Ask your question:")

if user_input:
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": user_input}
    )

    if response.status_code != 200:
        st.error(f"Error: {response.text}")
    else:
        try:
            result = response.json()
            st.write(result[0].get("generated_text", "No response"))
        except:
            st.warning("Model loading... try again ⏳")
