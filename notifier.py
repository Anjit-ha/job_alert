from config import USER_PREFERRED_SKILLS

def notify_user(df):
    alerts = []
    for _, row in df.iterrows():
        job_skills = [s.strip().lower() for s in row['skills'].split(',')]
        match = any(skill in job_skills for skill in USER_PREFERRED_SKILLS)
        if match:
            alert = f"🔔 New Job Match: {row['title']} at {row['company']}"
            alerts.append(alert)
    return alerts
