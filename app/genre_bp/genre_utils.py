def dict_by_genre(response):
    list_movies = []
    for _tuple in response:
        dict_val = list(_tuple)
        dict_keys = ['title', 'description']
        movie = {dict_keys[i]: dict_val[i] for i in range(2)}
        list_movies.append(movie)
    return list_movies
