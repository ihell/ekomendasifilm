import pandas as pd
from src.collaborative import get_collaborative_recommendations

def get_recommendations(user_id):
    # Membaca file ratings.csv dengan header yang sudah ada
    ratings = pd.read_csv("data/ratings.csv", sep='\t', header=0)
    movies = pd.read_csv("data/processed_movies.csv", sep=',')
    return get_collaborative_recommendations(user_id, ratings, movies)