# preprocess.py
from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_skills(job_df):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(job_df['skills'].fillna(''))
    return tfidf_matrix, vectorizer
