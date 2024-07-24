import streamlit as st
import pandas as pd
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

# Set the page configuration
st.set_page_config(
    page_title="AI Match Maker",
    page_icon=":mag:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #e0f7fa, #e1bee7);
        }
        .hero-section {
            background-color: #b2ebf2;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .sidebar-section {
            background-color: #f8bbd0;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .uploader-section {
            background-color: #ffe0b2;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .button-section {
            background-color: #c8e6c9;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .result-section {
            background-color: #e1bee7;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .stProgress > div > div > div {
            background-color: #4db6ac;
        }
    </style>
""", unsafe_allow_html=True)

# Hero section
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
st.write("## Welcome to AI Match Maker!")
st.write("Upload your resume and job description to find your perfect match.")
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar with instructions
st.sidebar.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
st.sidebar.write("## Instructions:")
st.sidebar.write("1. Upload your resume and job description in PDF format.")
st.sidebar.write("2. Click the 'Submit' button to see the match percentage.")
st.sidebar.write("3. The match percentage is based on the similarity between the resume and job description.")
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Uploader section
st.markdown('<div class="uploader-section">', unsafe_allow_html=True)
resume_file = st.file_uploader("Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("Job Description (PDF)", type=["pdf"])
st.markdown('</div>', unsafe_allow_html=True)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Submit button section
st.markdown('<div class="button-section">', unsafe_allow_html=True)
if st.button("Submit"):
    # Add a progress bar with a transition
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    
    # Extract text from PDF files
    resume_text = ""
    jd_text = ""
    if resume_file is not None:
        resume_text = extract_text_from_pdf(resume_file)
    if jd_file is not None:
        jd_text = extract_text_from_pdf(jd_file)

    if resume_text and jd_text:
        # Create a TF-IDF vectorizer
        vectorizer = TfidfVectorizer()

        # Fit the vectorizer to the resume and job description text
        vectorizer.fit([resume_text, jd_text])

        # Transform the text into vectors
        resume_vector = vectorizer.transform([resume_text])
        jd_vector = vectorizer.transform([jd_text])

        # Calculate the cosine similarity between the vectors
        similarity = cosine_similarity(resume_vector, jd_vector)[0][0]

        # Display the match percentage
        match_percentage = int(similarity * 100)
        st.markdown('<div class="result-section">', unsafe_allow_html=True)
        st.success(f"Match found! Your match percentage is {match_percentage}%", icon="✨")
        st.markdown('</div>', unsafe_allow_html=True)

        # Add some animations
        st.spinner("Congratulations! You've found a match!")

    else:
        st.error("Please upload both resume and job description PDFs.")
    
    # Set the background color to a gradient
    st.markdown("<style>body { background: linear-gradient(to bottom, #e0f7fa, #e1bee7); }</style>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
