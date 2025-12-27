import streamlit as st
from fpdf import FPDF
from LangChainInput import generate_resume_data

def clean_text(text):
    if not text:
        return ""
    replacements = {
        "\u2013": "-", "\u2014": "-", "\u2018": "'", 
        "\u2019": "'", "\u201c": '"', "\u201d": '"', 
        "\u2022": "*"
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text.encode('latin-1', 'replace').decode('latin-1')

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

class PDF(FPDF):
    def __init__(self, brand_color=(0, 0, 128)):
        super().__init__()
        self.brand_color = brand_color

    def header(self):
        pass

    def add_modern_header(self,name,contact_info):
        name = clean_text(name)
        contact_info = clean_text(contact_info)
        
        # Header Background using Brand Color
        self.set_fill_color(*self.brand_color)
        self.rect(0, 0, 210, 45, 'F') 
        
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', 'B', 26)
        self.set_xy(10, 15)
        self.cell(0, 10, name.upper(), 0, 1, 'C')
        
        self.set_font('Arial', '', 10)
        self.set_xy(10, 28)
        self.cell(0, 5, contact_info, 0, 1, 'C')
        
        self.ln(25)

    def add_classic_header(self, name, contact_info):
        name = clean_text(name)
        contact_info = clean_text(contact_info)
        self.set_text_color(*self.brand_color)
        self.set_font('Arial', 'B', 22)
        self.cell(0, 10, name.upper(), 0, 1, 'C')
        self.set_text_color(80, 80, 80)
        self.set_font('Arial', '', 10)
        self.cell(0, 5, contact_info, 0, 1, 'C')
        self.set_draw_color(*self.brand_color)
        self.set_line_width(0.5)
        self.line(10, 32, 200, 32) 
        self.ln(15)

    def section_title(self, title):
        title = clean_text(title)
        self.set_font('Arial', 'B', 13)
        self.set_text_color(*self.brand_color)
        self.cell(0, 10, title.upper(), 0, 1, 'L')
        
        curr_y = self.get_y() - 2 
        self.set_draw_color(*self.brand_color)
        self.set_line_width(0.3)  
        self.line(10, curr_y, 200, curr_y) 
        self.set_line_width(0.2)  
        self.ln(3)

    def section_body(self, text):
        text = clean_text(text)
        self.set_text_color(40, 40, 40)
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 5, text)
        self.ln(3)

    def bullet_points(self, items):
        self.set_font('Arial', '', 10)
        self.set_text_color(40, 40, 40)
        for item in items:
            item = clean_text(item)
            self.cell(8)
            self.cell(3, 5, chr(127), 0, 0) 
            self.multi_cell(0, 5, item)
        self.ln(3)

st.set_page_config(page_title="ResumeForge AI", page_icon="📄", layout="wide")

with st.sidebar:
    st.header("🎨 Resume Styling")
    template_choice = st.radio("Template Style", ["Modern (Bold Header)", "Classic (Minimal)"])
    theme_color = st.color_picker("Brand Accent Color", "#1A237E")
    rgb_color = hex_to_rgb(theme_color)
    
    st.divider()
    st.markdown("### 💡 Tips")
    st.caption("Use a professional color like Deep Blue, Charcoal, or Dark Green.")

st.title("📄 ResumeForge AI")
st.subheader("Professional Resume Engineering")

# Layout for the main form
with st.form("resume_form"):
    st.markdown("#### 👤 Personal Information")
    c1, c2, c3 = st.columns(3)
    with c1:
        profile_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
    with c2:
        phone = st.text_input("Phone Number")
        github = st.text_input("LinkedIn/Portfolio URL")
    with c3:
        education = st.text_area("Education Details", placeholder="B.Tech CS, XYZ University (2024)")

    st.divider()
    st.markdown("#### 🎯 Targeted Optimization")
    job_desc = st.text_area("Paste Target Job Description", placeholder="AI will optimize your keywords for this specific role...")

    st.divider()
    st.markdown("#### 📝 Professional Content")
    col_a, col_b = st.columns(2)
    with col_a:
        summary = st.text_area("About Me (Raw Draft)")
        skills = st.text_area("Technical Skills")
        experience = st.text_area("Experience/Internships")
    with col_b:
        projects = st.text_area("Key Projects")
        achievements = st.text_area("Awards & Achievements")
        other_info = st.text_area("Additional Info")

    submitted = st.form_submit_button("🔨 Build Professional Resume")

if submitted:
    if not profile_name or not skills:
        st.warning("Please enter your name and skills to proceed.")
    else:
        with st.spinner("🤖 AI Architect is designing your resume..."):
            try:
                ai_data = generate_resume_data(
                    profile_name, summary, skills, projects, 
                    experience, education, other_info, achievements, job_desc
                )
                
                # Initialize PDF with chosen color
                pdf = PDF(brand_color=rgb_color)
                pdf.add_page()
                
                contact_info = f"{email}  |  {phone}  |  {github}"

                if template_choice == "Modern (Bold Header)":
                    pdf.add_modern_header(ai_data.profile_name, contact_info)
                else:
                    pdf.add_classic_header(ai_data.profile_name, contact_info)

                sections = [
                    ("About Me", ai_data.summary, "text"),          # Renamed from Professional Summary
                    ("Technical Skills", ", ".join(ai_data.skills), "text"), # Renamed from Core Technical Skills
                    ("Work Experience", ai_data.experience, "bullets"),
                    ("Key Projects", ai_data.projects, "bullets"),
                    ("Education", ai_data.education, "text")
                ]

                for title, content, style in sections:
                    pdf.section_title(title)
                    if style == "text":
                        pdf.section_body(content)
                    else:
                        pdf.bullet_points(content)

                if ai_data.achievements:
                    pdf.section_title("Honors & Awards")
                    pdf.bullet_points(ai_data.achievements)
                
                if ai_data.other_information:
                    pdf.section_title("Additional Details")
                    pdf.section_body(ai_data.other_information)

                pdf_bytes = pdf.output(dest='S').encode('latin-1')
                
                st.balloons()
                st.success("✨ Your professional resume is ready!")
                st.download_button(
                    label="📥 Download PDF Resume",
                    data=pdf_bytes,
                    file_name=f"{profile_name}_Resume.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"Error during generation: {e}")