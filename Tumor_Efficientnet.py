import streamlit as st
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

welcome_html = """
<div>
<h2 style="color:#333;text-align:left;">Tumor Detection Using EfficientnetB3</h2>
</div>
"""

# Create an empty list to store image names and results
image_data = []


# Function to process uploaded images and store their data
def process_uploaded_image(image, probability):
    image_name = image.name
    result = "Tumor" if probability > 0.5 else "Healthy Brain"
    image_data.append({"Image Name": image_name, "Result": result})


def Tumor_Efficientnet():
    st.markdown(welcome_html, unsafe_allow_html=True)
    # Load the trained model
    model_path = 'Models/Tumor_Efficientnet.h5'
    model = tf.keras.models.load_model(model_path, compile=False)

    # st.title("Tumor Detection")
    st.write(
        "EfficientNetB3 is a cnn architecture type of transfer learning model known for its efficiency and effectiveness in image classification tasks.")

    uploaded_file = st.file_uploader("Upload Brain MRI Scan", type=["jpg", "jpeg", "png"])

    # Initialize boolean flag to track if image is uploaded
    image_uploaded = False

    # Check if file is uploaded
    if uploaded_file is not None:
        # Set flag to True
        image_uploaded = True

    # If image is uploaded, show the Predict button
    if image_uploaded:
        if st.button("Predict"):
            # Load and preprocess the image
            img = tf.keras.utils.load_img(uploaded_file, target_size=(256, 256))
            imag = tf.keras.utils.img_to_array(img)
            imaga = np.expand_dims(imag, axis=0)

            ypred = model.predict(imaga)
            probability = ypred[0][0]

            # Classify based on threshold (0.5)
            if probability > 0.5:
                prediction = "Tumor"
            else:
                prediction = "Healthy Brain"

            col1, col2 = st.columns([1, 1])

            with col1:
                st.image(img, caption="Uploaded Image", use_column_width=False, width=300, output_format='JPEG')

            with col2:
                st.markdown(f"<h3>Prediction: {prediction}</h3>", unsafe_allow_html=True)
                st.markdown(f"<h3>Probability: {probability:.2f}</h3>", unsafe_allow_html=True)

            st.write(f"The predictive analysis indicates the sample Brain MRI Scan shows **{prediction}**")
            st.write("Probability Bar Chart:")
            plt.rcParams.update({'font.size': 3})
            fig, ax = plt.subplots(figsize=(3, 1))
            ax.bar(['Healthy Brain', 'Tumor'], [1 - probability, probability], color=['#00BFFF'])
            ax.set_xlabel('Diagnostics', fontsize=4)
            ax.set_ylabel('Probability', fontsize=4)
            st.pyplot(fig)

            process_uploaded_image(uploaded_file, probability)

            st.write("Analysis Result")
            df = pd.DataFrame(image_data)
            st.dataframe(df)

            csv_file = df.to_csv(index=False)
            st.download_button(
                label="Download Report",
                data=csv_file,
                file_name="image_results.csv",
                mime="csv"
            )
