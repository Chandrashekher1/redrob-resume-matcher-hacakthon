def construct_vocabulary(resumes):
    vocabulary = set()
    for resume in resumes:
        vocabulary.update(resume.get('Normalized Skills', []))
    return sorted(vocabulary)