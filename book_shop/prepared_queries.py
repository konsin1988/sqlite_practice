import sqlite3
con = sqlite3.connect('book.db')
cur = con.cursor()

query = '''SELECT title, amount FROM book 
        WHERE amount >= ?'''
cur.execute(query, (8,))
books = cur.fetchall()

con.close()
print(books)