import pandas as pd

# Membaca file ratings.csv dengan header yang sudah ada
ratings = pd.read_csv("data/ratings.csv", sep='\t', header=0)

# Menampilkan daftar unik user ID
unique_user_ids = ratings['userId'].unique()
print("User ID yang tersedia dalam dataset:")
print(unique_user_ids)