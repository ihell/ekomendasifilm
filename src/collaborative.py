import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_ratings(file_path):
    """Membaca dataset ratings."""
    return pd.read_csv(file_path)

def create_user_item_matrix(ratings):
    """Membuat matriks user-item dari data ratings."""
    return ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

def calculate_similarity(user_item_matrix):
    """Menghitung kemiripan antar pengguna menggunakan Cosine Similarity."""
    return cosine_similarity(user_item_matrix)

def get_user_recommendations(user_id, user_item_matrix, similarity_matrix, movies, top_n=5):
    """Memberikan rekomendasi film untuk pengguna tertentu berdasarkan Collaborative Filtering."""
    if user_id not in user_item_matrix.index:
        return []
    
    user_index = user_item_matrix.index.get_loc(user_id)
    similarity_scores = similarity_matrix[user_index]
    similar_users = np.argsort(similarity_scores)[::-1][1:]
    
    weighted_ratings = np.dot(similarity_scores, user_item_matrix)
    recommended_movie_ids = np.argsort(weighted_ratings)[::-1]
    
    recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)].head(top_n)
    return recommended_movies[['movieId', 'title']].values.tolist()

if __name__ == "__main__":
    ratings = load_ratings("../data/ratings.csv")
    movies = pd.read_csv("../data/movies.csv")
    user_item_matrix = create_user_item_matrix(ratings)
    similarity_matrix = calculate_similarity(user_item_matrix)
    
    user_id = 1  # Ganti dengan ID pengguna yang diinginkan
    recommendations = get_user_recommendations(user_id, user_item_matrix, similarity_matrix, movies)
    print("Rekomendasi untuk User", user_id, ":", recommendations)
 