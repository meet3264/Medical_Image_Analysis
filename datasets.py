import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def reader():
    st.title(" BASIC DATA ANALYSIS")
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "csv"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)

        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)

        st.write("Data from uploaded file: ")
        st.dataframe(df.head())
        st.subheader("COLUMN NAMES:")
        st.write(df.columns)
        st.subheader("Check Null values in columns: ")
        st.write(df.isnull().sum())
        st.subheader("ROWS AND COLUMNS:")
        st.write(f"Rows  ->: {df.shape[0]}")
        st.write(f"Columns  ->: {df.shape[1]}")
        st.subheader("SUMMARY STATISTICS: ")
        st.write(df.describe())
        st.subheader("Check Columns have null values or not (TRUE/FALSE)")
        st.write(df.isnull().any())


def hoteldata():
    st.title("Hotel Data Analysis")
    st.subheader("Top 10 Hotel Reviews")
    df = pd.read_csv("Datasets/hotel.csv")
    hotel_counts = df['name'].value_counts()
    top_10_hotels = pd.DataFrame(hotel_counts.head(10)).rename_axis("Name")
    top_10_hotels.columns = ["Counts"]
    st.write(top_10_hotels)
    st.bar_chart(top_10_hotels)

    st.subheader("All Hotels Rating")
    rating_count = df["reviews.rating"].value_counts()
    rating_count = pd.DataFrame(rating_count)
    st.write(rating_count)

    st.title("Distribution of Rating")
    allratings = df["reviews.rating"].value_counts().reset_index()
    st.bar_chart(allratings)

    hotel_name = st.text_input("Enter the hotel name: ")
    hotel_data = df[df['name'] == hotel_name]

    if not hotel_data.empty:
        review_counts = hotel_data["reviews.rating"].value_counts().sort_index()
        st.write(f"Review counts for {hotel_name}:")
        st.write(review_counts)
    else:
        st.write("Hotel not found")


def zomato():
    st.title("ZOMATO DATA-ANALYSIS")

    st.subheader("Database")
    df = pd.read_csv("Datasets/zomato.csv", encoding='latin1')
    df1 = pd.read_excel("Datasets/Country-Code.xlsx")
    st.write(df)
    df.dropna(axis=0, inplace=True)
    st.write("_" * 100)

    st.subheader("Column Names :-")
    st.write(df.columns)
    final_df = pd.merge(df, df1, how="inner", on="Country Code")
    st.write()
    st.write("_" * 100)

    st.subheader("Number of Rows and Number of Columns:-")
    st.write("_" * 100)
    st.subheader("Rows:-")
    st.subheader(final_df.shape[0])
    st.write("_" * 100)
    st.subheader("Columns:-")
    st.subheader(final_df.shape[1])
    st.write("_" * 100)
    st.subheader("Checking Null values in Columns:-")
    st.write(final_df.isnull().sum())
    st.write("_" * 100)

    f, ax = plt.subplots(1, 1, figsize=(10, 10))
    st.subheader("Identify the Country with the Highest usage of Zomato:-")
    country_name = final_df["Country"].value_counts().index
    country_num = final_df["Country"].value_counts().values
    plt.pie(country_num[:3], labels=country_name[:3], autopct="%1.2f%%", shadow=True, explode=(0.2, 0.0, 0.0),
            colors=['pink', 'skyblue', 'red'])
    st.pyplot(f)
    st.write("_" * 100)
    st.write("Country Names:-")
    st.write(country_name)

    # rating
    st.write("_" * 100)
    st.subheader("Rating Analysis:-")
    rating = final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(
        columns={0: 'Rating Count'})
    st.write(rating)
    fig, ax = plt.subplots(2, 1, figsize=(10, 10))
    sns.barplot(x="Aggregate rating", y="Rating Count", data=rating, hue='Rating color', ax=ax[0])
    sns.countplot(x="Rating color", data=rating, ax=ax[1], color='skyblue')
    st.pyplot(fig)
    st.write("_" * 100)

    st.subheader("Names of those Countries that have not been rated")
    st.write(final_df[final_df['Rating color'] == 'white'].groupby('Country').size().reset_index())
