from flask import render_template
from datetime import datetime
from dev.server import app

#Home page before login
@app.route('/')
def start():
	return render_template("base.html")

#Home page after login
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        "index.html",
        title = "Home",
        year = datetime.now().year
    )

#Videos Category
@app.route('/category')
def category():
	return render_template("category.html")

@app.route('/signup')
def signup():
	return render_template("signup.html")

