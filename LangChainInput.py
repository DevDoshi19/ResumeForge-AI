from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    else:
        api_key = os.getenv("GOOGLE_API_KEY")
except:
    api_key = os.getenv("GOOGLE_API_KEY")

class ChatInputValidation(BaseModel):
    profile_name: str = Field(..., description="The full name of the user.")
    summary: str = Field(..., description="A polished, professional summary (max 3-4 lines).")
    skills: List[str] = Field(..., description="List of top 8-10 technical skills.")
    projects: List[str] = Field(..., description="List of projects, rewritten in 'Action-Metric-Result' format.")
    experience: List[str] = Field(..., description="List of job roles, rewritten professionally with action verbs.")
    education: str = Field(..., description="Formatted educational background.")
    other_information: str = Field(..., description="Formatted additional info (Languages, Hobbies).")
    achievements: List[str] = Field(..., description="List of formatted achievements.")


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.5, api_key=api_key)
Structured_model = model.with_structured_output(ChatInputValidation)

def generate_resume_data(name, summary, skills, projects, exp, edu, other, awards, job_desc):
    
    template = """
    ### ROLE: Expert Resume Writer
    You are rewriting a candidate's messy raw details into a High-Impact, ATS-Friendly Resume.

    ### TARGET JOB DESCRIPTION (CRITICAL):
    "{job_desc}"
    
    *INSTRUCTION:* - If the Job Description is provided above, PRIORITIZE skills and keywords from it. 
    - Rewrite the 'Summary' and 'Projects' to align with this role.
    - If empty, create a strong general technical resume.

    ### RAW CANDIDATE INPUTS:
    - Name: {profile_name}
    - Summary Draft: {summary}
    - Skills: {skills}
    - Projects: {projects}
    - Experience: {experience}
    - Education: {education}
    - Awards: {achievements}
    - Other: {other_information}

    ### WRITING RULES:
    1. **Polishing:** Use strong action verbs (e.g., "Architected", "Deployed", "Reduced").
    2. **Structure:** Ensure the output fits the strict JSON schema provided.
    3. **Professionalism:** Remove informal language.
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["profile_name", "summary", "skills", "projects", "experience", "education", "achievements", "other_information", "job_desc"],
    )

    chain = prompt | Structured_model

    return chain.invoke({
        "profile_name": name,
        "summary": summary,
        "skills": skills,
        "projects": projects,
        "experience": exp,
        "education": edu,
        "achievements": awards,
        "other_information": other,
        "job_desc": job_desc
    })