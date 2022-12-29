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
        " WHERE user_id= ? "
        " ORDER BY discovered DESC",
        (g.user["id"],)
    ).fetchall()
    return render_template("mydogs.html", dogs=dogs)