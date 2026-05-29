import streamlit as st
import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF
import PyPDF2
import docx
import google.generativeai as genai

# -----------------------------
# Configure Gemini
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------
# Helper Functions
# -----------------------------
def generate_questions(resume_text):
    prompt = f"Generate 3 personalized interview questions based on this resume:\n{resume_text}"
    response = model.generate_content(prompt)
    return response.text

def transcribe_audio(audio_bytes):
    prompt = "Transcribe this audio interview answer:"
    response = model.generate_content([
        {"role": "user", "parts": [{"text": prompt}, {"inline_data": {"mime_type": "audio/wav", "data": audio_bytes}}]}
    ])
    return response.text

# -----------------------------
# Streamlit App
# -----------------------------
st.title("AI Interview Simulator")

# Phase 1: Resume Upload
resume_file = st.file_uploader("📂 Upload Resume (PDF/DOCX)", type=["pdf","docx"])
resume_text = ""
if resume_file:
    if resume_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(resume_file)
        resume_text = " ".join([page.extract_text() for page in reader.pages])
    elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(resume_file)
        resume_text = " ".join([para.text for para in doc.paragraphs])
    st.success("Resume uploaded and parsed successfully!")

    st.subheader("📌 Personalized Interview Questions")
    questions = generate_questions(resume_text)
    st.write(questions)
# Phase 2: Direct Text Answer
st.subheader("📝 Type Your Answer")
typed_answer = st.text_area("Enter your interview response here:")

if typed_answer:
    st.success("Answer submitted successfully!")
    transcript = typed_answer  # Treat typed input as transcript

    # Metrics
    metrics = {
        "Word Count": len(transcript.split()),
        "Filler Words": transcript.lower().count("um"),
        "Words per Minute": 135  # Placeholder for consistency
    }

    st.subheader("📊 Voice/Text Metrics")
    for k,v in metrics.items():
        st.write(f"- {k}: {v}")

    st.subheader("💡 Feedback")
    st.write("Clear explanation, but reduce filler words. Confidence is good.")


# Phase 3: Readiness Score
readiness_score = 78
st.subheader("📈 Readiness Dashboard")
fig, ax = plt.subplots()
ax.barh(["Readiness"], [readiness_score], color="skyblue")
ax.set_xlim(0,100)
st.pyplot(fig)

# Phase 4: Multi-Session Tracking
st.subheader("📊 Multi-Session Progress")
sessions = ["Session 1","Session 2","Session 3","Session 4","Session 5"]
scores = [55,62,70,78,85]
fig2, ax2 = plt.subplots()
ax2.plot(sessions, scores, marker="o", color="green")
ax2.set_ylim(0,100)
ax2.set_title("Readiness Progress Over Sessions")
st.pyplot(fig2)

# Phase 5: Benchmarking
st.subheader("📊 Peer Benchmarking")
labels = ["Candidate","Peer Avg","Top 10%"]
bench_scores = [78,72,90]
fig3, ax3 = plt.subplots()
ax3.bar(labels, bench_scores, color=["blue","gray","green"])
ax3.set_ylim(0,100)
st.pyplot(fig3)

# Phase 6: PDF Report
if st.button("📄 Generate PDF Report"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Interview Report", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Transcript: {transcript}")
    for k,v in metrics.items():
        pdf.cell(200, 10, f"{k}: {v}", ln=True)
    pdf.cell(200, 10, f"Readiness Score: {readiness_score}", ln=True)
    pdf.output("Interview_Report.pdf")
    with open("Interview_Report.pdf","rb") as f:
        st.download_button("⬇️ Download Report", f, file_name="Interview_Report.pdf")

# Phase 7: Integration Placeholder
st.subheader("📤 Integration & Sharing")
st.write("Future: Email/LinkedIn integration to share reports.")
