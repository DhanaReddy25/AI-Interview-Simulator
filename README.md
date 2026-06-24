# 🤖 AI Interview Simulator

An AI-powered **interactive interview preparation platform** built with **Streamlit** and **Google Gemini AI** that helps candidates improve their interview readiness through personalized question generation, resume analysis, and AI-driven feedback.

---

## 📌 Overview

**AI Interview Simulator** is designed to simulate a real interview experience by analyzing a candidate's resume, generating role-specific interview questions, evaluating responses, and providing actionable improvement suggestions.

The application combines **Generative AI**, **Natural Language Processing**, and a simple user-friendly interface to create a personalized interview practice environment.

---

## ✨ Key Features

### 📄 Resume Analysis

* Upload your resume in **PDF/DOCX format**
* Automatically extracts resume content
* Analyzes skills, experience, and projects

### 🎯 Personalized Interview Questions

* Generates questions based on:

  * Resume content
  * Target job role
  * Candidate profile
* Includes technical and behavioral interview questions

### 📝 AI Answer Evaluation

* Submit your interview answers
* Receive instant AI-based evaluation:

  * Strengths
  * Weak areas
  * Improvement suggestions
  * Better answer recommendations

### ⭐ Resume Scoring

* Evaluates resume quality against a target role
* Provides:

  * Resume score
  * Missing skills
  * Optimization suggestions

### ⚡ Optimized Gemini Integration

* Uses a unified AI request workflow
* Reduces unnecessary API calls
* Improves efficiency while working with API limits

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/DhanaReddy25/AI-Interview-Simulator.git

cd AI-Interview-Simulator
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key from:

Google AI Studio
https://ai.google.dev

---

## 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🏗️ Project Structure

```
AI-Interview-Simulator/
│
├── app.py              # Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .env                # Environment variables (not committed)
│
└── assets/             # Project resources (optional)
```

---

# 🛠️ Tech Stack

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| Python            | Backend logic                      |
| Streamlit         | Web application interface          |
| Google Gemini AI  | AI-powered analysis and generation |
| NLP               | Resume and answer processing       |
| PyPDF/DOCX Parser | Resume extraction                  |

---

# 🔐 API Usage & Limitations

This project uses the **Google Gemini API**.

### Free Tier Limitations

* Limited requests per day
* API calls may fail after quota exhaustion

Example error:

```
ResourceExhausted: 429
You exceeded your current quota
```

### Solutions

* Wait until quota resets
* Enable billing for increased limits
* Use optimized API calls

The application minimizes API usage through a unified AI processing approach.

---

# ⚙️ Troubleshooting

## 1. ResourceExhausted (429)

**Cause:**
Gemini API quota limit exceeded.

**Solution:**

* Wait for quota reset
* Enable billing
* Reduce API requests

---

## 2. Gemini Returned Empty Response

**Possible Causes:**

* Invalid API key
* API quota exceeded
* Empty resume input

**Fix:**

* Verify `.env` configuration
* Upload a valid resume
* Check API availability

---

## 3. Resume Data Not Available

**Cause:**
Resume text is not stored properly.

**Fix:**

Ensure extracted resume content is saved using Streamlit session state:

```python
st.session_state.resume_text
```

---

# 🎯 Future Improvements

* Voice-based AI interviews
* Real-time interview scoring
* More detailed skill gap analysis
* User authentication
* Interview history dashboard

---

# 💡 Motivation

Many candidates struggle with interview preparation because practice sessions are not personalized.

AI Interview Simulator bridges this gap by providing an interactive AI-based platform that helps candidates practice, analyze mistakes, and continuously improve.

---

# 👩‍💻 Author

**Dhana Laxmi**

Computer Science Engineering Student
Interested in AI, Machine Learning, and Software Development

---

⭐ If you find this project useful, consider giving it a star!
