
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------------- Role Decorator ----------------
def role_required(role):
    def wrapper(f):
        from functools import wraps
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "user" not in session:
                return redirect(url_for("login"))
            if session["role"] != role:
                flash("Access denied! Insufficient permissions.", "danger")
                return redirect(url_for("dashboard"))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

# ---------------- Routes ----------------
@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with sqlite3.connect("payroll.db") as conn:
            user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user[2], password):
            session["user"] = user[1]
            session["role"] = user[3]
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password!", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have logged out.", "info")
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
@role_required("Admin")
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form.get("role", "HR")
        hashed_pw = generate_password_hash(password)
        try:
            with sqlite3.connect("payroll.db") as conn:
                conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_pw, role))
            flash("User registered successfully!", "success")
            return redirect(url_for("dashboard"))
        except sqlite3.IntegrityError:
            flash("Username already exists!", "danger")
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["user"], role=session["role"])

@app.route("/payroll", methods=["GET", "POST"])
def payroll():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        name = request.form["employee_name"]
        position = request.form["position"]
        salary = request.form["salary"]
        with sqlite3.connect("payroll.db") as conn:
            conn.execute("INSERT INTO payroll (employee_name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
        flash("Employee added successfully!", "success")
    with sqlite3.connect("payroll.db") as conn:
        records = conn.execute("SELECT * FROM payroll").fetchall()
    return render_template("payroll.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)
