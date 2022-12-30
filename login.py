import functools
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from db import get_db
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

bp = Blueprint("login",__name__)

def login_required(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("home.home"))

        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():

    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
         g.user = get_db().execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()
@bp.route("/login", methods=("GET", "POST"))
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username or password."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect username or password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("home.home"))

        flash(error)

    return render_template("login.html",error = error)


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))