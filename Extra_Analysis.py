import streamlit as st
from datasets import reader, hoteldata, zomato
from attrition import attrition
from Pneumonia import Pneumonia
from Customer_Segmentation import customer, region, product
from fracture import fracture


def database():
    selected_option1 = st.selectbox(
        "Select a DataBase:",
        ["Select a DataBase", "Hotel Data", "Zomato Data"]
    )
    if selected_option1 == "Hotel Data":
        hoteldata()
    elif selected_option1 == "Zomato Data":
        zomato()
    elif selected_option1 == "Select a DataBase":
        st.warning("Please select a DataBase from dropdown menu.")


def customer_segmentation():
    selected_option1 = st.selectbox(
        "Select Visualization Option:",
        ["Select Visualization Option", "Customer Wise Data Analysis", "Region Wise Data Analysis",
         "Product Wise Data Analysis"]
    )
    if selected_option1 == "Customer Wise Data Analysis":
        customer()
    elif selected_option1 == "Region Wise Data Analysis":
        region()
    elif selected_option1 == "Product Wise Data Analysis":
        product()
    elif selected_option1 == "Select a DataBase":
        st.warning("Please select a DataBase from dropdown menu.")


def extra_analysis():
    selected_option = st.selectbox(
        "Select an option:",
        # ["Select an option", "Basic Data Analysis", "DataBase", "Attrition", "Fracture", "Pneumonia",
        #  "Customer Segmentation"]
        ["Select an option", "Fracture", "Pneumonia",]
    )

    # if selected_option == "Basic Data Analysis":
    #     reader()
    # elif selected_option == "DataBase":
    #     database()
    # elif selected_option == "Attrition":
    #     attrition()
    if selected_option == "Fracture":
        fracture()
    elif selected_option == "Pneumonia":
        Pneumonia()
    # elif selected_option == "Customer Segmentation":
    #     customer_segmentation()
    elif selected_option == "Select an option":
        st.write("Please select an option from dropdown menu.")
