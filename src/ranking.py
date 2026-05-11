from src.cosine_similarity import computecosinesimilarity

def rank_candidates(resumes, job_descriptions, tfidf_vectors, job_description_vectors):
    rankings = []
    for jd_index, job_description in enumerate(job_descriptions):
        job_description_vector = job_description_vectors[jd_index]
        candidate_rankings = []
        for resume_index, resume in enumerate(resumes):
            tfidf_vector = tfidf_vectors[resume_index]
            similarity = computecosinesimilarity(tfidf_vector, job_description_vector)
            candidate_rankings.append((resume.get('Candidate', ''), similarity))
        candidate_rankings.sort(key=lambda x: x[1], reverse=True)
        rankings.append(candidate_rankings)
    return rankings