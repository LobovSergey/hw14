def dict_by_title(response):
    dict_val = list(response[0])
    dict_keys = ['title', 'country', 'release_year', 'listed_in', 'description']
    movie = {dict_keys[i]: dict_val[i] for i in range(5)}
    return movie


def dict_by_date(response):
    list_movies = []
    for _tuple in response:
        dict_val = list(_tuple)
        dict_keys = ['title', 'release_year']
        movie = {dict_keys[i]: dict_val[i] for i in range(2)}
        list_movies.append(movie)
    return list_movies



