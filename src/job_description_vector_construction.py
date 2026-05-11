def construct_job_description_vectors(job_descriptions, vocabulary):
    vocabulary_index = {skill: idx for idx, skill in enumerate(vocabulary)}
    job_description_vectors = []
    for job_description in job_descriptions:
        vector = [0] * len(vocabulary)
        for skill in job_description.get('required_skills', []) + job_description.get('preferred_skills', []):
            if skill in vocabulary_index:
                vector[vocabulary_index[skill]] = 1
        job_description_vectors.append(vector)
    return job_description_vectors