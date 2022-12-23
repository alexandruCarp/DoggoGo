from flask import Blueprint
from flask import render_template

bp = Blueprint("upload",__name__)

@bp.route("/upload")
def upload():
    return render_template("upload.html")