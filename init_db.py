import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

cur.execute("INSERT INTO posts (name, von, bis, nachname, kw, user_stunden_montag, user_beschreibung_montag, user_stunden_dienstag, user_beschreibung_dienstag, user_stunden_mittwoch, user_beschreibung_mittwoch, user_stunden_donnerstag, user_beschreibung_donnerstag, user_stunden_freitag, user_beschreibung_freitag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Luwey', '12', '19', 'Silva', '33', '8', 'Luwey', '8', 'Luwey', '8', 'Luwey', '8', 'Luwey', '8', 'Luwey')
            )

cur.execute("INSERT INTO posts (name, von, bis, nachname, kw, user_stunden_montag, user_beschreibung_montag, user_stunden_dienstag, user_beschreibung_dienstag, user_stunden_mittwoch, user_beschreibung_mittwoch, user_stunden_donnerstag, user_beschreibung_donnerstag, user_stunden_freitag, user_beschreibung_freitag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Sidney', '12', '19', 'Silva', '33', '8', 'Luwey', '8', 'Luwey', '8', 'Luwey', '8', 'Luwey', '8', 'Luwey')
            )


connection.commit()
connection.close()