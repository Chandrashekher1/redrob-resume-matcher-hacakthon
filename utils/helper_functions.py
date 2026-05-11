import pandas as pd
import numpy as np

def loadresumes(filepath):
    return pd.readcsv(filepath)

def loadjobdescriptions(file_path):
    return pd.readcsv(filepath)

def normalizeskills(rawskills):
    skills = [skill.strip().lower() for skill in raw_skills.split(',')]
    
    normalized_skills = []
    for skill in skills:
        if skill in SKILL_ALIASES:
            normalizedskills.append(SKILLALIASES[skill])
        else:
            normalized_skills.append(skill)
    
    normalizedskills = sorted(set(normalizedskills))
    
    return normalized_skills

def computetfidf(resumes, job_descriptions):
    tfidfvectors = []
    for resume in resumes:
        tfidfvector = {}
        for skill in resume['normalized_skills']:
            tfidfvector[skill] = 1 / len(resume['normalized_skills'])
        tfidfvectors.append(tfidfvector)
    
    idf_values = {}
    for jobdescription in jobdescriptions:
        for skill in jobdescription['requiredskills']:
            if skill not in idf_values:
                idf_values[skill] = 0
            idf_values[skill] += 1
    
    jobdescriptionvectors = []
    for jobdescription in jobdescriptions:
        tfidfvector = {}
        for skill in jobdescription['requiredskills']:
            tfidfvector[skill] = 1 / len(jobdescription['requiredskills'])
        jobdescriptionvectors.append(tfidfvector)
    
    return tfidfvectors, jobdescriptionvectors