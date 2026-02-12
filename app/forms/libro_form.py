from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class LibroForm(FlaskForm):
    titulo = StringField(
        "Título",
        validators=[DataRequired(message="El título es obligatorio"), Length(max=200)]
    )

    autor = StringField(
        "Autor",
        validators=[DataRequired(message="El autor es obligatorio"), Length(max=100)]
    )

    resumen = TextAreaField(
        "Resumen",
       # validators=[Length(min=5, max=1000)]
    )

    año = StringField(
        "Año",
        validators=[DataRequired(message="El año es obligatorio")]
    )

    categoria = StringField(
        "Categoria",
        validators=[DataRequired(message="La categoría es obligatoria"), Length(max=100)]
    )

    submit = SubmitField("Guardar")
