from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class commentForm(FlaskForm):
    description = TextAreaField('Add comment',Validators = [Required])
    Submit = SubmitField('submit')