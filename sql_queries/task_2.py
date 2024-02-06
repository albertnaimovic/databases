# Sukurti programą, kuri:
# 1. Sukurtų duomenų bazę
# 2. Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojais ir trukme
# 3. Sukurkite atskirą skriptą, kuris sugeneruotų įrašus atsitiktinę tvarka. reikia, kad sukurtų 1000 įrašų.
#     Tokių kaip ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80). studijų trukmė gali būto tarp 200-1000 valandų, suapvalinus iki 100.
# 5. Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 250
# 6. Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
# 7. Ištrintų paskaitą, kurios dėstytojas – „Tomas“
# 8. Atspausdintų visas paskaitas (visą lentelę)


import sqlite3, random

conn = sqlite3.connect("paskaitos.db")


def create_db(conn):
    c = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS paskaitos (
        pavadinimas VARCHAR(50),
        destytojas VARCHAR(50),
        trukme INT
    );
    """
    with conn:
        c.execute(query)

    print("DB ir lenta sukurta.")


def generate_records(conn):
    c = conn.cursor()
    names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Henry",
        "Ivy",
        "Jack",
        "Kate",
        "Liam",
        "Mia",
        "Noah",
        "Olivia",
        "Peter",
        "Quinn",
        "Ryan",
        "Sophia",
        "Thomas",
        "Uma",
        "Victor",
        "Wendy",
        "Xavier",
        "Yara",
        "Zoe",
        "Tomas",
    ]
    lectures = [
        "Python",
        "Java",
        "C++",
        "Matematika",
        "Biologija",
        "Fizika",
        "Daile",
        "Tikyba",
        "Duomenu bazes",
    ]

    with conn:
        for x in range(1000):
            c.execute(
                f"INSERT INTO paskaitos VALUES ('{random.choice(lectures)}', '{random.choice(names)}', {random.randint(2, 11) * 100})"
            )


def get_lectures_above_250(conn):
    c = conn.cursor()

    with conn:
        c.execute("SELECT * From paskaitos WHERE trukme > 250")
        print(c.fetchall())


def update_python_name(conn):
    c = conn.cursor()

    with conn:
        c.execute(
            "UPDATE paskaitos SET pavadinimas = 'Python paskaitos' WHERE pavadinimas = 'Python'"
        )


def delete_tomas_lectures(conn):
    c = conn.cursor()

    with conn:
        c.execute("DELETE FROM paskaitos WHERE destytojas = 'Tomas'")
    print(c.rowcount, "record(s) deleted")


def get_all_info(conn):
    c = conn.cursor()

    with conn:
        c.execute("SELECT * FROM paskaitos")
        result = c.fetchall()

    for x in result:
        print(f"Dalykas: {x[0]}, Destytojas: {x[1]}, Trukme: {x[2]}")


# create_db(conn)
# generate_records(conn)
# get_lectures_above_250(conn)
# update_python_name(conn)
# delete_tomas_lectures(conn)
# get_all_info(conn)
