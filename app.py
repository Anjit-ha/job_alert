import streamlit as st
import pandas as pd
from difflib import SequenceMatcher

# Load clustered job data
jobs_df = pd.read_csv("clustered_jobs.csv")  # Make sure this is your updated job+cluster file

# Example cluster name mapping
cluster_labels = {
    0: "Cloud & DevOps",
    1: "Data Science & Analytics",
    2: "Software Engineering",
    3: "ML & AI",
    4: "Strategy & Management"
}

st.set_page_config(page_title="Karkidi Job Monitor", layout="wide")
st.title("📊 Karkidi Job Monitor & Clustering Dashboard")

# --- Sidebar: Preferences ---
st.sidebar.header("🔧 Preferences")
user_input = st.sidebar.text_input("Enter preferred skills (comma-separated):", "python,data science")
user_skills = [s.strip().lower() for s in user_input.split(',') if s.strip()]

# --- Function to calculate fuzzy match ---
def skill_match(user_skills, job_skills):
    return any(
        SequenceMatcher(None, u, j).ratio() > 0.6
        for u in user_skills for j in job_skills
    )

# --- Match jobs based on user skills ---
matched_jobs = []
for _, row in jobs_df.iterrows():
    job_skills = [s.strip().lower() for s in row['skills'].split(',') if s.strip()]
    if skill_match(user_skills, job_skills):
        match_score = sum(1 for u in user_skills for j in job_skills if SequenceMatcher(None, u, j).ratio() > 0.6)
        matched_jobs.append((row['title'], row['company'], ', '.join(job_skills), match_score))

# --- Sidebar Alerts ---
st.sidebar.subheader("🔔 Job Alerts")
if matched_jobs:
    st.sidebar.success(f"{len(matched_jobs)} matching job(s) found!")
    for job in matched_jobs:
        st.sidebar.markdown(f"- **{job[0]}** at *{job[1]}* ({job[3]} skill match)")
else:
    st.sidebar.info("No matching jobs found.")

# --- Job Cluster Browser ---
st.subheader("📁 Browse Job Clusters")
cluster_options = list(sorted(jobs_df['cluster'].unique()))
selected_cluster = st.selectbox("Select Cluster", cluster_options)

cluster_df = jobs_df[jobs_df['cluster'] == selected_cluster][['title', 'company', 'skills']]
st.markdown(f"### Cluster: {cluster_labels.get(selected_cluster, 'Unknown')}")
st.dataframe(cluster_df.reset_index(drop=True), use_container_width=True)

# --- Matching Summary ---
if matched_jobs:
    st.subheader("✅ Matched Jobs")
    matched_df = pd.DataFrame(matched_jobs, columns=["title", "company", "skills", "match_score"])
    matched_df = matched_df.sort_values(by="match_score", ascending=False)
    st.dataframe(matched_df, use_container_width=True)

# --- Footer ---
st.markdown("""
---
✅ **Tip**: Improve match quality by including variations like `machine learning`, `ML`, `cloud`, etc.
""")