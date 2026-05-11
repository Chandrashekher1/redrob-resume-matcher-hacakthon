import pandas as pd
from src.skillnormalization import normalizeskillsinresumes
from src.deduplication import deduplicate_skills
from src.vocabularyconstruction import constructvocabulary
from src.tfidfvectorconstruction import computetfidfvectors
from src.jobdescriptionvectorconstruction import constructjobdescriptionvectors
from src.ranking import rank_candidates

def main():
    resumes = pd.read_csv('data/resumes.csv')
    jobdescriptions = pd.readcsv('data/job_descriptions.csv')
    
    normalizedresumes = normalizeskillsinresumes(resumes)
    
    deduplicatedresumes = deduplicateskills(normalized_resumes)
    
    vocabulary = constructvocabulary(deduplicatedresumes)
    
    tfidfvectors, jobdescriptionvectors = computetfidfvectors(deduplicatedresumes, job_descriptions)
    
    jobdescriptionvectors = constructjobdescriptionvectors(jobdescriptions, vocabulary)
    
    rankings = rankcandidates(deduplicatedresumes, jobdescriptions, tfidfvectors, jobdescription_vectors)
    
    # Print rankings
    for i, ranking in enumerate(rankings):
        print(f'Job Description {i+1}:')
        for candidate, similarity in ranking:
            print(f'{candidate}: {similarity:.2f}')

if name == 'main':
    main()