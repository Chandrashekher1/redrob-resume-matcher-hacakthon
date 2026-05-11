import pandas as pd

def constructjobdescriptionvectors(jobdescriptions, vocabulary):
    jobdescriptionvectors = []
    for jobdescription in jobdescriptions:
        vector = [0] * len(vocabulary)
        for skill in jobdescription['requiredskills']:
            if skill in vocabulary:
                vector[vocabulary.index(skill)] = 1
        jobdescriptionvectors.append(vector)
    return jobdescriptionvectors