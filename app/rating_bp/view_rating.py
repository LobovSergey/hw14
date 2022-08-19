from flask import Blueprint, jsonify

from main import get_movie_by_rating

rating_page = Blueprint('rating_page', __name__)


@rating_page.get('/rating/<rating_class>')
def movie_rating(rating_class):
    data_from_db = get_movie_by_rating(rating_class)
    return jsonify(data_from_db)
