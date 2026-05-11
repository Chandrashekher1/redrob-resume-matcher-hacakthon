from utils.helper_functions import compute_tfidf

def compute_tfidf_vectors(resumes, job_descriptions, vocabulary=None):
    return compute_tfidf(resumes, job_descriptions, vocabulary)