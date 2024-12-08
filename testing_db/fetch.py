import sqlite3

connect = sqlite3.connect('testing.db')
cursor = connect.cursor()

# Вывести студентов, которые сдавали дисциплину 
# «Основы баз данных», указать дату попытки и результат. 
# Информацию вывести по убыванию результатов тестирования.
cursor.execute('''
    SELECT name_student, date_attempt, result
FROM student 
    INNER JOIN attempt USING(student_id)
    INNER JOIN subject ON subject.subject_id = attempt.subject_id 
    AND name_subject = 'Основы баз данных'
ORDER BY result DESC
''')
print('name_student, date_attempt, result')
print(*cursor.fetchall(), sep='\n')
print()

# Вывести, сколько попыток сделали студенты по каждой дисциплине, 
# а также средний результат попыток, который округлить 
# до 2 знаков после запятой. Под результатом 
# попытки понимается процент правильных ответов 
# на вопросы теста, который занесен в столбец result.  
# В результат включить название дисциплины, 
# а также вычисляемые столбцы Количество и Среднее. 
# Информацию вывести по убыванию средних результатов.
cursor.execute('''
    SELECT name_subject, COUNT(attempt.subject_id) AS 'Количество', ROUND(AVG(attempt.result), 2) AS 'Среднее'
FROM subject 
    LEFT JOIN attempt USING(subject_id)
GROUP BY subject.subject_id
ORDER BY Среднее DESC;
''')
print(*cursor.fetchall(), sep='\n')
print()

# Вывести студентов (различных студентов), 
# имеющих максимальные результаты попыток. 
# Информацию отсортировать в алфавитном 
# порядке по фамилии студента.
cursor.execute('''
    SELECT name_student, result
FROM student
    INNER JOIN attempt ON student.student_id = attempt.student_id
    AND result = (
        SELECT result
        FROM attempt
        ORDER BY result DESC
        LIMIT 1
        )
    ORDER BY name_student
''')
print(*cursor.fetchall(), sep='\n')
print()

# Если студент совершал несколько попыток по одной 
# и той же дисциплине, то вывести разницу 
# в днях между первой и последней попыткой. 
# В результат включить фамилию и имя студента, 
# название дисциплины и вычисляемый столбец Интервал. 
# Информацию вывести по возрастанию разницы. 
# Студентов, сделавших одну попытку по дисциплине, не учитывать. 
cursor.execute('''
    SELECT name_student, name_subject,  CAST(julianday(MAX(date_attempt)) - julianday(MIN(date_attempt)) AS INTEGER) AS 'Интервал'
FROM student
  INNER JOIN attempt ON student.student_id = attempt.student_id
  INNER JOIN subject ON
subject.subject_id = attempt.subject_id
GROUP BY name_student, name_subject
HAVING COUNT(attempt.subject_id)>1
ORDER BY Интервал
''')
print(*cursor.fetchall(), sep='\n')
print()

# Студенты могут тестироваться по одной или 
# нескольким дисциплинам (не обязательно по всем). 
# Вывести дисциплину и количество уникальных студентов 
# (столбец назвать Количество), которые по ней проходили тестирование . 
# Информацию отсортировать сначала по убыванию количества, 
# а потом по названию дисциплины. В результат включить и дисциплины, 
# тестирование по которым студенты не проходили, 
# в этом случае указать количество студентов 0.
cursor.execute('''
    SELECT name_subject, COUNT(DISTINCT student_id) AS 'Количество'
FROM subject 
    LEFT JOIN attempt USING(subject_id)
GROUP BY name_subject
ORDER BY Количество DESC, name_subject;
''')
print(*cursor.fetchall(), sep='\n')
print()

# Случайным образом отберите 3 вопроса по 
# дисциплине «Основы баз данных». 
# В результат включите столбцы 
# question_id и name_question.
cursor.execute('''
SELECT question_id, name_question 
FROM question
    LEFT JOIN subject ON subject.subject_id = question.subject_id
    AND name_subject = 'Основы баз данных'
ORDER BY RANDOM()
LIMIT 3
''')
print(*cursor.fetchall(), sep='\n')
print()

# Вывести вопросы, которые были включены в тест для 
# Семенова Ивана по дисциплине «Основы SQL» 2020-05-17  
# (значение attempt_id для этой попытки равно 7). 
# Указать, какой ответ дал студент и правильный он 
# или нет(вывести Верно или Неверно). 
# В результат включить вопрос, ответ и 
# вычисляемый столбец  Результат.
cursor.execute('''
    SELECT name_question, name_answer, CASE WHEN is_correct = True THEN 'Верно' ELSE 'Неверно' END AS 'Результат'
FROM answer 
    INNER JOIN testing ON answer.answer_id = testing.answer_id
    INNER JOIN question ON question.question_id = testing.question_id
    INNER JOIN subject ON subject.subject_id = question.subject_id
    AND name_subject = 'Основы SQL'
    INNER JOIN attempt ON attempt.attempt_id = testing.attempt_id
    AND date_attempt = '2020-05-17'
    INNER JOIN student ON student.student_id = attempt.student_id
    AND name_student = 'Семенов Иван'
''')
print(*cursor.fetchall(), sep='\n')
print()

# Посчитать результаты тестирования. 
# Результат попытки вычислить как количество 
# правильных ответов, деленное на 3 
# (количество вопросов в каждой попытке) 
# и умноженное на 100. Результат округлить 
# до двух знаков после запятой. 
# Вывести фамилию студента, название предмета, 
# дату и результат. Последний столбец 
# назвать Результат. Информацию отсортировать 
# сначала по фамилии студента, потом 
# по убыванию даты попытки.
cursor.execute('''
    SELECT name_student, name_subject, date_attempt, ROUND((SUM(is_correct)/3.0) * 100, 2) AS 'Результат'
FROM student 
    INNER JOIN attempt USING(student_id)
    INNER JOIN subject USING(subject_id)
    INNER JOIN testing USING(attempt_id)
    INNER JOIN question USING(question_id)
    INNER JOIN answer USING(answer_id)
GROUP BY name_student, name_subject, date_attempt
ORDER BY name_student, date_attempt DESC;
''')
print(*cursor.fetchall(), sep='\n')
print()

# Для каждого вопроса вывести процент успешных решений, 
# то есть отношение количества верных ответов к общему 
# количеству ответов, значение округлить до 2-х знаков 
# после запятой. Также вывести название предмета, 
# к которому относится вопрос, и общее количество ответов 
# на этот вопрос. В результат включить название дисциплины, 
# вопросы по ней (столбец назвать Вопрос), а также 
# два вычисляемых столбца Всего_ответов и Успешность. 
# Информацию отсортировать сначала по названию дисциплины, 
# потом по убыванию успешности, а потом по тексту вопроса 
# в алфавитном порядке.

# Поскольку тексты вопросов могут быть длинными, 
# обрезать их 30 символов и добавить многоточие "...".
cursor.execute('''
    SELECT name_subject, 
    SUBSTR(name_question, 1, 30) || '...' AS 'Вопрос', 
    COUNT(question.question_id) AS 'Всего_ответов', 
    ROUND(SUM(is_correct)/COUNT(question.question_id) * 100, 2) AS 'Успешность'
FROM testing 
    INNER JOIN question USING(question_id)
    INNER JOIN answer USING(answer_id)
    INNER JOIN subject USING(subject_id)
GROUP BY name_subject, question.question_id
ORDER BY name_subject, Успешность DESC, name_question;
''')
print(*cursor.fetchall(), sep='\n')
print()


connect.commit()
connect.close()