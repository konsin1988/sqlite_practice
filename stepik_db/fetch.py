import sqlite3
import re

def match(expr, item):
    return re.search(expr, item) is not None




connection = sqlite3.connect('stepik.db')
connection.create_function('regexp', 2, match)
cursor = connection.cursor()




#  Отобрать все шаги, в которых рассматриваются вложенные запросы (то есть в названии шага упоминаются вложенные запросы). Указать к какому уроку и модулю они относятся. Для этого вывести 3 поля:

#     в поле Модуль указать номер модуля и его название через пробел;
#     в поле Урок указать номер модуля, порядковый номер урока (lesson_position) через точку и название урока через пробел;
#     в поле Шаг указать номер модуля, порядковый номер урока (lesson_position) через точку, порядковый номер шага (step_position) через точку и название шага через пробел.

# Длину полей Модуль и Урок ограничить 19 символами, при этом слишком длинные надписи обозначить многоточием в конце (16 символов - это номер модуля или урока, пробел и  название Урока или Модуля,к ним присоединить "..."). Информацию отсортировать по возрастанию номеров модулей, порядковых номеров уроков и порядковых номеров шагов.

# cursor.execute('''
#     SELECT CONCAT(SUBSTR(CONCAT(module_id, ' ', module_name),1, 16), '...') AS 'Модуль', 
#     CONCAT(SUBSTR(CONCAT(module_id, '.', lesson_position, ' ', lesson_name), 1, 16), '...') AS 'Урок',
#     CONCAT(module_id, '.', lesson_position, '.', step_position, ' ', step_name) AS 'Шаг'
# FROM step 
#     JOIN lesson USING(lesson_id)
#     JOIN module USING(module_id)
# WHERE step_name REGEXP '(?i)реляционн'
# /*'[Вв]ложенн(ы([йехм]|ми)|о(го|му|м)) запрос'*/
# ORDER BY Шаг;
# ''')

# print(*[x[0] for x in cursor.fetchall()], sep='\n')

#----------------------------------------------------------------------
# Заполнить таблицу step_keyword следующим образом: 
# если ключевое слово есть в названии шага, то включить 
# в step_keyword строку с id шага и id ключевого слова. 


# cursor.execute('''
#     INSERT INTO step_keyword (step_id, keyword_id)
#     SELECT (step_id, keyword_id)
#     FROM keyword, step
#     WHERE step_id = ANY(SELECT step_id FROM step 
#     WHERE step_name REGEXP (CONCAT('(?i)\\b', keyword_name, '\\b')));
# ''')

# print(*[x[0] for x in cursor.fetchall()], sep='\n')

# ---------------------------------------------------------------------
# Реализовать поиск по ключевым словам. Вывести шаги, 
# с которыми связаны ключевые слова MAX и AVG одновременно. 
# Для шагов указать id модуля, позицию урока в модуле, 
# позицию шага в уроке через точку, после позиции шага 
# перед заголовком - пробел. Позицию шага в уроке вывести 
# в виде двух цифр (если позиция шага меньше 10, то перед 
# цифрой поставить 0). Столбец назвать Шаг. Информацию 
# отсортировать по первому столбцу в алфавитном порядке.

# cursor.execute('''
#     SELECT CONCAT(
#         module_id, '.', 
#         lesson_position, '.',
#         CASE WHEN step_position > 10 THEN step_position ELSE  CONCAT('0', step_position) END, ' ',
#         step_name) AS 'Шаг'
# FROM step
#     JOIN lesson USING(lesson_id)
#     JOIN module USING(module_id)
#     JOIN step_keyword USING(step_id)
#     JOIN keyword USING(keyword_id)
# WHERE keyword_name = 'MAX' OR keyword_name = 'AVG'
# GROUP BY Шаг
# HAVING COUNT(Шаг) > 1
# ORDER BY Шаг
# ''')



# -------------------------------------------------------------
# Посчитать, сколько студентов относится к каждой группе. 
# Столбцы назвать Группа, Интервал, Количество. 
# Указать границы интервала.
# cursor.execute('''
#     SELECT Группа, 
#         CASE
#             WHEN Группа = 'I' THEN 'от 0 до 10'
#             WHEN Группа = 'II' THEN 'от 11 до 15'
#             WHEN Группа = 'III' THEN 'от 16 до 27'
#             WHEN Группа = 'IV' THEN 'больше 27'
#         END AS 'Интервал',    
#         COUNT(student_name) AS Количество
# FROM (
#     SELECT student_name, rate, 
#     CASE
#         WHEN rate <= 10 THEN "I"
#         WHEN rate <= 15 THEN "II"
#         WHEN rate <= 27 THEN "III"
#         ELSE "IV"
#     END AS Группа
# FROM      
#     (
#      SELECT student_name, count(*) as rate
#      FROM 
#          (
#           SELECT student_name, step_id
#           FROM 
#               student 
#               INNER JOIN step_student USING(student_id)
#           WHERE result = "correct"
#           GROUP BY student_name, step_id
#          ) query_in
#      GROUP BY student_name 
#      ORDER BY 2
#     ) query_in_1
# ) query_in_2
# GROUP BY Группа;
# ''')

print(*[x[0] for x in cursor.fetchall()], sep='\n')

connection.commit()
connection.close()