import sqlite3

connection = sqlite3.connect('abiturient.db')
cursor = connection.cursor()


# Список всех таблиц базы данных abiturient.db

# cursor.execute('''
#     ATTACH 'abiturient.db' AS exdb;
# ''')
# cursor.execute('''
#     SELECT name FROM exdb.sqlite_master WHERE type='table';
# ''')
# table_names = cursor.fetchall()
# table_names = [x[0] for x in table_names if x[0] != 'sqlite_sequence']
# print(table_names)

# Посмотреть код создания таблицы sql 
# for x in table_names:
#     cursor.execute(f'SELECT sql FROM exdb.sqlite_master WHERE type="table" and name="{x}"')
#     print(cursor.fetchall()[0][0])
#-----------------------------------------------------------
# Вывести абитуриентов, которые хотят поступать 
# на образовательную программу «Мехатроника и робототехника» 
# в отсортированном по фамилиям виде.
# cursor.execute('''
#     SELECT name_enrollee FROM enrollee
#     INNER JOIN program_enrollee USING(enrollee_id)
#     INNER JOIN program ON program_enrollee.program_id = program.program_id
#     AND name_program = 'Мехатроника и робототехника'
#     ORDER BY name_enrollee
# ''')
#--------------------------------------------------------
# Вывести образовательные программы, 
# на которые для поступления н
# еобходим предмет «Информатика». 
# Программы отсортировать в обратном алфавитном порядке.
# cursor.execute('''
#     SELECT name_program FROM program
#     INNER JOIN program_subject USING(program_id)
#     INNER JOIN subject ON subject.subject_id = program_subject.subject_id
#     AND name_subject = 'Информатика'
#     ORDER BY name_program DESC
# ''')
#-------------------------------------------------
# Выведите количество абитуриентов, сдавших ЕГЭ по каждому предмету, максимальное, минимальное и среднее значение баллов по предмету ЕГЭ. Вычисляемые столбцы назвать Количество, Максимум, Минимум, Среднее. Информацию отсортировать по названию предмета в алфавитном порядке, среднее значение округлить до одного знака после запятой.
# cursor.execute('''
#     SELECT name_subject, COUNT(enrollee_id) AS 'Количество', 
#         MAX(result) AS 'Максимум', 
#         MIN(result) AS 'Минимум', 
#         ROUND(AVG(result), 1) AS 'Среднее'
#     FROM enrollee_subject 
#     LEFT JOIN subject USING(subject_id)
#     ORDER  BY name_subject
# ''')
#--------------------------------------------

# Вывести образовательные программы, 
# для которых минимальный балл ЕГЭ 
# по каждому предмету больше или равен 40 баллам. 
# Программы вывести в отсортированном по алфавиту виде.
# cursor.execute('''
#     SELECT name_program 
#     FROM program
#         INNER JOIN program_subject USING(program_id)
#     WHERE min_result >= 40
#     HAVIN G COUNT(name_program) = 3
#     ORDER BY name_program
# ''')
#----------------------------------------------
# Вывести образовательные программы, 
# которые имеют самый большой план набора,  
# вместе с этой величиной.
# cursor.execute('''
#     SELECT name_program, plan
# FROM program
# WHERE plan = (
#     SELECT MAX(plan)
#     FROM program
#     )
# ''')
#---------------------------------------------
# Посчитать, сколько дополнительных баллов получит 
# каждый абитуриент. Столбец с дополнительными баллами 
# назвать Бонус. Информацию вывести 
# в отсортированном по фамилиям виде.
# cursor.execute('''
#     SELECT name_enrollee, CASE 
#                             WHEN SUM(bonus) IS NULL 
#                             THEN 0 
#                             ELSE SUM(bonus) END AS 'Бонус'
#     FROM enrollee
#         LEFT JOIN enrollee_achievement USING(enrollee_id)
#         LEFT JOIN achievement USING(achievement_id)
#     ORDER  BY name_enrollee
# ''')
#----------------------------------------------------
# Выведите сколько человек подало заявление на каждую 
# образовательную программу и конкурс на нее 
# (число поданных заявлений деленное на количество мест по плану), 
# округленный до 2-х знаков после запятой. 
# В запросе вывести название факультета, 
# к которому относится образовательная программа, 
# название образовательной программы, план набора 
# абитуриентов на образовательную программу (plan), 
# количество поданных заявлений (Количество) и Конкурс. 
# Информацию отсортировать в порядке убывания конкурса.
# cursor.execute('''
#     SELECT name_department, name_program, plan, COUNT(enrollee_id) AS 'Количество', ROUND(COUNT(enrollee_id) / plan, 2) AS 'Конкурс'
#     FROM department
#         INNER JOIN program USING(department_id)
#         LEFT JOIN program_enrollee USING(program_id)
#     ORDER  BY Конкурс DESC
# ''')
#---------------------------------------------------
# Вывести образовательные программы, на которые 
# для поступления необходимы предмет «Информатика» 
# и «Математика» в отсортированном по названию программ виде.
# cursor.execute('''
#     SELECT name_program
#     FROM program
#         JOIN program_subject USING(program_id)
#         JOIN subject USING(subject_id)
#     GROUP BY name_program, name_subject
#     HAVING name_subject = 'Информатика' OR name_subject = 'Математика' AND COUNT(name_subject) = 2
#     ORDER BY name_program
# ''')
#----------------------------------------------------------
# Посчитать количество баллов каждого абитуриента 
# на каждую образовательную программу, на которую 
# он подал заявление, по результатам ЕГЭ. В результат 
# включить название образовательной программы, 
# фамилию и имя абитуриента, а также столбец 
# с суммой баллов, который назвать itog. 
# Информацию вывести в отсортированном сначала 
# по образовательной программе, а потом по убыванию суммы баллов виде.
# cursor.execute('''
#     SELECT name_program, name_enrollee, SUM(result) AS 'itog'
#     FROM enrollee
#         JOIN program_enrollee USING(enrollee_id) 
#         JOIN program USING(program_id)
#         JOIN enrollee_subject USING(enrollee_id)
#         JOIN program_subject USING(program_id)
#         JOIN subject ON program_subject.subject_id = subject.subject_id
#         AND enrollee_subject.subject_id = subject.subject_id
#         GROUP BY name_program, name_enrollee
#         ORDER BY name_program, itog DESC;
# ''')
#----------------------------------------------
# Вывести название образовательной программы и фамилию 
# тех абитуриентов, которые подавали документы на эту 
# образовательную программу, но не могут быть зачислены на нее. 
# Эти абитуриенты имеют результат по одному или нескольким 
# предметам ЕГЭ, необходимым для поступления 
# на эту образовательную программу, 
# меньше минимального балла. Информацию вывести 
# в отсортированном сначала по программам, 
# а потом по фамилиям абитуриентов виде.
# Например, Баранов Павел по «Физике» набрал 41 балл, 
# а  для образовательной программы «Прикладная механика» 
# минимальный балл по этому предмету определен 
# в 45 баллов. Следовательно, абитуриент 
# на данную программу не может поступить.
# cursor.execute('''
#     SELECT name_program, name_enrollee
#     FROM program 
#         JOIN program_enrollee USING(program_id)
#         JOIN enrollee USING(enrollee_id)
#         JOIN enrollee_subject USING(enrollee_id)
#         JOIN program_subject USING(program_id)
#         JOIN subject ON program_subject.subject_id = subject.subject_id
#         AND enrollee_subject.subject_id = subject.subject_id   
#         AND result < min_result
#         GROUP BY name_program, name_enrollee
#         ORDER BY name_program, name_enrollee
# ''')
# -----------------------------------------------------
# Вывести по каждому предмету: минимум, максимум, среднее и количество сдавших предмет.
# Необходимо учесть:
# 1) Все названия на русском и начинаются с маленькой буквы используем функцию LOWER.
# 2) Округление до целого числа.
# 3) Использовать таблицы subject и enrollee_subject.
# 4) Сортировать по убыванию среднего балла.  
# cursor.execute('''
    
# ''')

# -----------------------------------------------------
# Создать вспомогательную таблицу applicant,  
# куда включить id образовательной программы, 
# id абитуриента, сумму баллов абитуриентов 
# (столбец itog) в отсортированном сначала 
# по id образовательной программы, а 
# потом по убыванию суммы баллов виде
# cursor.execute('''CREATE TABLE applicant AS
#     SELECT program_enrollee.program_id, enrollee.enrollee_id, SUM(result) AS itog
#     FROM program
#         JOIN program_enrollee ON program.program_id = program_enrollee.program_id
#         JOIN program_subject ON program.program_id = program_subject.program_id
#         JOIN subject ON program_subject.subject_id = subject.subject_id
#         JOIN enrollee ON enrollee.enrollee_id = program_enrollee.enrollee_id
#         JOIN enrollee_subject ON enrollee.enrollee_id = enrollee_subject.enrollee_id 
#         AND enrollee_subject.subject_id = subject.subject_id
#     GROUP BY program_enrollee.program_id, enrollee.enrollee_id
#     ORDER BY program_enrollee.program_id, itog DESC;
# ''')


# Из таблицы applicant, созданной на предыдущем шаге, 
# удалить записи, если абитуриент на выбранную 
# образовательную программу не набрал минимального 
# балла хотя бы по одному предмету
# cursor.execute('''
#     DELETE FROM applicant
# WHERE (program_id, enrollee_id) IN
# (SELECT program.program_id AS prog_id, enrollee.enrollee_id AS inr_id
# FROM program
#     JOIN program_enrollee ON program.program_id = program_enrollee.program_id
#     JOIN program_subject ON program.program_id = program_subject.program_id
#     JOIN enrollee ON program_enrollee.enrollee_id = enrollee.enrollee_id
#     JOIN subject ON subject.subject_id = program_subject.subject_id
#     JOIN enrollee_subject ON subject.subject_id = enrollee_subject.subject_id
#     AND enrollee.enrollee_id = enrollee_subject.enrollee_id
#     AND enrollee_subject.result < program_subject.min_result)
# ''')

# Повысить итоговые баллы абитуриентов в таблице 
# applicant на значения дополнительных баллов 
# (использовать запрос из предыдущего урока)
# cursor.execute('''
#     UPDATE applicant INNER JOIN (SELECT enrollee_id, IF(SUM(bonus) IS NULL, 0, SUM(bonus)) AS 'bonus'
#     FROM enrollee
#         LEFT JOIN enrollee_achievement USING(enrollee_id)
#         LEFT JOIN achievement USING(achievement_id)
#     GROUP BY enrollee_id) AS bonus USING(enrollee_id)
# SET itog = itog + bonus.bonus;
# ''')

# cursor.execute('''
# CREATE TABLE applicant_order AS
# SELECT * FROM applicant
#  ORDER BY program_id, itog DESC;
# ''')


# cursor.execute('''
#     ALTER TABLE applicant_order ADD str_id INTEGER;
# ''')

# print(list(map(lambda x: x[0], cursor.description)), *cursor.fetchall(), sep='\n')

# cursor.execute('''

# ''')
# print(list(map(lambda x: x[0], cursor.description)), *cursor.fetchall(), sep='\n')



connection.commit()
connection.close()
