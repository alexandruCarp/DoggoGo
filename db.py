import sqlite3
from flask import current_app, g

def init_db():
    db = sqlite3.connect('sqlite.db',detect_types=sqlite3.PARSE_DECLTYPES)
    f = open('schema.sql')
    db.executescript(f.read())

    ###pentru testare
    db.execute(
        "INSERT INTO dog (breed, photo_path) VALUES (?, ?)",
        ("maidanez","maidanez.jpeg"),
    )
    db.execute(
        "INSERT INTO dog (breed, photo_path) VALUES (?, ?)",
        ("bichon","bichon.jpg"),
    )
    db.execute(
        "INSERT INTO dog (breed, photo_path) VALUES (?, ?)",
        ("caine","caine.jpeg"),
    )
    db.commit()
    ###

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)