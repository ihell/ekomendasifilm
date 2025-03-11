from src.data_loader import load_ratings, load_movies
from src.collaborative import collaborative_filtering
from src.content_based import content_based_recommendation

def recommend(user_id, movie_id):
    ratings = load_ratings('data/ratings.csv')
    movies = load_movies('data/movies.csv')
    model, testset = collaborative_filtering(ratings)
    content_recs = content_based_recommendation(movie_id, movies)
    return content_recs