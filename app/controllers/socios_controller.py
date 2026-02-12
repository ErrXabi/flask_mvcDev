from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models.socio import Socio
from app.services.socio_service import listar_socios, editar_socio, eliminar_socio, crear_socio, listar_socios_con_prestamos, buscar_socios
from app.forms.socio_form import SocioForm
from app.forms.buscar_socio_form import BuscarSocioForm
from app.utils.decorators import login_required

socios_bp = Blueprint(
    "socios",
    __name__,
    url_prefix="/socios"
)

@socios_bp.route("/listar-socios")
def listar():
    socios = listar_socios()
    return render_template("paginas/socios/socios.html", socios=socios)

@socios_bp.route("/buscar", methods=["GET", "POST"])
def buscar():
    form = BuscarSocioForm()
    socios_encontrados = []
    
    if form.validate_on_submit():
        texto = form.busqueda.data
        socios_encontrados = buscar_socios(texto)
        
    return render_template("paginas/socios/sociosBuscar.html", form=form, socios=socios_encontrados)

@socios_bp.route("/registro", methods=["GET", "POST"])
@login_required
def registro():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")

        exito = crear_socio(nombre, email)

        if exito:
            return redirect(url_for("socios.listar"))

    return render_template("paginas/auth/registro.html")

@socios_bp.route("/editar/<int:id>", methods=["GET","POST"])
@login_required
def editar(id):
    socio = Socio.query.get(id)
    form = SocioForm(obj=socio)
    
    if request.method == "POST" and form.validate_on_submit():
        editar_socio(
            socio_id=id,
            nombre=form.nombre.data,
            email=form.email.data
        )
        return redirect(url_for('socios.listar'))

    return render_template("paginas/socios/socio_editar.html", form=form, socio=socio)

@socios_bp.route("/eliminar/<int:id>")
@login_required
def eliminar(id):
    exito, mensaje = eliminar_socio(id)
    
    if exito:
        flash(mensaje, "success")
    else:
        flash(mensaje, "danger") 
        
    return redirect(url_for("socios.listar"))

@socios_bp.route("/con-prestamos")
def con_prestamos():
    socios = listar_socios_con_prestamos()
    return render_template("paginas/socios/socios_prestamos.html", socios=socios)