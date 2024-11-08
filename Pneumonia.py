import streamlit as st
import numpy as np
import tensorflow as tf


def Pneumonia():
    # Load the trained model
    model_path = 'Models/pneumonia_model.h5'
    model = tf.keras.models.load_model(model_path, compile=False)

    st.title("Pneumonia Classification")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load and preprocess the image
        img = tf.keras.utils.load_img(uploaded_file, target_size=(224, 224))
        imag = tf.keras.utils.img_to_array(img)
        imaga = np.expand_dims(imag, axis=0)

        ypred = model.predict(imaga)
        probability = ypred[0][0]

        # Classify based on threshold (0.5)
        if probability > 0.5:
            prediction = "Pneumonia Present"
        else:
            prediction = "Pneumonia is not Present"

        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(img, caption="Uploaded Image", use_column_width=False, width=300, output_format='JPEG')
        with col2:
            st.markdown(f"<h3>Prediction: {prediction}</h3>", unsafe_allow_html=True)
            st.markdown(f"<h3>Probability: {probability:.2f}</h3>", unsafe_allow_html=True)
