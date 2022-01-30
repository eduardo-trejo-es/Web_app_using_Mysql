from flask import Blueprint, render_template, request, flash
from StockPricePredictionFIles.ForcastingGeneScript import PriceForcaster
from flask import Flask, render_template
from flask import Flask, redirect, url_for, render_template, session
from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField


views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
def home():
    return render_template("home.html")

