import sqlite3

connection = sqlite3.connect('abiturient.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE department(
    department_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name_department VARCHAR(30)
);
''')

cursor.execute('''
    CREATE TABLE subject(
    subject_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name_subject VARCHAR(30)
);
''')

cursor.execute('''
    CREATE TABLE program(
    program_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name_program VARCHAR(50),
    department_id INTEGER,
    plan INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE CASCADE
);
''')

cursor.execute('''
    CREATE TABLE enrollee(
    enrollee_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name_enrollee VARCHAR(50)
);  
''')

cursor.execute('''
    CREATE TABLE achievement(
    achievement_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name_achievement VARCHAR(30),
    bonus INTEGER
);
''')

cursor.execute('''
    CREATE TABLE enrollee_achievement(
    enrollee_achiev_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    enrollee_id INTEGER,
    achievement_id INTEGER,
    FOREIGN KEY (enrollee_id) REFERENCES enrollee(enrollee_id) ON DELETE CASCADE,
    FOREIGN KEY (achievement_id) REFERENCES achievement(achievement_id) ON DELETE CASCADE
);
''')
cursor.execute('''
    CREATE TABLE program_subject(
    program_subject_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER,
    subject_id INTEGER,
    min_result INTEGER,
    FOREIGN KEY (program_id) REFERENCES program(program_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE
);
''')
cursor.execute('''
    CREATE TABLE program_enrollee(
    program_enrollee_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    program_id INTEGER,
    enrollee_id INTEGER,
    FOREIGN KEY (program_id) REFERENCES program(program_id) ON DELETE CASCADE,
    FOREIGN KEY (enrollee_id) REFERENCES enrollee(enrollee_id) ON DELETE CASCADE
);
''')
cursor.execute('''
    CREATE TABLE enrollee_subject(
    enrollee_subject_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    enrollee_id INTEGER,
    subject_id INTEGER,
    result INTEGER,
    FOREIGN KEY (enrollee_id) REFERENCES enrollee(enrollee_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE
);
''')

connection.commit()
connection.close()