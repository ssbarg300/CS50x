import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    shares = db.execute("SELECT * FROM stocks WHERE user_id = ? AND shares > 0", user_id)
    try:
        cash = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)[0]['cash']
    except IndexError:
        return redirect("/register")
    total_value = cash
    stock_list = []
    for stock in shares:
        stock_info = lookup(stock["name"])
        stock_shares = stock["shares"]
        stock_tot = stock_info["price"] * stock_shares
        stock_value = stock_info["price"] * stock_shares
        total_value += stock_value
        stock_list.append({
            'name' : stock_info["name"],
            'price' : usd(stock_info["price"]),
            'shares' : stock_shares,
            'total' : usd(stock_tot)
        })
    try:
        return render_template("index.html", all=stock_list, cash=cash, total=total_value)
    except UnboundLocalError:
        return render_template("index.html", total=total_value, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("buy.html")

    # User reached route via POST (as by submitting a form via POST)
    elif request.method == "POST":

        # Check if symbol is entered and if it is valid or not.
        if not request.form.get("symbol") or not lookup(request.form.get("symbol")):
            return apology("Enter a valid symbol")

        # Check if shares is entered.
        if not request.form.get("shares"):
            return apology("Enter number of shares to buy")

        # Check if shares is a postive integer or not
        try:

            # If value enterd can be an integer.
            shares = int(request.form.get("shares"))

            # Check if shares to buy are a postive integer or not.
            if shares < 1:
                raise ValueError

        # Raise errors.
        except ValueError:
            return apology("Enter a postive integer for the shares")

        # If valid SYMBOL & SHARES are entered:

        # Time and Date:
        current_date = datetime.date.today()

        # Extracting Symbol and Shares:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Lookup price for SYMBOL and calculating the total amount required to buy shares:
        symbol_result = lookup(symbol)
        total_amount = float(shares) * symbol_result["price"]

        # Current User ID:
        current_user = session["user_id"]
        if isinstance(current_user, dict):
            current_user = session["user_id"][0]["id"]

        # Query amount of the user:
        cash_in_hand = db.execute("SELECT cash from users WHERE id = ?", current_user)[0]["cash"]

        # Check if shares can be bought:
        if cash_in_hand < total_amount:
            return apology("Not enought fund to buy these shares")

        else:
            # Query into HOLDINGS to see if already invested in this STOCK.
            check_stock_held = db.execute("SELECT shares FROM stocks where user_id = ? AND name = ?", current_user, symbol)

            # If a user doesn't hold this stock, add it.
            if not check_stock_held:
                db.execute("INSERT INTO stocks (user_id, name, shares) VALUES (?, ?, ?)", current_user, symbol, shares)

            # If the user holds this stock, update it.
            else:
                updated_shares = check_stock_held[0]["shares"] + int(shares)
                db.execute("UPDATE stocks SET shares = ? WHERE user_id = ? AND name = ?", updated_shares, current_user, symbol)

            # Add transaction
            db.execute("INSERT INTO transactions (user_id, stock_symbol, shares, price, timestamp, type) VALUES (?, ?, ?, ?, ?, ?)", current_user, symbol, shares, symbol_result["price"], current_date, "Buy")

            # Subtract balance
            update_cash = cash_in_hand - total_amount
            db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, current_user)

        return redirect("/")
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == 'GET':
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        s = lookup(symbol)
        if s != None:
            return render_template("quoted.html", name=s["name"], price=s["price"], symbol_=s["symbol"])
    return apology("None, The symbol you entered does not exist.")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # declare username confirmation and password to check later
    usernames = [row['username'] for row in db.execute("SELECT username FROM users;")]
    if request.method == 'POST':
        username = request.form.get("username")
        confirmation = request.form.get("confirmation")
        password = request.form.get("password")
        # check if username is blank or already exists
        if not username:
            return apology("Did not enter username.", 400)
        # else if password is blank or confirmation and pasword are not equal.
        elif username in usernames:
            return apology("Username Already Exists.", 400)

        elif not password or confirmation != password:
            return apology("password empty, or password and confirmation do not match.", 400)
    else:
        return render_template("register.html")
    try:
        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, generate_password_hash(password))
    except ValueError:
        return render_template("register.html")
    return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    """Sell shares of stock"""
    # set user id to current user's session
    user_id = session["user_id"]
    # get all the symbols from the database
    symbols = db.execute("SELECT name FROM stocks WHERE user_id = ?", user_id)
    # declare an empty list named slist which will contain the symbols
    slist = []
    # loop over symbols
    for i in symbols:
        # append symbol names to slist
        slist.append({'name': i["name"]})
    # check if request method is GET
    if request.method == "GET":
        # return sell.html with all the symbols the user has
        return render_template("sell.html", symbols=slist)
    # otherwise if the request method is get
    else:
        # get the symbol the user chose
        symbol = request.form.get("symbol")
        # get the number of shares the user chose
        share = request.form.get("shares")
        # check if symbol exists
        symbol_exists = False
        for i in slist:
            if symbol == i["name"]:
                symbol_exists = True
                break
        # if symbol doesnt exist return an apology
        if not symbol_exists:
            return apology("symbol doesnt exist")
        # get the shares the user owns from the database
        shares = db.execute("SELECT shares FROM stocks WHERE user_id = ? AND name = ?", user_id, symbol)[0]["shares"]
        # try to convert shares and share to integers
        try:
            shares = int(shares)
            share = int(share)
        # except if theres a value error or a type error so if they are not ints or they're none
        except ValueError:
            # return an apology invalid shares
            return apology("invalid shares")
        # check if shares are less than or equal to 0
        if share <= 0:
            # if they are we return an apology, and ask the user to enter a positive share
            return apology("enter positive shares!")
        # here we lookup the price from the api
        price = lookup(symbol)["price"]
        if share > shares or share is None:
            return apology("invalid shares")

        # from here on the sale should be valid

        # this is the shares after the sale
        sofsh = shares - share
        # cash in account. Basically selecting cash from the database where the user is the current user
        cash_earned = float(price) * share
        cash_in_account = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        new_cash_balance = float(cash_in_account) + cash_earned
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash_balance, user_id)
        db.execute("UPDATE stocks SET shares = ? WHERE user_id = ? AND name = ?", sofsh, user_id, symbol)
        # Add this sale to transactions.db:
        current_date = datetime.date.today()
        db.execute("INSERT INTO transactions (user_id, stock_symbol, shares, price, timestamp, type) VALUES (?, ?, ?, ?, ?, ?)", user_id, symbol, share, price, current_date, "Sell")
        return redirect("/")

@app.route("/remove")
@login_required
def remove():
    user_id = session["user_id"]
    db.execute("DELETE FROM stocks WHERE user_id = ?", user_id)
    db.execute("DELETE FROM transactions WHERE user_id = ?", user_id)
    db.execute("DELETE FROM users WHERE id = ?", user_id)
    session.clear()
    return redirect("/register")

