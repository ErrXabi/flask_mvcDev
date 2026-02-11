from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models.socio import Socio
from app.services.socio_service import listar_socios, editar_socio, eliminar_socio, crear_socio
from app.forms.socio_form import SocioForm

socios_bp = Blueprint(
    "socios",
    __name__,
    url_prefix="/socios"
)

@socios_bp.route("/listar-socios")
def listar():
    socios = listar_socios()
    return render_template("paginas/socios/socios.html", socios=socios)

@socios_bp.route("/editar/<int:id>", methods=["GET","POST"])
def editar(id):
    socio = Socio.query.get_or_404(id)
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
def eliminar(id):
    exito, mensaje = eliminar_socio(id)
    
    if exito:
        flash(mensaje, "success")
    else:
        flash(mensaje, "danger") 
        
    return redirect(url_for("socios.listar"))