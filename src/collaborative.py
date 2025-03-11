import pandas as pd

def get_collaborative_recommendations(user_id, ratings, movies):
    # Membuat pivot table dari ratings
    user_movie_ratings = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    
    # Menghitung similarity antar pengguna
    from sklearn.metrics.pairwise import cosine_similarity
    user_similarity = cosine_similarity(user_movie_ratings)
    
    # Mendapatkan indeks pengguna
    user_index = user_movie_ratings.index.get_loc(user_id)
    
    # Mendapatkan skor similarity untuk pengguna tertentu
    similarity_scores = user_similarity[user_index]
    
    # Mengurutkan skor similarity dan mendapatkan indeks pengguna yang mirip
    similar_users = user_movie_ratings.index[similarity_scores.argsort()[::-1]]
    
    # Mendapatkan rekomendasi film berdasarkan pengguna yang mirip
    similar_users_ratings = user_movie_ratings.loc[similar_users]
    movie_scores = similar_users_ratings.mean(axis=0)
    
    # Menghapus film yang sudah ditonton oleh pengguna
    watched_movies = user_movie_ratings.loc[user_id]
    movie_scores = movie_scores[watched_movies == 0]
    
    # Mengurutkan film berdasarkan skor
    recommendations = movie_scores.sort_values(ascending=False).index
    
    # Mengambil judul film dari DataFrame movies
    recommended_movies = movies[movies['movieId'].isin(recommendations)]['title'].tolist()
    
    return recommended_movies