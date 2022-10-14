from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('/genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200
