DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	name							TEXT	NOT NULL,
    von								INT,
    bis								INT,
    nachname						TEXT    NOT NULL,
    kw								INT,
    user_stunden_montag				INT,
    user_beschreibung_montag		TEXT    NOT NULL,
    user_stunden_dienstag			INT,
    user_beschreibung_dienstag		TEXT    NOT NULL,
    user_stunden_mittwoch			INT,
    user_beschreibung_mittwoch		TEXT    NOT NULL,
    user_stunden_Donnerstag			INT,
    user_beschreibung_Donnerstag	TEXT    NOT NULL,
    user_stunden_freitag			INT,
    user_beschreibung_freitag		TEXT    NOT NULL


);



/* DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
); */