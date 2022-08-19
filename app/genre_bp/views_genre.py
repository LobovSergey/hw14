from flask import Blueprint, jsonify
from main import get_movie_by_genre

genre_page = Blueprint('genre_page', __name__)


@genre_page.get('/genre/<genre>')
def genre_main(genre):
    origin_title = genre.title()
    data_from_db = get_movie_by_genre(origin_title)
    return jsonify(data_from_db)
