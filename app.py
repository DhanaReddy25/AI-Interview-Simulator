import streamlit as st
import PyPDF2, docx, os, re
import google.generativeai as genai
from dotenv import load_dotenv


# -----------------------------
# Configure Gemini
# -----------------------------
load_dotenv()
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Unified Helper Function
# -----------------------------
def analyze_resume(resume_text, role, answer=None):
    prompt = f"""
    Candidate Resume: {resume_text}
    Target Role: {role}

    Tasks:
    1. Generate 3 personalized interview questions.
    2. Rate the resume (skills relevance, project quality, interview suitability, structure & formatting, length).
    3. Provide a numeric score (0–100) and feedback (strengths, weaknesses, structure notes, length recommendation).
    {f"4. Evaluate candidate answer: {answer}" if answer else ""}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {e}"

def extract_score(text):
    match = re.search(r'(\d{1,3})/100', text)
    if match:
        return int(match.group(1))
    return None

# -----------------------------
# Streamlit Frontend
# -----------------------------
st.set_page_config(page_title="AI Interview Simulator", layout="wide")
st.title("AI Interview Simulator")

# Initialize session state
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
if "role" not in st.session_state:
    st.session_state.role = ""
if "analysis_output" not in st.session_state:
    st.session_state.analysis_output = ""

# Step 1: Upload Resume
st.header("Upload Resume")
resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf","docx"])
if resume_file:
    if resume_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(resume_file)
        st.session_state.resume_text = " ".join([page.extract_text() for page in reader.pages])
    elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(resume_file)
        st.session_state.resume_text = " ".join([para.text for para in doc.paragraphs])
    st.success("Resume uploaded successfully!")

# Step 2: Enter Role
st.header("Target Role")
st.session_state.role = st.text_input("Enter the role you are applying for:")

# Step 3: Analyze Resume
if st.button("Analyze Resume"):
    if st.session_state.resume_text and st.session_state.role:
        st.session_state.analysis_output = analyze_resume(st.session_state.resume_text, st.session_state.role)
        st.write(st.session_state.analysis_output)

# Step 4: Answer Evaluation
st.header("Type Your Answer")
typed_answer = st.text_area("Enter your interview response here:")
if st.button("Submit Answer"):
    if typed_answer and st.session_state.resume_text and st.session_state.role:
        st.session_state.analysis_output = analyze_resume(st.session_state.resume_text, st.session_state.role, typed_answer)
        st.success("Answer submitted successfully!")
        st.subheader("Feedback")
        st.write(st.session_state.analysis_output)
    else:
        st.warning("Please upload a resume and enter a role first.")

# Step 5: Resume Rating
st.header("Resume Rating")
if st.button("Rate Resume"):
    if st.session_state.resume_text and st.session_state.role:
        st.session_state.analysis_output = analyze_resume(st.session_state.resume_text, st.session_state.role)
        st.write(st.session_state.analysis_output)

        score = extract_score(st.session_state.analysis_output)
        if score is not None:
            st.progress(score / 100)
            st.write(f"Resume Score: {score}/100")
    else:
        st.warning("Please upload a resume and enter a role first.")
