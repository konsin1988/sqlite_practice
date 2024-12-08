import sqlite3
connect = sqlite3.connect('testing.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE `student` (
`student_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`name_student` varchar(50) DEFAULT NULL
);''')
cursor.execute('''
CREATE TABLE `subject` (
`subject_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`name_subject` varchar(30) DEFAULT NULL
);''')
cursor.execute('''
CREATE TABLE `attempt` (
`attempt_id` INTEGER PRIMARY KEY AUTOINCREMENT,
student_id int DEFAULT NULL,
`subject_id` int DEFAULT NULL,
`date_attempt` date DEFAULT NULL,
`result` int DEFAULT NULL,
CONSTRAINT `attempt_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`) ON DELETE CASCADE,
CONSTRAINT `attempt_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE
);''')
cursor.execute('''
CREATE TABLE `testing` (
`testing_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`attempt_id` int DEFAULT NULL,
`question_id` int DEFAULT NULL,
`answer_id` int DEFAULT NULL,
CONSTRAINT `testing_ibfk_1` FOREIGN KEY (`attempt_id`) REFERENCES `attempt` (`attempt_id`) ON DELETE CASCADE
);''')
cursor.execute('''
CREATE TABLE `question` (
`question_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`name_question` varchar(100) DEFAULT NULL, 
`subject_id` int DEFAULT NULL,
CONSTRAINT `question_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE
);''')
cursor.execute('''
CREATE TABLE `answer` (
`answer_id` INTEGER PRIMARY KEY AUTOINCREMENT,
`name_answer` varchar(100) DEFAULT NULL,
`question_id` int DEFAULT NULL,
`is_correct` tinyint(1) DEFAULT NULL,
CONSTRAINT `answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`) ON DELETE CASCADE
);''')

connect.commit()
connect.close()

