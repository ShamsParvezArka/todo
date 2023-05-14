from flask import Flask
from flask import render_template
import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM Tasks")
tasks = cursor.fetchall()

app = Flask(__name__)

@app.route('/')
def index(task_list = tasks):
    return render_template('index.html', task = task_list)

connection.commit()
connection.close()
