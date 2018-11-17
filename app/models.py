from . import db

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(2000))
    category = db.Column(db.String(255))
    


    
    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.order_by(pitch_id = id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'



