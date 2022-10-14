from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def filter(self, value):
        try:
            result = self.session.query(Movie).filter(Movie.__dict__[value[0]] == value[1])
        except Exception as e:
            all_movies = self.session.query(Movie).all()
            return all_movies
        return result

    def get_all(self):
        result = self.session.query(Movie).all()
        return result

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie_id):
        movie = self.get_one(movie_id)
        self.session.delete(movie)
        self.session.commit()
