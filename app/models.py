from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(2000))
    category = db.Column(db.String)
    comments = db.relationship('Comment',backref = 'pitch', lazy='dynamic')
    


    
    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'

    @classmethod
    def get_pitches_by_category(cls, category):
        '''
        '''
        pitches = Pitch.query.filter_by(category)
        return pitches
         

class Comment(db.Model):
    all_comments = []
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    description = db.Column(db.Text)

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    def __repe__(self):
        return f"Comment : id {self.id} comment : {self.description}"

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    

    def __repr__(self):
        return f'User {self.username}'



