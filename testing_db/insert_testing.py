import sqlite3
connect = sqlite3.connect('testing.db')
cursor = connect.cursor()

# В таблицу attempt включить новую 
# попытку для студента Баранова Павла 
# по дисциплине «Основы баз данных». 
# Установить текущую дату 
# в качестве даты выполнения попытки.

# cursor.execute('''INSERT INTO attempt (student_id, subject_id, date_attempt)
# SELECT student_id, subject_id, DATE('now') 
# FROM student 
#     INNER JOIN attempt USING(student_id)
#     INNER JOIN subject USING(subject_id)
# WHERE name_student = 'Баранов Павел' AND name_subject = 'Основы баз данных';''')

# ---------------------------------------------------

# Случайным образом выбрать три вопроса (запрос) по дисциплине, 
# тестирование по которой собирается проходить студент, 
# занесенный в таблицу attempt последним, и добавить 
# их в таблицу testing. id последней попытки получить 
# как максимальное значение id из таблицы attempt.

# cursor.execute('''
#     INSERT INTO testing(attempt_id, question_id)
# SELECT query_1.attempt_id, query_1.question_id
# FROM
# (SELECT attempt_id, question_id
# FROM question 
#     JOIN attempt ON question.subject_id = attempt.subject_id
#     AND attempt_id = (
#         SELECT MAX(attempt_id)
#         FROM attempt
#         )
# ORDER BY RANDOM()
# LIMIT 3) as query_1;

# ''')

#-----------------------------------------------------------

# Пополнение таблицы testng, студент прошёл тестирование
# cursor.execute('''
#     UPDATE testing
#     SET answer_id = 19
#     WHERE testing_id = 22
# ''')
# cursor.execute('''
#     UPDATE testing
#     SET answer_id = 17
#     WHERE testing_id = 23
# ''')
# cursor.execute('''
#     UPDATE testing
#     SET answer_id = 22
#     WHERE testing_id = 24
# ''')

#-----------------------------------------------------------

# Студент прошел тестирование (то есть все его ответы занесены 
# в таблицу testing), далее необходимо вычислить результат(запрос) 
# и занести его в таблицу attempt для соответствующей попытки.  
# Результат попытки вычислить как количество правильных ответов, 
# деленное на 3 (количество вопросов в каждой попытке) 
# и умноженное на 100. Результат округлить до целого.

#  Будем считать, что мы знаем id попытки,  
#  для которой вычисляется результат, в нашем 
#  случае это 8. В таблицу testing занесены 
#  следующие ответы пользователя: (19, 17, 22, смотри код выше)

# cursor.execute('''
#     UPDATE attempt
#     SET result = 
#     (SELECT CAST(ROUND(CAST(SUM(is_correct) AS REAL) / COUNT(is_correct) * 100) AS INTEGER) AS result_number
# FROM answer 
#     INNER JOIN testing ON answer.answer_id = testing.answer_id
#     AND testing_id IN (
#         SELECT testing_id 
#         FROM testing
#         WHERE attempt_id = 8)
# GROUP BY attempt_id)
#     WHERE attempt_id = 8;
# ''')

# ------------------------------------------------------

# Удалить из таблицы attempt все попытки, 
# выполненные раньше 1 мая 2020 года. 
# Также удалить и все соответствующие этим 
# попыткам вопросы из таблицы testing, 
# которая создавалась следующим запросом:

# CREATE TABLE testing (
#     testing_id INT PRIMARY KEY AUTO_INCREMENT, 
#     attempt_id INT, 
#     question_id INT, 
#     answer_id INT,
#     FOREIGN KEY (attempt_id)  
#     REFERENCES attempt (attempt_id) ON DELETE CASCADE
# );



cursor.execute('''SELECT * FROM attempt''')
print(*cursor.fetchall())


connect.commit()
connect.close()