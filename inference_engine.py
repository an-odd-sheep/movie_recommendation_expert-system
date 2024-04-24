# INFERENCE ENGINE WITH LEARNING MODULE
from utility import spelling_checker_genre_cast, spelling_checker_title, convert_into_lower

def recommend_by_genre(knowledegebase, preferred_genres, sm):
    if not preferred_genres:
        print("No preferred genres provided. Cannot make recommendations.")
        return

    preferred_genres = spelling_checker_genre_cast(knowledegebase, "genres", preferred_genres)

    if not preferred_genres:
        print("No movies found based on the preferred genres.")
        return
    
    recommendations = []

    if sm == "any":
        recommendations = [movie["title"] for movie in knowledegebase if any(genre in preferred_genres for genre in movie["genres"])]
    elif sm == "all" :
        recommendations = [movie["title"] for movie in knowledegebase if all(genre in preferred_genres for genre in movie["genres"])]

    if recommendations:
        print(f"\nRecommended movies based on your preferred genres {preferred_genres}:")
        for rec in recommendations:
            print(rec)

    else:
        print("No movies found based on the preferred genres.")
        return


def recommend_by_cast(knowledegebase, preferred_cast):
    if not preferred_cast:
        print("No preferred cast provided. Cannot make recommendations.")
        return
    preferred_cast = spelling_checker_genre_cast(knowledegebase, "cast", preferred_cast)

    if not preferred_cast :
        print("No movies found based on the preferred cast.")
        return
  
    recommendations = [movie["title"] for movie in knowledegebase if any(actor in preferred_cast for actor in movie["cast"])]

    if recommendations:
        print(f"\nRecommended movies based on your preferred cast {preferred_cast}:")
        for rec in recommendations:
            print(rec)
            
    else:
        print("No movies found based on the preferred cast.")
        return


            
def recommend_by_genre_and_cast(knowledegebase, preferred_genres, preferred_cast):
    if not preferred_cast or not preferred_genres :
        print("No preferred genre/cast provided. Cannot make recommendations.")
        return
    
    preferred_genres = spelling_checker_genre_cast(knowledegebase, "genres", preferred_genres)
    preferred_cast = spelling_checker_genre_cast(knowledegebase, "cast", preferred_cast)

    if not preferred_cast or preferred_genres:
        print("No movies found based on the preferred genre and cast.")
        return

    recommendations = [movie["title"] for movie in knowledegebase if 
                       all(genre in preferred_genres for genre in movie["genres"]) and any(actor in preferred_cast for actor in movie["cast"])]
    
    if recommendations:
        print(f"\nRecommended movies similar to your preferred cast {preferred_cast} in your preferred genre {preferred_genres} :")
        for rec in recommendations:
            print(rec)

    else:
            print("No movies found based on the preferred genre and cast.")
            return


def recommend_similar_movies(knowledgebase, movie_title):

    if not movie_title:
        print("No movie title provided. Cannot make recommendations.")
        return

    movie_title = spelling_checker_title(knowledgebase, movie_title)

    if not movie_title:
        return

    choice = input ("Choose recommend by\n1. By genre.\n2. By cast.\n3. By genre and cast.\nEnter 1, 2 or 3: ")
    
    if choice == '1':
        preferred_genres = [genre for movie in knowledgebase if movie["title"] == movie_title for genre in movie["genres"]]
        recommend_by_genre(knowledgebase, preferred_genres, "all")

    elif choice == '2':
        preferred_cast = [cast for movie in knowledgebase if movie["title"] == movie_title for cast in movie["cast"]]
        recommend_by_cast(knowledgebase, preferred_cast)

    elif choice == '3':
        preferred_genres = [genre for movie in knowledgebase if movie["title"] == movie_title for genre in movie["genres"]]
        preferred_cast = [cast for movie in knowledgebase if movie["title"] == movie_title for cast in movie["cast"]]
        recommend_by_genre_and_cast(knowledgebase, preferred_genres, preferred_cast)

    else:
        print("Invalid choice.")



