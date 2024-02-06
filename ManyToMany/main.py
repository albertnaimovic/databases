from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///many2many_test.db")
Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("movie_id", Integer, ForeignKey("movie.id")),
    Column("actor_id", Integer, ForeignKey("actor.id")),
)


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    actors = relationship("Actor", secondary=association_table, back_populates="movies")


class Actor(Base):
    __tablename__ = "actor"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    movies = relationship("Movie", secondary=association_table, back_populates="actors")


Base.metadata.create_all(engine)


# https://github.com/DonatasNoreika/Python-pamokos/wiki/ORM-(sqlalchemy)-II-dalis
