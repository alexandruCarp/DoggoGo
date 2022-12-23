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

bp = Blueprint("register",__name__)


@bp.route("/register", methods=("GET", "POST"))
def register():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("home.home"))

        flash(error)

    return render_template("register.html",error = error)
