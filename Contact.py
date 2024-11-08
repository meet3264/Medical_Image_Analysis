import streamlit as st
import pandas as pd


def contact():
    st.markdown("<h2>Contact With Us</h2>", unsafe_allow_html=True)

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", height=100)

    if st.button("Submit"):
        if not name:
            st.error("Please enter your name.")
        elif not email:
            st.error("Please enter your email.")
        elif not message:
            st.error("Please enter your message.")
        else:
            # Save the data to a CSV file
            save_to_csv(name, email, message)
            st.success("Your message has been sent successfully!")


def save_to_csv(name, email, message):
    csv_file_path = "contact_us_data.csv"

    contact_data = pd.DataFrame({
        "Name": [name],
        "Email": [email],
        "Message": [message]
    })

    # Append the data to the CSV file or create a new file if it doesn't exist
    contact_data.to_csv(csv_file_path, mode="a", index=False, header=not st.session_state.get("csv_exists", False))

    # Set csv_exists session state to True to avoid creating headers for subsequent submissions
    st.session_state.csv_exists = True
