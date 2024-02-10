def average_imdb_score_by_category(movie_list, category):
    category_movies = movies_by_category(movie_list, category)
    return average_imdb_score(category_movies)
