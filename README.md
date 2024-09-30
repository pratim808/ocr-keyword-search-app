README.md for OCR and Document Search Web Application Prototype
Project Title
OCR and Document Search Web Application Prototype
Introduction
This project is a web-based prototype designed to perform Optical Character Recognition (OCR) on images containing text in both Hindi and English. The application allows users to upload an image, extract the text, and search for specific keywords within the extracted content. The goal is to demonstrate the functionality of OCR technology in a user-friendly web application.
Technologies
The following technologies and libraries were used in this project:
Python: Programming language used for development.
EasyOCR: Library for performing OCR on images.
Streamlit: Framework for building the web application interface.
Pillow: Library for image processing.
Requirements
To run this project, you will need the following libraries installed:
text
easyocr
streamlit
Pillow

You can install these dependencies using pip:
bash
pip install -r requirements.txt

Project Structure
text
/OCR-Document-Search-App
│
├── app.py              # Main application file
├── ocr_utils.py        # Utility functions for OCR processing
└── requirements.txt     # List of required libraries

How to Run the Application Locally
Clone the Repository:
Clone this repository to your local machine using:
bash
git clone <repository-url>

Navigate to the Project Directory:
bash
cd OCR-Document-Search-App

Install Dependencies:
Ensure you have Python installed, then run:
bash
pip install -r requirements.txt

Run the Application:
Start the Streamlit application by executing:
bash
streamlit run app.py

Access the Application:
Open your web browser and go to http://localhost:8501 to access the application.
Features
Image Upload: Users can upload images in JPG, JPEG, or PNG format.
Text Extraction: The application uses EasyOCR to extract text from the uploaded image.
Keyword Search: Users can enter keywords to search within the extracted text, with matching sections highlighted.
Example Usage
Upload an image containing Hindi and English text.
View the extracted text displayed on the page.
Enter a keyword in the search box to find specific content in the extracted text.
Deployment
The application can be deployed on platforms such as Streamlit Sharing or Hugging Face Spaces. Ensure that you follow their respective deployment instructions for making your application accessible via a public URL.
Live URL
[Insert your live URL here once deployed]
Conclusion
This project serves as a demonstration of how OCR technology can be integrated into a web application, providing users with an efficient tool for extracting and searching text from images. The simplicity of the interface aims to enhance user experience while showcasing advanced functionalities.
