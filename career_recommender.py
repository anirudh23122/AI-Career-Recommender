import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("careers.csv")

# Vectorize career skills
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['skills'])

def recommend_career(user_skills):
    user_vector = vectorizer.transform([user_skills])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

    scores = similarity_scores[0]
    ranked_indices = scores.argsort()[::-1]

    recommendations = []
    for idx in ranked_indices[:3]:
        career = data.iloc[idx]['career']
        required_skills = set(data.iloc[idx]['skills'].split())
        user_skill_set = set(user_skills.lower().split())

        missing_skills = required_skills - user_skill_set

        recommendations.append({
            "Career": career,
            "Match Score": round(scores[idx] * 100, 2),
            "Missing Skills": list(missing_skills)
        })

    return recommendations
