import pandas as pd

def load_skills():

    skills = pd.read_csv(
        "skills.csv",
        header=None
    )

    return skills[0].tolist()


def extract_skills(
        resume_text,
        skill_list
):

    found_skills = []

    for skill in skill_list:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)

    return found_skills