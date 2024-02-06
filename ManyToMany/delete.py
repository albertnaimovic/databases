from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Actor, Movie


engine = create_engine("sqlite:///many2many_test.db")
Session = sessionmaker(bind=engine)
session = Session()

actor = session.query(Actor).get(4)
session.delete(actor)
session.commit()
