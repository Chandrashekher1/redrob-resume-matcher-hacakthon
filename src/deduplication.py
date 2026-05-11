def deduplicate_skills(resumes):
    deduplicated_resumes = []
    for resume in resumes:
        skills = resume.get('Normalized Skills', [])
        deduplicated_skills = sorted(set(skills))
        deduplicated_resumes.append({
            'ID': resume.get('ID', ''),
            'Candidate': resume.get('Candidate', ''),
            'Raw Skills': resume.get('Raw Skills', ''),
            'Normalized Skills': deduplicated_skills,
            'Background': resume.get('Background', ''),
        })
    return deduplicated_resumes