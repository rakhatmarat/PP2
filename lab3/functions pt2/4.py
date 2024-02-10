def average_imdb_score(movie_list):
    if not movie_list:
        return 0
    total_score = sum(movie["imdb"] for movie in movie_list)
    return total_score / len(movie_list)
