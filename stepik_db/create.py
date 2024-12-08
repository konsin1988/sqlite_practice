import sqlite3

connection = sqlite3.connect('stepik.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS module
    (
    module_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    module_name TEXT
);
''')
cursor.execute('''
               
INSERT INTO module (module_name)
VALUES ('Основы реляционной модели и SQL'),
       ('Запросы SQL к связанным таблицам');
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS lesson
(
    lesson_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_name     TEXT,
    module_id       INTEGER,
    lesson_position INTEGER,
    FOREIGN KEY (module_id) REFERENCES module (module_id) ON DELETE CASCADE
);
''')
cursor.execute('''
INSERT INTO lesson(lesson_name, module_id, lesson_position)
VALUES ('Отношение(таблица)', 1, 1),
       ('Выборка данных', 1, 2),
       ('Таблица "Командировки", запросы на выборку', 1, 6),
       ('Вложенные запросы', 1, 4);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS step
(
    step_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    step_name     TEXT,
    step_type     TEXT,
    lesson_id     INTEGER,
    step_position INTEGER,
    FOREIGN KEY (lesson_id) REFERENCES lesson (lesson_id) ON DELETE CASCADE
);
''')
cursor.execute('''
INSERT INTO step(step_name, step_type, lesson_id, step_position)
VALUES ('Структура уроков курса', 'text', 1, 1),
       ('Содержание урока', 'text', 1, 2),
       ('Реляционная модель, основные положения', 'table', 1, 3),
       ('Отношение, реляционная модель', 'choice', 1, 4);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS keyword
(
    keyword_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword_name TEXT
);
''')
cursor.execute('''
INSERT INTO keyword(keyword_name)
VALUES ('SELECT'),
       ('FROM');
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS step_keyword
(
    step_id    INTEGER,
    keyword_id INTEGER,
    PRIMARY KEY (step_id, keyword_id),
    FOREIGN KEY (step_id) REFERENCES step (step_id) ON DELETE CASCADE,
    FOREIGN KEY (keyword_id) REFERENCES keyword (keyword_id) ON DELETE CASCADE
);
''')
cursor.execute('''
/* SET FOREIGN_KEY_CHECKS = 0;*/
PRAGMA foreign_keys = ON;
''')
cursor.execute('''
INSERT INTO step_keyword (step_id, keyword_id) VALUES (38, 1);
''')
cursor.execute('''
INSERT INTO step_keyword (step_id, keyword_id) VALUES (81, 3);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS student
(
    student_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT
);
''')
cursor.execute('''
INSERT INTO student(student_name)
VALUES ('student_1'),
       ('student_2');
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS step_student
(
    step_student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    step_id         INTEGER,
    student_id      INTEGER,
    attempt_time    INTEGER,
    submission_time INTEGER,
    result          TEXT,
    FOREIGN KEY (student_id) REFERENCES student (student_id) ON DELETE CASCADE,
    FOREIGN KEY (step_id) REFERENCES step (step_id) ON DELETE CASCADE
);
''')
cursor.execute('''
INSERT INTO step_student (step_id, student_id, attempt_time, submission_time, result)
VALUES (10, 52, 1598291444, 1598291490, 'correct'),
       (10, 11, 1593291995, 1593292031, 'correct'),
       (10, 19, 1591017571, 1591017743, 'wrong'),
       (10, 4, 1590254781, 1590254800, 'correct');
''')
cursor.execute('''
/*включаем проверку*/
/* SET FOREIGN_KEY_CHECKS = 1;*/
PRAGMA foreign_keys = ON;
''')


connection.commit()
connection.close()