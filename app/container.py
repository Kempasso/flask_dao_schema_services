from app.dao.director_dao import DirectorDAO
from app.dao.genre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO

from app.database import db
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)


genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)