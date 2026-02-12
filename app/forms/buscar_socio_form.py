from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class BuscarSocioForm(FlaskForm):
    busqueda = StringField(
        "Nombre o Email",
        validators=[DataRequired(message="Debes ingresar un nombre o email"), Length(max=100)]
    )
    submit = SubmitField("Buscar")
