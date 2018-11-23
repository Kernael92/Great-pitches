from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db,photos
from ..models import Pitch,Comment,User,Upvote,Downvote 
from .forms import commentForm,UpdateProfile,PitchForm,UpvoteForm,DownvoteForm
from flask_login import login_required, current_user
import markdown2



@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    
    salespitch = Pitch.query.filter_by(category ="Sales")
    print(salespitch)
    investorpitch = Pitch.query.filter_by(category = "Investor")
    employeespitch = Pitch.query.filter_by(category = "Employees")
    pickuplinepitch = Pitch.query.filter_by(category = "Pickup")
    title = 'Home- welcome to the best pitches website online'

    return render_template('index.html', title = title, Sales=salespitch,Investor=investorpitch,Employees=employeespitch,Pickup=pickuplinepitch)

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
@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
  
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        name = form.name.data
        user_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(user_id =current_user._get_current_object().id, name = name,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form,my_upvotes = my_upvotes)
@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    form = UpvoteForm()
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
        db.session.add(new_upvote)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('Upvote.html',pitch = pitch, pitch_upvotes = pitch_upvotes, form = form)
@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    form = DownvoteForm()
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id = pitch_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
        new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
        db.session.add(new_downvote)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('downvote.html',pitch = pitch, pitch_downvotes = pitch_downvotes, form = form)


