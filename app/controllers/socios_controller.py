from flask import Blueprint,  request, render_template, redirect, url_for
from app.models.socio import Socio
from app.services.socio_service import listar_socios, editar_socio
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

@socios_bp.route("/<int:id>", methods=["GET","POST"])
def detalle(id):
    socio = Socio.query.get_or_404(id)
    form = SocioForm(obj=socio)  # ← precarga datos
    if request.method == "POST":
        if form.validate_on_submit():
            socio.nombre = form.nombre.data
            socio.email = form.email.data

            editar_socio(
                socio_id=id,
                nombre=socio.nombre,
                email=socio.email,
                password=socio.password
            )

    return render_template("paginas/socios/socio_editar.html", form=form, socio=socio)