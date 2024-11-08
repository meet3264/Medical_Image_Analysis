# Medical Image Analysis Streamlit Project

This repository contains a collection of medical image analysis applications developed with Streamlit. The project includes models for detecting tumors, fractures, and pneumonia from medical images, aiming to assist in the early diagnosis and treatment of these conditions.

## Project Structure

- `css/`: Contains CSS files for styling the Streamlit web application.
- `Datasets/`: Folder for storing datasets used for model training and testing.
- `Models/`: Directory for storing pre-trained models for medical image analysis.(Download saved Models from Drive link inside this folder.)
- `pages/`: Additional pages for the Streamlit application.
- `Train_Models_Notebookfile/`: Notebooks used for model training and experimentation.
- `Tumor/`: Contains resources and tumor dataset specifically for tumor analysis and classification.

### Key Files

- `Contact.py`: Contact page module for the Streamlit application.
- `contact_us_data.csv`: Dataset for contact information testing or other usage.
- `data.csv`: Store the details of the users.
- `datasets.py`: Helper script for dataset handling operations.
- `Extra_Analysis.py`: For Fracture and Pneumonia Detection
- `fracture.py`: Script for detecting and analyzing fractures in medical images.
- `imagesofdirectory.py`: Script for processing or managing image directories.
- `login.py`: Implements login functionality for application security.
- `Pneumonia.py`: Model for detecting pneumonia from chest X-ray images.
- `Tumor_CNN.py`: Convolutional Neural Network (CNN) model for tumor classification.
- `Tumor_Efficientnet.py`: EfficientNet model for advanced tumor detection.

## Datasets

- **Tumor**: The Tumor dataset can be accessed and downloaded [here](https://drive.google.com/drive/folders/1XrMfQ1eecrTzn1neRp2dgRMLjnOKfQej?usp=sharing).
- **Fracture**: The fracture dataset can be accessed and downloaded [here](https://drive.google.com/drive/folders/1-BXIftfH2ChhtsdAWeqtFMiy9BdpgFcc?usp=drive_link).
- **Pneumonia**: The pneumonia dataset can be accessed and downloaded [here](https://drive.google.com/drive/folders/1-3ipAqlXQAIGvyvP7STqjZtDfHgsilRB?usp=drive_link).

## Getting Started

### Prerequisites

- Python 3.11
- Streamlit
- Additional libraries as listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/meet3264/Medical_Image_Analysis.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Streamlit project
    ```
3. Create a virtual environment:
    ```bash
    python -m venv VE
    ```
4. Activate the virtual environment:
    - **Windows**:
        ```bash
        VE\Scripts\activate
        ```
    - **Linux/MacOS**:
        ```bash
        source VE/bin/activate
        ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Launch Streamlit:
    ```bash
    streamlit run login.py
    ```

### Project Modules

- **Tumor Detection**:
  - `Tumor_CNN.py`: Uses a Convolutional Neural Network to classify tumors.
  - `Tumor_Efficientnet.py`: Employs EfficientNet architecture for more accurate tumor classification.

- **Fracture Detection**: 
  - `fracture.py`: Model for detecting fractures in medical images, useful for diagnosing bone injuries.

- **Pneumonia Detection**: 
  - `Pneumonia.py`: Model for detecting pneumonia from chest X-ray images, assisting in early diagnosis.


