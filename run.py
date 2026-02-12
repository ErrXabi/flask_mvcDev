from app import create_app
from app.models.socio import Socio
from app.services.usuario_service import crear_usuario
from app.services.socio_service import crear_socio
from app.services.libros_service import crear_libro

app = create_app()

with app.app_context():
    if Socio.query.count() == 0:
        crear_usuario(
            nombre="admin",
            password="admin"
        )
        crear_socio(
            nombre="Juan García",
            email="juangarcia@gmail.com"
        )

        crear_socio(
            nombre="María López",
            email="marialopez@gmail.com"
        )

        crear_socio(
            nombre="Carlos Pérez",
            email="carlosperez@gmail.com"
        )

        crear_libro(
            titulo="Don Quijote de la Mancha",
            autor="Miguel de Cervantes",
            resumen="Las aventuras de un hidalgo que enloquece leyendo libros de caballería.",
            año="1605",
            categoria="Novela"
        )

        crear_libro(
            titulo="Cien años de soledad",
            autor="Gabriel García Márquez",
            resumen="La historia de la familia Buendía a lo largo de varias generaciones.",
            año="1967",
            categoria="Realismo mágico"
        )

        crear_libro(
            titulo="1984",
            autor="George Orwell",
            resumen="Una sociedad distópica vigilada por el Gran Hermano.",
            año="1949",
            categoria="Ciencia ficción"
        )

if __name__ == "__main__":
    app.run(debug=True)