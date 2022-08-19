import sqlite3
from collections import Counter

from app.genre_bp.genre_utils import dict_by_genre
from app.movie_bp.movie_utils import dict_by_title, dict_by_date
from app.rating_bp.rating_utils import dict_by_rating

group_rating = {
    'children': ['G'],
    'family': ['G', 'PG', 'PG-13'],
    'adult': ['R', 'NC-17']
}


def get_movie_by_title(data):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT `title`,`country`,`release_year`,`listed_in`,`description`
            FROM netflix
            WHERE `title` IN (?)
            AND `title` IS NOT NULL
            """, [data])
    return dict_by_title(cursor.fetchall())


def get_movie_by_date(date_one, date_two):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT `title`,`release_year`
            FROM netflix
            WHERE `release_year` BETWEEN (?) AND (?)
            AND `title` IS NOT NULL
            LIMIT 100
            """, (date_one, date_two))
    return dict_by_date(cursor.fetchall())


def get_movie_by_rating(rating):
    for key in group_rating.keys():
        if key == rating.lower():
            list_rating = tuple(group_rating[key])
    if len(list_rating) == 2:
        with sqlite3.connect('netflix.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT `title`,`rating`,`description`
                FROM netflix
                WHERE `rating` IN (?,?)
                AND `title` IS NOT NULL
                LIMIT 100
                """, (list_rating))
    elif len(list_rating) == 1:
        with sqlite3.connect('netflix.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT `title`,`rating`,`description`
                FROM netflix
                WHERE `rating` IN (?)
                AND `title` IS NOT NULL
                LIMIT 100
                """, (list_rating))
    elif len(list_rating) == 3:
        with sqlite3.connect('netflix.db') as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT `title`,`rating`,`description`
                FROM netflix
                WHERE `rating` IN (?,?,?)
                AND `title` IS NOT NULL
                LIMIT 100
                """, (list_rating))
    return dict_by_rating(cursor.fetchall())


def get_movie_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT `title`,`description`, `release_year`
            FROM netflix
            WHERE `listed_in` IN (?)
            AND `title` IS NOT NULL
            ORDER BY `release_year` DESC
            LIMIT 10
            """, [genre])
    return dict_by_genre(cursor.fetchall())


def two_actor(name_one, name_two):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f'''
                SELECT `cast`
                FROM netflix
                WHERE `cast` LIKE "%{name_one}%"
                AND `cast` LIKE "%{name_two}%"
                '''
        cursor.execute(query)
        result = cursor.fetchall()
        unique_actor = []
        for i in result:
            for name_string in i:
                name_list = name_string.split(', ')
                for name in name_list:
                    if name != name_one and name != name_two:
                        unique_actor.append(name)
        counter_names = Counter(unique_actor)
        for key, val in counter_names.items():
            if val >= 3:
                print(key)


two_actor('Rose McIver', 'Ben Lamb')
two_actor('Jack Black', 'Dustin Hoffman')


def movies_all_types(date, typed, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f"""
                   SELECT `title`, `description`
                   FROM netflix
                              
                   WHERE `release_year` = {date}
                   AND `type` LIKE '%{typed}%'
                   AND `listed_in` LIKE '%{genre}%'                    
                   """
        response = cursor.execute(query)
        return dict_by_genre(response)


print(movies_all_types(1963, 'tv show', 'classic'))
