from flask import Blueprint, render_template, request, flash
from flask import Flask, render_template
from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField


views = Blueprint('views', __name__)


@views.route('/save_email', methods=["POST", "GET"])
def Save_email():
    if request.method == "POST":
        email = request.form["email"]
        return redirect(url_for("views.write_email_func", email_send_val=email, other_A="hello world"))
    else:
        return render_template("Save_email.html")

@views.route("/write_email/<email_send_val>/<other_A>")
def write_email_func(email_send_val,other_A):
    return f"<h1>{email_send_val,other_A}</h1>"



"""@views.route('/save_email', methods=['POST', 'GET'])
def Save_email():
    if request.method == "POST":
        email = request.form["email"]
        print(email)
        return redirect(url_for("test_name_func", email_test=email))
    else:
        return render_template("Save_email.html")

@views.route("/<email_url>")
def test_name_func(email_url):
    return f"<h1>{email_url}</h1>"""

