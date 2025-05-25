from config import USER_PREFERRED_SKILLS

import os

def notify_user(df, seen_file="seen_jobs.txt"):
    alerts = []
    seen_jobs = set()

    # Load already seen jobs
    if os.path.exists(seen_file):
        with open(seen_file, "r") as f:
            seen_jobs = set(line.strip() for line in f)

    new_seen_jobs = []

    for _, row in df.iterrows():
        job_id = f"{row['title']}|{row['company']}" 

        if job_id in seen_jobs:
            continue  # Skip already seen

        job_skills = row['skills'].split(', ')
        match = any(skill in job_skills for skill in USER_PREFERRED_SKILLS)
        if match:
            alert = f"🔔 New Job Match: {row['title']} at {row['company']}"
            alerts.append(alert)
            new_seen_jobs.append(job_id)

    # Save new seen jobs
    with open(seen_file, "a") as f:
        for job in new_seen_jobs:
            f.write(job + "\n")

    return alerts

