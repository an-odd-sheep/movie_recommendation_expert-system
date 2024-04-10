# USER INTERFACE

from knowledgebase import hollywood, bollywood, animes
from inference_engine import recommend_by_genre, recommend_by_cast, recommend_by_genre_and_cast, recommend_similar_movies 
from utility import convert_into_lower, list_of_cast, list_of_genre, list_of_movies

def start():
    while True:
        industry = input("Choose your Film Industry type: \n1. Hollywood \n2. Bollywood. \n3. Anime \nEnter 1, 2 or 3: ")
        if (industry == '1'):
            run_recommendation(hollywood)
            print("\n")

        elif (industry == '2'):
            run_recommendation(bollywood)
            print("\n")

        elif (industry == '3'):
            run_recommendation(animes)
            print("\n")


def run_recommendation(knowledgebase):
    
    choice = input("Choose your recommendation type:\n1. By genre\n2. By cast\n3. Similar genre and cast\n4. Similar movies/animes. \nEnter 1, 2,3 or 4: ")
    
    if choice == '1':
        list_of_genre(knowledgebase)
        preferred_genres = str(input("Enter your preferred genre , separated by commas: ")).split(",")
        preferred_genres = convert_into_lower(preferred_genres)
        recommend_by_genre(knowledgebase, preferred_genres, "any")

    elif choice == '2':
        list_of_cast(knowledgebase)
        preferred_cast = str(input("Enter your preferred actor , separated by commas: ")).split(",")
        preferred_cast = convert_into_lower(preferred_cast)
        recommend_by_cast(knowledgebase, preferred_cast)

    elif choice == '3':
        list_of_genre(knowledgebase)
        preferred_genres = str(input("Enter your preferred genres , separated by commas: ")).split(",")
        list_of_cast(knowledgebase)
        preferred_cast = str(input("Enter your preferred actors , separated by commas: ")).split(",")
        preferred_genres = convert_into_lower(preferred_genres)
        preferred_cast = convert_into_lower(preferred_cast)
        recommend_by_genre_and_cast(knowledgebase, preferred_genres, preferred_cast)

    elif choice == '4':
        list_of_movies(knowledgebase)
        movie_title = str(input("Enter the title of a movie: "))
        movie_title = movie_title.lower()
        recommend_similar_movies(knowledgebase, movie_title)
        
    else:
        print("Invalid choice.")


start()
