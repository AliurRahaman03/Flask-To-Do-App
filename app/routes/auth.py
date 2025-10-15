from flask import Blueprint, render_template, redirect, request, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    "username": "admin",
    "password": "12345"
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            session["user"] = username
            flash("Login Successful", "success")
            # redirect to tasks (POST-Redirect-GET)
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Loged out", "info")
    return redirect(url_for("auth.login"))

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        id = request.form.get()