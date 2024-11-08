import streamlit as st
import pandas as pd

st.set_page_config(initial_sidebar_state="collapsed", page_title='Login', page_icon=':closed_lock_with_key:')
st.title('Login Page')


external_css = open("css/login.css").read()
st.markdown(f"<style>{external_css}</style>", unsafe_allow_html=True)

# Initialize session state
if 'email' not in st.session_state:
    st.session_state.email = None


# Read the CSV file
try:
    df = pd.read_csv("data.csv")
except pd.errors.EmptyDataError:
    st.warning("No user data found. Redirecting to the registration page.")
    st.markdown('<meta http-equiv="refresh" content="2;url=http://localhost:8501/signup">', unsafe_allow_html=True)
    st.header("Redirecting")
    st.stop()

# Create a DataFrame from the CSV data
data = pd.DataFrame(df)

# Get the user input
email = st.text_input("Enter Email").strip()
password = st.text_input("Enter Password", type="password").strip()

# Check if the login button is clicked
login_button_clicked = st.button("Login")

# Check if email and password are provided
if email and password and login_button_clicked:
    # Convert 'Email' and 'Password' columns to strings
    data['Email'] = data['Email'].astype(str)
    data['Password'] = data['Password'].astype(str)

    # Check if email and password match
    user_data = data[(data['Email'].str.strip() == email) & (data['Password'].str.strip() == password)]
    if not user_data.empty:
        st.success("Login Successful")
        st.markdown('<meta http-equiv="refresh" content="2;url=http://localhost:8501/dashboard">', unsafe_allow_html=True)
    else:
        st.error("Invalid email or password")
elif login_button_clicked:
    st.warning("Enter email and password ")

link = '[Register](http://localhost:8501/signup)'
button_html = f'<a href="http://localhost:8501/signup" target="_blank" style="padding: 8px 10px; background-color: #00BFFF; color: white; text-decoration: none; border-radius: 4px;">Register</a>'

st.markdown(button_html, unsafe_allow_html=True)