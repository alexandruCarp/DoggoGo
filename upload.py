import os
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.utils import secure_filename
from db import get_db

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

bp = Blueprint("upload",__name__)

@bp.route('/upload', methods=('GET', 'POST'))
def upload():
    error = None
    if request.method == 'POST':
        print(0)
        if 'file' not in request.files:
            return redirect(request.url)
        print(1)
        file = request.files['file']
        print(2)
        dog_breed = request.form['dog_breed']
        print(3)

        if not file or not allowed_file(file.filename):
            error = 'Image is required.\n' + 'Allowed extensions are:' + str(ALLOWED_EXTENSIONS)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join("./static/images/", filename))
            photo_path = filename

        if error is not None:
            flash(error)

        else:
            db = get_db()
            db.execute(
                'INSERT INTO dog (breed, photo_path, user_id)'
                ' VALUES (?, ?, ?)',
                (dog_breed, photo_path, g.user['id'])
            )
            db.commit()
            return redirect(url_for('mydogs.mydogs'))

    return render_template('upload.html', error = error)

@bp.route('/<id>/<file>/delete_pic', methods=('GET', 'POST'))
def delete_pic(id, file):
    db = get_db()
    filename='static/images/' + file

    os.remove(filename)
    db.execute(
        'DELETE FROM dog'
        ' WHERE id=?',
        (id, )
    )
    db.commit()
    return redirect(url_for('mydogs.mydogs'))