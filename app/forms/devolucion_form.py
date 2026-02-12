from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class DevolucionForm(FlaskForm):
    libro_id = SelectField(
        'Libro a devolver', 
        validators=[DataRequired()], coerce=int
    )
    submit = SubmitField('Confirmar Devolución')