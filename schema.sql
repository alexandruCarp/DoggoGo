DROP TABLE IF EXISTS dog;
DROP TABLE IF EXISTS user;

CREATE TABLE dog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    breed TEXT NOT NULL,
    photo_path TEXT NOT NULL,
    discovered TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime')),
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)

);

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);