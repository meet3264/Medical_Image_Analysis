import streamlit as st
import pandas as pd
import re

st.set_page_config(initial_sidebar_state="collapsed", page_title='SignUp', page_icon=':lock_with_ink_pen:')

external_css = open("css/signup.css").read()
st.markdown(f"<style>{external_css}</style>", unsafe_allow_html=True)

st.title("Sign Up page")
Email = st.text_input("Email")
Mobile = st.text_input("Mobile number")
Password = st.text_input("Password", type='password')
Cpassword = st.text_input("Confirm password", type='password')

if st.button("Signup"):
    if Password != Cpassword:
        st.error("Password does not match")
    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', Email):
        st.error("Please enter a valid email")
    elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', Password):
        st.error("Please enter a password atleast 8 character long")
    elif not re.match(r'^[0-9]{10}$', Mobile):
        st.error("Please enter the valid 10-digit mobile number")
    else:
        # Read existing data
        existing_data = pd.read_csv("data.csv", dtype=str) if st.session_state.get('file_created') else pd.DataFrame()

        # Check if the DataFrame is not empty and if the email is already registered
        if not existing_data.empty and Email in existing_data['Email'].values:
            st.error("Email is already registered. Use a different email.")
        else:
            # Append new data to the existing DataFrame
            new_data = {'Email': [Email], 'Mobile': [Mobile], 'Password': [Password]}
            new_user_df = pd.DataFrame(new_data)
            existing_data = pd.concat([existing_data, new_user_df], ignore_index=True)

            # Save the updated data to CSV
            existing_data.to_csv('data.csv', index=False)
            st.session_state.file_created = True

            st.success("Signup Successful")


link = '[Login](http://localhost:8501/login)'
button_html = f'<a href="http://localhost:8501/login" target="_blank" style="padding: 6px 17px;font-size: 17px; background-color: #00BFFF; color: white; text-decoration: none; border-radius: 4px;">Login</a>'

st.markdown(button_html, unsafe_allow_html=True)