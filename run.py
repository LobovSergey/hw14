from flask import Flask, redirect, url_for

from app.genre_bp.views_genre import genre_page
from app.movie_bp.views_movie import movie_page
from app.rating_bp.view_rating import rating_page

app = Flask(__name__)
app.register_blueprint(movie_page)
app.register_blueprint(rating_page)
app.register_blueprint(genre_page)


@app.get('/')
def redirect_main_page():
    return redirect(url_for('movie_page.movie_main'), code=302)


@app.errorhandler(404)
def abort(error):
    return 'Page not found'


if __name__ == '__main__':
    app.run(debug=True)
