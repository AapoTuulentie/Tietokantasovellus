from db import db


def insert_user(user_id, username):

    user_sql = "INSERT INTO millionaires (user_id, username) VALUES (:user_id, :user_name)"
    db.session.execute(user_sql, {"user_id": user_id, "user_name": username})
    db.session.commit()

def millionaires():

    millionaires_sql = "SELECT username FROM millionaires"
    millionaire = db.session.execute(millionaires_sql).fetchall()
    return millionaire

def check_user(username):

    user_sql = "SELECT username FROM millionaires WHERE username =:username"
    user = db.session.execute(user_sql, {"username": username}).fetchone()

    if not user:
        
        return False

    return True