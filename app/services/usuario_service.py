from app import db
from app.models.usuario import Usuario 

def crear_usuario(nombre, password):
    usuario_existente = Usuario.query.filter_by(nombre=nombre).first()
    
    if usuario_existente:
        return usuario_existente
    
    nuevo_usuario = Usuario(nombre=nombre)
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

def autenticar_usuario(nombre, password):
    usuario = Usuario.query.filter_by(nombre=nombre).first()

    if usuario and usuario.check_password(password):
        return usuario
    
    return None