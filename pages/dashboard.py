import streamlit as st
from Tumor_CNN import Tumor_CNN
from Tumor_Efficientnet import Tumor_Efficientnet
from streamlit_option_menu import option_menu
from Extra_Analysis import extra_analysis
from imagesofdirectory import showimage, imageanalysis
from Contact import contact
from PIL import Image

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Dashboard",
    page_icon=':chart_with_upwards_trend:'
)

with st.sidebar:
    choose = option_menu("App Gallery",
                         ["About", "Predict Tumor Using CNN", "Predict Tumor Using EfficientNetB3", "Model Comparison",
                          "Details of Image", "Image Visualizer", "Extra Analysis", "Contact Us", "Logout"],
                         icons=['house', 'activity ', 'activity', 'graph-up', 'camera', 'image', 'kanban', 'people',
                                'person-lines-fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "#FFDAB9"},
                             "icon": {"color": "#00BFFF", "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                          "--hover-color": "#eee"},
                             "nav-link-selected": {"background-color": "#02ab21"},
                         }
                         )

welcome_html = """
<div style="background-color:#FFDAB9;opacity:0.9;padding:8px;border-radius:10px">
<h2 style="color:#333;text-align:center;">AI BASED IMAGE ANALYZER</h2>
</div>
"""

external_css = open("css/dashboard.css").read()
st.markdown(f"<style>{external_css}</style>", unsafe_allow_html=True)


def about():
    st.markdown(welcome_html, unsafe_allow_html=True)
    # st.title("AI BASED IMAGE ANALYZER")
    st.write("")
    st.write("""
       AI Based Image Analyzer is strategically designed to address in healthcare diagnostics.In the healthcare,project focuses on MRI scans for checking **Presence of Brain Tumor** using the methods of AI and image analysis.By using MRI images we can identify tumor is present in image or not.Here we used a Deep Learning architectures CNN and EfficientNetB3 Transfer learning for detect the brain tumor.

       ### Objectives:

        1.  To provide good application software to identify tumor is present or not in the image.
        2.  Save patient’s and doctor’s time.
        3.  Provide a solution appropriately with good accuracy.
        4.  Provide easy interface and user-friendly application.

       ### Methodology:

       1. **Image Acquisition:**: Medical imaging techniques such as MRI (Magnetic Resonance Imaging) scans are used to acquire images of the brain.

       2. **Preprocessing & Feature Extraction**: The acquired images may undergo preprocessing steps such as noise reduction, image enhancement, normalization and many more to improve the quality and consistency of the data.Relevant features are extracted from the preprocessed images. 

       3. **Model Training**: Machine learning or deep learning models are trained using labeled datasets. The labeled data consists of images annotated with binary labels indicating the presence or absence of tumors.

       4. **Model Evaluation**: The trained model is evaluated using validation datasets to assess its performance in detecting brain tumors. Evaluation metrics such as accuracy, precision, recall, and F1-score are commonly used.
    
       """)


def comparison():
    st.markdown("<h2>Model Comparison</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    image1 = Image.open("Datasets/Tumor_cnn_accuracy.png")
    image2 = Image.open("Datasets/Tumor_efficientnet_accuracy.png")
    image3 = Image.open("Datasets/Tumor_cnn_loss.png")
    image4 = Image.open("Datasets/Tumor_efficientnet_loss.png")
    # Display the uploaded image in the first column
    with col1:
        st.markdown("<h4 style=text-align:center>CNN Model</h4>", unsafe_allow_html=True)
        st.image(image1, caption="CNN Model Accuracy", use_column_width=True, output_format='JPEG')
        st.image(image3, caption="CNN Model Loss", use_column_width=True, output_format='JPEG')

    # Display the prediction in the second column
    with col2:
        st.markdown("<h4 style=text-align:center>EfficientNet Model</h4>", unsafe_allow_html=True)
        st.image(image2, caption="EfficientNet Model Accuracy", use_column_width=True, output_format='JPEG')
        st.image(image4, caption="EfficientNet Model Loss", use_column_width=True, output_format='JPEG')


def logout():
    st.markdown('<meta http-equiv="refresh" content="2;url=http://localhost:8501/login">', unsafe_allow_html=True)


if choose == "About":
    about()
elif choose == "Predict Tumor Using CNN":
    Tumor_CNN()
elif choose == "Predict Tumor Using EfficientNetB3":
    Tumor_Efficientnet()
elif choose == "Model Comparison":
    comparison()
elif choose == "Details of Image":
    imageanalysis()
elif choose == "Image Visualizer":
    showimage()
elif choose == "Extra Analysis":
    extra_analysis()
elif choose == "Contact Us":
    contact()
elif choose == "Logout":
    logout()
