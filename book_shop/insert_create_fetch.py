import sqlite3 as sq 

with sq.connect('book.db') as con:
    cur = con.cursor()
    cur.execute('''
INSERT INTO client(name_client, city_id, email)
VALUES('Попов Илья', (
    SELECT city_id
    FROM city
    WHERE name_city = 'Москва'
    ), 'popov@test');''')

    cur.execute('''
INSERT INTO buy(buy_description, client_id)
SELECT 'Связаться со мной по вопросу доставки', client_id 
FROM client
WHERE name_client = 'Попов Илья';''')

    cur.execute('''
INSERT INTO buy_book(buy_id, book_id, amount)
VALUES
  (5, (
    SELECT book_id
    FROM book INNER JOIN author USING(author_id)
    WHERE title='Лирика' AND name_author LIKE 'Пастернак %'
  ), 2),
  (5, (
    SELECT book_id
    FROM book INNER JOIN author USING(author_id)
    WHERE title='Белая Гвардия' AND name_author LIKE 'Булгаков %'
  ), 1
  );''')

    cur.execute('''
  UPDATE book INNER JOIN buy_book ON book.book_id = buy_book.book_id AND buy_id = 5
SET book.amount = book.amount - buy_book.amount;''')

    cur.execute('''
CREATE TABLE buy_pay AS (
  SELECT title, name_author, price, buy_book.amount, price * buy_book.amount AS 'Стоимость'
  FROM book INNER JOIN author USING(author_id)
    INNER JOIN buy_book ON book.book_id = buy_book.book_id AND buy_id = 5
  ORDER BY title
);''')

    cur.execute('''
INSERT INTO buy_step(buy_id, step_id)
SELECT 5, step_id
FROM step;''')

    cur.execute('''
 UPDATE buy_step 
  INNER JOIN step ON step.step_id = buy_step.step_id 
    AND buy_step.step_id = 1 
    AND buy_step.buy_id = 5
SET date_step_beg = '2020.04.12';''')

    cur.execute('''
UPDATE buy_step
  JOIN (
    SELECT @step := step.step_id, @date := '2020.04.13', @next_step := step.step_id + 1
    FROM step 
    WHERE name_step = 'Оплата'
  ) var
  INNER JOIN step ON step.step_id = buy_step.step_id
  AND buy_id = 5
SET date_step_end = IF(buy_step.step_id = @step, @date, date_step_end),
  date_step_beg = IF(buy_step.step_id = @next_step, @date, date_step_beg);''')