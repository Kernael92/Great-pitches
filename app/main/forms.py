from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class commentForm(FlaskForm):
    description = TextAreaField('Add comment',Validators = [Required])
    Submit = SubmitField('submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('submit')
class PitchForm(FlaskForm):
	name = StringField('name', validators=[Required()])
	description = TextAreaField("Write your pitch here",validators=[Required()])
	category = RadioField('Label', choices=[ ('Sales','Sales'), ('Investor','Investor'),('Employees','Employees'),('Pickup','Pickup')],validators=[Required()])
	submit = SubmitField('Submit')