from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length , Email

class SocioForm(FlaskForm):
    nombre = StringField(
        "Nombre",
        validators=[DataRequired(message="El título es obligatorio"), Length(max=200)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired("El correo electrónico es obligatorio"), Email() , Length(max=200)]
    )
    submit = SubmitField("Guardar")
