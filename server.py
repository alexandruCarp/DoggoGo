from flask import Flask
import os
from sys import argv
import db
import mydogs
import home
import login
import register
import upload

app = Flask(__name__)
app.secret_key = 'dev'
app.config.from_mapping(
    DATABASE='sqlite.db'
)
db.init_app(app)
app.register_blueprint(mydogs.bp)
app.register_blueprint(home.bp)
app.register_blueprint(login.bp)
app.register_blueprint(register.bp)
app.register_blueprint(upload.bp)

if __name__ == "__main__":
    if len(argv) > 1 and argv[1] == "--init":
        for file in os.listdir("static/images"):
            os.remove("static/images/" + file)
        db.init_db()
    
    app.run(host="0.0.0.0", port=3000)