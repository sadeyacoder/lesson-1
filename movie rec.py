import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try: movies_df = pd.read_csv("Book1.csv")
except FileNotFoundError:
    print(Fore.MAGENTA + "Error: The file was not found."); raise SystemExit

genre_options = sorted({g.strip() for xs in movies_df["Genre"].dropna().str.split(", ") for g in xs})

def loading():
    for _ in range(3): print(Fore.WHITE + ".", end="", flush=True); time.sleep(0.5)

def sentiment_type(p): return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"

def get_recommendations(genre=None, mood=None, rating=None, n=4):
    filtered_movies = movies_df
    if genre: filtered_movies = filtered_movies[filtered_movies["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: filtered_movies = filtered_movies[filtered_movies["IMDB_Rating"] >= rating]
    if filtered_movies.empty: return "No suitable movie recommendations found."
    filtered_movies, mood_filter, recommendations = filtered_movies.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, movie in filtered_movies.iterrows():
        overview = movie.get("Overview")
        if pd.isna(overview): continue
        polarity = TextBlob(overview).sentiment.polarity
        if (not mood_filter) or polarity >= 0:
            recommendations.append((movie["Series_Title"], polarity))
            if len(recommendations) == n: break
    return recommendations if recommendations else "No suitable movie recommendations found."

def display_recommendations(recommendations, user_name):
    print(Fore.WHITE + f"\nMovie Recommendations for {user_name}:")
    for i, (t, p) in enumerate(recommendations, 1):
        print(f"{Fore.BLUE}{i}. {t} (Polarity: {p:.2f}, {sentiment_type(p)})")

def choose_genre():
    print(Fore.MAGENTA + "Available Genres: ", end="")
    for i, g in enumerate(genre_options, 1): print(f"{Fore.BLUE}{i}. {g}")
    print()
    while True:
        user_input = input(Fore.WHITE + "Enter genre number or name: ").strip()
        if user_input.isdigit() and 1 <= int(user_input) <= len(genre_options): return genre_options[int(user_input) - 1]
        user_input = user_input.title()
        if user_input in genre_options: return user_input
        print(Fore.RED + "Invalid input. Try again.\n")

def choose_rating():
    while True:
        user_input = input(Fore.WHITE + "Enter minimum IMDB rating (3.1-6.5) or 'skip': ").strip()
        if user_input.lower() == "skip": return None
        try:
            rating = float(user_input)
            if 3.6 <= rating <= 9.3: return rating
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

print(Fore.CYAN + "Welcome to the Movie Recommendation System!\n")
user_name = input(Fore.WHITE + "What's your name? ").strip()
print(f"\n{Fore.MAGENTA}Hello, {user_name}!\n")
print(Fore.CYAN + "\nSearching for movie recommendations.\n")

genre = choose_genre()
mood = input(Fore.WHITE + "How do you feel today? (Describe your mood): ").strip()

print(Fore.CYAN + "\nChecking mood", end="", flush=True); loading()
mood_score = TextBlob(mood).sentiment.polarity
mood_label = "positive" if mood_score > 0 else "negative" if mood_score < 0 else "neutral"
print(f"\n{Fore.MAGENTA}Your mood is {mood_label} (Polarity: {mood_score:.2f}).\n")

rating = choose_rating()
print(f"{Fore.CYAN}\nSearching movies for {user_name}", end="", flush=True); loading()
recommendations = get_recommendations(genre=genre, mood=mood, rating=rating, n=4)

print(Fore.RED + recommendations + "\n") if isinstance(recommendations, str) else display_recommendations(recommendations, user_name)

while True:
    choice = input(Fore.WHITE + "\nWould you like more recommendations? (yes/no): ").strip().lower()
    if choice == "no":
        print(Fore.MAGENTA + f"\nEnjoy your recommendations, {user_name}!\n"); break
    if choice == "yes":
        recommendations = get_recommendations(genre=genre, mood=mood, rating=rating, n=5)
        print(Fore.RED + recommendations + "\n") if isinstance(recommendations, str) else display_recommendations(recommendations, user_name)
    else:
        print(Fore.RED + "Invalid choice. Try again.\n")