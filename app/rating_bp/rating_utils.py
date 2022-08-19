def dict_by_rating(response):
    list_movies = []
    for _tuple in response:
        dict_val = list(_tuple)
        dict_keys = ['title', 'rating', 'description']
        movie = {dict_keys[i]: dict_val[i] for i in range(3)}
        list_movies.append(movie)
    return list_movies
