from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app.services.socio_service import crear_usuario, autenticar_usuario

auth_bp = Blueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios"
)

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        password = request.form.get("contraseña")

        # corregir exito de socios service, separar socio (no tiene q iniciar sesion), es una pagina de administrador
        exito = crear_usuario(nombre, email, password)

        if exito:
            return redirect(url_for("navigation.inicio"))
        else:
            flash("Error al crear el usuario")

    return render_template("paginas/auth/registro.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        password = request.form.get("contraseña")
        
        usuario = autenticar_usuario(nombre, password)
        
        if usuario:
            session["user_id"] = usuario.id
            session["user_name"] = usuario.nombre
            return redirect(url_for("libros.listar")) 
        else:
            flash("Usuario o contraseña incorrectos", "error")

    return render_template("paginas/auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("usuarios.login"))