import openai
import fitz  # PyMuPDF

# Set up your OpenAI API key
openai.api_key = 'PUT YOUR OPENAI KEY'


def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def match_resume_to_job(resume, job_description):
    prompt = (
        f"Evaluate how well the following resume matches the job description. "
        f"Provide a match percentage and a brief explanation.\n\n"
        f"Resume:\n{resume}\n\n"
        f"Job Description:\n{job_description}\n\n"
        f"Match Percentage and Explanation:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# File paths for resume and job description PDFs
resume_file_path = r'C:\Users\ganta.greshma\Desktop\AI RESUME Matchmaker\open ai\Resume_Prasad.pdf'
job_description_file_path = r'C:\Users\ganta.greshma\Desktop\AI RESUME Matchmaker\open ai\Job-desc-sample.pdf'

# Read resume and job description from PDF files
resume = read_pdf(resume_file_path)
job_description = read_pdf(job_description_file_path)

# Get the match percentage and explanation
result = match_resume_to_job(resume, job_description)
print(result)
