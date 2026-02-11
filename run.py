from app import create_app
from app.services.usuario_service import crear_usuario

app = create_app()

with app.app_context():
    crear_usuario(
        nombre="admin",
        password="admin"
    )

if __name__ == "__main__":
    app.run(debug=True)