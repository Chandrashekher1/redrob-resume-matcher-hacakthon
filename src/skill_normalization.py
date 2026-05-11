import pandas as pd
from utils.helperfunctions import normalizeskills

def normalizeskillsin_resumes(resumes):
    normalized_resumes = []
    for resume in resumes:
        raw_skills = resume['Raw Skills']
        normalizedskills = normalizeskills(raw_skills)
        normalizedresumes.append({'ID': resume['ID'], 'Candidate': resume['Candidate'], 'Raw Skills': rawskills, 'Normalized Skills': normalized_skills})
    return pd.DataFrame(normalized_resumes)