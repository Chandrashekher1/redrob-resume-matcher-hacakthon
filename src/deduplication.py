import pandas as pd

def deduplicate_skills(resumes):
    deduplicated_resumes = []
    for resume in resumes:
        skills = resume['Normalized Skills']
        deduplicated_skills = sorted(set(skills))
        deduplicatedresumes.append({'ID': resume['ID'], 'Candidate': resume['Candidate'], 'Raw Skills': resume['Raw Skills'], 'Normalized Skills': deduplicatedskills})
    return pd.DataFrame(deduplicated_resumes)