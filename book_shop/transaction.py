import sqlite3

authors = 0
books = 0

with sqlite3.connect('book.db') as con:
    cur = con.cursor()

    try:
        cur.execute('BEGIN')
        cur.execute('''INSERT INTO author(name_author) VALUES('Братья Стругацкие')''')
        cur.execute('''SELECT name_author FROM author''')
        authors = cur.fetchall()
        cur.execute('''SELECT title9 FROM book''')
        books = cur.fetchall()
    
    except:
        cur.execute('ROLLBACK')

print(authors)
print()
print(books)
print()

with sqlite3.connect('book.db') as con:
    cur = con.cursor()

    cur.execute('''SELECT name_author FROM author''')
    authors = cur.fetchall()

print(authors)

