from flask import Blueprint
from flask import render_template

bp = Blueprint("home",__name__)

@bp.route("/")
def home():
    return render_template("home.html")