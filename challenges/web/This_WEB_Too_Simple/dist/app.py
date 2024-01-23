from flask import Flask, request, g
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cur = get_db().cursor()
        cur.execute(query)
        result = cur.fetchone()
        

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


DATABASE = './database.db'
