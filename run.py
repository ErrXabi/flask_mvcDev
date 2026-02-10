from app import create_app
from app.services.socio_service import crear_usuario

app = create_app()

with app.app_context():
    crear_usuario(
        nombre="Admin",
        password="admin",
        email="admin@admin.com",
        rol="Administrador"
    )

if __name__ == "__main__":
    app.run(debug=True)