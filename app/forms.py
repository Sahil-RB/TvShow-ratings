from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class searchByIdForm(FlaskForm):
    id = StringField('Imdb ID', validators = [DataRequired()])
    season = StringField('Season', validators = [DataRequired()])
    submit = SubmitField('Calculate')
    
