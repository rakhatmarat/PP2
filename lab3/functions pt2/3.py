def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]
