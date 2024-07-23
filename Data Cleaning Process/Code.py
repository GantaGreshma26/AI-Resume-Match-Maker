# Install the required libraries
!pip install PyPDF2
!pip install nltk

# Import the required modules
import pandas as pd
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download the NLTK stopwords and wordnet corpora
nltk.download('stopwords')
nltk.download('wordnet')

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    pdf_file = open(file_path, 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file)  # Use PdfReader instead of PdfFileReader
    number_of_pages = len(read_pdf.pages)  # Corrected line
    text = ''
    for page_number in range(number_of_pages):
        page = read_pdf.pages[page_number]  # Use pages attribute instead of getPage()
        page_content = page.extract_text()
        text += page_content
    return text

# Function to clean the text data
def clean_text_data(text):
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

# Load the resume and document files
resume_file_path = 'resume.pdf'
document_file_path = 'document.pdf'

# Extract text from the files
resume_text = extract_text_from_pdf(resume_file_path)
document_text = extract_text_from_pdf(document_file_path)
print("Extracted resume text:")
print(resume_text)
print("Extracted document text:")
print(document_text)

# Clean the text data
resume_text = clean_text_data(resume_text)
document_text = clean_text_data(document_text)
print(resume_text)
print(document_text)

# Create a dictionary to store the data
data = {'Resume': [resume_text], 'Document': [document_text]}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('output.csv', index=False)

# Load the CSV file
df = pd.read_csv('output.csv')

# Explicitly convert 'Document' column to string before applying lower()
df['Document'] = df['Document'].astype(str)  # Convert to string type

# Apply cleaning techniques to the data
df['Resume'] = df['Resume'].apply(lambda x: x.lower())
df['Document'] = df['Document'].apply(lambda x: x.lower())

# Print the cleaned data
print(df)