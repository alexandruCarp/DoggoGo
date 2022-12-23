from flask import Blueprint
from flask import g
from db import get_db
from flask import render_template

bp = Blueprint("mydogs",__name__)

@bp.route("/mydogs")
#eventual @login_required
def mydogs():
    db = get_db()
    db.commit()
    dogs = db.execute(
        "SELECT *"
        " FROM dog"
        " ORDER BY discovered DESC"
    ).fetchall()                   # trebuie selectati doar cainii userului curent - de modificat cand avem user
    return render_template("mydogs.html", dogs=dogs)