import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()


connection.commit()
connection.close()
