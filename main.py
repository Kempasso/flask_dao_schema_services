from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.director import director_ns
from app.views.genre import genre_ns
from app.views.movie import movie_ns


def create_app(config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def set_configs(application):
    api = Api(app)
    db.init_app(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)

def get_data():
    db.create_all()


if __name__ == '__main__':
    configs = Config()
    app = create_app(configs)
    set_configs(app)
    get_data()
    app.run(debug=True)
