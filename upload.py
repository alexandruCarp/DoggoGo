from flask import Blueprint
from flask import render_template

bp = Blueprint("upload",__name__)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO dog (breed, photo_path, user_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['user_id'])
            )
            db.commit()
            return redirect(url_for('app.home'))

    return render_template('upload.html')
