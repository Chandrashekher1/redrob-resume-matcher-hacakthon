import pandas as pd
from src.cosinesimilarity import computecosine_similarity

def rankcandidates(resumes, jobdescriptions, tfidfvectors, jobdescriptionvectors):
    rankings = []
    for jobdescription in jobdescriptions:
        jobdescriptionvector = jobdescriptionvectors[jobdescriptions.index(jobdescription)]
        candidate_rankings = []
        for resume in resumes:
            tfidfvector = tfidfvectors[resumes.index(resume)]
            similarity = computecosinesimilarity(tfidfvector, jobdescriptionvector)
            candidate_rankings.append((resume['Candidate'], similarity))
        candidate_rankings.sort(key=lambda x: x[1], reverse=True)
        rankings.append(candidate_rankings)
    return rankings