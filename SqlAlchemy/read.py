from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Projektas

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()

project = session.query(Projektas).get(1)

print(project.name)

project2 = session.query(Projektas).filter_by(name="2 projektas").one()

print(project2)

projektai = session.query(Projektas).all()

for projektas in projektai:
    print(projektas.name, projektas.price)
# Naujas pr. 20000.0
# 2 projektas 55000.0