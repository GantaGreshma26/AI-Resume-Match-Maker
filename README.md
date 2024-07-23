# AI Resume Match Maker

The AI Resume Match Maker project aims to revolutionize the job recruitment process by leveraging artificial intelligence to match candidates' resumes with job descriptions accurately. The system automates screening, reduces human bias, and enhances hiring efficiency by identifying the most suitable candidates quickly.

## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Significance](#significance)
- [Project Scope](#project-scope)
- [Technical Stack](#technical-stack)
- [Architecture](#architecture)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [User Guide](#user-guide)
- [Conclusion](#conclusion)

## Introduction

The AI Resume Match Maker project aims to transform job recruitment by using AI to match resumes with job descriptions. This system automates screening, reduces bias, and boosts hiring efficiency.

## Objectives

1. **Automated Resume Screening**: Develop an AI system to screen resumes and match them with job descriptions.
2. **Bias Reduction**: Implement algorithms to minimize human bias.
3. **Efficiency Enhancement**: Streamline the recruitment process to save time.
4. **Accuracy Improvement**: Enhance resume-job matching accuracy.
5. **User-Friendly Interface**: Create an intuitive interface for recruiters.

## Significance

1. **Time and Cost Savings**: Reduce manual resume screening time.
2. **Improved Hiring Quality**: Ensure better hiring decisions.
3. **Enhanced Diversity and Inclusion**: Promote a diverse workforce.
4. **Scalability**: Handle large volumes of resumes.
5. **Competitive Advantage**: Gain an edge in the talent market.

## Project Scope

### Included

1. Automated Resume Screening
2. User Interface
3. Bias Reduction Mechanisms
4. Matching Accuracy
5. Reporting and Analytics

### Excluded

1. End-to-End Recruitment
2. Third-Party Integrations
3. Manual Screening
4. Candidate Feedback

## Technical Stack

- **Programming Languages**: Python
- **Frameworks/Libraries**: Streamlit, Scikit-learn, PyMuPDF, SentenceTransformer, Spacy, NLTK, OpenAI API, Qdrant
- **Databases**: Qdrant
- **Tools/Platforms**: Docker, Git, GitHub

## Architecture

### System Architecture

- **Frontend**: Streamlit for the user interface.
- **Backend**: Flask application for handling requests and integrating AI models.
- **Database**: Qdrant for vector storage.

## Development

### Technologies and Frameworks Used

- **Programming Languages**: Python
- **Libraries/Frameworks**: PyPDF2, spaCy, NLTK, Streamlit, OpenAI API

### Coding Standards and Best Practices

- **Clean Code**: Followed Python's PEP 8 style guide.
- **Modular Design**: Encapsulated functionality into separate functions.
- **Error Handling**: Implemented error handling mechanisms.
- **Version Control**: Utilized Git for managing code changes.

## Testing

- **Unit Tests**: Validate text extraction, cleaning, and normalization functions.
- **Integration Tests**: Verify the entire workflow and error handling.
- **System Tests**: Focus on performance and scalability.

## Deployment

### Deployment Instructions

1. **Local Deployment**:
   - Clone the GitHub repository.
   - Install dependencies using `pip install -r requirements.txt`.
   - Set up environment variables.
   - Run the application using Streamlit: `streamlit run app.py`.

2. **Cloud Deployment (e.g., Heroku)**:
   - Create a Heroku account and install the Heroku CLI.
   - Initialize a new Heroku app and connect it to your GitHub repository.
   - Configure environment variables.
   - Deploy the application to Heroku.

3. **Containerized Deployment (Docker)**:
   - Build the Docker image: `docker build -t ai-resume-matchmaker .`
   - Run the Docker container: `docker run -p 8501:8501 ai-resume-matchmaker`
   - Configure environment variables.

## User Guide

### Setup and Configuration

1. **Environment Preparation**:
   - Ensure Python is installed.
   - Install Streamlit and other required libraries.

2. **Running the Application**:
   - Open a terminal and navigate to the project directory.
   - Activate the virtual environment.
   - Run the application: `streamlit run resume_matchmaker.py`.

3. **Uploading Files**:
   - Open your browser and navigate to the Streamlit app.
   - Upload your resume in PDF format.

4. **Viewing Results**:
   - The application processes the document and compares it with job descriptions.
   - Matching results will be displayed on the screen.

## Conclusion

### Project Outcomes

1. Developed a functional web application using Streamlit.
2. Successfully integrated AI/ML models for resume-job matching.
3. Implemented basic user authentication.
4. Deployed the application to a cloud platform.

### Achievements

1. Leveraged Streamlit for a responsive web application.
2. Delivered a simple and intuitive user interface.
3. Optimized backend processes for performance.


For more details, refer to the full project documentation.
