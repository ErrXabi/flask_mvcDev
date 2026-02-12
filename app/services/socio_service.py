from app import db
from app.models.socio import Socio
from app.models.libro import Libro
from sqlalchemy import or_

def listar_socios():
    return Socio.query.all()

def listar_socios_con_prestamos():
    return Socio.query.join(Libro).filter(Libro.id_socio_prestado != None).distinct().all()

def crear_socio(nombre, email):
    socio_existente = Socio.query.filter_by(nombre=nombre).first()
    
    if socio_existente:
        return False
    
    nuevo_socio = Socio(nombre=nombre, email=email)

    db.session.add(nuevo_socio)
    db.session.commit()
    return True

def editar_socio(socio_id, nombre=None, email=None):
    socio = Socio.query.get(socio_id)
    if not socio:
        return None
    
    if nombre:
        socio.nombre = nombre
    if email:
        socio.email = email
        
    db.session.commit()
    return socio

def eliminar_socio(socio_id):
    socio = Socio.query.get(socio_id)
    
    if not socio:
        return False, "El socio no existe"
    
    if socio.libros_prestados:
        return False, "No se puede eliminar: El socio tiene libros pendientes de devolución."

    db.session.delete(socio)
    db.session.commit()
    return True, "Socio eliminado correctamente"

def buscar_socios(texto):
    if not texto:
        return []
    
    return Socio.query.filter(
        or_(
            Socio.nombre.ilike(f"%{texto}%"),
            Socio.email.ilike(f"%{texto}%")
        )
    ).all()