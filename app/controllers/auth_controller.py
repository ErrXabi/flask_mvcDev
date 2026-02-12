from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from app.services.usuario_service import autenticar_usuario

auth_bp = Blueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios"
)

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