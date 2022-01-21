from re import S
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template,url_for, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, provided

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///passes.db")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
@app.route("/saved")
@login_required
def saved():
    user_id = session["user_id"]
    hist = db.execute("SELECT platform, username, email, password FROM passwords WHERE user_id = :user_id", user_id = user_id)
    # for i in range(len(hist)):


     # Redirect user to home page
    return render_template("saved.html", hist = hist)

@app.route("/generator")
@login_required
def generator():
    user_id=session["user_id"]


    # Redirect user to home page
    return render_template("generator.html")

@app.route("/save", methods=["GET", "POST"])
@login_required
def save():
    if request.method == "POST":
        check3 = provided("platform") or provided("password") 
        if check3 is not None:
            return check3
        else:
            # try:
            user_id=session["user_id"]
            platform = request.form.get("platform")
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
        
            db_key = db.execute("INSERT INTO passwords (platform, username, email, password, user_id) VALUES(?, ?, ?, ?, ?)",platform, username, email, password, user_id)
            if db_key is None:
                return apology("error 'Not-Saved'", 400)
            else:
                return redirect ("/saved")
            # except:
            #     return apology("username already taken", 400)
    else:
        # Redirect user to home page
        return render_template("save.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username nd pass submitted
        check = provided("username") or provided("password")
        if check is not None:
            return check
         # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        check1 = provided("username") or provided("password") or provided("confirmation")
        if check1 is not None:
            return check1
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 400)
        else:
            try:
                username = request.form.get("username")
                hashpass = generate_password_hash(request.form.get("password"))
                db_key = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",username,hashpass)
                if db_key is None:
                    return apology("registration error", 400)
                else:
                    session["user_id"] = db_key
                    return redirect("/")
            except:
                return apology("username already taken", 400)
    else:
        return render_template("register.html")

        