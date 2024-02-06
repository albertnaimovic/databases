import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///projektai.db")
Base = declarative_base()


class Projektas(Base):
    __tablename__ = "Projektas"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    createdAt = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.createdAt}"


Base.metadata.create_all(engine)
