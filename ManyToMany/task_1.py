from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os, time

engine = create_engine("sqlite:///task_1.db")
Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    person_code = Column(Integer)
    phone = Column(Integer)


class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    bank_code = Column(Integer)
    swift = Column(Integer)


class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    balance = Column(Float)
    person_id = Column(Integer, ForeignKey("person.id"))
    person = relationship("Person")
    bank_id = Column(Integer, ForeignKey("bank.id"))
    bank = relationship("Bank")


# Base.metadata.create_all(engine)


def main_menu() -> None:
    while True:
        os.system("cls")
        print("\n----------------\n|--Bank--|\n----------------")
        category: str = input(
            "--Menu--\n1. Create bank, account or person\n2. View your account \n3. See all info\n4. Add or take your money\n5. Exit\n\nEnter number of selection: "
        )
        if category.isnumeric() == True:
            if category == "1":
                pass
            elif category == "2":
                pass
            elif category == "3":
                pass
            elif category == "4":
                pass
            elif category == "5":
                print("\nBye.")
                break
            else:
                print("\nThere is no such selection")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)


main_menu()
