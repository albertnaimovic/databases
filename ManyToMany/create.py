from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Actor, Movie


engine = create_engine("sqlite:///many2many_test.db")
Session = sessionmaker(bind=engine)
session = Session()

actor_1 = Actor(name="Stalone")
actor_2 = Actor(name="Schwarzenegger")

movie_1 = Movie(name="Rocky", genre="Drama")
movie_2 = Movie(name="Terminator", genre="Action")
movie_3 = Movie(name="The Expendables", genre="Action")

movie_1.actors.append(actor_1)
movie_2.actors.append(actor_2)
movie_3.actors.append(actor_1)
movie_3.actors.append(actor_2)


session.add(actor_1)
session.add(actor_2)

session.commit()
