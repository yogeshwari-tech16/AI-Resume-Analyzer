import streamlit as st
from resume_parser import extract_text
from skill_matcher import load_skills, extract_skills

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract text from resume
    resume_text = extract_text(uploaded_file)

    # Load skills from skills.csv
    skills = load_skills()

    # Detect skills from resume
    detected_skills = extract_skills(
        resume_text,
        skills
    )

    st.subheader("Detected Skills")

    for skill in detected_skills:
        st.write("✅", skill)

    # Job Description Analysis
    if job_description:

        job_skills = extract_skills(
            job_description,
            skills
        )

        common_skills = set(
            detected_skills
        ).intersection(
            set(job_skills)
        )

        score = (
            len(common_skills)
            / len(job_skills)
            * 100
        ) if job_skills else 0

        st.subheader("Match Score")
        st.write(f"{score:.2f}%")

        # Missing Skills
        missing_skills = set(job_skills) - set(detected_skills)

        st.subheader("Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.write("❌", skill)
        else:
            st.write("No missing skills found!")

        # Resume Strength
        st.subheader("Resume Strength")

        if score >= 80:
            st.success("Excellent Resume Match")
        elif score >= 60:
            st.warning("Good Resume Match")
        else:
            st.error("Needs Improvement")