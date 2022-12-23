from flask import Blueprint
from flask import render_template
from flask import session
from flask import g
from flask import request
from flask import redirect
from flask import url_for

bp = Blueprint("login",__name__)


@bp.before_app_request
def load_logged_in_user():

    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = {"username": "test"} #de schimbat

@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        session.clear()
        session["user_id"] = 1234
        return redirect(url_for("home.home"))
    return render_template("login.html")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))