from flask import Flask, g, render_template
import sqlite3
import os

app = Flask(__name__)
app.config.from_object('settings')

@app.before_request
def setup_db():
    if getattr(g, "db", None) is None:
        g.db = sqlite3.connect(app.config['DBFILE'])

@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, "db", None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', '8080'))
    app.run('127.0.0.1', port)
