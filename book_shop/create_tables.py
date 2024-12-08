import sqlite3
connect = sqlite3.connect('book.db')
cursor = connect.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS author(author_id INTEGER PRIMARY KEY AUTOINCREMENT, name_author TEXT);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS genre(genre_id INTEGER PRIMARY KEY AUTOINCREMENT, name_genre TEXT);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT, 
  author_id INTEGER NOT NULL, 
  genre_id INTEGER NOT NULL, 
  price REAL,
  amount INTEGER,
  FOREIGN KEY(author_id) REFERENCES author(author_id),
  FOREIGN KEY(genre_id) REFERENCES genre(genre_id)
  );''')
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS city(city_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name_city TEXT, days_delivery INTEGER);
  ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS client(client_id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name_client TEXT, 
  city_id INTEGER NOT NULL,
  email TEXT,
  FOREIGN KEY(city_id) REFERENCES city(city_id)
  );
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS buy(buy_id INTEGER PRIMARY KEY AUTOINCREMENT, buy_description TEXT,
  client_id INTEGER NOT NULL,
  FOREIGN KEY(client_id) REFERENCES client(client_id)
  );
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS step(
  step_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_step TEXT
  );
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS buy_book(
  buy_book_id INTEGER PRIMARY KEY AUTOINCREMENT,
  buy_id INTEGER NOT NULL,
  book_id INTEGER NOT NULL,
  amount INTEGER,
  FOREIGN KEY(buy_id) REFERENCES buy(buy_id),
  FOREIGN KEY(book_id) REFERENCES book(book_id)
  );
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS buy_step(
  buy_step_id INTEGER PRIMARY KEY AUTOINCREMENT,
  buy_id INTEGER NOT NULL,
  step_id INTEGER NOT NULL,
  date_step_beg TEXT,
  date_step_end TEXT,
  FOREIGN KEY(buy_id) REFERENCES buy(buy_id),
  FOREIGN KEY(step_id) REFERENCES step(step_id)
  );
''')


connect.commit()
connect.close()