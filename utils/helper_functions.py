import json
import os
import math
from collections import Counter

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALIASES_PATH = os.path.join(ROOT_DIR, 'data', 'skill_aliases.json')
with open(ALIASES_PATH, encoding='utf-8') as f:
    SKILL_ALIASES = json.load(f)


def load_resumes(filepath):
    resumes = []
    with open(filepath, encoding='utf-8') as f:
        lines = f.read().splitlines()
    if not lines:
        return resumes

    for line in lines[1:]:
        if not line.strip():
            continue
        left, background = line.rsplit(',', 1)
        parts = left.split(',', 2)
        if len(parts) < 3:
            continue
        resume_id, candidate, raw_skills = parts
        resumes.append({
            'ID': resume_id.strip(),
            'Candidate': candidate.strip(),
            'Raw Skills': raw_skills.strip(),
            'Background': background.strip(),
        })
    return resumes


def load_job_descriptions(filepath):
    job_descriptions = []
    with open(filepath, encoding='utf-8') as f:
        lines = f.read().splitlines()
    if not lines:
        return job_descriptions

    for line in lines[1:]:
        parts = line.split(',', 3)
        if len(parts) < 4:
            continue
        jd_id, company, role, skills = parts
        normalized_skills = normalize_skill_list(skills)
        job_descriptions.append({
            'JD': jd_id.strip(),
            'Company': company.strip(),
            'Role': role.strip(),
            'required_skills': normalized_skills,
            'preferred_skills': [],
        })
    return job_descriptions


def normalize_skill_list(skills):
    return [normalize_skill(skill) for skill in skills.split(',') if skill.strip()]


def normalize_skills(raw_skills):
    skills = [skill.strip().lower() for skill in raw_skills.split(',') if skill.strip()]
    normalized_skills = []
    for skill in skills:
        if skill in SKILL_ALIASES:
            normalized_skills.append(SKILL_ALIASES[skill])
        else:
            normalized_skills.append(skill.replace(' ', '_'))
    return sorted(set(normalized_skills))


def normalize_skill(skill):
    normalized = skill.strip().lower()
    if not normalized:
        return ''
    return SKILL_ALIASES.get(normalized, normalized.replace(' ', '_'))


def compute_tfidf(resumes, job_descriptions, vocabulary=None):
    if vocabulary is None:
        vocabulary = set()
        for resume in resumes:
            vocabulary.update(resume.get('Normalized Skills', []))
        for jd in job_descriptions:
            vocabulary.update(jd.get('required_skills', []))
            vocabulary.update(jd.get('preferred_skills', []))
        vocabulary = sorted(vocabulary)

    documents = []
    for resume in resumes:
        documents.append(resume.get('Normalized Skills', []))
    for jd in job_descriptions:
        documents.append(jd.get('required_skills', []) + jd.get('preferred_skills', []))

    total_documents = len(documents)
    idf = {}
    for skills in documents:
        unique_skills = set(skills)
        for skill in unique_skills:
            idf[skill] = idf.get(skill, 0) + 1
    idf = {skill: math.log((total_documents + 1) / (count + 1)) + 1 for skill, count in idf.items()}

    tfidf_resumes = []
    for resume in resumes:
        skills = resume.get('Normalized Skills', [])
        counts = Counter(skills)
        total = sum(counts.values()) or 1
        tfidf = {skill: counts[skill] / total * idf.get(skill, 1.0) for skill in counts}
        tfidf_resumes.append(tfidf)

    tfidf_job_descriptions = []
    for jd in job_descriptions:
        skills = jd.get('required_skills', []) + jd.get('preferred_skills', [])
        counts = Counter(skills)
        total = sum(counts.values()) or 1
        tfidf = {skill: counts[skill] / total * idf.get(skill, 1.0) for skill in counts}
        tfidf_job_descriptions.append(tfidf)

    return tfidf_resumes, tfidf_job_descriptions