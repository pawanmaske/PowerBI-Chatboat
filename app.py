import streamlit as st
import requests

st.title("Power BI Assistant 🤖")

API_URL = "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"

headers = {
    "Authorization": "Bearer sk-or-v1-xxxxxxxxxxxxxxxx",  # your key
    "Content-Type": "application/json"
}

def ask_ai(prompt):
    try:
        payload = {
            "model": "mistralai/mistral-7b-instruct:free",
            "messages": [
                {"role": "system", "content": "You are a Power BI expert."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        # Debug (see API response)
        # st.write(data)

        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        elif "error" in data:
            return f"Error: {data['error']}"
        else:
            return "Unexpected response"

    except Exception as e:
        return f"Error: {str(e)}"

# UI always loads first
query = st.text_input("Ask your question:")

if query:
    answer = ask_ai(query)
    st.write("Answer:", answer)
