import sqlite3

#connect to a database
connection = sqlite3.connect('task3.db')
cursor = connection.cursor()

#create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS  audience (id INTEGER PRIMARY KEY, name TEXT, place TEXT)''')


 
#Insert data into table
cursor.execute("INSERT INTO audience (id, name, place) VALUES (34236, 'Sony', 'Florida')")
cursor.execute("INSERT INTO audience (id, name, place) VALUES (98745, 'Dharma', 'Chicago')")
cursor.execute("INSERT INTO audience (id, name, place) VALUES (?, ?, ?)", (74536, 'Chimpu', 'Newyork'))


#Fetch and display all data
cursor.execute("SELECT * FROM audience")
rows = cursor.fetchall()
for row in rows:
    print(row)

#error handling
try:
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
    print(f"An error occurred:{e}")


#commiting and closing the connection
connection.commit()
connection.close()
