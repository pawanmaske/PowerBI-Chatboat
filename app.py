import streamlit as st
import requests

st.title("Power BI Assistant 🤖")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_KEY']}"
}

user_input = st.text_input("Ask your question:")

if user_input:
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": user_input}
    )

    # 🔥 SAFE HANDLING
    if response.status_code != 200:
        st.error(f"Error: {response.text}")
    else:
        try:
            result = response.json()
            
            if isinstance(result, list):
                st.write(result[0]["generated_text"])
            else:
                st.write(result)

        except:
            st.error("Model is loading... Please try again in a few seconds ⏳")
