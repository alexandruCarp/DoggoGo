DROP TABLE IF EXISTS dog;

CREATE TABLE dog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    breed TEXT NOT NULL,
    photo_path TEXT NOT NULL,
    discovered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    
    -- TODO cand avem databaseu de user
    -- user_id INTEGER NOT NULL,
    -- FOREIGN KEY (user_id) REFERENCES user (id)
);