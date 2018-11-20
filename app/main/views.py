from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from ..models import Pitch,Comment,User 
from .forms import commentForm,UpdateProfile
from flask_login import login_required, current_user
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.filter_by.first()
    
    salespitch = Pitch.query.filter_by(category = "Sales")
    print(salespitch)
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
        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
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
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort (404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)

        db.session.commit()
        return redirect(url_for('.profile', uname = user.username))
    return render_template('profile/update.html', form = form)
@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))

