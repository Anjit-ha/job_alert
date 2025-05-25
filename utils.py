# utils.py
from scraper import scrape_jobs
from preprocess import vectorize_skills
from cluster import cluster_jobs, save_model, assign_clusters, load_model
import os

def run_pipeline():
    jobs = scrape_jobs()
    if 'skills' not in jobs.columns:
        raise ValueError("The scraped job data does not contain a 'skills' column.")

    tfidf_matrix, vectorizer = vectorize_skills(jobs)

    if not os.path.exists('job_cluster_model.pkl'):
        model = cluster_jobs(tfidf_matrix)
        save_model(model)
    else:
        model = load_model()

    clustered_jobs = assign_clusters(jobs, model, tfidf_matrix)
    return clustered_jobs
