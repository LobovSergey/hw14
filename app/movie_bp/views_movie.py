from flask import Blueprint, jsonify

from main import get_movie_by_title, get_movie_by_date

movie_page = Blueprint('movie_page', __name__)


@movie_page.get('/movie/')
def movie_main():
    return f' <h2>Start enter your movie in URL after /</h2>'


@movie_page.get('/movie/<title>')
def movie_title(title):
    origin_title = title.title()
    data_from_db = get_movie_by_title(origin_title)
    return jsonify(data_from_db)


@movie_page.get('/movie/<int:year_one>/to/<int:year_two>')
def movie_date(year_one, year_two):
    data_from_db = get_movie_by_date(year_one, year_two)
    return jsonify(data_from_db)






