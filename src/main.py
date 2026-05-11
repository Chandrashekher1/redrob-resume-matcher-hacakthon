import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.skill_normalization import normalize_skills_in_resumes
from src.deduplication import deduplicate_skills
from src.vocabulary_construction import construct_vocabulary
from src.tf_idf_vector_construction import compute_tfidf_vectors
from src.job_description_vector_construction import construct_job_description_vectors
from src.ranking import rank_candidates
from utils.helper_functions import load_resumes, load_job_descriptions

def main():
    print('Resume vs Job Description Matching Pipeline')
    print('===========================================')

    resumes = load_resumes(os.path.join(ROOT_DIR, 'data', 'resume.csv'))
    job_descriptions = load_job_descriptions(os.path.join(ROOT_DIR, 'data', 'job_descriptions.csv'))

    normalized_resumes = normalize_skills_in_resumes(resumes)
    deduplicated_resumes = deduplicate_skills(normalized_resumes)
    vocabulary = construct_vocabulary(deduplicated_resumes)

    tfidf_vectors, job_description_tfidf_vectors = compute_tfidf_vectors(
        deduplicated_resumes,
        job_descriptions,
        vocabulary,
    )
    job_description_binary_vectors = construct_job_description_vectors(job_descriptions, vocabulary)

    print('\nStage 1 & 2: Skill Normalization')
    print('-----------------------------------')
    for resume in normalized_resumes:
        print(f"{resume['Candidate']}    -> {resume['Normalized Skills']}")

    print('\nStage 3: TF-IDF Computation')
    print('-----------------------------------')
    print(f"Shared vocabulary: {len(vocabulary)} unique canonical skills")

    print('\nStage 4: JD Binary Vectors')
    print('-----------------------------------')
    for i, jd in enumerate(job_descriptions):
        skills = jd.get('required_skills', []) + jd.get('preferred_skills', [])
        active_count = sum(job_description_binary_vectors[i])
        outside_vocab = [skill for skill in skills if skill not in vocabulary]
        if outside_vocab:
            print(f"{jd['JD']} - {jd['Company']} ({jd['Role']}): {active_count} active skills (outside vocab: {outside_vocab})")
        else:
            print(f"{jd['JD']} - {jd['Company']} ({jd['Role']}): {active_count} active skills")

    print('\nStage 5: Cosine Similarity Rankings')
    print('-----------------------------------')
    rankings = rank_candidates(
        deduplicated_resumes,
        job_descriptions,
        tfidf_vectors,
        job_description_tfidf_vectors,
    )

    for i, ranking in enumerate(rankings):
        jd = job_descriptions[i]
        print(f"\n{jd['JD']} - {jd['Company']} ({jd['Role']})")
        for rank, (candidate, similarity) in enumerate(ranking, start=1):
            print(f"{rank}. {candidate}    {similarity:.2f}")


if __name__ == '__main__':
    main()