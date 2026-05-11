Resume Matching Engine

This project aims to build a resume matching engine that can match resumes with job descriptions based on the skills required for each job.

Data

The project uses two datasets:
resumes.csv: contains information about 10 candidates, including their raw skills and background.
job_descriptions.csv: contains information about 3 job descriptions, including the required and preferred skills.

The project also uses a skill_aliases.json file to map different skill names to a standard format.

Code

The project consists of several Python scripts:
utils/constants.py: defines constants used throughout the project.
utils/helper_functions.py: contains helper functions for loading data, normalizing skills, and computing TF-IDF vectors.
src/skill_normalization.py: normalizes skills in the resumes dataset.
src/deduplication.py: deduplicates skills in the resumes dataset.
src/vocabulary_construction.py: constructs a vocabulary of unique skills from the resumes dataset.
src/tfidfvector_construction.py: computes TF-IDF vectors for the resumes and job descriptions datasets.
src/jobdescriptionvector_construction.py: constructs job description vectors from the job descriptions dataset.
src/cosine_similarity.py: computes cosine similarity between resumes and job descriptions.
src/ranking.py: ranks candidates based on their similarity to each job description.
src/main.py: runs the entire pipeline and prints the ranked candidates for each job description.

Requirements
Python 3.8+
pandas
numpy
json

Usage
Clone the repository:(https://github.com/Chandrashekher1/redrob-resume-matcher-hacakthon.git)
Install requirements: pip install -r requirements.txt
Run the pipeline: python src/main.py

Output

The project outputs a ranked list of candidates for each job description, along with their similarity scores.

Future Work
Improve the skill normalization and deduplication steps to handle more complex skill names and synonyms.
Experiment with different TF-IDF vectorization techniques and parameters to improve the accuracy of the matching engine.
Integrate the project with a web interface or API to make it more accessible and user-friendly.