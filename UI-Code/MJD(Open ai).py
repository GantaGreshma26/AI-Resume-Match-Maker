import streamlit as st
import fitz  # PyMuPDF
import openai
import base64

# Set up your OpenAI API key
openai.api_key = 'PUT YPUR OPENAI KEY'

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
        f"Match Percentage"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

# Define 20 job roles
job_roles = [
    "Software Engineer",
    "Data Scientist",
    "Product Manager",
    "Marketing Manager",
    "Sales Representative",
    "Customer Support Specialist",
    "IT Project Manager",
    "UX Designer",
    "DevOps Engineer",
    "Cybersecurity Specialist",
    "Business Analyst",
    "Financial Analyst",
    "Human Resources Manager",
    "Operations Manager",
    "Supply Chain Manager",
    "Logistics Coordinator",
    "Digital Marketing Specialist",
    "Content Writer",
    "Graphic Designer",
    "Web Developer"
]

# Set up Streamlit layout
st.set_page_config(
    page_title="Resume Matcher",
    page_icon=":briefcase:",
    layout="wide"
)


# Set up background color with transparent rainbow


def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image
set_background("background.jpg")





# Set up sidebar
st.sidebar.header("Instructions")
st.sidebar.write("1. Upload your resume in PDF format")
st.sidebar.write("2. Click the 'Submit' button to get the top 5 matching job descriptions")
st.sidebar.write("3. Explore your potential matches")

# Set up main content
st.title("AI Resume Match Maker")
st.write("")
# Create two columns, one with a fixed width and the other with a flexible width
col1, col2 = st.columns([2, 2])  # adjust the column widths to your desired values

# Add the file uploader to the fixed-width column
with col1:
    resume_file = st.file_uploader("Upload your resume", type=["pdf"], label_visibility="hidden")

submit_button = st.button("Submit")

if submit_button:
    if resume_file:
        resume = read_pdf(resume_file)
        results = []
        for job_role in job_roles:
            job_description = f"This is a job description for a {job_role}."
            result = match_resume_to_job(resume, job_description)
            match_range = result.split("%")[0].strip().split()[-1]
            if "-" in match_range:
                match_values = [int(x) for x in match_range.split("-")]
                match_percentage = sum(match_values) / len(match_values)  # Calculate the average of the range
            else:
                match_percentage = int(match_range)
            results.append((job_role,round(match_percentage)))

        results = [(job_role, match_percentage) for job_role, match_percentage in results if match_percentage >= 50]

        if not results:
            st.write("No matches")
        else:
            st.write("Top 5 JD's matching with your resume:")
            for job_role, match_percentage in sorted(results, key=lambda x: x[1], reverse=True)[:5]:
                st.write(f"{job_role} - {match_percentage:.2f}%")
    else:
        st.write("Please upload your resume")