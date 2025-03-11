import pandas as pd

# Membaca file ratings.csv tanpa menambahkan header baru
ratings = pd.read_csv('data/ratings.csv', sep='\t', skiprows=1, names=['userId', 'movieId', 'rating', 'timestamp'])

# Menyimpan file ratings.csv yang sudah dibersihkan tanpa menambahkan header baru
ratings.drop(columns=['timestamp'], inplace=True)
ratings.to_csv('data/ratings.csv', sep='\t', index=False)
print("✅ ratings.csv berhasil dikonversi!")

# Membaca file movies.csv
movies = pd.read_csv('data/movies.csv', sep=',', usecols=['movieId', 'title'])

# Menyimpan file movies.csv yang sudah dikonversi
movies.to_csv('data/processed_movies.csv', index=False)
print("✅ movies.csv berhasil dikonversi!")