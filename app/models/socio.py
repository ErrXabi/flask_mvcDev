from app import db

class Socio(db.Model):
    __tablename__ = "socios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    libros_prestados = db.relationship("Libro", backref="socio", lazy=True)

    def to_dict(self):
            return {
                "id": self.id,
                "nombre": self.nombre,
                "email": self.email,
                "libros_prestados": [l.titulo for l in self.libros_prestados]
            }