def create_structure1():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS quiz ( 
        id INTEGER PRIMARY KEY,
        name VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz ( 
        id INTEGER PRIMARY KEY,
        question CARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content (
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER,
        FOREIGN KEY (quiz_id) REFERENCES quiz (id),
        question_id INTEGER
        FOREIGN KEY (quiz_id) REFERENCES quiz (id))''')
    close()

def create_structure2():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CREATE TABLE IF NOT EXISTS math_question (
        id INTEGER PRIMARY KEY,
        20* 45 INTEGER)''')

    do(''' CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY,
        workout INTEGER,
        Answer INTEGER,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')
    
    do('''CREATE TABLE IF NOT EXISTS question_content (
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER,
        FOREIGN KEY (quiz_id) REFERENCES math_question (id),
        question_id INTEGER
        FOREIGN KEY (quiz_id) REFERENCES question (id))''')
    close()

