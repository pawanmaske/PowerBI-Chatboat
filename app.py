import streamlit as st
import streamlit_authenticator as stauth

# user details
names = ["Pawan", "Friend"]
usernames = ["pawan", "friend"]
passwords = ["1234", "abcd"]

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
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
