import streamlit as st
import streamlit_authenticator as stauth

# user details
credentials = {
    "usernames": {
        "pawan": {
            "name": "Pawan",
            "password": "1234"
        },
        "friend": {
            "name": "Friend",
            "password": "abcd"
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "chatbot_cookie",
    "abc123",
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.title("Power BI Assistant 🤖")
    st.write(f"Welcome {name}")

    query = st.text_input("Ask your question:")

    if query:
        st.write("You asked:", query)
        st.write("Answer: Coming soon...")

elif authentication_status == False:
    st.error("Wrong username/password")

elif authentication_status == None:
    st.warning("Please login")
