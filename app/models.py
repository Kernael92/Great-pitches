from . import db

class PItch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String)
    category = db.Column(db.String(255))
    


    def __repr__(self):
        return f'Pitch {self.description}'


