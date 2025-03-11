from src.recommend import recommend

def main():
    user_id = int(input("Masukkan ID pengguna: "))
    movie_id = int(input("Masukkan ID film: "))
    recommendations = recommend(user_id, movie_id)
    print("Rekomendasi film berdasarkan kesukaan Anda:")
    for rec in recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    main()
