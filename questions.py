from random import randint
from db import db

def get_question():

    questions_amount_sql = "SELECT COUNT(question) FROM questions"
    questions_amount = db.session.execute(questions_amount_sql).fetchone()[0]
    number = randint(0, questions_amount - 1)
    question_sql = "SELECT question FROM questions LIMIT 1 OFFSET :number"
    question = db.session.execute(question_sql, {"number":number}).fetchone()[0]

    correct_sql = "SELECT correct FROM questions LIMIT 1 OFFSET :number"
    correct = db.session.execute(correct_sql, {"number":number}).fetchone()[0]
    wrong1_sql = "SELECT wrong1 FROM questions LIMIT 1 OFFSET :number"
    wrong1 =  db.session.execute(wrong1_sql, {"number":number}).fetchone()[0]
    wrong2_sql = "SELECT wrong2 FROM questions LIMIT 1 OFFSET :number"
    wrong2 = db.session.execute(wrong2_sql, {"number":number}).fetchone()[0]
    wrong3_sql = "SELECT wrong3 FROM questions LIMIT 1 OFFSET :number"
    wrong3 = db.session.execute(wrong3_sql, {"number":number}).fetchone()[0]

    print(question)

    return(question, correct, wrong1, wrong2, wrong3)
    


