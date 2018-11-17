from flask import render_template,request,redirect,url_for
from . import main
from .. import db
from ..models import Pitch,Comment 
from .forms import commentForm
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

@main.route('/comment/new/<int: pitch_id>', methods = ['GET', 'POST'])
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


