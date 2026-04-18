import streamlit as st

# --- Simple credentials ---
USER_DB = {
    "pawan": "1234",
    "friend": "abcd"
}

# --- Session state init ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

# --- Login UI ---
def login_ui():
    st.title("Login 🔐")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_DB and USER_DB[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")

# --- App UI ---
def app_ui():
    st.title("Power BI Assistant 🤖")
    st.write(f"Welcome {st.session_state.username}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

    query = st.text_input("Ask your question:")

    if query:
        st.write("You asked:", query)
        st.write("Answer: Coming soon...")

# --- Main ---
if not st.session_state.logged_in:
    login_ui()
else:
    app_ui()
