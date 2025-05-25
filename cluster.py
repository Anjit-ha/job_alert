# cluster.py
import pickle
from sklearn.cluster import KMeans
import pandas as pd

def cluster_jobs(tfidf_matrix, n_clusters=5):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(tfidf_matrix)
    return model

def assign_clusters(jobs_df, model, tfidf_matrix):
    clusters = model.predict(tfidf_matrix)
    jobs_df['cluster'] = clusters
    jobs_df.to_csv('clustered_jobs.csv', index=False)
    return jobs_df

def save_model(model, path='job_cluster_model.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(model, f)

def load_model(path='job_cluster_model.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)
