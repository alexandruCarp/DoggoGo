from flask import Blueprint
from flask import render_template
from db import get_db

bp = Blueprint("home",__name__)

@bp.route("/")
def home():
    db = get_db()
    db.commit()
    discoveries = db.execute(
        "SELECT *"
        " FROM dog"
        " ORDER BY discovered DESC"
        " LIMIT 3"
    ).fetchall()
    users={}
    for disc in discoveries:
        users[disc['user_id']] = db.execute(
            " SELECT username "
            " FROM user "
            " WHERE id = ? ",
            (disc['user_id'],)
        ).fetchall()[0]

    return render_template("home.html", discoveries=discoveries, users=users)