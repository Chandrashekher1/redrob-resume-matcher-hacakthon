import pandas as pd
from utils.helperfunctions import computetf_idf

def computetfidfvectors(resumes, jobdescriptions):
    tfidfvectors, jobdescriptionvectors = computetfidf(resumes, job_descriptions)
    return tfidfvectors, jobdescriptionvectors