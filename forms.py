from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    """
    Input form to get the specified address from the user
    """
    input_address = StringField(
        'Enter address', validators=[DataRequired()])
    submit = SubmitField('Get Distance')
