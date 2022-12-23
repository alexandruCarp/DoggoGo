from flask import Blueprint
from flask import render_template

bp = Blueprint("register",__name__)

@bp.route("/register")
def register():
    return render_template("register.html")