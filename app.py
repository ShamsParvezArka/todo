from flask import Flask
from flask import request
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def update():
    if request.method == 'POST':
        task = request.form.get('box')

        connection = sqlite3.connect('tasks.db')
        cursor = connection.cursor()
        query = "INSERT INTO Tasks VALUES ('{T}')".format(T = task)
        cursor.execute(query)

        connection.commit()
        connection.close()
    return main()
