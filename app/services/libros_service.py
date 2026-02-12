from sqlalchemy import func
from app import db
from app.models.libro import Libro

def listar_libros():
    return Libro.query.all()
    #return Libro.query.order_by(func.lower(Libro.titulo)).all()

def listar_libros_disponibles():
    return Libro.query.filter(Libro.id_socio_prestado == None).all()

def buscar_libro(texto):
    return Libro.query.filter(Libro.titulo.ilike(f"%{texto}%")).all()

def obtener_libro(id):
    return Libro.query.get(id)


def crear_libro(titulo, autor, resumen, año, categoria):
    libro = Libro(titulo=titulo, autor=autor, resumen=resumen, año=año, categoria=categoria)
    db.session.add(libro)
    db.session.commit()
    return libro

def editar_libro(libro_id, titulo=None, autor=None, resumen=None, año=None, categoria=None):
    libro = Libro.query.get(libro_id)
    if not libro:
        return None

    if titulo is not None:
        libro.titulo = titulo
    if autor is not None:
        libro.autor = autor
    if resumen is not None:
        libro.resumen = resumen
    if año is not None:
        libro.año = año
    if categoria is not None:
        libro.categoria = categoria

    db.session.commit()
    return libro

def eliminar_libro(libro_id):
    libro = Libro.query.get(libro_id)
    if not libro:
        return None
    
    if libro.id_socio_prestado is not None:
        return False
    
    db.session.delete(libro)
    db.session.commit()
    return True

def prestar_libro(libro_id, socio_id):
    libro = Libro.query.get(libro_id)

    if not libro:
        return False, "El libro no existe"
    
    if libro.id_socio_prestado is not None:
        return False, "El libro ya está prestado a otro socio"
    
    libro.id_socio_prestado = socio_id
    db.session.commit()
    return True, "Libro prestado correctamente"

def devolver_libro(libro_id):
    libro = Libro.query.get(libro_id)

    if not libro:
        return False, "El libro no existe"

    libro.id_socio_prestado = None
    db.session.commit()
    return True, "Libro devuelto correctamente"

def listar_libros_prestados():
    return Libro.query.filter(Libro.id_socio_prestado != None).all()