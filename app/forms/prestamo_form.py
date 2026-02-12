from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class PrestamoForm(FlaskForm):
    libro_id = SelectField(
        'Libro', 
        validators=[DataRequired()], coerce=int
    )
    
    socio_id = SelectField(
        'Socio', 
        validators=[DataRequired()], coerce=int
    )
    submit = SubmitField('Prestar Libro')