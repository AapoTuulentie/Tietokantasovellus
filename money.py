from db import db


def get_amount(index):

    sql = "SELECT amount FROM money WHERE id = :index"
    amounts = db.session.execute(sql, {"index": index})
    return amounts.fetchone()


def get_all_amounts():

    sql = "SELECT amount FROM money ORDER BY DESC"
    amounts = db.session.execute(sql)
    return amounts.fetchall()