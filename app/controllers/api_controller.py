from flask import Blueprint, jsonify, request
from app.services.libros_service import listar_libros, listar_libros_disponibles, buscar_libro
from app.services.socio_service import listar_socios_con_prestamos

api_bp = Blueprint(
    "api",
    __name__,       
    url_prefix="/api"
)

@api_bp.route("/libros", methods=["GET"])
def listar():
    libros = listar_libros()
    return jsonify([l.to_dict() for l in libros])

@api_bp.route("/libros/disponibles", methods=["GET"])
def libros_disponibles():
    libros = listar_libros_disponibles()
    return jsonify([l.to_dict() for l in libros])

@api_bp.route("/libros/buscar/<string:titulo>", methods=["GET"])
def buscar_por_titulo(titulo):
    libros = buscar_libro(titulo)
    return jsonify([l.to_dict() for l in libros])

@api_bp.route("/libros/socios/prestamos", methods=["GET"])
def socios_con_prestamos():
    socios = listar_socios_con_prestamos()
    return jsonify([s.to_dict() for s in socios])