
'''import easyocr
import streamlit as st
from PIL import Image

# Initialize the EasyOCR reader for Hindi and English
reader = easyocr.Reader(['hi', 'en'])

# Streamlit application title
st.title("OCR and Keyword Search Application")
st.write("Upload an image containing Hindi and English text to extract and search within the text.")

# File uploader for image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Text input for keyword search
keyword = st.text_input("Enter Keyword to Search")

if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Perform OCR on the uploaded image
    extracted_text = reader.readtext(uploaded_file, detail=0)

    # Join the extracted text into a single string
    full_text = " ".join(extracted_text)

    # Display the extracted text
    st.subheader("Extracted Text")
    st.write(full_text)

    # Highlight the keyword in the extracted text
    if keyword:
        highlighted_text = full_text.replace(
            keyword, f"<mark>{keyword}</mark>")
        st.subheader("Highlighted Search Results")
        st.markdown(highlighted_text, unsafe_allow_html=True)
    else:
        st.subheader("Highlighted Search Results")
        st.write("No keyword entered for highlighting.")'''
import easyocr
import streamlit as st
from PIL import Image
import numpy as np

# Initialize the EasyOCR reader for Hindi and English
reader = easyocr.Reader(['hi', 'en'])

# Streamlit application title
st.title("OCR and Keyword Search Application")
st.write("Upload an image containing Hindi and English text to extract and search within the text.")

# File uploader for image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Text input for keyword search
keyword = st.text_input("Enter Keyword to Search")

if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert the image to a NumPy array
    image_np = np.array(image)

    # Perform OCR on the uploaded image
    extracted_text = reader.readtext(image_np, detail=0)

    # Join the extracted text into a single string
    full_text = " ".join(extracted_text)

    # Display the extracted text
    st.subheader("Extracted Text")
    st.write(full_text)

    # Highlight the keyword in the extracted text
    if keyword:
        highlighted_text = full_text.replace(
            keyword, f"<mark>{keyword}</mark>")
        st.subheader("Highlighted Search Results")
        st.markdown(highlighted_text, unsafe_allow_html=True)
    else:
        st.subheader("Highlighted Search Results")
        st.write("No keyword entered for highlighting.")
