from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField('Pet Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing an pets"""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)],)
    available = BooleanField("Available?")