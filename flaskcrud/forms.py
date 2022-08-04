from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from flaskcrud.models import Data

class Item(FlaskForm):
    name = StringField(label='Name', validators=[Length(min=3, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    phone = StringField(label='Phone Number:', validators=[DataRequired()])
    # img = FileField(label='Picture:', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField(label='Add Information')