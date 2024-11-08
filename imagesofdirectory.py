import streamlit as st
import os
import math
from PIL import Image


def display_images_in_directory(directory_path, fixed_size=(200, 200), num_columns=4):
    file_list = os.listdir(directory_path)
    # Filter out only image files (you can add more file extensions if needed)
    image_files = [file for file in file_list if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    # Calculate the number of rows based on the number of images and columns
    num_images = len(image_files)
    st.write(f"Total number of images in the directory: {num_images}")
    num_rows = math.ceil(num_images / num_columns)

    # Display images in rows and columns
    with st.container():
        for i in range(num_rows):
            row_columns = st.columns(num_columns)
            for j in range(num_columns):
                index = i * num_columns + j
                if index < num_images:
                    image_file = image_files[index]
                    image_path = os.path.join(directory_path, image_file)
                    image = Image.open(image_path)

                    # Resize the image to a fixed size
                    image = image.resize(fixed_size)

                    row_columns[j].image(image, caption=image_file, use_column_width=True)


def showimage():
    st.markdown("<h2>Image Visualizer</h2>", unsafe_allow_html=True)
    directory_path = st.text_input("Enter the directory path:")
    num_columns = st.slider("Number of Columns", 1, 8, 4)

    if directory_path and os.path.exists(directory_path):
        display_images_in_directory(directory_path, num_columns=num_columns)
    else:
        st.write("Please enter a valid directory path.")


def imageanalysis():
    st.markdown("<h2>Basic Details of Image</h2>", unsafe_allow_html=True)
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        uploaded_file_path = os.path.abspath(uploaded_image.name)
        image = Image.open(uploaded_image)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=False, width=300, output_format='JPEG')
        with col2:
            st.write(f"Image Path: {uploaded_file_path}")
            st.write(f"Image Size: {image.size}")
            st.write(f"Image Format: {image.format}")
            st.write(f"Image mode: {image.mode}")
