import PyPDF2
import spacy
import nltk
import string
import re
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Download NLTK stopwords
nltk.download('stopwords')

# Load spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load('en_core_web_sm')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Function to read PDF and extract text
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to clean text by removing punctuation, stop words, and special symbols
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\b\w{1,2}\b', '', text)  # Remove words with less than 3 characters
    text = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    text = re.sub(r'\S+@\S+', '', text)  # Remove emails
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Remove stop words
    return text

# Function to normalize text by lemmatizing
def normalize_text(text):
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return ' '.join(lemmas)

# Function to process PDF and return cleaned and normalized text
def process_pdf(file_path):
    raw_text = read_pdf(file_path)
    cleaned_text = clean_text(raw_text)
    normalized_text = normalize_text(cleaned_text)
    return normalized_text

# Main script
def main():
    # File paths for the uploaded PDF files
    resume_file_path = 'resume.pdf'  # Update with the correct path to your file
    job_desc_file_path = 'job_description.pdf'  # Update with the correct path to your file

    # Process each file
    resume_text = process_pdf(resume_file_path)
    job_desc_text = process_pdf(job_desc_file_path)

    # Print out the extracted resume and job description texts
    print("Extracted Resume Text:")
    print(resume_text)
    print("\nExtracted Job Description Text:")
    print(job_desc_text)

    # Save the processed text to separate text files
    with open('extracted_resume.txt', 'w') as resume_txt_file:
        resume_txt_file.write(resume_text)

    with open('extracted_job_description.txt', 'w') as job_desc_txt_file:
        job_desc_txt_file.write(job_desc_text)

    print("\nText extraction and file saving completed.")
    print("Extracted resume text saved to 'extracted_resume.txt'.")
    print("Extracted job description text saved to 'extracted_job_description.txt'.")

    # Verify Sentence Transformers model loading and encoding process
    model = SentenceTransformer('all-MiniLM-L6-v2')
    resume_vector = model.encode(resume_text)
    job_desc_vector = model.encode(job_desc_text)

    print("\nEncoded Resume Vector:")
    print(resume_vector)
    print("\nEncoded Job Description Vector:")
    print(job_desc_vector)

    # Compute cosine similarity between the two vectors
    similarity_score = cosine_similarity([resume_vector], [job_desc_vector])[0][0]
    print("\nCosine Similarity between Resume and Job Description Vectors:", similarity_score)

    # Save the data to a file
    data = {
        "resume_text": resume_text,
        "job_desc_text": job_desc_text,
        "resume_vector": resume_vector,
        "job_desc_vector": job_desc_vector
    }

    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

    print("\nData saved to 'data.pkl' file.")

if __name__ == "__main__":
    main()