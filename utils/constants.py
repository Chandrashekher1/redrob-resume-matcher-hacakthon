import json

with open('data/skill_aliases.json') as f:
    SKILL_ALIASES = json.load(f)

RESUME_FILE = 'data/resumes.csv'
JOBDESCRIPTIONFILE = 'data/job_descriptions.csv'
OUTPUT_FILE = 'output/results.txt'