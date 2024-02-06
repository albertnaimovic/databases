from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Actor, Movie


engine = create_engine("sqlite:///many2many_test.db")
Session = sessionmaker(bind=engine)
session = Session()


actor = session.query(Actor).get(2)

actor.name = "Arnold Schwarzenegger"
movie = Movie(name="Terminator 2")

actor.movies.append(movie)


session.commit()
