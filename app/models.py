from . import db

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(2000))
    category = db.Column(db.String)
    comments = db.relationship('Comment',backref = 'pitch', lazy='dynamic')
    


    
    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.order_by(id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'
class Comment(db.Model):
    all_comments = []
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    description = db.Column(db.Text)

    def save_comments(self):
        Comment.all_commments(self)

    def __repe__(self):
        return f"Comment : id {self.id} comment : {self.description}"



