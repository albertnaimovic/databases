import sqlite3

conn = sqlite3.connect('zmones.db')
c = conn.cursor()


with conn:
    c.execute("INSERT INTO draugai VALUES ('Domantas', 'Rutkauskas', 'd.rutkauskas@imone.lt')")
    c.execute("INSERT INTO draugai VALUES ('Rimas', 'Radzevičius', 'RR@gmail.com')")

# query = '''
# CREATE TABLE IF NOT EXISTS draugai (
#     f_name VARCHAR(50),
#     l_name VARCHAR(50),
#     email VARCHAR(100)
# );
# '''


# query = '''
# INSERT INTO draugai (f_name, l_name, email) 
# VALUES ("Jonas", "Viršaitis", "ponasjonas@gmail.com");
# '''


# c.execute(query)

# conn.commit()
# conn.close()