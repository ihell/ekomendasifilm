import pandas as pd

def load_ratings(filepath: str):
    """Memuat data rating dari file CSV."""
    return pd.read_csv(filepath)

def load_movies(filepath: str):
    """Memuat data film dari file CSV."""
    return pd.read_csv(filepath)

### src/collaborative.py
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

def collaborative_filtering(ratings):
    """Menerapkan Collaborative Filtering dengan SVD."""
    reader = Reader(rating_scale=(ratings['rating'].min(), ratings['rating'].max()))
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(trainset)
    return model, testset
