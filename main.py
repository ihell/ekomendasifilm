from src.recommend import get_recommendations

if __name__ == "__main__":
    user_id = int(input("Masukkan User ID: "))  # Meminta input user ID
    recommendations = get_recommendations(user_id)  # Mendapatkan rekomendasi
    print("\n🎬 Rekomendasi Film untuk Anda:\n")
    for idx, movie in enumerate(recommendations, 1):
        print(f"{idx}. {movie}")