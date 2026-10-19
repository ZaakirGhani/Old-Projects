import sqlite3

conn = sqlite3.connect('hospital.db')
c = conn.cursor()

#c.execute('''CREATE TABLE patients (
#          name text,
 #         age integer,
  #        gender text,
   #       diagnosis text,
    #      treatment text)''')

c.execute("SELECT * FROM patients")

print(c.fetchall())

conn.commit()
conn.close()