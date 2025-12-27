# 🚧 UNDER CONSTRUCTION: ResumeForge AI

> **Current Status:** 🛠️ Development in progress. Testing frontend logic and PDF generation flow.

![ResumeForge Banner](https://img.shields.io/badge/Status-Building-orange?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

**ResumeForge AI** is an intelligent document generator that solves the "Blank Page Problem" for job seekers. Instead of worrying about formatting or phrasing, users simply input their raw, messy notes, and the AI architect builds a polished, professional PDF resume in seconds.


## ✨ Key Features

* **🧠 Intelligent Rewriting:** Uses **Google Gemini (via LangChain)** to transform informal text (e.g., "I made a website") into professional "Action-Result" bullet points.
* **📄 PDF Engineering:** Custom **FPDF** class generating pixel-perfect layouts with coordinate-based drawing.
* **🎨 Dynamic Theming:** Switch between **Modern (Blue/Bold)** and **Classic (Clean/Minimal)** designs instantly.
* **🎯 Context Awareness:** Paste a **Target Job Description**, and the AI will tailor your skills and summary to match the role keywords.
* **🛡️ Robust Text Sanitization:** Automatically cleans and transcodes special characters to ensure PDF compatibility.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Interactive UI and State Management |
| **LLM Orchestration** | LangChain | Managing Prompts and Structured Output (JSON) |
| **AI Model** | Google Gemini 2.5 | The logic brain for rewriting content |
| **Document Gen** | FPDF | Low-level library for drawing the PDF canvas |
| **Data Validation** | Pydantic | Enforcing strict schema for AI responses |

---

## 👨‍💻 Developer's Note (Transparency)

This project is a deep dive into **Backend GenAI Engineering**.

While I architected the **LangChain pipelines, Pydantic schemas, and Application Logic** from scratch, I leveraged **Google Gemini** as a coding assistant to help generate the complex coordinate mathematics required for the `FPDF` frontend layout. This allowed me to focus 90% of my energy on the core AI logic and data flow, while treating the frontend code generation as an accelerated "drafting" process.

---

## 🚀 How to Run Locally

Follow these steps to set up the project on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/ResumeForge-AI.git](https://github.com/your-username/ResumeForge-AI.git)
cd ResumeForge-AI

```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Set up Environment Variables

Create a file named `.env` in the root directory and add your Google API key:

```env
GOOGLE_API_KEY="your_actual_api_key_here"

```

### 5. Run the Application

```bash
streamlit run app.py

```

---

## 📂 Project Structure

```text
ResumeForge-AI/
├── app.py                # Main Application (UI + PDF Generation Logic)
├── LangChainInput.py     # Backend Logic (Gemini + Pydantic + Prompt)
├── requirements.txt      # Project Dependencies
├── .env                  # API Keys (Not uploaded to GitHub)
├── .gitignore            # Files to ignore (env, pycache)
├── LICENSE               # MIT License
└── README.md             # Documentation

```

---

## 🤝 Contributing

Since this project is currently "Under Construction," I am primarily looking for feedback on the Resume Parsing logic. Feel free to open an issue if you find a bug!

---
*Built with ❤️ by DEV DOSHI*
