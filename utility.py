
from fuzzywuzzy import process

def convert_into_lower(demolist):
    return [item.lower() for item in demolist]

def spelling_checker_genre_cast(knowledgebase, checking_for, words_to_check):
    main_list = []
    correct_list = []
    incorrect_list  = []

    for movie in knowledgebase:
        for item in movie[checking_for]:
            if item not in main_list:
                main_list.append(item)
    
    for word in words_to_check:
        if word in main_list:
            correct_list.append(word)
        else:
            correct_word, similarity_ratio = process.extractOne(word, main_list)
            if similarity_ratio >= 70:
                correct_list.append(correct_word)
            else:
                incorrect_list.append(correct_word)

    if incorrect_list:
        print(f"This {checking_for} does not exist in our knowledge base. Please try again with correct spelling.")
        return []
                    
    return correct_list

def spelling_checker_title(knowledgebase, word_to_check):

    main_list = [movie["title"] for movie in knowledgebase]

    if word_to_check in main_list:
        return word_to_check
    
    else:
        correct_word, similarity_ratio = process.extractOne(word_to_check, main_list)
        if similarity_ratio >= 70 :
            return correct_word
        else:
            print(f"This {word_to_check} does not exist in our knowledge base. Please try again with correct spelling.")
            update_knowledgebase(knowledgebase, word_to_check.lower())
            return []

def list_of_genre(knowledgebase):
    main_list = []

    for movie in knowledgebase:
        for item in movie["genres"]:
            if item not in main_list:
                main_list.append(item)
    
    
    print(f"LIST OF GENRES : {main_list}")

def list_of_cast(knowledgebase):
    main_list = []

    for movie in knowledgebase:
        for item in movie["cast"]:
            if item not in main_list:
                main_list.append(item)
    
    
    print(f"LIST OF CAST : {main_list}")

def list_of_movies(knowledgebase):

    main_list = [movie["title"] for movie in knowledgebase]
    
    print(f"LIST OF MOVIES : {main_list}")

def update_knowledgebase(knowledgebase, movie_title):

    choice = input(f"Would you like to add details for {movie_title}? (yes or no) ")
    if choice.lower() == "yes":
        new_movie_genres = input(f"Enter the genres for the new movie '{movie_title}': ").split(",")
        new_movie_cast = input(f"Enter the cast for the new movie '{movie_title}': ").split(",")

        new_movie_genres = convert_into_lower(new_movie_genres)
        new_movie_cast = convert_into_lower(new_movie_cast)

        new_movie = {
            "title": movie_title,
            "genres": new_movie_genres,
            "cast": new_movie_cast
        }
        knowledgebase.append(new_movie)
        print(f"\n'{movie_title}' added to the knowledge base.")
        return
    else:
        print("No changes made.")
        return