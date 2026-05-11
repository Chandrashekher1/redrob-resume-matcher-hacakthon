from utils.helper_functions import normalize_skills


def normalize_skills_in_resumes(resumes):
    normalized_resumes = []
    for resume in resumes:
        raw_skills = resume.get('Raw Skills', '')
        normalized_skills = normalize_skills(raw_skills)
        normalized_resumes.append({
            'ID': resume.get('ID', ''),
            'Candidate': resume.get('Candidate', ''),
            'Raw Skills': raw_skills,
            'Normalized Skills': normalized_skills,
            'Background': resume.get('Background', ''),
        })
    return normalized_resumes