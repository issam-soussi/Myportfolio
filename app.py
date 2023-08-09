from pathlib import Path
import streamlit as st
from PIL import Image
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Analyste_de données.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
piano_track_path = current_dir / "assets" / "bach_prelude_c_major.mp3"
# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Analyste_de données | Issam Soussi"
PAGE_ICON = ":wave:"
NAME = "Issam Soussi"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "issam.soussi.pro@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/issam-soussi/",
    "GitHub": "https://github.com/issam-soussi",
    "Twitter": "https://twitter.com/issamsoussi3",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

# Function to read the file contents
def read_file():
    with open(piano_track_path, 'rb') as file:
        file_contents = file.read()
    encoded_audio = base64.b64encode(file_contents).decode('utf-8')
    audio_html = f'<audio id="audio-player" controls autoplay><source src="data:audio/mp3;base64,{encoded_audio}" type="audio/mp3"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

# --- Streamlit Configuration ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load CSS, PDF & Profile Pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- Hero Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- Social Links ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Experience & Qualifications ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Versatile Data Analyst with a background in Business Administration.
- ✔️ Experienced in data mining and analysis to provide meaningful insights.
- ✔️ Proficient in statistical techniques, data visualization, and business intelligence tools.
- ✔️ Ability to translate complex data into strategic decisions.
- ✔️ Self-motivated, collaborative team player with strong problem-solving skills and innovative solutions.
- ✔️ Strong hands-on experience and knowledge in Python and Excel.
- ✔️ Fluent in French and English, enabling effective communication across diverse global markets and facilitating seamless collaboration with international teams.
"""
)

# --- Skills ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visualization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

# --- Work History ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- Job 1 ---
st.write("🚧", "**Business data analyst | Solutions Connect IT**")
st.write("2022 - 2023")
st.write(
    """
- ► Analysis of customers' data analysis needs and supplied recommendations to boost landing page conversion rate by 27%.
- ► co-worked with a team of 2 developpers and 2 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 10% more client leads.
- ► Redesigned data model through iterations that improved predictions by 12%.
- ► Development of performance and management indicators (Tableau).
- ► Development of strategic analysis and statistical models to aid in decision-making
- ► Development, automation, and presentation of report results.

"""
)

# --- Job 2 ---
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales efforts by 12%.
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K.
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing.
"""
)

# --- Job 3 ---
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across the company website in collaboration with cross-functional teams to achieve a 120% jump in organic traffic.
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%.
- ► Collaborated with the analyst team to oversee the end-to-end process surrounding customers' return data.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- JavaScript to AutoPlay Audio ---
st.write("<script>document.getElementById('audio-player').play()</script>", unsafe_allow_html=True)
