
import streamlit as st

# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="ResumeIQ | Dashboard",
    page_icon="📄",
    layout="wide"
)

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>
.stApp {
    background: #F4F7FC;
    color: #1E293B;
}

.block-container {
    max-width: 1250px;
    padding: 2rem 2rem 1rem 2rem;
}

#MainMenu, footer {
    visibility: hidden;
}

.hero {
    background: linear-gradient(120deg, #142F50, #2869A5);
    padding: 30px 34px;
    border-radius: 16px;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 36px;
    margin-bottom: 5px;
}

.hero p {
    color: #DCE9F8;
    font-size: 15px;
}

.eyebrow {
    color: #B9D5F5;
    font-size: 11px;
    letter-spacing: 2px;
    font-weight: bold;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #173B63;
    margin: 25px 0 13px 0;
}

.module-card {
    background: white;
    border: 1px solid #E1E8F0;
    border-radius: 13px;
    padding: 20px;
    min-height: 158px;
    margin-bottom: 12px;
    box-shadow: 0 2px 8px rgba(20,47,80,0.04);
}

.module-card:hover {
    border-color: #75A6D7;
}

.module-icon {
    font-size: 25px;
}

.module-card h4 {
    color: #1D4F80;
    font-size: 16px;
    margin: 12px 0 7px 0;
}

.module-card p {
    color: #64748B;
    font-size: 13px;
    line-height: 1.5;
}

.module-status {
    display: inline-block;
    background: #FFF4D9;
    color: #956300;
    padding: 4px 9px;
    border-radius: 5px;
    font-size: 10px;
    font-weight: 600;
}

.flow-card {
    background: white;
    border: 1px solid #E1E8F0;
    border-radius: 12px;
    padding: 17px 8px;
    text-align: center;
    min-height: 88px;
}

.flow-card strong {
    color: #205B94;
    font-size: 13px;
}

.flow-card small {
    color: #64748B;
    font-size: 11px;
}

.eval-card {
    background: white;
    border: 1px solid #E1E8F0;
    border-radius: 11px;
    padding: 16px;
    min-height: 105px;
}

.eval-card strong {
    color: #205B94;
    font-size: 14px;
}

.eval-card p {
    color: #64748B;
    font-size: 12px;
}

.tech-box {
    background: white;
    border: 1px solid #E1E8F0;
    padding: 17px;
    border-radius: 12px;
    line-height: 2.5;
}

.tech {
    background: #EAF1FA;
    color: #205B94;
    border-radius: 6px;
    padding: 7px 11px;
    margin: 4px;
    font-size: 12px;
    font-weight: 600;
    display: inline-block;
}

.footer {
    text-align: center;
    color: #8290A3;
    font-size: 12px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------
# PROJECT HEADER
# ----------------------------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">RESEARCH PROJECT · VERSION 1.0</div>
    <h1>📄 ResumeIQ</h1>
    <p>
        Cloud-Based Intelligent Resume Compression
        and ATS Optimization System
    </p>
    <p>
        An intelligent framework for resume parsing,
        semantic compression and job-description matching.
    </p>
</div>
""", unsafe_allow_html=True)


# ----------------------------------
# MAIN MODULES
# ----------------------------------

st.markdown(
    '<div class="section-title">Core Modules</div>',
    unsafe_allow_html=True
)

modules = [
    ("📥", "Resume Ingestion",
     "Accepts resume documents in PDF, DOCX and text formats with OCR support."),

    ("🔍", "Resume Parsing",
     "Extracts and normalizes skills, education, experience and other information."),

    ("✂️", "Semantic Compression",
     "Reduces redundant content while preserving important facts and meaning."),

    ("🎯", "ATS Optimization",
     "Aligns resume content with job requirements using lexical and semantic matching."),

    ("📄", "Template Rendering",
     "Generates a structured and ATS-friendly resume.")
]

for start in range(0, 5, 3):
    cols = st.columns(3)

    for col, item in zip(cols, modules[start:start+3]):
        with col:
            st.markdown(f"""
            <div class="module-card">
                <div class="module-icon">{item[0]}</div>
                <h4>{item[1]}</h4>
                <p>{item[2]}</p>
                <span class="module-status">PLANNED MODULE</span>
            </div>
            """, unsafe_allow_html=True)


# ----------------------------------
# SYSTEM WORKFLOW
# ----------------------------------

st.markdown(
    '<div class="section-title">System Workflow</div>',
    unsafe_allow_html=True
)

st.caption("How the proposed application processes a resume")

steps = [
    ("01", "Ingestion"),
    ("02", "Parsing"),
    ("03", "Compression"),
    ("04", "ATS Matching"),
    ("05", "Rendering")
]

cols = st.columns(5)

for col, step in zip(cols, steps):
    with col:
        st.markdown(f"""
        <div class="flow-card">
            <small>{step[0]}</small><br>
            <strong>{step[1]}</strong>
        </div>
        """, unsafe_allow_html=True)


# ----------------------------------
# EVALUATION PARAMETERS
# ----------------------------------

st.markdown(
    '<div class="section-title">Evaluation Parameters</div>',
    unsafe_allow_html=True
)

evaluations = [
    ("Parsing Accuracy",
     "Correct extraction of resume information."),

    ("Keyword Coverage (K)",
     "Measures job-description keyword matching."),

    ("Semantic Score (S)",
     "Measures meaning similarity using embeddings."),

    ("Compression Ratio (CR)",
     "Measures reduction in resume word count.")
]

cols = st.columns(4)

for col, item in zip(cols, evaluations):
    with col:
        st.markdown(f"""
        <div class="eval-card">
            <strong>{item[0]}</strong>
            <p>{item[1]}</p>
        </div>
        """, unsafe_allow_html=True)


# ----------------------------------
# TECHNOLOGY STACK
# ----------------------------------

st.markdown(
    '<div class="section-title">Technology Stack</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="tech-box">
    <span class="tech">Python</span>
    <span class="tech">Streamlit</span>
    <span class="tech">Tesseract OCR</span>
    <span class="tech">spaCy / NER</span>
    <span class="tech">TextRank</span>
    <span class="tech">BART / T5</span>
    <span class="tech">TF-IDF</span>
    <span class="tech">Sentence-BERT</span>
    <span class="tech">Docker</span>
    <span class="tech">Cloud Storage</span>
</div>
""", unsafe_allow_html=True)


# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("""
<div class="footer">
    ResumeIQ · Research Prototype · Experimental Results Pending
</div>
""", unsafe_allow_html=True)
