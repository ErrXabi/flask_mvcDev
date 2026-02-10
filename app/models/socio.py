from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Socio(db.Model):
    __tablename__ = "socios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(100), nullable=False, default="Socio")
    email = db.Column(db.String(100), nullable=False)
    libros_prestados = db.relationship("Libro", backref="socio_asignado", lazy=True)

    def to_dict(self):
            return {
                "id": self.id,
                "nombre": self.nombre,
                "rol": self.rol,
                "email": self.email
            }
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)