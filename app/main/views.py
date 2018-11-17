from flask import render_template,request,redirect,url_for
from . import main
from .. import db
from ..models import Pitch 
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home- welcome to the best pitches website online'
    salespitch = Pitch.query.filter_by(category = "Sales")
    investorpitch = Pitch.query.filtet_by(category = "Investor")
    employeespitch = Pitch.query.filter_by(category = "Employees")
    Pickuplinepitch = Pitch.query.filter_by(category = "Pickup")

    return render_template('index.html', titlt = title,salespitch = salespitch, investorpitch = investorpitch, employeespitch = employeespitch, pickuplinepitch = Pickuplinepitch)


