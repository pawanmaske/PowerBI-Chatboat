import streamlit as st

st.title("Power BI Assistant 🤖")

query = st.text_input("Ask your question:")

if query:
    st.write("You asked:", query)
    st.write("Answer: Coming soon...")
