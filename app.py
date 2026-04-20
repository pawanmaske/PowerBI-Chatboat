import streamlit as st
from openai import OpenAI

st.title("Power BI Assistant 🤖")

client = OpenAI(api_key="PASTE_YOUR_REAL_KEY_HERE")

user_input = st.text_input("Ask your question:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Power BI expert."},
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)
