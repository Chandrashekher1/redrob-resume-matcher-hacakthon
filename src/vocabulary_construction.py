import pandas as pd

def construct_vocabulary(resumes):
    vocabulary = set()
    for resume in resumes:
        skills = resume['Normalized Skills']
        vocabulary.update(skills)
    return sorted(list(vocabulary))