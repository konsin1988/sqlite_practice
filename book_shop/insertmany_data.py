import sqlite3 as sq

# data
authors = [['Булгаков М.А.'], ['Достоевский Ф.М.'], 
  ['Есенин С.А.'], ['Пастернак Б.Л.'], ['Лермонтов М.Ю.']]
genres = [['Роман'], ['Поэзия'], ['Приключения']]
books = [['Мастер и Маргарита', 1, 1, 670.99, 3],
          ['Белая гвардия', 1, 1, 540.50, 5],
          ['Идиот', 2, 1, 460.00, 10],
          ['Братья Карамазовы', 2, 1, 799.01, 2],
          ['Игрок', 2, 1, 480.50, 10],
          ['Стихотворения и поэмы', 3, 2, 650.00, 15],
          ['Черный человек', 3, 2, 570.20, 6],
          ['Лирика', 4, 2, 518.99, 2]]
cities = [['Москва', 5],
          ['Санкт-Петербург', 3],
          ['Владивосток', 12]]
clients = [['Баранов Павел', 3, 'baranov@test'],
          ['Абрамова Катя', 1, 'abramova@test'],
          ['Семенонов Иван', 2, 'semenov@test'],
          ['Яковлева Галина', 1, 'yakovleva@test']]
buys = [['Доставка только вечером', 1],
          ['', 3],
          ['Упаковать каждую книгу по отдельности', 2],
          ['', 1]]
buy_book = [ [1, 1, 1],
          [1, 7, 2],
          [1, 3, 1],
          [2, 8, 2],
          [3, 3, 2],
          [3, 2, 1],
          [3, 1, 1],
          [4, 5, 1]]
steps = [ ['Оплата'],
          ['Упаковка'],
          ['Транспортировка'],
          ['Доставка']]
buy_step = [ [1, 1, '2020-02-20', '2020-02-20'],
          [1, 2, '2020-02-20', '2020-02-21'],
          [1, 3, '2020-02-22', '2020-03-07'],
          [1, 4, '2020-03-08', '2020-03-08'],
          [2, 1, '2020-02-28', '2020-02-28'],
          [2, 2, '2020-02-29', '2020-03-01'],
          [2, 3, '2020-03-02', 'NULL'],
          [2, 4, 'NULL', 'NULL'],
          [3, 1, '2020-03-05', '2020-03-05'],
          [3, 2, '2020-03-05', '2020-03-06'],
          [3, 3, '2020-03-06', '2020-03-10'],
          [3, 4, '2020-03-11', 'NULL'],
          [4, 1, '2020-03-20', 'NULL'],
          [4, 2, 'NULL', 'NULL'],
          [4, 3, 'NULL', 'NULL'],
          [4, 4, 'NULL', 'NULL']]


# executemany
with sq.connect('book.db') as connect:
    cur = connect.cursor()
    cur.executemany('''INSERT INTO author(name_author) VALUES(?)''', authors)
    cur.executemany('''INSERT INTO genre(name_genre)
  VALUES(?);''', genres)
    cur.executemany('''INSERT INTO book(title, author_id, genre_id, price, amount)
  VALUES(?, ?, ?, ?, ?);''', books)
    cur.executemany('''INSERT INTO city(name_city, days_delivery)
  VALUES(?, ?);''', cities)
    cur.executemany('''INSERT INTO client(name_client, city_id, email)
  VALUES(?, ?, ?);''', clients)
    cur.executemany('''INSERT INTO buy(buy_description, client_id) VALUES(?, ?);''', buys)
    cur.executemany('''INSERT INTO buy_book(buy_id, book_id, amount)
  VALUES(?,?,?);''', buy_book)
    cur.executemany('''INSERT INTO step(name_step)
  VALUES(?);''', steps)
    cur.executemany('''INSERT INTO buy_step(buy_id, step_id, date_step_beg, date_step_end)
  VALUES(?, ?, ?, ?);''', buy_step)