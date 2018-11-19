from flask import render_template,request,redirect,url_for,abort
from . import main
from .. import db
from ..models import Pitch,Comment,User 
from .forms import commentForm
from flask_login import login_required
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.filter_by().first()
    
    salespitch = Pitch.query.filter_by(category = "Sales")
    # print(Sales)
    investorpitch = Pitch.query.filter_by(category = "Investor")
    employeespitch = Pitch.query.filter_by(category = "Employees")
    pickuplinepitch = Pitch.query.filter_by(category = "Pickup")
    title = 'Home- welcome to the best pitches website online'

    return render_template('index.html', title = title,pitches =pitches, Sales=salespitch,Investor=investorpitch,Employees=employeespitch,Pickup=pickuplinepitch)

@main.route('/pitch/comment/new/<int:pitch_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    form = commentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data
        new_comment = Comment(description = description, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', pitch_id = pitch_id))
    
    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    return render_template('comments.html',form = form ,comment = all_comments, pitch=pitch)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)


