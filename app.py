import streamlit as st
from career_recommender import recommend_career

st.set_page_config(page_title="AI Career Guidance Agent")

st.title("🚀 AI-Powered Career Guidance & Skill Recommendation Agent")

st.write("Enter your skills separated by space (example: python sql machine learning)")

user_skills = st.text_input("Your Skills:")

if st.button("Get Career Recommendations"):
    if user_skills.strip() == "":
        st.warning("Please enter your skills.")
    else:
        results = recommend_career(user_skills)

        st.subheader("🎯 Top Career Matches")
        for res in results:
            st.markdown(f"### {res['Career']}")
            st.write(f"Match Score: {res['Match Score']}%")
            st.write("Missing Skills:", ", ".join(res["Missing Skills"]))
            st.write("---")
