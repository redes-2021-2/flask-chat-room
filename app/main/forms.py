from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    name = StringField('Name', validators=[Required()])
    room = StringField('Name', validators=[Required()])
    submit = SubmitField('Entrar a la sala de chat')