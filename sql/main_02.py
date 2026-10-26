def add_data():
    quizquestions = [
        ('What is current president of indonesia?', 'Prabowo', 'Soekarno', 'Jokowi', 'Gojek'),
        ('What is 3*3?', '9', '10', '6', '13'),
        ('What is 8/2?', '4', '10', '12', '100'),
        ('What is the colour of the flag indonesia?', 'Red and white', 'Blue and black', 'brown', 'grey'),
        ('Which one is an insect?', 'stick bug', 'dog', 'bird', 'fish')
        ('if a person breaks one of your friends window, what should you do?', 'stop them and make them apologize', 'Join them', 'cheer them on', 'run away'),
        ('Budi gave steph 1 ball and steph has 5 balls before Budi gave him a ball, how much does steph has now?', '6', '4', '10', '5'),
        ('What is the capital of indonesia?', 'Jakarta', 'Depok', 'Cibubur', 'Bandung')
        ('What the current top university in indonesia', 'University Indonesia', 'ITB', 'UNPAD', 'UGM')
        ('What happens when a person does not revise before an exam', ('they fails'), 'they pass', 'they get a prize', 'they go to jail')
        ('What happens when you put an egg in a microwave?', 'it explodes', 'its hot', 'becomes colder', 'they fly')
        ('what happens when productivity and quantity increases in a business', 'profit decreases', 'profit increases', 'business is successful', 
    ]

        open()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong 2, wrong3) VALUES (?, ?,?,?)''', questions)
    conn.commit()
    close()

def add_quiz():
    quizes = [
        ('Own game', ),
        ('Who wants to be a millionarie?', ),
        ('The smartest', )
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)"
    answer = input("Add a link(y/n)?")
    while answer!= 'n':
        quiz_id = int(input("quiz id: "))
        question_id = int(input("question id: "))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input("Add a link (y/n)?")
    close()

def show(table):
    query = 'SELECT * FROM' + table
    open()
    cursor.execute(query)
    print(cursor.fetchhall())
    close()

def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')

def get_question_after(question_id = 0, quiz_id=1):
    open()
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3 FROM question, quiz_content
    WHERE quiz_content.question_id == question.id AND quiz_content.id > ? AND quiz_content.quiz_id == ? ORDER BY quiz_content.id'''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result

def main():
    clear_db()
    create()
    add_question()
    add_quiz()
    add_links()
    show_tables()
    print(get_question_after(3, 1))

if __name__ == "__main__":
    main()
