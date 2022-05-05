from db import db


def insert_feedback(user_id, username, comment):

    insert_sql = "INSERT INTO feedback (user_id, username, comment) VALUES (:user_id, :user_name, :comment)"
    db.session.execute(insert_sql, {"user_id": user_id, "user_name": username, "comment": comment})
    db.session.commit()


def get_feedback():

    feedback_sql = "SELECT username, comment FROM feedback"
    feedback = db.session.execute(feedback_sql).fetchall()
    return feedback