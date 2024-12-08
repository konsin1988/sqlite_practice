# Представления позволяют создавать виртуальные таблицы, которые являются результатом выполнения SQL-запроса. Это упрощает выполнение сложных запросов. Давайте создадим представление для выбора активных пользователей:

import sqlite3 as sq
with sq.connect('book.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE VIEW IF NOT EXISTS PaidOrders AS
    SELECT * FROM buy_step 
        INNER JOIN step ON step.step_id = buy_step.step_id
        AND step.name_step = 'Оплата' 
        AND date_step_end != 'NULL'
        ''')
    cur.execute('''
        SELECT * FROM PaidOrders
    ''')
    steps = cur.fetchall()

print(steps)

