import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Power BI Assistant 🤖")

user_input = st.text_input("Ask your question:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Power BI expert."},
            {"role": "user", "content": user_input}
        ]
    )

    st.write("### Answer:")
    st.write(response.choices[0].message.content)
