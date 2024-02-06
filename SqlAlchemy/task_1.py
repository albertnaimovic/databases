import datetime, os, time
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///employees.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Employee(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birthdate = Column(String)
    position = Column(String)
    salary = Column(Float)
    startedAt = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(
        self, name: str, surname: str, birthdate: str, position: str, salary: float
    ) -> None:
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.position = position
        self.salary = salary


# Base.metadata.create_all(engine) # sitas kaip suprantu tik sukurimui



def create_employee():
    os.system("cls")
    print("\nAdding new employee")
    name = str(input("\nEnter name: "))
    surname = str(input("Enter surname: "))
    birthdate = str(input("Enter birthdate: "))
    position = str(input("Enter position: "))
    salary = float(input("Enter salary (€): "))

    new_employee = Employee(name, surname, birthdate, position, salary)
    session.add(new_employee)
    session.commit()
    print(f"\nEmployee {name} {surname} has been added")
    time.sleep(1.5)


def get_employees():
    employees = session.query(Employee).all()

    os.system("cls")
    print("\nEmployees list\n")
    for employee in employees:
        print(
            f"{employee.id}. {employee.name} {employee.surname}, {employee.position}\n   Birthdate: {employee.birthdate}\n   Salary: {employee.salary} €\n"
        )
    input("\n Press enter to continue")


def delete_employee():
    while True:
        os.system("cls")
        id = input("\nEnter ID of employee you want to delete: ")

        try:
            employee = session.query(Employee).filter_by(id=id).one()
        except Exception:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)
            continue
        break

    while True:
        os.system("cls")
        decision = input(
            f"\nDo you want to delete {employee.name} {employee.surname} ?\n\n1. Yes\n2. No\n\n Enter number of selection: "
        )
        if decision.isnumeric() == True:
            if decision == "1":
                session.delete(employee)
                session.commit()
                print(f"\nDELETED")
                time.sleep(1.5)
                break
            elif decision == "2":
                break
            else:
                print("\nThere is no such selection.\n")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces.\n"
            )
            time.sleep(2)


def update_employee():
    while True:
        os.system("cls")
        id = input("\nEnter ID of employee you want to update: ")

        try:
            employee = session.query(Employee).filter_by(id=id).one()
        except Exception:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)
            continue
        break

    while True:
        os.system("cls")
        decision = input(
            f"\nWhat do you want to update in {employee.name} {employee.surname} ?\n\n1. Name\n2. Surname\n3. Birthdate\n4. Position\n5. Salary\n6. Back to main menu\n\n Enter number of selection: "
        )
        if decision.isnumeric() == True:
            if decision == "1":
                name = str(input("\nEnter new name: "))
                employee.name = name
                session.commit()
                print("Employee updated")
                time.sleep(1.5)
                break
            elif decision == "2":
                surname = str(input("\nEnter new surname: "))
                employee.surname = surname
                session.commit()
                print("Employee updated")
                time.sleep(1.5)
                break
            if decision == "3":
                birthdate = str(input("\nEnter new birthdate: "))
                employee.birthdate = birthdate
                session.commit()
                print("Employee updated")
                time.sleep(1.5)
                break
            if decision == "4":
                position = str(input("\nEnter new position: "))
                employee.position = position
                session.commit()
                print("Employee updated")
                time.sleep(1.5)
                break
            if decision == "5":
                salary = float(input("\nEnter new salary: "))
                employee.salary = salary
                session.commit()
                print("Employee updated")
                time.sleep(1.5)
                break
            elif decision == "6":
                break
            else:
                print("\nThere is no such selection.\n")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces.\n"
            )
            time.sleep(2)


def main_menu() -> None:
    while True:
        os.system("cls")
        print("\n----------------\n|--Employees--|\n----------------")
        category: str = input(
            "--Menu--\n1. Add new employee\n2. See employees\n3. Delete employee\n4. Update employee\n5. Exit\n\nEnter number of selection: "
        )
        if category.isnumeric() == True:
            if category == "1":
                create_employee()
            elif category == "2":
                get_employees()
            elif category == "3":
                delete_employee()
            elif category == "4":
                update_employee()
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
