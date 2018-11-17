from flask import render_template,request,redirect,url_for
from . import main
from .. import db
from ..models import Pitch 
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    Sales = Pitch.query.filter_by(category = "Sales")
    Investor = Pitch.query.filter_by(category = "Investor")
    Employees = Pitch.query.filter_by(category = "Employees")
    Pickup = Pitch.query.filter_by(category = "Pickup")
    title = 'Home- welcome to the best pitches website online'

    return render_template('index.html', title = title,pitch =pitch, Sales= Sales, Investor = Investor, Employees = Employees, Pickup = Pickup)


