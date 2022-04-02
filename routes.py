from app import app
from flask import render_template, request, redirect
import users
import questions

@app.route("/")
def index():
    
    return render_template("index.html")

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














@app.route("/quiz")
def quiz():

    question_data = questions.get_question()
    return render_template("questions.html", question = question_data[0], correct = question_data[1], wrong1 = question_data[2], wrong2 = question_data[3], wrong3 = question_data[4])

@app.route("/result", methods=["POST"])
def answer():

    answer = request.form["answer"].strip()
    correct = request.form["correct"].strip()
    
    return render_template("result.html", answer=answer, correct=correct)


    


