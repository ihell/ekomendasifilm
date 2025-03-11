import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def content_based_recommendation(movie_id, movies):
    """Menerapkan Content-Based Filtering berdasarkan deskripsi film."""
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['description'].fillna(''))
    similarity = cosine_similarity(tfidf_matrix)
    idx = movies.index[movies['movieId'] == movie_id].tolist()[0]
    similar_movies = list(enumerate(similarity[idx]))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:11]
    return [movies.iloc[i[0]]['title'] for i in similar_movies]