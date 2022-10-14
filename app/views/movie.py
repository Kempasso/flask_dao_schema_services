from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema

movie_ns = Namespace('/movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        a = request.json
        res = tuple(*request.args.items())
        if res:
            movies = movie_service.filter(res)
            return movies_schema.dump(movies), 200
        movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        data = request.values
        new_movie = movie_service.create(data)
        return movie_schema.dump(new_movie), 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        data = dict(request.values)
        data['id'] = movie_id
        movie_service.update(data)
        return 'Успешное изменение', 200

    def patch(self, movie_id):
        data = dict(request.values)
        data['id'] = movie_id
        movie_service.partial_update(data)
        return 'Успешное изменение', 200

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return 'Успешное удаление', 200
