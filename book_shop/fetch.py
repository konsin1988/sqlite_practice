import sqlite3 as sq
days = 0

# В таблице city для каждого города указано количество дней, 
# за которые заказ может быть доставлен в этот город 
# (рассматривается только этап Транспортировка). 
# Для тех заказов, которые прошли этап транспортировки, 
# вывести количество дней за которое заказ 
# реально доставлен в город. 
# А также, если заказ доставлен с опозданием, 
# указать количество дней задержки, 
# в противном случае вывести 0. 
# В результат включить номер заказа (buy_id), 
# а также вычисляемые столбцы 
# Количество_дней и Опоздание. 
# Информацию вывести в отсортированном по номеру заказа виде. 
with sq.connect('book.db') as con:
    cur = con.cursor()
    cur.execute('''
        SELECT buy.buy_id, Cast((JulianDay(date_step_end) - JulianDay(date_step_beg)) As Integer) AS 'Количество_дней', CASE WHEN (Cast((JulianDay(date_step_end) - JulianDay(date_step_beg)) As Integer)) - city.days_delivery > 0 THEN (Cast((JulianDay(date_step_end) - JulianDay(date_step_beg)) As Integer)) - city.days_delivery ELSE 0 END AS 'Опоздание'
        FROM buy 
            INNER JOIN buy_step ON buy.buy_id = buy_step.buy_id AND date_step_beg != 'NULL' AND date_step_end != 'NULL' AND name_step = 'Транспортировка'
            INNER JOIN step USING(step_id)
            INNER JOIN client USING(client_id)
            INNER JOIN city USING(city_id)
        ORDER BY buy.buy_id
    ''')
    books = cur.fetchall()

print(books)