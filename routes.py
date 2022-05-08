from app import app
from flask import render_template, request, redirect, session
from random import randint
import users
import questions
import stats
import feedback
import money


@app.route("/")
def index():
    
    comments = feedback.get_feedback()
    return render_template("index.html", comments = comments)


@app.route("/review", methods=["post"])
def review():

    users.check_csrf()
    comment = request.form["comment"]
    feedback.insert_feedback(session["user_id"], session["user_name"], comment)
    return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():
    
    if request.method == "GET":
        
        return render_template("register.html")

    if request.method == "POST":
        
        username = request.form["username"]
        
        if len(username) < 1 or len(username) > 20:
            
            return render_template("error.html", message = "Username must be 1-20 characters long")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        
        if password1 != password2:
            
            return render_template("error.html", message = "Passwords are different")
        
        if password1 == "":
            
            return render_template("error.html", message = "Password is empty")

        if len(password1) > 20 or len(password1) < 6:

            return render_template("error.html", message = "Password length should be 6-20 characters")
        
        if not users.register(username, password1):
            
            return render_template("error.html", message = "Registration failed")
        
        return redirect("/")
   

@app.route("/login", methods=["get", "post"])
def login():
    
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Username or password is incorrect")
        return redirect("/")


@app.route("/logout")
def logout():
    
    users.logout()
    return redirect("/")


@app.route("/quiz/start")
def start_quiz():

    try:

        session["username"]

    except:

        return render_template("error.html", message="You need to log in before playing")

    session['asked'] = []
    random = randint(1, 4)
    question_data = questions.get_question()
    amount = ["100"]
    millionaires = stats.millionaires()

    
    return render_template("questions.html", question = question_data[0], correct = question_data[1], wrong1 = question_data[2], wrong2 = question_data[3], wrong3 = question_data[4], random = random, index = 0, amount = amount, millionaires = millionaires)
    

@app.route("/result", methods=["POST"])
def answer():

    index = int(request.form["index"])
    amount = money.get_amount(index + 2)  
    amount2 = money.get_amount(index + 1)
    answer = request.form["answer"].strip()
    correct = request.form["correct"].strip()

    if index == 14:
        
        stats.insert_user(session["user_id"], session["user_name"])    
        millionaires = stats.millionaires()
        return render_template("millionaire.html", millionaires = millionaires)
        
    return render_template("result.html", answer=answer, correct=correct, index = index, amount = amount, amount2 = amount2)


@app.route("/quiz", methods=["POST"])
def quiz():

    index = int(request.form["index"])
    index += 1
    amount = money.get_amount(index + 2)
    random = randint(1, 4)
    millionaires = stats.millionaires()
    
    if 0 <= index <= 4:
        
        question_data = questions.get_question()

    if 5 <= index <= 9:

        question_data = questions.get_advanced_question()

    if index >= 10:

        question_data = questions.get_hard_question()


    return render_template("questions.html", question = question_data[0], correct = question_data[1], wrong1 = question_data[2], wrong2 = question_data[3], wrong3 = question_data[4], random = random, index = index, amount = amount, millionaires = millionaires)



if __name__ == "__main__":
    app.run(debug=True)