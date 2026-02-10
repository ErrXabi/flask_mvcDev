from app import db
from app.models.socio import Socio

def crear_usuario(nombre, email, password, rol="Socio"):
    usuario_existente = Socio.query.filter_by(nombre=nombre).first()
    if (usuario_existente):
        return "El usuario ya existe"
    
    nuevo_usuario = Socio(nombre=nombre, email=email, rol=rol)
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()
    return True

def autenticar_usuario(nombre, password):
    usuario = Socio.query.filter_by(nombre=nombre).first()

    if (usuario and usuario.check_password(password)):
        return usuario
    return None

def listar_socios():
    return Socio.query.all()

def editar_socio(socio_id, nombre=None, email=None, password=None):
    socio = Socio.query.get(socio_id)
    if not socio:
        return None
    
    if nombre is not None:
        socio.nombre = nombre
    if email is not None:
        socio.email = email
    if password is not None:
        socio.password = password
    db.session.commit()
    return socio