from flask import render_template
from . import app

@app.route('/')
def index():
	return render_template('index.html')


@app.route("/about_us")
def about_us():
	return render_template("about_us.html")


@app.route("/contact")
def contact_us():
	return "Contact Us"


	