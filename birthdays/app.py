import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        month = 0
        day = 0
        name = request.form.get("name")
        try:
            month = int(request.form.get("month"))
            day = int(request.form.get("day"))
        except ValueError:
            return redirect("/")
        if day > 31 or day < 1 or month > 12 or month < 1 or name == '':
            return redirect("/")
        else:

            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?);", name, month, day)
            return redirect("/")
    # TODO: Display the entries in the database on index.html
    
    """if "remove" in request.form:
        id = db.execute("SELECT id FROM birthdays")
        db.execute("REMOVE * FROM birthdays WHERE id = ?", id)"""

    bday = db.execute("SELECT name, month, day FROM birthdays")
    return render_template("index.html", bday=bday)


